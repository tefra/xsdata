from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Class


class AddNillableTextOverrides(RelativeHandlerInterface):
    """Override inherited text attrs for nillable classes.

    A nillable element accepts nil content, even if its base type
    requires a text value. The parser binds the nil text as None,
    so the class needs its own nillable copy of the text attr.
    """

    __slots__ = ()

    def process(self, target: Class) -> None:
        """Process entrypoint for classes.

        Skip classes that are not nillable or have their own text
        attr, the attr types processor cascades the flag to them.

        Args:
            target: The target class instance
        """
        if not target.nillable or any(x.xml_type is None for x in target.attrs):
            return

        for attr in self.base_attrs(target):
            if attr.xml_type is None:
                if not attr.is_nillable:
                    clone = attr.clone()
                    clone.restrictions.nillable = True
                    target.attrs.insert(0, clone)
                return
