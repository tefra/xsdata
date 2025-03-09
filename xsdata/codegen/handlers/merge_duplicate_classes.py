from xsdata.codegen.mixins import ContainerHandlerInterface, ContainerInterface
from xsdata.codegen.models import (
    Class,
)


class MergeDuplicateClasses(ContainerHandlerInterface):
    """Remove duplicate classes.

    Args:
        container: The class container instance

    Attributes:
        merges: The merge instructions applied at the end
    """

    __slots__ = ("merges",)

    def __init__(self, container: ContainerInterface):
        """Initialize the rename duplicate class handler."""
        super().__init__(container)

        self.merges: dict[int, int] = {}

    def run(self) -> None:
        """Detect and merge duplicate classes conflicts."""
        for classes in self.group_duplicate_classes():
            if len(classes) > 1:
                self.merge_classes(classes)

        if self.merges:
            for target in self.container:
                self.update_references(target)

    def group_duplicate_classes(self) -> list[list[Class]]:
        """Group duplicate classes.

        This is very slow, because our gen models are unhashable.
        """
        groups: list[list[Class]] = []
        for cls in self.container:
            found = False
            for group in groups:
                if cls == group[0]:
                    group.append(cls)
                    found = True
                    break
            if not found:
                groups.append([cls])
        return groups

    def merge_classes(self, classes: list[Class]) -> None:
        """Remove the duplicate classes and schedule updates.

        Args:
            classes: A list of duplicate classes
        """
        keep = classes.pop()
        replace = keep.ref
        self.container.remove(*classes)

        for item in classes:
            self.merges[item.ref] = replace

    def update_references(self, target: Class) -> None:
        """Search and update the target class for merged references.

        Args:
            target: The target class instance to inspect and update
        """
        for tp in target.types():
            if tp.reference in self.merges:
                tp.reference = self.merges[tp.reference]
