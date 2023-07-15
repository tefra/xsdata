import sys
from typing import Dict
from typing import List
from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, get_restriction_choice
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_slug
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections
from xsdata.utils.collections import group_by


class ValidateAttributesOverrides(RelativeHandlerInterface):
    """
    Check override attributes are valid.

    Steps:
        1. The attribute is a valid override, leave it alone
        2. The attribute is unnecessary remove it
        3. The attribute is an invalid override, rename one of them
    """

    __slots__ = ()

    def process(self, target: Class):
        base_attrs_map = self.base_attrs_map(target)
        for attr in list(target.attrs):
            base_attrs = base_attrs_map.get(attr.slug)

            if base_attrs:
                base_attr = base_attrs[0]
                if self.overrides(attr, base_attr):
                    self.validate_override(target, attr, base_attr)
                else:
                    self.resolve_conflict(attr, base_attr)

                # imagine the situation where the restriction in the child
                # class would choice it to either one element of the upstream
                # choice or the other upstream choice, potentially having the
                # same class name, what to retain?
                if attr.restrictions.choice is None and base_attr.restrictions.choice:
                    self.rename_choice_to_basename(attr, base_attrs[0], target)

            elif attr.is_prohibited:
                self.remove_attribute(target, attr)


    def group_fields(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""
        choice = attrs[0].restrictions.choice

        assert choice is not None

        names = []
        for attr in attrs:
            names.append(attr.local_name)

        # Must use the same self.choose_name(target, names) as create_compound_fields,
        # this does not fulfill this.
        return "_Or_".join(names)

    def rename_choice_to_basename(self, attr:Attr, base_attr:Attr, target: Class):
        base_attrs = self.base_attrs(target)
        groups = group_by(base_attrs, get_restriction_choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1 and base_attr.restrictions.choice == choice:
                attr.name = self.group_fields(target, attrs)
                break

    @classmethod
    def overrides(cls, a: Attr, b: Attr) -> bool:
        return a.xml_type == b.xml_type and a.namespace == b.namespace

    def base_attrs_map(self, target: Class) -> Dict[str, List[Attr]]:
        base_attrs = self.base_attrs(target)
        return collections.group_by(base_attrs, key=get_slug)

    @classmethod
    def validate_override(cls, target: Class, attr: Attr, source_attr: Attr):
        if source_attr.is_any_type and not attr.is_any_type:
            return

        if attr.is_list and not source_attr.is_list:
            # Hack much??? idk but Optional[str] can't override List[str]
            source_attr.restrictions.max_occurs = sys.maxsize

        if (
            attr.default == source_attr.default
            and bool_eq(attr.fixed, source_attr.fixed)
            and bool_eq(attr.mixed, source_attr.mixed)
            and bool_eq(attr.restrictions.tokens, source_attr.restrictions.tokens)
            and bool_eq(attr.restrictions.nillable, source_attr.restrictions.nillable)
            and bool_eq(attr.restrictions.is_optional, source_attr.restrictions.is_optional)
            and bool_eq(attr.restrictions.is_prohibited, source_attr.restrictions.is_prohibited)
            and bool_eq(attr.restrictions.choice, source_attr.restrictions.choice)
        ):
            cls.remove_attribute(target, attr)

    @classmethod
    def remove_attribute(cls, target: Class, attr: Attr):
        ClassUtils.remove_attribute(target, attr)
        ClassUtils.clean_inner_classes(target)

    @classmethod
    def resolve_conflict(cls, attr: Attr, source_attr: Attr):
        ClassUtils.rename_attribute_by_preference(attr, source_attr)


def bool_eq(a: Optional[bool], b: Optional[bool]) -> bool:
    return bool(a) is bool(b)
