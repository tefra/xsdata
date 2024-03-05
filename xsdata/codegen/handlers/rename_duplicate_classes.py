from typing import List, Set

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import (
    Attr,
    AttrType,
    Class,
    get_location,
    get_name,
    get_qname,
)
from xsdata.models.config import StructureStyle
from xsdata.utils import collections, namespaces, text

REQUIRE_UNIQUE_NAMES = (StructureStyle.SINGLE_PACKAGE, StructureStyle.CLUSTERS)


class RenameDuplicateClasses(ContainerHandlerInterface):
    """Resolve class name conflicts depending on the output structure style."""

    __slots__ = ()

    def run(self):
        """Detect and resolve class name conflicts."""
        use_name = self.should_use_names()
        getter = get_name if use_name else get_qname
        groups = collections.group_by(self.container, lambda x: text.alnum(getter(x)))

        for classes in groups.values():
            if len(classes) < 2:
                continue

            if all(x == classes[0] for x in classes):
                self.merge_classes(classes)
            else:
                self.rename_classes(classes, use_name)

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

    def merge_classes(self, classes: List[Class]):
        """Remove the duplicate classes and update all references.

        Args:
            classes: A list of duplicate classes
        """
        keep = classes.pop()
        replace = keep.ref
        self.container.remove(*classes)
        search = {item.ref for item in classes}

        for item in self.container:
            self.update_class_references(item, search, replace)

    def rename_classes(self, classes: List[Class], use_name: bool):
        """Rename all the classes in the list.

        Protect classes derived from xs:element if there is only one in
        the list.

        Args:
            classes: A list of classes with duplicate names
            use_name: Whether simple or qualified names should be used
                during renaming
        """
        total_elements = sum(x.is_element for x in classes)
        for target in sorted(classes, key=get_name):
            if not target.is_element or total_elements > 1:
                self.rename_class(target, use_name)

    def rename_class(self, target: Class, use_name: bool):
        """Find the next available class name.

        Save the original name in the class metadata and update
        the class qualified name and all classes that depend on
        the target class.

        Args:
            target: The target class instance to rename
            use_name: Whether simple or qualified names should be
                used during renaming
        """
        qname = target.qname
        namespace, name = namespaces.split_qname(target.qname)
        target.qname = self.next_qname(namespace, name, use_name)
        target.meta_name = name
        self.container.reset(target, qname)

        for item in self.container:
            self.rename_class_dependencies(item, id(target), target.qname)

    def next_qname(self, namespace: str, name: str, use_name: bool) -> str:
        """Use int suffixes to get the next available qualified name.

        Args:
            namespace: The class namespace
            name: The class name
            use_name: Whether simple or qualified names should be
                used during renaming
        """
        index = 0

        if use_name:
            reserved = {text.alnum(obj.name) for obj in self.container}
        else:
            reserved = {text.alnum(obj.qname) for obj in self.container}

        while True:
            index += 1
            new_name = f"{name}_{index}"
            qname = namespaces.build_qname(namespace, new_name)
            cmp = text.alnum(new_name if use_name else qname)

            if cmp not in reserved:
                return qname

    def update_class_references(self, target: Class, search: Set[int], replace: int):
        """Go through all class types and update all references.

        Args:
            target: The target class instance to update
            search: A set of class references to find
            replace: The new class reference to replace
        """

        def update_maybe(attr_type: AttrType):
            if attr_type.reference in search:
                attr_type.reference = replace

        for attr in target.attrs:
            for tp in attr.types:
                update_maybe(tp)

            for choice in attr.choices:
                for tp in choice.types:
                    update_maybe(tp)

        for ext in target.extensions:
            update_maybe(ext.type)

        for inner in target.inner:
            self.update_class_references(inner, search, replace)

    def rename_class_dependencies(self, target: Class, reference: int, replace: str):
        """Search and replace the old qualified class name in all classes.

        Args:
            target: The target class instance to inspect
            reference: The reference id of the renamed class
            replace: The new qualified name of the renamed class
        """
        for attr in target.attrs:
            self.rename_attr_dependencies(attr, reference, replace)

        for ext in target.extensions:
            if ext.type.reference == reference:
                ext.type.qname = replace

        for inner in target.inner:
            self.rename_class_dependencies(inner, reference, replace)

    def rename_attr_dependencies(self, attr: Attr, reference: int, replace: str):
        """Search and replace the old qualified class name in the attr types.

        This also covers any choices and references to enum values.

        Args:
            attr: The target attr instance to inspect
            reference: The reference id of the renamed class
            replace: The new qualified name of the renamed class
        """
        for attr_type in attr.types:
            if attr_type.reference == reference:
                attr_type.qname = replace

                if isinstance(attr.default, str) and attr.default.startswith("@enum@"):
                    members = text.suffix(attr.default, "::")
                    attr.default = f"@enum@{replace}::{members}"

        for choice in attr.choices:
            self.rename_attr_dependencies(choice, reference, replace)
