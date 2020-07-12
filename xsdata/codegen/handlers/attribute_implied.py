from lxml.etree import QName

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag


class AttributeImpliedHandler(HandlerInterface):
    """Add attributes to classes that are implied from the class other
    properties."""

    @classmethod
    def process(cls, target: Class):
        """Add an xs:anyType attribute to the given class if it supports mixed
        content and doesn't have a wildcard attribute yet."""

        if not target.mixed or target.has_wild_attr:
            return

        attr = Attr(
            name="content",
            local_name="content",
            types=[
                AttrType(
                    qname=QName(Namespace.XS.uri, DataType.ANY_TYPE.code), native=True,
                )
            ],
            tag=Tag.ANY,
            namespace=NamespaceType.ANY.value,
        )
        target.attrs.insert(0, attr)
