import sys

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag


class ProcessMixedContentClass(HandlerInterface):
    """
    Mixed content handler.

    If the target class supports mixed content, a new wildcard attr will
    replace the originals except any attributes. All the previous attrs
    derived from  xs:element will be moved as choices for the new
    content attr.
    """

    __slots__ = ()

    def process(self, target: Class):
        if not target.is_mixed:
            return

        attrs = []
        choices = []
        for attr in list(target.attrs):
            if attr.is_attribute:
                attrs.append(attr)
            elif attr.tag != Tag.ANY:
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
