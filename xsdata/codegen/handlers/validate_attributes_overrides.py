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
        """Process entrypoint for classes.

        - Validate override attrs
        - Add restricted attrs

        Args:
            target: The target class instance
        """
        base_attrs_map = self.base_attrs_map(target)
        # We need the original class attrs before validation, in order to
        # prohibit the rest of the parent attrs later...
        explicit_attrs = {
            attr.slug for attr in target.attrs if attr.can_be_restricted()
        }
        self.validate_attrs(target, base_attrs_map)
        if target.is_restricted:
            self.prohibit_parent_attrs(target, explicit_attrs, base_attrs_map)

    @classmethod
    def prohibit_parent_attrs(
        cls,
        target: Class,
        explicit_attrs: Set[str],
        base_attrs_map: Dict[str, List[Attr]],
    ):
        """Prepend prohibited parent attrs to the target class.

        Prepend the parent prohibited attrs and reset their
        types and default values in order to avoid conflicts
        later.

        Args:
            target: The target class instance
            explicit_attrs: The list of explicit attrs in the class
            base_attrs_map: A mapping of qualified names to lists of parent attrs

        """
        for slug, attrs in reversed(base_attrs_map.items()):
            attr = attrs[0]
            if attr.can_be_restricted() and slug not in explicit_attrs:
                attr_restricted = attr.clone()
                attr_restricted.restrictions.max_occurs = 0
                attr_restricted.default = None
                attr_restricted.types.clear()
                target.attrs.insert(0, attr_restricted)

    @classmethod
    def validate_attrs(cls, target: Class, base_attrs_map: Dict[str, List[Attr]]):
        """Validate overriding attrs.

        Cases:
            - Overriding attr, either remove it or update parent attr
            - Duplicate names, resolve conflicts
            - Remove prohibited attrs.


        Args:
            target: The target class instance
            base_attrs_map: A mapping of qualified names to lists of parent attrs
        """
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
        """Override attrs must belong to the same xml type and namespace.

        Args:
            a: The first attr
            b: The second attr

        Returns:
            The bool result.
        """
        return a.xml_type == b.xml_type and a.namespace == b.namespace

    def base_attrs_map(self, target: Class) -> Dict[str, List[Attr]]:
        """Create a mapping of qualified names to lists of parent attrs.

        Args:
            target: The target class instance

        Returns:
            A mapping of qualified names to lists of parent attrs.
        """
        base_attrs = self.base_attrs(target)
        return collections.group_by(base_attrs, key=get_slug)

    @classmethod
    def validate_override(cls, target: Class, child_attr: Attr, parent_attr: Attr):
        """Validate the override will not break mypy type checking.

        - Ignore wildcard attrs.
        - If child is a list and parent isn't convert parent to list
        - If restrictions are the same we can safely remove override attr

        Args:
            target: The target class instance
            child_attr: The child attr
            parent_attr: The parent attr
        """
        if parent_attr.is_any_type and not child_attr.is_any_type:
            return

        if child_attr.is_list and not parent_attr.is_list:
            # Hack much??? idk but Optional[str] can't override List[str]
            parent_attr.restrictions.max_occurs = sys.maxsize
            assert parent_attr.parent is not None
            logger.warning(
                "Converting parent field `%s::%s` to a list to match child class `%s`",
                parent_attr.parent,
                parent_attr.name,
                target.name,
            )

        if (
            child_attr.default == parent_attr.default
            and _bool_eq(child_attr.fixed, parent_attr.fixed)
            and _bool_eq(child_attr.mixed, parent_attr.mixed)
            and _bool_eq(
                child_attr.restrictions.tokens, parent_attr.restrictions.tokens
            )
            and _bool_eq(
                child_attr.restrictions.nillable, parent_attr.restrictions.nillable
            )
            and _bool_eq(child_attr.is_prohibited, parent_attr.is_prohibited)
            and _bool_eq(child_attr.is_optional, parent_attr.is_optional)
        ):
            cls.remove_attribute(target, child_attr)

    @classmethod
    def remove_attribute(cls, target: Class, attr: Attr):
        """Safely remove attr.

        The search is done with the reference id for safety,
        of removing attrs with same name. If the attr has
        a forward reference, the inner class will also be removed
        if it's unused!

        Args:
            target: The target class instance
            attr: The attr to remove

        """
        ClassUtils.remove_attribute(target, attr)
        ClassUtils.clean_inner_classes(target)

    @classmethod
    def resolve_conflict(cls, child_attr: Attr, parent_attr: Attr):
        """Rename the child or parent attr.

        Args:
            child_attr: The child attr instance
            parent_attr: The  parent attr instance
        """
        ClassUtils.rename_attribute_by_preference(child_attr, parent_attr)


def _bool_eq(a: Optional[bool], b: Optional[bool]) -> bool:
    return bool(a) is bool(b)
