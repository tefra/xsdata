from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, Class

ALL = "a"
GROUP = "g"
SEQUENCE = "s"
CHOICE = "c"


class CalculateAttributePaths(HandlerInterface):
    """Calculate min/max occurs and sequence/choice/group from the schema path."""

    __slots__ = ()

    @classmethod
    def process(cls, target: Class):
        """Calculating the class attrs restrictions by their schema path.

        For each attr calculate the min/max occurs and set the
        sequence/choice/group reference id. Ignore attrs derived
        from xs:attribute and xs:enumeration as these are not affected
        by the parent element.

        Args:
            target: The target class instance
        """
        for attr in target.attrs:
            if (
                attr.restrictions.path
                and not attr.is_attribute
                and not attr.is_enumeration
            ):
                cls.process_attr_path(attr)

    @classmethod
    def process_attr_path(cls, attr: Attr):
        """Entrypoint for processing a class attr.

        Example path:
            ("s", 1, 1, 1), ("s", 2, 1, 2), ("c", 3, 0, 10)  ->
            sequence:1 with min=1 and max_occurs=1
            sequence:2 with min=1 and max_occurs=2
            choice:3 with min=0 and max_occurs=10

        Steps:
            - Every attr starts with a min/max occurs equal to one.
            - For every parent container multiply the min/max occurs
            - Set the sequence/choice/group reference ids as you go along

        Args:
            attr: The attr of the class to check and process
        """
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
