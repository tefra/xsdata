import abc
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.enums import EventType

NoneStr = Optional[str]


class PushParser(AbstractParser):
    """
    A generic interface for event based content handlers like sax.

    :param config: Parser configuration.
    """

    config: ParserConfig

    @abc.abstractmethod
    def start(
        self,
        queue: List,
        qname: str,
        attrs: Dict,
        ns_map: Dict,
        objects: List,
        clazz: Type[T],
    ):
        """Queue the next xml node for parsing."""

    @abc.abstractmethod
    def end(
        self,
        queue: List,
        qname: str,
        text: NoneStr,
        tail: NoneStr,
        objects: List,
    ) -> Any:
        """
        Parse the last xml node and bind any intermediate objects.

        :return: The result of the binding process.
        """

    @abc.abstractmethod
    def start_prefix_mapping(self, prefix: NoneStr, uri: str):
        """Add the given namespace in the registry."""


class XmlNode(abc.ABC):
    """
    A generic interface for xml nodes that need to implement the two public
    methods to be used in an event based parser with start/end element events.

    The parser needs to maintain a queue for these nodes and a list of
    objects that these nodes return.
    """

    @abc.abstractmethod
    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> "XmlNode":
        """
        Initialize the next child node to be queued, when a new xml element
        starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.
        """

    @abc.abstractmethod
    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the current element bind child objects and return the result.

        This entry point is called when an xml element ends and is responsible to parse
        the current element attributes/text, bind any children objects and initialize
        a new object.

        :return: Whether or not anything was appended in the objects list.
        """


@dataclass
class XmlHandler:
    """
    Xml content handler interface.

    :param clazz: The Dataclass model to bind the xml document data.
    :param parser: The parser instance to feed events.
    :param queue: The queue list of xml nodes.
    :param objects: Temporary storage for intermediate objects, eg [(qname, object)]
    """

    clazz: Type
    parser: PushParser
    queue: List = field(default_factory=list)
    objects: List = field(default_factory=list)

    def parse(self, source: Any) -> Any:
        """Parse an XML document from a system identifier or an InputSource."""
        raise NotImplementedError("This method must be implemented!")

    def start_ns_bulk(self, ns_map: Dict) -> Dict:
        """Bulk start-ns event handler that returns a normalized copy of the
        prefix-URI mapping that also includes the parent mapping."""
        try:
            result = self.queue[-1].ns_map.copy()
        except (IndexError, AttributeError):
            result = {}

        for prefix, uri in ns_map.items():
            self.parser.start_prefix_mapping(prefix, uri)
            result[prefix or None] = uri

        return result


@dataclass
class EventsHandler(XmlHandler):
    """Content handler based on pre-recorded events."""

    def parse(self, source: List[Tuple]) -> Any:
        """Forward the pre-recorded events to the main parser."""

        obj = None
        for event in source:
            if event[0] == EventType.START:
                _, qname, attrs, ns_map = event
                self.parser.start(
                    self.queue, qname, attrs, ns_map, self.objects, self.clazz
                )
            elif event[0] == EventType.END:
                _, qname, text, tail = event
                obj = self.parser.end(self.queue, qname, text, tail, self.objects)
            elif event[0] == EventType.START_NS:
                _, prefix, uri = event
                self.parser.start_prefix_mapping(prefix, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event[0]}`.")

        return obj
