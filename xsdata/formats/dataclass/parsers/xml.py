from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import split_qname
from xsdata.utils.text import snake_case


@dataclass
class XmlParser(NodeParser):
    """
    Bind xml nodes to dataclasses with event hooks.

    :param handler: Xml handler type
    :param emit_cache: Cache for qnames to event names
    """

    handler: Type[XmlHandler] = field(default=LxmlEventHandler)
    emit_cache: Dict = field(init=False, default_factory=dict)

    def start(
        self,
        clazz: Type,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """
        Queue the next xml node for parsing.

        Emit a start event with the current element qualified name and
        attributes.
        """
        super().start(clazz, queue, objects, qname, attrs, ns_map)
        self.emit_event(EventType.START, qname, attrs=attrs)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
    ) -> Any:
        """
        Parse the last xml node and bind any intermediate objects.

        Emit an end event with the result object if any.

        :return: The result of the binding process.
        """
        obj = super().end(queue, objects, qname, text, tail)
        if obj:
            self.emit_event(EventType.END, qname, obj=obj)
        return obj

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """Call if exist the parser's hook for the given element and event."""

        key = (event, name)
        if key not in self.emit_cache:
            method_name = f"{event}_{snake_case(split_qname(name)[1])}"
            self.emit_cache[key] = getattr(self, method_name, None)

        method = self.emit_cache[key]
        if method:
            method(**kwargs)
