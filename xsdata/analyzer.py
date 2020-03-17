from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType
from xsdata.utils import text


def simple_type(item: Class):
    return item.is_enumeration or item.is_abstract or item.is_common


@dataclass
class ClassAnalyzer:
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

    def process(self, classes: List[Class]) -> List[Class]:
        """
        Process class list in steps.

        Steps:
            * Merge redefined classes
            * Create a class qname index
            * Mark as abstract classes with the same qname
            * Flatten classes
            * Return a final class list for code generators.
        """

        self.merge_redefined_classes(classes)

        self.create_class_qname_index(classes)

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
            if item.is_enumeration or not (item.is_abstract or item.is_common)
        ]

        return primary_classes or all_classes

    def create_class_qname_index(self, classes: List[Class]):
        self.class_index.clear()
        self.processed.clear()
        for item in classes:
            self.class_index[item.source_qname()].append(item)

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
                    new_ext.restrictions.update(self_extension.restrictions, force=True)
                    winner.extensions.append(new_ext)

    def mark_abstract_duplicate_classes(self):
        """Search for groups with more than one class and mark as abstract any
        complex type with the same name as an element."""
        for classes in self.class_index.values():
            if len(classes) == 1:
                continue

            element = next(
                (obj for obj in classes if obj.is_element and not obj.is_abstract), None
            )

            if not element:
                continue

            for obj in classes:
                if obj is not element and not obj.is_common:
                    obj.is_abstract = True

    def flatten_classes(self):
        for classes in self.class_index.values():
            for obj in classes:
                if obj.key not in self.processed:
                    self.flatten_class(obj)

    def flatten_class(self, target: Class):
        """
        Flatten class extensions, attributes and inner classes.

        Steps:
            * Enum unions
            * Parent classes
            * Attributes
            * Inner classes
        """
        self.processed[target.key] = True

        if target.is_common:
            self.flatten_enumeration_unions(target)

        for extension in reversed(target.extensions):
            self.flatten_extension(target, extension)

        for attr in list(target.attrs):
            self.flatten_attribute(target, attr)

        for inner in target.inner:
            self.flatten_class(inner)

    def flatten_enumeration_unions(self, target: Class):

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
        If the extension class is found in the registry prepend it's attributes
        to the given class.

        The attribute list is deep cloned and each attribute type is
        prepended with the extension prefix if it isn't a reference to
        another schema.
        """
        if extension.type.native and not target.is_enumeration:
            return self.create_default_attribute(target, extension)

        type_qname = target.source_qname(extension.type.name)
        source = self.find_class(type_qname)
        if source is None:
            if self.is_extension_subset(target, extension):
                target.extensions.remove(extension)
        elif source is target:
            target.extensions.remove(extension)
        elif source.is_enumeration and not target.is_enumeration:
            self.create_default_attribute(target, extension)
        elif source.is_enumeration == target.is_enumeration:
            self.copy_attributes(source, target, extension)
        elif target.is_enumeration:
            target.extensions.remove(extension)

    def flatten_attribute(self, target: Class, attr: Attr):
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
                attr_type.self_ref = self.is_attribute_self_reference(target, attr_type)
                types.append(attr_type)
            elif source.is_enumeration:
                types.append(attr_type)
            elif len(source.attrs) == 1:
                source_attr = source.attrs[0]
                types.extend(source_attr.types)
                attr.restrictions.update(source_attr.restrictions)
                self.copy_inner_classes(source, target)
            else:
                types.append(AttrType(name=DataType.STRING.code, native=True))
                logger.warning("Missing type implementation: %s", source.type.__name__)

        attr.types = types

    def is_extension_subset(self, target, extension) -> bool:
        if not len(target.attrs):
            return False

        type_qname = target.source_qname(extension.type.name)
        source = self.find_class(type_qname, condition=None)

        if not source:
            return False

        source_attrs = {attr.name for attr in source.attrs}
        target_attrs = {attr.name for attr in target.attrs}
        return len(source_attrs - target_attrs) == 0

    def is_attribute_self_reference(self, target: Class, dependency: AttrType) -> bool:
        qname = target.source_qname(dependency.name)
        return self.find_class(qname, condition=lambda x: x is target) is not None

    @staticmethod
    def copy_attributes(source: Class, target: Class, extension: Extension):
        prefix = text.prefix(extension.type.name)
        target.inner.extend(source.inner)
        target.extensions.remove(extension)
        position = next(
            (
                index
                for index, attr in enumerate(target.attrs)
                if attr.index > extension.type.index
            ),
            len(target.attrs),
        )
        for attr in source.attrs:
            new_attr = attr.clone()
            new_attr.restrictions.update(extension.restrictions, force=True)
            if prefix:
                for attr_type in new_attr.types:
                    if not attr_type.native and attr_type.name.find(":") == -1:
                        attr_type.name = f"{prefix}:{attr_type.name}"

            target.attrs.insert(position, new_attr)
            position += 1

    @staticmethod
    def copy_inner_classes(source: Class, target: Class):
        for inner in source.inner:
            exists = next(
                (found for found in target.inner if found.name == inner.name), None
            )
            if not exists:
                target.inner.append(inner)

    @staticmethod
    def create_default_attribute(item: Class, extension: Extension):
        if extension.type.native_code == DataType.ANY_TYPE.code:
            attr = Attr(
                name="##any_element",
                index=0,
                wildcard=True,
                default=list if extension.restrictions.is_list else None,
                types=[extension.type.clone()],
                local_type=TagType.ANY,
                restrictions=extension.restrictions.clone(),
            )
        else:
            attr = Attr(
                name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                local_type=TagType.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)
