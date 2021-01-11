from dataclasses import dataclass
from typing import Any
from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname


@dataclass
class ClassEnumerationHandler(HandlerInterface):
    """Enumeration class processor."""

    container: ContainerInterface

    def process(self, target: Class):
        """
        Process class receiver.

        Steps:
            1. Filter attrs not derived from xs:enumeration
            2. Flatten attrs derived from xs:union of enumerations
            3. Promote inner enumeration classes to root classes
        """
        self.filter(target)
        self.flatten(target)
        self.promote(target)

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

    def promote(self, target: Class):
        """
        Promote inner enumeration classes to root classes.

        Steps:
            1. Find inner enumerations
            2. Clone and update their qualified name
            3. Update attributes types
        """
        for inner in list(target.inner):
            if inner.is_enumeration:
                target.inner.remove(inner)
                clone = self.clone_enumeration(inner, target.name)
                self.container.add(clone)
                for attr in target.attrs:
                    self.update_types(attr, inner.qname, clone.qname)

    @classmethod
    def clone_enumeration(cls, inner: Class, name: str) -> Class:
        clone = inner.clone()
        clone.qname = build_qname(clone.target_namespace, f"{name}_{clone.name}")
        return clone

    @classmethod
    def update_types(cls, attr: Attr, search: str, replace: str):
        for attr_type in attr.types:
            if attr_type.qname == search and attr_type.forward:
                attr_type.qname = replace
                attr_type.forward = False
