from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class


class AttributeRestrictionsHandler(HandlerInterface):
    """Sanitize attributes restrictions."""

    __slots__ = ()

    def process(self, target: Class):

        for index, attr in enumerate(target.attrs):
            self.reset_occurrences(attr)
            self.reset_sequential(target, index)

    @classmethod
    def reset_occurrences(cls, attr: Attr):
        """Sanitize attribute required flag by comparing the min/max
        occurrences restrictions."""
        restrictions = attr.restrictions
        min_occurs = restrictions.min_occurs or 0
        max_occurs = restrictions.max_occurs or 0

        if attr.is_attribute:
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif attr.is_tokens:
            restrictions.required = None
            if max_occurs <= 1:
                restrictions.min_occurs = None
                restrictions.max_occurs = None
        elif attr.xml_type is None or min_occurs == max_occurs == 1:
            restrictions.required = True
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif min_occurs == 0 and max_occurs < 2:
            restrictions.required = None
            restrictions.min_occurs = None
            restrictions.max_occurs = None
            attr.default = None
            attr.fixed = False
        else:  # max_occurs > 1
            restrictions.min_occurs = min_occurs
            restrictions.required = None
            attr.fixed = False

        if attr.default or attr.fixed or attr.restrictions.nillable:
            restrictions.required = None

    @classmethod
    def reset_sequential(cls, target: Class, index: int):
        """Reset the attribute at the given index if it has no siblings with
        the sequential restriction."""

        attr = target.attrs[index]
        before = target.attrs[index - 1] if index - 1 >= 0 else None
        after = target.attrs[index + 1] if index + 1 < len(target.attrs) else None

        if not attr.is_list:
            attr.restrictions.sequential = False

        if (
            not attr.restrictions.sequential
            or (before and before.restrictions.sequential)
            or (after and after.restrictions.sequential and after.is_list)
        ):
            return

        attr.restrictions.sequential = False
