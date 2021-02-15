from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import TextIO
from typing import Tuple
from xml.etree.ElementTree import QName
from xml.sax.handler import ContentHandler

from xsdata.exceptions import XmlWriterError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.utils.constants import EMPTY_MAP
from xsdata.utils.namespaces import generate_prefix
from xsdata.utils.namespaces import prefix_exists
from xsdata.utils.namespaces import split_qname

XSI_NIL = (Namespace.XSI.uri, "nil")


class XmlWriterEvent:
    START = "start"
    ATTR = "attr"
    DATA = "data"
    END = "end"


@dataclass
class XmlWriter:
    """
    A consistency wrapper for sax content handlers.

    - Implements a custom sax-like event api with separate start
      element/attribute events.
    - Buffers events until all content has been received or a child
      element is starting in order to build the current element's
      namespace context correctly.
    - Prepares values for serialization.

    :param config: Configuration instance
    :param output: Output text stream
    :param ns_map: User defined namespace prefix-URI map
    """

    config: SerializerConfig
    output: TextIO
    ns_map: Dict = field(default_factory=dict)

    # Scope vars
    handler: ContentHandler = field(init=False)
    in_tail: bool = field(init=False, default=False)
    tail: Optional[str] = field(init=False, default=None)
    attrs: Dict = field(init=False, default_factory=dict)
    ns_context: List[Dict] = field(init=False, default_factory=list)
    pending_tag: Optional[Tuple] = field(init=False, default=None)
    pending_prefixes: List[List] = field(init=False, default_factory=list)

    def write(self, events: Generator):
        """
        Iterate over the generator events and feed the sax content handler with
        the information needed to generate the xml output.

        Example::

            (XmlWriterEvent.START, "{http://www.w3.org/1999/xhtml}p"),
            (XmlWriterEvent.ATTR, "class", "paragraph"),
            (XmlWriterEvent.DATA, "Hello"),
            (XmlWriterEvent.END, "{http://www.w3.org/1999/xhtml}p"),

        :param events: Events generator
        """
        self.start_document()

        if self.config.schema_location:
            self.add_attribute(
                QNames.XSI_SCHEMA_LOCATION,
                self.config.schema_location,
                check_pending=False,
            )

        if self.config.no_namespace_schema_location:
            self.add_attribute(
                QNames.XSI_NO_NAMESPACE_SCHEMA_LOCATION,
                self.config.no_namespace_schema_location,
                check_pending=False,
            )

        for event, *args in events:
            if event == XmlWriterEvent.START:
                self.start_tag(*args)
            elif event == XmlWriterEvent.END:
                self.end_tag(*args)
            elif event == XmlWriterEvent.ATTR:
                self.add_attribute(*args)
            elif event == XmlWriterEvent.DATA:
                self.set_data(*args)
            else:
                raise XmlWriterError(f"Unhandled event: `{event}`")

        self.handler.endDocument()

    def start_document(self):
        """"""
        if self.config.xml_declaration:
            self.output.write(f'<?xml version="{self.config.xml_version}"')
            self.output.write(f' encoding="{self.config.encoding}"?>\n')

    def start_tag(self, qname: str):
        """
        Start tag notification receiver.

        The receiver will flush the start of any pending element,
        create new namespaces context and queue the current tag
        for generation.

        :param qname: Tag qualified name
        """
        self.flush_start(False)

        self.ns_context.append(self.ns_map.copy())
        self.ns_map = self.ns_context[-1]

        self.pending_tag = split_qname(qname)
        self.add_namespace(self.pending_tag[0])

    def add_attribute(self, key: str, value: Any, check_pending: bool = True):
        """
        Add attribute notification receiver.

        The receiver will convert the key to a namespace, name tuple
        and convert the value to string. Internally the converter will
        also generate any missing namespace prefixes.

        :param key: Attribute name
        :param value: Attribute value
        :param check_pending: Raise exception if not no element is
            pending start
        """

        if not self.pending_tag and check_pending:
            raise XmlWriterError("Empty pending tag.")

        if self.is_xsi_type(key, value):
            value = QName(value)

        name = split_qname(key)
        self.attrs[name] = self.encode_data(value)

    def add_namespace(self, uri: Optional[str]):
        """
        Add the given uri to the current namespace context if the uri is valid
        and new.

        The prefix will be auto generated if it doesn't exist in the
        prefix-URI mappings.

        :param uri: Namespace uri
        """
        if uri and not prefix_exists(uri, self.ns_map):
            generate_prefix(uri, self.ns_map)

    def set_data(self, data: Any):
        """
        Set data notification receiver.

        The receiver will convert the data to string, flush any previous pending
        start element and send it to the handler for generation.

        If the text content of the tag has already been generated then treat the
        current data as element tail content and queue it to be generated when the
        tag ends.

        :param data: Element text or tail content
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
        """
        End tag notification receiver.

        The receiver will flush if pending the start of the element, end
        the element, its tail content and its namespaces prefix mapping
        and current context.

        :param qname: Tag qualified name
        """
        self.flush_start(True)
        self.handler.endElementNS(split_qname(qname), None)

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
        """
        Flush start notification receiver.

        The receiver will pop the xsi:nil attribute if the element is
        not empty, prepare and send the namespaces prefix mappings and
        the element with its attributes to the content handler for
        generation.

        :param is_nil: If true add ``xsi:nil="true"`` to the element
            attributes
        """

        if self.pending_tag:

            if not is_nil:
                self.attrs.pop(XSI_NIL, None)

            for name in self.attrs.keys():
                self.add_namespace(name[0])

            self.reset_default_namespace()
            self.start_namespaces()

            self.handler.startElementNS(self.pending_tag, None, self.attrs)
            self.attrs = {}
            self.in_tail = False
            self.pending_tag = None

    def start_namespaces(self):
        """
        Send the new prefixes and namespaces added in the current context to
        the content handler.

        Save the list of prefixes to be removed at the end of the
        current pending tag.
        """

        prefixes = []
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
        """Reset the default namespace if exists and the current pending tag is
        not qualified."""
        if not self.pending_tag[0] and None in self.ns_map:
            self.ns_map[None] = ""

    @classmethod
    def is_xsi_type(cls, key: str, value: Any) -> bool:
        """
        Return whether the value is an xsi:type or not based on the given
        attribute name/value.

        :param key: Attribute name
        :param value: Attribute value
        """

        if isinstance(value, str) and value.startswith("{"):
            return key == QNames.XSI_TYPE or DataType.from_qname(value) is not None

        return False

    def encode_data(self, data: Any) -> Optional[str]:
        """Encode data for xml rendering."""
        if data is None or isinstance(data, str):
            return data

        if isinstance(data, list) and not data:
            return None

        return converter.serialize(data, ns_map=self.ns_map)
