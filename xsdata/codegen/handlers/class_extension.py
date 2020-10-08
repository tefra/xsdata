from dataclasses import dataclass
from typing import Optional

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import SimpleType


@dataclass
class ClassExtensionHandler(HandlerInterface):
    """Reduce class extensions by copying or creating new attributes."""

    REMOVE_EXTENSION = 0
    FLATTEN_EXTENSION = 1
    IGNORE_EXTENSION = 2

    container: ContainerInterface

    def process(self, target: Class):
        """
        Iterate and process the target class's extensions in reverser order.

        The reverse order is necessary in order to maintain the correct
        attributes ordering during cloning.
        """
        for extension in reversed(target.extensions):
            self.process_extension(target, extension)

    def process_extension(self, target: Class, extension: Extension):
        """Slit the process of extension into schema data types and user
        defined types."""
        if extension.type.native:
            self.process_native_extension(target, extension)
        else:
            self.process_dependency_extension(target, extension)

    @classmethod
    def process_native_extension(cls, target: Class, extension: Extension):
        """
        Native type flatten handler.

        In case of enumerations copy the native data type to all enum
        members, otherwise create a default text value with the
        extension attributes.
        """
        if target.is_enumeration:
            cls.copy_extension_type(target, extension)
        else:
            cls.add_default_attribute(target, extension)

    def process_dependency_extension(self, target: Class, extension: Extension):
        """User defined type flatten handler."""
        source = self.find_dependency(extension.type)
        if not source:
            logger.warning("Missing extension type: %s", extension.type.name)
            target.extensions.remove(extension)
        elif not source.is_complex or source.is_enumeration:
            self.process_simple_extension(source, target, extension)
        else:
            self.process_complex_extension(source, target, extension)

    @classmethod
    def process_simple_extension(cls, source: Class, target: Class, ext: Extension):
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
            cls.add_default_attribute(target, ext)
        elif source.is_enumeration == target.is_enumeration:
            ClassUtils.copy_attributes(source, target, ext)
        else:  # this is an enumeration
            target.extensions.remove(ext)

    @classmethod
    def process_complex_extension(cls, source: Class, target: Class, ext: Extension):
        """
        Complex flatten extension handler for primary classes eg ComplexType,
        Element.

        Compare source and target classes and either remove the
        extension completely, copy all source attributes to the target
        class or leave the extension alone.
        """
        res = cls.compare_attributes(source, target)
        if res == cls.REMOVE_EXTENSION:
            target.extensions.remove(ext)
        elif res == cls.FLATTEN_EXTENSION:
            ClassUtils.copy_attributes(source, target, ext)
        else:
            logger.debug("Ignore extension: %s", ext.type.name)

    def find_dependency(self, attr_type: AttrType) -> Optional[Class]:
        """
        Find dependency for the given extension type with priority.

        Search priority: xs:SimpleType >  xs:ComplexType
        """

        conditions = (lambda x: x.type is SimpleType, lambda x: x.type is ComplexType)

        for condition in conditions:
            result = self.container.find(attr_type.qname, condition=condition)
            if result:
                return result

        return None

    @classmethod
    def compare_attributes(cls, source: Class, target: Class) -> int:
        """
        Compare the attributes of the two classes and return whether the source
        class can and should be flattened.

        Remove:
            1. Source is the Target
            2. Target includes all the source attributes

        Flatten:
            1. Source includes some of the target attributes
            2. The source class is marked to be forced flattened
            3. Source class includes an attribute that needs to be last
            4. Target class includes an attribute that needs to be last
            5. Source class is a simple type
        """
        if source is target:
            return cls.REMOVE_EXTENSION

        if target.attrs and source.attrs:
            source_attrs = {attr.name for attr in source.attrs}
            target_attrs = {attr.name for attr in target.attrs}
            difference = source_attrs - target_attrs

            if not difference:
                return cls.REMOVE_EXTENSION
            if len(difference) != len(source_attrs):
                return cls.FLATTEN_EXTENSION

        if (
            source.strict_type
            or (source.has_suffix_attr and target.attrs)
            or target.has_suffix_attr
            or source.is_simple_type
        ):
            return cls.FLATTEN_EXTENSION

        return cls.IGNORE_EXTENSION

    @classmethod
    def copy_extension_type(cls, target: Class, extension: Extension):
        """Add the given extension type to all target attributes types and
        remove it from the target class extensions."""

        for attr in target.attrs:
            attr.types.append(extension.type.clone())
        target.extensions.remove(extension)

    @classmethod
    def add_default_attribute(cls, target: Class, extension: Extension):
        """Add a default value field to the given class based on the extension
        type."""
        if extension.type.native_code != DataType.ANY_TYPE.code:
            tag = Tag.EXTENSION
            name = "value"
            default = None
            namespace = None
        else:
            tag = Tag.ANY
            name = "any_element"
            default = list if extension.restrictions.is_list else None
            namespace = NamespaceType.ANY

        attr = cls.get_or_create_attribute(target, name, tag)
        attr.types.append(extension.type.clone())
        attr.restrictions.merge(extension.restrictions)
        attr.namespace = namespace
        attr.default = default
        target.extensions.remove(extension)

    @classmethod
    def get_or_create_attribute(cls, target: Class, name: str, tag: str) -> Attr:
        """Find or create for the given parameters an attribute in the target
        class."""
        for attr in target.attrs:
            if attr.name == attr.local_name == name and attr.tag == tag:
                return attr

        attr = Attr(name=name, local_name=name, tag=tag)
        target.attrs.insert(0, attr)
        return attr
