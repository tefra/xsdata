from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional

from lxml import etree

from xsdata.exceptions import XmlHandlerError
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
class LxmlSaxHandler(XmlHandler):
    """
    Sax content handler based on :class:`lxml.etree.XMLParser` api.

    :param parser: The parser instance to feed with events
    :param clazz: The target binding model. If None the parser will
        auto locate it from the active xml context instance
    :param queue: The XmlNode queue
    :param objects: The list of intermediate parsed objects,
        eg [(qname, object)]
    """

    # Scope vars
    data_frames: List = field(init=False, default_factory=list)
    flush_next: Optional[str] = field(init=False, default=None)

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

    def start(self, qname: str, attrs: Dict, ns_map: Dict):
        """
        Start element notification receiver.

        The receiver will flush any previous active element, append a
        new data frame  to collect data content for the next active
        element and notify the main  parser to prepare for next binding
        instruction.

        :param qname: Qualified name
        :param attrs: Attribute key-value map
        :param ns_map: Namespace prefix-URI map
        """
        self.flush()
        self.data_frames.append(([], []))
        self.parser.start(
            self.clazz,
            self.queue,
            self.objects,
            qname,
            attrs,
            self.start_ns_bulk(ns_map),
        )

    def end(self, qname: str):
        """
        End element notification receiver.

        The receiver will flush any previous active element and set the
        next element to be flushed.

        :param qname: Qualified name
        """
        self.flush()
        self.flush_next = qname

    def close(self) -> Any:
        """
        Close document notification receiver.

        The receiver will flush any previous active element and return
        the first item in the objects stack.
        """
        try:
            self.flush()
            return self.objects[0][1]
        except IndexError:
            return None

    def flush(self):
        """
        Flush element notification receiver.

        The receiver will check if there is an active element present,
        collect and join the data frames for text/tail content and
        notify the main parser to finish the binding process for the
        element.
        """
        if self.flush_next:
            data = self.data_frames.pop()
            text = "".join(data[0]) if data[0] else None
            tail = "".join(data[1]) if data[1] else None

            self.parser.end(self.queue, self.objects, self.flush_next, text, tail)
            self.flush_next = None

    def data(self, data: str):
        """
        Data notification receiver.

        The receiver will append the given data content in the current
        data frame either in the text position 0 or in the tail position
        1 whether the element has ended or not.

        :param data: Text or tail content
        """
        index = 0 if self.flush_next is None else 1
        self.data_frames[-1][index].append(data)
