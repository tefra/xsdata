from dataclasses import dataclass
from typing import List
from typing import Optional

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.collections import group_by


@dataclass
class ClassValidator:
    """Run validations against the class container in order to remove or merge
    invalid or redefined types."""

    container: ClassContainer

    def process(self):
        """
        Remove if possible classes with the same qualified name.

        Steps:
            1. Remove invalid classes
            2. Handle duplicate types
            3. Merge dummy types
        """
        for classes in self.container.data.values():

            if len(classes) > 1:
                self.remove_invalid_classes(classes)

            if len(classes) > 1:
                self.handle_duplicate_types(classes)

            if len(classes) > 1:
                self.merge_global_types(classes)

    def remove_invalid_classes(self, classes: List[Class]):
        """Remove from the given class list any class with missing extension
        type."""

        def is_invalid(ext: Extension) -> bool:
            """Check if given type declaration is not native and is missing."""
            return not ext.type.native and ext.type.qname not in self.container.data

        for target in list(classes):
            if any(is_invalid(extension) for extension in target.extensions):
                classes.remove(target)

    @classmethod
    def handle_duplicate_types(cls, classes: List[Class]):
        """Handle classes with same namespace, name that are derived from the
        same xs type."""

        grouped = group_by(classes, lambda x: f"{x.tag}{x.qname}")
        for items in grouped.values():
            if len(items) == 1:
                continue

            index = cls.select_winner(list(items))
            winner = items.pop(index)

            for item in items:
                classes.remove(item)

                if winner.container == Tag.REDEFINE:
                    cls.merge_redefined_type(item, winner)

    @classmethod
    def merge_redefined_type(cls, source: Class, target: Class):
        """
        Copy any attributes and extensions to redefined types from the original
        definitions.

        Redefined inheritance is optional search for self references in
        extensions and attribute groups.
        """
        circular_extension = cls.find_circular_extension(target)
        circular_group = cls.find_circular_group(target)

        if circular_extension:
            ClassUtils.copy_attributes(source, target, circular_extension)
            ClassUtils.copy_extensions(source, target, circular_extension)

        if circular_group:
            ClassUtils.copy_group_attributes(source, target, circular_group)

    @classmethod
    def select_winner(cls, candidates: List[Class]) -> int:
        """
        Returns the index of the class that will survive the duplicate process.

        Classes that were extracted from in xs:override/xs:redefined
        containers have priority, otherwise pick the last in the list.
        """

        for index, item in enumerate(candidates):
            if item.container in (Tag.OVERRIDE, Tag.REDEFINE):
                return index

        return -1

    @classmethod
    def find_circular_extension(cls, target: Class) -> Optional[Extension]:
        """Search for any target class extensions that is a circular
        reference."""
        for ext in target.extensions:
            if ext.type.name == target.name:
                return ext

        return None

    @classmethod
    def find_circular_group(cls, target: Class) -> Optional[Attr]:
        """Search for any target class attributes that is a circular
        reference."""
        for attr in target.attrs:
            if attr.name == target.name:
                return attr

        return None

    @classmethod
    def merge_global_types(cls, classes: List[Class]):
        """
        Merge parent-child global types.

        Conditions
            1. One of them is derived from xs:element
            2. One of them is derived from xs:complexType
            3. The xs:element is a subclass of the xs:complexType
            4. The xs:element has no attributes (This can't happen in a valid schema)
        """

        el = collections.first(x for x in classes if x.tag == Tag.ELEMENT)
        ct = collections.first(x for x in classes if x.tag == Tag.COMPLEX_TYPE)

        if (
            el is None
            or ct is None
            or el is ct
            or el.attrs
            or len(el.extensions) != 1
            or el.extensions[0].type.qname != el.qname
        ):
            return

        ct.namespace = el.namespace or ct.namespace
        ct.help = el.help or ct.help
        classes.remove(el)
