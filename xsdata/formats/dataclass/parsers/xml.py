import io
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import QName

from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.json import T
from xsdata.formats.dataclass.parsers.nodes import RootNode
from xsdata.formats.dataclass.parsers.nodes import XmlNode
from xsdata.models.enums import EventType
from xsdata.utils import text

ParsedObjects = List[Tuple[QName, Any]]
XmlNodes = List[XmlNode]


@dataclass
class XmlParser(AbstractParser):
    """
    :param namespaces:
    :param context:
    :param event_names:
    :param config:
    """

    namespaces: Namespaces = field(init=False, default_factory=Namespaces)
    context: XmlContext = field(default_factory=XmlContext)
    event_names: Dict = field(default_factory=dict)
    config: ParserConfig = field(default_factory=ParserConfig)

    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the XML input stream and return the resulting object tree."""
        ctx = iterparse(
            source=source,
            events=(EventType.START, EventType.END, EventType.START_NS),
            recover=True,
            remove_comments=True,
        )
        return self.parse_context(ctx, clazz)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        :raises ParserError: When the requested type doesn't match the result object
        """
        obj = None
        meta = self.context.build(clazz)
        self.namespaces.clear()
        objects: ParsedObjects = []
        queue: XmlNodes = [RootNode(position=0, meta=meta, config=self.config)]

        for event, element in context:
            if event == EventType.START_NS:
                self.add_namespace(element)
            if event == EventType.START:
                self.queue(element, queue, objects)
            elif event == EventType.END:
                obj = self.dequeue(element, queue, objects)

        if not obj:
            raise ParserError(f"Failed to create target class `{clazz.__name__}`")

        return obj

    def add_namespace(self, namespace: Tuple):
        """Add the given namespace in the registry."""
        prefix, uri = namespace
        self.namespaces.add(uri, prefix)

    def queue(self, element: Element, queue: XmlNodes, objects: ParsedObjects):
        """Queue the next xml node for parsing based on the given element
        qualified name."""
        item = queue[-1]
        position = len(objects)

        queue_item = item.next_node(element, position, self.context)

        queue.append(queue_item)
        self.emit_event(EventType.START, element.tag, item=item, element=element)

    def dequeue(self, element: Element, queue: XmlNodes, objects: ParsedObjects) -> Any:
        """
        Use the last xml node to parse the given element and bind any child
        objects.

        :return: Any: A dataclass instance or a python primitive value or None
        """
        item = queue.pop()
        qname, obj = item.parse_element(element, objects)

        if qname:
            objects.append((qname, obj))
            self.emit_event(EventType.END, element.tag, obj=obj, element=element)

        element.clear()

        return obj

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """Call if exist the parser's hook for the given element and event."""

        if name not in self.event_names:
            self.event_names[name] = text.snake_case(QName(name).localname)

        method_name = f"{event}_{self.event_names[name]}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)
