from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils


class PrimitiveNode(XmlNode):
    """XmlNode for text elements with simple type values.

    Args:
        meta: The parent xml meta instance
        var: The xml var instance
        ns_map: The element namespace prefix-URI map
        config: The parser config instance
        xsi_nil: Specifies whether the element has the xsi:nil attribute
    """

    __slots__ = "config", "meta", "ns_map", "var", "xsi_nil"

    def __init__(
        self,
        meta: XmlMeta,
        var: XmlVar,
        ns_map: dict,
        config: ParserConfig,
        xsi_nil: bool | None,
    ):
        """Initialize the xml node."""
        self.meta = meta
        self.var = var
        self.ns_map = ns_map
        self.config = config
        self.xsi_nil = xsi_nil

    def bind(
        self,
        qname: str,
        text: str | None,
        tail: str | None,
        objects: list,
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text/tail
        content.

        An element with empty content takes the value of the schema
        default or fixed constraint, unless it's nil.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """
        if not text and not self.xsi_nil and self.var.empty_value is not None:
            text = self.var.empty_value

        obj = ParserUtils.parse_var(
            meta=self.meta,
            var=self.var,
            config=self.config,
            value=text,
            ns_map=self.ns_map,
        )

        if obj is None and not self.var.nillable:
            obj = b"" if bytes in self.var.types else ""

        objects.append((qname, obj))

        if self.meta.mixed_content:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Raise an exception if there is a child element inside this node."""
        raise XmlContextError("Primitive node doesn't support child nodes!")
