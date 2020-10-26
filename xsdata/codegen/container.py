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
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.utils import collections
from xsdata.utils.collections import group_by
from xsdata.utils.constants import return_true

methodcaller("source_qname")


class ClassContainer(UserDict, ContainerInterface):
    def __init__(self, data: Dict[str, List[Class]] = None) -> None:
        """
        Initialize container structure and the list of process handlers.

        :params data: class map indexed by their source qualified name.
        """
        super().__init__(data)

        self.processors: List[HandlerInterface] = [
            AttributeGroupHandler(self),
            ClassExtensionHandler(self),
            AttributeEnumUnionHandler(self),
            AttributeSubstitutionHandler(self),
            AttributeTypeHandler(self),
            AttributeMergeHandler(),
            AttributeMixedContentHandler(),
            AttributeMismatchHandler(),
        ]

    @property
    def class_list(self) -> List[Class]:
        return list(self.iterate())

    @classmethod
    def from_list(cls, items: List[Class]) -> "ClassContainer":
        """Static constructor from a list of classes."""
        return cls(group_by(items, attrgetter("qname")))

    def iterate(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""
        for items in list(self.data.values()):
            yield from items

    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""
        for row in self.data.get(qname, []):
            if condition(row):
                if row.status == Status.RAW:
                    self.process_class(row)
                    return self.find(qname, condition)

                return row
        return None

    def find_inner(
        self, source: Class, name: str, condition: Callable = return_true
    ) -> Optional[Class]:
        for inner in source.inner:
            if inner.status == Status.RAW:
                self.process_class(inner)

            if inner.name == name and condition(inner):
                return inner

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

    def filter_classes(self):
        """If there is any class derived from complexType or element then
        filter classes that should be generated, otherwise leave the container
        as it is."""

        candidates = list(filter(lambda x: x.should_generate, self.iterate()))
        if candidates:
            self.data = group_by(candidates, attrgetter("qname"))

    def add(self, item: Class):
        """Add class item to the container."""
        self.data.setdefault(item.qname, []).append(item)

    def reset(self, item: Class, qname: str):
        self.data[qname].remove(item)
        self.add(item)

    def extend(self, items: List[Class]):
        """Add a list of classes the container."""
        collections.apply(items, self.add)
