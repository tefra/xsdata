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

    INCLUDES_NONE = 0
    INCLUDES_SOME = 1
    INCLUDES_ALL = 2

    container: ContainerInterface

    def process(self, target: Class):
        for extension in reversed(target.extensions):
            self.process_extension(target, extension)

    def process_extension(self, target: Class, extension: Extension):
        if extension.type.native:
            self.process_native_extension(target, extension)
        else:
            self.process_dependency_extension(target, extension)

    @classmethod
    def process_native_extension(cls, target: Class, extension: Extension):
        """Native type flatten extension handler, ignore enumerations."""
        if target.is_enumeration:
            cls.copy_extension_type(target, extension)
        else:
            cls.create_default_attribute(target, extension)

    def process_dependency_extension(self, target: Class, extension: Extension):
        source = self.find_dependency(target, extension.type)
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
            cls.create_default_attribute(target, ext)
        elif source.is_enumeration == target.is_enumeration:
            ClassUtils.copy_attributes(source, target, ext)
        else:  # this is an enumeration
            target.extensions.remove(ext)

    @classmethod
    def process_complex_extension(cls, source: Class, target: Class, ext: Extension):
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
        res = cls.compare_attributes(source, target)
        if res == cls.INCLUDES_ALL:
            target.extensions.remove(ext)
        elif (
            res == cls.INCLUDES_SOME
            or source.abstract
            or (source.has_suffix_attr and len(target.attrs) > 0)
            or target.has_suffix_attr
        ):
            ClassUtils.copy_attributes(source, target, ext)

    def find_dependency(self, target: Class, attr_type: AttrType) -> Optional[Class]:
        """
        Find dependency for the given extension type with priority.

        Search priority: xs:SimpleType >  xs:ComplexType
        """

        conditions = (
            lambda x: x.type is SimpleType,
            lambda x: x.type is ComplexType,
        )

        qname = target.source_qname(attr_type.name)
        for condition in conditions:
            result = self.container.find(qname, condition=condition)
            if result:
                return result

        return None

    @classmethod
    def compare_attributes(cls, source: Class, target: Class) -> int:
        """Compare the attributes of the two classes and return whether the
        source includes all, some or none of the target attributes."""
        if source is target:
            return cls.INCLUDES_ALL

        if not target.attrs:
            return cls.INCLUDES_NONE

        source_attrs = {attr.name for attr in source.attrs}
        target_attrs = {attr.name for attr in target.attrs}
        difference = source_attrs - target_attrs

        if not difference:
            return cls.INCLUDES_ALL
        if len(difference) != len(source_attrs):
            return cls.INCLUDES_SOME

        return cls.INCLUDES_NONE

    @classmethod
    def copy_extension_type(cls, target: Class, extension: Extension):
        """Add the given extension type to all target attributes types and
        remove it from the target class extensions."""

        for attr in target.attrs:
            attr.types.append(extension.type.clone())
        target.extensions.remove(extension)

    @classmethod
    def create_default_attribute(cls, item: Class, extension: Extension):
        """Add a default value field to the given class based on the extension
        type."""
        if extension.type.native_code == DataType.ANY_TYPE.code:
            attr = Attr(
                name="any_element",
                local_name="any_element",
                index=0,
                default=list if extension.restrictions.is_list else None,
                types=[extension.type.clone()],
                tag=Tag.ANY,
                namespace=NamespaceType.ANY.value,
                restrictions=extension.restrictions.clone(),
            )
        else:
            attr = Attr(
                name="value",
                local_name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                tag=Tag.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)
