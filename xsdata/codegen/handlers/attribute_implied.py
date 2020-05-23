from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag


class AttributeImpliedHandler(HandlerInterface):
    """
    Add implied attributes.

    Scenarios:
        1. Mixed content class with missing wildcard attribute

    Add an xs:anyType attribute to the given class if it supports mixed
    content and doesn't have a wildcard attribute yet.
    """

    @classmethod
    def process(cls, target: Class):
        if not target.mixed or target.has_wild_attr:
            return

        attr = Attr(
            name="content",
            local_name="content",
            index=0,
            types=[AttrType(name=DataType.ANY_TYPE.code, native=True)],
            tag=Tag.ANY,
            namespace=NamespaceType.ANY.value,
        )
        target.attrs.insert(0, attr)
