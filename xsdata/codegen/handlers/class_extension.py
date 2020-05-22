from dataclasses import dataclass
from typing import Optional

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.logger import logger
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.elements import ComplexType
from xsdata.models.elements import SimpleType
from xsdata.utils.classes import ClassUtils


@dataclass
class ClassExtensionHandler(HandlerInterface):
    """Reduce class extensions by copying or creating new attributes."""

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
            ClassUtils.copy_extension_type(target, extension)
        else:
            ClassUtils.create_default_attribute(target, extension)

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
            ClassUtils.create_default_attribute(target, ext)
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
        res = ClassUtils.compare_attributes(source, target)
        if res == ClassUtils.INCLUDES_ALL:
            target.extensions.remove(ext)
        elif (
            res == ClassUtils.INCLUDES_SOME
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
