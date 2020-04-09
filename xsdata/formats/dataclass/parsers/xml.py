import io
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import QName

from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.parsers.json import T
from xsdata.formats.dataclass.parsers.nodes import BaseNode
from xsdata.formats.dataclass.parsers.nodes import ElementNode
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.models.enums import EventType
from xsdata.utils import text


@dataclass
class XmlParser(AbstractParser):
    index: int = field(default_factory=int)
    queue: List[BaseNode] = field(init=False, default_factory=list)
    namespaces: Namespaces = field(init=False, default_factory=Namespaces)
    objects: List[Tuple[QName, Any]] = field(init=False, default_factory=list)
    context: ModelContext = field(default_factory=ModelContext)

    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the XML input stream and return the resulting object tree."""
        ctx = iterparse(
            source=source,
            events=(EventType.START, EventType.END),
            recover=True,
            remove_comments=True,
        )
        return self.parse_context(ctx, clazz)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        :raises ValueError: When the requested type doesn't match the result object
        """
        obj = None
        meta = self.context.class_meta(clazz)
        self.objects = []
        self.index = 0
        self.namespaces.clear()
        self.queue = [RootNode(index=0, position=0, meta=meta, default=None)]

        for event, element in context:
            if event == EventType.START:
                self.queue_node(element)
            elif event == EventType.END:
                obj = self.dequeue_node(element)
                if obj is not None:
                    element.clear()

        if not obj or not isinstance(obj, clazz):
            raise ParserError(f"Failed to create target class `{clazz.__name__}`")

        return obj

    def queue_node(self, element: Element):
        """
        Queue the next xml node for parsing based on the given element
        qualified name.

        :raises ParserError: When the parser doesn't know how to proceed.
        """
        qname = QName(element.tag)
        item = self.queue[-1]
        position = len(self.objects)

        queue_item = item.next_node(qname, self.index, position, self.context)

        if queue_item is None:
            parent = item.meta.qname if isinstance(item, ElementNode) else "unknown"
            raise ParserError(f"{parent} does not support mixed content: {qname}")

        self.index += 1
        self.queue.append(queue_item)
        self.emit_event(EventType.START, element.tag, item=item, element=element)

    def dequeue_node(self, element: Element) -> Optional[T]:
        """
        Use the last xml node to parse the given element and bind any child
        objects.

        :returns object: A dataclass object or a python primitive value.
        """
        item = self.queue.pop()
        qname, obj = item.parse_element(element, self.objects)

        if qname:
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
