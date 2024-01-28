from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils.collections import group_by
from xsdata.utils.constants import DEFAULT_ATTR_NAME


class RenameDuplicateAttributes(HandlerInterface):
    """Resolve attr name conflicts defined in the class."""

    __slots__ = ()

    def process(self, target: Class):
        """Detect and resolve naming conflicts.

        Args:
            target: The target class instance
        """
        grouped = group_by(target.attrs, key=self._attr_unique_slug)
        for items in grouped.values():
            total = len(items)
            if total == 2 and not items[0].is_enumeration:
                ClassUtils.rename_attribute_by_preference(*items)
            elif total > 1:
                ClassUtils.rename_attributes_by_index(target.attrs, items)

    @staticmethod
    def _attr_unique_slug(attr: Attr) -> str:
        return attr.slug or DEFAULT_ATTR_NAME
