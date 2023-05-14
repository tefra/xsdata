from typing import Dict
from typing import Generator
from typing import TextIO

from lxml.etree import indent
from lxml.etree import tostring
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.config import SerializerConfig
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

    :param config: Configuration instance
    :param output: Output text stream
    :param ns_map: User defined namespace prefix-URI map
    """

    __slots__ = ()

    def __init__(self, config: SerializerConfig, output: TextIO, ns_map: Dict):
        super().__init__(config, output, ns_map)

        self.handler = ElementTreeContentHandler()

    def write(self, events: Generator):
        super().write(events)

        assert isinstance(self.handler, ElementTreeContentHandler)

        if self.config.pretty_print and self.config.pretty_print_indent is not None:
            indent(self.handler.etree, self.config.pretty_print_indent)

        xml = tostring(
            self.handler.etree,
            encoding=self.config.encoding,
            pretty_print=self.config.pretty_print,
            xml_declaration=False,
        ).decode()

        self.output.write(xml)
