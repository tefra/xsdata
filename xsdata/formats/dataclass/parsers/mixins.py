import abc
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Type

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.enums import EventType

NoneStr = Optional[str]


@dataclass
class PushParser(AbstractParser):
    """A generic interface for event based content handlers like sax.

    Args:
        config: The parser configuration instance

    Attributes:
        ns_map: The parsed namespace prefix-URI map
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    ns_map: Dict[Optional[str], str] = field(init=False, default_factory=dict)

    @abc.abstractmethod
    def start(
        self,
        clazz: Optional[Type],
        queue: List[Any],
        objects: List[Any],
        qname: str,
        attrs: Dict[str, str],
        ns_map: Dict[Optional[str], str],
    ):
        """Build and queue the XmlNode for the starting element.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """

    @abc.abstractmethod
    def end(
        self,
        queue: List,
        objects: List,
        qname: str,
        text: NoneStr,
        tail: NoneStr,
    ) -> bool:
        """Parse the last xml node and bind any intermediate objects.

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """

    def register_namespace(self, prefix: NoneStr, uri: str):
        """Register the uri prefix in the namespace registry.

        Args:
            prefix: Namespace prefix
            uri: Namespace uri
        """
        if prefix not in self.ns_map:
            self.ns_map[prefix] = uri


class XmlNode(abc.ABC):
    """The xml node interface.

    The nodes are responsible to find and queue the child nodes when a
    new element starts and build the resulting object tree when the
    element ends. The parser needs to maintain a queue for these nodes
    and a list of all the intermediate objects.
    """

    @abc.abstractmethod
    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> "XmlNode":
        """Initialize the next child node to be queued, when an element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects

        Returns:
            The child xml node instance.
        """

    @abc.abstractmethod
    def bind(
        self,
        qname: str,
        text: NoneStr,
        tail: NoneStr,
        objects: List[Any],
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text, bind
        any children objects and initialize new object.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """


class XmlHandler:
    """Abstract content handler.

    Args:
        parser: The parser instance to feed with events
        clazz: The target class type, auto locate if omitted

    Attributes:
        queue: The XmlNode queue list
        objects: The list of intermediate parsed objects
    """

    __slots__ = ("parser", "clazz", "queue", "objects")

    def __init__(self, parser: PushParser, clazz: Optional[Type]):
        self.parser = parser
        self.clazz = clazz
        self.queue: List = []
        self.objects: List = []

    def parse(self, source: Any) -> Any:
        """Parse the source XML document.

        Args:
            source: The xml source, can be a file resource or an input stream.

        Returns:
            An instance of the class type representing the parsed content.
        """
        raise NotImplementedError("This method must be implemented!")

    def merge_parent_namespaces(self, ns_map: Dict[Optional[str], str]) -> Dict:
        """Merge the given prefix-URI map with the parent node map.

        This method also registers new prefixes with the parser.

        Args:
            ns_map: The current element namespace prefix-URI map

        Returns:
            The new merged namespace prefix-URI map.
        """
        if self.queue:
            parent_ns_map = self.queue[-1].ns_map

            if not ns_map:
                return parent_ns_map

            result = parent_ns_map.copy() if parent_ns_map else {}
        else:
            result = {}

        for prefix, uri in ns_map.items():
            self.parser.register_namespace(prefix, uri)
            result[prefix] = uri

        return result


class EventsHandler(XmlHandler):
    """Sax content handler for pre-recorded events."""

    def parse(self, source: List[Tuple]) -> Any:
        """Forward the pre-recorded events to the main parser.

        Args:
            source: A list of event data

        Returns:
            An instance of the class type representing the parsed content.
        """
        for event, *args in source:
            if event == EventType.START:
                qname, attrs, ns_map = args
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    qname,
                    attrs,
                    ns_map,
                )
            elif event == EventType.END:
                qname, text, tail = args
                self.parser.end(self.queue, self.objects, qname, text, tail)
            elif event == EventType.START_NS:
                prefix, uri = args
                self.parser.register_namespace(prefix or None, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None
