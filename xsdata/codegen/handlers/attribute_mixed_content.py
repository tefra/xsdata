import sys

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag
from xsdata.utils.collections import first


class AttributeMixedContentHandler(HandlerInterface):
    """Add/Update a wildcard field for classes that support mixed content."""

    @classmethod
    def process(cls, target: Class):
        """Add or update an existing an xs:anyType derived attribute if the
        target class supports mixed content."""

        if not target.mixed:
            return

        wildcard = first(attr for attr in target.attrs if attr.tag == Tag.ANY)

        if wildcard:
            wildcard.mixed = True
            if not wildcard.is_list:
                wildcard.restrictions.min_occurs = 0
                wildcard.restrictions.max_occurs = sys.maxsize
        else:
            attr = Attr(
                name="content",
                local_name="content",
                index=0,
                types=[AttrType(qname=DataType.ANY_TYPE.qname, native=True)],
                tag=Tag.ANY,
                mixed=True,
                namespace=NamespaceType.ANY,
                restrictions=Restrictions(min_occurs=0, max_occurs=sys.maxsize),
            )
            target.attrs.insert(0, attr)
