from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.utils.namespaces import build_qname


class UnnestInnerClasses(RelativeHandlerInterface):
    """Unnest class processor."""

    __slots__ = ()

    def process(self, target: Class):
        """
        Promote enumeration classes to root classes.

        Candidates
            - Enumerations
            - All if config is enabled
        """
        for inner in list(target.inner):
            if inner.is_enumeration or self.container.config.output.unnest_classes:
                self.promote(target, inner)

    def promote(self, target: Class, inner: Class):
        target.inner.remove(inner)
        attr = self.find_forward_attr(target, inner.qname)
        if attr:
            clone = self.clone_class(inner, target.name)
            self.update_types(attr, inner.qname, clone.qname)
            self.container.add(clone)

    @classmethod
    def clone_class(cls, inner: Class, name: str) -> Class:
        clone = inner.clone()
        clone.local_type = True
        clone.qname = build_qname(inner.target_namespace, f"{name}_{inner.name}")
        return clone

    @classmethod
    def update_types(cls, attr: Attr, search: str, replace: str):
        for attr_type in attr.types:
            if attr_type.qname == search and attr_type.forward:
                attr_type.qname = replace
                attr_type.forward = False

    @classmethod
    def find_forward_attr(cls, target: Class, qname: str) -> Optional[Attr]:
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.qname == qname:
                    return attr

        return None
