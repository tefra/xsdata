from dataclasses import dataclass
from dataclasses import field
from typing import Generator

from lxml.etree import tostring
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


@dataclass
class LxmlEventWriter(XmlWriter):
    handler: ElementTreeContentHandler = field(
        init=False, default_factory=ElementTreeContentHandler
    )

    def write(self, events: Generator):
        super().write(events)

        xml = tostring(
            self.handler.etree,
            encoding=self.encoding,
            pretty_print=self.pretty_print,
            xml_declaration=True,
        ).decode()

        self.output.write(xml)
