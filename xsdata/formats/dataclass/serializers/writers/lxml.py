from typing import Iterator

from lxml import etree
from lxml.sax import ElementTreeContentHandler

from xsdata.formats.dataclass.serializers.mixins import XmlWriter


class LxmlEventWriter(XmlWriter):
    """Xml event writer based on `lxml.sax.ElementTreeContentHandler`.

    The writer converts the events to an lxml tree which is
    then converted to string.

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

    def build_handler(self) -> ElementTreeContentHandler:
        """Build the content handler instance.

        Returns:
            An element tree content handler instance.
        """
        return ElementTreeContentHandler()

    def write(self, events: Iterator):
        """Feed the sax content handler with events.

        The receiver will also add additional root attributes
        like xsi or no namespace location. In the end convert
        the handler etree to string based on the configuration.

        Args:
            events: An iterator of sax events

        Raises:
            XmlWriterError: On unknown events.
        """
        super().write(events)

        assert isinstance(self.handler, ElementTreeContentHandler)

        if self.config.indent:
            etree.indent(self.handler.etree, self.config.indent)

        xml = etree.tostring(
            self.handler.etree,
            encoding=self.config.encoding,
            xml_declaration=False,
        ).decode(self.config.encoding)

        self.output.write(xml)

        if self.config.indent:
            self.output.write("\n")
