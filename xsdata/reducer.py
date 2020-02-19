from dataclasses import dataclass
from dataclasses import field
from typing import Callable
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
    redefined_types: Dict[str, Class] = field(default_factory=dict)

    def process(self, schema: Schema, classes: List[Class]) -> List[Class]:
        """
        Process class list in steps.

        Steps:
            * Separate common/enumerations from class list
            * Add all common/enumerations to registry
            * Flatten the current common types
            * Flatten the generation types

        :return: The final list of normalized classes/enumerations
        """
        classes, common = self.separate_common_types(classes)

        self.add_common_types(common, schema)

        self.flatten_classes(common, schema)
        self.flatten_classes(classes, schema)

        self.redefined_types.clear()

        return [obj for obj in common if obj.is_enumeration] + classes

    def flatten_classes(self, classes: List[Class], schema: Schema):
        for obj in classes:
            self.flatten_class(obj, schema)

    def add_common_types(self, classes: List[Class], schema: Schema):
        """Add class to the common types registry with its qualified name with
        the target namespace."""

        for item in classes:
            qname = etree.QName(schema.target_namespace, item.name).text
            if qname in self.common_types:
                self.flatten_class(item, schema)
                self.redefined_types[qname] = item
            else:
                self.common_types[qname] = item

    def find_common_type(self, name: str, schema: Schema) -> Optional[Class]:
        """Find a common type by the qualified named with the prefixed
        namespace if exists or the target namespace."""
        prefix, suffix = text.split(name)
        namespace = schema.target_namespace

        if prefix:
            name = suffix
            namespace = schema.nsmap.get(prefix)

        qname = etree.QName(namespace, name)

        redefined = self.redefined_types.get(qname.text)
        return redefined or self.common_types.get(qname.text)

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

    def separate_common_types(self, classes: List[Class]):
        def condition(x: Class):
            return x.is_enumeration or x.is_abstract or x.is_common

        matches = self.pop_classes(classes, condition=condition)
        return classes, matches

    @staticmethod
    def pop_classes(classes: List[Class], condition: Callable) -> List[Class]:
        """Pop and return the objects matching the given condition from the
        given list of of classes."""
        matches = []
        for i in range(len(classes) - 1, -1, -1):
            if condition(classes[i]):
                matches.append(classes.pop(i))

        return list(reversed(matches))

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
