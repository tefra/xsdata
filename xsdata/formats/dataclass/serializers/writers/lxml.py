from typing import Generator
from xml.sax.handler import ContentHandler

from lxml.etree import tostring
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


class LxmlEventWriter(XmlWriter):
    """
    :class:`~xsdata.formats.dataclass.serializers.mixins.XmlWriter`
    implementation based on lxml package.

    Based on the :class:`lxml.sax.ElementTreeContentHandler`, converts
    sax events to an lxml ElementTree, serialize and write the result
    to the output stream. Despite that since it's lxml it's still
    pretty fast and has better support for special characters and
    encodings than native python.
    """

    __slots__ = ()

    def initialize_handler(self) -> ContentHandler:
        return ElementTreeContentHandler()

    def write(self, events: Generator):
        super().write(events)

        assert isinstance(self.handler, ElementTreeContentHandler)

        xml = tostring(
            self.handler.etree,
            encoding=self.config.encoding,
            pretty_print=self.config.pretty_print,
            xml_declaration=False,
        ).decode()

        self.output.write(xml)
