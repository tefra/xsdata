from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType


class StandardNode(XmlNode):
    """
    XmlNode for any type elements with a standard xsi:type.

    :param datatype: Standard xsi data type
    :param ns_map: Namespace prefix-URI map
    :param nillable: Specify whether the node supports nillable content
    :param derived_factory: Optional derived element factory
    """

    __slots__ = "datatype", "ns_map", "nillable", "derived_factory"

    def __init__(
        self,
        datatype: DataType,
        ns_map: Dict,
        nillable: bool,
        derived_factory: Optional[Type],
    ):
        self.datatype = datatype
        self.ns_map = ns_map
        self.nillable = nillable
        self.derived_factory = derived_factory

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        obj = ParserUtils.parse_value(
            value=text,
            types=[self.datatype.type],
            ns_map=self.ns_map,
            format=self.datatype.format,
        )

        if obj is None and not self.nillable:
            obj = ""

        if self.datatype.wrapper:
            obj = self.datatype.wrapper(obj)

        if self.derived_factory:
            obj = self.derived_factory(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")
