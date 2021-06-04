from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.enums import DataType


class ClassBareInnerHandler(HandlerInterface):
    """
    Search and vacuum inner classes with no attributes or a single extension.

    Cases:
        1. Removing identical overriding fields can some times leave a class
           bare with just an extension. For inner classes we can safely
           replace the forward reference with the inner extension reference.
        2. Empty nested complexContent with no restrictions or extensions,
           we can replace these references with xs:anySimpleType
    """

    __slots__ = ()

    def process(self, target: Class):
        for inner in list(target.inner):
            if not inner.attrs and len(inner.extensions) < 2:
                self.remove_inner(target, inner)

    @classmethod
    def remove_inner(cls, target: Class, inner: Class):
        target.inner.remove(inner)

        for attr in target.attrs:
            for attr_type in attr.types:

                if attr_type.forward and attr_type.qname == inner.qname:
                    attr_type.circular = False
                    attr_type.forward = False

                    if inner.extensions:
                        ext = inner.extensions[0]
                        attr_type.reference = ext.type.reference
                        attr_type.qname = ext.type.qname
                        attr_type.native = False
                    else:
                        attr_type.native = True
                        attr_type.qname = str(DataType.ANY_SIMPLE_TYPE)
                        attr_type.reference = 0
