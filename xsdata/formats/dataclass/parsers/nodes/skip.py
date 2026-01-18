from typing import Optional

from xsdata.formats.dataclass.parsers.mixins import XmlNode


class SkipNode(XmlNode):
    """Utility node to skip parsing unknown properties."""

    __slots__ = "ns_map"

    def __init__(self):
        """Initialize the xml node."""
        self.ns_map = {}

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Skip nodes children are skipped as well."""
        return self

    def bind(
        self, qname: str, text: str | None, tail: str | None, objects: list
    ) -> bool:
        """Skip nodes are not building any objects."""
        return False
