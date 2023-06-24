import copy
import warnings
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.exceptions import ConverterWarning
from xsdata.exceptions import ParserError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import EventsHandler
from xsdata.formats.dataclass.parsers.mixins import PushParser
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import EventType

Parsed = Tuple[Optional[str], Any]


@dataclass
class NodeParser(PushParser):
    """
    Bind xml nodes to dataclasses.

    :param config: Parser configuration
    :param context: Model context provider
    :param handler: Override default XmlHandler
    :ivar ms_map: Namespace registry of parsed prefix-URI mappings
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    handler: Type[XmlHandler] = field(default=EventsHandler)
    ns_map: Dict = field(init=False, default_factory=dict)

    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream or filename and return the resulting object
        tree."""
        handler = self.handler(clazz=clazz, parser=self)

        with warnings.catch_warnings():
            if self.config.fail_on_converter_warnings:
                warnings.filterwarnings("error", category=ConverterWarning)

            try:
                result = handler.parse(source)
            except (ConverterWarning, SyntaxError) as e:
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
        """
        Start element notification receiver.

        Build and queue the XmlNode for the starting element.

        :param clazz: Root class type, if it's missing look for any
            suitable models from the current context.
        :param queue: The active XmlNode queue
        :param objects: The list of all intermediate parsed objects
        :param qname: Qualified name
        :param attrs: Attribute key-value map
        :param ns_map: Namespace prefix-URI map
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
        """
        End element notification receiver.

        Pop the last XmlNode from the queue and use it to build and
        return the resulting object tree with its text and tail content.

        :param queue: Xml nodes queue
        :param objects: List of parsed objects
        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        """
        item = queue.pop()
        return item.bind(qname, text, tail, objects)


@dataclass
class RecordParser(NodeParser):
    """
    Bind xml nodes to dataclasses and store the intermediate events.

    :ivar events: List of pushed events
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
        """
        Start element notification receiver.

        Build and queue the XmlNode for the starting element, append the
        event with the attributes and ns map to the events list.

        :param clazz: Root class type, if it's missing look for any
            suitable models from the current context.
        :param queue: The active XmlNode queue
        :param objects: The list of all intermediate parsed objects
        :param qname: Qualified name
        :param attrs: Attributes key-value map
        :param ns_map: Namespace prefix-URI map
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
        """
        End element notification receiver.

        Pop the last XmlNode from the queue and use it to build and
        return the resulting object tree with its text and tail content.
        Append the end event with the text,tail content to the events
        list.

        :param queue: Xml nodes queue
        :param objects: List of parsed objects
        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        """
        self.events.append((EventType.END, qname, text, tail))
        return super().end(queue, objects, qname, text, tail)

    def register_namespace(self, prefix: Optional[str], uri: str):
        self.events.append((EventType.START_NS, prefix, uri))
        super().register_namespace(prefix, uri)
