from typing import List, Optional

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.models import Attr, Class, Extension, get_tag
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.collections import group_by


class ClassValidator:
    """Container class validator.

    Args:
        container: The class container instance
    """

    __slots__ = "container"

    def __init__(self, container: ContainerInterface):
        self.container = container

    def process(self):
        """Main process entrypoint.

        Runs on groups of classes with the same
        qualified name.

        Steps:
            1. Remove invalid classes
            2. Handle duplicate types
            3. Merge global types
        """
        for classes in self.container.data.values():
            if len(classes) > 1:
                self.remove_invalid_classes(classes)

            if len(classes) > 1:
                self.handle_duplicate_types(classes)

            if len(classes) > 1:
                self.merge_global_types(classes)

    def remove_invalid_classes(self, classes: List[Class]):
        """Remove classes with undefined extensions.

        Args:
            classes: A list of class instances
        """

        def is_invalid(ext: Extension) -> bool:
            """Check if given type declaration is not native and is missing."""
            return not ext.type.native and ext.type.qname not in self.container.data

        for target in list(classes):
            if any(is_invalid(extension) for extension in target.extensions):
                classes.remove(target)

    @classmethod
    def handle_duplicate_types(cls, classes: List[Class]):
        """Find and handle duplicate classes.

        If a class is defined more than once, keep either
        the one that was in redefines or overrides, or the
        last definition. If a class was redefined merge
        circular group attrs and extensions.

        In order for two classes to be duplicated they must
        have the same qualified name and be derived from the
        same xsd element.

        Args:
            classes: A list of classes with the same qualified name
        """
        for items in group_by(classes, get_tag).values():
            if len(items) == 1:
                continue

            index = cls.select_winner(list(items))

            if index == -1:
                logger.warning(
                    "Duplicate type %s, will keep the last defined",
                    items[0].qname,
                )

            winner = items.pop(index)

            for item in items:
                classes.remove(item)

                if winner.container == Tag.REDEFINE:
                    cls.merge_redefined_type(item, winner)

    @classmethod
    def merge_redefined_type(cls, source: Class, target: Class):
        """Merge source properties to the target redefined target class instance.

        Redefined classes usually have references to the original
        class. We need to copy those.

        Args:
            source: The original source class instance
            target: The redefined target class instance
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
        """From a list of classes select which class index will remain.

        Classes that were extracted from in xs:override/xs:redefined
        containers have priority, otherwise pick the last in the list.

        Args:
            candidates: A list of duplicate class instances

        Returns:
            The index of winner class or -1 if there is no clear winner.
        """
        for index, item in enumerate(candidates):
            if item.container in (Tag.OVERRIDE, Tag.REDEFINE):
                return index

        return -1

    @classmethod
    def find_circular_extension(cls, target: Class) -> Optional[Extension]:
        """Find the first circular reference extension.

        Redefined classes usually have references to the original
        class with the same qualified name. We need to locate
        those and copy any attrs.

        Args:
            target: The target class instance to inspect

        Returns:
            An extension instance or None if there is no circular extension.
        """
        for ext in target.extensions:
            if ext.type.name == target.name:
                return ext

        return None

    @classmethod
    def find_circular_group(cls, target: Class) -> Optional[Attr]:
        """Find an attr with the same name as the target class name.

        Redefined classes usually have references to the original
        class with the same qualified name. We need to locate
        those and copy any attrs.

        Args:
            target: The target class instance to inspect

        Returns:
            An attr instance or None if there is no circular attr.
        """
        return ClassUtils.find_attr(target, target.name)

    @classmethod
    def merge_global_types(cls, classes: List[Class]):
        """Merge parent-child global types.

        Conditions
            1. One of them is derived from xs:element
            2. One of them is derived from xs:complexType
            3. The xs:element is a subclass of the xs:complexType
            4. The xs:element has no attributes (This can't happen in a valid schema)


        Args:
             classes: A list of duplicate classes
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
        ct.substitutions = el.substitutions
        classes.remove(el)
