from typing import Dict

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
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
        self.cascade_default_value(target)
        self.reset_unsupported_types(target)

    @classmethod
    def cascade_default_value(cls, target: Class):
        """
        Set the text xml field default value from parent.

        At this stage all flattening and merging has finished only one
        xml text field should exists.
        """
        if not target.is_nillable and target.default is not None:
            for attr in target.attrs:
                if not attr.xml_type and attr.default is None:
                    attr.default = target.default
                    attr.fixed = target.fixed

    @classmethod
    def reset_unsupported_types(cls, target: Class):
        for attr in target.attrs:

            if not cls.validate_default_value(attr, target.ns_map):
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
