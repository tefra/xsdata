import operator
import sys
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from dataclasses import replace
from enum import IntEnum
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.exceptions import CodeGenerationError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.models.mixins import ElementBase
from xsdata.utils import namespaces
from xsdata.utils import text

xml_type_map = {
    Tag.ANY: XmlType.WILDCARD,
    Tag.ANY_ATTRIBUTE: XmlType.ATTRIBUTES,
    Tag.ATTRIBUTE: XmlType.ATTRIBUTE,
    Tag.CHOICE: XmlType.ELEMENTS,
    Tag.ELEMENT: XmlType.ELEMENT,
}

SIMPLE_TYPES = (Tag.EXTENSION, Tag.LIST, Tag.SIMPLE_TYPE, Tag.UNION)
GLOBAL_TYPES = (Tag.ELEMENT, Tag.BINDING_OPERATION, Tag.BINDING_MESSAGE, Tag.MESSAGE)


@dataclass
class Restrictions:
    """
    Model representation of a dataclass field validation and type metadata.

    :param min_occurs:
    :param max_occurs:
    :param min_exclusive:
    :param min_inclusive:
    :param min_length:
    :param max_exclusive:
    :param max_inclusive:
    :param max_length:
    :param total_digits:
    :param fraction_digits:
    :param length:
    :param white_space:
    :param pattern:
    :param explicit_timezone:
    :param nillable:
    :param sequence:
    :param tokens:
    :param format:
    :param choice:
    """

    min_occurs: Optional[int] = field(default=None)
    max_occurs: Optional[int] = field(default=None)
    min_exclusive: Optional[str] = field(default=None)
    min_inclusive: Optional[str] = field(default=None)
    min_length: Optional[int] = field(default=None)
    max_exclusive: Optional[str] = field(default=None)
    max_inclusive: Optional[str] = field(default=None)
    max_length: Optional[int] = field(default=None)
    total_digits: Optional[int] = field(default=None)
    fraction_digits: Optional[int] = field(default=None)
    length: Optional[int] = field(default=None)
    white_space: Optional[str] = field(default=None)
    pattern: Optional[str] = field(default=None)
    explicit_timezone: Optional[str] = field(default=None)
    nillable: Optional[bool] = field(default=None)
    sequence: Optional[int] = field(default=None)
    tokens: Optional[bool] = field(default=None)
    format: Optional[str] = field(default=None)
    choice: Optional[int] = field(default=None)
    group: Optional[int] = field(default=None)
    path: List[Tuple[str, int, int, int]] = field(default_factory=list)

    @property
    def is_list(self) -> bool:
        """Return true if max occurs property is larger than one."""
        return self.max_occurs is not None and self.max_occurs > 1

    @property
    def is_optional(self) -> bool:
        """Return true if min occurs property equals zero."""
        return self.min_occurs == 0

    @property
    def is_prohibited(self) -> bool:
        return self.max_occurs == 0

    def merge(self, source: "Restrictions"):
        """Update properties from another instance."""
        self.update(source)

        self.path = source.path + self.path
        self.sequence = self.sequence or source.sequence
        self.choice = self.choice or source.choice
        self.tokens = self.tokens or source.tokens
        self.format = self.format or source.format
        self.group = self.group or source.group

        if self.min_occurs is None and source.min_occurs is not None:
            self.min_occurs = source.min_occurs

        if self.max_occurs is None and source.max_occurs is not None:
            self.max_occurs = source.max_occurs

    def update(self, source: "Restrictions"):
        keys = (
            "min_exclusive",
            "min_inclusive",
            "min_length",
            "max_exclusive",
            "max_inclusive",
            "max_length",
            "total_digits",
            "fraction_digits",
            "length",
            "white_space",
            "pattern",
            "explicit_timezone",
        )

        for key in keys:
            value = getattr(source, key)
            if value is not None:
                setattr(self, key, value)

    def asdict(self, types: Optional[List[Type]] = None) -> Dict:
        """
        Return the initialized only properties as a dictionary.

        Skip None or implied values, and optionally use the parent
        attribute types to convert relevant options.
        """
        result = {}
        sorted_types = converter.sort_types(types) if types else []

        if self.is_list:
            if self.min_occurs is not None and self.min_occurs > 0:
                result["min_occurs"] = self.min_occurs
            if self.max_occurs is not None and self.max_occurs < sys.maxsize:
                result["max_occurs"] = self.max_occurs
        elif self.min_occurs == self.max_occurs == 1 and not self.nillable:
            result["required"] = True

        for key, value in asdict(self).items():
            if value is None or key in (
                "choice",
                "group",
                "min_occurs",
                "max_occurs",
                "path",
            ):
                continue

            if key.endswith("clusive") and types:
                value = converter.deserialize(value, sorted_types)

            result[key] = value

        return result

    def clone(self) -> "Restrictions":
        """Return a deep cloned instance."""
        return replace(self)

    @classmethod
    def from_element(cls, element: ElementBase) -> "Restrictions":
        """Static constructor from an xsd model."""
        return cls(**element.get_restrictions())


class AttrCategory(IntEnum):
    NATIVE = 0
    FORWARD = 1
    EXTERNAL = 2


@dataclass(unsafe_hash=True)
class AttrType:
    """
    Model representation for the typing information for fields and extensions.

    :param qname:
    :param alias:
    :param reference:
    :param native:
    :param forward:
    :param circular:
    :param substituted:
    """

    qname: str
    alias: Optional[str] = field(default=None, compare=False)
    reference: int = field(default=0, compare=False)
    native: bool = field(default=False)
    forward: bool = field(default=False)
    circular: bool = field(default=False)
    substituted: bool = field(default=False, compare=False)

    @property
    def datatype(self) -> Optional[DataType]:
        return DataType.from_qname(self.qname) if self.native else None

    @property
    def name(self) -> str:
        """Shortcut for qname local name."""
        return namespaces.local_name(self.qname)

    def is_dependency(self, allow_circular: bool) -> bool:
        """Return true if attribute is not a forward/circular references and
        it's not a native python time."""

        return not (
            self.forward or self.native or (not allow_circular and self.circular)
        )

    def clone(self) -> "AttrType":
        """Return a deep cloned instance."""
        return replace(self)


@dataclass
class Attr:
    """
    Model representation for a dataclass field.

    :param tag:
    :param name:
    :param local_name:
    :param index:
    :param default:
    :param fixed:
    :param mixed:
    :param types:
    :param choices:
    :param namespace:
    :param help:
    :param restrictions:
    """

    tag: str
    name: str = field(compare=False)
    local_name: str = field(init=False)
    index: int = field(compare=False, default_factory=int)
    default: Optional[str] = field(default=None, compare=False)
    fixed: bool = field(default=False, compare=False)
    mixed: bool = field(default=False, compare=False)
    types: List[AttrType] = field(default_factory=list, compare=False)
    choices: List["Attr"] = field(default_factory=list, compare=False)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None, compare=False)
    restrictions: Restrictions = field(default_factory=Restrictions, compare=False)

    def __post_init__(self):
        self.local_name = self.name

    @property
    def key(self) -> str:
        return f"{self.tag}.{self.namespace}.{self.local_name}"

    @property
    def is_attribute(self) -> bool:
        """Return whether this attribute is derived from an xs:attribute or
        xs:anyAttribute."""
        return self.tag in (Tag.ATTRIBUTE, Tag.ANY_ATTRIBUTE)

    @property
    def is_enumeration(self) -> bool:
        """Return whether this attribute is derived from an xs:enumeration."""
        return self.tag == Tag.ENUMERATION

    @property
    def is_dict(self) -> bool:
        """Return whether this attribute is a mapping of values."""
        return self.tag == Tag.ANY_ATTRIBUTE

    @property
    def is_factory(self) -> bool:
        """Return whether this attribute is a list of items or a mapping."""
        return self.is_list or self.is_dict or self.is_tokens

    @property
    def is_group(self) -> bool:
        """Return whether this attribute is derived from an xs:group or
        xs:attributeGroup."""
        return self.tag in (Tag.ATTRIBUTE_GROUP, Tag.GROUP)

    @property
    def is_list(self) -> bool:
        """Return whether this attribute is a list of values."""
        return self.restrictions.is_list

    @property
    def is_prohibited(self) -> bool:
        """Return whether this attribute is prohibited."""
        return self.restrictions.is_prohibited

    @property
    def is_nameless(self) -> bool:
        """Return whether this attribute has a local name that will be used
        during parsing/serialization."""
        return self.tag not in (Tag.ATTRIBUTE, Tag.ELEMENT)

    @property
    def is_nillable(self) -> bool:
        return self.restrictions.nillable is True

    @property
    def is_optional(self) -> bool:
        """Return whether this attribute is not required."""
        return self.restrictions.is_optional

    @property
    def is_suffix(self) -> bool:
        """Return whether this attribute is not derived from an xs element with
        mode suffix."""
        return self.index == sys.maxsize

    @property
    def is_xsi_type(self) -> bool:
        """Return whether this attribute qualified name is equal to
        xsi:type."""
        return self.namespace == Namespace.XSI.uri and self.name == "type"

    @property
    def is_tokens(self) -> bool:
        """Return whether this attribute is a list of values."""
        return self.restrictions.tokens is True

    @property
    def is_wildcard(self) -> bool:
        """Return whether this attribute is derived from xs:anyAttribute or
        xs:any."""
        return self.tag in (Tag.ANY_ATTRIBUTE, Tag.ANY)

    @property
    def is_any_type(self) -> bool:
        return any(tp is object for tp in self.get_native_types())

    @property
    def native_types(self) -> List[Type]:
        """Return a list of all builtin data types."""
        return list(set(self.get_native_types()))

    @property
    def user_types(self) -> Iterator[AttrType]:
        """Return an iterator of all the user defined types."""
        for tp in self.types:
            if not tp.native:
                yield tp

    @property
    def slug(self) -> str:
        return text.alnum(self.name)

    @property
    def xml_type(self) -> Optional[str]:
        """Return the xml node type this attribute is mapped to."""
        return xml_type_map.get(self.tag)

    def clone(self) -> "Attr":
        """Return a deep cloned instance."""
        return replace(
            self,
            types=[x.clone() for x in self.types],
            restrictions=self.restrictions.clone(),
        )

    def get_native_types(self) -> Iterator[Type]:
        for tp in self.types:
            datatype = tp.datatype
            if datatype:
                yield datatype.type


@dataclass(unsafe_hash=True)
class Extension:
    """
    Model representation of a dataclass base class.

    :param tag:
    :param type:
    :param restrictions:
    """

    tag: str
    type: AttrType
    restrictions: Restrictions = field(hash=False)

    def clone(self) -> "Extension":
        """Return a deep cloned instance."""
        return replace(
            self,
            type=self.type.clone(),
            restrictions=self.restrictions.clone(),
        )


class Status(IntEnum):
    RAW = 0
    UNGROUPING = 10
    UNGROUPED = 11
    FLATTENING = 20
    FLATTENED = 21
    SANITIZING = 30
    SANITIZED = 31
    RESOLVING = 40
    RESOLVED = 41
    FINALIZING = 50
    FINALIZED = 51


@dataclass
class Class:
    """
    Model representation of a dataclass with fields, base/inner classes and
    additional metadata settings.

    :param qname:
    :param tag:
    :param location:
    :param mixed:
    :param abstract:
    :param nillable:
    :param local_type:
    :param status:
    :param container:
    :param package:
    :param module:
    :param namespace:
    :param help:
    :param meta_name:
    :param default:
    :param fixed:
    :param substitutions:
    :param extensions:
    :param attrs:
    :param inner:
    :param ns_map:
    """

    qname: str
    tag: str
    location: str
    mixed: bool = field(default=False)
    abstract: bool = field(default=False)
    nillable: bool = field(default=False)
    local_type: bool = field(default=False)
    status: Status = field(default=Status.RAW)
    container: Optional[str] = field(default=None)
    package: Optional[str] = field(default=None)
    module: Optional[str] = field(default=None)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    meta_name: Optional[str] = field(default=None)
    default: Any = field(default=None, compare=False)
    fixed: bool = field(default=False, compare=False)
    substitutions: List[str] = field(default_factory=list)
    extensions: List[Extension] = field(default_factory=list)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)
    ns_map: Dict = field(default_factory=dict)

    @property
    def name(self) -> str:
        """Shortcut for qname local name."""
        return namespaces.local_name(self.qname)

    @property
    def slug(self) -> str:
        return text.alnum(self.name)

    @property
    def ref(self) -> int:
        return id(self)

    @property
    def target_namespace(self) -> Optional[str]:
        return namespaces.target_uri(self.qname)

    @property
    def has_suffix_attr(self) -> bool:
        """Return whether it includes a suffix attribute."""
        return any(attr.is_suffix for attr in self.attrs)

    @property
    def has_help_attr(self) -> bool:
        """Return whether it includes at least one attr with help content."""
        return any(attr.help and attr.help.strip() for attr in self.attrs)

    @property
    def is_complex(self) -> bool:
        """Return whether this instance is derived from an xs:element or
        xs:complexType."""
        return self.tag in (Tag.ELEMENT, Tag.COMPLEX_TYPE)

    @property
    def is_element(self) -> bool:
        """Return whether this instance is derived from an non abstract
        xs:element."""
        return self.tag == Tag.ELEMENT

    @property
    def is_enumeration(self) -> bool:
        """Return whether all attributes are derived from xs:enumeration."""
        return len(self.attrs) > 0 and all(attr.is_enumeration for attr in self.attrs)

    @property
    def is_global_type(self) -> bool:
        """Return whether this instance is a non-abstract element, wsdl binding
        class or a complex type without simple content."""
        return (not self.abstract and self.tag in GLOBAL_TYPES) or (
            self.tag == Tag.COMPLEX_TYPE and not self.is_simple_type
        )

    @property
    def is_group(self) -> bool:
        """Return whether this attribute is derived from an xs:group or
        xs:attributeGroup."""
        return self.tag in (Tag.ATTRIBUTE_GROUP, Tag.GROUP)

    @property
    def is_nillable(self) -> bool:
        """Return whether this class represents a nillable xml element."""
        return self.nillable or any(x.restrictions.nillable for x in self.extensions)

    @property
    def is_mixed(self) -> bool:
        """Return whether this class supports mixed content."""
        return self.mixed or any(x.mixed for x in self.attrs)

    @property
    def is_service(self) -> bool:
        """Return whether this instance is derived from wsdl:operation."""
        return self.tag == Tag.BINDING_OPERATION

    @property
    def is_simple_type(self) -> bool:
        """Return whether the class represents a simple text type."""
        return (
            len(self.attrs) == 1
            and self.attrs[0].tag in SIMPLE_TYPES
            and not self.extensions
        )

    @property
    def references(self) -> Iterator[int]:
        def all_refs():
            for ext in self.extensions:
                yield ext.type.reference

            for attr in self.attrs:
                for tp in attr.types:
                    yield tp.reference

                for choice in attr.choices:
                    for ctp in choice.types:
                        yield ctp.reference

            for inner in self.inner:
                yield from inner.references

        for ref in all_refs():
            if ref:
                yield ref

    @property
    def target_module(self) -> str:
        """Return the target module this class is assigned to."""
        if self.package and self.module:
            return f"{self.package}.{self.module}"

        if self.module:
            return self.module

        raise CodeGenerationError(
            f"Class `{self.name}` has not been assigned to a module yet!"
        )

    def clone(self) -> "Class":
        """Return a deep cloned instance."""
        inners = [inner.clone() for inner in self.inner]
        extensions = [extension.clone() for extension in self.extensions]
        attrs = [attr.clone() for attr in self.attrs]
        return replace(self, inner=inners, extensions=extensions, attrs=attrs)

    def dependencies(self, allow_circular: bool = False) -> Iterator[str]:
        """
        Return a set of dependencies for the given class.

        Collect:
            * base classes
            * attribute types
            * attribute choice types
            * recursively go through the inner classes
            * Ignore inner class references
            * Ignore native types.
        """
        types = {ext.type for ext in self.extensions}

        for attr in self.attrs:
            types.update(attr.types)
            types.update(tp for choice in attr.choices for tp in choice.types)

        for tp in types:
            if tp.is_dependency(allow_circular):
                yield tp.qname

        for inner in self.inner:
            yield from inner.dependencies(allow_circular)


@dataclass
class Import:
    """
    Model representation of a python import statement.

    :param qname:
    :param source:
    :param alias:
    """

    qname: str
    source: str
    alias: Optional[str] = field(default=None)

    @property
    def name(self) -> str:
        """Shortcut for qname local name."""
        return namespaces.local_name(self.qname)

    @property
    def slug(self) -> str:
        return text.alnum(self.name)


# Getters used all over the codegen process
get_location = operator.attrgetter("location")
get_name = operator.attrgetter("name")
get_qname = operator.attrgetter("qname")
get_tag = operator.attrgetter("tag")
get_restriction_choice = operator.attrgetter("restrictions.choice")
get_restriction_sequence = operator.attrgetter("restrictions.sequence")
get_slug = operator.attrgetter("slug")
get_target_namespace = operator.attrgetter("target_namespace")
is_enumeration = operator.attrgetter("is_enumeration")
is_group = operator.attrgetter("is_group")
