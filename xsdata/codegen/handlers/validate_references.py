from typing import Set

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

    def run(self):
        """Validate type references."""
        self.validate_unique_qualified_names()
        self.validate_unique_instances()
        self.validate_resolved_references()

    def validate_unique_qualified_names(self):
        """Validate all root classes have unique qualified names."""
        duplicate_types = []
        groups = collections.group_by(self.container, get_qname)
        for qname, items in groups.items():
            if len(items) > 1:
                duplicate_types.append(qname)

        if duplicate_types:
            raise CodegenError("Duplicate types found", qnames=duplicate_types)

    def validate_unique_instances(self):
        """Validate all codegen instances are unique."""
        references: Set[int] = set()
        for item in self.container:
            item_references = {id(child) for child in item.children()}
            if item_references.intersection(references):
                raise CodegenError("Cross reference detected", type=item.qname)

            references.update(item_references)

    def validate_resolved_references(self):
        """Validate all types match a class reference and qualified name."""

        def build_reference_map():
            def build(target: Class):
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
