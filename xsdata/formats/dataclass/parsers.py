import io
import json
import re
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

from xsdata.formats.dataclass.mixins import Field
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.mixins import NodeType
from xsdata.formats.dataclass.mixins import QueueItem
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

        for arg in self.fields(clazz):
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
    def get_value(data: Dict, field: Field):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.local_name in data:
            value = data[field.local_name]
            if field.is_list and not isinstance(value, list):
                value = [value]
        elif callable(field.default):
            value = field.default()
        else:
            value = field.default

        return value


@dataclass
class XmlParser(AbstractXmlParser, ModelInspect):
    index: int = field(default_factory=int)
    queue: List[Optional[QueueItem]] = field(init=False, default_factory=list)
    namespace: Optional[str] = field(init=False, default=None)
    elements: List[Tuple[QName, Any]] = field(init=False, default_factory=list)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """Forward the xml stream iterator to move after the root element."""
        meta = self.class_meta(clazz)

        self.queue = []
        self.elements = []
        self.namespace = meta.namespace
        qname = QName(meta.namespace, meta.name)

        self.queue.append(
            QueueItem(
                qname=qname,
                clazz=clazz,
                fields={
                    qname: Field(
                        name=clazz.__name__,
                        local_name=meta.name,
                        node_type=NodeType.ROOT,
                        type=clazz,
                        namespace=meta.namespace,
                        is_dataclass=True,
                    )
                },
            )
        )

        return super(XmlParser, self).parse_context(context, clazz)

    def start_node(self, element: Element):
        """
        Append to queue the necessary, to construct, metadata for the given
        element.

        The metadata includes:
        - the qualified name of the element
        - the python dataclass type
        - the fields objects list of the class
        - the next elements index for the object that will be created
        """
        qname = element.tag
        item = self.queue[-1]

        if not item:
            return self.queue.append(None)
        if qname not in item.fields:
            if item.meta and item.meta.mixed:
                return self.queue.append(None)
            raise ValueError(f"{item.qname} does not support mixed content: {qname}")

        arg = item.fields[qname]
        item = QueueItem(
            qname=qname,
            clazz=arg.type,
            meta=self.class_meta(arg.type) if arg.is_dataclass else None,
            fields=self.class_ns_fields(arg.type) if arg.is_dataclass else dict(),
            index=self.index,
            child_index=len(self.elements),
        )
        self.queue.append(item)
        self.index += 1
        self.emit_event(EventType.START, qname, item=item, element=element)

    def end_node(self, element: Element) -> Optional[Type]:
        """Build an object for the given element by the last queue metadata."""
        item = self.queue.pop()
        obj = None
        if item is not None:
            obj = self.build_object(item, element)
            self.elements.append((item.qname, obj))
            self.emit_event(EventType.END, element.tag, obj=obj, element=element)

        return obj

    def emit_event(self, event: str, name: str, **kwargs):
        local_name = QName(name).localname
        method_name = f"{event}_{local_name}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)

    def build_object(self, item: QueueItem, element: Element) -> Any:
        """
        Objectify current element by the item clazz type.

        If the clazz is a dataclass build the objects tree and parse
        attributes from the element. Otherwise parse the elements text
        value
        """
        if item.fields and item.clazz:
            attributes = self.parse_element_attributes(item, element)
            children = self.fetch_class_children(item)
            obj = item.clazz(**children, **attributes)
        elif item.clazz:
            obj = self.parse_value(item.clazz, element.text)
        else:
            raise ValueError(f"Failed to create object from {element.tag}")

        return obj

    def fetch_class_children(self, item: QueueItem) -> Dict[str, Any]:
        """
        Return a dictionary of qualified object names and objects for the given
        queue item.

        The object can be a primitive, another dataclass, or a list of
        either primitive values and dataclasses.
        """
        params: Dict[str, Any] = dict()
        while len(self.elements) > item.child_index:
            qname, value = self.elements.pop(item.child_index)
            arg = item.fields[qname]

            if arg.is_list:
                if arg.name not in params:
                    params[arg.name] = []

                params[arg.name].append(value)
            else:
                params[arg.name] = value
        return params

    def parse_element_attributes(
        self, item: QueueItem, element: Element
    ) -> Dict[str, Any]:
        """Parse the given element's attributes and text value if any and
        return a dictionary of field names and values."""

        params: Dict[str, Any] = dict()
        for qname, arg in item.fields.items():
            value = None
            if qname in element.attrib:
                value = element.attrib[qname]
            elif arg.is_text:
                if item.meta and item.meta.mixed:
                    value = self.parse_mixed_content(element)
                elif not len(element):
                    value = element.text

            if value is not None:
                params[arg.name] = self.parse_value(arg.type, value)

        return params

    def class_ns_fields(self, clazz: Type) -> Dict[str, Field]:
        """Returns the given class fields indexed by their qualified names."""

        res: Dict = dict()
        for arg in self.fields(clazz):
            if arg.is_attribute and arg.namespace is None:
                res[arg.local_name] = arg
            elif arg.namespace == "":
                res[arg.local_name] = arg
            else:
                qname = QName(arg.namespace or self.namespace, arg.local_name)
                res[qname.text] = arg
        return res

    @classmethod
    def parse_mixed_content(cls, element: Element):
        """Parse element mixed content by preserving the raw string."""

        xml = tostring(element, method="c14n", pretty_print=True).decode()
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
