from typing import List

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections


class MergeAttributes(HandlerInterface):
    """Merge same type attr and their restrictions."""

    __slots__ = ()

    @classmethod
    def process(cls, target: Class):
        """Detect and process duplicate attributes.

        Cases:
            - Enumeration: remove duplicates
            - Otherwise: merge attrs and

        Args:
            target: The target class instance
        """
        if target.is_enumeration:
            cls.filter_duplicate_attrs(target)
        else:
            cls.merge_duplicate_attrs(target)

    @classmethod
    def filter_duplicate_attrs(cls, target: Class):
        """Removes duplicate attrs.

        Args:
            target: The target class instance
        """
        attrs = collections.unique_sequence(target.attrs, key="default")
        target.attrs = attrs

    @classmethod
    def merge_duplicate_attrs(cls, target: Class):
        """Find duplicate attrs and merge them.

        In order for two attrs to be considered duplicates,
        they must have the same name, namespace and tag.

        Args:
            target: The target class instance
        """
        result: List[Attr] = []
        for attr in target.attrs:
            pos = collections.find(result, attr)
            existing = result[pos] if pos > -1 else None

            if not existing:
                result.append(attr)
            elif not (attr.is_attribute or attr.is_enumeration):
                existing.help = existing.help or attr.help

                e_res = existing.restrictions
                a_res = attr.restrictions

                min_occurs = e_res.min_occurs or 0
                max_occurs = e_res.max_occurs or 1
                attr_min_occurs = a_res.min_occurs or 0
                attr_max_occurs = a_res.max_occurs or 1

                e_res.min_occurs = min(min_occurs, attr_min_occurs)
                e_res.max_occurs = max_occurs + attr_max_occurs

                if a_res.sequence is not None:
                    e_res.sequence = a_res.sequence

                existing.fixed = False
                existing.types.extend(attr.types)

        target.attrs = result
        ClassUtils.cleanup_class(target)
