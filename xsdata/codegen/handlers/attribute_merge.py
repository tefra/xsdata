from typing import List

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections


class AttributeMergeHandler(HandlerInterface):
    """Merge same type attributes and their restrictions."""

    __slots__ = ()

    @classmethod
    def process(cls, target: Class):
        """
        Detect same type attributes in order to merge them together with their
        restrictions.

        Two attributes are considered equal if they have the same name,
        tag and namespace.
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
                e_res.sequential = a_res.sequential or e_res.sequential
                existing.fixed = False
                existing.types.extend(attr.types)

        target.attrs = result
        ClassUtils.cleanup_class(target)
