from typing import Any, Iterable, Tuple

from lxml import etree

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


class LxmlEventHandler(XmlHandler):
    """An lxml event handler."""

    def parse(self, source: Any) -> Any:
        """Parse the source XML document.

        Args:
            source: The xml source, can be a file resource or an input stream,
                or a lxml tree/element.

        Returns:
            An instance of the class type representing the parsed content.
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

    def process_context(self, context: Iterable[Tuple[str, Any]]) -> Any:
        """Iterate context and push events to main parser.

        Args:
            context: The iterable lxml context

        Returns:
            An instance of the class type representing the parsed content.
        """
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
