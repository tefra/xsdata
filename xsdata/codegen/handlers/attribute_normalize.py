from typing import Any
from typing import Dict

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType
from xsdata.utils import collections


class AttributeNormalizeHandler(HandlerInterface):
    """
    Validate attribute types against default values.

    Rules:
        1. Cascade class default to the text field
        2. Reset types when roundtrip conversion of fixed value fails
    """

    __slots__ = ()

    def process(self, target: Class):
        for attr in target.attrs:
            if attr.xml_type is None:
                self.cascade_properties(
                    attr, target.nillable, target.fixed, target.default
                )

            if attr.default is not None:
                self.reset_unsupported_types(attr, target.ns_map)
            elif object in attr.native_types and not attr.is_list:
                attr.restrictions.min_occurs = 0

    @classmethod
    def cascade_properties(
        cls, attr: Attr, nillable: bool, fixed: bool, default_value: Any
    ):
        """Cascade xsd:element properties to the default value field of the
        class."""
        if nillable:
            attr.restrictions.nillable = True

        if default_value and attr.default is None:
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
