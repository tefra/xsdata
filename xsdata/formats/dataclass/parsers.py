import io
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import QName
from lxml.etree import tostring

from xsdata.formats.dataclass.mixins import ClassMeta
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.mixins import AbstractParser
from xsdata.formats.mixins import AbstractXmlParser
from xsdata.models.enums import EventType

T = TypeVar("T")


@dataclass
class JsonParser(AbstractParser, ModelInspect):
    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the JSON input stream and return the resulting object tree."""
        ctx = json.load(source)
        return self.parse_context(ctx, clazz)

    def parse_context(self, data: Dict, clazz: Type[T]) -> T:
        """
        Recursively build the given model from the input dict data.

        :raise TypeError: When parsing fails for any reason
        """
        params = {}

        if isinstance(data, list) and len(data) == 1:
            data = data[0]

        for _, arg in self.class_meta(clazz).vars.items():
            value = self.get_value(data, arg)

            if value is None:
                pass
            elif arg.is_list:
                if arg.is_dataclass:
                    value = [self.parse_context(val, arg.type) for val in value]
                else:
                    value = list(map(arg.type, value))
            else:
                if arg.is_dataclass:
                    value = self.parse_context(value, arg.type)
                else:
                    value = arg.type(value)

            params[arg.name] = value

        try:
            return clazz(**params)  # type: ignore
        except Exception:
            raise TypeError("Parsing failed")

    @staticmethod
    def get_value(data: Dict, field: ClassVar):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.qname.localname in data:
            value = data[field.qname.localname]
            if field.is_list and not isinstance(value, list):
                value = [value]
        elif callable(field.default):
            value = field.default()
        else:
            value = field.default

        return value


@dataclass(frozen=True)
class QueueItem:
    type: Type
    index: int
    meta: Optional[ClassMeta] = field(default=None)
    position: int = field(default_factory=int)


@dataclass
class XmlParser(AbstractXmlParser, ModelInspect):
    index: int = field(default_factory=int)
    queue: List[Optional[QueueItem]] = field(init=False, default_factory=list)
    namespace: Optional[str] = field(init=False, default=None)
    objects: List[Tuple[QName, Any]] = field(init=False, default_factory=list)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        Initialize queue with clazz metadata and reset pending objects list.

        :raises ValueError: When the requested type doesn't match the result object
        """
        meta = self.class_meta(clazz)

        self.objects = []
        self.queue = [QueueItem(type=clazz, index=0, meta=meta)]

        return super(XmlParser, self).parse_context(context, clazz)

    def start_node(self, element: Element):
        """
        Prepare metadata queue to bind the given element to a dataclass object.

        In order:
        - If last item in queue is None assume we are inside mixed content
        - If element qname is not a var in the last item in the queue.
          - Check if the first element element is root and skip the rest.
          - Check if the last queue item supports mixed content and setup the queue to
          bypass direct data binding to a new dataclass object.
        - If element qname is a var in the last item in the queue append its class
        metadata to the queue for the upcoming data binding.

        :raises Value: When the parser doesn't know how to handle the given element.
        """
        qname = element.tag
        item = self.queue[-1]

        if not item or not item.meta:
            return self.queue.append(None)

        if item.meta and qname not in item.meta.vars:
            if item.meta.qname == qname:
                self.index += 1
                self.emit_event(EventType.START, qname, item=item, element=element)
                return None  # root
            elif item.meta.mixed:
                return self.queue.append(None)
            else:
                raise ValueError(
                    f"{item.meta.qname} does not support mixed content: {qname}"
                )

        var = item.meta.vars[qname]
        meta = self.class_meta(var.type, item.meta.qname) if var.is_dataclass else None
        queue_item = QueueItem(
            type=var.type, index=self.index, meta=meta, position=len(self.objects)
        )

        self.queue.append(queue_item)
        self.index += 1
        self.emit_event(EventType.START, qname, item=item, element=element)

    def end_node(self, element: Element) -> Optional[T]:
        """
        Build an objects tree for the given element.

        Construct a dataclass instance with the attributes of the given element and if
        any pending objects that belong to the model. Otherwise parse as a primitive
        type the element's text content.

        :returns object: A dataclass object or a python primitive value.
        :raises ValueError: When parser has no data bind strategy for the given object.
        """
        item = self.queue.pop()

        if item is None:
            return None
        elif item.meta:
            attributes = self.parse_element_attributes(item.meta, element)
            children = self.fetch_class_children(item)
            obj = item.type(**children, **attributes)
        elif item.type:
            obj = self.parse_value(item.type, element.text)
        else:
            raise ValueError(f"Failed to create object from {element.tag}")

        self.objects.append((QName(element.tag), obj))
        self.emit_event(EventType.END, element.tag, obj=obj, element=element)

        return obj

    def emit_event(self, event: str, name: str, **kwargs):
        """Call if exist the parser's hook for the given element and event."""
        local_name = QName(name).localname
        method_name = f"{event}_{local_name}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)

    def fetch_class_children(self, item: QueueItem) -> Dict[str, Any]:
        """
        Return a dictionary of qualified object names and their values for the
        given queue item.

        :raises ValueError: if queue item type is primitive.
        """
        if not item.meta:
            raise ValueError("Queue item is not a dataclass!")

        params: Dict[str, Any] = defaultdict(list)
        while len(self.objects) > item.position:
            qname, value = self.objects.pop(item.position)
            arg = item.meta.vars[qname]

            if arg.is_list:
                params[arg.name].append(value)
            else:
                params[arg.name] = value

        return params

    def parse_element_attributes(self, metadata: ClassMeta, element: Element) -> Dict:
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        var = metadata.vars
        params = {
            var[qname].name: self.parse_value(var[qname].type, value)
            for qname, value in element.attrib.items()
            if qname in var
        }

        text_var = next((var for var in metadata.vars.values() if var.is_text), None)
        if text_var and element.text is not None:
            text = self.parse_mixed_content(element) if metadata.mixed else element.text
            params[text_var.name] = self.parse_value(text_var.type, text)

        return params

    @classmethod
    def parse_mixed_content(cls, element: Element):
        """Parse element mixed content by preserving the raw string."""

        xml = tostring(element, pretty_print=True).decode()
        start_root = xml.find(">")
        end_root = xml.rfind("<")

        return re.sub(r"\s+", " ", xml[start_root + 1 : end_root]).strip()

    @classmethod
    def parse_value(cls, tp: Type, value: Any) -> Any:
        """Convert xml string values to s python primitive type."""

        if hasattr(tp, "__origin__"):
            for tp_arg in tp.__args__:
                try:
                    return cls.parse_value(tp_arg, value)
                except ValueError:
                    pass
            return value

        return value == "true" if tp is bool else tp(value)
