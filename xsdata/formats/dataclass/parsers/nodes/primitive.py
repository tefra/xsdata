from typing import Dict, List, Optional

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


class PrimitiveNode(XmlNode):
    """XmlNode for text elements with simple type values.

    Args:
        var: The xml var instance
        ns_map: The element namespace prefix-URI map
        mixed: Specifies if this node supports mixed content
    """

    __slots__ = "var", "ns_map"

    def __init__(self, var: XmlVar, ns_map: Dict, mixed: bool):
        self.var = var
        self.ns_map = ns_map
        self.mixed = mixed

    def bind(
        self,
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: List,
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text/tail
        content.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """
        obj = ParserUtils.parse_value(
            value=text,
            types=self.var.types,
            default=self.var.default,
            ns_map=self.ns_map,
            tokens_factory=self.var.tokens_factory,
            format=self.var.format,
        )

        if obj is None and not self.var.nillable:
            obj = b"" if bytes in self.var.types else ""

        objects.append((qname, obj))

        if self.mixed:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Raise an exception if there is a child element inside this node."""
        raise XmlContextError("Primitive node doesn't support child nodes!")
