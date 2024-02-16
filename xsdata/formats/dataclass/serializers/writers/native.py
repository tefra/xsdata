from typing import Dict, TextIO
from xml.sax.saxutils import XMLGenerator

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import XmlWriter


class XmlEventWriter(XmlWriter):
    """Xml event writer based on `xml.sax.saxutils.XMLGenerator`.

    The writer converts sax events directly to xml output
    without storing any intermediate results in memory.

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

    __slots__ = ("current_level", "pending_end_element")

    def __init__(self, config: SerializerConfig, output: TextIO, ns_map: Dict):
        super().__init__(config, output, ns_map)

        self.current_level = 0
        self.pending_end_element = False

    def build_handler(self) -> XMLGenerator:
        """Build the content handler instance.

        Returns:
            A xml generator content handler instance.
        """
        return XMLGenerator(
            out=self.output,
            encoding=self.config.encoding,
            short_empty_elements=True,
        )

    def start_tag(self, qname: str):
        """Start tag notification receiver.

        The receiver will flush the start of any pending element, create
        new namespaces context and queue the current tag for generation.

        The receiver will also write the necessary whitespace if
        pretty print is enabled.

        Args:
            qname: The qualified name of the starting element
        """
        super().start_tag(qname)

        if self.config.indent:
            if self.current_level:
                self.handler.ignorableWhitespace("\n")
                self.handler.ignorableWhitespace(
                    self.config.indent * self.current_level
                )

            self.current_level += 1
            self.pending_end_element = False

    def end_tag(self, qname: str):
        """End tag notification receiver.

        The receiver will flush if pending the start of the element, end
        the element, its tail content and its namespaces prefix mapping
        and current context.

        The receiver will also write the necessary whitespace if
        pretty print is enabled.

        Args:
            qname: The qualified name of the element
        """
        if not self.config.indent:
            super().end_tag(qname)
            return

        self.current_level -= 1
        if self.pending_end_element:
            self.handler.ignorableWhitespace("\n")
            self.handler.ignorableWhitespace(self.config.indent * self.current_level)

        super().end_tag(qname)

        self.pending_end_element = True
        if not self.current_level:
            self.handler.ignorableWhitespace("\n")
