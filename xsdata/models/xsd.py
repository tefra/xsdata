import sys
import textwrap
from dataclasses import dataclass, field
from typing import Any as Anything
from typing import Dict, Iterator, Optional
from typing import List as Array
from typing import Union as UnionType

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.enums import (
    DataType,
    FormType,
    Mode,
    Namespace,
    ProcessType,
    UseType,
)
from xsdata.models.mixins import (
    ElementBase,
    array_any_element,
    array_element,
    attribute,
    element,
)
from xsdata.utils import text
from xsdata.utils.collections import unique_sequence
from xsdata.utils.constants import DEFAULT_ATTR_NAME
from xsdata.utils.namespaces import clean_uri

docstring_serializer = XmlSerializer(
    config=SerializerConfig(indent="  ", xml_declaration=False)
)


@dataclass(frozen=True)
class Docstring:
    """Docstring model representation.

    Args:
        content: A list of mixed content elements
    """

    class Meta:
        """Metadata options."""

        namespace = "http://www.w3.org/1999/xhtml"

    content: Array[object] = array_any_element()


@dataclass
class Documentation(ElementBase):
    """XSD MinLength model representation."""

    lang: Optional[str] = attribute()
    source: Optional[str] = attribute()
    attributes: Optional["AnyAttribute"] = element()
    content: Array[object] = array_any_element(mixed=True)

    def tostring(self) -> Optional[str]:
        """Convert the content to a help string."""
        obj = Docstring(self.content)
        ns_map = {None: "http://www.w3.org/1999/xhtml"}
        xml = docstring_serializer.render(obj, ns_map=ns_map)
        start = xml.find(">") + 1
        end = xml.rfind("<")
        return textwrap.dedent(xml[start:end]).strip()


@dataclass
class Appinfo(ElementBase):
    """XSD Appinfo model representation."""

    class Meta:
        """Metadata options."""

        mixed = True

    source: Optional[str] = attribute()
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")
    content: Array[object] = array_any_element(mixed=True)


@dataclass
class Annotation(ElementBase):
    """XSD Annotation model representation."""

    app_infos: Array[Appinfo] = array_element(name="appinfo")
    documentations: Array[Documentation] = array_element(name="documentation")
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")


@dataclass
class AnnotationBase(ElementBase):
    """XSD AnnotationBase model representation."""

    id: Optional[str] = attribute()
    annotations: Array[Annotation] = array_element(name="annotation")
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")

    @property
    def display_help(self) -> Optional[str]:
        """Return all annotation documentations concatenated."""
        help_str = "\n".join(
            documentation.tostring() or ""
            for annotation in self.annotations
            for documentation in annotation.documentations
        ).strip()

        return help_str or None


@dataclass
class AnyAttribute(AnnotationBase):
    """XSD AnyAttribute model representation."""

    namespace: str = attribute(default="##any")
    process_contents: Optional[ProcessType] = attribute(
        name="processContents", default="strict"
    )

    def __post_init__(self):
        """Clean the namespace value."""
        self.namespace = " ".join(unique_sequence(self.namespace.split()))

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def raw_namespace(self) -> Optional[str]:
        """The element explicit namespace."""
        return self.namespace

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        clean_ns = "_".join(map(clean_uri, self.namespace.split()))
        return f"@{clean_ns}_attributes"

    @property
    def attr_types(self) -> Iterator[str]:
        """Yields the attr types for this element."""
        yield DataType.ANY_TYPE.prefixed(self.xs_prefix)


@dataclass
class Assertion(AnnotationBase):
    """XSD Assertion model representation."""

    test: Optional[str] = attribute()


@dataclass
class SimpleType(AnnotationBase):
    """XSD SimpleType model representation."""

    name: Optional[str] = attribute()
    restriction: Optional["Restriction"] = element()
    list: Optional["List"] = element()
    union: Optional["Union"] = element()

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def is_enumeration(self) -> bool:
        """Return whether it is an enumeration restriction."""
        return self.restriction is not None and len(self.restriction.enumerations) > 0

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        if self.name:
            return self.name
        return DEFAULT_ATTR_NAME

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if not self.is_enumeration and self.restriction:
            yield from self.restriction.attr_types
        elif self.list:
            yield from self.list.attr_types
        elif self.union:
            yield from self.union.bases

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        if self.restriction:
            return self.restriction.get_restrictions()
        if self.list:
            return self.list.get_restrictions()
        return {}


@dataclass
class List(AnnotationBase):
    """XSD List model representation."""

    simple_type: Optional[SimpleType] = element(name="simpleType")
    item_type: str = attribute(name="itemType", default="")

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        return DEFAULT_ATTR_NAME

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.item_type:
            yield self.item_type

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        return {"tokens": True}


@dataclass
class Union(AnnotationBase):
    """XSD Union model representation."""

    member_types: Optional[str] = attribute(name="memberTypes")
    simple_types: Array[SimpleType] = array_element(name="simpleType")

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.member_types:
            yield from self.member_types.split()

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        return DEFAULT_ATTR_NAME

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        for simple_type in self.simple_types:
            yield from simple_type.attr_types

        if self.member_types:
            yield from self.member_types.split()

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        restrictions = {}
        for simple_type in self.simple_types:
            restrictions.update(simple_type.get_restrictions())
        return restrictions


@dataclass
class Attribute(AnnotationBase):
    """XSD Attribute model representation."""

    default: Optional[str] = attribute()
    fixed: Optional[str] = attribute()
    form: Optional[FormType] = attribute()
    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    type: Optional[str] = attribute()
    target_namespace: Optional[str] = attribute(name="targetNamespace")
    simple_type: Optional[SimpleType] = element(name="simpleType")
    use: Optional[UseType] = attribute(default=UseType.OPTIONAL)

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.type:
            yield self.type
        elif not self.has_children:
            yield DataType.STRING.prefixed(self.xs_prefix)

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.simple_type:
            yield from self.simple_type.attr_types
        elif self.type:
            yield self.type
        elif self.ref:
            yield self.ref

    @property
    def default_type(self) -> str:
        """Returned the inferred default type qname."""
        datatype = DataType.STRING if self.fixed else DataType.ANY_SIMPLE_TYPE
        return datatype.prefixed(self.xs_prefix)

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        if self.use == UseType.REQUIRED:
            restrictions = {"min_occurs": 1, "max_occurs": 1}
        elif self.use == UseType.PROHIBITED:
            restrictions = {"max_occurs": 0, "min_occurs": 0}
        else:
            restrictions = {"max_occurs": 1, "min_occurs": 0}

        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        return restrictions


@dataclass
class AttributeGroup(AnnotationBase):
    """XSD AttributeGroup model representation."""

    ref: str = attribute(default="")
    name: Optional[str] = attribute()
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array["AttributeGroup"] = array_element(name="attributeGroup")

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.ref:
            yield self.ref


@dataclass
class Any(AnnotationBase):
    """XSD Any model representation."""

    namespace: str = attribute(default="##any")
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    process_contents: ProcessType = attribute(
        default=ProcessType.STRICT, name="processContents"
    )

    def __post_init__(self):
        """Clean the namespace value."""
        self.namespace = " ".join(unique_sequence(self.namespace.split()))

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        clean_ns = "_".join(map(clean_uri, self.namespace.split()))
        return f"@{clean_ns}_element"

    @property
    def raw_namespace(self) -> Optional[str]:
        """The element explicit namespace."""
        return self.namespace

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        yield DataType.ANY_TYPE.prefixed(self.xs_prefix)

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "min_occurs": 0,
            "max_occurs": max_occurs,
            "process_contents": self.process_contents.value,
        }


@dataclass
class All(AnnotationBase):
    """XSD All model representation."""

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    any: Array[Any] = array_element(name="any")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "path": [("a", id(self), self.min_occurs, max_occurs)],
        }


@dataclass
class Sequence(AnnotationBase):
    """XSD Sequence model representation."""

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array["Sequence"] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "path": [("s", id(self), self.min_occurs, max_occurs)],
        }


@dataclass
class Choice(AnnotationBase):
    """XSD Choice model representation."""

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array[Sequence] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "path": [("c", id(self), self.min_occurs, max_occurs)],
        }


@dataclass
class Group(AnnotationBase):
    """XSD Group model representation."""

    name: Optional[str] = attribute()
    ref: str = attribute(default="")
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.ref:
            yield self.ref

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "path": [("g", id(self), self.min_occurs, max_occurs)],
        }


@dataclass
class OpenContent(AnnotationBase):
    """XSD OpenContent model representation."""

    applies_to_empty: bool = attribute(default=False, name="appliesToEmpty")
    mode: Mode = attribute(default=Mode.INTERLEAVE)
    any: Any = element()


@dataclass
class DefaultOpenContent(OpenContent):
    """XSD DefaultOpenContent model representation."""


@dataclass
class Extension(AnnotationBase):
    """XSD Extension model representation."""

    base: Optional[str] = attribute()
    group: Optional[Group] = element()
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()
    any_attribute: Optional[AnyAttribute] = element(name="anyAttribute")
    open_content: Optional[OpenContent] = element(name="openContent")
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    assertions: Array[Assertion] = array_element(name="assert")

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.base:
            yield self.base


@dataclass
class Enumeration(AnnotationBase):
    """XSD Enumeration model representation."""

    value: str = attribute()

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def real_name(self) -> str:
        """Return the enumeration value as its name."""
        return self.value

    @property
    def default(self) -> str:
        """Return the enumeration value as its default value."""
        return self.value

    @property
    def is_fixed(self) -> bool:
        """Specify this element has a fixed value."""
        return True


@dataclass
class FractionDigits(AnnotationBase):
    """XSD FractionDigits model representation."""

    value: int = attribute()


@dataclass
class Length(AnnotationBase):
    """XSD Length model representation."""

    value: int = attribute()


@dataclass
class MaxExclusive(AnnotationBase):
    """XSD MaxExclusive model representation."""

    value: str = attribute()


@dataclass
class MaxInclusive(AnnotationBase):
    """XSD MaxInclusive model representation."""

    value: str = attribute()


@dataclass
class MaxLength(AnnotationBase):
    """XSD MaxLength model representation."""

    value: int = attribute()


@dataclass
class MinExclusive(AnnotationBase):
    """XSD MinExclusive model representation."""

    value: str = attribute()


@dataclass
class MinInclusive(AnnotationBase):
    """XSD MinInclusive model representation."""

    value: str = attribute()


@dataclass
class MinLength(AnnotationBase):
    """XSD MinLength model representation."""

    value: int = attribute()


@dataclass
class Pattern(AnnotationBase):
    """XSD Pattern model representation."""

    value: str = attribute()


@dataclass
class TotalDigits(AnnotationBase):
    """XSD TotalDigits model representation."""

    value: int = attribute()


@dataclass
class WhiteSpace(AnnotationBase):
    """XSD WhiteSpace model representation."""

    value: str = attribute()


@dataclass
class ExplicitTimezone(AnnotationBase):
    """XSD ExplicitTimezone model representation."""

    value: str = attribute()
    fixed: bool = attribute(default=False)


@dataclass
class Restriction(AnnotationBase):
    """XSD Restriction model representation."""

    base: Optional[str] = attribute()
    group: Optional[Group] = element()
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()
    open_content: Optional[OpenContent] = element(name="openContent")
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    enumerations: Array[Enumeration] = array_element(name="enumeration")
    asserts: Array[Assertion] = array_element(name="assert")
    assertions: Array[Assertion] = array_element(name="assertion")
    any_element: Array[object] = array_any_element()
    min_exclusive: Optional[MinExclusive] = element(name="minExclusive")
    min_inclusive: Optional[MinInclusive] = element(name="minInclusive")
    min_length: Optional[MinLength] = element(name="minLength")
    max_exclusive: Optional[MaxExclusive] = element(name="maxExclusive")
    max_inclusive: Optional[MaxInclusive] = element(name="maxInclusive")
    max_length: Optional[MaxLength] = element(name="maxLength")
    total_digits: Optional[TotalDigits] = element(name="totalDigits")
    fraction_digits: Optional[FractionDigits] = element(name="fractionDigits")
    length: Optional[Length] = element()
    white_space: Optional[WhiteSpace] = element(name="whiteSpace")
    patterns: Array[Pattern] = array_element(name="pattern")
    explicit_timezone: Optional[ExplicitTimezone] = element(name="explicitTimezone")
    simple_type: Optional[SimpleType] = element(name="simpleType")

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.simple_type:
            yield from self.simple_type.attr_types
        elif self.base and not self.enumerations:
            yield self.base

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        return DEFAULT_ATTR_NAME

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.base:
            yield self.base

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        restrictions = {}
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

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
            "explicit_timezone",
        )
        restrictions.update(
            {
                key: getattr(self, key).value
                for key in keys
                if getattr(self, key) is not None
            }
        )

        if self.patterns:
            restrictions["pattern"] = "|".join(
                pattern.value for pattern in self.patterns
            )

        return restrictions


@dataclass
class SimpleContent(AnnotationBase):
    """XSD SimpleContent model representation."""

    restriction: Optional[Restriction] = element()
    extension: Optional[Extension] = element()


@dataclass
class ComplexContent(SimpleContent):
    """XSD ComplexContent model representation."""

    mixed: bool = attribute(default=False)


@dataclass
class ComplexType(AnnotationBase):
    """XSD ComplexType model representation."""

    name: Optional[str] = attribute()
    block: Optional[str] = attribute()
    final: Optional[str] = attribute()
    simple_content: Optional[SimpleContent] = element(name="simpleContent")
    complex_content: Optional[ComplexContent] = element(name="complexContent")
    group: Optional[Group] = element()
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()
    any_attribute: Optional[AnyAttribute] = element(name="anyAttribute")
    open_content: Optional[OpenContent] = element(name="openContent")
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    assertion: Array[Assertion] = array_element(name="assert")
    abstract: bool = attribute(default=False)
    mixed: bool = attribute(default=False)
    default_attributes_apply: bool = attribute(
        default=True, name="defaultAttributesApply"
    )

    @property
    def is_mixed(self) -> bool:
        """Return whether this element accepts mixed content value."""
        if self.mixed:
            return True

        if self.complex_content:
            return self.complex_content.mixed

        return False


@dataclass
class Field(AnnotationBase):
    """XSD Field model representation."""

    xpath: Optional[str] = attribute()


@dataclass
class Selector(Field):
    """XSD Selector model representation."""


@dataclass
class Unique(AnnotationBase):
    """XSD Unique model representation."""

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Field] = array_element(name="field")


@dataclass
class Key(AnnotationBase):
    """XSD Key model representation."""

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Keyref(AnnotationBase):
    """XSD Keyref model representation."""

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    refer: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Alternative(AnnotationBase):
    """XSD Alternative model representation."""

    type: Optional[str] = attribute()
    test: Optional[str] = attribute()
    simple_type: Optional[SimpleType] = element(name="simpleType")
    complex_type: Optional[ComplexType] = element(name="complexType")

    @property
    def real_name(self) -> str:
        """Return the real name for this element."""
        if self.test:
            return text.snake_case(self.test)
        if self.id:
            return self.id
        return DEFAULT_ATTR_NAME

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.type:
            yield self.type

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        return {
            "path": [("alt", id(self), 0, 1)],
        }


@dataclass
class Element(AnnotationBase):
    """XSD Element model representation."""

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    type: Optional[str] = attribute()
    substitution_group: Optional[str] = attribute(name="substitutionGroup")
    default: Optional[str] = attribute()
    fixed: Optional[str] = attribute()
    form: Optional[FormType] = attribute()
    block: Optional[str] = attribute()
    final: Optional[str] = attribute()
    target_namespace: Optional[str] = attribute(name="targetNamespace")
    simple_type: Optional[SimpleType] = element(name="simpleType")
    complex_type: Optional[ComplexType] = element(name="complexType")
    alternatives: Array[Alternative] = array_element(name="alternative")
    uniques: Array[Unique] = array_element(name="unique")
    keys: Array[Key] = array_element(name="key")
    keyrefs: Array[Keyref] = array_element(name="keyref")
    min_occurs: Optional[int] = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[None, int, str] = attribute(default=1, name="maxOccurs")
    nillable: bool = attribute(default=False)
    abstract: bool = attribute(default=False)

    @property
    def bases(self) -> Iterator[str]:
        """Return an iterator of all the base types."""
        if self.type:
            yield self.type
        elif not self.has_children:
            yield DataType.ANY_TYPE.prefixed(self.xs_prefix)

    @property
    def is_property(self) -> bool:
        """Specify it is qualified to be a class property."""
        return True

    @property
    def is_mixed(self) -> bool:
        """Return whether this element accepts mixed content value."""
        return self.complex_type.is_mixed if self.complex_type else False

    @property
    def default_type(self) -> str:
        """Returned the inferred default type qname."""
        datatype = DataType.STRING if self.fixed else DataType.ANY_TYPE
        return datatype.prefixed(self.xs_prefix)

    @property
    def attr_types(self) -> Iterator[str]:
        """Return the attr types for this element."""
        if self.type:
            yield self.type
        elif self.ref:
            yield self.ref
        elif self.simple_type:
            yield from self.simple_type.attr_types

        yield from (alt.type for alt in self.alternatives if alt.type)

    @property
    def substitutions(self) -> Array[str]:
        """Return a list of the substitution groups."""
        return self.substitution_group.split() if self.substitution_group else []

    def get_restrictions(self) -> Dict[str, Anything]:
        """Return the restrictions dictionary of this element."""
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        restrictions = {
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }

        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        if self.nillable:
            restrictions.update(nillable=True)

        return restrictions


@dataclass
class Notation(AnnotationBase):
    """XSD Notation model representation."""

    name: Optional[str] = attribute()
    public: Optional[str] = attribute()
    system: Optional[str] = attribute()


@dataclass
class Import(AnnotationBase):
    """XSD Import model representation."""

    namespace: Optional[str] = attribute()
    schema_location: Optional[str] = attribute(name="schemaLocation")
    location: Optional[str] = field(default=None, metadata={"type": "ignore"})


@dataclass
class Include(AnnotationBase):
    """XSD Include model representation."""

    schema_location: Optional[str] = attribute(name="schemaLocation")
    location: Optional[str] = field(default=None, metadata={"type": "ignore"})


@dataclass
class Redefine(AnnotationBase):
    """XSD Redefine model representation."""

    schema_location: Optional[str] = attribute(name="schemaLocation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    location: Optional[str] = field(default=None, metadata={"type": "ignore"})


@dataclass
class Override(AnnotationBase):
    """XSD Override model representation."""

    schema_location: Optional[str] = attribute(name="schemaLocation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    elements: Array[Element] = array_element(name="element")
    attributes: Array[Attribute] = array_element(name="attribute")
    notations: Array[Notation] = array_element(name="notation")
    location: Optional[str] = field(default=None, metadata={"type": "ignore"})


@dataclass
class Schema(AnnotationBase):
    """XSD Schema model representation."""

    class Meta:
        """Metadata options."""

        name = "schema"
        namespace = Namespace.XS.uri

    target: Optional[str] = attribute()
    block_default: Optional[str] = attribute(name="blockDefault")
    default_attributes: Optional[str] = attribute(name="defaultAttributes")
    final_default: Optional[str] = attribute(name="finalDefault")
    target_namespace: Optional[str] = attribute(name="targetNamespace")
    version: Optional[str] = attribute()
    xmlns: Optional[str] = attribute()
    element_form_default: FormType = attribute(
        default=FormType.UNQUALIFIED,
        name="elementFormDefault",
    )
    attribute_form_default: FormType = attribute(
        default=FormType.UNQUALIFIED,
        name="attributeFormDefault",
    )
    default_open_content: Optional[DefaultOpenContent] = element(
        name="defaultOpenContent"
    )
    includes: Array[Include] = array_element(name="include")
    imports: Array[Import] = array_element(name="import")
    redefines: Array[Redefine] = array_element(name="redefine")
    overrides: Array[Override] = array_element(name="override")
    annotations: Array[Annotation] = array_element(name="annotation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    elements: Array[Element] = array_element(name="element")
    attributes: Array[Attribute] = array_element(name="attribute")
    notations: Array[Notation] = array_element(name="notation")
    location: Optional[str] = field(default=None, metadata={"type": "ignore"})

    def included(self) -> Iterator[UnionType[Import, Include, Redefine, Override]]:
        """Yields an iterator of included resources."""
        yield from self.imports

        yield from self.includes

        yield from self.redefines

        yield from self.overrides
