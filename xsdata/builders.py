from dataclasses import MISSING
from dataclasses import Field as DataField
from dataclasses import dataclass, fields
from typing import List as Array
from typing import Optional

import stringcase
from lxml import etree


def stripns(text: str):
    try:
        namespace, text = text.split("}", 1)
        return text
    except ValueError:
        return text


def val(field: DataField, attrs: dict):
    name = stringcase.camelcase(field.name)
    if name not in attrs:
        return None if field.default is MISSING else field.default
    elif field.type == int or field.type == Optional[int]:
        try:
            return int(attrs[name])
        except ValueError:
            return 0
    elif field.type == float or field.type == Optional[float]:
        return float(attrs[name])
    elif field.type == bool or field.type == Optional[bool]:
        return attrs[name] == "true"
    else:
        return attrs[name]


class Base:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_element(cls, el: etree.Element):
        attrs = {stripns(key): value for key, value in el.attrib.items()}
        data = {field.name: val(field, attrs) for field in fields(cls)}
        data["nsmap"] = el.nsmap
        data["prefix"] = el.prefix
        return cls(**data)


@dataclass
class ElementBase(Base):
    id: Optional[str]
    prefix: str
    nsmap: dict


@dataclass
class Documentation(ElementBase):
    lang: str
    source: str
    text: str


@dataclass
class Appinfo(ElementBase):
    source: Optional[str]


@dataclass
class Annotation(ElementBase):
    appinfo: Optional[Appinfo]
    documentation: Optional[Documentation]


@dataclass
class AnnotationBase(Annotation):
    pass


@dataclass
class SimpleType(AnnotationBase):
    name: Optional[str]
    restriction: Optional["Restriction"]
    list: Optional["List"]
    union: Optional["Union"]


@dataclass
class List(AnnotationBase):
    item_type: Optional[str]
    simple_type: SimpleType


@dataclass
class Union(AnnotationBase):
    member_types: Optional[str]
    simple_types: Array[SimpleType]


@dataclass
class AnyAttribute(AnnotationBase):
    namespace: Optional[str]
    process_contents: Optional[str]  # lax | skip | strict
    annotation: Optional[Annotation]
    simple_type: Optional[SimpleType]


@dataclass
class Attribute(AnnotationBase):
    default: Optional[str]
    fixed: Optional[str]
    form: Optional[str]  # qualified | unqualified
    name: Optional[str]
    ref: Optional[str]
    type: Optional[str]
    simple_type: Optional[SimpleType]
    use: Optional[str] = "optional"  # optional | prohibited | required


@dataclass
class AttributeGroup(AnnotationBase):
    name: Optional[str]
    ref: Optional[str]

    any_attribute: Optional[AnyAttribute]
    attributes: Array[Attribute]
    attribute_groups: Array["AttributeGroup"]


@dataclass
class All(AnnotationBase):
    elements: Array["Element"]
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Sequence(AnnotationBase):
    elements: Array["Element"]
    groups: Array["Group"]
    choices: Array["Choice"]
    sequences: Array["Sequence"]
    anys: Array["Any"]

    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Choice(AnnotationBase):
    elements: Array["Element"]
    groups: Array["Group"]
    choices: Array["Choice"]
    sequences: Array[Sequence]
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Group(AnnotationBase):
    name: Optional[str]
    ref: Optional[str]
    max_occurs: int = 1
    min_occurs: int = 1
    all = Optional[All]
    choice = Optional[Choice]
    sequence = Optional[Sequence]


@dataclass
class Extension(AnnotationBase):
    base: str
    group: Optional[Group]
    all: Optional[All]
    choice: Optional[Choice]
    sequence: Optional[Sequence]
    any_attribute: Optional[AnyAttribute]
    attributes: Array[Attribute]
    attribute_groups: Array[AttributeGroup]


@dataclass
class Enumeration(Base):
    value: str


@dataclass
class FractionDigits(Base):
    value: int


@dataclass
class Length(Base):
    value: int


@dataclass
class MaxExclusive(Base):
    value: float


@dataclass
class MaxInclusive(Base):
    value: float


@dataclass
class MaxLength(Base):
    value: float


@dataclass
class MinExclusive(Base):
    value: float


@dataclass
class MinInclusive(Base):
    value: float


@dataclass
class MinLength(Base):
    value: float


@dataclass
class Pattern(Base):
    value: str


@dataclass
class TotalDigits(Base):
    value: int


@dataclass
class WhiteSpace(Base):
    value: str  # preserve, collapse, replace


@dataclass
class Restriction(AnnotationBase):
    base: str
    group: Optional[Group]
    all: Optional[All]
    choice: Optional[Choice]
    sequence: Optional[Sequence]
    any_attribute: Optional[AnyAttribute]
    attributes: Array[Attribute]
    attribute_groups: Array[AttributeGroup]

    min_exclusive: Optional[MinExclusive]
    min_inclusive: Optional[MinInclusive]
    min_length: Optional[MinLength]
    max_exclusive: Optional[MaxExclusive]
    max_inclusive: Optional[MaxInclusive]
    max_length: Optional[MaxLength]
    total_digits: Optional[TotalDigits]
    fraction_digits: Optional[FractionDigits]
    length: Optional[Length]
    whiteSpace: Optional[WhiteSpace]
    pattern: Optional[Pattern]
    enumerations: Array[Enumeration]


@dataclass
class SimpleContent(AnnotationBase):
    restriction: Optional[Restriction]
    extension: Optional[Extension]


@dataclass
class ComplexContent(AnnotationBase):
    restriction: Optional[Restriction]
    extension: Optional[Extension]
    mixed: bool = False


@dataclass
class ComplexType:
    name: Optional[str]
    block: Optional[str]
    final: Optional[str]

    simple_content: Optional[SimpleContent]
    complex_content: Optional[ComplexContent]
    group: Optional[Group]
    all: Optional[All]
    choice: Optional[Choice]
    sequence: Optional[Sequence]
    any_attribute: Optional[AnyAttribute]
    attributes: Array[Attribute]
    attribute_groups: Array[AttributeGroup]
    abstract: bool = False
    mixed: bool = False


@dataclass
class Field(AnnotationBase):
    xpath: str


@dataclass
class Selector(Field):
    pass


@dataclass
class Unique(AnnotationBase):
    name: str
    selector: Optional[Selector]
    field: Optional[Field]


@dataclass
class Key(AnnotationBase):
    name: str
    selector: Optional[Selector]
    fields: Array[Selector]


@dataclass
class Keyref(AnnotationBase):
    name: str
    refer: str
    selector: Optional[Selector]
    fields: Array[Selector]


@dataclass
class Element(AnnotationBase):
    id: Optional[str]
    name: str
    ref: Optional[str]
    type: Optional[str]
    substitution_group: Optional[str]
    default: Optional[str]
    fixed: Optional[str]
    form: Optional[str]
    block: Optional[List]
    final: Optional[List]

    simple_type: Optional[SimpleType]
    complex_type: Optional[ComplexType]

    uniques: Array[Unique]
    keys: Array[Key]
    keyrefs: Array[Keyref]

    min_occurs: int = 1
    max_occurs: int = 0

    nillable: bool = False
    abstract: bool = False


@dataclass
class Any(AnnotationBase):
    namespace: Optional[str]
    process_contents: Optional[str]  # lax | skip | strict
    annotation: Optional[Annotation]
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Import(AnnotationBase):
    namespace: Optional[str]
    schema_location: Optional[str]


@dataclass
class Include(AnnotationBase):
    schema_location: Optional[str]


@dataclass
class Notation(AnnotationBase):
    name: str
    public: str
    system: Optional[str]


@dataclass
class Redefined(AnnotationBase):
    schema_location: str
    simple_type: Optional[SimpleType]
    complex_type: Optional[ComplexType]
    group: Optional[Group]
    attribute_group: Optional[AttributeGroup]


@dataclass
class Schema(AnnotationBase):
    attribute_form_default: Optional[str]
    element_form_default: Optional[str]
    block_default: Optional[str]
    final_default: Optional[str]
    target_namespace: Optional[str]
    version: Optional[str]
    xmlns: Optional[str]

    includes: Array[Include]
    imports: Array[Import]
    redefineds: Array[Redefined]
    annotations: Array[Annotation]
    simpleTypes: Array[SimpleType]
    complexTypes: Array[ComplexType]
    groups: Array[Group]
    attributeGroups: Array[AttributeGroup]
    elements: Array[Element]
    attributes: Array[Attribute]
