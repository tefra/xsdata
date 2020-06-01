from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple

from lxml.etree import Element
from lxml.etree import QName

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils


@dataclass(frozen=True)
class XmlNode:
    """
    A generic interface for xml nodes that need to implement the two public
    methods to be used in an event based parser with start/end element events.
    The parser needs to maintain a queue for these nodes and a list of objects
    that these nodes return.

    :param position: The current objects size, when the node is created.
    """

    position: int

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> "XmlNode":
        """
        Initialize the next node to be queued, when a new xml element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.
        """
        raise NotImplementedError("Not Implemented")

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        """
        Parse the current element bind child objects and return the result.

        This entry point is called when an xml element ends and is responsible to parse
        the current element attributes/text, bind any children objects and initialize
        a new object.

        :return: A tuple of the object's qualified name and the new object.
        """
        raise NotImplementedError(f"Not Implemented {element.tag}.")


@dataclass(frozen=True)
class ElementNode(XmlNode):
    """
    Element type node is equivalent to xml elements and is used to bind user
    defined dataclasses.

    :param meta: xml metadata of a dataclass model.
    :param config: Parser config instance passed down from the root node.
    """

    meta: XmlMeta
    config: ParserConfig

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        """
        Parse the given element attributes/text, find all child objects and
        mixed content and initialize a new dataclass instance.

        :return: A tuple of the object's qualified name and the new object.
        """
        params: Dict = {}
        ParserUtils.bind_element_attrs(params, self.meta, element)
        ParserUtils.bind_element_text(params, self.meta, element)
        ParserUtils.bind_element_children(params, self.meta, self.position, objects)
        ParserUtils.bind_element_wild_text(params, self.meta, element)

        qname = QName(element.tag)
        obj = self.meta.clazz(**params)

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """
        Initialize the next node to be queued for the given starting element.

        Search by the given element tag for a matching variable and create the next
        node by the variable type.

        :return: The next node to be queued.
        :raises: XmlContextError if the element is unknown and parser config is strict.
        """
        qname = QName(element.tag)
        var = self.meta.find_var(qname, FindMode.NOT_WILDCARD)
        if not var:
            var = self.meta.find_var(qname, FindMode.WILDCARD)

        if not var:
            if self.config.fail_on_unknown_properties:
                raise XmlContextError(
                    f"{self.meta.qname} does not support mixed content: {qname}"
                )
            return SkipNode(position=position)

        if var.clazz:
            xsi_type = ParserUtils.parse_xsi_type(element)
            meta = ctx.fetch(var.clazz, self.meta.qname.namespace, xsi_type)
            return ElementNode(position=position, meta=meta, config=self.config)

        if var.is_any_type:
            return WildcardNode(position=position, qname=var.qname)

        return PrimitiveNode(position=position, var=var)


@dataclass(frozen=True)
class RootNode(ElementNode):
    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """Override parent to return itself if the current element is root."""
        if element.getparent() is None:
            return self
        return super().next_node(element, position, ctx)


@dataclass(frozen=True)
class WildcardNode(XmlNode):
    """
    Wildcard nodes are used for extensible elements that can hold any attribute
    and content and don't have a specific dataclass or primitive type.

    Notes:
        In the future this node should check all known user defined models in the
        target namespace and use that instead of the generic.

    :param qname: xml element tag
    """

    qname: QName

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        """
        Parse the given element attributes/text/tail, find all child objects
        and mixed content and initialize a new generic element instance.

        :return: A tuple of the object's qualified name and a new
            :class:`xsdata.formats.dataclass.models.generics.AnyElement` instance.
        """
        obj = ParserUtils.parse_any_element(element)
        obj.children = ParserUtils.fetch_any_children(self.position, objects)

        return self.qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """
        Initialize the next wildcard node to be queued for the given starting
        element.

        Notes:     Wildcard nodes can only queue other wildcard nodes.
        """
        return WildcardNode(position=position, qname=self.qname)


@dataclass(frozen=True)
class PrimitiveNode(XmlNode):
    var: XmlVar

    def parse_element(self, element: Element, objects: List) -> Tuple:
        """
        Parse the given element text according to the node possible types.

        :return: A tuple of the object's qualified name and the new object.
        """
        qname = QName(element.tag)
        value = element.text
        ns_map = element.nsmap
        obj = ParserUtils.parse_value(
            self.var.types, value, self.var.default, ns_map, self.var.is_tokens
        )

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


@dataclass(frozen=True)
class SkipNode(XmlNode):
    """
    This node is used by the parser to skip unknown elements and their
    children.

    The result of the next_node is always another SkipNode and the
    result of parse_element is always a tuple of None values.
    """

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        return SkipNode(position=position)

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        return None, None
