from typing import List

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.utils import collections


class AttributeMergeHandler(HandlerInterface):
    """Merge same type attributes and their restrictions."""

    @classmethod
    def process(cls, target: Class):
        """
        Detect same type attributes in order to merge them together with their
        restrictions.

        Two attributes are considered equal if they have the same name,
        types and namespace.
        """
        result: List[Attr] = []
        for attr in target.attrs:
            pos = collections.find(result, attr)
            existing = result[pos] if pos > -1 else None

            if not existing:
                result.append(attr)
            elif not (attr.is_attribute or attr.is_enumeration):
                existing.help = existing.help or attr.help

                min_occurs = existing.restrictions.min_occurs or 0
                max_occurs = existing.restrictions.max_occurs or 1
                attr_min_occurs = attr.restrictions.min_occurs or 0
                attr_max_occurs = attr.restrictions.max_occurs or 1

                existing.restrictions.min_occurs = min(min_occurs, attr_min_occurs)
                existing.restrictions.max_occurs = max_occurs + attr_max_occurs
                existing.fixed = False
                existing.restrictions.sequential = (
                    existing.restrictions.sequential or attr.restrictions.sequential
                )

        target.attrs = result
