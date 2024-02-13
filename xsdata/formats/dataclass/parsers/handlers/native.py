import functools
from typing import Any, Dict, Iterable, Iterator, Optional, Tuple
from urllib.parse import urljoin
from xml.etree import ElementInclude as xinclude
from xml.etree import ElementTree as etree

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType
from xsdata.utils import namespaces

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


class XmlEventHandler(XmlHandler):
    """A native xml event handler."""

    def parse(self, source: Any) -> Any:
        """Parse the source XML document.

        Args:
            source: The xml source, can be a file resource or an input stream,
                or a xml tree/element.

        Returns:
            An instance of the class type representing the parsed content.
        """
        if isinstance(source, etree.ElementTree):
            source = source.getroot()

        if isinstance(source, etree.Element):
            ctx = iterwalk(source, {})
        elif self.parser.config.process_xinclude:
            root = etree.parse(source).getroot()  # nosec
            base_url = get_base_url(self.parser.config.base_url, source)
            loader = functools.partial(xinclude_loader, base_url=base_url)

            xinclude.include(root, loader=loader)
            ctx = iterwalk(root, {})
        else:
            ctx = etree.iterparse(source, EVENTS)  # nosec

        return self.process_context(ctx)

    def process_context(self, context: Iterable[Tuple[str, Any]]) -> Any:
        """Iterate context and push events to main parser.

        Args:
            context: The iterable xml context

        Returns:
            An instance of the class type representing the parsed content.
        """
        ns_map: Dict = {}
        for event, element in context:
            if event == EventType.START:
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    self.merge_parent_namespaces(ns_map),
                )
                ns_map = {}
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
                ns_map[prefix or None] = uri
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None


def iterwalk(element: etree.Element, ns_map: Dict) -> Iterator[Tuple[str, Any]]:
    """Walk over the element tree and emit events.

    The ElementTree doesn't preserve the original namespace prefixes, we
    have to generate new ones.

    Args:
        element: The etree element instance
        ns_map: The namespace prefix-URI mapping

    Yields:
        An iterator of events
    """
    uri = namespaces.target_uri(element.tag)
    if uri is not None:
        prefix = namespaces.load_prefix(uri, ns_map)
        yield EventType.START_NS, (prefix, uri)

    yield EventType.START, element

    for child in element:
        yield from iterwalk(child, ns_map)

    yield EventType.END, element


def get_base_url(base_url: Optional[str], source: Any) -> Optional[str]:
    """Return the base url of the source.

    Args:
        base_url: The base url from the parser config
        source: The xml source input

    Returns:
        A base url str or None, if no base url is provided
        and the source is not a string path.
    """
    if base_url:
        return base_url

    return source if isinstance(source, str) else None


def xinclude_loader(
    href: str,
    parse: str,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Any:
    """Custom loader for xinclude parsing.

    The base_url argument was added in python >= 3.9.
    """
    return xinclude.default_loader(urljoin(base_url or "", href), parse, encoding)
