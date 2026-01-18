from __future__ import annotations

import abc
import io
import pathlib
from dataclasses import dataclass, field
from typing import Any, Optional

from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.types import T
from xsdata.models.enums import EventType


@dataclass
class PushParser:
    """A generic interface for event based content handlers like sax.

    Args:
        config: The parser configuration instance

    Attributes:
        ns_map: The parsed namespace prefix-URI map
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    ns_map: dict[str | None, str] = field(init=False, default_factory=dict)

    def from_path(
        self,
        path: pathlib.Path,
        clazz: type[T] | None = None,
        ns_map: dict[str | None, str] | None = None,
    ) -> T:
        """Parse the input file into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            path: The path to the input file
            clazz: The target class type to parse the file into
            ns_map: A namespace prefix-URI map to record prefixes during parsing

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.parse(str(path.resolve()), clazz, ns_map)

    def from_string(
        self,
        source: str,
        clazz: type[T] | None = None,
        ns_map: dict[str | None, str] | None = None,
    ) -> T:
        """Parse the input source string into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source string to parse
            clazz: The target class type to parse the source string into
            ns_map: A namespace prefix-URI map to record prefixes during parsing

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.from_bytes(source.encode(), clazz, ns_map)

    def from_bytes(
        self,
        source: bytes,
        clazz: type[T] | None = None,
        ns_map: dict[str | None, str] | None = None,
    ) -> T:
        """Parse the input source bytes object into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source bytes object to parse
            clazz: The target class type to parse the source bytes object
            ns_map: A namespace prefix-URI map to record prefixes during parsing

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.parse(io.BytesIO(source), clazz, ns_map)

    @abc.abstractmethod
    def parse(
        self,
        source: Any,
        clazz: type[T] | None = None,
        ns_map: dict[str | None, str] | None = None,
    ) -> T:
        """Parse the input file or stream into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source stream object to parse
            clazz: The target class type to parse the source bytes object
            ns_map: A namespace prefix-URI map to record prefixes during parsing

        Returns:
            An instance of the specified class representing the parsed content.
        """

    @abc.abstractmethod
    def start(
        self,
        clazz: type | None,
        queue: list[Any],
        objects: list[Any],
        qname: str,
        attrs: dict[str, str],
        ns_map: dict[str | None, str],
    ) -> None:
        """Build and queue the XmlNode for the starting element.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """

    @abc.abstractmethod
    def end(
        self,
        queue: list,
        objects: list,
        qname: str,
        text: str | None,
        tail: str | None,
    ) -> bool:
        """Parse the last xml node and bind any intermediate objects.

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """

    def register_namespace(
        self, ns_map: dict[str | None, str], prefix: str | None, uri: str
    ) -> None:
        """Register the uri prefix in the namespace prefix-URI map.

        Args:
            ns_map: The namespace prefix-URI map
            prefix: The namespace prefix
            uri: The namespace uri
        """
        if prefix not in ns_map:
            ns_map[prefix] = uri


class XmlNode(abc.ABC):
    """The xml node interface.

    The nodes are responsible to find and queue the child nodes when a
    new element starts and build the resulting object tree when the
    element ends. The parser needs to maintain a queue for these nodes
    and a list of all the intermediate objects.
    """

    __slots__ = ()

    @abc.abstractmethod
    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Initialize the next child node to be queued, when an element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects

        Returns:
            The child xml node instance.
        """

    @abc.abstractmethod
    def bind(
        self,
        qname: str,
        text: str | None,
        tail: str | None,
        objects: list[Any],
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text, bind
        any children objects and initialize new object.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """


class XmlHandler:
    """Abstract content handler.

    Args:
        parser: The parser instance to feed with events
        clazz: The target class type, auto locate if omitted

    Attributes:
        queue: The XmlNode queue list
        objects: The list of intermediate parsed objects
    """

    __slots__ = ("clazz", "objects", "parser", "queue")

    def __init__(self, parser: PushParser, clazz: type | None):
        """Initialize the handler."""
        self.parser = parser
        self.clazz = clazz
        self.queue: list = []
        self.objects: list = []

    def parse(self, source: Any, ns_map: dict[str | None, str]) -> Any:
        """Parse the source XML document.

        Args:
            source: The xml source, can be a file resource or an input stream.
            ns_map: A dictionary to capture namespace prefixes.

        Returns:
            An instance of the class type representing the parsed content.
        """
        raise NotImplementedError("This method must be implemented!")


class EventsHandler(XmlHandler):
    """Sax content handler for pre-recorded events."""

    def parse(self, source: list[tuple], ns_map: dict[str | None, str]) -> Any:
        """Forward the pre-recorded events to the main parser.

        Args:
            source: A list of event data
            ns_map: A namespace prefix-URI map

        Returns:
            An instance of the class type representing the parsed content.
        """
        for event, *args in source:
            if event == EventType.START:
                qname, attrs, element_ns_map = args
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    qname,
                    attrs,
                    element_ns_map,
                )
            elif event == EventType.END:
                qname, text, tail = args
                self.parser.end(self.queue, self.objects, qname, text, tail)
            elif event == EventType.START_NS:
                prefix, uri = args
                self.parser.register_namespace(ns_map, prefix or None, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None
