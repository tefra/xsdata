from collections import defaultdict

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Class


class ResetAttributeSequenceNumbers(RelativeHandlerInterface):
    """
    Reset attributes sequence numbers.

    Until now all sequence numbers point to the id of sequence class!!!
    """

    __slots__ = ()

    def process(self, target: Class):
        groups = defaultdict(list)
        for attr in target.attrs:
            if attr.restrictions.sequence:
                groups[attr.restrictions.sequence].append(attr)

        if groups:
            next_sequence_number = self.find_next_sequence_number(target)
            for attrs in groups.values():
                for attr in attrs:
                    attr.restrictions.sequence = next_sequence_number

                next_sequence_number += 1

    def find_next_sequence_number(self, target: Class) -> int:
        return (
            max(
                (attr.restrictions.sequence or 0 for attr in self.base_attrs(target)),
                default=0,
            )
            + 1
        )
