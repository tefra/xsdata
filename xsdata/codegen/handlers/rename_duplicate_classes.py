from xsdata.codegen.mixins import ContainerHandlerInterface, ContainerInterface
from xsdata.codegen.models import (
    Attr,
    Class,
    get_location,
    get_name,
    get_qname,
)
from xsdata.models.config import StructureStyle
from xsdata.utils import collections, namespaces, text

REQUIRE_UNIQUE_NAMES = (StructureStyle.SINGLE_PACKAGE, StructureStyle.CLUSTERS)


class RenameDuplicateClasses(ContainerHandlerInterface):
    """Resolve class name conflicts depending on the output structure style.

    Args:
        container: The class container instance

    Attributes:
        use_names: Whether names or qualified names should be used to group classes
        renames: The renamed instructions applied at the end
        reserved: The reserved class names or qualified names
    """

    __slots__ = ("merges", "renames", "reserved", "use_names")

    def __init__(self, container: ContainerInterface):
        """Initialize the rename duplicate class handler."""
        super().__init__(container)

        self.use_names = self.should_use_names()
        self.renames: dict[int, str] = {}
        self.merges: dict[int, int] = {}
        self.reserved: set[str] = set()

    def run(self) -> None:
        """Detect and resolve class name conflicts."""
        getter = get_name if self.use_names else get_qname
        groups = collections.group_by(self.container, lambda x: text.alnum(getter(x)))

        for classes in groups.values():
            if len(classes) > 1:
                self.rename_classes(classes)

        if self.renames or self.merges:
            for target in self.container:
                self.update_references(target)

    def should_use_names(self) -> bool:
        """Determine if names or qualified names should be used for detection.

        Strict unique names:
            - Single package
            - Clustered packages
            - All classes have the same source location.
        """
        return (
            self.container.config.output.structure_style in REQUIRE_UNIQUE_NAMES
            or len(set(map(get_location, self.container))) == 1
        )

    def rename_classes(self, classes: list[Class]) -> None:
        """Rename the classes in the list.

        Cases:
            - Two classes, one abstract append the abstract suffix
            - One element, add numeric suffixes to the rest of the classes
            - Add numeric suffixes to all classes.

        Args:
            classes: A list of classes with duplicate names
        """
        abstract = [x for x in classes if x.abstract]
        if len(classes) == 2 and len(abstract) == 1:
            self.add_abstract_suffix(abstract[0])
        else:
            total_elements = sum(x.is_element for x in classes)
            for target in sorted(classes, key=get_name):
                if not target.is_element or total_elements > 1:
                    self.add_numeric_suffix(target)

    def add_abstract_suffix(self, target: Class) -> None:
        """Add the abstract suffix to class name."""
        new_qname = f"{target.qname}_abstract"
        self.rename_class(target, new_qname)

    def add_numeric_suffix(self, target: Class) -> None:
        """Find the next available class name.

        Save the original name in the class metadata and update
        the class qualified name and all classes that depend on
        the target class.

        Args:
            target: The target class instance to rename
        """
        namespace, name = namespaces.split_qname(target.qname)
        new_qname = self.next_qname(namespace, name)
        self.rename_class(target, new_qname)

    def rename_class(self, target: Class, new_qname: str) -> None:
        """Update the class qualified name and schedule updates.

        Args:
            target: The target class to update
            new_qname: The new class qualified name
        """
        qname = target.qname
        target.qname = new_qname
        target.meta_name = namespaces.local_name(qname)

        self.container.reset(target, qname)
        self.renames[target.ref] = new_qname

    def next_qname(self, namespace: str, name: str) -> str:
        """Use int suffixes to get the next available qualified name.

        Args:
            namespace: The class namespace
            name: The class name
        """
        index = 0
        reserved = self.get_reserved()

        while True:
            index += 1
            new_name = f"{name}_{index}"
            qname = namespaces.build_qname(namespace, new_name)
            cmp = text.alnum(new_name if self.use_names else qname)

            if cmp not in reserved:
                reserved.add(cmp)
                return qname

    def get_reserved(self) -> set[str]:
        """Build the reserved names or qualified names of the container."""
        if not self.reserved:
            getter = get_name if self.use_names else get_qname
            self.reserved = {text.alnum(getter(obj)) for obj in self.container}

        return self.reserved

    def update_references(self, target: Class) -> None:
        """Search and update the target class for renamed references.

        Args:
            target: The target class instance to inspect and update
        """
        for parent, tp in target.types_with_parents():
            if tp.reference in self.renames:
                tp.qname = self.renames[tp.reference]

                if (
                    isinstance(parent, Attr)
                    and isinstance(parent.default, str)
                    and parent.default.startswith("@enum@")
                ):
                    members = text.suffix(parent.default, "::")
                    parent.default = f"@enum@{tp.qname}::{members}"
