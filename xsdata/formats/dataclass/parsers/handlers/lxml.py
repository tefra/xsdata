from dataclasses import dataclass
from typing import Any
from typing import Iterable

from lxml import etree

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.mixins import SaxHandler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


@dataclass
class LxmlEventHandler(XmlHandler):
    """
    Event handler based on :class:`lxml.etree.iterparse` api.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model. If None the parser will
        auto locate it from the active xml context instance
    :param queue: The XmlNode queue
    :param objects: The list of intermediate parsed objects,
        eg [(qname, object)]
    """

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource.

        The xml parser will ignore comments, recover from errors. The
        parser will parse the whole document and then walk down the tree
        if the process xinclude is enabled.
        """
        if self.parser.config.process_xinclude:
            tree = etree.parse(source, base_url=self.parser.config.base_url)  # nosec
            tree.xinclude()
            ctx = etree.iterwalk(tree, EVENTS)
        else:
            ctx = etree.iterparse(source, EVENTS, recover=True, remove_comments=True)

        return self.process_context(ctx)

    def process_context(self, context: Iterable) -> Any:
        """Iterate context and push the events to main parser."""
        obj = None
        for event, element in context:
            if event == EventType.START:
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    element.nsmap,
                )
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
                self.parser.start_prefix_mapping(prefix, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return obj


@dataclass
class LxmlSaxHandler(SaxHandler):
    """
    Sax content handler based on :class:`lxml.etree.XMLParser` api.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model. If None the parser will
        auto locate it from the active xml context instance
    :param queue: The XmlNode queue
    :param objects: The list of intermediate parsed objects,
        eg [(qname, object)]
    """

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource.

        The xml parser will ignore comments, recover from errors and
        clean duplicate namespace prefixes.
        """

        if self.parser.config.process_xinclude:
            raise XmlHandlerError(
                f"{type(self).__name__} doesn't support xinclude elements."
            )

        parser = etree.XMLParser(
            target=self,
            recover=True,
            remove_comments=True,
            ns_clean=True,
            resolve_entities=False,
            no_network=True,
        )

        return etree.parse(source, parser=parser)  # nosec
