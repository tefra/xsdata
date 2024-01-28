import abc
from typing import (
    Any,
    Dict,
    Final,
    Iterator,
    List,
    Literal,
    Optional,
    TextIO,
    Tuple,
    Union,
)
from xml.etree.ElementTree import QName
from xml.sax.handler import ContentHandler

from typing_extensions import TypeAlias

from xsdata.exceptions import XmlWriterError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.enums import DataType, Namespace, QNames
from xsdata.utils.constants import EMPTY_MAP
from xsdata.utils.namespaces import generate_prefix, prefix_exists, split_qname

XSI_NIL = (Namespace.XSI.uri, "nil")


class XmlWriterEvent:
    """Event names."""

    START: Final = "start"
    ATTR: Final = "attr"
    DATA: Final = "data"
    END: Final = "end"


StartEvent: TypeAlias = Tuple[Literal["start"], str]
AttrEvent: TypeAlias = Tuple[Literal["attr"], str, Any]
DataEvent: TypeAlias = Tuple[Literal["data"], str]
EndEvent: TypeAlias = Tuple[Literal["end"], str]

EventIterator = Iterator[Union[StartEvent, AttrEvent, DataEvent, EndEvent]]


class XmlWriter(abc.ABC):
    """A consistency wrapper for sax content handlers.

    Args:
        config: The serializer config instance
        output: The output stream to write the result
        ns_map: A user defined namespace prefix-URI map

    Attributes:
        handler: The content handler instance
        in_tail: Specifies whether the text content has been written
        tail: The current element tail content
        attrs: The current element attributes
        ns_context: The namespace context queue
        pending_tag: The pending element namespace, name tuple
        pending_prefixes: The pending element namespace prefixes
    """

    __slots__ = (
        "config",
        "output",
        "ns_map",
        # Instance attributes
        "handler",
        "in_tail",
        "tail",
        "attrs",
        "ns_context",
        "pending_tag",
        "pending_prefixes",
    )

    def __init__(
        self,
        config: SerializerConfig,
        output: TextIO,
        ns_map: Dict,
    ):
        self.config = config
        self.output = output
        self.ns_map = ns_map

        self.in_tail = False
        self.tail: Optional[str] = None
        self.attrs: Dict = {}
        self.ns_context: List[Dict] = []
        self.pending_tag: Optional[Tuple] = None
        self.pending_prefixes: List[List] = []
        self.handler = self.build_handler()

    @abc.abstractmethod
    def build_handler(self) -> ContentHandler:
        """Build the content handler instance.

        Returns:
            A content handler instance.
        """

    def write(self, events: EventIterator):
        """Feed the sax content handler with events.

        The receiver will also add additional root attributes
        like xsi or no namespace location.

        Args:
            events: An iterator of sax events

        Raises:
            XmlWriterError: On unknown events.
        """
        self.start_document()

        if self.config.schema_location:
            self.add_attribute(
                QNames.XSI_SCHEMA_LOCATION,
                self.config.schema_location,
                root=True,
            )

        if self.config.no_namespace_schema_location:
            self.add_attribute(
                QNames.XSI_NO_NAMESPACE_SCHEMA_LOCATION,
                self.config.no_namespace_schema_location,
                root=True,
            )

        for name, *args in events:
            if name == XmlWriterEvent.START:
                self.start_tag(*args)
            elif name == XmlWriterEvent.END:
                self.end_tag(*args)
            elif name == XmlWriterEvent.ATTR:
                self.add_attribute(*args)
            elif name == XmlWriterEvent.DATA:
                self.set_data(*args)
            else:
                raise XmlWriterError(f"Unhandled event: `{name}`")

        self.handler.endDocument()

    def start_document(self):
        """Start document notification receiver.

        Write the xml version and encoding, if the
        configuration is enabled.
        """
        if self.config.xml_declaration:
            self.output.write(f'<?xml version="{self.config.xml_version}"')
            self.output.write(f' encoding="{self.config.encoding}"?>\n')

    def start_tag(self, qname: str):
        """Start tag notification receiver.

        The receiver will flush the start of any pending element, create
        new namespaces context and queue the current tag for generation.

        Args:
            qname: The qualified name of the starting element
        """
        self.flush_start(False)

        self.ns_context.append(self.ns_map.copy())
        self.ns_map = self.ns_context[-1]

        self.pending_tag = split_qname(qname)
        self.add_namespace(self.pending_tag[0])

    def add_attribute(self, qname: str, value: Any, root: bool = False):
        """Add attribute notification receiver.

        The receiver will convert the key to a namespace, name tuple and
        convert the value to string. Internally the converter will also
        generate any missing namespace prefixes.

        Args:
            qname: The qualified name of the attribute
            value: The value of the attribute
            root: Specifies if attribute is for the root element

        Raises:
            XmlWriterError: If it's not a root element attribute
                and not no element is pending to start.
        """
        if not self.pending_tag and not root:
            raise XmlWriterError("Empty pending tag.")

        if self.is_xsi_type(qname, value):
            value = QName(value)

        name_tuple = split_qname(qname)
        self.attrs[name_tuple] = self.encode_data(value)

    def add_namespace(self, uri: Optional[str]):
        """Add the given uri to the current namespace context.

         If the uri empty or a prefix already exists, skip silently.

        Args:
            uri: The namespace URI
        """
        if uri and not prefix_exists(uri, self.ns_map):
            generate_prefix(uri, self.ns_map)

    def set_data(self, data: Any):
        """Set data notification receiver.

        The receiver will convert the data to string, flush any previous
        pending start element and send it to the handler for generation.

        If the text content of the tag has already been generated then
        treat the current data as element tail content and queue it to
        be generated when the tag ends.

        Args:
            data: The element text or tail content
        """
        value = self.encode_data(data)
        self.flush_start(is_nil=value is None)

        if value:
            if not self.in_tail:
                self.handler.characters(value)
            else:
                self.tail = value

        self.in_tail = True

    def end_tag(self, qname: str):
        """End tag notification receiver.

        The receiver will flush if pending the start of the element, end
        the element, its tail content and its namespaces prefix mapping
        and current context.

        Args:
            qname: The qualified name of the element
        """
        self.flush_start(True)
        self.handler.endElementNS(split_qname(qname), "")

        if self.tail:
            self.handler.characters(self.tail)

        self.tail = None
        self.in_tail = False
        self.ns_context.pop()
        if self.ns_context:
            self.ns_map = self.ns_context[-1]

        for prefix in self.pending_prefixes.pop():
            self.handler.endPrefixMapping(prefix)

    def flush_start(self, is_nil: bool = True):
        """Flush start notification receiver.

        The receiver will pop the xsi:nil attribute if the element is
        not empty, prepare and send the namespace prefix-URI map and
        the element with its attributes to the content handler for
        generation.

        Args:
            is_nil: Specify if the element requires `xsi:nil="true"`
                when content is empty
        """
        if not self.pending_tag:
            return

        if not is_nil:
            self.attrs.pop(XSI_NIL, None)

        for name in self.attrs:
            self.add_namespace(name[0])

        self.reset_default_namespace()
        self.start_namespaces()

        self.handler.startElementNS(self.pending_tag, "", self.attrs)  # type: ignore
        self.attrs = {}
        self.in_tail = False
        self.pending_tag = None

    def start_namespaces(self):
        """Send the current namespace prefix-URI map to the content handler.

        Save the list of prefixes to be removed at the end of the
        current pending tag.
        """
        prefixes: List[str] = []
        self.pending_prefixes.append(prefixes)

        try:
            parent_ns_map = self.ns_context[-2]
        except IndexError:
            parent_ns_map = EMPTY_MAP

        for prefix, uri in self.ns_map.items():
            if parent_ns_map.get(prefix) != uri:
                prefixes.append(prefix)
                self.handler.startPrefixMapping(prefix, uri)

    def reset_default_namespace(self):
        """Reset the default namespace if the pending element is not qualified."""
        if self.pending_tag and not self.pending_tag[0] and None in self.ns_map:
            self.ns_map[None] = ""

    @classmethod
    def is_xsi_type(cls, qname: str, value: Any) -> bool:
        """Return whether the value is a xsi:type.

        Args:
            qname: The attribute qualified name
            value: The attribute value

        Returns:
            The bool result.
        """
        if isinstance(value, str) and value.startswith("{"):
            return qname == QNames.XSI_TYPE or DataType.from_qname(value) is not None

        return False

    def encode_data(self, data: Any) -> Optional[str]:
        """Encode data for xml rendering.

        Args:
            data: The content to encode/serialize

        Returns:
            The xml encoded data
        """
        if data is None or isinstance(data, str):
            return data

        if isinstance(data, list) and not data:
            return None

        return converter.serialize(data, ns_map=self.ns_map)
