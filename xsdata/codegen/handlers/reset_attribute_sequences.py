from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_restriction_sequence
from xsdata.utils import collections


class ResetAttributeSequences(HandlerInterface):
    """Validate if fields are part of a repeatable sequence otherwise reset the
    sequence flag."""

    __slots__ = ()

    def process(self, target: Class):
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
        seq = attr.restrictions.sequence
        if seq:
            for path in attr.restrictions.path:
                if path[0] == "s" and path[1] == seq:
                    return path[3] > 1 if path else False

                if path[3] > 1:
                    return True

        return False
