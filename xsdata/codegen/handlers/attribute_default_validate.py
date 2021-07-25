from typing import Any
from typing import Dict

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType
from xsdata.utils import collections


class AttributeDefaultValidateHandler(HandlerInterface):
    """
    Validate attribute types against default values.

    Rules:
        1. Cascade class default to the text field
        2. Reset types when roundtrip conversion of fixed value fails
    """

    __slots__ = ()

    def process(self, target: Class):
        is_nillable = target.is_nillable
        default_value = target.default
        fixed = target.fixed
        ns_map = target.ns_map
        for attr in target.attrs:
            if is_nillable:
                self.set_optional(attr)
            elif default_value:
                self.set_default_value(attr, default_value, fixed)

            self.reset_unsupported_types(attr, ns_map)

    @classmethod
    def set_optional(cls, attr: Attr):
        if attr.xml_type == XmlType.ELEMENT:
            attr.restrictions.min_occurs = 0
            attr.default = None
            attr.fixed = False

    @classmethod
    def set_default_value(cls, attr: Attr, default_value: Any, fixed: bool):
        """
        Set the text xml field default value from parent.

        At this stage all flattening and merging has finished only one
        xml text field should exists.
        """
        if not attr.xml_type and attr.default is None:
            attr.default = default_value
            attr.fixed = fixed

    @classmethod
    def reset_unsupported_types(cls, attr: Attr, ns_map: Dict):
        if not cls.validate_default_value(attr, ns_map):
            attr.types.clear()
            attr.types.append(AttrType(qname=str(DataType.STRING), native=True))
            attr.restrictions.format = None

        attr.types = collections.unique_sequence(attr.types, key="qname")

    @classmethod
    def validate_default_value(cls, attr: Attr, ns_map: Dict) -> bool:
        """Reset attribute types when roundtrip conversion of fixed values
        fail."""
        is_enum = attr.is_enumeration
        if attr.default is None or not attr.fixed and not is_enum:
            return True

        types = converter.sort_types(attr.native_types)
        if not types:
            return True

        if attr.restrictions.tokens:
            tokens = attr.default.split()
        else:
            tokens = [attr.default]

        if is_enum and attr.restrictions.tokens and len(tokens) == 1:
            attr.restrictions.tokens = False

        return all(
            converter.test(token, types, ns_map=ns_map, format=attr.restrictions.format)
            for token in tokens
        )
