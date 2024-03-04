from dataclasses import fields
from typing import Iterator, List, Tuple

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import (
    AttrType,
    Class,
    CodegenModel,
)
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
    def validate_references(cls, classes: List[Class]):
        """Validate codegen object references.

        #Todo - Add details on these exceptions

        Rules:
            1. No shared codegen objects between classes
            2. All attr types must have a reference id, except natives

        Args:
            classes: The list of classes to be generated.

        Raises:
            AnalyzerValueError: If an object violates the rules.
        """
        seen = set()
        for target in classes:
            for objects in cls.codegen_models(target):
                child = objects[-1]
                ref = id(child)
                if ref in seen:
                    raise AnalyzerValueError("Cross reference detected")

                if (
                    isinstance(child, AttrType)
                    and not child.reference
                    and not child.native
                ):
                    raise AnalyzerValueError("Unresolved reference")

                seen.add(ref)

    @classmethod
    def codegen_models(cls, *args: CodegenModel) -> Iterator[Tuple[CodegenModel, ...]]:
        """Find and yield all children codegen models.

        Args:
            *args: The codegen objects path.

        Yields:
            A tuple of codegen models like a path e.g. class, attr, attr_type
        """
        yield args
        model = args[-1]
        for f in fields(model):
            value = getattr(model, f.name)
            if isinstance(value, list) and value and isinstance(value[0], CodegenModel):
                for val in value:
                    yield from cls.codegen_models(*args, val)
            elif isinstance(value, CodegenModel):
                yield *args, value
