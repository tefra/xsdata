import functools
from collections.abc import Iterable, Iterator
from typing import Any, Literal
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

    def parse(self, source: Any, ns_map: dict[str | None, str]) -> Any:
        """Parse the source XML document.

        Args:
            source: The xml source, can be a file resource or an input stream,
                or a xml tree/element.
            ns_map: A namespace prefix-URI recorder map

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

        return self.process_context(ctx, ns_map)

    def process_context(
        self, context: Iterable[tuple[str, Any]], ns_map: dict[str | None, str]
    ) -> Any:
        """Iterate context and push events to main parser.

        Args:
            context: The iterable xml context
            ns_map: A namespace prefix-URI recorder map

        Returns:
            An instance of the class type representing the parsed content.
        """
        element_ns_map: dict = {}
        for event, element in context:
            if event == EventType.START:
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    self.merge_parent_namespaces(element_ns_map),
                )
                element_ns_map = {}
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
                prefix = prefix or None
                element_ns_map[prefix] = uri
                self.parser.register_namespace(ns_map, prefix, uri)

            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None

    def merge_parent_namespaces(self, ns_map: dict[str | None, str]) -> dict:
        """Merge the given prefix-URI map with the parent node map.

        This method also registers new prefixes with the parser.

        Args:
            ns_map: The current element namespace prefix-URI map

        Returns:
            The new merged namespace prefix-URI map.
        """
        if self.queue:
            parent_ns_map = self.queue[-1].ns_map

            if not ns_map:
                return parent_ns_map

            result = parent_ns_map.copy() if parent_ns_map else {}
        else:
            result = {}

        for prefix, uri in ns_map.items():
            result[prefix] = uri

        return result


def iterwalk(element: etree.Element, ns_map: dict) -> Iterator[tuple[str, Any]]:
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


def get_base_url(base_url: str | None, source: Any) -> str | None:
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
    parse: Literal["xml"],
    encoding: str | None = None,
    base_url: str | None = None,
) -> Any:
    """Custom loader for xinclude parsing.

    The base_url argument was added in python >= 3.9.
    """
    return xinclude.default_loader(urljoin(base_url or "", href), parse, encoding)
