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
        clazz: Optional[Type],
        queue: List,
        objects: List,
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Queue the next xml node for parsing."""

    @abc.abstractmethod
    def end(
        self,
        queue: List,
        objects: List,
        qname: str,
        text: NoneStr,
        tail: NoneStr,
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
    The xml node interface.

    The nodes are responsible to find and queue the child nodes when a
    new element starts and build the resulting object tree when the
    element ends. The parser needs to maintain a queue for these nodes
    and a list of all the intermediate object trees.
    """

    @abc.abstractmethod
    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> "XmlNode":
        """
        Initialize the next child node to be queued, when a new xml element
        starts.

        This entry point is responsible to create the next node
        type with all the necessary information on how to bind
        the incoming input data.

        :param qname: Qualified name
        :param attrs: Attribute key-value map
        :param ns_map: Namespace prefix-URI map
        :param position: The current objects position, to mark future
            objects as children
        """

    @abc.abstractmethod
    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Build the object tree for the ending element and return whether the
        result was successful or not.

        This entry point is called when an xml element ends and is
        responsible to parse the current element attributes/text,
        bind any children objects and initialize  new object.

        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        :param objects: The list of intermediate parsed objects,
            eg [(qname, object)]
        """


@dataclass
class XmlHandler:
    """
    Abstract content handler.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model. If None the parser will
        auto locate it from the active xml context instance
    :param queue: The XmlNode queue
    :param objects: The list of intermediate parsed objects,
        eg [(qname, object)]
    """

    parser: PushParser
    clazz: Optional[Type]
    queue: List = field(default_factory=list)
    objects: List = field(default_factory=list)

    def parse(self, source: Any) -> Any:
        """Parse an XML document from a system identifier or an InputSource."""
        raise NotImplementedError("This method must be implemented!")

    def start_ns_bulk(self, ns_map: Dict) -> Dict:
        """
        Bulk start-ns event handler that returns a normalized copy of the
        prefix-URI map merged with the parent element map.

        :param ns_map: Namespace prefix-URI map
        """
        try:
            result = self.queue[-1].ns_map.copy()
        except (IndexError, AttributeError):
            result = {}

        for prefix, uri in ns_map.items():
            prefix = prefix or None
            self.parser.start_prefix_mapping(prefix, uri)
            result[prefix] = uri

        return result


@dataclass
class EventsHandler(XmlHandler):
    """
    Sax content handler for pre-recorded events.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model. If None the parser will
        auto locate it from the active xml context instance
    :param queue: The XmlNode queue
    :param objects: The list of intermediate parsed objects,
        eg [(qname, object)]
    """

    def parse(self, source: List[Tuple]) -> Any:
        """Forward the pre-recorded events to the main parser."""

        obj = None
        for event, *args in source:
            if event == EventType.START:
                self.parser.start(self.clazz, self.queue, self.objects, *args)
            elif event == EventType.END:
                obj = self.parser.end(self.queue, self.objects, *args)
            elif event == EventType.START_NS:
                self.parser.start_prefix_mapping(*args)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return obj
