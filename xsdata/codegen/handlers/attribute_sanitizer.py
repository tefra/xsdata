from dataclasses import dataclass
from typing import Dict
from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType
from xsdata.utils import collections
from xsdata.utils.text import alnum


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

        for extension in target.extensions:
            self.process_inherited_fields(target, extension)

        self.set_effective_choices(target)

    def process_inherited_fields(self, target: Class, extension: Extension):
        source = self.container.find(extension.type.qname)
        assert source is not None

        for attr in list(target.attrs):
            search = alnum(attr.name)
            source_attr = collections.first(
                source_attr
                for source_attr in source.attrs
                if alnum(source_attr.name) == search
            )

            if not source_attr:
                continue

            if attr.tag == source_attr.tag:
                self.process_inherited_field(target, attr, source_attr)
            else:
                ClassUtils.rename_attribute_by_preference(attr, source_attr)

        for extension in source.extensions:
            self.process_inherited_fields(target, extension)

    def process_inherited_field(self, target: Class, attr: Attr, source_attr: Attr):
        choices = self.container.config.output.compound_fields
        with_occurrences = not all(
            (choices, attr.restrictions.choice, source_attr.restrictions.choice)
        )

        if (
            attr.default == source_attr.default
            and attr.fixed == source_attr.fixed
            and attr.mixed == source_attr.mixed
            and attr.restrictions.is_compatible(
                source_attr.restrictions, with_occurrences
            )
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
