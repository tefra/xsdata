from typing import List

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class


class AttributeEffectiveChoiceHandler(HandlerInterface):
    """Look for sequential lists and non list elements and set effective choice
    group for compound fields."""

    __slots__ = ()

    def process(self, target: Class):
        groups: List[List[Attr]] = [[]]
        for attr in target.attrs:
            # If attr is sequential and is list or the group is not empty
            if attr.restrictions.sequential and (attr.is_list or groups[-1]):
                groups[-1].append(attr)
            elif groups[-1]:
                groups.append([])

        for idx, group in enumerate(groups):
            total_lists = sum(attr.restrictions.is_list for attr in group)
            if total_lists != len(group) and total_lists > 0:
                for attr in group:
                    attr.restrictions.choice = f"effective_{idx}"
