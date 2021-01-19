import warnings
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.exceptions import ConverterWarning
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType
from xsdata.utils import collections


class AttributeSanitizerHandler(HandlerInterface):
    """
    Sanitize attribute types and restrictions by rules.

    Rules:
        1. Cascade class default to the text field.
        2. Reset types when roundtrip conversion of fixed value fails
    """

    @classmethod
    def process(cls, target: Class):
        cascade_default = not target.is_nillable and target.default
        for attr in target.attrs:
            if cascade_default:
                cls.cascade_default_value(target, attr)

            cls.reset_unsupported_types(attr, target.ns_map)

    @classmethod
    def cascade_default_value(cls, target: Class, attr: Attr):
        """
        Set the text xml field default value from parent.

        At this stage all flattening and merging has finished, a class
        should only have one xml text field.
        """
        if not attr.xml_type and attr.default is None:
            attr.default = target.default
            attr.fixed = target.fixed

    @classmethod
    def reset_unsupported_types(cls, attr: Attr, ns_map: Dict):
        """Reset attribute types when roundtrip conversion of fixed values
        fail."""
        is_enum = attr.is_enumeration
        if attr.default is None or not attr.fixed and not is_enum:
            return

        types = converter.sort_types(attr.native_types)
        if not types:
            return

        if attr.restrictions.tokens:
            tokens = attr.default.split()
        else:
            tokens = [attr.default]

        if is_enum and attr.restrictions.tokens and len(tokens) == 1:
            attr.restrictions.tokens = False

        fmt = attr.restrictions.format
        if not all(cls.match(token, types, ns_map, fmt) for token in tokens):
            attr.types.clear()
            attr.types.append(AttrType(qname=str(DataType.STRING), native=True))
            attr.restrictions.format = None

        attr.types = collections.unique_sequence(attr.types, key="qname")

    @classmethod
    def match(
        cls, raw: str, types: List[Type], ns_map: Dict, fmt: Optional[str]
    ) -> bool:
        """Check fixed value can be deserialized with the given list of types
        without warnings and for float/byte instances check that lexical
        representation matches original string."""

        with warnings.catch_warnings(record=True) as w:
            decoded = converter.deserialize(raw, types, ns_map=ns_map, format=fmt)

        if w and w[-1].category is ConverterWarning:
            return False

        if isinstance(decoded, float) and decoded != 0:
            encoded = converter.serialize(decoded, ns_map=ns_map, format=fmt)
            return raw.strip() == encoded

        return True
