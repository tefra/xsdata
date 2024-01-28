from typing import Dict, List, Optional

from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes.element import ElementNode


class WrapperNode(XmlNode):
    """XmlNode for wrapper class fields.

    This node represents wrap class fields, that
    don't actually appear in the serialized document.

    These fields simplify classes and this kind of
    node simply proxies the child requests to the parent
    node.

    Args:
        parent: The parent node

    Attributes:
        ns_map: The node namespace prefix-URI map
    """

    def __init__(self, parent: ElementNode):
        self.parent = parent
        self.ns_map = parent.ns_map

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        """This node will never appear in the xml, so it never binds any data.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Always false because no binding takes place.
        """
        return False

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Proxy the next child node to the parent node.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects

        Returns:
            The child xml node instance.
        """
        return self.parent.child(qname, attrs, ns_map, position)
