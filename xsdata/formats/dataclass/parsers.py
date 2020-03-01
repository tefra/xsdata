import io
import json
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

from xsdata.formats.dataclass.mixins import ClassMeta
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.mixins import AbstractParser
from xsdata.formats.mixins import AbstractXmlParser
from xsdata.models.enums import EventType
from xsdata.utils import text

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
            return self.parse_context(value, var.clazz)
        elif var.is_any_attribute:
            return dict(value)
        elif var.is_any_element:
            return (
                value
                if isinstance(value, str)
                else self.parse_context(value, AnyElement)
            )
        else:
            return self.parse_value(var.types, value, var.default)

    @staticmethod
    def get_value(data: Dict, field: ClassVar):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.qname.localname in data:
            value = data[field.qname.localname]
        elif field.name in data:
            value = data[field.name]
        else:
            return None

        if field.is_list and not isinstance(value, list):
            value = [value]

        return value


@dataclass(frozen=True)
class QueueItem:
    index: int
    position: int
    default: Any = field(default=None)
    qname: Optional[str] = field(default=None)
    meta: Optional[ClassMeta] = field(default=None)
    types: List[Type] = field(default_factory=list)


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
        self.queue = [QueueItem(index=0, position=0, meta=meta, default=None)]

        return super(XmlParser, self).parse_context(context, clazz)

    def start_node(self, element: Element):
        """
        Queue the necessary metadata to bind the given element when it's fully
        parsed.

        Checks for the last item in queue:
        - Is none or has none meta                        -> inside a wildcard
        - Element tag exists in known variables           -> dataclass or primitive
        - Element tag equals meta qualified name          -> root element
        - Element tag unknown but queue supports wildcard -> start a wildcard

        :raises Value: When the parser doesn't know how to handle the given element.
        """
        qname = element.tag
        item = self.queue[-1]

        if not item or not item.meta:  # Assuming inside a wildcard
            return self.queue.append(None)
        elif qname in item.meta.vars:  # A dataclass or a primitive field
            queue_item = self.create_queue_item(item.meta.vars[qname], item.meta.qname)
            self.queue.append(queue_item)
        elif item.meta.qname == qname:  # root
            pass
        elif item.meta.any_element:  # Wildcard jackpot
            queue_item = self.create_wildcard_queue_item(item.meta.any_element.qname)
            self.queue.append(queue_item)
        else:  # Unknown :)
            raise ValueError(
                f"{item.meta.qname} does not support mixed content: {qname}"
            )

        self.index += 1
        self.emit_event(EventType.START, qname, item=item, element=element)

    def create_queue_item(self, var: ClassVar, parent_qname: QName):
        meta = None
        types = var.types
        if var.is_dataclass:
            meta = self.class_meta(var.clazz, parent_qname)
            types = []

        return QueueItem(
            meta=meta,
            index=self.index,
            types=types,
            position=len(self.objects),
            default=var.default,
        )

    def create_wildcard_queue_item(self, parent_qname: QName):
        return QueueItem(
            index=self.index, position=len(self.objects), qname=parent_qname,
        )

    def end_node(self, element: Element) -> Optional[T]:
        """
        Build an objects tree for the given element.

        Construct a dataclass instance with the attributes of the given element and any
        pending objects that belong to the model. Otherwise parse as a primitive type
        the element's text content.

        :returns object: A dataclass object or a python primitive value.
        """
        item = self.queue.pop()
        if not item:  # Assuming inside a wildcard
            return None

        qname = QName(element.tag)
        if item.meta:  # dataclass
            attr_params = self.bind_element_attrs(item.meta, element)
            text_params = self.bind_element_text(item.meta, element)
            children = self.fetch_class_children(item, element)
            obj = item.meta.clazz(**attr_params, **text_params, **children)
        elif item.types:  # primitive
            obj = self.parse_value(item.types, element.text, item.default)
        elif item.qname:  # wildcard
            obj = self.parse_any_element(element)
            obj.children = self.fetch_any_children(item)
            qname = item.qname
        else:  # unknown :)
            raise ValueError(f"Failed to create object from {element.tag}")

        self.objects.append((qname, obj))
        self.emit_event(EventType.END, element.tag, obj=obj, element=element)

        return obj

    def emit_event(self, event: str, name: str, **kwargs):
        """Call if exist the parser's hook for the given element and event."""
        local_name = text.snake_case(QName(name).localname)
        method_name = f"{event}_{local_name}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)

    def fetch_class_children(self, item: QueueItem, element: Element) -> Dict[str, Any]:
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

            if not arg.init:
                continue
            if value is None:
                value = ""

            if arg.is_list:
                params[arg.name].append(value)
            else:
                params[arg.name] = value

        if item.meta.mixed and item.meta.any_element:
            var = item.meta.any_element
            txt, tail = self.element_text_and_tail(element)
            if text:
                params[var.name].insert(0, txt)
            if tail:
                params[var.name].append(tail)

        return params

    def fetch_any_children(self, item: QueueItem) -> List[object]:
        children = []
        while len(self.objects) > item.position:
            _, value = self.objects.pop(item.position)
            children.append(value)
        return children

    def bind_element_attrs(self, metadata: ClassMeta, element: Element) -> Dict:
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        params = dict()
        any_attr = metadata.any_attribute
        for qname, value in element.attrib.items():
            if qname in metadata.vars:
                var = metadata.vars[qname]
                if var.init:
                    params[var.name] = self.parse_value(var.types, value, var.default)
            elif any_attr:
                if any_attr.name not in params:
                    params[any_attr.name] = dict()
                params[any_attr.name][qname] = value

        return params

    def bind_element_text(self, metadata: ClassMeta, element: Element):
        params = dict()
        var = metadata.any_text
        if var and element.text is not None and var.init:
            params[var.name] = self.parse_value(var.types, element.text, var.default)

        return params

    @classmethod
    def parse_any_element(cls, element: Element) -> Optional[AnyElement]:
        if not isinstance(element.tag, str):
            return None
        else:
            txt, tail = cls.element_text_and_tail(element)
            return AnyElement(
                qname=element.tag,
                text=txt or None,
                tail=tail or None,
                attributes={k: v for k, v in element.attrib.items()},
            )

    @classmethod
    def element_text_and_tail(cls, element: Element) -> Tuple:
        return (
            element.text.strip() if element.text else None,
            element.tail.strip() if element.tail else None,
        )
