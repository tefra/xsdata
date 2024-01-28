import sys

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class, Restrictions
from xsdata.models.enums import DataType, NamespaceType, Tag


class ProcessMixedContentClass(HandlerInterface):
    """Mixed content handler."""

    __slots__ = ()

    def process(self, target: Class):
        """Add a wildcard attr if the class supports mixed content.

        All other elements will be moved as the wildcard attr choices.

        Args:
            target: Tha target class instance
        """
        if not target.is_mixed:
            return

        attrs = []
        choices = []
        for attr in list(target.attrs):
            if attr.is_attribute:
                attrs.append(attr)
            elif not attr.is_any_type:
                choice = attr.clone()
                choice.restrictions.min_occurs = None
                choice.restrictions.max_occurs = None
                choice.restrictions.sequence = None
                choices.append(choice)

        wildcard = Attr(
            name="content",
            types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
            tag=Tag.ANY,
            mixed=True,
            choices=choices,
            namespace=NamespaceType.ANY_NS,
            restrictions=Restrictions(min_occurs=0, max_occurs=sys.maxsize),
        )
        attrs.append(wildcard)

        target.attrs = attrs
