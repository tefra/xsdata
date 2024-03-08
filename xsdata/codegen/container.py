from typing import Callable, Dict, Iterator, List, Optional

from xsdata.codegen.handlers import (
    AddAttributeSubstitutions,
    CalculateAttributePaths,
    CreateCompoundFields,
    DesignateClassPackages,
    DetectCircularReferences,
    DisambiguateChoices,
    FilterClasses,
    FlattenAttributeGroups,
    FlattenClassExtensions,
    MergeAttributes,
    ProcessAttributeTypes,
    ProcessMixedContentClass,
    RenameDuplicateAttributes,
    RenameDuplicateClasses,
    ResetAttributeSequenceNumbers,
    ResetAttributeSequences,
    SanitizeAttributesDefaultValue,
    SanitizeEnumerationClass,
    UnnestInnerClasses,
    UpdateAttributesEffectiveChoice,
    VacuumInnerClasses,
    ValidateAttributesOverrides,
    ValidateReferences,
)
from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Class, Status
from xsdata.codegen.utils import ClassUtils
from xsdata.codegen.validator import ClassValidator
from xsdata.models.config import GeneratorConfig
from xsdata.utils import collections
from xsdata.utils.constants import return_true


class Steps:
    """Process steps."""

    UNGROUP = 10
    FLATTEN = 20
    SANITIZE = 30
    RESOLVE = 40
    CLEANUP = 50
    FINALIZE = 60


class ClassContainer(ContainerInterface):
    """A class list wrapper with an easy access api.

    Args:
        config: The generator configuration instance

    Attributes:
        processors: A step-processors mapping
        data: The class qname map
        step: The current process step
    """

    __slots__ = ("processors", "step")

    def __init__(self, config: GeneratorConfig):
        """Initialize the container and all the class processors.

        The order of the steps and the processors is the secret
        recipe of the xsdata code generator.

        Args:
            config: The generator configuration instance
        """
        super().__init__(config)
        self.step: int = 0
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
            Steps.CLEANUP: [
                VacuumInnerClasses(),
            ],
            Steps.FINALIZE: [
                DetectCircularReferences(self),
                CreateCompoundFields(self),
                DisambiguateChoices(self),
                ResetAttributeSequenceNumbers(self),
            ],
        }

    def __iter__(self) -> Iterator[Class]:
        """Yield an iterator for the class map values."""
        for items in list(self.data.values()):
            yield from items

    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Find class that matches the given qualified name and condition callable.

        Classes are allowed to have the same qualified name, e.g. xsd:Element
        extending xsd:ComplexType with the same name, you can provide and additional
        callback to filter the classes like the tag.

        Args:
            qname: The qualified name of the class
            condition: A user callable to filter further

        Returns:
            A class instance or None if no match found.
        """
        for row in self.data.get(qname, []):
            if condition(row):
                if row.status < self.step:
                    self.process_class(row, self.step)
                    return self.find(qname, condition)

                return row
        return None

    def find_inner(self, source: Class, qname: str) -> Class:
        """Search by qualified name for a specific inner class or fail.

        Args:
            source: The source class to search for the inner class
            qname: The qualified name of the inner class to look up

        Returns:
            The inner class instance

        Raises:
            CodeGenerationError: If the inner class is not found.
        """
        inner = ClassUtils.find_inner(source, qname)
        if inner.status < self.step:
            self.process_class(inner, self.step)

        return inner

    def first(self, qname: str) -> Class:
        """Return the first class that matches the qualified name.

        Args:
            qname: The qualified name of the class

        Returns:
            The first matching class

        Raises:
            KeyError: If no class matches the qualified name
        """
        classes = self.data.get(qname)
        if not classes:
            raise KeyError(f"Class {qname} not found")

        return classes[0]

    def process(self):
        """Run the processor and filter steps."""
        self.validate_classes()
        self.process_classes(Steps.UNGROUP)
        self.remove_groups()
        self.process_classes(Steps.FLATTEN)
        self.filter_classes()
        self.process_classes(Steps.SANITIZE)
        self.process_classes(Steps.RESOLVE)
        self.process_classes(Steps.CLEANUP)
        self.process_classes(Steps.FINALIZE)
        self.designate_classes()

    def validate_classes(self):
        """Merge redefined classes."""
        ClassValidator(self).process()

    def process_classes(self, step: int):
        """Run the given step processors for all classes.

        Args:
            step: The step reference number
        """
        self.step = step
        for obj in self:
            if obj.status < step:
                self.process_class(obj, step)

    def process_class(self, target: Class, step: int):
        """Run the step processors for the given class.

        Process recursively any inner classes as well.

        Args:
            target: The target class to process
            step: The step reference number
        """
        target.status = Status(step)
        for processor in self.processors.get(step, []):
            processor.process(target)

        for inner in target.inner:
            if inner.status < step:
                self.process_class(inner, step)

        target.status = Status(step + 1)

    def designate_classes(self):
        """Designate the final class names, packages and modules."""
        designators = [
            RenameDuplicateClasses(self),
            ValidateReferences(self),
            DesignateClassPackages(self),
        ]

        for designator in designators:
            designator.run()

    def filter_classes(self):
        """Filter the classes to be generated."""
        FilterClasses(self).run()

    def remove_groups(self):
        """Remove xs:groups and xs:attributeGroups from the container."""
        self.set([x for x in iter(self) if not x.is_group])

    def add(self, item: Class):
        """Add class item to the container.

        Args:
            item: The class instance to add
        """
        self.data.setdefault(item.qname, []).append(item)

    def remove(self, *items: Class):
        """Safely remove classes from the container.

        Args:
            items: The classes to remove
        """
        for item in items:
            self.data[item.qname] = [
                c for c in self.data[item.qname] if c.ref != item.ref
            ]

    def reset(self, item: Class, qname: str):
        """Update the given class qualified name.

        Args:
            item: The target class instance to update
            qname: The new qualified name of the class
        """
        self.data[qname] = [c for c in self.data[qname] if c.ref != item.ref]
        self.add(item)

    def set(self, items: List[Class]):
        """Set the list of classes to the container.

        Args:
            items: The list of classes
        """
        self.data.clear()
        self.extend(items)

    def extend(self, items: List[Class]):
        """Add a list of classes to the container.

        Args:
            items: The list of class instances to add
        """
        collections.apply(items, self.add)
