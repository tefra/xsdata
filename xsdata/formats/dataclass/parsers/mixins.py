import abc
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
    ns_map: Dict

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
    ) -> bool:
        """
        Parse the last xml node and bind any intermediate objects.

        :return: The result of the binding process.
        """

    def register_namespace(self, prefix: NoneStr, uri: str):
        """
        Add the given prefix-URI namespaces mapping if the prefix is new.

        :param prefix: Namespace prefix
        :param uri: Namespace uri
        """
        if prefix not in self.ns_map:
            self.ns_map[prefix] = uri


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

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.

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
        responsible to parse the current element attributes/text, bind
        any children objects and initialize  new object.

        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        :param objects: The list of intermediate parsed objects, eg
            [(qname, object)]
        """


class XmlHandler:
    """
    Abstract content handler.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model, auto located if omitted.
    """

    __slots__ = ("parser", "clazz", "queue", "objects")

    def __init__(self, parser: PushParser, clazz: Optional[Type]):
        self.parser = parser
        self.clazz = clazz
        self.queue: List = []
        self.objects: List = []

    def parse(self, source: Any) -> Any:
        """Parse an XML document from a system identifier or an InputSource."""
        raise NotImplementedError("This method must be implemented!")

    def merge_parent_namespaces(self, ns_map: Dict) -> Dict:
        """
        Merge and return the given prefix-URI map with the parent node.

        Register new prefixes with the parser.

        :param ns_map: Namespace prefix-URI map
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

    __slots__ = ("data_frames", "flush_next")

    def __init__(self, parser: PushParser, clazz: Optional[Type]):
        super().__init__(parser, clazz)
        self.data_frames: List = []
        self.flush_next: Optional[str] = None

    def parse(self, source: List[Tuple]) -> Any:
        """Forward the pre-recorded events to the main parser."""
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
