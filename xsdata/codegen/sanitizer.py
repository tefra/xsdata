from dataclasses import dataclass
from typing import List
from typing import Optional

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.collections import first
from xsdata.utils.collections import group_by
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import clean_uri
from xsdata.utils.namespaces import split_qname
from xsdata.utils.text import alnum


@dataclass
class ClassSanitizer:
    """Prepare all the classes attributes for code generation and cleanup after
    the analyzer processors."""

    container: ClassContainer

    def process(self):
        """Iterate through all classes and run the sanitizer procedure."""

        for target in self.container.iterate():
            self.process_class(target)

        self.resolve_conflicts()

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
        collections.apply(target.inner, self.process_class)

        if self.container.config.output.compound_fields:
            self.group_compound_fields(target)

        for attr in target.attrs:
            self.process_attribute_restrictions(attr)
            self.process_attribute_default(target, attr)
            self.process_attribute_sequence(target, attr)

        self.process_duplicate_attribute_names(target.attrs)

    def group_compound_fields(self, target: Class):
        """Group and process target attributes by the choice group."""

        groups = group_by(target.attrs, lambda x: x.restrictions.choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1 and any(attr.is_list for attr in attrs):
                self.group_fields(target, attrs)

    def group_fields(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""

        pos = target.attrs.index(attrs[0])
        choice = attrs[0].restrictions.choice
        sum_occurs = choice and choice.startswith("effective_")
        names = []
        choices = []
        min_occurs = []
        max_occurs = []
        for attr in attrs:
            target.attrs.remove(attr)
            names.append(attr.local_name)
            min_occurs.append(attr.restrictions.min_occurs or 0)
            max_occurs.append(attr.restrictions.max_occurs or 0)
            choices.append(self.build_attr_choice(attr))

        if len(names) > 3 or len(names) != len(set(names)):
            name = "choice"
        else:
            name = "_Or_".join(names)

        target.attrs.insert(
            pos,
            Attr(
                name=name,
                index=0,
                types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=sum(min_occurs) if sum_occurs else min(min_occurs),
                    max_occurs=sum(max_occurs) if sum_occurs else max(max_occurs),
                ),
                choices=choices,
            ),
        )

    def process_attribute_default(self, target: Class, attr: Attr):
        """
        Sanitize attribute default value.

        Cases:
            1. Ignore enumerations.
            2. List fields can not have a fixed value.
            3. Optional fields or xsi:type can not have a default or fixed value.
            4. Convert string literal default value for enum fields.
        """

        if attr.is_enumeration:
            return

        if attr.is_optional or attr.is_xsi_type:
            attr.fixed = False
            attr.default = None

        if attr.default:
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
            source = self.find_enum(attr_type)
            if not source:
                continue

            source_found = True
            source_attr = first(x for x in source.attrs if x.default == attr.default)

            if source_attr:
                attr.default = f"@enum@{source.qname}::{source_attr.name}"
                return

        if source_found:
            logger.warning(
                "No enumeration member matched %s.%s default value `%s`",
                target.name,
                attr.local_name,
                attr.default,
            )
            attr.default = None

    def resolve_conflicts(self):
        """Find classes with the same case insensitive qualified name and
        rename them."""
        groups = group_by(self.container.iterate(), lambda x: alnum(x.qname))
        for classes in groups.values():
            if len(classes) > 1:
                self.rename_classes(classes)

    def rename_classes(self, classes: List[Class]):
        """
        Rename all the classes in the list.

        Protect classes derived from xs:element if there is only one in
        the list.
        """
        total_elements = sum(x.is_element for x in classes)
        for target in classes:
            if not target.is_element or total_elements > 1:
                self.rename_class(target)

    def rename_class(self, target: Class):
        """Find the next available class identifier, save the original name in
        the class metadata and update the class qualified name and all classes
        that depend on the target class."""

        qname = target.qname
        namespace, name = split_qname(target.qname)
        target.qname = self.next_qname(namespace, name)
        target.meta_name = name
        self.container.reset(target, qname)

        for item in self.container.iterate():
            self.rename_class_dependencies(item, qname, target.qname)

    def next_qname(self, namespace: str, name: str) -> str:
        """Append the next available index number for the given namespace and
        local name."""
        index = 0
        reserved = set(map(alnum, self.container.data.keys()))
        while True:
            index += 1
            qname = build_qname(namespace, f"{name}_{index}")
            if alnum(qname) not in reserved:
                return qname

    def rename_class_dependencies(self, target: Class, search: str, replace: str):
        """Search and replace the old qualified attribute type name with the
        new one if it exists in the target class attributes, extensions and
        inner classes."""
        for attr in target.attrs:
            self.rename_attr_dependencies(attr, search, replace)

        for ext in target.extensions:
            if ext.type.qname == search:
                ext.type.qname = replace

        for inner in target.inner:
            self.rename_class_dependencies(inner, search, replace)

    def rename_attr_dependencies(self, attr: Attr, search: str, replace: str):
        """Search and replace the old qualified attribute type name with the
        new one in the attr types, choices and default value."""
        for attr_type in attr.types:
            if attr_type.qname == search:
                attr_type.qname = replace

                if isinstance(attr.default, str) and attr.default.startswith("@enum@"):
                    attr.default = attr.default.replace(search, replace)

        for choice in attr.choices:
            self.rename_attr_dependencies(choice, search, replace)

    def find_enum(self, attr_type: AttrType) -> Optional[Class]:
        """Find an enumeration class byte the attribute type."""
        if attr_type.native:
            return None

        return self.container.find(
            attr_type.qname, condition=lambda x: x.is_enumeration
        )

    @classmethod
    def process_attribute_restrictions(cls, attr: Attr):
        """Sanitize attribute required flag by comparing the min/max
        occurrences restrictions."""
        restrictions = attr.restrictions
        min_occurs = restrictions.min_occurs or 0
        max_occurs = restrictions.max_occurs or 0

        if attr.is_attribute:
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif attr.is_tokens:
            restrictions.required = None
            if max_occurs <= 1:
                restrictions.min_occurs = None
                restrictions.max_occurs = None
        elif attr.xml_type is None or min_occurs == max_occurs == 1:
            restrictions.required = True
            restrictions.min_occurs = None
            restrictions.max_occurs = None
        elif min_occurs == 0 and max_occurs < 2:
            restrictions.required = None
            restrictions.min_occurs = None
            restrictions.max_occurs = None
            attr.default = None
            attr.fixed = False
        else:  # max_occurs > 1
            restrictions.min_occurs = min_occurs
            restrictions.required = None
            attr.fixed = False

        if attr.default or attr.fixed or attr.restrictions.nillable:
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
    def process_duplicate_attribute_names(cls, attrs: List[Attr]) -> None:
        """Sanitize duplicate attribute names that might exist by applying
        rename strategies."""
        grouped = group_by(attrs, lambda attr: alnum(attr.name))
        for items in grouped.values():
            total = len(items)
            if total == 2 and not items[0].is_enumeration:
                cls.rename_attribute_by_preference(*items)
            elif total > 1:
                cls.rename_attributes_with_index(attrs, items)

    @classmethod
    def rename_attributes_with_index(cls, attrs: List[Attr], rename: List[Attr]):
        """Append the next available index number to all the rename attributes
        names."""
        for index in range(1, len(rename)):
            num = 1
            name = rename[index].name

            while any(alnum(attr.name) == alnum(f"{name}_{num}") for attr in attrs):
                num += 1

            rename[index].name = f"{name}_{num}"

    @classmethod
    def rename_attribute_by_preference(cls, a: Attr, b: Attr):
        """
        Decide and rename one of the two given attributes.

        When both attributes are derived from the same xs:tag and one of the two fields
        has a specific namespace prepend it to the name. Preferable rename the second
        attribute.

        Otherwise append the derived from tag to the name of one of the two attributes.
        Preferably rename the second field or the field derived from xs:attribute.
        """
        if a.tag == b.tag and (a.namespace or b.namespace):
            change = b if b.namespace else a
            assert change.namespace is not None
            change.name = f"{clean_uri(change.namespace)}_{change.name}"
        else:
            change = b if b.is_attribute else a
            change.name = f"{change.name}_{change.tag}"

    @classmethod
    def build_attr_choice(cls, attr: Attr) -> Attr:
        """
        Converts the given attr to a choice.

        The most important part is the reset of certain restrictions
        that don't make sense as choice metadata like occurrences.
        """
        restrictions = attr.restrictions.clone()
        restrictions.min_occurs = None
        restrictions.max_occurs = None
        restrictions.sequential = None

        return Attr(
            name=attr.local_name,
            namespace=attr.namespace,
            default=attr.default,
            types=attr.types,
            tag=attr.tag,
            help=attr.help,
            restrictions=restrictions,
        )
