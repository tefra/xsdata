from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, Class, get_restriction_sequence
from xsdata.utils import collections


class ResetAttributeSequences(HandlerInterface):
    """Inspect a class for non-repeatable choices and unset the sequence number."""

    __slots__ = ()

    def process(self, target: Class):
        """Process entrypoint for classes.

        Reset Cases:
            - A sequence only contains one attr
            - The sequence includes attrs with max_occurs==1

        Args:
            target: The target class instance
        """
        groups = collections.group_by(target.attrs, get_restriction_sequence)
        for sequence, attrs in groups.items():
            if not sequence:
                continue

            if len(attrs) == 1:
                attrs[0].restrictions.sequence = None
            else:
                for attr in attrs:
                    if not self.is_repeatable_sequence(attr):
                        attr.restrictions.sequence = None

    @classmethod
    def is_repeatable_sequence(cls, attr: Attr) -> bool:
        """Determine if the given attr is repeatable.

        Repeatable means max_occurs > 1

        Args:
            attr: The attr instance

        Returns:
            The bool result
        """
        seq = attr.restrictions.sequence
        if seq:
            for path in attr.restrictions.path:
                if path[0] == "s" and path[1] == seq:
                    return path[3] > 1 if path else False

                if path[3] > 1:
                    return True

        return False
