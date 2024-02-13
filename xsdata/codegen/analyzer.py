from typing import List

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError


class ClassAnalyzer:
    """Validate, analyze, sanitize and filter the generated classes."""

    @classmethod
    def process(cls, container: ClassContainer) -> List[Class]:
        """Main entrypoint for the class container instance.

        Orchestrate the class validations and processors.

        Args:
            container: The class container instance

        Returns:
            The list of classes to be generated.
        """
        # Run validation checks for duplicate, invalid and redefined types.
        ClassValidator(container).process()

        # Run analyzer handlers
        container.process()

        classes = list(container)
        cls.validate_references(classes)

        return classes

    @classmethod
    def class_references(cls, target: Class) -> List[int]:
        """Produce a list of instance references for the given class.

        Collect the ids of the class, attr, extension and inner instances.

        Args:
            target: The target class instance

        List:
            The list of id references.
        """
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
        """Validate all codegen objects are not cross-referenced.

        This validation ensures we never share any attr, or extension
        between classes.

        Args:
            classes: The list of classes to be generated.

        Raises:
            AnalyzerValueError: If an object is shared between the classes.
        """
        references = [ref for obj in classes for ref in cls.class_references(obj)]
        if len(references) != len(set(references)):
            raise AnalyzerValueError("Cross references detected!")
