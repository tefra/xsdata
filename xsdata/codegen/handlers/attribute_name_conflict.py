from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import text
from xsdata.utils.collections import group_by


class AttributeNameConflictHandler(HandlerInterface):
    """Resolve attribute name conflicts defined in the class."""

    __slots__ = ()

    def process(self, target: Class):
        """Sanitize duplicate attribute names that might exist by applying
        rename strategies."""
        grouped = group_by(target.attrs, lambda attr: text.alnum(attr.name))
        for items in grouped.values():
            total = len(items)
            if total == 2 and not items[0].is_enumeration:
                ClassUtils.rename_attribute_by_preference(*items)
            elif total > 1:
                ClassUtils.rename_attributes_by_index(target.attrs, items)
