from dataclasses import dataclass
from dataclasses import field
from typing import List

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError


@dataclass
class ClassAnalyzer:
    """Validate, analyze, sanitize and select the final class list to be
    generated."""

    container: ClassContainer = field(default_factory=ClassContainer)

    def process(self) -> List[Class]:
        """Run all the processes."""
        self.pre_process()
        self.container.process()
        self.post_process()

        return self.select_classes()

    def pre_process(self):
        """Run validation checks for duplicate, invalid and redefined types."""
        ClassValidator(self.container).process()

    def post_process(self):
        """Sanitize class attributes after merging and flattening types and
        extensions."""
        ClassSanitizer(self.container).process()

    def select_classes(self) -> List[Class]:
        """
        Return the qualified classes for code generation.

        Return all if no classes are derived from xs:element or
        xs:complexType.
        """

        classes = list(self.container.iterate())
        if any(item.is_complex for item in classes):
            classes = list(
                filter(
                    lambda x: x.is_enumeration or (x.is_complex and not x.strict_type),
                    classes,
                )
            )

        self.validate_references(classes)

        return classes

    @classmethod
    def from_classes(cls, classes: List[Class]) -> "ClassAnalyzer":
        """Instantiate from a list of classes."""
        container = ClassContainer.from_list(classes)
        return cls(container)

    @classmethod
    def class_references(cls, target: Class) -> List:
        """Produce a list of instance references for the given class."""
        result = [id(target)]
        for attr in target.attrs:
            result.append(id(attr))
            result.extend(id(attr_type) for attr_type in attr.types)

        for extension in target.extensions:
            result.append(id(extension))
            result.append(id(extension.type))

        for inner in target.inner:
            result.extend(cls.class_references(inner))

        return result

    @classmethod
    def validate_references(cls, classes: List[Class]):
        """Validate all code gen objects are not cross referenced."""
        references = [ref for obj in classes for ref in cls.class_references(obj)]
        if len(references) != len(set(references)):
            raise AnalyzerValueError("Cross references detected!")
