import operator
import sys
from dataclasses import asdict, dataclass, field, replace
from enum import IntEnum
from typing import Any, Dict, Iterator, List, Optional, Tuple, Type

from xsdata.codegen.exceptions import CodegenError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType, Namespace, Tag
from xsdata.models.mixins import ElementBase
from xsdata.utils import namespaces, text

xml_type_map = {
    Tag.ANY: XmlType.WILDCARD,
    Tag.ANY_ATTRIBUTE: XmlType.ATTRIBUTES,
    Tag.ATTRIBUTE: XmlType.ATTRIBUTE,
    Tag.CHOICE: XmlType.ELEMENTS,
    Tag.ELEMENT: XmlType.ELEMENT,
}

GLOBAL_TYPES = (
    Tag.ELEMENT,
    Tag.COMPLEX_TYPE,
    Tag.BINDING_OPERATION,
    Tag.BINDING_MESSAGE,
    Tag.MESSAGE,
)


@dataclass
class CodegenModel:
    """Base codegen model."""


@dataclass
class Restrictions(CodegenModel):
    """Class field validation restrictions.

    Args:
        min_occurs: The minimum number of occurrences
        max_occurs: The maximum number of occurrences
        min_exclusive: The lower exclusive bound for numeric values
        min_inclusive: The lower inclusive bound for numeric values
        min_length: The minimum length of characters or list items allowed
        max_exclusive: The upper exclusive bound for numeric values
        max_inclusive: The upper inclusive bound for numeric values
        max_length: The max length of characters or list items allowed
        total_digits:  The exact number of digits allowed for numeric values
        fraction_digits: The maximum number of decimal places allowed
        length: The exact number of characters or list items allowed
        white_space: Specifies how white space is handled
        pattern: Defines the exact sequence of characters that are acceptable
        explicit_timezone: Require or prohibit the time zone offset in date/time
        nillable: Specifies whether nil content is allowed
        sequence: The sequence reference number of the attr
        tokens: Specifies whether the value needs tokenization
        format: The output format used for byte and datetime types
        choice: The choice reference number of the attr
        group: The group reference number of the attr
        process_contents: Specifies the content processed mode: strict, lax, skip
        path: The coded attr path in the source document
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
    sequence: Optional[int] = field(default=None, compare=False)
    tokens: Optional[bool] = field(default=None)
    format: Optional[str] = field(default=None)
    choice: Optional[int] = field(default=None, compare=False)
    group: Optional[int] = field(default=None)
    process_contents: Optional[str] = field(default=None)
    path: List[Tuple[str, int, int, int]] = field(default_factory=list)

    @property
    def is_list(self) -> bool:
        """Return whether the max occurs larger than one."""
        return self.max_occurs is not None and self.max_occurs > 1

    @property
    def is_optional(self) -> bool:
        """Return whether the min occurs is zero."""
        return self.min_occurs == 0

    @property
    def is_prohibited(self) -> bool:
        """Return whether the max occurs is zero."""
        return self.max_occurs == 0

    def merge(self, source: "Restrictions"):
        """Update properties from another instance.

        Args:
            source: The source instance to merge properties from
        """
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
            "process_contents",
        )

        for key in keys:
            value = getattr(source, key)
            if value is not None:
                setattr(self, key, value)

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

    def asdict(self, types: Optional[List[Type]] = None) -> Dict:
        """Return the initialized only properties as a dictionary.

        Skip None or implied values, and optionally use the
        attribute types to convert relevant options.

        Args:
            types: An optional list of attr python types

        Returns:
            A key-value of map of the attr restrictions for generation.
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

            if key == "process_contents" and value != "skip":
                continue

            if key.endswith("clusive") and types:
                value = converter.deserialize(value, sorted_types)

            result[key] = value

        return result

    def clone(self, **kwargs: Any) -> "Restrictions":
        """Return a deep cloned instance and replace any args."""
        return replace(self, **kwargs)

    @classmethod
    def from_element(cls, element: ElementBase) -> "Restrictions":
        """Static constructor from a xsd model.

        Args:
            element: A element base instance.

        Returns:
            The new restrictions instance
        """
        return cls(**element.get_restrictions())


@dataclass(unsafe_hash=True)
class AttrType(CodegenModel):
    """Class field typing information.

    Args:
        qname: The namespace qualified name
        alias: The type alias
        reference: The type reference number
        native: Specifies if it's python native type
        forward: Specifies if it's a forward reference
        circular: Specifies if it's a circular reference
        substituted: Specifies if it has been processed for substitution groups
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
        """Return the datatype instance if native, none otherwise."""
        return DataType.from_qname(self.qname) if self.native else None

    @property
    def name(self) -> str:
        """Shortcut for qname local name."""
        return namespaces.local_name(self.qname)

    def is_dependency(self, allow_circular: bool) -> bool:
        """Return whether this type is a dependency.

        The type must a reference to a user type, not a forward
        reference and not a circular unless if it's allowed.

        Args:
            allow_circular: Allow circular references as dependencies

        Returns:
            The bool result/
        """
        return not (
            self.forward or self.native or (not allow_circular and self.circular)
        )

    def clone(self, **kwargs: Any) -> "AttrType":
        """Return a deep cloned instance."""
        return replace(self, **kwargs)


@dataclass
class Attr(CodegenModel):
    """Class field model representation.

    Args:
        tag: The xml tag that produced this attr
        name: The final attr name
        local_name: The original attr name
        index: The index position of this attr in the class
        default: The default value
        fixed: Specifies if the default value is fixed
        mixed: Specifies if the attr supports mixed content
        types: The attr types list
        choices: The attr choice list
        namespace: The attr namespace
        help: The attr help text
        restrictions: The attr restrictions instance
        parent: The parent class qualified name of the attr
        substitution: The substitution group this attr belongs to
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
    parent: Optional[str] = field(default=None, compare=False)
    substitution: Optional[str] = field(default=None, compare=False)

    def __post_init__(self):
        """Set the original attr name on init."""
        self.local_name = self.name

    @property
    def key(self) -> str:
        """Generate a key for this attr.

        Concatenate the tag/namespace/local_name.
        This key is used to find duplicates, it's not
        supposed to be unique.

        Returns:
            The unique key for this attr.

        """
        return f"{self.tag}.{self.namespace}.{self.local_name}"

    @property
    def qname(self) -> str:
        """Return the fully qualified name of the attr."""
        return namespaces.build_qname(self.namespace, self.local_name)

    @property
    def is_attribute(self) -> bool:
        """Return whether this attr represents a xml attribute node."""
        return self.tag in (Tag.ATTRIBUTE, Tag.ANY_ATTRIBUTE)

    @property
    def is_enumeration(self) -> bool:
        """Return whether this attr an enumeration member."""
        return self.tag == Tag.ENUMERATION

    @property
    def is_dict(self) -> bool:
        """Return whether this attr is derived from xs:anyAttribute."""
        return self.tag == Tag.ANY_ATTRIBUTE

    @property
    def is_factory(self) -> bool:
        """Return whether this attribute is a list of items or a mapping."""
        return self.is_list or self.is_dict or self.is_tokens

    @property
    def is_forward_ref(self) -> bool:
        """Return whether any attr types is a forward or circular reference."""
        return any(tp.circular or tp.forward for tp in self.types)

    @property
    def is_circular_ref(self) -> bool:
        """Return whether any attr types is a circular reference."""
        return any(tp.circular for tp in self.types)

    @property
    def is_group(self) -> bool:
        """Return whether this attr is a reference to a group class."""
        return self.tag in (Tag.ATTRIBUTE_GROUP, Tag.GROUP)

    @property
    def is_list(self) -> bool:
        """Return whether this attr requires a list of values."""
        return self.restrictions.is_list

    @property
    def is_prohibited(self) -> bool:
        """Return whether this attr is prohibited."""
        return self.restrictions.is_prohibited

    @property
    def is_nameless(self) -> bool:
        """Return whether this attr is a real xml node."""
        return self.tag not in (Tag.ATTRIBUTE, Tag.ELEMENT)

    @property
    def is_nillable(self) -> bool:
        """Return whether this attr supports nil values."""
        return self.restrictions.nillable is True

    @property
    def is_optional(self) -> bool:
        """Return whether this attr is not required."""
        return self.restrictions.is_optional

    @property
    def is_suffix(self) -> bool:
        """Return whether this attr is supposed to be generated last."""
        return self.index == sys.maxsize

    @property
    def is_xsi_type(self) -> bool:
        """Return whether this attr represents a xsi:type attribute."""
        return self.namespace == Namespace.XSI.uri and self.name == "type"

    @property
    def is_tokens(self) -> bool:
        """Return whether this attr supports token values."""
        return self.restrictions.tokens is True

    @property
    def is_wildcard(self) -> bool:
        """Return whether this attr supports any content."""
        return self.tag in (Tag.ANY_ATTRIBUTE, Tag.ANY)

    @property
    def is_any_type(self) -> bool:
        """Return whether this attr types support any content."""
        return any(tp is object for tp in self.get_native_types())

    @property
    def native_types(self) -> List[Type]:
        """Return a list of all the builtin data types."""
        return list(set(self.get_native_types()))

    @property
    def user_types(self) -> Iterator[AttrType]:
        """Yield an iterator of all the user defined types."""
        for tp in self.types:
            if not tp.native:
                yield tp

    @property
    def slug(self) -> str:
        """Return the slugified name of the attr."""
        return text.alnum(self.name)

    @property
    def xml_type(self) -> Optional[str]:
        """Return the xml type this attribute is mapped to."""
        return xml_type_map.get(self.tag)

    def clone(self) -> "Attr":
        """Return a deep cloned instance."""
        return replace(
            self,
            types=[x.clone() for x in self.types],
            restrictions=self.restrictions.clone(),
        )

    def get_native_types(self) -> Iterator[Type]:
        """Yield an iterator of all the native attr types."""
        for tp in self.types:
            datatype = tp.datatype
            if datatype:
                yield datatype.type

    def can_be_restricted(self) -> bool:
        """Return whether this attr can be restricted."""
        return self.xml_type not in (Tag.ATTRIBUTE, None)


@dataclass(unsafe_hash=True)
class Extension(CodegenModel):
    """Base class model representation.

    Args:
        tag: The xml tag that produced this extension
        type: The extension type
        restrictions: The extension restrictions instance
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
    """Class process status enumeration."""

    RAW = 0
    UNGROUPING = 10
    UNGROUPED = 11
    FLATTENING = 20
    FLATTENED = 21
    SANITIZING = 30
    SANITIZED = 31
    RESOLVING = 40
    RESOLVED = 41
    CLEANING = 50
    CLEANED = 51
    FINALIZING = 60
    FINALIZED = 61


@dataclass
class Class(CodegenModel):
    """Class model representation.

    Args:
        qname: The namespace qualified name
        tag: The xml tag that produced this class
        location: The schema/document location uri
        mixed: Specifies whether this class supports mixed content
        abstract: Specifies whether this is an abstract class
        nillable: Specifies whether this class supports nil content
        local_type: Specifies if this class was an inner type at some point
        status: The processing status of the class
        container: The xml container of the class, schema, override, redefine
        package: The designated package of the class
        module: The designated module of the class
        namespace: The class namespace
        help: The help text
        meta_name: The xml element name of the class
        default: The default value
        fixed: Specifies whether the default value is fixed
        substitutions: The list of all the substitution groups this class belongs to
        extensions: The list of all the extension instances
        attrs: The list of all the attr instances
        inner: The list of all the inner class instances
        ns_map: The namespace prefix-URI map
    """

    qname: str
    tag: str
    location: str = field(compare=False)
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
        """Shortcut for the class local name."""
        return namespaces.local_name(self.qname)

    @property
    def slug(self) -> str:
        """Return a slugified version of the class name."""
        return text.alnum(self.name)

    @property
    def ref(self) -> int:
        """Return this id reference of this instance."""
        return id(self)

    @property
    def target_namespace(self) -> Optional[str]:
        """Return the class target namespace."""
        return namespaces.target_uri(self.qname)

    @property
    def has_suffix_attr(self) -> bool:
        """Return whether it includes a suffix attr."""
        return any(attr.is_suffix for attr in self.attrs)

    @property
    def has_help_attr(self) -> bool:
        """Return whether at least one of attrs has help content."""
        return any(attr.help and attr.help.strip() for attr in self.attrs)

    @property
    def is_element(self) -> bool:
        """Return whether this class represents a xml element."""
        return self.tag == Tag.ELEMENT

    @property
    def is_enumeration(self) -> bool:
        """Return whether all attrs are enumeration members."""
        return len(self.attrs) > 0 and all(attr.is_enumeration for attr in self.attrs)

    @property
    def is_complex_type(self) -> bool:
        """Return whether this class represents a root/global class.

        Global classes are the only classes that get generated by default.
        """
        return self.tag in GLOBAL_TYPES

    @property
    def is_group(self) -> bool:
        """Return whether this class is derived from a xs:group/attributeGroup."""
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
    def is_restricted(self) -> bool:
        """Return whether this class includes any restriction extensions."""
        return any(
            True for extension in self.extensions if extension.tag == Tag.RESTRICTION
        )

    @property
    def is_service(self) -> bool:
        """Return whether this instance is derived from a wsdl:operation."""
        return self.tag == Tag.BINDING_OPERATION

    @property
    def references(self) -> Iterator[int]:
        """Yield all class object reference numbers."""
        for tp in self.types():
            if tp.reference:
                yield tp.reference

    @property
    def target_module(self) -> str:
        """Return the designated full module path.

        Raises:
            CodeGenerationError: if the target was not designated
                a package and module.
        """
        if self.package and self.module:
            return f"{self.package}.{self.module}"

        if self.module:
            return self.module

        raise CodegenError(
            "Type has not been assigned to a module yet!", type=self.qname
        )

    def clone(self) -> "Class":
        """Return a deep cloned instance."""
        inners = [inner.clone() for inner in self.inner]
        extensions = [extension.clone() for extension in self.extensions]
        attrs = [attr.clone() for attr in self.attrs]
        return replace(self, inner=inners, extensions=extensions, attrs=attrs)

    def dependencies(self, allow_circular: bool = False) -> Iterator[str]:
        """Yields all class dependencies.

        Omit circular and forward references by default.

        Collect:
            * base classes
            * attribute types
            * attribute choice types
            * recursively go through the inner classes
            * Ignore inner class references
            * Ignore native types.

        Args:
            allow_circular: Allow circular references
        """
        for tp in set(self.types()):
            if tp.is_dependency(allow_circular=allow_circular):
                yield tp.qname

    def types(self) -> Iterator[AttrType]:
        """Yields all class types."""
        for ext in self.extensions:
            yield ext.type

        for attr in self.attrs:
            yield from attr.types

            for choice in attr.choices:
                yield from choice.types

        for inner in self.inner:
            yield from inner.types()

    def children(self) -> Iterator[CodegenModel]:
        """Yield all codegen children."""
        for attr in self.attrs:
            yield attr
            yield attr.restrictions

            for tp in attr.types:
                yield tp

            for choice in attr.choices:
                yield choice
                yield choice.restrictions

                for tp in choice.types:
                    yield tp

        for ext in self.extensions:
            yield ext
            yield ext.type
            yield ext.restrictions

        for inner in self.inner:
            yield from inner.children()

    def has_forward_ref(self) -> bool:
        """Return whether this class has any forward references."""
        for attr in self.attrs:
            if attr.is_forward_ref:
                return True

            if any(choice for choice in attr.choices if choice.is_forward_ref):
                return True

        return any(inner.has_forward_ref() for inner in self.inner)


@dataclass
class Import:
    """Python import statement model representation.

    Args:
        qname: The qualified name of the imported class
        source: The absolute module path
        alias: Specifies an alias to avoid naming conflicts
    """

    qname: str
    source: str
    alias: Optional[str] = field(default=None)

    @property
    def name(self) -> str:
        """Return the name of the imported class."""
        return namespaces.local_name(self.qname)

    @property
    def slug(self) -> str:
        """Return a slugified version of the imported class name."""
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
