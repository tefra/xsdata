from collections import defaultdict

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Class


class ResetAttributeSequenceNumbers(RelativeHandlerInterface):
    """Reset attrs sequence numbers.

    The sequence numbers are the ids of xs:sequence elements, because
    up until now it was important to determine which child/parent
    attrs belong to different sequence numbers.

    Before we generate the classes let's reset them to simple auto
    increment numbers per class.
    """

    __slots__ = ()

    def process(self, target: Class):
        """Process entrypoint for classes.

        Args:
            target: The target class instance
        """
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
        """Calculate the next sequence number from the base classes.

        Args:
            target: The target class instance

        Returns:
            The next sequence number
        """
        base_attrs = self.base_attrs(target)
        sequences = (attr.restrictions.sequence or 0 for attr in base_attrs)
        max_sequence = max(sequences, default=0)
        return max_sequence + 1
