from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.exceptions import AnalyzerError
from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.utils import text
from xsdata.utils.classes import ClassUtils
from xsdata.utils.collections import unique_sequence


@dataclass
class ClassAnalyzer(ClassUtils):
    """
    Class analyzer is responsible to minize the final classes footprint by
    merging and flattening extensions and attributes.

    Also promotes the classes necessary for generation and demotes the
    classes to be used as common types for future runs.
    """

    MAX_DEPENDENCY_CHECK_DEPTH = 5

    processed: List = field(default_factory=list)
    class_index: Dict[QName, List[Class]] = field(
        default_factory=lambda: defaultdict(list)
    )
    substitutions_index: Dict[QName, List[Attr]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def process(self, classes: List[Class]) -> List[Class]:
        """
        Process class list in steps.

        Steps:
            * Create a class index.
            * Handle duplicate types.
            * Create a substitution index.
            * Flatten classes.
            * Return a final class list for code generators.
        """

        self.create_class_index(classes)

        self.handle_duplicate_classes()

        self.create_substitutions_index()

        self.flatten_classes()

        self.sanitize_classes()

        return self.fetch_classes_for_generation()

    def handle_duplicate_classes(self):
        """
        Remove if possible classes with the same qualified name.

        Steps:
            1. Remove classes with missing extension type.
            2. Merge redefined classes.
            3. Fix implied abstract flags.
        """
        for classes in self.class_index.values():

            if len(classes) > 1:
                self.remove_invalid_classes(classes)

            if len(classes) > 1:
                self.merge_redefined_classes(classes)

            if len(classes) > 1:
                self.update_abstract_classes(classes)

    def remove_invalid_classes(self, classes: List[Class]):
        """Remove from the given class list any class with missing extension
        type."""
        for target in list(classes):
            if any(
                self.attr_type_is_missing(target, extension.type)
                for extension in target.extensions
            ):
                classes.remove(target)

    def fetch_classes_for_generation(self) -> List[Class]:
        """
        Return the qualified classes for code generation.

        Return all if no classes are derived from xs:element or
        xs:complexType.
        """
        classes = [item for values in self.class_index.values() for item in values]
        if any(item.is_complex for item in classes):
            classes = list(filter(lambda x: x.is_enumeration or x.is_complex, classes))

        return classes

    def create_class_index(self, classes: List[Class]):
        """Group classes by their fully qualified name."""
        self.class_index.clear()
        for item in classes:
            self.class_index[item.source_qname()].append(item)

    def create_substitutions_index(self):
        """Create reference attributes for all the classes substitutions and
        group them by their fully qualified name."""

        for classes in self.class_index.values():
            for item in classes:
                for substitution in item.substitutions:
                    item.abstract = False
                    qname = item.source_qname(substitution)
                    attr = self.create_reference_attribute(item, qname)
                    self.substitutions_index[qname].append(attr)

    def find_attr_type(self, source: Class, attr_type: AttrType) -> Optional[Class]:
        """Find the source class for the given class and attribute type."""
        qname = source.source_qname(attr_type.name)
        return self.find_class(qname)

    def attr_type_is_missing(self, source: Class, attr_type: AttrType) -> bool:
        """Check if given type declaration is not native and is missing."""
        if attr_type.native:
            return False

        qname = source.source_qname(attr_type.name)
        return qname not in self.class_index

    def find_attr_simple_type(
        self, source: Class, attr_type: AttrType
    ) -> Optional[Class]:
        """Find the source class for the given class and attribute type,
        excluding enumerations, complex types and self references."""
        qname = source.source_qname(attr_type.name)
        return self.find_class(
            qname,
            condition=lambda x: not x.is_enumeration
            and not x.is_complex
            and x is not source,
        )

    def find_simple_class(self, qname: QName) -> Optional[Class]:
        """Find an enumeration or simple type source class for the given
        qualified name."""
        return self.find_class(
            qname, condition=lambda x: x.is_enumeration or x.is_simple,
        )

    def find_class(
        self, qname: QName, condition: Optional[Callable] = None
    ) -> Optional[Class]:
        """Find the flattened source class for the given qualified name."""
        candidates = list(filter(condition, self.class_index.get(qname, [])))
        if candidates:
            candidate = candidates.pop(0)
            if candidates:
                logger.warning("More than one candidate found for %s", qname)

            if id(candidate) not in self.processed:
                self.flatten_class(candidate)
            return candidate

        return None

    def flatten_classes(self):
        """Flatten the class index objects once."""
        for classes in self.class_index.values():
            for obj in classes:
                if id(obj) not in self.processed:
                    self.flatten_class(obj)

    def flatten_class(self, target: Class):
        """
        Simplify class footprint by flattening class extensions, attributes and
        inner classes.

        Steps:
            * Expand attribute groups
            * Flatten extensions
            * Flatten attribute types
            * Add substitution attributes
            * Merge duplicate attributes
            * Create mixed content attribute
            * Flatten inner classes
        """
        self.processed.append(id(target))

        for attr in list(target.attrs):
            self.expand_attribute_group(target, attr)

        for extension in reversed(target.extensions):
            self.flatten_extension(target, extension)

        for attr in list(target.attrs):
            self.flatten_attribute_types(target, attr)

        for attr in list(target.attrs):
            self.add_substitution_attrs(target, attr)

        self.merge_duplicate_attributes(target)

        self.create_mixed_attribute(target)

        for inner in target.inner:
            if id(inner) not in self.processed:
                self.flatten_class(inner)

    def flatten_extension(self, target: Class, extension: Extension):
        """
        Flatten target class extension based on the extension type.

        Types:
            1. Native primitive type (int, str, float, etc)
            2. Simple source type (simpleType, Extension)
            3. Complex source type (ComplexType, Element)
            4. Unknown type
        """
        if extension.type.native:
            self.flatten_extension_native(target, extension)
        else:
            qname = target.source_qname(extension.type.name)
            simple_source = self.find_simple_class(qname)
            complex_source = None if simple_source else self.find_class(qname)

            if simple_source:
                self.flatten_extension_simple(simple_source, target, extension)
            elif complex_source:
                self.flatten_extension_complex(complex_source, target, extension)
            else:
                logger.warning("Missing extension type: %s", extension.type.name)
                target.extensions.remove(extension)

    def flatten_extension_native(self, target: Class, extension: Extension):
        """Native type flatten extension handler, ignore enumerations."""
        if target.is_enumeration:
            self.copy_extension_type(target, extension)
        else:
            self.create_default_attribute(target, extension)

    def flatten_extension_simple(self, source: Class, target: Class, ext: Extension):
        """
        Simple flatten extension handler for common classes eg SimpleType,
        Restriction.

        Steps:
            1. If target is source: drop the extension.
            2. If source is enumeration and target isn't create default value attribute.
            3. If both source and target are enumerations copy all attributes.
            4. If both source and target are not enumerations copy all attributes.
            5. If target is enumeration: drop the extension.
        """
        if source is target:
            target.extensions.remove(ext)
        elif source.is_enumeration and not target.is_enumeration:
            self.create_default_attribute(target, ext)
        elif source.is_enumeration == target.is_enumeration:
            self.copy_attributes(source, target, ext)
        else:  # this is an enumeration
            target.extensions.remove(ext)

    def flatten_extension_complex(self, source: Class, target: Class, ext: Extension):
        """
        Complex flatten extension handler for primary classes eg ComplexType,
        Element.

        Drop extension when:
            - source includes all target attributes
        Copy all attributes when:
            - source includes some of the target attributes
            - source has suffix attribute and target has at least one attribute
            - target has at least one suffix attribute
            - source or target class is abstract
        """
        res = self.compare_attributes(source, target)
        if res == self.INCLUDES_ALL:
            target.extensions.remove(ext)
        elif (
            res == self.INCLUDES_SOME
            or source.abstract
            or target.abstract
            or (source.has_suffix_attr and len(target.attrs) > 0)
            or target.has_suffix_attr
        ):
            self.copy_attributes(source, target, ext)

    def expand_attribute_group(self, target: Class, attr: Attr):
        """
        Expand a group attribute with the source class attributes.

        Clone the attributes and apply the group restrictions as well.
        """

        if not attr.is_group:
            return

        attr_qname = target.source_qname(attr.name)
        source = self.find_class(attr_qname)

        if not source:
            raise AnalyzerError(f"Group attribute not found: `{attr_qname}`")

        if source is target:
            target.attrs.remove(attr)
        else:
            index = target.attrs.index(attr)
            target.attrs.pop(index)
            prefix = text.prefix(attr.name)

            for source_attr in source.attrs:
                clone = self.clone_attribute(source_attr, attr.restrictions, prefix)
                target.attrs.insert(index, clone)
                index += 1

            self.copy_inner_classes(source, target)

    def flatten_attribute_types(self, target: Class, attr: Attr):
        """
        Loop over the the given attribute types to flatten simple definitions.

        Notes:
            * xs:pattern is not yet supported reset all native types to xs:string.
            * skip over forward references aka inner classes.
            * Copy all parent extensions if class is enumeration.
        """
        for current_type in list(attr.types):
            if current_type.native:
                if attr.restrictions.pattern:
                    self.reset_attribute_type(current_type)
            elif not current_type.forward_ref:
                self.flatten_attribute_type(target, attr, current_type)

        attr.types = unique_sequence(attr.types, key="name")

    def flatten_attribute_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Flatten attribute type if it's a simple type otherwise check for
        circular reference or missing type."""
        simple_source = self.find_attr_simple_type(target, attr_type)
        if simple_source:
            self.merge_attribute_type(simple_source, target, attr, attr_type)
        else:
            complex_source = self.find_attr_type(target, attr_type)
            if complex_source:
                attr_type.self_ref = self.class_depends_on(complex_source, target)
            elif not attr_type.self_ref:
                logger.warning("Missing type: %s", attr_type.name)
                self.reset_attribute_type(attr_type)

    def add_substitution_attrs(self, target: Class, attr: Attr):
        """
        Find all the substitution attributes for the given attribute and add
        them to the target class.

        Exclude enumerations and wildcard attributes.
        """
        if attr.is_enumeration or attr.is_wildcard:
            return

        index = target.attrs.index(attr)
        qname = target.source_qname(attr.name)
        for substitution in self.substitutions_index[qname]:
            pos = self.find_attribute(target.attrs, substitution)
            index = pos + 1 if pos > -1 else index

            clone = substitution.clone()
            clone.restrictions.merge(attr.restrictions)
            target.attrs.insert(index, clone)

            self.add_substitution_attrs(target, clone)

    def sanitize_classes(self):
        """Sanitize the class index objects."""
        for classes in self.class_index.values():
            for target in classes:
                self.sanitize_class(target)

    def sanitize_class(self, target: Class):
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
            self.sanitize_class(inner)

        for attr in target.attrs:
            self.sanitize_attribute_default_value(target, attr)
            self.sanitize_attribute_restrictions(attr)
            self.sanitize_attribute_name(attr)

        for i in range(len(target.attrs)):
            self.sanitize_attribute_sequence(target.attrs, i)

        self.sanitize_duplicate_attribute_names(target.attrs)

    def sanitize_attribute_default_value(self, target: Class, attr: Attr):
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

        if attr.default:
            self.sanitize_attribute_default_enum(target, attr)

    def sanitize_attribute_default_enum(self, target: Class, attr: Attr):
        """
        Convert string literal default value for enum fields.

        Loop through all attributes types and search for enum sources.
        If an enum source exist map the default string literal value to
        a qualified name. Inner enum references are ignored.
        """
        for attr_type in attr.types:
            if attr_type.native:
                continue
            if attr_type.forward_ref:
                attr.default = None
                continue

            source = self.find_class(
                target.source_qname(attr_type.name),
                condition=lambda x: x.is_enumeration,
            )

            if not source:
                continue

            enumeration = next(
                (x.name for x in source.attrs if x.default == attr.default), None,
            )

            if not enumeration:
                raise AnalyzerError(
                    f"Unknown enumeration {source.name}: {attr.default}"
                )

            attr.default = f"@enum@{source.name}.{enumeration}"

    def class_depends_on(self, source: Class, target: Class, depth: int = 1) -> bool:
        """Check if any source dependencies recursively match the target
        class."""

        if source is target:
            return True

        if depth > self.MAX_DEPENDENCY_CHECK_DEPTH:
            return False

        for qname in source.dependencies():
            check = self.find_class(qname)
            if check and self.class_depends_on(check, target, depth + 1):
                return True

        return False
