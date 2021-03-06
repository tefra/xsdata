from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.formats.dataclass.parsers.handlers import default_handler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import local_name
from xsdata.utils.text import snake_case


@dataclass
class XmlParser(NodeParser):
    """
    Xml parser for dataclasses.

    :param config: Parser configuration
    :param context: Model context provider
    :param handler: Override default XmlHandler
    :ivar ms_map: The prefix-URI map generated during parsing
    :ivar emit_cache: Qname to event name cache
    """

    handler: Type[XmlHandler] = field(default=default_handler())
    emit_cache: Dict = field(init=False, default_factory=dict)

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """
        Start element notification receiver.

        Build and queue the XmlNode for the starting element and
        emits and propagate the event to subclasses.

        :param clazz: Root class type, if it's missing look for any
            suitable models from the current context.
        :param queue: The active XmlNode queue
        :param objects: The list of all intermediate parsed objects
        :param qname: Qualified name
        :param attrs: Attribute key-value map
        :param ns_map: Namespace prefix-URI map
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
        End element notification receiver.

        Pop the last XmlNode from the queue and use it to build and
        return the resulting object tree with its text and tail
        content. Propagate the event to subclasses.

        :param queue: Xml nodes queue
        :param objects: List of parsed objects
        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        """
        obj = super().end(queue, objects, qname, text, tail)
        if obj:
            self.emit_event(EventType.END, qname, obj=obj)
        return obj

    def emit_event(self, event: str, name: str, **kwargs: Any):
        """
        Propagate event to subclasses.

        Match event and name to a subclass method and trigger it with
        any input keyword arguments.

        Example::

            event=start, name={urn}bookTitle -> start_booking_title(**kwargs)

        :param event: Event type start|end
        :param name: Element qualified name
        :param kwargs: Event keyword arguments
        """

        key = (event, name)
        if key not in self.emit_cache:
            method_name = f"{event}_{snake_case(local_name(name))}"
            self.emit_cache[key] = getattr(self, method_name, None)

        method = self.emit_cache[key]
        if method:
            method(**kwargs)
