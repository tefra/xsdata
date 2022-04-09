from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.handlers import AddAttributeSubstitutions
from xsdata.codegen.handlers import CreateCompoundFields
from xsdata.codegen.handlers import DesignateClassPackages
from xsdata.codegen.handlers import FlattenAttributeGroups
from xsdata.codegen.handlers import FlattenClassExtensions
from xsdata.codegen.handlers import MergeAttributes
from xsdata.codegen.handlers import ProcessAttributeTypes
from xsdata.codegen.handlers import ProcessMixedContentClass
from xsdata.codegen.handlers import RenameDuplicateAttributes
from xsdata.codegen.handlers import RenameDuplicateClasses
from xsdata.codegen.handlers import SanitizeAttributesDefaultValue
from xsdata.codegen.handlers import SanitizeEnumerationClass
from xsdata.codegen.handlers import UnnestInnerClasses
from xsdata.codegen.handlers import UpdateAttributesEffectiveChoice
from xsdata.codegen.handlers import VacuumInnerClasses
from xsdata.codegen.handlers import ValidateAttributesOverrides
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_qname
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.config import GeneratorConfig
from xsdata.utils import collections
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
        the provided configuration."""
        super().__init__(config)

        self.data: Dict = {}

        self.processors = {
            Steps.FLATTEN: [
                FlattenAttributeGroups(self),
                FlattenClassExtensions(self),
                SanitizeEnumerationClass(self),
                UnnestInnerClasses(self),
                AddAttributeSubstitutions(self),
                ProcessAttributeTypes(self),
                MergeAttributes(),
                ProcessMixedContentClass(),
            ],
            Steps.SANITIZE: [
                UpdateAttributesEffectiveChoice(),
                SanitizeAttributesDefaultValue(self),
            ],
            Steps.RESOLVE: [
                ValidateAttributesOverrides(self),
                RenameDuplicateAttributes(),
            ],
            Steps.FINALIZE: [
                VacuumInnerClasses(),
                CreateCompoundFields(self),
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

    def first(self, qname: str) -> Class:
        classes = self.data.get(qname)
        if not classes:
            raise KeyError(f"Class {qname} not found")

        return classes[0]

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
            RenameDuplicateClasses(self),
            DesignateClassPackages(self),
        ]

        for designator in designators:
            designator.run()

    def filter_classes(self):
        """
        Filter classes to be generated.

        1. If there are no global elements generate them all
        2. Generate all global types and the referred types
        """

        # No global elements, generate them all!!!
        if not any(obj.is_global_type for obj in self):
            return

        occurs = {}
        for obj in self:
            if obj.is_global_type:
                occurs[obj.ref] = None
                occurs.update({ref: None for ref in obj.references})

        candidates = [obj for obj in self if obj.ref in occurs]
        self.data = collections.group_by(candidates, key=get_qname)

    def add(self, item: Class):
        """Add class item to the container."""
        self.data.setdefault(item.qname, []).append(item)

    def reset(self, item: Class, qname: str):
        self.data[qname].remove(item)
        self.add(item)

    def extend(self, items: List[Class]):
        """Add a list of classes the container."""
        collections.apply(items, self.add)
