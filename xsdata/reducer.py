from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml import etree

from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType
from xsdata.utils import text


@dataclass
class ClassReducer:
    """The purpose of this class is to minimize the number of generated classes
    because of excess verbosity in the given xsd schema and duplicate types."""

    common_types: Dict[str, Class] = field(default_factory=dict)
    processed: Dict = field(default_factory=dict)
    class_index: Dict = field(default_factory=lambda: defaultdict(list))

    def process(self, schema: Schema, classes: List[Class]) -> List[Class]:
        """
        Process class list in steps.

        Steps:
            * Merge redefined classes
            * Create a class qname index
            * Flatten classes
            * Store common types and return the rest
        """

        self.merge_classes(classes)

        self.index_classes(classes, schema)

        self.flatten_classes(classes, schema)

        remaining = self.store_common_types(classes, schema)

        return remaining

    def store_common_types(self, classes: List[Class], schema: Schema) -> List[Class]:
        result = []
        for item in classes:
            should_store = item.is_common or item.is_abstract

            if should_store:
                qname = self.qname(item.name, schema)
                self.common_types[qname] = item

            if not should_store or item.is_enumeration:
                result.append(item)

        return result

    def index_classes(self, classes: List[Class], schema: Schema):
        self.class_index.clear()
        self.processed.clear()
        for item in classes:
            qname = self.qname(item.name, schema)
            self.class_index[qname].append(item)

    def flatten_classes(self, classes: List[Class], schema: Schema):
        for obj in classes:
            if obj.key not in self.processed:
                self.processed[obj.key] = True
                self.flatten_class(obj, schema)

    def find_common_type(self, name: str, schema: Schema) -> Optional[Class]:
        """Find a common type by the qualified named with the prefixed
        namespace if exists or the target namespace."""

        qname = self.qname(name, schema)
        common = None
        candidates = self.class_index.get(qname)

        if candidates:
            common = next(
                (
                    item
                    for item in candidates
                    if item.is_common or item.is_abstract or item.is_enumeration
                ),
                None,
            )

        common = common or self.common_types.get(qname)

        if common and common.key not in self.processed:
            self.flatten_class(common, schema)

        return common

    def merge_classes(self, classes: List[Class]):
        """Merge original and redefined classes."""
        grouped: Dict[str, List[Class]] = defaultdict(list)
        for item in classes:
            grouped[f"{item.type.__name__}{item.name}"].append(item)

        for items in grouped.values():
            if len(items) == 1:
                continue
            if len(items) > 2:
                raise NotImplementedError(
                    f"Redefined class `{items[0].name}` more than once."
                )

            winner: Class = items.pop()
            looser: Class = items.pop()
            classes.remove(looser)

            for i in range(len(winner.attrs)):
                attr = winner.attrs[i]

                if attr.types[0].name == winner.name or attr.types[0].name.endswith(
                    f":{winner.name}"
                ):
                    restrictions = looser.attrs[i].restrictions
                    attr.types = looser.attrs[i].types
                    for key, value in restrictions.items():
                        if getattr(attr, key) is None:
                            setattr(attr, key, value)

            for i in range(len(winner.extensions) - 1, -1, -1):
                extension = winner.extensions[i]
                if extension.name == winner.name or extension.name.endswith(
                    f":{winner.name}"
                ):
                    winner.extensions.pop(i)
                    self.copy_attributes(looser, winner, extension)

    def flatten_class(self, item: Class, schema: Schema):
        """
        Flatten class traits from the common types registry.

        Steps:
            * Enum unions
            * Parent classes
            * Attributes
            * Inner classes
        """

        if item.is_common:
            self.flatten_enumeration_unions(item, schema)

        for extension in list(item.extensions):
            self.flatten_extension(item, extension, schema)

        for attr in item.attrs:
            self.flatten_attribute(item, attr, schema)

        for inner in item.inner:
            self.flatten_class(inner, schema)

    def flatten_enumeration_unions(self, item: Class, schema: Schema):

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
                    common = self.find_common_type(attr_type.name, schema)
                    if common is not None and common.is_enumeration:
                        is_enumeration = True
                        attrs.extend(common.attrs)

                if not is_enumeration:
                    all_enums = False

            if all_enums:
                item.attrs = attrs

    def flatten_extension(self, item: Class, extension: AttrType, schema: Schema):
        """
        If the extension class is found in the registry prepend it's attributes
        to the given class.

        The attribute list is deep cloned and each attribute type is
        prepended with the extension prefix if it isn't a reference to
        another schema.
        """
        if extension.native:
            return

        common = self.find_common_type(extension.name, schema)
        if common is None:
            return
        elif common is item:
            pass
        elif not item.is_enumeration and common.is_enumeration:
            self.create_default_attribute(item, extension)
        elif not item.is_enumeration:
            self.copy_attributes(common, item, extension)

        item.extensions.remove(extension)

    def flatten_attribute(self, item: Class, attr: Attr, schema: Schema):
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
                common = self.find_common_type(attr_type.name, schema)

            restrictions = {}
            if common is None or common.is_enumeration:
                types.append(attr_type)
            elif len(common.attrs) == 1:
                common_attr = common.attrs[0]
                types.extend(common_attr.types)
                restrictions = common_attr.restrictions
                self.copy_inner_classes(common, item)
            else:
                types.append(AttrType(name=DataType.STRING.code, native=True))
                logger.warning("Missing type implementation: %s", common.type.__name__)

            for key, value in restrictions.items():
                if getattr(attr, key) is None:
                    setattr(attr, key, value)

        attr.types = types

    @staticmethod
    def qname(name: str, schema: Schema) -> str:
        prefix, suffix = text.split(name)
        namespace = schema.target_namespace

        if prefix:
            name = suffix
            namespace = schema.nsmap.get(prefix)

        return etree.QName(namespace, name).text

    @staticmethod
    def copy_attributes(source: Class, target: Class, extension: AttrType):
        prefix = text.prefix(extension.name)
        target.inner.extend(source.inner)
        position = next(
            (
                index
                for index, attr in enumerate(target.attrs)
                if attr.index > extension.index
            ),
            0,
        )
        for attr in source.attrs:
            new_attr = attr.clone()
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
    def create_default_attribute(item: Class, extension: AttrType):
        item.attrs.append(
            Attr(
                name="value",
                index=0,
                default=None,
                types=[extension],
                local_type=TagType.EXTENSION,
            )
        )


reducer = ClassReducer()
