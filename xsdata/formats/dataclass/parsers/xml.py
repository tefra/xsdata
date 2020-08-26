from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Type

from lxml.etree import Element
from lxml.etree import iterparse
from lxml.etree import iterwalk
from lxml.etree import parse

from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.formats.dataclass.parsers.nodes import XmlNodes
from xsdata.models.enums import EventType
from xsdata.utils import text


@dataclass
class XmlParser(NodeParser, AbstractParser):
    """Xml parsing and binding for dataclasses."""

    event_names: Dict = field(init=False, default_factory=dict)

    def parse(self, source: Any, clazz: Type[T]) -> T:
        """Parse the XML input stream and return the resulting object tree."""

        events = EventType.START, EventType.END, EventType.START_NS
        if self.config.process_xinclude:
            tree = parse(source, base_url=self.config.base_url)  # nosec
            tree.xinclude()
            ctx = iterwalk(tree, events=events)
        else:
            ctx = iterparse(source, events=events, recover=True, remove_comments=True)

        return self.parse_context(ctx, clazz)

    def start(
        self, element: Element, queue: XmlNodes, objects: List[Parsed], clazz: Type[T]
    ):
        """Queue the next xml node for parsing based on the given element
        qualified name."""
        super().start(element, queue, objects, clazz)
        self.emit_event(EventType.START, element.tag, element=element)

    def end(self, element: Element, queue: XmlNodes, objects: List[Parsed]) -> Any:
        """
        Use the last xml node to parse the given element and bind any child
        objects.

        :return: Any: A dataclass instance or a python primitive value or None
        """

        obj = super().end(element, queue, objects)
        if obj:
            self.emit_event(EventType.END, element.tag, obj=obj, element=element)
            element.clear()

        return obj

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """Call if exist the parser's hook for the given element and event."""

        if name not in self.event_names:
            self.event_names[name] = text.snake_case(text.split_qname(name)[1])

        method_name = f"{event}_{self.event_names[name]}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)
