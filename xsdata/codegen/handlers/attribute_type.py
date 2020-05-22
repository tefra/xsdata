from dataclasses import dataclass
from typing import Optional
from typing import Set

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.exceptions import AnalyzerValueError
from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.enums import DataType
from xsdata.utils.classes import ClassUtils
from xsdata.utils.collections import unique_sequence


@dataclass
class AttributeTypeHandler(HandlerInterface):
    """Minimize class attributes complexity by filtering and flattening
    types."""

    container: ContainerInterface

    def process(self, target: Class):
        """
        Process the given class attributes and their types.

        Ensure all types are unique.
        """
        for attr in list(target.attrs):
            for attr_type in list(attr.types):
                self.process_type(target, attr, attr_type)

            attr.types = unique_sequence(attr.types, key="name")

    def process_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """
        Process attribute type, split process for xml schema and user defined
        types.

        Ignore forward references to inner classes.
        """
        if attr_type.native:
            self.process_native_type(attr, attr_type)
        elif attr_type.forward:
            logger.debug("Skipping attribute type that points to inner class.")
        else:
            self.process_dependency_type(target, attr, attr_type)

    @classmethod
    def process_native_type(cls, attr: Attr, attr_type: AttrType):
        """Reset attribute type if the attribute has a pattern restriction as
        they are not yet supported."""
        if attr.restrictions.pattern:
            cls.reset_attribute_type(attr_type)

    def find_dependency(self, target: Class, attr_type: AttrType) -> Optional[Class]:
        """
        Find dependency for the given attribute.

        Avoid conflicts by search in order:
            1. Non element/complexType
            2. Non abstract
            3. anything
        """
        qname = target.source_qname(attr_type.name)
        result = self.container.find(qname, condition=lambda obj: not obj.is_complex)
        if result:
            return result

        result = self.container.find(qname, condition=lambda x: not x.abstract)
        if result:
            return result

        return self.container.find(qname)

    def process_dependency_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """
        Process user defined attribute types, split process between complex and
        simple types.

        Reset absent attribute types with a warning.

        Complex Type: xs:Element and xs:ComplexType
        Simple stype: the rest
        """

        source = self.find_dependency(target, attr_type)
        if not source:
            logger.warning("Missing type: %s", attr_type.name)
            self.reset_attribute_type(attr_type)
        elif source.is_complex and not source.is_enumeration:
            self.process_complex_dependency(source, target, attr, attr_type)
        else:
            self.process_simple_dependency(source, target, attr, attr_type)

    @classmethod
    def process_simple_dependency(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Replace the given attribute type with the types of the single field
        source class.

        Ignore enumerations and gracefully handle dump types with no attributes.

        :raises: AnalyzerValueError if the source class has more than one attributes
        """
        if source.is_enumeration:
            return

        total = len(source.attrs)
        if total == 0:
            cls.reset_attribute_type(attr_type)
        elif total == 1:
            source_attr = source.attrs[0]
            index = attr.types.index(attr_type)
            attr.types.pop(index)

            for source_attr_type in source_attr.types:
                clone_type = source_attr_type.clone()
                attr.types.insert(index, clone_type)
                index += 1

            restrictions = source_attr.restrictions.clone()
            restrictions.merge(attr.restrictions)
            attr.restrictions = restrictions
            ClassUtils.copy_inner_classes(source, target)
        else:
            raise AnalyzerValueError(
                f"{source.type.__name__} with more than one attribute: `{source.name}`"
            )

    def process_complex_dependency(
        self, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Process complex attribute type.

        Abstract: If it can not be flattened remove abstract flag
        Non abstract: check for circular references.
        """
        if not source.abstract:
            attr_type.circular = self.is_circular_dependency(source, target)
        elif not source.extensions or source.attrs:
            source.abstract = False
        else:
            index = attr.types.index(attr_type)
            attr.types.pop(index)
            for extension in source.extensions:
                clone_type = extension.type.clone()
                attr.types.insert(index, clone_type)
                index += 1

                attr.restrictions.merge(extension.restrictions)

    def is_circular_dependency(
        self, source: Class, target: Class, seen: Optional[Set] = None
    ) -> bool:
        """Check if any source dependencies recursively match the target
        class."""

        if source is target:
            return True

        seen = seen or set()
        for qname in source.dependencies():

            if qname in seen:
                continue

            seen.add(qname)
            check = self.container.find(qname)
            if check and self.is_circular_dependency(check, target, seen):
                return True

        return False

    @classmethod
    def reset_attribute_type(cls, attr_type: AttrType):
        """Reset the attribute type to native string."""
        attr_type.name = DataType.STRING.code
        attr_type.native = True
        attr_type.circular = False
        attr_type.forward = False
