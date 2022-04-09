from typing import List

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_location
from xsdata.codegen.models import get_name
from xsdata.codegen.models import get_qname
from xsdata.models.config import StructureStyle
from xsdata.utils import collections
from xsdata.utils import namespaces
from xsdata.utils import text

REQUIRE_UNIQUE_NAMES = (StructureStyle.SINGLE_PACKAGE, StructureStyle.CLUSTERS)


class RenameDuplicateClasses(ContainerHandlerInterface):
    """Resolve class name conflicts depending on the output structure style."""

    __slots__ = ()

    def run(self):
        """Search for conflicts either by qualified name or local name
        depending on the configuration and start renaming classes and
        dependencies."""

        use_name = self.should_use_names()
        getter = get_name if use_name else get_qname
        groups = collections.group_by(self.container, lambda x: text.alnum(getter(x)))

        for classes in groups.values():
            if len(classes) > 1:
                self.rename_classes(classes, use_name)

    def should_use_names(self) -> bool:
        """
        Determine if we should be using names or qualified names to detect
        collisions.

        Strict unique names:
        - Single package
        - Clustered packages
        - All classes have the same source location.
        """
        return (
            self.container.config.output.structure_style in REQUIRE_UNIQUE_NAMES
            or len(set(map(get_location, self.container))) == 1
        )

    def rename_classes(self, classes: List[Class], use_name: bool):
        """
        Rename all the classes in the list.

        Protect classes derived from xs:element if there is only one in
        the list.
        """
        total_elements = sum(x.is_element for x in classes)
        for target in sorted(classes, key=get_name):
            if not target.is_element or total_elements > 1:
                self.rename_class(target, use_name)

    def rename_class(self, target: Class, use_name: bool):
        """Find the next available class identifier, save the original name in
        the class metadata and update the class qualified name and all classes
        that depend on the target class."""

        qname = target.qname
        namespace, name = namespaces.split_qname(target.qname)
        target.qname = self.next_qname(namespace, name, use_name)
        target.meta_name = name
        self.container.reset(target, qname)

        for item in self.container:
            self.rename_class_dependencies(item, id(target), target.qname)

    def next_qname(self, namespace: str, name: str, use_name: bool) -> str:
        """Append the next available index number for the given namespace and
        local name."""
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

    def rename_class_dependencies(self, target: Class, reference: int, replace: str):
        """Search and replace the old qualified attribute type name with the
        new one if it exists in the target class attributes, extensions and
        inner classes."""
        for attr in target.attrs:
            self.rename_attr_dependencies(attr, reference, replace)

        for ext in target.extensions:
            if ext.type.reference == reference:
                ext.type.qname = replace

        for inner in target.inner:
            self.rename_class_dependencies(inner, reference, replace)

    def rename_attr_dependencies(self, attr: Attr, reference: int, replace: str):
        """Search and replace the old qualified attribute type name with the
        new one in the attr types, choices and default value."""
        for attr_type in attr.types:
            if attr_type.reference == reference:
                attr_type.qname = replace

                if isinstance(attr.default, str) and attr.default.startswith("@enum@"):
                    members = text.suffix(attr.default, "::")
                    attr.default = f"@enum@{replace}::{members}"

        for choice in attr.choices:
            self.rename_attr_dependencies(choice, reference, replace)
