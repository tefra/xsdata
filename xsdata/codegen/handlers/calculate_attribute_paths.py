from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class


ALL = "a"
GROUP = "g"
SEQUENCE = "s"
CHOICE = "c"


class CalculateAttributePaths(HandlerInterface):
    """Calculate min/max occurs and sequence/choice/group from the schema
    path."""

    __slots__ = ()

    @classmethod
    def process(cls, target: Class):
        for attr in target.attrs:
            if (
                attr.restrictions.path
                and not attr.is_attribute
                and not attr.is_enumeration
            ):
                cls.process_attr_path(attr)

    @classmethod
    def process_attr_path(cls, attr: Attr):
        min_occurs = 1
        max_occurs = 1
        for path in attr.restrictions.path:
            name, index, mi, ma = path

            if name == SEQUENCE:
                if not attr.restrictions.sequence:
                    attr.restrictions.sequence = index
            elif name == CHOICE:
                if not attr.restrictions.choice:
                    attr.restrictions.choice = index
            elif name == GROUP:
                attr.restrictions.group = index
            else:
                pass

            min_occurs *= mi
            max_occurs *= ma

        assert attr.restrictions.min_occurs is not None
        assert attr.restrictions.max_occurs is not None

        attr.restrictions.min_occurs *= min_occurs
        attr.restrictions.max_occurs *= max_occurs
