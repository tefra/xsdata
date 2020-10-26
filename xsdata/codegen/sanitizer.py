import re
from dataclasses import dataclass
from typing import List
from typing import Optional

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrChoice
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.collections import first
from xsdata.utils.collections import group_by
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import clean_uri
from xsdata.utils.namespaces import split_qname


@dataclass
class ClassSanitizer:
    """Prepare all the classes attributes for code generation and cleanup after
    the analyzer processors."""

    container: ClassContainer
    config: GeneratorConfig

    @classmethod
    def process(cls, container: ClassContainer, config: GeneratorConfig):
        """Iterate through all classes and run the sanitizer procedure."""

        sanitizer = cls(container, config)

        collections.apply(container.iterate(), sanitizer.process_class)

        sanitizer.resolve_conflicts()

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

        if self.config.output.compound_fields:
            self.group_compound_fields(target)

        for attr in target.attrs:
            self.process_attribute_default(target, attr)
            self.process_attribute_restrictions(attr)
            self.process_attribute_name(attr)
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
        names = []
        choices = []
        min_occurs = []
        max_occurs = []
        for attr in attrs:
            target.attrs.remove(attr)
            names.append(attr.local_name)
            min_occurs.append(attr.restrictions.min_occurs)
            max_occurs.append(attr.restrictions.max_occurs)
            choices.append(self.build_attr_choice(attr))

        name = "choice" if len(names) > 3 else "_Or_".join(names)
        target.attrs.insert(
            pos,
            Attr(
                name=name,
                local_name=name,
                index=0,
                types=[AttrType(qname=DataType.ANY_TYPE.qname, native=True)],
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=min((x for x in min_occurs if x is not None), default=0),
                    max_occurs=max((x for x in max_occurs if x is not None), default=0),
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

        if attr.is_list:
            attr.fixed = False

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
            source = self.find_enum(target, attr_type)
            if not source:
                continue

            source_found = True
            source_attr = first(x for x in source.attrs if x.default == attr.default)

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
        qname = build_qname(inner.target_namespace, name)
        parent.inner.remove(inner)

        for attr in parent.attrs:
            for attr_type in attr.types:
                if attr_type.name == inner.name:
                    attr_type.forward = False
                    attr_type.qname = qname

        inner.qname = qname

        self.container.add(inner)

    def resolve_conflicts(self):
        """Find classes with the same case insensitive qualified name and
        rename them."""
        groups = group_by(self.container.iterate(), lambda x: x.qname.lower())
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
            self.rename_dependency(item, qname, target.qname)

    def next_qname(self, namespace: str, name: str) -> str:
        """Append the next available index number for the given namespace and
        local name."""
        index = 0
        reserved = map(str.lower, self.container.keys())
        while True:
            index += 1
            qname = build_qname(namespace, f"{name}_{index}")
            if qname.lower() not in reserved:
                return qname

    def rename_dependency(self, target: Class, search: str, replace: str):
        """Search and replace the old qualified attribute type name with the
        new one if it exists in the target class attributes, extensions and
        inner classes."""
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.qname == search:
                    attr_type.qname = replace

        for ext in target.extensions:
            if ext.type.qname == search:
                ext.type.qname = replace

        for inner in target.inner:
            self.rename_dependency(inner, search, replace)

    def find_enum(self, source: Class, attr_type: AttrType) -> Optional[Class]:
        """
        Find the enumeration source class for the given class and attribute
        type.

        Search in root classes an inner class and exclude native types.
        """
        if attr_type.native:
            return None

        if attr_type.forward:
            for inner in source.inner:
                if inner.name == attr_type.name and inner.is_enumeration:
                    return inner

            return None

        qname = attr_type.qname
        return self.container.find(qname, condition=lambda x: x.is_enumeration)

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
            attr.name = re.sub("[^0-9a-zA-Z]", " ", attr.name).strip()

        if not attr.name:
            attr.name = "value"
        elif not attr.name[0].isalpha():
            attr.name = f"value_{attr.name}"

    @classmethod
    def process_duplicate_attribute_names(cls, attrs: List[Attr]) -> None:
        """Sanitize duplicate attribute names that might exist by applying
        rename strategies."""
        grouped = group_by(attrs, lambda attr: attr.name.lower())
        for items in grouped.values():
            if len(items) > 2 or items[0].is_enumeration:
                cls.rename_attributes_with_index(attrs, items)
            elif len(items) == 2:
                cls.rename_attribute_by_preference(*items)

    @classmethod
    def rename_attributes_with_index(cls, all_attrs: List[Attr], rename: List[Attr]):
        """Append the next available index number to all the rename attributes
        names."""
        for index in range(1, len(rename)):
            num = 1
            name = rename[index].name.lower()

            while any(attr.name.lower() == f"{name}_{num}" for attr in all_attrs):
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
    def build_attr_choice(cls, attr: Attr) -> AttrChoice:
        """
        Converts the given attr to a choice.

        The most important part is the reset of certain restrictions
        that don't make sense as choice metadata like occurrences.
        """
        restrictions = attr.restrictions.clone()
        restrictions.min_occurs = None
        restrictions.max_occurs = None
        restrictions.sequential = None

        return AttrChoice(
            name=attr.local_name,
            namespace=attr.namespace,
            default=attr.default,
            types=attr.types,
            tag=attr.tag,
            restrictions=restrictions,
        )
