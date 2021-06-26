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
from xsdata.codegen.handlers import AttributeSubstitutionHandler
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.handlers import ClassDesignateHandler
from xsdata.codegen.handlers import ClassEnumerationHandler
from xsdata.codegen.handlers import ClassExtensionHandler
from xsdata.codegen.handlers import ClassInnersHandler
from xsdata.codegen.handlers import ClassNameConflictHandler
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_qname
from xsdata.codegen.models import should_generate
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.config import GeneratorConfig
from xsdata.utils import collections
from xsdata.utils.collections import group_by
from xsdata.utils.constants import return_true


class Steps:
    FLATTEN = 10
    SANITIZE = 20
    RESOLVE = 30
    FINALIZE = 40


class ClassContainer(ContainerInterface):

    __slots__ = ("data", "processors")

    def __init__(self, config: GeneratorConfig):
        """Initialize a class container instance with its processors based on
        the the provided configuration."""
        super().__init__(config)

        self.data: Dict = {}

        self.processors = {
            Steps.FLATTEN: [
                AttributeGroupHandler(self),
                ClassExtensionHandler(self),
                ClassEnumerationHandler(self),
                AttributeSubstitutionHandler(self),
                AttributeTypeHandler(self),
                AttributeMergeHandler(),
                AttributeMixedContentHandler(),
                AttributeDefaultValidateHandler(),
            ],
            Steps.SANITIZE: [
                AttributeEffectiveChoiceHandler(),
                AttributeDefaultValueHandler(self),
            ],
            Steps.RESOLVE: [
                AttributeOverridesHandler(self),
                AttributeNameConflictHandler(),
            ],
            Steps.FINALIZE: [
                ClassInnersHandler(),
                AttributeCompoundChoiceHandler(self),
            ],
        }

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
                    self.process_class(row, Steps.FLATTEN)
                    return self.find(qname, condition)

                return row
        return None

    def find_inner(self, source: Class, qname: str) -> Class:
        inner = ClassUtils.find_inner(source, qname)
        if inner.status == Status.RAW:
            self.process_class(inner, Steps.FLATTEN)

        return inner

    def process(self):
        """
        Run all the process handlers.

        Steps
            1. Flatten extensions, attribute types
            2. Filter classes to be actually generated
            3. Sanitize attributes and extensions
            4. Resolve attributes conflicts
            5. Replace repeatable elements with compound fields
            6. Designate packages and modules
        """

        self.process_classes(Steps.FLATTEN)
        self.filter_classes()
        self.process_classes(Steps.SANITIZE)
        self.process_classes(Steps.RESOLVE)
        self.process_classes(Steps.FINALIZE)
        self.designate_classes()

    def process_classes(self, step: int) -> None:
        for obj in self:
            if obj.status < step:
                self.process_class(obj, step)

        if any(obj.status < step for obj in self):
            return self.process_classes(step)

    def process_class(self, target: Class, step: int):
        target.status = Status(step)
        for processor in self.processors.get(step, []):
            processor.process(target)

        for inner in target.inner:
            if inner.status < step:
                self.process_class(inner, step)

        target.status = Status(step + 1)

    def designate_classes(self):
        designators = [
            ClassNameConflictHandler(self),
            ClassDesignateHandler(self),
        ]

        for designator in designators:
            designator.run()

    def filter_classes(self):
        """If there is any class derived from complexType or element then
        filter classes that should be generated, otherwise leave the container
        as it is."""

        candidates = list(filter(should_generate, self))
        if candidates:
            self.data = group_by(candidates, key=get_qname)

    def add(self, item: Class):
        """Add class item to the container."""
        self.data.setdefault(item.qname, []).append(item)

    def reset(self, item: Class, qname: str):
        self.data[qname].remove(item)
        self.add(item)

    def extend(self, items: List[Class]):
        """Add a list of classes the container."""
        collections.apply(items, self.add)
