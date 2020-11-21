from dataclasses import dataclass
from dataclasses import field
from xml.sax.saxutils import XMLGenerator

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


@dataclass
class XmlEventWriter(XmlWriter):
    handler: XMLGenerator = field(init=False)
    depth: int = field(default=0, init=False)
    ended: int = field(default=0, init=False)

    def __post_init__(self):
        self.handler = XMLGenerator(
            out=self.output,
            encoding=self.encoding,
            short_empty_elements=True,
        )

    def start_tag(self, qname: str):
        super().start_tag(qname)

        if self.pretty_print:
            if self.depth:
                self.handler.ignorableWhitespace("\n")
                self.handler.ignorableWhitespace("  " * self.depth)

            self.depth += 1
            self.ended = 0

    def end_tag(self, qname: str):
        if not self.pretty_print:
            super().end_tag(qname)
            return

        self.depth -= 1
        if self.ended:
            self.handler.ignorableWhitespace("\n")
            self.handler.ignorableWhitespace("  " * self.depth)

        super().end_tag(qname)

        self.ended += 1
        if not self.depth:
            self.handler.ignorableWhitespace("\n")
