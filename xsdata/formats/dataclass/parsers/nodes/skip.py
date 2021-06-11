from typing import Dict
from typing import List
from typing import Optional

from xsdata.formats.dataclass.parsers.mixins import XmlNode


class SkipNode(XmlNode):
    """Utility node to skip parsing unknown properties."""

    __slots__ = "ns_map"

    def __init__(self):
        self.ns_map = {}

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Skip nodes children are skipped as well."""
        return self

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        """Skip nodes are not building any objects."""
        return False
