from dataclasses import dataclass
from dataclasses import field
from typing import Generator

from lxml.etree import tostring
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


@dataclass
class LxmlEventWriter(XmlWriter):
    """
    :class:`~xsdata.formats.dataclass.serializers.mixins.XmlWriter`
    implementation based on lxml package.

    Based on the :class:`lxml.sax.ElementTreeContentHandler`, converts
    sax events to an lxml ElementTree, serialize and write the result
    to the output stream. Despite that since it's lxml it's still
    pretty fast and has better support for special characters and
    encodings than native python.

    :param config: Configuration instance
    :param output: Output text stream
    :param ns_map: User defined namespace prefix-URI map
    """

    handler: ElementTreeContentHandler = field(
        init=False, default_factory=ElementTreeContentHandler
    )

    def write(self, events: Generator):
        super().write(events)

        xml = tostring(
            self.handler.etree,
            encoding=self.config.encoding,
            pretty_print=self.config.pretty_print,
            xml_declaration=False,
        ).decode()

        self.output.write(xml)
