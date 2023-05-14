from typing import Dict
from typing import TextIO
from xml.sax.saxutils import XMLGenerator

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import XmlWriter


class XmlEventWriter(XmlWriter):
    """
    :class:`~xsdata.formats.dataclass.serializers.mixins.XmlWriter`
    implementation based on native python.

    Based on the native python :class:`xml.sax.saxutils.XMLGenerator`
    with support for indentation. Converts sax events directly to xml
    output without storing intermediate result to memory.

    :param config: Configuration instance
    :param output: Output text stream
    :param ns_map: User defined namespace prefix-URI map
    """

    __slots__ = ("current_level", "pending_end_element")

    def __init__(self, config: SerializerConfig, output: TextIO, ns_map: Dict):
        """
        :param config: Configuration instance
        :param output: Output text stream
        :param ns_map: User defined namespace prefix-URI map
        """
        super().__init__(config, output, ns_map)

        self.current_level = 0
        self.pending_end_element = False
        self.handler = XMLGenerator(
            out=self.output, encoding=self.config.encoding, short_empty_elements=True
        )

    def start_tag(self, qname: str):
        super().start_tag(qname)

        if self.config.pretty_print:
            if self.current_level:
                self.handler.ignorableWhitespace("\n")
                self.handler.ignorableWhitespace(
                    (self.config.pretty_print_indent or "  ") * self.current_level
                )

            self.current_level += 1
            self.pending_end_element = False

    def end_tag(self, qname: str):
        if not self.config.pretty_print:
            super().end_tag(qname)
            return

        self.current_level -= 1
        if self.pending_end_element:
            self.handler.ignorableWhitespace("\n")
            self.handler.ignorableWhitespace(
                (self.config.pretty_print_indent or "  ") * self.current_level
            )

        super().end_tag(qname)

        self.pending_end_element = True
        if not self.current_level:
            self.handler.ignorableWhitespace("\n")
