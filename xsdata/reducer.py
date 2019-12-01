import copy
import logging
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

from lxml import etree

from xsdata.models.codegen import Attr, Class
from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.utils.text import split_prefix

logger = logging.getLogger(__name__)


def is_enumeration(obj: Class) -> bool:
    return obj.is_enumeration


def is_common(obj: Class) -> bool:
    return obj.is_common


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
        namespace = schema.target_namespace
        nsmap = schema.nsmap

        enumerations = self.pop_classes(classes, condition=is_enumeration)
        common_types = self.pop_classes(classes, condition=is_common)

        self.add_common_types(enumerations, namespace)
        self.add_common_types(common_types, namespace)

        self.flatten_classes(common_types, nsmap)
        self.flatten_classes(classes, nsmap)

        return enumerations + classes

    def flatten_classes(self, classes: List[Class], nsmap: Dict):
        for obj in classes:
            self.flatten_class(obj, nsmap)

    def add_common_types(self, classes: List[Class], namespace: Optional[str]):
        """Add class to the common types registry with its qualified name with
        the target namespace."""

        self.common_types.update(
            {etree.QName(namespace, obj.name).text: obj for obj in classes}
        )

    def find_common_type(self, name: str, nsmap: Dict) -> Optional[Class]:
        """Find a common type by the qualified named with the namespace
        prefix."""
        prefix = None
        split_name = name.split(":")
        if len(split_name) == 2:
            prefix, name = split_name

        namespace = nsmap.get(prefix)
        qname = etree.QName(namespace, name)
        return self.common_types.get(qname.text)

    def flatten_class(self, item: Class, nsmap: Dict):
        """
        Flatten class traits from the common types registry.

        Steps:
            * Parent classes
            * Attributes
            * Inner classes
        """
        for extension in list(item.extensions):
            self.flatten_extension(item, extension, nsmap)

        for attr in item.attrs:
            self.flatten_attribute(attr, nsmap)

        for inner in item.inner:
            self.flatten_class(inner, nsmap)

    def flatten_extension(self, item: Class, extension: str, nsmap: Dict):
        """
        If the extension class is found in the registry prepend it's attributes
        to the given class.

        The attribute list is deep cloned and each attribute type is
        prepended with the extension prefix if it isn't a reference to
        another schema.
        """
        common = self.find_common_type(extension, nsmap)
        if common is not None:
            prefix, ext = split_prefix(extension)
            new_attrs = copy.deepcopy(common.attrs)
            if prefix:
                for attr in new_attrs:
                    if attr.type.find(":") == -1:
                        attr.type = f"{prefix}:{attr.type}"

            item.attrs = new_attrs + item.attrs
            item.extensions.remove(extension)

    def flatten_attribute(self, attr: Attr, nsmap: Dict):
        """
        If the attribute type is found in the registry overwrite the given
        attribute type and merge the restrictions.

        If the common type doesn't have just one attribute fallback to
        the default xsd type xs:string
        """
        common = self.find_common_type(attr.type, nsmap)
        if common is not None:
            if len(common.attrs) == 1:
                value = common.attrs[0]
                attr.type = value.type
                for key, value in value.restrictions.items():
                    setattr(attr, key, value)
            else:
                logger.debug(
                    f"Missing type implementation: {common.type.__name__}"
                )
                attr.type = XSDType.STRING.code

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
