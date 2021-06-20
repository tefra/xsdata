from operator import attrgetter
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.handlers import AttributeCompoundChoiceHandler
from xsdata.codegen.handlers import AttributeDefaultValidateHandler
from xsdata.codegen.handlers import AttributeDefaultValueHandler
from xsdata.codegen.handlers import AttributeEffectiveChoiceHandler
from xsdata.codegen.handlers import AttributeGroupHandler
from xsdata.codegen.handlers import AttributeMergeHandler
from xsdata.codegen.handlers import AttributeMixedContentHandler
from xsdata.codegen.handlers import AttributeNameConflictHandler
from xsdata.codegen.handlers import AttributeOverridesHandler
from xsdata.codegen.handlers import AttributeRestrictionsHandler
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.handlers import ClassDesignateHandler
from xsdata.codegen.handlers import ClassEnumerationHandler
from xsdata.codegen.handlers import ClassExtensionHandler
from xsdata.codegen.handlers import ClassInnersHandler
from xsdata.codegen.handlers import ClassNameConflictHandler
from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.config import GeneratorConfig
from xsdata.utils import collections
from xsdata.utils.collections import group_by
from xsdata.utils.constants import return_true


class ClassContainer(ContainerInterface):

    __slots__ = ("data", "pre_processors", "post_processors", "collection_processors")

    def __init__(self, config: GeneratorConfig):
        """Initialize a class container instance with its processors based on
        the the provided configuration."""
        super().__init__(config)

        self.data: Dict = {}
        self.pre_processors: List[HandlerInterface] = [
            AttributeGroupHandler(self),
            ClassExtensionHandler(self),
            ClassEnumerationHandler(self),
            AttributeSubstitutionHandler(self),
            AttributeTypeHandler(self),
            AttributeMergeHandler(),
            AttributeMixedContentHandler(),
            AttributeDefaultValidateHandler(),
            AttributeOverridesHandler(self),
            AttributeEffectiveChoiceHandler(),
        ]

        self.post_processors: List[HandlerInterface] = [
            AttributeDefaultValueHandler(self),
            AttributeRestrictionsHandler(),
            AttributeNameConflictHandler(),
            ClassInnersHandler(),
        ]

        self.collection_processors: List[ContainerHandlerInterface] = [
            ClassNameConflictHandler(self),
            ClassDesignateHandler(self),
        ]

        if self.config.output.compound_fields:
            self.post_processors.insert(0, AttributeCompoundChoiceHandler(self))

    def __iter__(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""
        for items in list(self.data.values()):
            yield from items

    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""
        for row in self.data.get(qname, []):
            if condition(row):
                if row.status == Status.RAW:
                    self.pre_process_class(row)
                    return self.find(qname, condition)

                return row
        return None

    def find_inner(self, source: Class, qname: str) -> Class:
        inner = ClassUtils.find_inner(source, qname)
        if inner.status == Status.RAW:
            self.pre_process_class(inner)

        return inner

    def process(self):
        """
        Run all the process handlers.

        Steps
            1. Run all pre-selection handlers
            2. Filter classes to be actually generated
            3. Run all post-selection handlers
            4. Resolve any naming conflicts
            5. Assign packages and modules
        """
        for obj in self:
            if obj.status == Status.RAW:
                self.pre_process_class(obj)

        self.filter_classes()

        for obj in self:
            self.post_process_class(obj)

        for handler in self.collection_processors:
            handler.run()

    def pre_process_class(self, target: Class):
        """Run the pre process handlers for the target class."""
        target.status = Status.PROCESSING

        for processor in self.pre_processors:
            processor.process(target)

        # We go top to bottom because it's easier to handle circular
        # references.
        for inner in target.inner:
            if inner.status == Status.RAW:
                self.pre_process_class(inner)

        target.status = Status.PROCESSED

    def post_process_class(self, target: Class):
        """Run the post process handlers for the target class."""
        for inner in target.inner:
            self.post_process_class(inner)

        for processor in self.post_processors:
            processor.process(target)

    def filter_classes(self):
        """If there is any class derived from complexType or element then
        filter classes that should be generated, otherwise leave the container
        as it is."""

        candidates = list(filter(attrgetter("should_generate"), self))
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
