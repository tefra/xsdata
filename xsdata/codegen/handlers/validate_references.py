from collections.abc import Iterator

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class, get_qname
from xsdata.utils import collections


class ValidateReferences(ContainerHandlerInterface):
    """Validate type references.

    Rules:
        - An extension, type, restriction can not be shared
        - All user types have to match the reference number
          and qualified name of a class.
        - All global class qualified names must be unique
    """

    def run(self) -> None:
        """Validate type references."""
        self.validate_unique_qualified_names()
        self.validate_unique_instances()
        self.validate_resolved_references()
        self.validate_parent_references()

    def validate_unique_qualified_names(self) -> None:
        """Validate all root classes have unique qualified names."""
        duplicate_types = []
        groups = collections.group_by(self.container, get_qname)
        for qname, items in groups.items():
            if len(items) > 1:
                duplicate_types.append(qname)

        if duplicate_types:
            raise CodegenError("Duplicate types found", qnames=duplicate_types)

    def validate_unique_instances(self) -> None:
        """Validate all codegen instances are unique."""
        references: set[int] = set()
        for item in self.container:
            item_references = {id(child) for child in item.children()}
            if item_references.intersection(references):
                raise CodegenError("Cross reference detected", type=item.qname)

            references.update(item_references)

    def validate_resolved_references(self) -> None:
        """Validate all types match a class reference and qualified name."""

        def build_reference_map() -> Iterator[tuple[int, str]]:
            def build(target: Class) -> Iterator[tuple[int, str]]:
                yield target.ref, target.qname

                for inner in target.inner:
                    yield from build(inner)

            for target in self.container:
                yield from build(target)

        references = dict(build_reference_map())
        for item in self.container:
            for tp in item.types():
                if tp.native:
                    continue

                if tp.reference not in references:
                    raise CodegenError(
                        "Unresolved reference detected", cls=item.qname, type=tp.qname
                    )

                if tp.qname != references[tp.reference]:
                    raise CodegenError(
                        "Misrepresented reference", cls=item.qname, type=tp.qname
                    )

    def validate_parent_references(self) -> None:
        """Validate inner to outer classes is accurate."""

        def _validate(target: Class, parent: Class | None = None) -> None:
            actual_qname = actual_ref = expected_qname = expected_ref = None
            if target.parent:
                actual_qname = target.parent.qname
                actual_ref = target.parent.ref

            if parent:
                expected_qname = parent.qname
                expected_ref = parent.ref

            if actual_qname != expected_qname:
                raise CodegenError(
                    "Invalid parent class reference",
                    cls=target.qname,
                    expected=expected_qname,
                    actual=actual_qname,
                )

            if actual_ref != expected_ref:
                raise CodegenError(
                    "Invalid parent class reference",
                    cls=target.qname,
                    ref=actual_qname,
                )

            for inner in target.inner:
                _validate(inner, target)

        for item in self.container:
            _validate(item)
