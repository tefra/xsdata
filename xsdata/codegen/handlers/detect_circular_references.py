from typing import Dict, List

from xsdata.codegen.mixins import (
    ContainerInterface,
    RelativeHandlerInterface,
)
from xsdata.codegen.models import AttrType, Class


class DetectCircularReferences(RelativeHandlerInterface):
    """Accurately detect circular dependencies between classes.

    Args:
        container: The class container instance

    Attributes:
        reference_types: A map of class refs to dependency types
    """

    __slots__ = "container", "reference_types"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.reference_types: Dict[int, List[AttrType]] = {}

    def process(self, target: Class):
        """Go through all the attr types and find circular references.

        Args:
            target: The class to inspect and update
        """
        if not self.reference_types:
            self.build_reference_types()

        for attr in target.attrs:
            self.process_types(attr.types, target.ref)

            for choice in attr.choices:
                self.process_types(choice.types, target.ref)

    def process_types(self, types: List[AttrType], class_reference: int):
        """Go through the types and find circular references.

        Args:
            types: A list attr/choice type instances
            class_reference: The parent attr/choice class reference
        """
        for tp in types:
            if not tp.forward and not tp.native and not tp.circular:
                tp.circular = self.is_circular(tp.reference, class_reference)

    def is_circular(self, start: int, stop: int) -> bool:
        """Detect if the start reference leads to the stop reference.

        The procedure is a dfs search to avoid max recursion errors.

        Args:
            start: The attr type reference
            stop: The parent class reference

        Returns:
            Whether the start reference leads back to the stop reference.
        """
        path = set()
        stack = [start]
        while len(stack) != 0:
            if stop in path:
                return True

            ref = stack.pop()
            path.add(ref)

            for tp in self.reference_types[ref]:
                if not tp.circular and tp.reference not in path:
                    stack.append(tp.reference)

        return stop in path

    def build_reference_types(self):
        """Build the reference types mapping."""

        def generate(target: Class):
            yield target.ref, [tp for tp in target.types() if tp.reference]

            for inner in target.inner:
                yield from generate(inner)

        for item in self.container:
            for ref, types in generate(item):
                self.reference_types[ref] = types
