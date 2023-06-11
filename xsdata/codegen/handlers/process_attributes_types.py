from typing import Dict
from typing import Optional
from typing import Set
from typing import Tuple

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils import collections


class ProcessAttributeTypes(RelativeHandlerInterface):
    """Minimize class attributes complexity by filtering and flattening
    types."""

    __slots__ = "dependencies"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.dependencies: Dict = {}

    def process(self, target: Class):
        """Process the given class attributes and their types."""
        for attr in list(target.attrs):
            self.process_types(target, attr)
            self.cascade_properties(target, attr)

    def process_types(self, target: Class, attr: Attr):
        """Process every attr type and filter out duplicates."""
        if self.container.config.output.ignore_patterns:
            attr.restrictions.pattern = None

        for attr_type in list(attr.types):
            self.process_type(target, attr, attr_type)

        attr.types = ClassUtils.filter_types(attr.types)

    @classmethod
    def cascade_properties(cls, target: Class, attr: Attr):
        """Cascade target class default/fixed/nillable properties to the given
        attr if it's a text node."""
        if attr.xml_type is None:
            if target.default is not None and attr.default is None:
                attr.default = target.default
                attr.fixed = target.fixed

            if target.nillable:
                attr.restrictions.nillable = True

    def process_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Process attribute type, split process for xml schema and user
        defined types."""
        if attr_type.native:
            self.process_native_type(attr, attr_type)
        elif attr_type.forward:
            self.process_inner_type(target, attr, attr_type)
        else:
            self.process_dependency_type(target, attr, attr_type)

    @classmethod
    def process_native_type(cls, attr: Attr, attr_type: AttrType):
        """
        Process native attribute types.

        - Update restrictions from the datatype
        - Reset attribute type if there is a pattern restriction
        """
        datatype = attr_type.datatype

        assert datatype is not None

        cls.update_restrictions(attr, datatype)

        if attr.restrictions.pattern:
            cls.reset_attribute_type(attr_type)

    def find_dependency(self, attr_type: AttrType, tag: str) -> Optional[Class]:
        """
        Find dependency for the given attribute and tag.

        Avoid conflicts by selecting any matching type by qname and preferably:
            1. Match the candidate object tag
            2. Match element again complexType
            3. Match non element and complexType
            4. Anything
        """
        conditions = (
            lambda obj: obj.tag == tag,
            lambda obj: tag == Tag.ELEMENT and obj.tag == Tag.COMPLEX_TYPE,
            lambda obj: not obj.is_complex,
            lambda x: True,
        )

        for condition in conditions:
            result = self.container.find(attr_type.qname, condition=condition)
            if result:
                return result

        return None

    def process_inner_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """
        Process an attributes type that depends on an inner type.

        Ignore inner circular references.
        """
        if attr_type.circular:
            return

        inner = self.container.find_inner(target, attr_type.qname)
        if inner.is_simple_type:
            self.copy_attribute_properties(inner, target, attr, attr_type)
            target.inner.remove(inner)

    def process_dependency_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """
        Process an attributes type that depends on any global type.

        Strategies:
            1. Reset absent types with a warning
            2. Copy attribute properties from a simple type
            3. Copy format restriction from an enumeration
            4. Set circular flag for the rest
        """
        source = self.find_dependency(attr_type, attr.tag)
        if not source:
            logger.warning("Reset absent type: %s", attr_type.name)
            use_str = not source or not source.is_complex
            self.reset_attribute_type(attr_type, use_str)
        elif source.is_simple_type:
            self.copy_attribute_properties(source, target, attr, attr_type)
        elif source.is_enumeration:
            attr.restrictions.min_length = None
            attr.restrictions.max_length = None
            attr.restrictions.format = collections.first(
                x.restrictions.format for x in source.attrs if x.restrictions.format
            )
            attr_type.reference = id(source)
        elif source.is_element and source.abstract:
            # Substitution groups with abstract elements are used like
            # placeholders and shouldn't be added as standalone fields.
            ClassUtils.remove_attribute(target, attr)
        else:
            if source.nillable:
                attr.restrictions.nillable = True
            self.set_circular_flag(source, target, attr_type)
            self.detect_lazy_namespace(source, target, attr)

    @classmethod
    def copy_attribute_properties(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Replace the given attribute type with the types of the single field
        source class.

        Ignore enumerations and gracefully handle dump types with no
        attributes.

        :raises: AnalyzerValueError if the source class has more than
            one attributes
        """
        source_attr = source.attrs[0]
        index = attr.types.index(attr_type)
        attr.types.pop(index)

        for source_attr_type in source_attr.types:
            clone_type = source_attr_type.clone()
            attr.types.insert(index, clone_type)
            index += 1

            ClassUtils.copy_inner_class(source, target, attr, clone_type)

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

    def set_circular_flag(self, source: Class, target: Class, attr_type: AttrType):
        """Update circular reference flag."""
        attr_type.reference = id(source)
        attr_type.circular = self.is_circular_dependency(source, target, set())

        if attr_type.circular:
            logger.debug("Possible circular reference %s, %s", target.name, source.name)

    def is_circular_dependency(self, source: Class, target: Class, seen: Set) -> bool:
        """Check if any source dependencies recursively match the target
        class."""

        if source is target or source.status == Status.FLATTENING:
            return True

        for qname in self.cached_dependencies(source):
            if qname not in seen:
                seen.add(qname)
                check = self.container.find(qname)
                if check and self.is_circular_dependency(check, target, seen):
                    return True

        return False

    def cached_dependencies(self, source: Class) -> Tuple[str]:
        """Returns from cache the source class dependencies as a collection of
        qualified names."""
        cache_key = id(source)
        if cache_key not in self.dependencies:
            self.dependencies[cache_key] = tuple(source.dependencies())

        return self.dependencies[cache_key]

    @classmethod
    def reset_attribute_type(cls, attr_type: AttrType, use_str: bool = True):
        """Reset the attribute type to string or any simple type."""
        attr_type.qname = str(DataType.STRING if use_str else DataType.ANY_SIMPLE_TYPE)
        attr_type.native = True
        attr_type.circular = False
        attr_type.forward = False

    @classmethod
    def update_restrictions(cls, attr: Attr, datatype: DataType):
        attr.restrictions.format = datatype.format

        if datatype in (DataType.NMTOKENS, DataType.IDREFS):
            attr.restrictions.tokens = True

    @classmethod
    def detect_lazy_namespace(cls, source: Class, target: Class, attr: Attr):
        """
        Override attr namespace with the source namespace when during the
        initial mapping the namespace detection wasn't possible.

        Case 1: WSDL message part type can be an element, complex or
        simple type, we can't do the detection during the initial
        mapping to class objects.
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
