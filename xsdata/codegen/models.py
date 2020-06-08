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
from typing import Type

from lxml.etree import QName

from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.utils import text


def qname(name: str, ns_map: Dict, default_namespace: Optional[str] = None) -> QName:
    """
    Create an :class:`lxml.etree.QName` for the given name and namespaces map.

    Use the default namespace if the prefix is not in the ns_map.
    """
    prefix, suffix = text.split(name)
    namespace = default_namespace

    if prefix:
        name = suffix
        namespace = ns_map.get(prefix, prefix)

    return QName(namespace, name)


xml_type_map = {
    Tag.ELEMENT: XmlType.ELEMENT,
    Tag.ANY: XmlType.WILDCARD,
    Tag.ANY_ATTRIBUTE: XmlType.ATTRIBUTES,
    Tag.ATTRIBUTE: XmlType.ATTRIBUTE,
    None: XmlType.TEXT,
}


@dataclass
class Restrictions:
    """
    Model representation of a dataclass field validation and type metadata.

    :param required:
    :param prohibited:
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
    :param sequential:
    """

    required: Optional[bool] = field(default=None)
    prohibited: Optional[bool] = field(default=None)
    min_occurs: Optional[int] = field(default=None)
    max_occurs: Optional[int] = field(default=None)
    min_exclusive: Optional[float] = field(default=None)
    min_inclusive: Optional[float] = field(default=None)
    min_length: Optional[float] = field(default=None)
    max_exclusive: Optional[float] = field(default=None)
    max_inclusive: Optional[float] = field(default=None)
    max_length: Optional[float] = field(default=None)
    total_digits: Optional[int] = field(default=None)
    fraction_digits: Optional[int] = field(default=None)
    length: Optional[int] = field(default=None)
    white_space: Optional[str] = field(default=None)
    pattern: Optional[str] = field(default=None)
    explicit_timezone: Optional[str] = field(default=None)
    nillable: Optional[bool] = field(default=None)
    sequential: Optional[bool] = field(default=None)

    @property
    def is_list(self) -> bool:
        """Return true if max occurs property is larger than one."""
        return self.max_occurs is not None and self.max_occurs > 1

    @property
    def is_optional(self) -> bool:
        """Return true if min occurs property equals zero."""
        return self.min_occurs == 0

    def merge(self, source: "Restrictions"):
        """Merge the source properties to the current instance."""
        self.update(source.asdict())

    def update(self, data: Dict):
        """Update the instance properties from the given data dictionary."""
        min_occurs = data.pop("min_occurs", None)
        max_occurs = data.pop("max_occurs", None)
        sequential = data.pop("sequential", False)

        for key, value in data.items():
            setattr(self, key, value)

        is_list = max_occurs is not None and max_occurs > 1
        if sequential and (is_list or not self.is_list):
            self.sequential = sequential

        if self.min_occurs is None or (min_occurs is not None and min_occurs != 1):
            self.min_occurs = min_occurs

        if self.max_occurs is None or (max_occurs is not None and max_occurs != 1):
            self.max_occurs = max_occurs

    def asdict(self) -> Dict:
        """Return the initialized only properties as a dictionary."""
        return {k: v for k, v in asdict(self).items() if v is not None}

    def clone(self) -> "Restrictions":
        """Return a deep cloned instance."""
        return replace(self)

    @classmethod
    def from_element(cls, element: ElementBase) -> "Restrictions":
        """Static constructor from an xsd model."""
        return cls(**element.get_restrictions())


@dataclass(unsafe_hash=True)
class AttrType:
    """
    Model representation for the typing information for fields and extensions.

    :param name:
    :param index:
    :param alias:
    :param native:
    :param forward:
    :param circular:
    """

    name: str
    index: int = field(default_factory=int)
    alias: Optional[str] = field(default=None)
    native: bool = field(default=False)
    forward: bool = field(default=False)
    circular: bool = field(default=False)

    @property
    def is_dependency(self) -> bool:
        """Return true if attribute is not a forward/circular references and
        it's not a native python time."""
        return not (self.forward or self.native or self.circular)

    @property
    def native_name(self) -> Optional[str]:
        """Return the python build-in type name: `'str'`, `'int'` if it's
        native type."""
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.local_name if data_type else None

    @property
    def native_code(self) -> Optional[str]:
        """Return the xml data type if it's native type."""
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.code if data_type else None

    @property
    def native_type(self) -> Any:
        """Return the python build-in type if it's a native type."""
        data_type = DataType.get_enum(self.name) if self.native else None
        return data_type.local if data_type else None

    def clone(self) -> "AttrType":
        """Return a deep cloned instance."""
        return replace(self)


@dataclass
class Attr:
    """
    Model representation for a dataclass field.

    :param tag:
    :param name:
    :param index:
    :param local_name:
    :param default:
    :param fixed:
    :param types:
    :param display_type:
    :param namespace:
    :param help:
    :param restrictions:
    """

    tag: str
    name: str
    index: int = field(compare=False)
    local_name: Optional[str] = field(default=None)
    default: Any = field(default=None, compare=False)
    fixed: bool = field(default=False, compare=False)
    types: List[AttrType] = field(default_factory=list)
    display_type: Optional[str] = field(default=None)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    restrictions: Restrictions = field(default_factory=Restrictions, compare=False)

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
    def is_factory(self) -> bool:
        """Return whether this attribute is a list of items or a mapping."""
        return self.is_list or self.is_map

    @property
    def is_group(self) -> bool:
        """Return whether this attribute is derived from an xs:group or
        xs:attributeGroup."""
        return self.tag in (Tag.ATTRIBUTE_GROUP, Tag.GROUP)

    @property
    def is_map(self) -> bool:
        """Return whether this attribute is a mapping of values."""
        return (
            len(self.types) == 1
            and self.types[0].native
            and isinstance(self.types[0].native_type, tuple)
        )

    @property
    def is_nameless(self) -> bool:
        """Return whether this attribute has a local name that will be used
        during parsing/serialization."""
        return self.xml_type in (XmlType.WILDCARD, XmlType.ATTRIBUTES, None)

    @property
    def is_list(self) -> bool:
        """Return whether this attribute is a list of values."""
        return self.restrictions.is_list

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
        return (
            QNames.XSI_TYPE.namespace == self.namespace
            and QNames.XSI_TYPE.localname == text.suffix(self.name)
        )

    @property
    def is_wildcard(self) -> bool:
        """Return whether this attribute is derived from xs:anyAttribute or
        xs:any."""
        return self.tag in (Tag.ANY_ATTRIBUTE, Tag.ANY)

    @property
    def xml_type(self) -> Optional[str]:
        """Return the xml node type this attribute is mapped to."""
        return xml_type_map.get(self.tag)

    def clone(self) -> "Attr":
        """Return a deep cloned instance."""
        return replace(
            self,
            types=[type.clone() for type in self.types],
            restrictions=self.restrictions.clone(),
        )


@dataclass
class Extension:
    """
    Model representation of a dataclass base class.

    :param type:
    :restrictions type:
    """

    type: AttrType
    restrictions: Restrictions

    def clone(self) -> "Extension":
        """Return a deep cloned instance."""
        return replace(
            self, type=self.type.clone(), restrictions=self.restrictions.clone()
        )


class Status(IntEnum):
    RAW = 0
    PROCESSING = 1
    PROCESSED = 2


@dataclass
class Class:
    """
    Model representation of a dataclass with fields, base/inner classes and
    additional metadata settings.

    :param name:
    :param type:
    :param module:
    :param mixed:
    :param abstract:
    :param nillable:
    :param status:
    :param container:
    :param package:
    :param namespace:
    :param help:
    :param substitutions:
    :param extensions:
    :param attrs:
    :param inner:
    :param ns_map:
    :param source_namespace:
    """

    name: str
    type: Type
    module: str
    mixed: bool
    abstract: bool
    nillable: bool
    status: Status = field(default=Status.RAW)
    container: Optional[str] = field(default=None)
    package: Optional[str] = field(default=None)
    namespace: Optional[str] = field(default=None)
    help: Optional[str] = field(default=None)
    substitutions: List[str] = field(default_factory=list)
    extensions: List[Extension] = field(default_factory=list)
    attrs: List[Attr] = field(default_factory=list)
    inner: List["Class"] = field(default_factory=list)
    ns_map: Dict = field(default_factory=dict)
    source_namespace: Optional[str] = field(default=None)

    @property
    def has_suffix_attr(self) -> bool:
        """Return whether or not it includes a suffix attribute."""
        return any(attr.is_suffix for attr in self.attrs)

    @property
    def has_wild_attr(self) -> bool:
        """Return whether or not it includes a wildcard attribute."""
        return any(attr.is_wildcard for attr in self.attrs)

    @property
    def is_complex(self) -> bool:
        """Return whether or not this instance is derived from an xs:element or
        xs:complexType."""
        return self.type in (Element, ComplexType)

    @property
    def is_element(self) -> bool:
        """Return whether or not this instance is derived from an non abstract
        xs:element."""
        return self.type is Element and not self.abstract

    @property
    def is_enumeration(self) -> bool:
        """Return whether all attributes are derived from xs:enumeration."""
        return len(self.attrs) > 0 and all(attr.is_enumeration for attr in self.attrs)

    @property
    def is_nillable(self) -> bool:
        """Return whether this class represents a nillable xml element."""
        return self.nillable or next(
            (True for ext in self.extensions if ext.restrictions.nillable), False
        )

    @property
    def source_prefix(self) -> Optional[str]:
        """Return the source namespace prefix as it was defined in the schema
        definition."""
        if not self.source_namespace:
            return None

        for prefix, namespace in self.ns_map.items():
            if namespace == self.source_namespace and prefix:
                return prefix

        return (
            None
            if self.source_namespace.startswith("http://")
            else self.source_namespace
        )

    @property
    def target_module(self) -> str:
        """Return the target module this class is assigned to."""
        return f"{self.package}.{self.module}"

    def clone(self) -> "Class":
        """Return a deep cloned instance."""
        inners = [inner.clone() for inner in self.inner]
        extensions = [extension.clone() for extension in self.extensions]
        attrs = [attr.clone() for attr in self.attrs]
        return replace(self, inner=inners, extensions=extensions, attrs=attrs)

    def dependencies(self) -> Iterator[QName]:
        """
        Return a set of dependencies for the given class.

        Collect:
            * base classes
            * attribute types
            * recursively go through the inner classes
            * Ignore inner class references
            * Ignore native types.
        """

        seen = set()
        for attr in self.attrs:
            for attr_type in attr.types:
                if attr_type.is_dependency and attr_type.name not in seen:
                    yield self.source_qname(attr_type.name)
                    seen.add(attr_type.name)

        for ext in self.extensions:
            if ext.type.is_dependency and ext.type.name not in seen:
                yield self.source_qname(ext.type.name)
                seen.add(ext.type.name)

        for inner in self.inner:
            yield from inner.dependencies()

    def source_qname(self, name: Optional[str] = None) -> QName:
        return qname(name or self.name, self.ns_map, self.source_namespace)


@dataclass
class Package:
    """
    Model representation of a python import statement.

    :param name:
    :param source:
    :param alias:
    """

    name: str
    source: str
    alias: Optional[str] = field(default=None)
