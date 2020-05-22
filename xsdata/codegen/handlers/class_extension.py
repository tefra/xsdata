from dataclasses import dataclass

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.logger import logger
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.utils.classes import ClassUtils


def simple_cond(candidate: Class) -> bool:
    return candidate.is_enumeration or candidate.is_simple


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
            qname = target.source_qname(extension.type.name)
            simple_source = self.container.find(qname, simple_cond)
            complex_source = None if simple_source else self.container.find(qname)

            if simple_source:
                self.process_simple_extension(simple_source, target, extension)
            elif complex_source:
                self.process_complex_extension(complex_source, target, extension)
            else:
                logger.warning("Missing extension type: %s", extension.type.name)
                target.extensions.remove(extension)

    @classmethod
    def process_native_extension(cls, target: Class, extension: Extension):
        """Native type flatten extension handler, ignore enumerations."""
        if target.is_enumeration:
            ClassUtils.copy_extension_type(target, extension)
        else:
            ClassUtils.create_default_attribute(target, extension)

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
