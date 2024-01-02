import sys
from typing import Dict, List, Optional, Set

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class, get_slug
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.utils import collections


class ValidateAttributesOverrides(RelativeHandlerInterface):
    """Validate override and restricted attributes."""

    __slots__ = ()

    def process(self, target: Class):
        base_attrs_map = self.base_attrs_map(target)
        # We need the original class attrs before validation, in order to
        # prohibit the rest of the parent attrs later...
        restricted_attrs = {
            attr.slug for attr in target.attrs if attr.can_be_restricted()
        }
        self.validate_attrs(target, base_attrs_map)
        if target.is_restricted:
            self.prohibit_parent_attrs(target, restricted_attrs, base_attrs_map)

    @classmethod
    def prohibit_parent_attrs(
        cls,
        target: Class,
        restricted_attrs: Set[str],
        base_attrs_map: Dict[str, List[Attr]],
    ):
        """
        Prepend prohibited parent attrs to the target class.

        Reset the types and default value in order to avoid conflicts
        later.
        """
        for slug, attrs in reversed(base_attrs_map.items()):
            attr = attrs[0]
            if attr.can_be_restricted() and slug not in restricted_attrs:
                attr_restricted = attr.clone()
                attr_restricted.restrictions.max_occurs = 0
                attr_restricted.default = None
                attr_restricted.types.clear()
                target.attrs.insert(0, attr_restricted)

    @classmethod
    def validate_attrs(cls, target: Class, base_attrs_map: Dict[str, List[Attr]]):
        for attr in list(target.attrs):
            base_attrs = base_attrs_map.get(attr.slug)

            if base_attrs:
                base_attr = base_attrs[0]
                if cls.overrides(attr, base_attr):
                    cls.validate_override(target, attr, base_attr)
                else:
                    cls.resolve_conflict(attr, base_attr)
            elif attr.is_prohibited:
                cls.remove_attribute(target, attr)

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
            assert source_attr.parent is not None
            logger.warning(
                "Converting parent field `%s::%s` to a list to match child class `%s`",
                source_attr.parent.name,
                source_attr.name,
                target.name,
            )

        if (
            attr.default == source_attr.default
            and bool_eq(attr.fixed, source_attr.fixed)
            and bool_eq(attr.mixed, source_attr.mixed)
            and bool_eq(attr.restrictions.tokens, source_attr.restrictions.tokens)
            and bool_eq(attr.restrictions.nillable, source_attr.restrictions.nillable)
            and bool_eq(attr.is_prohibited, source_attr.is_prohibited)
            and bool_eq(attr.is_optional, source_attr.is_optional)
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
