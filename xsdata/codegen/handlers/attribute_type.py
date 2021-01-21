from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.utils import collections


@dataclass
class AttributeTypeHandler(HandlerInterface):
    """Minimize class attributes complexity by filtering and flattening
    types."""

    container: ContainerInterface
    dependencies: Dict = field(default_factory=dict)

    def process(self, target: Class):
        """
        Process the given class attributes and their types.

        Ensure all types are unique.
        """
        for attr in list(target.attrs):
            for attr_type in list(attr.types):
                self.process_type(target, attr, attr_type)

            attr.types = self.filter_types(attr.types)

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

        Avoid conflicts by search in order:
            1. Non element/complexType
            2. Non abstract
            3. anything
        """
        conditions = (
            lambda obj: obj.tag == tag,
            lambda obj: not obj.is_complex,
            lambda x: not x.abstract,
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
            1. Reset absent or dummy attribute types with a warning
            2. Copy attribute properties from a simple type
            3. Copy format restriction from an enumeration
            4. Set circular flag for the rest
        """

        source = self.find_dependency(attr_type, attr.tag)
        if not source or (not source.attrs and not source.extensions):
            logger.warning("Reset dummy type: %s", attr_type.name)
            use_str = not source or not source.is_complex
            self.reset_attribute_type(attr_type, use_str)
        elif source.is_simple_type:
            self.copy_attribute_properties(source, target, attr, attr_type)
        elif source.is_enumeration:
            attr.restrictions.format = collections.first(
                x.restrictions.format for x in source.attrs if x.restrictions.format
            )
        else:
            self.set_circular_flag(source, target, attr_type)

    @classmethod
    def copy_attribute_properties(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Replace the given attribute type with the types of the single field
        source class.

        Ignore enumerations and gracefully handle dump types with no attributes.

        :raises: AnalyzerValueError if the source class has more than one attributes
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
        attr.restrictions = restrictions
        attr.help = attr.help or source_attr.help

        if source.nillable:
            restrictions.nillable = True

    def set_circular_flag(self, source: Class, target: Class, attr_type: AttrType):
        """Update circular reference flag."""
        attr_type.circular = self.is_circular_dependency(source, target, set())

    def is_circular_dependency(self, source: Class, target: Class, seen: Set) -> bool:
        """Check if any source dependencies recursively match the target
        class."""

        if source is target or source.status == Status.PROCESSING:
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
    def filter_types(cls, types: List[AttrType]) -> List[AttrType]:
        """
        Remove duplicate and invalid types.

        Invalid:
            1. xs:error
            2. xs:anyType and xs:anySimpleType when there are other types present
        """
        types = collections.unique_sequence(types, key="qname")
        types = collections.remove(types, lambda x: x.datatype == DataType.ERROR)

        if len(types) > 1:
            types = collections.remove(
                types,
                lambda x: x.datatype in (DataType.ANY_TYPE, DataType.ANY_SIMPLE_TYPE),
            )

        if not types:
            types.append(AttrType(qname=str(DataType.STRING), native=True))

        return types
