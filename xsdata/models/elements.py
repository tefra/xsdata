from dataclasses import dataclass
from dataclasses import field
from dataclasses import MISSING
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as ArrayList
from typing import Optional
from typing import Union as UnionType

from xsdata.formats.dataclass.utils import tostring
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
from xsdata.models.enums import ProcessType
from xsdata.models.enums import TagType
from xsdata.models.enums import UseType
from xsdata.models.mixins import ElementBase
from xsdata.models.mixins import NamedField
from xsdata.models.mixins import OccurrencesMixin
from xsdata.models.mixins import RestrictedField


def attribute(default=MISSING, default_factory=MISSING, init=True, **kwargs):
    kwargs.update(type=TagType.ATTRIBUTE)
    return field(
        init=init, default=default, default_factory=default_factory, metadata=kwargs
    )


def element(default=MISSING, default_factory=MISSING, init=True, **kwargs):
    kwargs.update(type=TagType.ELEMENT)
    return field(
        init=init, default=default, default_factory=default_factory, metadata=kwargs
    )


def any_element(default=MISSING, default_factory=MISSING, init=True, **kwargs):
    kwargs.update(type=TagType.ANY)
    return field(
        init=init, default=default, default_factory=default_factory, metadata=kwargs
    )


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

    lang: Optional[str] = attribute(default=None)
    source: Optional[str] = attribute(default=None)
    elements: ArrayList[object] = any_element(default_factory=list)

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

    source: Optional[str] = attribute(default=None)
    elements: ArrayList[object] = any_element(default_factory=list)


@dataclass
class Annotation(ElementBase):
    """
    <annotation
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (appinfo | documentation)*
    </annotation>
    """

    appinfo: Optional[Appinfo] = element(default=None)
    documentations: ArrayList[Documentation] = element(
        default_factory=list, name="documentation"
    )


@dataclass
class AnnotationBase(ElementBase):
    """Base Class for elements that can contain annotations."""

    annotation: Optional[Annotation] = element(default=None)

    @property
    def display_help(self) -> Optional[str]:
        if self.annotation and len(self.annotation.documentations):
            return "\n".join(
                filter(None, [doc.tostring() for doc in self.annotation.documentations])
            )
        return None


@dataclass
class Assertion(AnnotationBase):
    """
    {annotations} A sequence of Annotation components.

    {test} An XPath Expression property record. Required.
    """

    test: Optional[str] = attribute(default=None)


@dataclass
class SimpleType(AnnotationBase, NamedField, RestrictedField):
    """
    <simpleType
      final = (#all | List of (list | union | restriction | extension))
      id = ID
      name = NCName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (restriction | list | union))
    </simpleType>
    """

    name: Optional[str] = attribute(default=None)
    restriction: Optional["Restriction"] = element(default=None)
    list: Optional["List"] = element(default=None)
    union: Optional["Union"] = element(default=None)

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
class List(AnnotationBase, RestrictedField, NamedField):
    """
    <list
      id = ID
      itemType = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType?)
    </list>
    """

    simple_type: Optional[SimpleType] = element(default=None)
    item_type: Optional[str] = attribute(default=None)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> Optional[str]:
        return None

    def get_restrictions(self) -> Dict[str, Anything]:
        return dict()


@dataclass
class Union(AnnotationBase, NamedField, RestrictedField):
    """
    <union
      id = ID
      memberTypes = List of QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, simpleType*)
    </union>
    """

    member_types: Optional[str] = attribute(default=None)
    simple_types: ArrayList[SimpleType] = element(
        default_factory=list, name="simpleType"
    )

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
class AnyAttribute(AnnotationBase, NamedField, RestrictedField):
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

    namespace: Optional[str] = attribute(default=None)
    process_contents: Optional[ProcessType] = attribute(default=None)

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> Optional[str]:
        return DataType.QMAP.xml_prefixed

    @property
    def real_name(self) -> str:
        return "attributes"

    def get_restrictions(self) -> Dict[str, Anything]:
        return dict()


@dataclass
class Attribute(AnnotationBase, NamedField, RestrictedField):
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

    default: Optional[str] = attribute(default=None)
    fixed: Optional[str] = attribute(default=None)
    form: Optional[FormType] = attribute(default=None)
    name: Optional[str] = attribute(default=None)
    ref: Optional[str] = attribute(default=None)
    type: Optional[str] = attribute(default=None)
    simple_type: Optional[SimpleType] = element(default=None)
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
            restrictions["required"] = True
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        return restrictions


@dataclass
class AttributeGroup(AnnotationBase, NamedField):
    """
    <attributeGroup
      id = ID
      ref = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </attributeGroup>
    """

    name: Optional[str] = attribute(default=None)
    ref: Optional[str] = attribute(default=None)
    any_attribute: Optional[AnyAttribute] = element(default=None)
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")
    attribute_groups: ArrayList["AttributeGroup"] = element(
        default_factory=list, name="attributeGroup"
    )

    @property
    def extends(self) -> Optional[str]:
        return self.ref

    @property
    def real_type(self) -> Optional[str]:
        return None


@dataclass
class Any(AnnotationBase, OccurrencesMixin, NamedField):
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

    min_occurs: Optional[int] = attribute(default=None)
    max_occurs: Optional[int] = attribute(default=None)
    namespace: Optional[str] = attribute(default=None)
    process_contents: Optional[ProcessType] = attribute(default=None)
    annotation: Optional[Annotation] = element(default=None)

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
    elements: ArrayList["Element"] = element(default_factory=list, name="element")
    any: Any = element(default=None)


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
    elements: ArrayList["Element"] = element(default_factory=list, name="element")
    groups: ArrayList["Group"] = element(default_factory=list, name="group")
    choices: ArrayList["Choice"] = element(default_factory=list, name="choice")
    sequences: ArrayList["Sequence"] = element(default_factory=list, name="sequence")
    any: ArrayList["Any"] = element(default_factory=list)


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
    elements: ArrayList["Element"] = element(default_factory=list, name="element")
    groups: ArrayList["Group"] = element(default_factory=list, name="group")
    choices: ArrayList["Choice"] = element(default_factory=list, name="choice")
    sequences: ArrayList[Sequence] = element(default_factory=list, name="sequence")
    any: ArrayList["Any"] = element(default_factory=list)


@dataclass
class Group(AnnotationBase, OccurrencesMixin, NamedField):
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

    name: Optional[str] = attribute(default=None)
    ref: Optional[str] = attribute(default=None)
    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    all: Optional[All] = element(default=None)
    choice: Optional[Choice] = element(default=None)
    sequence: Optional[Sequence] = element(default=None)

    @property
    def extends(self) -> Optional[str]:
        return self.ref


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

    base: Optional[str] = attribute(default=None)
    group: Optional[Group] = element(default=None)
    all: Optional[All] = element(default=None)
    choice: Optional[Choice] = element(default=None)
    sequence: Optional[Sequence] = element(default=None)
    any_attribute: Optional[AnyAttribute] = element(default=None)
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )
    assertions: ArrayList[Assertion] = element(default_factory=list, name="assert")

    @property
    def extends(self) -> Optional[str]:
        return self.base


@dataclass
class Enumeration(AnnotationBase, NamedField, RestrictedField):
    """
    <enumeration
      id = ID
      value = anySimpleType
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?)
    </enumeration>
    """

    value: Optional[str] = attribute(default=None)

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

    def get_restrictions(self):
        return {}


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

    value: Optional[int] = attribute(default=None)


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

    value: Optional[int] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[float] = attribute(default=None)


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

    value: Optional[str] = attribute(default=None)


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

    value: Optional[int] = attribute(default=None)


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

    value: Optional[str] = attribute(default=None)  # preserve, collapse, replace


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

    value: Optional[UseType] = attribute(default=None)
    fixed: Optional[str] = attribute(default=None)


@dataclass
class Restriction(RestrictedField, AnnotationBase, NamedField):
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
    CONTAINER_FIELDS = (
        "group",
        "all",
        "choice",
        "sequence",
        "any_attribute",
        "attributes",
        "attribute_groups",
        "enumerations",
    )

    base: Optional[str] = attribute(default=None)
    group: Optional[Group] = element(default=None)
    all: Optional[All] = element(default=None)
    choice: Optional[Choice] = element(default=None)
    sequence: Optional[Sequence] = element(default=None)
    any_attribute: Optional[AnyAttribute] = element(default=None)
    min_exclusive: Optional[MinExclusive] = element(default=None)
    min_inclusive: Optional[MinInclusive] = element(default=None)
    min_length: Optional[MinLength] = element(default=None)
    max_exclusive: Optional[MaxExclusive] = element(default=None)
    max_inclusive: Optional[MaxInclusive] = element(default=None)
    max_length: Optional[MaxLength] = element(default=None)
    total_digits: Optional[TotalDigits] = element(default=None)
    fraction_digits: Optional[FractionDigits] = element(default=None)
    length: Optional[Length] = element(default=None)
    white_space: Optional[WhiteSpace] = element(default=None)
    pattern: Optional[Pattern] = element(default=None)
    explicit_timezone: Optional[ExplicitTimezone] = element(default=None)
    simple_type: Optional[SimpleType] = element(default=None)
    enumerations: ArrayList[Enumeration] = element(
        default_factory=list, name="enumeration"
    )
    asserts: ArrayList[Assertion] = element(default_factory=list, name="assert")
    assertions: ArrayList[Assertion] = element(default_factory=list, name="assertion")
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )

    @property
    def is_attribute(self) -> bool:
        for key in self.CONTAINER_FIELDS:
            if getattr(self, key):
                return False
        return True

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

    restriction: Optional[Restriction] = element(default=None)
    extension: Optional[Extension] = element(default=None)


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
class ComplexType(AnnotationBase, NamedField):
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

    name: Optional[str] = attribute(default=None)
    block: Optional[str] = attribute(default=None)
    final: Optional[str] = attribute(default=None)
    simple_content: Optional[SimpleContent] = element(default=None)
    complex_content: Optional[ComplexContent] = element(default=None)
    group: Optional[Group] = element(default=None)
    all: Optional[All] = element(default=None)
    choice: Optional[Choice] = element(default=None)
    sequence: Optional[Sequence] = element(default=None)
    any_attribute: Optional[AnyAttribute] = element(default=None)
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )
    assertion: ArrayList[Assertion] = element(default_factory=list, name="assert")
    abstract: bool = attribute(default=False)
    mixed: bool = attribute(default=False)

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

    xpath: Optional[str] = attribute(default=None)


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

    name: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    field: Optional[Field] = element(default=None)


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

    name: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    fields: ArrayList[Selector] = element(default_factory=list, name="field")


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

    name: Optional[str] = attribute(default=None)
    refer: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    fields: ArrayList[Selector] = element(default_factory=list, name="field")


@dataclass
class Element(AnnotationBase, NamedField, OccurrencesMixin):
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

    name: Optional[str] = attribute(default=None)
    id: Optional[str] = attribute(default=None)
    ref: Optional[str] = attribute(default=None)
    type: Optional[str] = attribute(default=None)
    substitution_group: Optional[str] = attribute(default=None)
    default: Optional[str] = attribute(default=None)
    fixed: Optional[str] = attribute(default=None)
    form: Optional[FormType] = attribute(default=None)
    block: Optional[str] = attribute(default=None)
    final: Optional[str] = attribute(default=None)
    simple_type: Optional[SimpleType] = element(default=None)
    complex_type: Optional[ComplexType] = element(default=None)
    uniques: ArrayList[Unique] = element(default_factory=list, name="unique")
    keys: ArrayList[Key] = element(default_factory=list, name="key")
    keyrefs: ArrayList[Keyref] = element(default_factory=list, name="keyref")
    min_occurs: Optional[int] = attribute(default=None)
    max_occurs: Optional[int] = attribute(default=None)
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
        if self.type:
            return self.type
        if self.ref:
            return self.ref
        if self.simple_type:
            return self.simple_type.real_type

        return None

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

    namespace: Optional[str] = attribute(default=None)
    schema_location: Optional[str] = attribute(default=None)


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

    schema_location: Optional[str] = attribute(default=None)

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

    name: Optional[str] = attribute(default=None)
    public: Optional[str] = attribute(default=None)
    system: Optional[str] = attribute(default=None)


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

    schema_location: Optional[str] = attribute(default=None)
    simple_types: ArrayList[SimpleType] = element(
        default_factory=list, name="simpleType"
    )
    complex_types: ArrayList[ComplexType] = element(
        default_factory=list, name="complexType"
    )
    groups: ArrayList[Group] = element(default_factory=list, name="group")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )


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

    schema_location: Optional[str] = attribute(default=None)
    simple_types: ArrayList[SimpleType] = element(
        default_factory=list, name="simpleType"
    )
    complex_types: ArrayList[ComplexType] = element(
        default_factory=list, name="complexType"
    )
    groups: ArrayList[Group] = element(default_factory=list, name="group")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )
    elements: ArrayList[Element] = element(default_factory=list, name="element")
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")


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
        namespace = Namespace.SCHEMA.uri

    target: Optional[str] = attribute(default=None)
    block_default: Optional[str] = attribute(default=None)
    final_default: Optional[str] = attribute(default=None)
    target_namespace: Optional[str] = attribute(default=None)
    version: Optional[str] = attribute(default=None)
    xmlns: Optional[str] = attribute(default=None)
    nsmap: Dict = field(default_factory=dict)
    location: Optional[Path] = field(default=None)
    element_form_default: FormType = attribute(default=FormType.UNQUALIFIED)
    attribute_form_default: FormType = attribute(default=FormType.UNQUALIFIED)
    includes: ArrayList[Include] = element(default_factory=list, name="include")
    imports: ArrayList[Import] = element(default_factory=list, name="import")
    redefines: ArrayList[Redefine] = element(default_factory=list, name="redefine")
    overrides: ArrayList[Override] = element(default_factory=list, name="override")
    annotations: ArrayList[Annotation] = element(
        default_factory=list, name="annotation"
    )
    simple_types: ArrayList[SimpleType] = element(
        default_factory=list, name="simpleType"
    )
    complex_types: ArrayList[ComplexType] = element(
        default_factory=list, name="complexType"
    )
    groups: ArrayList[Group] = element(default_factory=list, name="group")
    attribute_groups: ArrayList[AttributeGroup] = element(
        default_factory=list, name="attributeGroup"
    )
    elements: ArrayList[Element] = element(default_factory=list, name="element")
    attributes: ArrayList[Attribute] = element(default_factory=list, name="attribute")
    notations: ArrayList[Notation] = element(default_factory=list, name="notation")

    # any_attribute: AnyAttribute = aat(default_factory=list)

    def sub_schemas(self) -> Iterator[UnionType[Import, Include, Redefine, Override]]:
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
            return self.location.stem

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
