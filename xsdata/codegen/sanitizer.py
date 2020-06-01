import re
from dataclasses import dataclass
from typing import Callable
from typing import List
from typing import Optional

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.logger import logger
from xsdata.utils import text
from xsdata.utils.collections import group_by


@dataclass
class ClassSanitizer:
    container: ClassContainer

    def process(self):
        for obj in self.container.iterate():
            self.process_class(obj)

    def process_class(self, target: Class):
        """
        Sanitize the attributes of the given class. After applying all the
        flattening handlers the attributes need to be further sanitized to
        squash common issues like duplicate attribute names.

        Steps:
            1. Sanitize inner classes
            2. Sanitize attributes default value
            3. Sanitize attributes name
            4. Sanitize attributes sequential flag
            5. Sanitize duplicate attribute names
        """
        for inner in target.inner:
            self.process_class(inner)

        for attr in target.attrs:
            self.process_attribute_default(target, attr)
            self.process_attribute_restrictions(attr)
            self.process_attribute_name(attr)
            self.process_attribute_sequence(target, attr)

        self.process_duplicate_attribute_names(target.attrs)

    def process_attribute_default(self, target: Class, attr: Attr):
        """
        Sanitize attribute default value.

        Cases:
            1. List fields can not have a fixed value.
            2. Optional fields or xsi:type can not have a default or fixed value.
            3. Convert string literal default value for enum fields.
        """
        if attr.is_list:
            attr.fixed = False

        if attr.is_optional or attr.is_xsi_type:
            attr.fixed = False
            attr.default = None

        if attr.default and not attr.is_enumeration:
            self.process_attribute_default_enum(target, attr)

    def process_attribute_default_enum(self, target: Class, attr: Attr):
        """
        Convert string literal default value for enum fields.

        Loop through all attributes types and search for enum sources.
        If an enum source exist map the default string literal value to
        a qualified name. If the source class in inner promote it to
        root classes.
        """

        source_found = False
        for attr_type in attr.types:
            source = self.find_enum(target, attr_type)
            if not source:
                continue

            source_found = True
            source_attr = next(
                (x for x in source.attrs if x.default == attr.default), None
            )
            if source_attr:
                if attr_type.forward:
                    self.promote_inner_class(target, source)

                attr.default = f"@enum@{source.name}::{source_attr.name}"
                return

        if source_found:
            logger.warning(
                "No enumeration member matched %s.%s default value `%s`",
                target.name,
                attr.local_name,
                attr.default,
            )
            attr.default = None

    def promote_inner_class(self, parent: Class, inner: Class):
        """
        Convert inner class to root class.

        Steps:
            1. Remove inner class from parent
            2. Prepend parent name to inner class name.
            3. Search and replace all matching attribute types.
            4. Add inner class to the global class index.
        """
        name = f"{parent.name}_{inner.name}"
        parent.inner.remove(inner)

        for attr in parent.attrs:
            for attr_type in attr.types:
                if attr_type.name == inner.name:
                    attr_type.forward = False
                    attr_type.name = name

        inner.name = name

        self.container.add(inner)

    @classmethod
    def process_attribute_restrictions(cls, attr: Attr):
        """Sanitize attribute required flag by comparing the min/max
        occurrences restrictions."""
        restrictions = attr.restrictions
        min_occurs = restrictions.min_occurs or 0
        max_occurs = restrictions.max_occurs or 0

        if min_occurs == 0 and max_occurs <= 1:
            restrictions.required = None
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        if min_occurs == 1 and max_occurs == 1:
            restrictions.required = True
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif restrictions.max_occurs and max_occurs > 1:
            restrictions.min_occurs = min_occurs
            restrictions.required = None

    @classmethod
    def process_attribute_sequence(cls, target: Class, attr: Attr):
        """Reset the attribute at the given index if it has no siblings with
        the sequential restriction."""

        index = target.attrs.index(attr)
        before = target.attrs[index - 1] if index - 1 >= 0 else None
        after = target.attrs[index + 1] if index + 1 < len(target.attrs) else None

        if not attr.is_list:
            attr.restrictions.sequential = False

        if (
            not attr.restrictions.sequential
            or (before and before.restrictions.sequential)
            or (after and after.restrictions.sequential and after.is_list)
        ):
            return

        attr.restrictions.sequential = False

    @classmethod
    def process_attribute_name(cls, attr: Attr):
        """
        Sanitize attribute name in preparation for duplicate attribute names
        handler.

        Steps:
            1. Remove non alpha numerical values
            2. Handle Enum negative numerical values
            3. Remove namespaces prefixes
            4. Ensure name not empty
            5. Ensure name starts with a letter
        """
        if attr.is_enumeration:
            attr.name = attr.default
            if re.match(r"^-\d*\.?\d+$", attr.name):
                attr.name = f"value_minus_{attr.name}"
            else:
                attr.name = re.sub("[^0-9a-zA-Z]", " ", attr.name).strip()
        else:
            attr.name = re.sub("[^0-9a-zA-Z]", " ", text.suffix(attr.name)).strip()

        if not attr.name:
            attr.name = "value"
        elif not attr.name[0].isalpha():
            attr.name = f"value_{attr.name}"

    @classmethod
    def process_duplicate_attribute_names(cls, attrs: List[Attr]) -> None:
        """
        Sanitize duplicate attribute names that might exist by applying rename
        strategies.

        Steps:
            1. If more than two attributes share the same name or if they are
            enumerations append a numerical index to the attribute names.
            2. If one of the two fields has a specific namespace prepend it to the
            name. If possible rename the second field.
            3. Append the xml type to the name of one of the two attributes. if
            possible rename the second field or the field with xml type `attribute`.
        """
        grouped = group_by(attrs, lambda attr: attr.name.lower())
        for items in grouped.values():
            if len(items) == 1:
                continue

            if len(items) > 2 or items[0].is_enumeration:
                for index in range(1, len(items)):
                    num = 1
                    name = items[index].name.lower()

                    while any(
                        attr for attr in attrs if attr.name.lower() == f"{name}_{num}"
                    ):
                        num += 1

                    items[index].name = f"{name}_{num}"
            else:
                first, second = items
                if first.tag == second.tag and any((first.namespace, second.namespace)):
                    change = second if second.namespace else first
                    change.name = f"{change.namespace}_{change.name}"
                else:
                    change = second if second.is_attribute else first
                    change.name = f"{change.name}_{change.tag}"

    def find_enum(self, source: Class, attr_type: AttrType) -> Optional[Class]:
        """
        Find the enumeration source class for the given class and attribute
        type.

        Search in root classes an inner class and exclude native types.
        """
        if attr_type.native:
            return None

        if attr_type.forward:
            return self.find_inner(
                source,
                condition=lambda x: x.is_enumeration and x.name == attr_type.name,
            )

        qname = source.source_qname(attr_type.name)
        return self.container.find(qname, condition=lambda x: x.is_enumeration)

    @classmethod
    def find_inner(cls, target: Class, condition: Callable) -> Optional[Class]:
        """Find the first inner class that matches the given condition."""
        return next((inner for inner in target.inner if condition(inner)), None)
