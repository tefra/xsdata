from typing import List

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerError


class ClassAnalyzer:
    """Analyzer main responsibility is to orchestrate the processing of the
    class list and the selection of the final list of classes that need to be
    generated."""

    def __init__(self, classes: List[Class]):
        self.container = ClassContainer.from_list(classes)

    def process(self) -> List[Class]:
        self.pre_process()
        self.container.process()
        self.post_process()

        return self.select_classes()

    def pre_process(self):
        ClassValidator(self.container).process()

    def post_process(self):
        ClassSanitizer(self.container).process()

    def select_classes(self) -> List[Class]:
        """
        Return the qualified classes for code generation.

        Return all if no classes are derived from xs:element or
        xs:complexType.
        """

        classes = list(self.container.iterate())
        if any(item.is_complex for item in classes if not item.abstract):
            classes = list(
                filter(
                    lambda x: x.is_enumeration or (x.is_complex and not x.abstract),
                    classes,
                )
            )

        self.validate_references(classes)

        return classes

    @classmethod
    def class_references(cls, target: Class) -> List:
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
            raise AnalyzerError("Cross references detected!")
