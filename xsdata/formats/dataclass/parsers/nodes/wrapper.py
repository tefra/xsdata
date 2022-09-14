from typing import Dict
from typing import List
from typing import Optional

from xsdata.formats.dataclass.parsers.mixins import XmlNode


class WrapperNode(XmlNode):
    """
    XmlNode to wrap an element or primitive list.

    :param parent: The parent node
    """

    def __init__(self, parent: XmlNode):
        self.parent = parent

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        return False

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        return self.parent.child(qname, attrs, ns_map, position)
