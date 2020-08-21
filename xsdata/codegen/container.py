from collections import UserDict
from operator import attrgetter
from operator import methodcaller
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.handlers import AttributeEnumUnionHandler
from xsdata.codegen.handlers import AttributeGroupHandler
from xsdata.codegen.handlers import AttributeMergeHandler
from xsdata.codegen.handlers import AttributeMismatchHandler
from xsdata.codegen.handlers import AttributeMixedContentHandler
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.handlers import ClassExtensionHandler
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.utils import collections
from xsdata.utils.collections import group_by

methodcaller("source_qname")

Condition = Optional[Callable]


class ClassContainer(UserDict, ContainerInterface):
    def __init__(self, data: Dict[str, List[Class]] = None) -> None:
        """
        Initialize container structure and the list of process handlers.

        :params data: class map indexed by their source qualified name.
        """
        super().__init__(data)

        self.processors = [
            AttributeGroupHandler(self),
            ClassExtensionHandler(self),
            AttributeEnumUnionHandler(self),
            AttributeTypeHandler(self),
            AttributeSubstitutionHandler(self),
            AttributeMergeHandler(),
            AttributeMixedContentHandler(),
            AttributeMismatchHandler(),
        ]

    @classmethod
    def from_list(cls, items: List[Class]) -> "ClassContainer":
        """Static constructor from a list of classes."""
        return cls(group_by(items, attrgetter("qname")))

    def iterate(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""
        for items in list(self.data.values()):
            yield from items

    def find(self, qname: str, condition: Condition = None) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""
        for row in self.data.get(qname, []):
            if not condition or condition(row):
                if row.status == Status.RAW:
                    self.process_class(row)

                    if condition:
                        return self.find(qname, condition)

                return row
        return None

    def process(self):
        """Run the process handlers for ever non processed class."""
        for obj in self.iterate():
            if obj.status == Status.RAW:
                self.process_class(obj)

    def process_class(self, target: Class):
        """Run the process handlers for the target class."""
        target.status = Status.PROCESSING

        for processor in self.processors:
            processor.process(target)

        for inner in target.inner:
            if inner.status == Status.RAW:
                self.process_class(inner)

        target.status = Status.PROCESSED

    def add(self, item: Class):
        """Add class item to the container."""
        self.data.setdefault(item.qname, []).append(item)

    def extend(self, items: List[Class]):
        """Add a list of classes the container."""
        collections.apply(items, self.add)
