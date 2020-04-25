import sys
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as Array
from typing import Optional
from typing import Union as UnionType

from xsdata.exceptions import SchemaValueError
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import ProcessType
from xsdata.models.enums import UseType
from xsdata.models.mixins import ElementBase
from xsdata.utils import text
from xsdata.utils.text import collapse_whitespace


def attribute(default: Anything = None, init: bool = True, **kwargs: str) -> Anything:
    kwargs.update(type=XmlType.ATTRIBUTE)
    return field(init=init, default=default, metadata=kwargs)


def element(init: bool = True, **kwargs: str) -> Anything:
    kwargs.update(type=XmlType.ELEMENT)
    return field(init=init, default=None, metadata=kwargs)


def array_element(init: bool = True, **kwargs: str) -> Anything:
    kwargs.update(type=XmlType.ELEMENT)
    return field(init=init, default_factory=list, metadata=kwargs)


def array_any_element(init: bool = True, **kwargs: str) -> Anything:
    kwargs.update(type=XmlType.WILDCARD, namespace=NamespaceType.ANY.value)
    return field(init=init, default_factory=list, metadata=kwargs)


def occurrences(min_value: int, max_value: UnionType[int, str]) -> Dict[str, int]:
    max_value = sys.maxsize if max_value == "unbounded" else int(max_value)
    return dict(min_occurs=min_value, max_occurs=max_value)


@dataclass(frozen=True)
class XmlString:
    elements: Array[object] = array_any_element()

    def render(self) -> str:
        name = self.__class__.__name__
        xml = XmlSerializer(pretty_print=True, xml_declaration=False).render(self)
        start = xml.find(">") + 1
        return xml[start:].replace(f"</{name}>", "").strip()


@dataclass
class Documentation(ElementBase):
    """
    <documentation
      source = anyURI
      xml:lang = language
      {any attributes with non-schema namespace . . .}>
      Content: ({any})*
    </documentation>
    """

    class Meta:
        mixed = True

    lang: Optional[str] = attribute()
    source: Optional[str] = attribute()
    elements: Array[object] = array_any_element()
    attributes: Optional["AnyAttribute"] = element()

    def tostring(self) -> Optional[str]:
        return XmlString(self.elements).render() if self.elements else None


@dataclass
class Appinfo(ElementBase):
    """
    <appinfo
      source = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: ({any})*
    </appinfo>
    """

    class Meta:
        mixed = True

    source: Optional[str] = attribute()
    elements: Array[object] = array_any_element()
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")


@dataclass
class Annotation(ElementBase):
    """
    <annotation
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (appinfo | documentation)*
    </annotation>
    """

    appinfo: Optional[Appinfo] = element()
    documentations: Array[Documentation] = array_element(name="documentation")
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")


@dataclass
class AnnotationBase(ElementBase):
    """Base Class for elements that can contain annotations."""

    id: Optional[str] = attribute()
    annotation: Optional[Annotation] = element()
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")

    @property
    def display_help(self) -> Optional[str]:
        if self.annotation and len(self.annotation.documentations) > 0:
            return "\n".join(
                filter(None, [doc.tostring() for doc in self.annotation.documentations])
            )
        return None


@dataclass
class AnyAttribute(AnnotationBase):
    """
    <anyAttribute
      id = ID
      namespace = ((##any | ##other) | List of (anyURI | (##targetNamespace | ##local)))
      notNamespace = List of (anyURI | (##targetNamespace | ##local))
      notQName = List of (QName | ##defined)
      processContents = (lax | skip | strict) : strict
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </anyAttribute>
    """

    namespace: Optional[str] = attribute(default="##any")
    process_contents: Optional[ProcessType] = attribute(name="processContents")

    def __post_init__(self):
        self.namespace = collapse_whitespace(self.namespace)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def raw_namespace(self) -> Optional[str]:
        return self.namespace

    @property
    def real_name(self) -> str:
        if self.namespace is None:
            raise SchemaValueError("Wildcards namespace can't be None.")

        namespace = (
            self.namespace[2:] if self.namespace.startswith("##") else self.namespace
        )
        return f"{namespace}_attributes"

    @property
    def real_type(self) -> Optional[str]:
        prefix = self.schema_prefix()
        suffix = DataType.QMAP.code
        return f"{prefix}:{suffix}" if prefix else suffix


@dataclass
class Assertion(AnnotationBase):
    """
    <assertion
      id = ID
      test = an XPath expression
      xpathDefaultNamespace =
        (anyURI | (##defaultNamespace | ##targetNamespace | ##local))
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </assertion>
    """

    test: Optional[str] = attribute()


@dataclass
class SimpleType(AnnotationBase):
    """
    <simpleType
      final = (#all | List of (list | union | restriction | extension))
      id = ID
      name = NCName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (restriction | list | union))
    </simpleType>
    """

    name: Optional[str] = attribute()
    restriction: Optional["Restriction"] = element()
    list: Optional["List"] = element()
    union: Optional["Union"] = element()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def is_enumeration(self) -> bool:
        return (
            True
            if self.restriction and len(self.restriction.enumerations) > 0
            else False
        )

    @property
    def real_name(self) -> str:
        if self.name:
            return self.name
        return "value"

    @property
    def real_type(self) -> Optional[str]:
        if not self.is_enumeration and self.restriction:
            return self.restriction.real_type
        if self.list:
            return self.list.real_type
        if self.union:
            return self.union.member_types

        return None

    def get_restrictions(self) -> Dict[str, Anything]:
        if self.restriction:
            return self.restriction.get_restrictions()
        if self.list:
            return self.list.get_restrictions()
        return dict()


@dataclass
class List(AnnotationBase):
    """
    <list
      id = ID
      itemType = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType?)
    </list>
    """

    simple_type: Optional[SimpleType] = element(name="simpleType")
    item_type: Optional[str] = attribute(name="itemType")

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> Optional[str]:
        return self.item_type

    def get_restrictions(self) -> Dict[str, Anything]:
        return occurrences(0, sys.maxsize)


@dataclass
class Union(AnnotationBase):
    """
    <union
      id = ID
      memberTypes = List of QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType*)
    </union>
    """

    member_types: Optional[str] = attribute(name="memberTypes")
    simple_types: Array[SimpleType] = array_element(name="simpleType")

    @property
    def extends(self) -> Optional[str]:
        if self.member_types:
            return self.member_types
        return None

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> Optional[str]:
        types = []
        if self.simple_types:
            types.extend(
                [
                    simple_type.real_type
                    for simple_type in self.simple_types
                    if simple_type.real_type
                ]
            )
        if self.member_types:
            types.extend([member for member in self.member_types.split(" ") if member])

        return " ".join(types) if types else None

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict()
        for simple_type in self.simple_types:
            restrictions.update(simple_type.get_restrictions())
        return restrictions


@dataclass
class Attribute(AnnotationBase):
    """
    <attribute
      default = string
      fixed = string
      form = (qualified | unqualified)
      id = ID
      name = NCName
      ref = QName
      targetNamespace = anyURI
      type = QName
      use = (optional | prohibited | required) : optional
      inheritable = boolean
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType?)
    </attribute>
    """

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
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        if self.simple_type:
            return self.simple_type.real_type
        if self.type:
            return self.type
        if self.ref:
            return self.ref

        return None

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict()
        if self.use == UseType.REQUIRED:
            restrictions.update({"min_occurs": 1, "max_occurs": 1, "required": True})
        elif self.use == UseType.PROHIBITED:
            restrictions.update({"prohibited": True})

        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        return restrictions


@dataclass
class AttributeGroup(AnnotationBase):
    """
    <attributeGroup
      id = ID
      ref = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </attributeGroup>
    """

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array["AttributeGroup"] = array_element(name="attributeGroup")

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        return self.ref


@dataclass
class Any(AnnotationBase):
    """
    <any
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      namespace = ((##any | ##other) | List of (anyURI | (##targetNamespace | ##local)))
      notNamespace = List of (anyURI | (##targetNamespace | ##local))
      notQName = List of (QName | (##defined | ##definedSibling))
      processContents = (lax | skip | strict) : strict
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </any>
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    namespace: Optional[str] = attribute(default="##any")
    process_contents: Optional[ProcessType] = attribute(name="processContents")

    def __post_init__(self):
        self.namespace = collapse_whitespace(self.namespace)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        if self.namespace is None:
            raise SchemaValueError("Wildcards namespace can't be None.")

        namespace = (
            self.namespace[2:] if self.namespace.startswith("##") else self.namespace
        )
        return f"{namespace}_element"

    @property
    def raw_namespace(self) -> Optional[str]:
        return self.namespace

    @property
    def real_type(self) -> Optional[str]:
        prefix = self.schema_prefix()
        suffix = DataType.OBJECT.code
        return f"{prefix}:{suffix}" if prefix else suffix

    def get_restrictions(self) -> Dict[str, Anything]:
        return occurrences(self.min_occurs, self.max_occurs)


@dataclass
class All(AnnotationBase):
    """
    <all
      id = ID
      maxOccurs = (0 | 1) : 1
      minOccurs = (0 | 1) : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | any | group)*)
    </all>
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    any: Array[Any] = array_element(name="any")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")

    def get_restrictions(self) -> Dict[str, Anything]:
        return occurrences(self.min_occurs, self.max_occurs)


@dataclass
class Sequence(AnnotationBase):
    """
    <sequence
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | group | choice | sequence | any)*)
    </sequence>
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array["Sequence"] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = occurrences(self.min_occurs, self.max_occurs)
        restrictions.update(dict(sequential=True))
        return restrictions


@dataclass
class Choice(AnnotationBase):
    """
    <choice
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | group | choice | sequence | any)*)
    </choice>
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array[Sequence] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        return occurrences(
            self.min_occurs if self.min_occurs > 1 else 0, self.max_occurs
        )


@dataclass
class Group(AnnotationBase):
    """
    <group
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      name = NCName
      ref = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (all | choice | sequence)?)
    </group>
    """

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        return self.ref

    def get_restrictions(self) -> Dict[str, Anything]:
        return occurrences(self.min_occurs, self.max_occurs)


@dataclass
class OpenContent(AnnotationBase):
    """
    <openContent
      id = ID
      mode = (none | interleave | suffix) : interleave
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, any?)
    </openContent>
    """

    applies_to_empty: bool = attribute(default=False, name="appliesToEmpty")
    mode: Mode = attribute(default=Mode.INTERLEAVE)
    any: Any = element()


@dataclass
class DefaultOpenContent(OpenContent):
    """
    <defaultOpenContent
      appliesToEmpty = boolean : false
      id = ID
      mode = (interleave | suffix) : interleave
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, any)
    </defaultOpenContent>
    """


@dataclass
class Extension(AnnotationBase):
    """
    <extension
      base = QName
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, ((attribute | attributeGroup)*, anyAttribute?), assert*)
    </extension>
    """

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
    def extends(self) -> Optional[str]:
        return self.base


@dataclass
class Enumeration(AnnotationBase):
    """
    <enumeration
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </enumeration>
    """

    value: str = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> None:
        return None

    @property
    def real_name(self) -> str:
        return self.value

    @property
    def default(self) -> str:
        return self.value


@dataclass
class FractionDigits(AnnotationBase):
    """
    <fractionDigits
      fixed = boolean : false
      id = ID
      value = nonNegativeInteger
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </fractionDigits>
    """

    value: int = attribute()


@dataclass
class Length(AnnotationBase):
    """
    <length
      fixed = boolean : false
      id = ID
      value = nonNegativeInteger
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </length>
    """

    value: int = attribute()


@dataclass
class MaxExclusive(AnnotationBase):
    """
    <maxExclusive
      fixed = boolean : false
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </maxExclusive>
    """

    value: float = attribute()


@dataclass
class MaxInclusive(AnnotationBase):
    """
    <maxInclusive
      fixed = boolean : false
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </maxInclusive>
    """

    value: float = attribute()


@dataclass
class MaxLength(AnnotationBase):
    """
    <maxLength
      fixed = boolean : false
      id = ID
      value = nonNegativeInteger
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </maxLength>
    """

    value: float = attribute()


@dataclass
class MinExclusive(AnnotationBase):
    """
    <minExclusive
      fixed = boolean : false
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </minExclusive>
    """

    value: float = attribute()


@dataclass
class MinInclusive(AnnotationBase):
    """
    <minInclusive
      fixed = boolean : false
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </minInclusive>
    """

    value: float = attribute()


@dataclass
class MinLength(AnnotationBase):
    """
    <minLength
      fixed = boolean : false
      id = ID
      value = nonNegativeInteger
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </minLength>
    """

    value: float = attribute()


@dataclass
class Pattern(AnnotationBase):
    """
    <pattern
      id = ID
      value = string
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </pattern>
    """

    value: str = attribute()


@dataclass
class TotalDigits(AnnotationBase):
    """
    <totalDigits
      fixed = boolean : false
      id = ID
      value = positiveInteger
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </totalDigits>
    """

    value: int = attribute()


@dataclass
class WhiteSpace(AnnotationBase):
    """
    <whiteSpace
      fixed = boolean : false
      id = ID
      value = (collapse | preserve | replace)
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </whiteSpace>
    """

    value: str = attribute()  # preserve, collapse, replace


@dataclass
class ExplicitTimezone(AnnotationBase):
    """
    <explicitTimezone
      fixed = boolean : false
      id = ID
      value = NCName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </explicitTimezone>
    """

    value: str = attribute()
    fixed: bool = attribute(default=False)


@dataclass
class Restriction(AnnotationBase):
    """
    <restriction
      base = QName
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (simpleType?, (
        minExclusive | minInclusive | maxExclusive | maxInclusive |
        totalDigits | fractionDigits | length | minLength | maxLength |
        enumeration | whiteSpace | pattern | assertion | explicitTimezone |
        {any with namespace: ##other})*)
      )
    </restriction>
    """

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
    def real_type(self) -> Optional[str]:
        if self.simple_type:
            return self.simple_type.real_type
        if self.enumerations:
            return None
        return self.base

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def extends(self) -> Optional[str]:
        return self.base

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict()
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
                [pattern.value for pattern in self.patterns]
            )

        return restrictions


@dataclass
class SimpleContent(AnnotationBase):
    """
    <simpleContent
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (restriction | extension))
    </simpleContent>
    """

    restriction: Optional[Restriction] = element()
    extension: Optional[Extension] = element()


@dataclass
class ComplexContent(SimpleContent):
    """
    <complexContent
      id = ID
      mixed = boolean
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (restriction | extension))
    </complexContent>
    """

    mixed: bool = attribute(default=False)


@dataclass
class ComplexType(AnnotationBase):
    """
    <complexType
      abstract = boolean : false
      block = (#all | List of (extension | restriction))
      final = (#all | List of (extension | restriction))
      id = ID
      mixed = boolean
      name = NCName
      defaultAttributesApply = boolean : true
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (
        simpleContent | complexContent |
        (openContent?, (group | all | choice | sequence)?,
        ((attribute | attributeGroup)*, anyAttribute?), assert*))
      )
    </complexType>
    """

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
        if self.mixed:
            return True

        if self.complex_content:
            return self.complex_content.mixed

        return False


@dataclass
class Field(AnnotationBase):
    """
    <field
      id = ID
      xpath = a subset of XPath expression, see below
      xpathDefaultNamespace =
        (anyURI | (##defaultNamespace | ##targetNamespace | ##local))
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </field>
    """

    xpath: Optional[str] = attribute()


@dataclass
class Selector(Field):
    """
    <selector
      id = ID
      xpath = a subset of XPath expression, see below
      xpathDefaultNamespace =
        (anyURI | (##defaultNamespace | ##targetNamespace | ##local))
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </selector>
    """


@dataclass
class Unique(AnnotationBase):
    """
    <unique
      id = ID
      name = NCName
      ref = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (selector, field+)?)
    </unique>
    """

    name: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Field] = array_element(name="field")


@dataclass
class Key(AnnotationBase):
    """
    <key
      id = ID
      name = NCName
      ref = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (selector, field+)?)
    </key>
    """

    name: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Keyref(AnnotationBase):
    """
    <keyref
      id = ID
      name = NCName
      ref = QName
      refer = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (selector, field+)?)
    </keyref>
    """

    name: Optional[str] = attribute()
    refer: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Alternative(AnnotationBase):
    """
    <alternative
      id = ID
      test = an XPath expression
      type = QName
      xpathDefaultNamespace =
        (anyURI | (##defaultNamespace | ##targetNamespace | ##local))
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (simpleType | complexType)?)
    </alternative>
    """

    type: Optional[str] = attribute()
    test: Optional[str] = attribute()
    simple_type: Optional[SimpleType] = element(name="simpleType")
    complex_type: Optional[ComplexType] = element(name="complexType")

    @property
    def real_name(self) -> str:
        if self.test:
            return text.snake_case(self.test)
        if self.id:
            return self.id
        return "value"


@dataclass
class Element(AnnotationBase):
    """
    <element
      abstract = boolean : false
      block = (#all | List of (extension | restriction | substitution))
      default = string
      final = (#all | List of (extension | restriction))
      fixed = string
      form = (qualified | unqualified)
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      name = NCName
      nillable = boolean : false
      ref = QName
      substitutionGroup = List of QName
      targetNamespace = anyURI
      type = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?,
        ((simpleType | complexType)?, alternative*, (unique | key | keyref)*))
    </element>
    """

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
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    nillable: bool = attribute(default=False)
    abstract: bool = attribute(default=False)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def is_mixed(self) -> bool:
        return self.complex_type.is_mixed if self.complex_type else False

    @property
    def default_type(self) -> DataType:
        return DataType.ANY_TYPE

    @property
    def raw_type(self) -> Optional[str]:
        if self.type:
            return self.type

        if self.has_children:
            return None

        prefix = self.schema_prefix()
        suffix = DataType.ANY_TYPE.code
        return f"{prefix}:{suffix}" if prefix else suffix

    @property
    def real_type(self) -> Optional[str]:

        types = set(
            alternative.type for alternative in self.alternatives if alternative.type
        )
        if self.type:
            types.add(self.type)
        elif self.ref:
            types.add(self.ref)
        elif self.simple_type and self.simple_type.real_type:
            types.add(self.simple_type.real_type)

        return " ".join(sorted(types)) or None

    @property
    def substitutions(self) -> Array[str]:
        if self.substitution_group:
            return list(filter(None, self.substitution_group.split(" ")))

        return list()

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = occurrences(self.min_occurs, self.max_occurs)
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())
        if self.nillable:
            restrictions.update({"nillable": True})

        return restrictions


@dataclass
class Notation(AnnotationBase):
    """
    <notation
      id = ID
      name = NCName
      public = token
      system = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </notation>
    """

    name: Optional[str] = attribute()
    public: Optional[str] = attribute()
    system: Optional[str] = attribute()


@dataclass
class SchemaLocation(AnnotationBase):
    location: Optional[Path] = field(default=None)


@dataclass
class Import(SchemaLocation):
    """
    <import
      id = ID
      namespace = anyURI
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </import>
    """

    namespace: Optional[str] = attribute()
    schema_location: Optional[str] = attribute(name="schemaLocation")


@dataclass
class Include(SchemaLocation):
    """
    <include
      id = ID
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </include>
    """

    schema_location: Optional[str] = attribute(name="schemaLocation")


@dataclass
class Redefine(SchemaLocation):
    """
    <redefine
      id = ID
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation | (simpleType | complexType | group | attributeGroup))*
    </redefine>
    """

    schema_location: Optional[str] = attribute(name="schemaLocation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")


@dataclass
class Override(SchemaLocation):
    """
    <override
      id = ID
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (
        annotation | (simpleType | complexType | group |
        attributeGroup | element | attribute | notation)
      )*
    </override>
    """

    schema_location: Optional[str] = attribute(name="schemaLocation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    elements: Array[Element] = array_element(name="element")
    attributes: Array[Attribute] = array_element(name="attribute")
    notations: Array[Notation] = array_element(name="notation")


@dataclass
class Schema(SchemaLocation):
    """
    <schema
      attributeFormDefault = (qualified | unqualified) : unqualified
      blockDefault = (#all | List of (extension | restriction | substitution))  : ''
      defaultAttributes = QName
      xpathDefaultNamespace =
      (anyURI | (##defaultNamespace | ##targetNamespace | ##local)) : ##local
      elementFormDefault = (qualified | unqualified) : unqualified
      finalDefault = (#all | List of (extension | restriction | list | union))  : ''
      id = ID
      targetNamespace = anyURI
      version = token
      xml:lang = language
      {any attributes with non-schema namespace . . .}>
      Content: (
        (include | import | redefine | override | annotation)*,
        (defaultOpenContent, annotation*)?,
        ((simpleType | complexType | group | attributeGroup |
         element | attribute | notation), annotation*)*)
    </schema>
    """

    class Meta:
        namespace = Namespace.XS.uri

    target: Optional[str] = attribute()
    block_default: Optional[str] = attribute(name="blockDefault")
    default_attributes: Optional[str] = attribute(name="defaultAttributes")
    final_default: Optional[str] = attribute(name="finalDefault")
    target_namespace: Optional[str] = attribute(name="targetNamespace")
    version: Optional[str] = attribute()
    xmlns: Optional[str] = attribute()
    element_form_default: FormType = attribute(
        default=FormType.UNQUALIFIED, name="elementFormDefault"
    )
    attribute_form_default: FormType = attribute(
        default=FormType.UNQUALIFIED, name="attributeFormDefault"
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

    def included(self) -> Iterator[UnionType[Import, Include, Redefine, Override]]:
        for imp in self.imports:
            yield imp

        for inc in self.includes:
            yield inc

        for red in self.redefines:
            yield red

        for over in self.overrides:
            yield over

    @property
    def module(self) -> str:
        if self.location:
            return self.location.name

        if self.target_namespace:
            return Path(self.target_namespace).stem

        raise SchemaValueError("Unknown schema module.")
