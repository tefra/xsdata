import copy
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

from lxml import etree

from xsdata.logger import logger
from xsdata.models.codegen import Attr, AttrType, Class, Extension
from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.utils.text import split


@dataclass
class ClassReducer:
    """The purpose of this class is to minimize the number of generated classes
    because of excess verbosity in the given xsd schema and duplicate types."""

    common_types: Dict[str, Class] = field(default_factory=dict)

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

        self.add_common_types(common, schema.target_namespace)

        self.flatten_classes(common, schema)
        self.flatten_classes(classes, schema)

        return [obj for obj in common if obj.is_enumeration] + classes

    def flatten_classes(self, classes: List[Class], schema: Schema):
        for obj in classes:
            self.flatten_class(obj, schema)

    def add_common_types(self, classes: List[Class], namespace: Optional[str]):
        """Add class to the common types registry with its qualified name with
        the target namespace."""

        self.common_types.update(
            {etree.QName(namespace, obj.name).text: obj for obj in classes}
        )

    def find_common_type(self, name: str, schema: Schema) -> Optional[Class]:
        """Find a common type by the qualified named with the prefixed
        namespace if exists or the target namespace."""
        prefix = None
        split_name = name.split(":")
        if len(split_name) == 2:
            prefix, name = split_name

        namespace = schema.nsmap.get(prefix, schema.target_namespace)
        qname = etree.QName(namespace, name)
        return self.common_types.get(qname.text)

    def flatten_class(self, item: Class, schema: Schema):
        """
        Flatten class traits from the common types registry.

        Steps:
            * Parent classes
            * Attributes
            * Inner classes
        """
        for extension in list(item.extensions):
            self.flatten_extension(item, extension, schema)

        for attr in item.attrs:
            self.flatten_attribute(attr, schema)

        for inner in item.inner:
            self.flatten_class(inner, schema)

    def flatten_extension(
        self, item: Class, extension: Extension, schema: Schema
    ):
        """
        If the extension class is found in the registry prepend it's attributes
        to the given class.

        The attribute list is deep cloned and each attribute type is
        prepended with the extension prefix if it isn't a reference to
        another schema.
        """
        common = self.find_common_type(extension.name, schema)
        if common is None:
            return

        if not (extension.is_restriction and item.is_enumeration):
            self.copy_attributes(common, item, extension)

        item.extensions.remove(extension)

    @staticmethod
    def copy_attributes(source: Class, target: Class, extension: Extension):
        prefix, ext = split(extension.name)
        target.inner.extend(copy.deepcopy(source.inner))
        new_attrs = copy.deepcopy(source.attrs)
        position = next(
            (
                index
                for index, attr in enumerate(target.attrs)
                if attr.index > extension.index
            ),
            0,
        )
        for attr in new_attrs:
            if prefix:
                for attr_type in attr.types:
                    if attr_type.name.find(":") == -1:
                        attr_type.name = f"{prefix}:{attr_type.name}"

            target.attrs.insert(position, attr)
            position += 1

    def flatten_attribute(self, attr: Attr, schema: Schema):
        """
        If the attribute type is found in the registry overwrite the given
        attribute type and merge the restrictions.

        If the common type doesn't have just one attribute fallback to
        the default xsd type xs:string
        """
        types = []
        for attr_type in attr.types:
            common = self.find_common_type(attr_type.name, schema)
            restrictions = {}
            if common is None or common.is_enumeration:
                types.append(attr_type)
            elif len(common.attrs) == 1:
                common_attr = common.attrs[0]
                types.extend(copy.deepcopy(common_attr.types))
                restrictions = common_attr.restrictions
            else:
                types.append(AttrType(name=XSDType.STRING.code))
                logger.warning(
                    "Missing type implementation: %s", common.type.__name__
                )

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


reducer = ClassReducer()
