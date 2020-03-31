from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.exceptions import AnalyzerError
from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.enums import DataType
from xsdata.utils import text
from xsdata.utils.codegen import ClassUtils


def simple_type(item: Class):
    return item.is_enumeration or item.abstract or item.is_common


@dataclass
class ClassAnalyzer(ClassUtils):
    """
    Class analyzer is responsible to minize the final classes footprint by
    merging and flattening extensions and attributes.

    Also promotes the classes necessary for generation and demotes the
    classes to be used as common types for future runs.
    """

    processed: Dict = field(default_factory=dict)
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
            * Merge redefined classes
            * Create a class index
            * Create a substitution index
            * Mark as abstract classes with the same qname
            * Flatten classes
            * Return a final class list for code generators.
        """

        self.merge_redefined_classes(classes)

        self.create_class_index(classes)

        self.create_substitutions_index(classes)

        self.mark_abstract_duplicate_classes()

        self.flatten_classes()

        gen_classes = self.fetch_classes_for_generation()

        return gen_classes

    def fetch_classes_for_generation(self) -> List[Class]:
        """
        Return the qualified classes to continue for code generation. Return
        all if there are not primary classes.

        Qualifications:
            * not an abstract
            * type: element | complexType | simpleType with enumerations
        """
        all_classes = [item for values in self.class_index.values() for item in values]
        primary_classes = [
            item
            for item in all_classes
            if item.is_enumeration or not (item.abstract or item.is_common)
        ]

        classes = primary_classes or all_classes

        for target in classes:
            self.sanitize_attributes(target)

        return classes

    def create_class_index(self, classes: List[Class]):
        """Group classes by their fully qualified name."""
        self.class_index.clear()
        for item in classes:
            self.class_index[item.source_qname()].append(item)

    def create_substitutions_index(self, classes: List[Class]):
        """Create reference attributes for all the classes substitutions and
        group them by their fully qualified name."""
        for item in classes:
            for substitution in item.substitutions:
                item.abstract = False
                qname = item.source_qname(substitution)
                attr = self.create_reference_attribute(item, qname)
                self.substitutions_index[qname].append(attr)

    def find_class(self, qname: QName, condition=simple_type) -> Optional[Class]:
        candidates = list(filter(condition, self.class_index.get(qname, [])))
        if candidates:
            candidate = candidates.pop(0)
            if candidates:
                logger.warning("More than one candidate found for %s", qname)

            if candidate.key not in self.processed:
                self.flatten_class(candidate)
            return candidate

        return None

    def merge_redefined_classes(self, classes: List[Class]):
        """Merge original and redefined classes."""
        grouped: Dict[str, List[Class]] = defaultdict(list)
        for item in classes:
            grouped[f"{item.type.__name__}{item.source_qname()}"].append(item)

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

                self.copy_attributes(item, winner, self_extension)
                for looser_ext in item.extensions:
                    new_ext = looser_ext.clone()
                    new_ext.restrictions.merge(self_extension.restrictions)
                    winner.extensions.append(new_ext)

    def mark_abstract_duplicate_classes(self):
        """Search for groups with more than one class and mark as abstract any
        complex type with the same name as an element."""
        for classes in self.class_index.values():
            if len(classes) == 1:
                continue

            element = next(
                (obj for obj in classes if obj.is_element and not obj.abstract), None
            )

            if not element:
                continue

            for obj in classes:
                if obj is not element and not obj.is_common:
                    obj.abstract = True

    def flatten_classes(self):
        for classes in self.class_index.values():
            for obj in classes:
                if obj.key not in self.processed:
                    self.flatten_class(obj)

    def flatten_class(self, target: Class):
        """
        Simplify class footprint by flattening class extensions, attributes and
        inner classes.

        Steps:
            * Merge enum unions
            * Expand attribute groups
            * Copy extensions attributes
            * Flatten attribute types
            * Merge duplicate attributes
            * Unset sequential attributes
            * Flatten inner classes
        """
        self.processed[target.key] = True

        self.flatten_enumeration_unions(target)

        for attr in list(target.attrs):
            self.expand_attribute_group(target, attr)

        for extension in reversed(target.extensions):
            self.flatten_extension(target, extension)

        for attr in list(target.attrs):
            self.flatten_attribute_types(target, attr)

        for attr in list(target.attrs):
            self.add_substitution_attrs(target, attr)

        self.merge_duplicate_attributes(target)

        for inner in target.inner:
            self.flatten_class(inner)

    def flatten_enumeration_unions(self, target: Class):
        if not target.is_common:
            return

        if len(target.attrs) == 1 and target.attrs[0].name == "value":
            all_enums = True
            attrs = []
            for attr_type in target.attrs[0].types:
                is_enumeration = False
                if attr_type.forward_ref and len(target.inner) == 1:
                    if target.inner[0].is_enumeration:
                        is_enumeration = True
                        attrs.extend(target.inner[0].attrs)

                elif not attr_type.forward_ref and not attr_type.native:
                    type_qname = target.source_qname(attr_type.name)
                    source = self.find_class(type_qname)

                    if source is not None and source.is_enumeration:
                        is_enumeration = True
                        attrs.extend(source.attrs)

                if not is_enumeration:
                    all_enums = False

            if all_enums:
                target.attrs = attrs

    def flatten_extension(self, target: Class, extension: Extension):
        """
        Remove if possible the given extension for the target class.

        If extension type is xsd native and target is not enumeration
        create a default value attribute otherwise delegate the task to
        the responsible handler based on the extension source type
        complex or simple.
        """
        if extension.type.native and not target.is_enumeration:
            return self.create_default_attribute(target, extension)

        type_qname = target.source_qname(extension.type.name)
        simple_source = self.find_class(type_qname)

        if simple_source:
            return self.flatten_extension_simple(simple_source, target, extension)

        complex_source = self.find_class(type_qname, condition=None)
        if complex_source:
            return self.flatten_extension_complex(complex_source, target, extension)

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
        elif target.is_enumeration:
            target.extensions.remove(ext)

    def flatten_extension_complex(self, source: Class, target: Class, ext: Extension):
        """
        Complex flatten extension handler for primary classes eg ComplexType,
        Element.

        Steps:
            1. If source includes all target attributes: drop the extension
            2. If source includes some of the target attributes copy attributes
            3. If source depends on target class copy all attributes
            4. Otherwise maintain the extension.
        """
        res = self.compare_attributes(source, target)
        if res == self.INCLUDES_ALL:
            target.extensions.remove(ext)
        elif res == self.INCLUDES_SOME:
            self.copy_attributes(source, target, ext)
        elif self.class_depends_on(source, target):
            self.copy_attributes(source, target, ext)

    def expand_attribute_group(self, target: Class, attr: Attr):
        """
        Expand a group attribute with the source class attributes.

        Clone the attributes and apply the group restrictions as well.
        """

        if not attr.is_group:
            return

        attr_qname = target.source_qname(attr.name)
        source = self.find_class(attr_qname, condition=None)

        if not source:
            raise AnalyzerError(f"Group attribute not found: `{attr_qname}`")
        elif source is target:
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
        Flatten attribute types by using the source attribute type.

        Steps:
            * Skip xsd native types
            * Detect circular references if no source is found
            * Skip enumeration types
            * Overwrite attribute type from source
        """
        types = []
        for attr_type in attr.types:
            source = None
            if not attr_type.native:
                type_qname = target.source_qname(attr_type.name)
                source = self.find_class(type_qname)

            if source is None:
                attr_type.self_ref = self.attr_depends_on(attr_type, target)
                types.append(attr_type)
            elif source.is_enumeration:
                types.append(attr_type)
            elif len(source.attrs) == 1:
                source_attr = source.attrs[0]
                types.extend(source_attr.types)
                restrictions = source_attr.restrictions.clone()
                restrictions.merge(attr.restrictions)
                attr.restrictions = restrictions
                self.copy_inner_classes(source, target)
            else:
                types.append(AttrType(name=DataType.STRING.code, native=True))
                logger.warning("Missing type implementation: %s", source.type.__name__)

        attr.types = types

    def add_substitution_attrs(self, target: Class, attr: Attr):
        """
        Find all the substitution attributes for the given attribute and add
        them to the target class.

        Exclude enumerations and wildcard attributes.
        """
        if attr.is_enumeration or attr.wildcard:
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

    def class_depends_on(self, source: Class, target: Class) -> bool:
        """Check if any source dependencies recursively match the target
        class."""
        for qname in source.dependencies():
            check = self.find_class(qname, condition=None)
            if check is target or (check and self.class_depends_on(check, target)):
                return True

        return False

    def attr_depends_on(self, dependency: AttrType, target: Class) -> bool:
        """Check if dependency or any of its dependencies match the target
        class."""
        qname = target.source_qname(dependency.name)
        source = self.find_class(qname, condition=None)

        if source is None:
            return False
        elif source is target:
            return True
        else:
            return self.class_depends_on(source, target)
