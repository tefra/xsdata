from typing import Iterator

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.models.enums import DataType
from xsdata.utils import collections
from xsdata.utils.namespaces import build_qname


class VacuumInnerClasses(HandlerInterface):
    """
    Cleanup nested classes.

    Search and vacuum inner classes with no attributes or a single extension or
    rename inner classes that have the same name as the outer/parent class.

    Cases:
        1. Filter duplicate inner classes
        2. Removing identical overriding fields can some times leave a class
           bare with just an extension. For inner classes we can safely
           replace the forward reference with the inner extension reference.
        3. Empty nested complexContent with no restrictions or extensions,
           we can replace these references with xs:anySimpleType
    """

    __slots__ = ()

    def process(self, target: Class):
        target.inner = collections.unique_sequence(target.inner, key="qname")
        for inner in list(target.inner):
            if not inner.attrs and len(inner.extensions) < 2:
                self.remove_inner(target, inner)
            elif inner.qname == target.qname:
                self.rename_inner(target, inner)

    @classmethod
    def remove_inner(cls, target: Class, inner: Class):
        target.inner.remove(inner)

        for attr_type in cls.find_attr_types(target, inner.qname):
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

    @classmethod
    def rename_inner(cls, target: Class, inner: Class):
        namespace = inner.target_namespace
        old_qname = inner.qname
        inner.qname = build_qname(namespace, f"{inner.name}_Inner")

        for attr_type in cls.find_attr_types(target, old_qname):
            attr_type.qname = inner.qname

    @classmethod
    def find_attr_types(cls, target: Class, qname: str) -> Iterator[AttrType]:
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.qname == qname:
                    yield attr_type

            for choice in attr.choices:
                for choice_type in choice.types:
                    if choice_type.forward and choice_type.qname == qname:
                        yield choice_type
