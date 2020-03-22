from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import QName

from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractXmlParser
from xsdata.formats.dataclass.mixins import ClassMeta
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.dataclass.models import AnyText
from xsdata.formats.dataclass.models import Namespaces
from xsdata.formats.dataclass.parsers.json import T
from xsdata.logger import logger
from xsdata.models.enums import EventType
from xsdata.utils import text


@dataclass(frozen=True)
class QueueItem:
    index: int
    position: int


@dataclass(frozen=True)
class ClassQueueItem(QueueItem):
    meta: ClassMeta
    default: Any = field(default=None)


@dataclass(frozen=True)
class PrimitiveQueueItem(QueueItem):
    types: List[Type]
    default: Any = field(default=None)


@dataclass(frozen=True)
class WildcardQueueItem(QueueItem):
    qname: str


@dataclass(frozen=True)
class SkipQueueItem(QueueItem):
    pass


@dataclass
class XmlParser(AbstractXmlParser, ModelInspect):
    index: int = field(default_factory=int)
    queue: List[Optional[QueueItem]] = field(init=False, default_factory=list)
    namespaces: Namespaces = field(init=False, default_factory=Namespaces)
    objects: List[Tuple[QName, Any]] = field(init=False, default_factory=list)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        Initialize queue with clazz metadata and reset pending objects list.

        :raises ValueError: When the requested type doesn't match the result object
        """
        meta = self.class_meta(clazz)

        self.objects = []
        self.index = 0
        self.namespaces.clear()
        self.queue = [ClassQueueItem(index=0, position=0, meta=meta)]

        return super(XmlParser, self).parse_context(context, clazz)

    def queue_node(self, element: Element):
        """
        Queue the necessary metadata to bind the given element when it's fully
        parsed.

        Checks for the last item in queue:
        - Is none or has none meta                        -> inside a wildcard
        - Element tag exists in known variables           -> dataclass or primitive
        - Element tag equals meta qualified name          -> root element
        - Element tag unknown but queue supports wildcard -> start a wildcard

        :raises ParserError: When the parser cant compute next queue item.
        """
        qname = QName(element.tag)
        queue_item = None
        item = self.queue[-1]

        if isinstance(item, (SkipQueueItem, PrimitiveQueueItem)):
            queue_item = self.create_skip_queue_item()
        elif isinstance(item, WildcardQueueItem):
            queue_item = self.create_wildcard_queue_item(item.qname)
        elif isinstance(item, ClassQueueItem):

            if item.meta.qname == qname and self.index == 0:
                queue_item = self.queue.pop()
            else:
                var = item.meta.get_var(qname)
                if var and var.is_dataclass:
                    queue_item = self.create_class_queue_item(var, item.meta.qname)
                elif var and var.is_any_element:
                    queue_item = self.create_wildcard_queue_item(var.qname)
                elif var:
                    queue_item = self.create_primitive_queue_item(var)

        if queue_item is None:
            parent = item.meta.qname if isinstance(item, ClassQueueItem) else "unknown"
            raise ParserError(f"{parent} does not support mixed content: {qname}")

        self.index += 1
        self.queue.append(queue_item)
        self.emit_event(EventType.START, element.tag, item=item, element=element)

    def create_skip_queue_item(self):
        return SkipQueueItem(index=self.index, position=len(self.objects))

    def create_class_queue_item(self, var: ClassVar, parent_qname: QName):
        return ClassQueueItem(
            index=self.index,
            position=len(self.objects),
            meta=self.class_meta(var.clazz, parent_qname.namespace),
            default=var.default,
        )

    def create_primitive_queue_item(self, var: ClassVar):
        return PrimitiveQueueItem(
            index=self.index,
            position=len(self.objects),
            types=var.types,
            default=var.default,
        )

    def create_wildcard_queue_item(self, parent_qname: QName):
        return WildcardQueueItem(
            index=self.index, position=len(self.objects), qname=parent_qname,
        )

    def dequeue_node(self, element: Element) -> Optional[T]:
        """
        Build an objects tree for the given element.

        Construct a dataclass instance with the attributes of the given element and any
        pending objects that belong to the model. Otherwise parse as a primitive type
        the element's text content.

        :returns object: A dataclass object or a python primitive value.
        """
        item = self.queue.pop()
        qname = obj = None

        if isinstance(item, SkipQueueItem):
            return None
        elif isinstance(item, PrimitiveQueueItem):
            qname = QName(element.tag)
            obj = self.parse_value(item.types, element.text, item.default)
        elif isinstance(item, WildcardQueueItem):
            obj = self.parse_any_element(element)
            if not obj:
                return None
            obj.children = self.fetch_any_children(item)
            qname = item.qname
        elif isinstance(item, ClassQueueItem):
            attr_params = self.bind_element_attrs(item.meta, element)
            text_params = self.bind_element_text(item.meta, element)
            child_params = self.fetch_class_children(item, element)
            qname = QName(element.tag)
            obj = item.meta.clazz(**attr_params, **text_params, **child_params)
        else:  # unknown :)
            raise ParserError(f"Failed to create object from {element.tag}")

        self.objects.append((qname, obj))
        self.emit_event(EventType.END, element.tag, obj=obj, element=element)
        self.namespaces.add_all(element.nsmap)
        return obj

    def emit_event(self, event: str, name: str, **kwargs):
        """Call if exist the parser's hook for the given element and event."""
        local_name = text.snake_case(QName(name).localname)
        method_name = f"{event}_{local_name}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)

    def fetch_class_children(self, item: ClassQueueItem, element: Element) -> Dict:
        """Return a dictionary of qualified object names and their values for
        the given queue item."""

        params: Dict[str, Any] = defaultdict(list)
        while len(self.objects) > item.position:
            qname, value = self.objects.pop(item.position)
            arg = item.meta.vars[qname]

            if not arg.init:
                continue
            if value is None:
                value = ""
            if arg.name in params and not arg.is_list:
                wild_var = item.meta.get_wild_var(qname)
                if wild_var is None:
                    logger.warning("Unassigned parsed object %s", qname)
                    continue
                if is_dataclass(value):
                    value.qname = qname
                else:
                    value = AnyElement(qname=qname, text=value)
                arg = wild_var

            if arg.is_list:
                params[arg.name].append(value)
            elif arg.name not in params:
                params[arg.name] = value

        if item.meta.mixed and item.meta.any_element:
            var = item.meta.any_element
            txt, tail = self.element_text_and_tail(element)
            if var.is_list:
                if text:
                    params[var.name].insert(0, txt)
                if tail:
                    params[var.name].append(tail)
            elif var.name in params:
                if text:
                    params[var.name].text = txt
                if tail:
                    params[var.name].tail = tail

        return params

    def fetch_any_children(self, item: WildcardQueueItem) -> List[object]:
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
        if len(element):
            return dict()

        var = metadata.any_text
        if var and element.text is not None and var.init:
            return {var.name: self.parse_value(var.types, element.text, var.default)}
        var = metadata.any_element
        if var and element.text is not None and not var.is_list:
            return {var.name: self.parse_any_text(element)}
        return {}

    @classmethod
    def parse_any_element(cls, element: Element) -> Optional[AnyElement]:
        if not isinstance(element.tag, str):
            return None
        else:
            txt, tail = cls.element_text_and_tail(element)
            return AnyElement(
                qname=element.tag,
                text=txt,
                tail=tail,
                attributes=cls.parse_any_attributes(element),
            )

    @classmethod
    def parse_any_text(cls, element: Element) -> Optional[AnyText]:
        return AnyText(
            text=element.text or None,
            nsmap=element.nsmap,
            attributes=cls.parse_any_attributes(element),
        )

    @classmethod
    def parse_any_attributes(cls, element: Element):
        def qname(name):
            prefix, suffix = text.split(name)
            if prefix and prefix in element.nsmap:
                return QName(element.nsmap[prefix], suffix)
            return name

        return {qname(key): qname(value) for key, value in element.attrib.items()}

    @classmethod
    def element_text_and_tail(cls, element: Element) -> Tuple:
        txt = element.text.strip() if element.text else None
        tail = element.tail.strip() if element.tail else None

        return txt or None, tail or None
