from dataclasses import dataclass
from typing import Any
from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.enums import Tag


@dataclass
class AttributeEnumUnionHandler(HandlerInterface):
    """Convert classes with a single attribute derived from xs:union where all
    types are enumerations to standalone enumeration."""

    container: ContainerInterface

    def process(self, target: Class):
        """
        Merge enumeration unions attributes.

        Lookup for the source class in the local namespace or inner
        class list.
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
