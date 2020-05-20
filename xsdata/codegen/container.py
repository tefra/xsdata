from collections import UserDict
from operator import methodcaller
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.codegen.handlers import AttributeEnumUnionClassHandler
from xsdata.codegen.handlers import AttributeGroupClassHandler
from xsdata.codegen.handlers import AttributeImpliedClassHandler
from xsdata.codegen.handlers import AttributeMergeClassHandler
from xsdata.codegen.handlers import AttributeMismatchClassHandler
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.handlers import AttributeTypeClassHandler
from xsdata.codegen.handlers import ClassExtensionClassHandler
from xsdata.codegen.mixins import ContainerInterface
from xsdata.models.codegen import Class
from xsdata.utils.collections import group_by

methodcaller("source_qname")

Condition = Optional[Callable]


class ClassContainer(UserDict, ContainerInterface):
    def __init__(self, data: Dict[QName, List[Class]] = None) -> None:
        super().__init__(data)

        self.processors = [
            AttributeGroupClassHandler(self),
            ClassExtensionClassHandler(self),
            AttributeEnumUnionClassHandler(self),
            AttributeTypeClassHandler(self),
            AttributeSubstitutionHandler(self),
            AttributeMergeClassHandler(),
            AttributeImpliedClassHandler(),
            AttributeMismatchClassHandler(),
        ]

    @classmethod
    def from_list(cls, items: List[Class]) -> "ClassContainer":
        return cls(group_by(items, methodcaller("source_qname")))

    def iterate(self) -> Iterator[Class]:
        for items in list(self.data.values()):
            yield from items

    def find(self, qname: QName, condition: Condition = None) -> Optional[Class]:
        for row in self.data.get(qname, []):
            if not condition or condition(row):
                if not row.processed:
                    self.process_class(row)

                return row
        return None

    def process(self):
        for obj in self.iterate():
            if not obj.processed:
                self.process_class(obj)

    def process_class(self, target: Class):
        target.processed = True

        for processor in self.processors:
            processor.process(target)

        for inner in target.inner:
            if not inner.processed:
                self.process_class(inner)

    def add(self, item: Class):
        self.data.setdefault(item.source_qname(), []).append(item)

    def extend(self, items: List[Class]):
        for item in items:
            self.add(item)
