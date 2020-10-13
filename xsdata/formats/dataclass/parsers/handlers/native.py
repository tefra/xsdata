from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Tuple
from xml import sax
from xml.etree.ElementTree import iterparse

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.handlers import LxmlSaxHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import build_qname

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


@dataclass
class XmlEventHandler(XmlHandler):
    """Content handler based on xml.ElementTree iterparse api."""

    ns_map: Dict = field(default_factory=dict, init=False)

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource.

        :raises XmlHandlerError: If process xinclude config is enabled.
        """
        if self.parser.config.process_xinclude:
            raise XmlHandlerError(
                f"{type(self).__name__} doesn't support xinclude elements."
            )

        return self.process_context(iterparse(source, EVENTS))  # nosec

    def process_context(self, context: Iterable) -> Any:
        """Iterate context and push the events to main parser."""
        obj = None
        self.ns_map = {}
        for event, element in context:
            if event == EventType.START:
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    self.start_ns_bulk(self.ns_map),
                )
                self.ns_map = {}
            elif event == EventType.END:
                obj = self.parser.end(
                    self.queue,
                    self.objects,
                    element.tag,
                    element.text,
                    element.tail,
                )
                element.clear()
            elif event == EventType.START_NS:
                prefix, uri = element
                self.ns_map[prefix] = uri
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return obj


@dataclass
class XmlSaxHandler(LxmlSaxHandler, sax.handler.ContentHandler):
    """
    Xml sax content handler.

    :param ns_map: Active element prefix-URI Namespace mapping
    """

    ns_map: Dict = field(default_factory=dict)

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource.

        :raises XmlHandlerError: If process xinclude config is enabled.
        """
        if self.parser.config.process_xinclude:
            raise XmlHandlerError(
                f"{type(self).__name__} doesn't support xinclude elements."
            )

        parser = sax.make_parser()  # nosec
        parser.setFeature(sax.handler.feature_namespaces, True)
        parser.setContentHandler(self)
        parser.parse(source)
        return self.close()

    def startElementNS(self, name: Tuple[Optional[str], str], qname: Any, attrs: Dict):
        """
        Start element notification receiver.

        The receiver will flush any previous active element, append a new data frame
        to collect data content for the next active element and notify the main parser
        to prepare for next binding instruction.

        Converts name and attribute keys to fully qualified tags to respect the main
        parser api, eg (foo, bar) -> {foo}bar
        """
        tag = build_qname(name[0], name[1])
        attrs = {build_qname(key[0], key[1]): value for key, value in attrs.items()}
        self.start(tag, attrs, self.ns_map)
        self.ns_map = {}

    def endElementNS(self, name: Tuple, qname: Any):
        """
        End element notification receiver.

        The receiver will flush any previous active element and set the next element
        to be flushed.

        Converts name and attribute keys to fully qualified tags to respect the
        main parser api, eg (foo, bar) -> {foo}bar
        """
        self.end(build_qname(name[0], name[1]))

    def characters(self, content: str):
        """Proxy for the data notification receiver."""
        self.data(content)

    def startPrefixMapping(self, prefix: str, uri: str):
        """Start element prefix-URI namespace mapping."""
        self.ns_map[prefix] = uri
