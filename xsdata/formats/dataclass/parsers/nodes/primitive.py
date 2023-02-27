from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


class PrimitiveNode(XmlNode):
    """
    XmlNode for text elements with primitive values like str, int, float.

    :param var: Class field xml var instance
    :param ns_map: Namespace prefix-URI map
    :param mixed: The node supports mixed content
    :param derived_factory: Derived element factory
    """

    __slots__ = "var", "ns_map", "derived_factory"

    def __init__(self, var: XmlVar, ns_map: Dict, mixed: bool, derived_factory: Type):
        self.var = var
        self.ns_map = ns_map
        self.derived_factory = derived_factory
        self.mixed = mixed

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        obj = ParserUtils.parse_value(
            value=text,
            types=self.var.types,
            default=self.var.default,
            ns_map=self.ns_map,
            tokens_factory=self.var.tokens_factory,
            format=self.var.format,
        )

        if obj is None and not self.var.nillable:
            obj = ""

        if self.var.derived:
            obj = self.derived_factory(qname=qname, value=obj)

        objects.append((qname, obj))

        if self.mixed:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")
