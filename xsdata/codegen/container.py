from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.handlers import AddAttributeSubstitutions
from xsdata.codegen.handlers import CalculateAttributePaths
from xsdata.codegen.handlers import CreateCompoundFields
from xsdata.codegen.handlers import DesignateClassPackages
from xsdata.codegen.handlers import FilterClasses
from xsdata.codegen.handlers import FlattenAttributeGroups
from xsdata.codegen.handlers import FlattenClassExtensions
from xsdata.codegen.handlers import MergeAttributes
from xsdata.codegen.handlers import ProcessAttributeTypes
from xsdata.codegen.handlers import ProcessMixedContentClass
from xsdata.codegen.handlers import RenameDuplicateAttributes
from xsdata.codegen.handlers import RenameDuplicateClasses
from xsdata.codegen.handlers import ResetAttributeSequenceNumbers
from xsdata.codegen.handlers import ResetAttributeSequences
from xsdata.codegen.handlers import SanitizeAttributesDefaultValue
from xsdata.codegen.handlers import SanitizeEnumerationClass
from xsdata.codegen.handlers import UnnestInnerClasses
from xsdata.codegen.handlers import UpdateAttributesEffectiveChoice
from xsdata.codegen.handlers import VacuumInnerClasses
from xsdata.codegen.handlers import ValidateAttributesOverrides
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.config import GeneratorConfig
from xsdata.utils import collections
from xsdata.utils.constants import return_true


class Steps:
    UNGROUP = 10
    FLATTEN = 20
    SANITIZE = 30
    RESOLVE = 40
    FINALIZE = 50


class ClassContainer(ContainerInterface):
    __slots__ = ("data", "processors", "step")

    def __init__(self, config: GeneratorConfig):
        """Initialize a class container instance with its processors based on
        the provided configuration."""
        super().__init__(config)

        self.step: int = 0
        self.data: Dict = {}

        self.processors: Dict[int, List] = {
            Steps.UNGROUP: [
                FlattenAttributeGroups(self),
            ],
            Steps.FLATTEN: [
                CalculateAttributePaths(),
                FlattenClassExtensions(self),
                SanitizeEnumerationClass(self),
                UpdateAttributesEffectiveChoice(),
                UnnestInnerClasses(self),
                AddAttributeSubstitutions(self),
                ProcessAttributeTypes(self),
                MergeAttributes(),
                ProcessMixedContentClass(),
            ],
            Steps.SANITIZE: [
                ResetAttributeSequences(),
                RenameDuplicateAttributes(),
                SanitizeAttributesDefaultValue(self),
            ],
            Steps.RESOLVE: [
                ValidateAttributesOverrides(self),
            ],
            Steps.FINALIZE: [
                VacuumInnerClasses(),
                CreateCompoundFields(self),
                # Prettify things!!!
                ResetAttributeSequenceNumbers(self),
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
                if row.status < self.step:
                    self.process_class(row, self.step)
                    return self.find(qname, condition)

                return row
        return None

    def find_inner(self, source: Class, qname: str) -> Class:
        inner = ClassUtils.find_inner(source, qname)
        if inner.status < self.step:
            self.process_class(inner, self.step)

        return inner

    def first(self, qname: str) -> Class:
        classes = self.data.get(qname)
        if not classes:
            raise KeyError(f"Class {qname} not found")

        return classes[0]

    def process(self):
        """The hidden naive recipe of processing xsd models."""
        self.process_classes(Steps.UNGROUP)
        self.remove_groups()
        self.process_classes(Steps.FLATTEN)
        self.filter_classes()
        self.process_classes(Steps.SANITIZE)
        self.process_classes(Steps.RESOLVE)
        self.process_classes(Steps.FINALIZE)
        self.designate_classes()

    def process_classes(self, step: int) -> None:
        self.step = step
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
        """Filter the classes to be generated."""
        FilterClasses(self).run()

    def remove_groups(self):
        self.set([x for x in iter(self) if not x.is_group])

    def add(self, item: Class):
        """Add class item to the container."""
        self.data.setdefault(item.qname, []).append(item)

    def reset(self, item: Class, qname: str):
        self.data[qname].remove(item)
        self.add(item)

    def set(self, items: List[Class]):
        self.data.clear()
        self.extend(items)

    def extend(self, items: List[Class]):
        """Add a list of classes the container."""
        collections.apply(items, self.add)
