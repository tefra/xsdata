import sys
from typing import Dict
from typing import List
from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, Restrictions
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_slug
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections


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
        original_attrs = []
        if len([ext for ext in target.extensions if ext.tag == 'Restriction']) > 0:
            original_attrs = list(target.attrs)

        base_attrs_map = self.base_attrs_map(target)
        for attr in list(target.attrs):
            base_attrs = base_attrs_map.get(attr.slug)

            if base_attrs:
                base_attr = base_attrs[0]
                if self.overrides(attr, base_attr):
                    self.validate_override(target, attr, base_attr)
                else:
                    self.resolve_conflict(attr, base_attr)
            elif attr.is_prohibited:
                self.remove_attribute(target, attr)

        if len([ext for ext in target.extensions if ext.tag == 'Restriction']) > 0:
            # What we want here is to check the restriction.attrs against base_attrs_map
            # restriction_attrs = {a.slug: a for a in self.base_attrs(self.container.find(target.extensions[0].type.qname))}
            restriction_attrs = {a.slug: a for a in original_attrs}
            all_attrs = dict(base_attrs_map.items())
            for slug, attr in all_attrs.items():
                if not attr[0].is_attribute and slug not in restriction_attrs:
                    attr_new = Attr(tag=attr[0].tag, name=attr[0].name, index=attr[0].index, restrictions=Restrictions(is_null=True))
                    target.attrs.append(attr_new)

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
