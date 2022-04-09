from typing import Any
from typing import List

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.enums import Tag


class SanitizeEnumerationClass(RelativeHandlerInterface):
    """Enumeration class processor."""

    __slots__ = ()

    def process(self, target: Class):
        """
        Process class receiver.

        Steps:
            1. Filter attrs not derived from xs:enumeration
            2. Flatten attrs derived from xs:union of enumerations
        """
        self.filter(target)
        self.flatten(target)

    @classmethod
    def filter(cls, target: Class):
        """Filter attrs not derived from xs:enumeration if there are any
        xs:enumeration attrs."""
        enumerations = [attr for attr in target.attrs if attr.is_enumeration]
        if enumerations:
            target.attrs = enumerations

    def flatten(self, target: Class):
        """
        Flatten attrs derived from xs:union of enumeration classes.

        Find the enumeration classes and merge all of their members in
        the target class.
        """
        if len(target.attrs) != 1 or target.attrs[0].tag != Tag.UNION:
            return

        enums: List[Any] = []
        for attr_type in target.attrs[0].types:
            if attr_type.forward:
                enums.extend(target.inner)
            elif not attr_type.native:
                enums.append(self.container.find(attr_type.qname))
            else:
                enums.append(None)

        merge = all(isinstance(x, Class) and x.is_enumeration for x in enums)
        if merge:
            target.attrs.clear()
            target.inner.clear()

            target.attrs.extend(attr.clone() for enum in enums for attr in enum.attrs)
