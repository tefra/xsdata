import sys
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml import etree

from xsdata.exceptions import AnalyzerValueError
from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Restrictions
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

    common_types: Dict[etree.QName, Class] = field(default_factory=dict)
    processed: Dict = field(default_factory=dict)
    class_index: Dict[etree.QName, List[Class]] = field(
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

        return self.fetch_classes_for_generation()

    def fetch_classes_for_generation(self) -> List[Class]:
        """
        Return the qualified classes to continue for code generation.

        The rest of the classes are stored as common types to be used later
        by the next schemas in the process.

        Qualifications:
            * not an abstract
            * type: element | complexType | simpleType with enumerations
        """
        result = []
        for classes in self.class_index.values():
            for item in classes:
                should_store = item.is_common or item.is_abstract

                if should_store:
                    self.common_types[item.source_qname()] = item

                if not should_store or item.is_enumeration:
                    result.append(item)

        return result

    def create_class_qname_index(self, classes: List[Class]):
        self.class_index.clear()
        self.processed.clear()
        for item in classes:
            self.class_index[item.source_qname()].append(item)

    def flatten_classes(self):
        for classes in self.class_index.values():
            for obj in classes:
                if obj.key not in self.processed:
                    self.flatten_class(obj)

    def is_self_referencing(self, item: Class, dependency: AttrType) -> bool:
        dependency_qname = item.source_qname(dependency.name)
        return (
            self.find_class(dependency_qname, condition=lambda x: x is item) is not None
        )

    def find_class(self, qname: etree.QName, condition=simple_type) -> Optional[Class]:
        item = self.find_schema_class(qname, condition=condition)
        return item or self.find_common_class(qname, condition=condition)

    def find_common_class(self, qname: str, condition=None):
        if qname in self.common_types:
            candidate = self.common_types[qname]
            return candidate if not condition or condition(candidate) else None
        else:
            return None

    def find_schema_class(self, qname: str, condition=None) -> Optional[Class]:
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
            grouped[f"{item.type.__name__}{item.name}"].append(item)

        for items in grouped.values():
            if len(items) == 1:
                continue
            if len(items) > 2:
                raise AnalyzerValueError(
                    f"Redefined class `{items[0].name}` more than once."
                )

            winner: Class = items.pop()
            looser: Class = items.pop()
            classes.remove(looser)

            self_extension = next(
                (
                    ext
                    for ext in winner.extensions
                    if text.suffix(ext.type.name) == winner.name
                ),
                None,
            )

            if self_extension:
                winner.extensions.remove(self_extension)
                self.copy_attributes(looser, winner, self_extension)
                for looser_ext in looser.extensions:
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

    def flatten_class(self, item: Class):
        """
        Flatten class traits from the common types registry.

        Steps:
            * Enum unions
            * Parent classes
            * Attributes
            * Inner classes
        """
        self.processed[item.key] = True

        if item.is_common:
            self.flatten_enumeration_unions(item)

        for extension in list(item.extensions):
            self.flatten_extension(item, extension)

        for attr in list(item.attrs):
            self.flatten_attribute(item, attr)

        for inner in item.inner:
            self.flatten_class(inner)

    def flatten_enumeration_unions(self, item: Class):

        if len(item.attrs) == 1 and item.attrs[0].name == "value":
            all_enums = True
            attrs = []
            for attr_type in item.attrs[0].types:
                is_enumeration = False
                if attr_type.forward_ref and len(item.inner) == 1:
                    if item.inner[0].is_enumeration:
                        is_enumeration = True
                        attrs.extend(item.inner[0].attrs)

                elif not attr_type.forward_ref and not attr_type.native:
                    type_qname = item.source_qname(attr_type.name)
                    common = self.find_class(type_qname)

                    if common is not None and common.is_enumeration:
                        is_enumeration = True
                        attrs.extend(common.attrs)

                if not is_enumeration:
                    all_enums = False

            if all_enums:
                item.attrs = attrs

    def flatten_extension(self, item: Class, extension: Extension):
        """
        If the extension class is found in the registry prepend it's attributes
        to the given class.

        The attribute list is deep cloned and each attribute type is
        prepended with the extension prefix if it isn't a reference to
        another schema.
        """
        if extension.type.native and not item.is_enumeration:
            self.create_default_attribute(item, extension)
        else:
            type_qname = item.source_qname(extension.type.name)
            common = self.find_class(type_qname)
            if common is None:
                return
            elif common is item:
                pass
            elif not item.is_enumeration and common.is_enumeration:
                self.create_default_attribute(item, extension)
            elif not item.is_enumeration or common.is_enumeration:
                self.copy_attributes(common, item, extension)

        item.extensions.remove(extension)

    def flatten_attribute(self, item: Class, attr: Attr):
        """
        If the attribute type is found in the registry overwrite the given
        attribute type and merge the restrictions.

        If the common type doesn't have just one attribute fallback to
        the default xsd type xs:string
        """
        types = []
        for attr_type in attr.types:
            common = None
            if not attr_type.native:
                type_qname = item.source_qname(attr_type.name)
                common = self.find_class(type_qname)

            if common is None:
                attr_type.self_ref = self.is_self_referencing(item, attr_type)
                types.append(attr_type)
            elif common.is_enumeration:
                types.append(attr_type)
            elif len(common.attrs) == 1:
                common_attr = common.attrs[0]
                types.extend(common_attr.types)
                attr.restrictions.update(common_attr.restrictions)
                self.copy_inner_classes(common, item)
            else:
                types.append(AttrType(name=DataType.STRING.code, native=True))
                logger.warning("Missing type implementation: %s", common.type.__name__)

        attr.types = types

    @staticmethod
    def copy_attributes(source: Class, target: Class, extension: Extension):
        prefix = text.prefix(extension.type.name)
        target.inner.extend(source.inner)
        position = next(
            (
                index
                for index, attr in enumerate(target.attrs)
                if attr.index > extension.type.index
            ),
            0,
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
            restrictions = Restrictions(min_occurs=0, max_occurs=sys.maxsize)
            restrictions.update(extension.restrictions, force=True)
            attr = Attr(
                name="##any_element",
                index=0,
                wildcard=True,
                default=list if restrictions.is_list else None,
                types=[extension.type.clone()],
                local_type=TagType.ANY,
                restrictions=restrictions,
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


analyzer = ClassAnalyzer()
