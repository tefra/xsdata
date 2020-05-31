from collections import UserDict
from operator import methodcaller
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.codegen.handlers import AttributeEnumUnionHandler
from xsdata.codegen.handlers import AttributeGroupHandler
from xsdata.codegen.handlers import AttributeImpliedHandler
from xsdata.codegen.handlers import AttributeMergeHandler
from xsdata.codegen.handlers import AttributeMismatchHandler
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.handlers import ClassExtensionHandler
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.utils.collections import group_by

methodcaller("source_qname")

Condition = Optional[Callable]


class ClassContainer(UserDict, ContainerInterface):
    def __init__(self, data: Dict[QName, List[Class]] = None) -> None:
        super().__init__(data)

        self.processors = [
            AttributeGroupHandler(self),
            ClassExtensionHandler(self),
            AttributeEnumUnionHandler(self),
            AttributeTypeHandler(self),
            AttributeSubstitutionHandler(self),
            AttributeMergeHandler(),
            AttributeImpliedHandler(),
            AttributeMismatchHandler(),
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
                if row.status == Status.RAW:
                    self.process_class(row)

                    if condition:
                        return self.find(qname, condition)

                return row
        return None

    def process(self):
        for obj in self.iterate():
            if obj.status == Status.RAW:
                self.process_class(obj)

    def process_class(self, target: Class):
        target.status = Status.PROCESSING

        for processor in self.processors:
            processor.process(target)

        for inner in target.inner:
            if inner.status == Status.RAW:
                self.process_class(inner)

        target.status = Status.PROCESSED

    def add(self, item: Class):
        self.data.setdefault(item.source_qname(), []).append(item)

    def extend(self, items: List[Class]):
        for item in items:
            self.add(item)
