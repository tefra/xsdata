from dataclasses import dataclass
from dataclasses import field
from typing import Generator

from lxml.etree import tostring
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.mixins import XmlEventWriter


@dataclass
class LxmlContentWriter(XmlEventWriter):
    handler: ElementTreeContentHandler = field(
        init=False, default_factory=ElementTreeContentHandler
    )

    def write(self, events: Generator):
        super().write(events)

        xml = tostring(
            self.handler.etree,
            encoding=self.encoding,
            pretty_print=self.pretty_print,
            xml_declaration=self.xml_declaration,
        ).decode()

        self.output.write(xml)
