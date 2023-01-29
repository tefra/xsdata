import functools
from typing import Any
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import Tuple
from urllib.parse import urljoin
from xml.etree import ElementInclude as xinclude
from xml.etree import ElementTree as etree

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.models.enums import EventType
from xsdata.utils import namespaces

EVENTS = (EventType.START, EventType.END, EventType.START_NS)


class XmlEventHandler(XmlHandler):
    """
    Event handler based on :func:`xml.etree.ElementTree.iterparse` api.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model, auto located if omitted.
    """

    __slots__ = ()

    def parse(self, source: Any) -> Any:
        """
        Parse an XML document from a system identifier or an InputSource or
        directly from an xml Element or ElementTree.

        When source is an Element or ElementTree the handler will walk
        over the objects structure.

        When source is a system identifier or an InputSource the parser
        will ignore comments and recover from errors.

        When config process_xinclude is enabled the handler will parse
        the whole document and then walk down the element tree.
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

    def process_context(self, context: Iterable) -> Any:
        """Iterate context and push the events to main parser."""
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
    """
    Walk over the element tree structure and emit start-ns/start/end events.

    The ElementTree doesn't preserve the original namespace prefixes, we
    have to generate new ones.
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
    if base_url:
        return base_url

    return source if isinstance(source, str) else None


def xinclude_loader(
    href: str,
    parse: str,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Any:
    """Custom loader for xinclude to support base_url argument that doesn't
    exist for python < 3.9."""
    return xinclude.default_loader(urljoin(base_url or "", href), parse, encoding)
