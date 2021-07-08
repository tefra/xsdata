from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


class WildcardNode(XmlNode):
    """
    XmlNode for extensible elements that can hold any attribute and content.

    The resulting object tree will be a
    :class:`~xsdata.formats.dataclass.models.generics.AnyElement`
    instance.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param position: The node position of objects cache
    :param factory: Wildcard element factory
    """

    __slots__ = "var", "attrs", "ns_map", "position", "factory"

    def __init__(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int, factory: Type
    ):
        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.factory = factory

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        children = self.fetch_any_children(self.position, objects)
        attributes = ParserUtils.parse_any_attributes(self.attrs, self.ns_map)
        derived = self.var.derived or qname != self.var.qname
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
        """Fetch the children of a wildcard node."""
        children = [value for _, value in objects[position:]]

        del objects[position:]

        return children

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        return WildcardNode(
            position=position,
            var=self.var,
            attrs=attrs,
            ns_map=ns_map,
            factory=self.factory,
        )
