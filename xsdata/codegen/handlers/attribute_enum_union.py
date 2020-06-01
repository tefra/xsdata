from dataclasses import dataclass
from typing import Any
from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.enums import Tag


@dataclass
class AttributeEnumUnionHandler(HandlerInterface):
    """Convert simple types with a single field which is a union of enums to a
    standalone enumeration."""

    container: ContainerInterface

    def process(self, target: Class):

        if len(target.attrs) == 1 and target.attrs[0].tag == Tag.UNION:
            enums: List[Any] = []
            attr = target.attrs[0]
            for attr_type in attr.types:
                if attr_type.forward:
                    enums.extend(target.inner)
                elif not attr_type.native:
                    qname = target.source_qname(attr_type.name)
                    enums.append(self.container.find(qname))
                else:
                    enums.append(None)

            merge = all(isinstance(x, Class) and x.is_enumeration for x in enums)
            if merge:
                target.attrs.clear()
                target.inner.clear()
                for enum in enums:
                    target.attrs.extend(x.clone() for x in enum.attrs)
