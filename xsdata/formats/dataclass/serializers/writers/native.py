from dataclasses import dataclass
from dataclasses import field
from xml.sax.saxutils import XMLGenerator

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


@dataclass
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

    # Score vars
    handler: XMLGenerator = field(init=False)
    current_level: int = field(default=0, init=False)
    pending_end_element: bool = field(default=False, init=False)

    def __post_init__(self):
        self.handler = XMLGenerator(
            out=self.output,
            encoding=self.config.encoding,
            short_empty_elements=True,
        )

    def start_tag(self, qname: str):
        super().start_tag(qname)

        if self.config.pretty_print:
            if self.current_level:
                self.handler.ignorableWhitespace("\n")
                self.handler.ignorableWhitespace("  " * self.current_level)

            self.current_level += 1
            self.pending_end_element = False

    def end_tag(self, qname: str):
        if not self.config.pretty_print:
            super().end_tag(qname)
            return

        self.current_level -= 1
        if self.pending_end_element:
            self.handler.ignorableWhitespace("\n")
            self.handler.ignorableWhitespace("  " * self.current_level)

        super().end_tag(qname)

        self.pending_end_element = True
        if not self.current_level:
            self.handler.ignorableWhitespace("\n")
