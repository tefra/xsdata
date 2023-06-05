from typing import Any
from typing import Iterable

from lxml import etree

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


class LxmlEventHandler(XmlHandler):
    """
    Event handler based on :class:`lxml.etree.iterparse` api.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model, auto located if omitted.
    """

    __slots__ = ()

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource or
        directly from a lxml Element or Tree.

        When Source is a lxml Element or Tree the handler will switch to
        the :class:`lxml.etree.iterwalk` api.

        When source is a system identifier or an InputSource the parser
        will ignore comments and recover from errors.

        When config process_xinclude is enabled the handler will parse
        the whole document and then walk down the element tree.
        """
        if isinstance(source, (etree._ElementTree, etree._Element)):
            ctx = etree.iterwalk(source, EVENTS)
        elif self.parser.config.process_xinclude:
            tree = etree.parse(source, base_url=self.parser.config.base_url)  # nosec
            tree.xinclude()
            ctx = etree.iterwalk(tree, EVENTS)
        else:
            ctx = etree.iterparse(
                source,
                EVENTS,
                recover=True,
                remove_comments=True,
                load_dtd=self.parser.config.load_dtd,
            )

        return self.process_context(ctx)

    def process_context(self, context: Iterable) -> Any:
        """Iterate context and push the events to main parser."""
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
                self.parser.end(
                    self.queue,
                    self.objects,
                    element.tag,
                    element.text,
                    element.tail,
                )
                element.clear()
            elif event == EventType.START_NS:
                prefix, uri = element
                self.parser.register_namespace(prefix or None, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None
