from dataclasses import dataclass
from typing import Dict
from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType
from xsdata.utils import collections


@dataclass
class AttributeSanitizerHandler(HandlerInterface):
    """
    Sanitize attribute types and restrictions by rules.

    Rules:
        1. Remove inherited fields that match parent exactly
        2. Cascade class default to the text field
        3. Reset types when roundtrip conversion of fixed value fails
    """

    container: ContainerInterface

    def process(self, target: Class):
        self.cascade_default_value(target)
        self.reset_unsupported_types(target)
        self.remove_inherited_fields(target)
        self.set_effective_choices(target)

    def remove_inherited_fields(self, target: Class):
        """Compare all override fields and if they mach the parent definition
        remove them."""

        if len(target.extensions) == 1:
            source = self.container.find(target.extensions[0].type.qname)

            # All dummy extensions have been removed at this stage.
            assert source is not None

            choices = self.container.config.output.compound_fields
            for attr in list(target.attrs):
                # Quick match with attr types
                pos = collections.find(source.attrs, attr)
                if pos > -1:
                    cmp = source.attrs[pos]
                    res = attr.restrictions
                    cmp_res = cmp.restrictions
                    with_occurrences = not all((choices, res.choice, cmp_res.choice))

                    if (
                        attr.default == cmp.default
                        and attr.fixed == cmp.fixed
                        and attr.mixed == cmp.mixed
                        and res.is_compatible(cmp_res, with_occurrences)
                    ):
                        target.attrs.remove(attr)

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
    def set_effective_choices(cls, target: Class):
        """Look for sequential lists and non list elements and set effective
        choice group for compound fields."""
        groups: List[List[Attr]] = [[]]
        for attr in target.attrs:
            # If attr is sequential and is list or the group is not empty
            if attr.restrictions.sequential and (attr.is_list or groups[-1]):
                groups[-1].append(attr)
            elif groups[-1]:
                groups.append([])

        for idx, group in enumerate(groups):
            total_lists = sum(attr.restrictions.is_list for attr in group)
            if total_lists != len(group) and total_lists > 0:
                for attr in group:
                    attr.restrictions.choice = f"effective_{idx}"

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
