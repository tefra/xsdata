from typing import List

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.config import GeneratorConfig


class ClassAnalyzer:
    """Validate, analyze, sanitize and select the final class list to be
    generated."""

    @classmethod
    def process(cls, classes: List[Class], config: GeneratorConfig) -> List[Class]:
        """Run all the processes."""

        # Wrap classes with container for easy access.
        container = ClassContainer.from_list(classes)

        # Run validation checks for duplicate, invalid and redefined types.
        ClassValidator.process(container)

        # Run analyzer handlers
        container.process()

        # Filter classes that should be generated.
        container.filter_classes()

        # Sanitize class attributes after merging and flattening types and extensions.
        ClassSanitizer.process(container, config)

        classes = container.class_list
        cls.validate_references(classes)

        return classes

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
