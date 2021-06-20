import sys
from operator import attrgetter
from typing import Dict
from typing import List

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections


class AttributeOverridesHandler(RelativeHandlerInterface):
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
                if attr.tag == base_attr.tag:
                    self.validate_override(target, attr, base_attr)
                else:
                    self.resolve_conflict(attr, base_attr)

    def base_attrs_map(self, target: Class) -> Dict[str, List[Attr]]:
        base_attrs = self.base_attrs(target)
        return collections.group_by(base_attrs, key=attrgetter("slug"))

    @classmethod
    def validate_override(cls, target: Class, attr: Attr, source_attr: Attr):
        if attr.is_list and not source_attr.is_list:
            # Hack much??? idk but Optional[str] can't override List[str]
            source_attr.restrictions.max_occurs = sys.maxsize

        if (
            attr.default == source_attr.default
            and attr.fixed == source_attr.fixed
            and attr.mixed == source_attr.mixed
            and attr.restrictions.is_compatible(source_attr.restrictions)
        ):
            ClassUtils.remove_attribute(target, attr)

    @classmethod
    def resolve_conflict(cls, attr: Attr, source_attr: Attr):
        ClassUtils.rename_attribute_by_preference(attr, source_attr)
