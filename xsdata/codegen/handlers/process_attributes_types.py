from typing import Dict, Optional

from xsdata.codegen.mixins import ContainerInterface, RelativeHandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType, Tag
from xsdata.utils import collections


class ProcessAttributeTypes(RelativeHandlerInterface):
    """Minimize class attrs complexity by filtering and flattening types.

    Args:
        container: The container instance

    Attributes:
        dependencies: Class qname dependencies mapping
    """

    __slots__ = "dependencies"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.dependencies: Dict = {}

    def process(self, target: Class):
        """Process the given class attrs and their types.

        Cascades class restrictions to class attrs.

        Args:
            target: The target class instance
        """
        for attr in list(target.attrs):
            self.process_types(target, attr)
            self.cascade_properties(target, attr)

    def process_types(self, target: Class, attr: Attr):
        """Process every attr type and filter out duplicates.

        Args:
            target: The target class instance
            attr: The attr instance
        """
        if self.container.config.output.ignore_patterns:
            attr.restrictions.pattern = None

        for attr_type in list(attr.types):
            self.process_type(target, attr, attr_type)

        attr.types = ClassUtils.filter_types(attr.types)

    @classmethod
    def cascade_properties(cls, target: Class, attr: Attr):
        """Cascade class properties to the attr if it's a text node.

        Properties:
            - Default value
            - Fixed flag
            - Nillable flag

        Args:
            target: The target class instance
            attr: The attr instance
        """
        if attr.xml_type is None:
            if target.default is not None and attr.default is None:
                attr.default = target.default
                attr.fixed = target.fixed

            if target.nillable:
                attr.restrictions.nillable = True

    def process_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Process attr type.

        Cases:
            - Attr type is a native xsd type
            - Attr type is a forward reference (inner class)
            - Attr type is a complex user defined type

        Args:
            target: The target class instance
            attr: The attr instance
            attr_type: The attr type instance
        """
        if attr_type.native:
            self.process_native_type(attr, attr_type)
        elif attr_type.forward:
            self.process_inner_type(target, attr, attr_type)
        else:
            self.process_dependency_type(target, attr, attr_type)

    @classmethod
    def process_native_type(cls, attr: Attr, attr_type: AttrType):
        """Process native xsd types.

        Cascade the datatype restrictions to the attr and also
        resets the type to a simple xsd:string if there is a pattern
        restriction.

        Args:
            attr: The attr instance
            attr_type: The attr type instance
        """
        datatype = attr_type.datatype

        assert datatype is not None

        cls.update_restrictions(attr, datatype)

        if attr.restrictions.pattern:
            cls.reset_attribute_type(attr_type)

    def find_dependency(self, attr_type: AttrType, tag: str) -> Optional[Class]:
        """Find the source type from the attr type and tag.

        Avoid conflicts by selecting any matching type by qname and preferably:
            1. Match the candidate object tag
            2. Match element again complexType
            3. Match non element and complexType
            4. Anything

        Args:
            attr_type: The attr type instance
            tag: The xml tag name, e.g. Element, Attribute, ComplexType

        Returns:
            The source class or None if no match is found
        """
        conditions = (
            lambda obj: obj.tag == tag,
            lambda obj: tag == Tag.ELEMENT and obj.tag == Tag.COMPLEX_TYPE,
            lambda obj: not obj.is_complex_type,
            lambda x: True,
        )

        for condition in conditions:
            result = self.container.find(attr_type.qname, condition=condition)
            if result:
                return result

        return None

    def process_inner_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Process an attr type that depends on a simple inner type.

        Skip If the source class is not simple type, or it's a circular reference.

        Args:
            target: The target class instance
            attr: The attr instance
            attr_type: The attr type instance
        """
        if attr_type.circular:
            attr_type.reference = target.ref
            return

        inner = self.container.find_inner(target, attr_type.qname)

        # If the inner class behaves as a simple type flatten it.
        if (
            len(inner.attrs) == 1
            and not inner.attrs[0].xml_type
            and not inner.extensions
        ):
            self.copy_attribute_properties(inner, target, attr, attr_type)
            target.inner.remove(inner)
        else:
            attr_type.reference = inner.ref

    def process_dependency_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Process an attr type that depends on any global type.

        Strategies:
            1. Reset absent types with a warning
            3. Copy format restriction from an enumeration
            2. Copy attribute properties from a simple type
            4. Set circular flag for the rest

        Args:
            target: The target class instance
            attr: The attr instance
            attr_type: The attr type instance
        """
        source = self.find_dependency(attr_type, attr.tag)
        if not source:
            logger.warning("Reset absent type: %s", attr_type.name)
            self.reset_attribute_type(attr_type, True)
        elif source.is_enumeration:
            attr.restrictions.min_length = None
            attr.restrictions.max_length = None
            attr.restrictions.format = collections.first(
                x.restrictions.format for x in source.attrs if x.restrictions.format
            )
            attr_type.reference = id(source)
        elif not source.is_complex_type:
            self.copy_attribute_properties(source, target, attr, attr_type)
        elif source.is_element and source.abstract:
            # Substitution groups with abstract elements are used like
            # placeholders and shouldn't be added as standalone fields.
            ClassUtils.remove_attribute(target, attr)
        else:
            if source.nillable:
                attr.restrictions.nillable = True

            attr_type.reference = id(source)
            self.detect_lazy_namespace(source, target, attr)

    @classmethod
    def copy_attribute_properties(
        cls,
        source: Class,
        target: Class,
        attr: Attr,
        attr_type: AttrType,
    ):
        """Replace the attr type with the types of the first attr in the source class.

        Ignore enumerations and gracefully handle dump types with no
        attrs.

        Args:
            source: The source class instance
            target: The target class instance
            attr: The attr instance
            attr_type: The attr type instance

        Raises:
            AnalyzerValueError: if the source class has more than one attributes
        """
        source_attr = source.attrs[0]
        index = attr.types.index(attr_type)
        attr.types.pop(index)

        for source_attr_type in source_attr.types:
            clone_type = source_attr_type.clone()
            attr.types.insert(index, clone_type)
            index += 1

            ClassUtils.copy_inner_class(source, target, clone_type)

        restrictions = source_attr.restrictions.clone()
        restrictions.merge(attr.restrictions)

        # Maintain occurrences no matter what!
        restrictions.min_occurs = attr.restrictions.min_occurs
        restrictions.max_occurs = attr.restrictions.max_occurs

        if source.nillable:
            restrictions.nillable = True

        attr.restrictions = restrictions
        attr.help = attr.help or source_attr.help
        attr.fixed = attr.fixed or source_attr.fixed
        attr.default = attr.default or source_attr.default

    @classmethod
    def reset_attribute_type(cls, attr_type: AttrType, use_str: bool = True):
        """Reset the attribute type to string or any simple type.

        The method will also unset the circular/forward flags, as native
        types only depend on python builtin types.

        Args:
            attr_type: The attr type instance to reset
            use_str: Whether to use xs:string or xs:anySimpleType
        """
        attr_type.qname = str(DataType.STRING if use_str else DataType.ANY_SIMPLE_TYPE)
        attr_type.native = True
        attr_type.circular = False
        attr_type.forward = False

    @classmethod
    def update_restrictions(cls, attr: Attr, datatype: DataType):
        """Helper method to copy the native datatype restriction to the attr.

        Sets:
            - The format restriction, e.g. hexBinary, base64Binary
            - The tokens flag for xs:NMTOKENS and xs:IDREFS

        Args:
            attr: The attr to update
            datatype: The datatype to extract the restrictions.
        """
        attr.restrictions.format = datatype.format

        if datatype in (DataType.NMTOKENS, DataType.IDREFS):
            attr.restrictions.tokens = True

    @classmethod
    def detect_lazy_namespace(cls, source: Class, target: Class, attr: Attr):
        """Set the attr namespace if the current is marked as lazy.

        Cases:
            WSDL message part type can be an element, complex or
            simple type, we can't do the detection during the initial
            mapping to class objects.

        Args:
            source: The source class instance
            target: The target class instance
            attr: The target class attr instance
        """
        if attr.namespace == "##lazy":
            logger.warning(
                "Overriding field type namespace %s:%s (%s)",
                target.name,
                attr.name,
                source.namespace,
            )

            if not source.namespace:
                attr.namespace = "" if target.namespace else None
            else:
                attr.namespace = source.namespace
