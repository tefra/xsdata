from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.models.enums import EventType
from xsdata.utils.text import snake_case
from xsdata.utils.text import split_qname


@dataclass
class XmlParser(NodeParser):
    """
    Bind xml nodes to dataclasses with event hooks.

    :param handler: Xml handler.
    :param event_names: Cache for qnames to event names.
    """

    handler: Type[XmlHandler] = field(default=LxmlEventHandler)
    event_names: Dict = field(init=False, default_factory=dict)

    def start(
        self,
        queue: List[XmlNode],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
        objects: List[Parsed],
        clazz: Type[T],
    ):
        """
        Queue the next xml node for parsing.

        Emit a start event with the current element qualified name and
        attributes.
        """
        super().start(queue, qname, attrs, ns_map, objects, clazz)
        self.emit_event(EventType.START, qname, attrs=attrs)

    def end(
        self,
        queue: List[XmlNode],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: List[Parsed],
    ) -> Any:
        """
        Parse the last xml node and bind any intermediate objects.

        Emit an end event with the result object if any.

        :return: The result of the binding process.
        """
        obj = super().end(queue, qname, text, tail, objects)
        if obj:
            self.emit_event(EventType.END, qname, obj=obj)
        return obj

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """Call if exist the parser's hook for the given element and event."""
        if name not in self.event_names:
            self.event_names[name] = snake_case(split_qname(name)[1])

        method_name = f"{event}_{self.event_names[name]}"
        if hasattr(self, method_name):
            getattr(self, method_name)(**kwargs)
