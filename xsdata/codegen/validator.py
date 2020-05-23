from dataclasses import dataclass
from typing import List

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import text
from xsdata.utils.collections import group_by


@dataclass
class ClassValidator:

    container: ClassContainer

    def process(self):
        """
        Remove if possible classes with the same qualified name.

        Steps:
            1. Remove classes with missing extension type.
            2. Merge redefined classes.
            3. Fix implied abstract flags.
        """
        for classes in self.container.values():

            if len(classes) > 1:
                self.remove_invalid_classes(classes)

            if len(classes) > 1:
                self.merge_redefined_classes(classes)

            if len(classes) > 1:
                self.update_abstract_classes(classes)

    def remove_invalid_classes(self, classes: List[Class]):
        """Remove from the given class list any class with missing extension
        type."""

        def is_invalid(source: Class, ext: Extension) -> bool:
            """Check if given type declaration is not native and is missing."""
            if ext.type.native:
                return False

            qname = source.source_qname(ext.type.name)
            return qname not in self.container

        for target in list(classes):
            if any(is_invalid(target, extension) for extension in target.extensions):
                classes.remove(target)

    @classmethod
    def merge_redefined_classes(cls, classes: List[Class]):
        """Merge original and redefined classes."""

        grouped = group_by(classes, lambda x: f"{x.type.__name__}{x.source_qname()}")
        for items in grouped.values():
            if len(items) == 1:
                continue

            winner: Class = items.pop()
            for item in items:
                classes.remove(item)

                self_extension = next(
                    (
                        ext
                        for ext in winner.extensions
                        if text.suffix(ext.type.name) == winner.name
                    ),
                    None,
                )

                if not self_extension:
                    continue

                ClassUtils.copy_attributes(item, winner, self_extension)
                for looser_ext in item.extensions:
                    new_ext = looser_ext.clone()
                    new_ext.restrictions.merge(self_extension.restrictions)
                    winner.extensions.append(new_ext)

    @classmethod
    def update_abstract_classes(cls, classes: List[Class]):
        """
        Update classes with the same qualified name to set implied abstract
        flags.

        If a non abstract xs:element exists in the list mark the rest
        xs:complexType(s) as abstract.
        """

        element = next((obj for obj in classes if obj.is_element), None)
        if element:
            for obj in classes:
                if obj is not element and obj.is_complex:
                    obj.abstract = True
