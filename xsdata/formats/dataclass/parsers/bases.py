import copy
import warnings
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Type, cast

from xsdata.exceptions import ConverterWarning, ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.mixins import (
    EventsHandler,
    PushParser,
    XmlHandler,
    XmlNode,
)
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.formats.types import T
from xsdata.models.enums import EventType

Parsed = Tuple[Optional[str], Any]


@dataclass
class NodeParser(PushParser):
    """Bind xml nodes to data classes.

    Args:
        context: The models context instance
        handler: The xml handler class

    Attributes:
        ns_map: The parsed namespace prefix-URI map
    """

    context: XmlContext = field(default_factory=XmlContext)
    handler: Type[XmlHandler] = field(default=EventsHandler)

    def parse(
        self,
        source: Any,
        clazz: Optional[Type[T]] = None,
        ns_map: Optional[Dict[Optional[str], str]] = None,
    ) -> T:
        """Parse the input file or stream into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source file or stream object to parse
            clazz: The target class type to parse the source bytes object
            ns_map: A namespace prefix-URI map to record prefixes during parsing

        Returns:
            An instance of the specified class representing the parsed content.
        """
        handler = self.handler(clazz=clazz, parser=self)

        try:
            ns_map = self.ns_map if ns_map is None else ns_map
            result = handler.parse(source, ns_map)
        except SyntaxError as e:
            raise ParserError(e)

        if result is not None:
            return result

        target_class = clazz.__name__ if clazz else ""
        raise ParserError(f"Failed to create target class `{target_class}`")

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Build and queue the XmlNode for the starting element.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """
        from xsdata.formats.dataclass.parsers.nodes import ElementNode, WrapperNode

        try:
            item = queue[-1]
            if isinstance(item, ElementNode) and qname in item.meta.wrappers:
                child = cast(XmlNode, WrapperNode(parent=item))
            else:
                child = item.child(qname, attrs, ns_map, len(objects))
        except IndexError:
            xsi_type = ParserUtils.xsi_type(attrs, ns_map)

            # Match element qname directly
            if clazz is None:
                clazz = self.context.find_type(qname)

            # Root is xs:anyType try xsi:type
            if clazz is None and xsi_type:
                clazz = self.context.find_type(xsi_type)

            # Exit if we still have no binding model
            if clazz is None:
                raise ParserError(f"No class found matching root: {qname}")

            meta = self.context.fetch(clazz, xsi_type=xsi_type)
            if xsi_type is None or meta.qname == qname:
                derived_factory = None
            else:
                derived_factory = self.context.class_type.derived_element

            xsi_nil = ParserUtils.xsi_nil(attrs)

            child = ElementNode(
                position=0,
                meta=meta,
                config=self.config,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                derived_factory=derived_factory,
                xsi_type=xsi_type if derived_factory else None,
                xsi_nil=xsi_nil,
            )

        queue.append(child)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
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
        item = queue.pop()
        return item.bind(qname, text, tail, objects)


@dataclass
class RecordParser(NodeParser):
    """Bind xml nodes to dataclasses and store the intermediate events.

    Attributes:
        events: The list of recorded events
    """

    events: List = field(init=False, default_factory=list)

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Build and queue the XmlNode for the starting element.

        Record the start event for later processing.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """
        self.events.append((EventType.START, qname, copy.deepcopy(attrs), ns_map))
        super().start(clazz, queue, objects, qname, attrs, ns_map)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
    ) -> Any:
        """Parse the last xml node and bind any intermediate objects.

        Record the end event for later processing

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """
        self.events.append((EventType.END, qname, text, tail))
        return super().end(queue, objects, qname, text, tail)

    def register_namespace(
        self, ns_map: Dict[Optional[str], str], prefix: Optional[str], uri: str
    ):
        """Register the uri prefix in the namespace prefix-URI map.

        Record the start-ns event for later processing.

        Args:
            ns_map: The namespace prefix-URI map
            prefix: The namespace prefix
            uri: The namespace uri
        """
        self.events.append((EventType.START_NS, prefix, uri))
        super().register_namespace(ns_map, prefix, uri)
