from typing import Dict, List, Optional, Type

from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


class WildcardNode(XmlNode):
    """XmlNode for extensible elements that can hold any attribute and content.

    The resulting object tree will be a
    :class:`~xsdata.formats.dataclass.models.generics.AnyElement`
    instance.

    Args:
        var: The xml var instance
        attrs: The element attributes
        ns_map: The element namespace prefix-URI map
        position: The current objects length, everything after
            this position are considered children of this node.
        factory: The generic element factory
    """

    __slots__ = "var", "attrs", "ns_map", "position", "factory"

    def __init__(
        self,
        var: XmlVar,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        factory: Type,
    ):
        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.factory = factory

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        """Bind the parsed data into a generic element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text, bind
        any children objects and initialize new generic element that
        can fit any xml string.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """
        children = self.fetch_any_children(self.position, objects)
        attributes = ParserUtils.parse_any_attributes(self.attrs, self.ns_map)
        derived = qname != self.var.qname
        text = ParserUtils.normalize_content(text) if children else text
        text = "" if text is None and not self.var.nillable else text
        tail = ParserUtils.normalize_content(tail)

        if tail or attributes or children or self.var.is_wildcard or derived:
            obj = self.factory(
                qname=qname,
                text=text,
                tail=tail,
                attributes=attributes,
                children=children,
            )
            objects.append((self.var.qname, obj))
        else:
            objects.append((self.var.qname, text))

        return True

    @classmethod
    def fetch_any_children(cls, position: int, objects: List) -> List:
        """Fetch the children of this node in the objects list.

        The children are removed from the objects list.

        Args:
            position: The position of the objects when this node was created.
            objects: The list of intermediate parsed objects

        Returns:
            A list of parsed objects.
        """
        children = [value for _, value in objects[position:]]

        del objects[position:]

        return children

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Initialize the next child wildcard node to be queued, when an element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data. Wildcard nodes always return wildcard children.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects
        """
        return WildcardNode(
            position=position,
            var=self.var,
            attrs=attrs,
            ns_map=ns_map,
            factory=self.factory,
        )
