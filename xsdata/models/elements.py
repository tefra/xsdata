from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as Array
from typing import Optional
from typing import Union as UnionType

from xsdata.formats.dataclass.utils import tostring
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.enums import ProcessType
from xsdata.models.enums import TagType
from xsdata.models.enums import UseType
from xsdata.models.mixins import ElementBase
from xsdata.models.mixins import OccurrencesMixin
from xsdata.models.mixins import RestrictedField


def attribute(default=None, init=True, **kwargs):
    kwargs.update(type=TagType.ATTRIBUTE)
    return field(init=init, default=default, metadata=kwargs)


def element(init=True, **kwargs):
    kwargs.update(type=TagType.ELEMENT)
    return field(init=init, default=None, metadata=kwargs)


def array_element(init=True, **kwargs):
    kwargs.update(type=TagType.ELEMENT)
    return field(init=init, default_factory=list, metadata=kwargs)


def array_any_element(init=True, **kwargs):
    kwargs.update(type=TagType.ANY)
    return field(init=init, default_factory=list, metadata=kwargs)


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
    any_attribute: Optional["AnyAttribute"] = element()

    def tostring(self) -> Optional[str]:
        if not self.elements:
            return None

        return tostring(self.elements)


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
    any_attribute: Optional["AnyAttribute"] = element()


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
    any_attribute: Optional["AnyAttribute"] = element()


@dataclass
class AnnotationBase(ElementBase):
    """Base Class for elements that can contain annotations."""

    annotation: Optional[Annotation] = element()
    any_attribute: Optional["AnyAttribute"] = element()

    @property
    def display_help(self) -> Optional[str]:
        if self.annotation and len(self.annotation.documentations):
            return "\n".join(
                filter(None, [doc.tostring() for doc in self.annotation.documentations])
            )
        return None


@dataclass
class AnyAttribute(AnnotationBase, RestrictedField):
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

    namespace: Optional[str] = attribute()
    process_contents: Optional[ProcessType] = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        return DataType.QMAP.xml_prefixed

    @property
    def real_name(self) -> str:
        return "attributes"


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
class SimpleType(AnnotationBase, RestrictedField):
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
    def is_enumeration(self):
        return self.restriction and len(self.restriction.enumerations) > 0

    @property
    def is_attribute(self) -> bool:
        return self.is_enumeration

    @property
    def real_type(self) -> Optional[str]:
        if self.restriction:
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
class List(AnnotationBase, RestrictedField):
    """
    <list
      id = ID
      itemType = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType?)
    </list>
    """

    simple_type: Optional[SimpleType] = element()
    item_type: Optional[str] = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> Optional[str]:
        return None


@dataclass
class Union(AnnotationBase, RestrictedField):
    """
    <union
      id = ID
      memberTypes = List of QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType*)
    </union>
    """

    member_types: Optional[str] = attribute()
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

    @property
    def real_name(self) -> str:
        return "value"

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict()
        for simple_type in self.simple_types:
            restrictions.update(simple_type.get_restrictions())
        return restrictions


@dataclass
class Attribute(AnnotationBase, RestrictedField):
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
    simple_type: Optional[SimpleType] = element()
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
        if self.use in (UseType.REQUIRED, UseType.PROHIBITED):
            restrictions[self.use.value] = True
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        return restrictions


@dataclass
class AttributeGroup(AnnotationBase, RestrictedField):
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
    def extends(self) -> Optional[str]:
        return self.ref

    @property
    def real_type(self) -> Optional[str]:
        return None


@dataclass
class Any(AnnotationBase, OccurrencesMixin):
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

    min_occurs: Optional[int] = attribute()
    max_occurs: Optional[int] = attribute()
    namespace: Optional[str] = attribute()
    process_contents: Optional[ProcessType] = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        return DataType.OBJECT.xml_prefixed

    @property
    def real_name(self) -> str:
        return "elements"


@dataclass
class All(AnnotationBase, OccurrencesMixin):
    """
    <all
      id = ID
      maxOccurs = (0 | 1) : 1
      minOccurs = (0 | 1) : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | any | group)*)
    </all>
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    any: Any = element()
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")


@dataclass
class Sequence(AnnotationBase, OccurrencesMixin):
    """
    <sequence
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | group | choice | sequence | any)*)
    </sequence>
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array["Sequence"] = array_element(name="sequence")
    any: Array["Any"] = array_element()


@dataclass
class Choice(AnnotationBase, OccurrencesMixin):
    """
    <choice
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (element | group | choice | sequence | any)*)
    </choice>
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array[Sequence] = array_element(name="sequence")
    any: Array["Any"] = array_element()


@dataclass
class Group(AnnotationBase, OccurrencesMixin):
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
    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()

    @property
    def extends(self) -> Optional[str]:
        return self.ref


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
class Extension(AnnotationBase, RestrictedField):
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
    any_attribute: Optional[AnyAttribute] = element()
    open_content: Optional[OpenContent] = element(name="openContent")
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    assertions: Array[Assertion] = array_element(name="assert")

    @property
    def extends(self) -> Optional[str]:
        return self.base


@dataclass
class Enumeration(AnnotationBase, RestrictedField):
    """
    <enumeration
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </enumeration>
    """

    value: Optional[str] = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self):
        return None

    @property
    def real_name(self):
        return self.value

    @property
    def default(self):
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

    value: Optional[int] = attribute()


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

    value: Optional[int] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[float] = attribute()


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

    value: Optional[str] = attribute()


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

    value: Optional[int] = attribute()


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

    value: Optional[str] = attribute()  # preserve, collapse, replace


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

    value: Optional[UseType] = attribute()
    fixed: Optional[str] = attribute()


@dataclass
class Restriction(RestrictedField, AnnotationBase):
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

    VALUE_FIELDS = (
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

    min_exclusive: Optional[MinExclusive] = element()
    min_inclusive: Optional[MinInclusive] = element()
    min_length: Optional[MinLength] = element()
    max_exclusive: Optional[MaxExclusive] = element()
    max_inclusive: Optional[MaxInclusive] = element()
    max_length: Optional[MaxLength] = element()
    total_digits: Optional[TotalDigits] = element()
    fraction_digits: Optional[FractionDigits] = element()
    length: Optional[Length] = element()
    white_space: Optional[WhiteSpace] = element()
    pattern: Optional[Pattern] = element()
    explicit_timezone: Optional[ExplicitTimezone] = element()
    simple_type: Optional[SimpleType] = element()

    @property
    def real_type(self) -> Optional[str]:
        if self.simple_type:
            return self.simple_type.real_type
        return self.base

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def extends(self) -> Optional[str]:
        return self.base

    def get_restrictions(self) -> Dict[str, Anything]:
        return {
            key: getattr(self, key).value
            for key in self.VALUE_FIELDS
            if getattr(self, key) is not None
        }


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
class ComplexType(AnnotationBase, RestrictedField):
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
    simple_content: Optional[SimpleContent] = element()
    complex_content: Optional[ComplexContent] = element()
    group: Optional[Group] = element()
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()
    any_attribute: Optional[AnyAttribute] = element()
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
        elif self.complex_content and self.complex_content.mixed:
            return True
        else:
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
    field: Optional[Field] = element()


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
    simple_type: Optional[SimpleType] = element()
    complex_type: Optional[ComplexType] = element()


@dataclass
class Element(AnnotationBase, OccurrencesMixin):
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
    id: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    type: Optional[str] = attribute()
    substitution_group: Optional[str] = attribute()
    default: Optional[str] = attribute()
    fixed: Optional[str] = attribute()
    form: Optional[FormType] = attribute()
    block: Optional[str] = attribute()
    final: Optional[str] = attribute()
    target_namespace: Optional[str] = attribute(name="targetNamespace")
    simple_type: Optional[SimpleType] = element()
    complex_type: Optional[ComplexType] = element()
    alternatives: Array[Alternative] = array_element(name="alternative")
    uniques: Array[Unique] = array_element(name="unique")
    keys: Array[Key] = array_element(name="key")
    keyrefs: Array[Keyref] = array_element(name="keyref")
    min_occurs: Optional[int] = attribute()
    max_occurs: Optional[int] = attribute()
    nillable: bool = attribute(default=False)
    abstract: bool = attribute(default=False)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def is_mixed(self) -> bool:
        if self.complex_type:
            return self.complex_type.is_mixed

        return False

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

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = super().get_restrictions()
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())
        if self.nillable:
            restrictions.update({"nillable": True})
        return restrictions


@dataclass
class Import(AnnotationBase):
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
    schema_location: Optional[str] = attribute()


@dataclass
class Include(AnnotationBase):
    """
    <include
      id = ID
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </include>
    """

    schema_location: Optional[str] = attribute()

    @property
    def namespace(self):
        return None


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
class Redefine(AnnotationBase):
    """
    <redefine
      id = ID
      schemaLocation = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: (annotation | (simpleType | complexType | group | attributeGroup))*
    </redefine>
    """

    schema_location: Optional[str] = attribute()
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")


@dataclass
class Override(AnnotationBase):
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

    schema_location: Optional[str] = attribute()
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")
    elements: Array[Element] = array_element(name="element")
    attributes: Array[Attribute] = array_element(name="attribute")
    notations: Array[Notation] = array_element(name="notation")


@dataclass
class Schema(AnnotationBase):
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
    block_default: Optional[str] = attribute()
    default_attributes: Optional[str] = attribute(name="defaultAttributes")
    final_default: Optional[str] = attribute()
    target_namespace: Optional[str] = attribute()
    version: Optional[str] = attribute()
    xmlns: Optional[str] = attribute()
    nsmap: Dict = field(default_factory=dict)
    location: Optional[Path] = field(default=None)
    element_form_default: FormType = attribute(default=FormType.UNQUALIFIED)
    attribute_form_default: FormType = attribute(default=FormType.UNQUALIFIED)
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

    def sub_schemas(self) -> Iterator[UnionType[Import, Include, Redefine, Override]]:
        imp_namespaces = [imp.namespace for imp in self.imports]
        instance_ns = Namespace.XSI.value
        if instance_ns in self.nsmap.values() and instance_ns not in imp_namespaces:
            yield Import.create(namespace=instance_ns)

        for imp in self.imports:
            yield imp

        for inc in self.includes:
            yield inc

        for red in self.redefines:
            yield red

        for over in self.overrides:
            yield over

    @property
    def module(self):
        if self.location:
            return self.location.name

        if self.target_namespace:
            return Path(self.target_namespace).stem

        for el in self.elements:
            if el.name:
                return Path(el.name).stem

        for el in self.complex_types:
            if el.name:
                return Path(el.name).stem

        raise ValueError("Unknown schema module")

    @property
    def target_prefix(self):
        return next(
            (
                prefix
                for prefix, namespace in self.nsmap.items()
                if namespace == self.target_namespace
            ),
            None,
        )
