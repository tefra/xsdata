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
from xsdata.formats.dataclass.models import AnyElement
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

        for var in self.class_meta(clazz).vars.values():
            value = self.get_value(data, var)

            if value is None:
                continue
            elif var.is_list:
                params[var.name] = [self.bind_value(var, val) for val in value]
            else:
                params[var.name] = self.bind_value(var, value)

        try:
            return clazz(**params)  # type: ignore
        except Exception:
            raise TypeError("Parsing failed")

    def bind_value(self, var: ClassVar, value) -> Any:
        """
        Bind value according to the class var.

        The return value can be:
        - a dataclass instance
        - a dictionary with unknown attributes
        - a list of unknown elements
        - an enumeration
        - a primitive value
        """
        if var.is_dataclass:
            return self.parse_context(value, var.type)
        elif var.is_any_attribute:
            return dict(value)
        elif var.is_any_element:
            return (
                value
                if isinstance(value, str)
                else self.parse_context(value, AnyElement)
            )
        else:
            return self.parse_value(var.type, value)

    @staticmethod
    def get_value(data: Dict, field: ClassVar):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.qname.localname in data:
            value = data[field.qname.localname]
        elif field.name in data:
            value = data[field.name]
        elif callable(field.default):
            value = field.default()
        else:
            value = field.default

        if field.is_list and not isinstance(value, list):
            value = [value]

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
            attr_params = self.bind_element_attrs(item.meta, element)
            text_params = self.bind_element_text(item.meta, element)
            any_params = self.bind_element_any(item.meta, element)
            children = self.fetch_class_children(item)

            obj = item.type(**attr_params, **text_params, **any_params, **children)
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

    def bind_element_attrs(self, metadata: ClassMeta, element: Element) -> Dict:
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        params = dict()
        any_attr = metadata.any_attribute
        for qname, value in element.attrib.items():
            if qname in metadata.vars:
                var = metadata.vars[qname]
                params[var.name] = self.parse_value(var.type, value)
            elif any_attr:
                if any_attr.name not in params:
                    params[any_attr.name] = dict()
                params[any_attr.name][qname] = value

        return params

    def bind_element_text(self, metadata: ClassMeta, element: Element):
        params = dict()
        text_var = metadata.any_text
        if text_var and element.text is not None:
            params[text_var.name] = self.parse_value(text_var.type, element.text)

        return params

    def bind_element_any(self, metadata: ClassMeta, element: Element):
        params = dict()
        any_var = metadata.any_element
        if any_var:
            text = element.text.strip() if element.text else None
            tail = element.tail.strip() if element.tail else None
            value: List[object] = list(
                filter(None, map(self.parse_any_element, element))
            )

            if text:
                value.insert(0, text)
            if tail:
                value.append(tail)
            if value:
                params[any_var.name] = value

        return params

    @classmethod
    def parse_any_element(cls, element: Element) -> Optional[AnyElement]:
        text = element.text.strip() if element.text else None
        tail = element.tail.strip() if element.tail else None

        if isinstance(element.tag, str):
            return AnyElement(
                qname=element.tag,
                text=text or None,
                tail=tail or None,
                children=list(filter(None, map(cls.parse_any_element, element))),
                attributes={k: v for k, v in element.attrib.items()},
            )
        return None

    @classmethod
    def parse_mixed_content(cls, element: Element):
        """Parse element mixed content by preserving the raw string."""

        xml = tostring(element, pretty_print=True).decode()
        start_root = xml.find(">")
        end_root = xml.rfind("<")

        return re.sub(r"\s+", " ", xml[start_root + 1 : end_root]).strip()
