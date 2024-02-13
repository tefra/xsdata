from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type

from xsdata.formats.dataclass.parsers.bases import NodeParser, Parsed
from xsdata.formats.dataclass.parsers.handlers import default_handler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler, XmlNode
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import local_name
from xsdata.utils.text import snake_case


@dataclass
class XmlParser(NodeParser):
    """Default Xml parser for data classes.

    Args:
        config: The parser config instance
        context: The xml context instance
        handler: The xml handler class

    Attributes:
        ns_map: The parsed namespace prefix-URI map
    """

    handler: Type[XmlHandler] = field(default=default_handler())


@dataclass
class UserXmlParser(NodeParser):
    """Xml parser for dataclasses with hooks to events.

    The event hooks allow custom parsers to inject custom
    logic between the start/end element events.

    Args:
        config: The parser config instance
        context: The xml context instance
        handler: The xml handler class

    Attributes:
        ns_map: The parsed namespace prefix-URI map
        hooks_cache: The hooks cache is used to avoid
            inspecting the class for custom methods
            on duplicate events.
    """

    handler: Type[XmlHandler] = field(default=default_handler())
    hooks_cache: Dict = field(init=False, default_factory=dict)

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Build and queue the XmlNode for the starting element.

        Override to emit the start element event.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
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
    ) -> bool:
        """Parse the last xml node and bind any intermediate objects.

        Override to emit the end element event if the binding process
        is successful.

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """
        result = super().end(queue, objects, qname, text, tail)
        if result:
            self.emit_event(EventType.END, qname, obj=objects[-1][1])
        return result

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """Propagate event to subclasses.

        Match event and name to a subclass method and trigger it with
        any input keyword arguments.

        Example::
            event=start, name={urn}bookTitle -> start_booking_title(**kwargs)

        Args:
            event: The event type start|end
            name: The qualified name of the element
            kwargs: Additional keyword arguments passed to the hooks
        """
        key = (event, name)
        if key not in self.hooks_cache:
            method_name = f"{event}_{snake_case(local_name(name))}"
            self.hooks_cache[key] = getattr(self, method_name, None)

        method = self.hooks_cache[key]
        if method:
            method(**kwargs)
