import re
import sys
from dataclasses import MISSING
from dataclasses import Field as Attrib
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import List as ArrayList
from typing import Optional

from lxml import etree

from xsdata.models.enums import XMLSchema, XSDType
from xsdata.models.mixins import (
    ExtendsMixin,
    NamedField,
    OccurrencesMixin,
    RestrictedField,
    TypedField,
)
from xsdata.utils.text import snake_case


def stripns(text: str) -> str:
    try:
        namespace, text = text.split("}", 1)
        return text
    except ValueError:
        return text


class BaseModel:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_element(cls, el: etree.Element):
        attrs = {
            snake_case(stripns(key)): value for key, value in el.attrib.items()
        }
        data = {
            attr.name: cls.xsd_value(attr, attrs)
            if attr.name in attrs
            else cls.default_value(attr)
            for attr in fields(cls)
            if attr.init
        }

        if "nsmap" in data:
            data["nsmap"] = el.nsmap
        if "prefix" in data:
            data["prefix"] = el.prefix
        if "text" in data and el.text:
            data["text"] = re.sub(r"\s+", " ", el.text).strip()

        return cls(**data)

    @classmethod
    def default_value(cls, field: Attrib):
        factory = getattr(field, "default_factory")
        if getattr(field, "default_factory") is not MISSING:
            return factory()  # mypy: ignore
        return None if field.default is MISSING else field.default

    @classmethod
    def xsd_value(cls, field: Attrib, kwargs):
        name = field.name
        value = kwargs[name]
        clazz = field.type

        if name == "max_occurs" and value == "unbounded":
            return sys.maxsize

        # Optional
        if hasattr(clazz, "__origin__"):
            clazz = clazz.__args__[0]

        if clazz == bool:
            return value == "true"

        try:
            if clazz == int:
                return int(value)
            if clazz == float:
                return float(value)
        except ValueError:
            pass

        return str(value)

    @classmethod
    def build(cls, **kwargs):
        if not kwargs.get("prefix") and not kwargs.get("nsmap"):
            kwargs.update({"prefix": "xs", "nsmap": {"xs": XMLSchema}})

        data = {
            attr.name: kwargs[attr.name]
            if attr.name in kwargs
            else cls.default_value(attr)
            for attr in fields(cls)
            if attr.init
        }

        return cls(**data)


@dataclass
class ElementBase(BaseModel):
    id: Optional[str]
    prefix: str
    nsmap: dict

    def children(self):
        for attribute in fields(self):
            value = getattr(self, attribute.name)
            if (
                isinstance(value, list)
                and len(value)
                and isinstance(value[0], ElementBase)
            ):
                for v in value:
                    yield v
            elif isinstance(value, ElementBase):
                yield value


@dataclass
class Documentation(ElementBase):
    lang: Optional[str]
    source: Optional[str]
    text: Optional[str]


@dataclass
class Appinfo(ElementBase):
    source: Optional[str]


@dataclass
class Annotation(ElementBase):
    appinfo: Optional[Appinfo]
    documentation: Optional[Documentation]


@dataclass
class AnnotationBase(ElementBase):
    annotation: Optional[Annotation]

    @property
    def display_help(self) -> Optional[str]:
        return (
            self.annotation.documentation.text
            if self.annotation and self.annotation.documentation
            else None
        )


@dataclass
class SimpleType(
    AnnotationBase, TypedField, NamedField, ExtendsMixin, RestrictedField
):
    name: Optional[str]
    restriction: Optional["Restriction"]
    list: Optional["List"]
    union: Optional["Union"]

    @property
    def real_type(self) -> Optional[str]:
        if self.restriction:
            return self.restriction.real_type
        if self.list:
            return self.list.real_type
        if self.union:
            pass  # I can't do unions
        return XSDType.STRING.code

    @property
    def extensions(self) -> ArrayList[str]:
        return []

    def get_restrictions(self) -> Dict[str, Anything]:
        if self.restriction:
            return self.restriction.get_restrictions()
        if self.list:
            return self.list.get_restrictions()
        return dict()


@dataclass
class List(AnnotationBase, RestrictedField):
    item_type: Optional[str]
    simple_type: SimpleType

    @property
    def real_type(self) -> Optional[str]:
        if self.item_type:
            return self.item_type
        if self.simple_type:
            return self.simple_type.real_type
        return None

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict(min_occurs=0, max_occurs=sys.maxsize)
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())
        return restrictions


@dataclass
class Union(AnnotationBase):
    member_types: Optional[str]
    simple_types: ArrayList[SimpleType] = field(default_factory=list)


@dataclass
class AnyAttribute(AnnotationBase):
    namespace: Optional[str]
    process_contents: Optional[str]  # lax | skip | strict
    simple_type: Optional[SimpleType]


@dataclass
class Attribute(
    AnnotationBase, TypedField, NamedField, RestrictedField, ExtendsMixin
):
    default: Optional[str]
    fixed: Optional[str]
    form: Optional[str]  # qualified | unqualified
    name: Optional[str]
    ref: Optional[str]
    type: Optional[str]
    simple_type: Optional[SimpleType]
    use: Optional[str] = "optional"  # optional | prohibited | required

    @property
    def real_type(self) -> Optional[str]:
        if self.simple_type:
            return self.simple_type.real_type
        if self.type:
            return self.type
        if self.ref:
            return self.ref

        return XSDType.STRING.code

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = dict()
        if self.use == "required":
            restrictions["required"] = True
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        return restrictions

    @property
    def extensions(self) -> ArrayList[str]:
        return []


@dataclass
class AttributeGroup(AnnotationBase, NamedField, ExtendsMixin):
    name: Optional[str]
    ref: Optional[str]
    any_attribute: Optional[AnyAttribute]
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList["AttributeGroup"] = field(default_factory=list)

    @property
    def extensions(self) -> ArrayList[str]:
        return []


@dataclass
class All(AnnotationBase, OccurrencesMixin):
    elements: ArrayList["Element"] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Sequence(AnnotationBase, OccurrencesMixin):
    elements: ArrayList["Element"] = field(default_factory=list)
    groups: ArrayList["Group"] = field(default_factory=list)
    choices: ArrayList["Choice"] = field(default_factory=list)
    sequences: ArrayList["Sequence"] = field(default_factory=list)
    anys: ArrayList["Any"] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Choice(AnnotationBase, OccurrencesMixin):
    elements: ArrayList["Element"] = field(default_factory=list)
    groups: ArrayList["Group"] = field(default_factory=list)
    choices: ArrayList["Choice"] = field(default_factory=list)
    sequences: ArrayList[Sequence] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Group(AnnotationBase, OccurrencesMixin):
    name: Optional[str]
    ref: Optional[str]
    max_occurs: int = 1
    min_occurs: int = 1
    all = Optional[All]
    choice = Optional[Choice]
    sequence = Optional[Sequence]


@dataclass
class Extension(AnnotationBase, ExtendsMixin):
    base: str
    group: Optional[Group]
    all: Optional[All]
    choice: Optional[Choice]
    sequence: Optional[Sequence]
    any_attribute: Optional[AnyAttribute]
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)

    @property
    def extensions(self) -> ArrayList[str]:
        return [self.base]


@dataclass
class RestrictionType(AnnotationBase):
    pass


@dataclass
class Enumeration(RestrictionType):
    value: str


@dataclass
class FractionDigits(RestrictionType):
    value: int


@dataclass
class Length(RestrictionType):
    value: int


@dataclass
class MaxExclusive(RestrictionType):
    value: float


@dataclass
class MaxInclusive(RestrictionType):
    value: float


@dataclass
class MaxLength(RestrictionType):
    value: float


@dataclass
class MinExclusive(RestrictionType):
    value: float


@dataclass
class MinInclusive(RestrictionType):
    value: float


@dataclass
class MinLength(RestrictionType):
    value: float


@dataclass
class Pattern(RestrictionType):
    value: str


@dataclass
class TotalDigits(RestrictionType):
    value: int


@dataclass
class WhiteSpace(RestrictionType):
    value: str  # preserve, collapse, replace


@dataclass
class Restriction(RestrictedField, AnnotationBase, TypedField, NamedField):
    base: str
    group: Optional[Group]
    all: Optional[All]
    choice: Optional[Choice]
    sequence: Optional[Sequence]
    any_attribute: Optional[AnyAttribute]
    min_exclusive: Optional[MinExclusive]
    min_inclusive: Optional[MinInclusive]
    min_length: Optional[MinLength]
    max_exclusive: Optional[MaxExclusive]
    max_inclusive: Optional[MaxInclusive]
    max_length: Optional[MaxLength]
    total_digits: Optional[TotalDigits]
    fraction_digits: Optional[FractionDigits]
    length: Optional[Length]
    white_space: Optional[WhiteSpace]
    pattern: Optional[Pattern]
    enumerations: ArrayList[Enumeration] = field(default_factory=list)
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)

    @property
    def real_type(self) -> Optional[str]:
        return self.base

    @property
    def real_name(self) -> str:
        return "value"

    def get_restrictions(self) -> Dict[str, Anything]:
        lookup = [
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
            "enumerations",
        ]
        return {
            key: getattr(self, key).value
            for key in lookup
            if isinstance(getattr(self, key), RestrictionType)
        }


@dataclass
class SimpleContent(AnnotationBase, ExtendsMixin):
    restriction: Optional[Restriction]
    extension: Optional[Extension]

    @property
    def extensions(self) -> ArrayList[str]:
        if self.extension:
            return self.extension.extensions
        else:
            return []


@dataclass
class ComplexContent(SimpleContent):
    mixed: bool = False


@dataclass
class ComplexType(AnnotationBase, NamedField, ExtendsMixin):
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
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)
    abstract: bool = False
    mixed: bool = False

    @property
    def extensions(self) -> ArrayList[str]:
        if self.complex_content:
            return self.complex_content.extensions
        if self.simple_content:
            return self.simple_content.extensions
        if self.attribute_groups:
            return [group.real_name for group in self.attribute_groups]
        return []


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
    fields: ArrayList[Selector] = field(default_factory=list)


@dataclass
class Keyref(AnnotationBase):
    name: str
    refer: str
    selector: Optional[Selector]
    fields: ArrayList[Selector] = field(default_factory=list)


@dataclass
class Element(
    AnnotationBase, TypedField, NamedField, OccurrencesMixin, ExtendsMixin
):
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
    uniques: ArrayList[Unique] = field(default_factory=list)
    keys: ArrayList[Key] = field(default_factory=list)
    keyrefs: ArrayList[Keyref] = field(default_factory=list)
    min_occurs: int = 1
    max_occurs: int = 1
    nillable: bool = False
    abstract: bool = False

    @property
    def real_type(self) -> Optional[str]:
        if self.type:
            return self.type
        if self.ref:
            return self.ref
        if self.simple_type:
            return self.simple_type.real_type
        if self.complex_type:
            return None
        return XSDType.STRING.code

    @property
    def extensions(self) -> ArrayList[str]:
        if self.complex_type:
            return self.complex_type.extensions
        elif self.type:
            return [self.type]
        return []

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = super().get_restrictions()
        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())
        return restrictions


@dataclass
class Any(AnnotationBase, OccurrencesMixin):
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
    target: Optional[str]
    attribute_form_default: Optional[str]
    element_form_default: Optional[str]
    block_default: Optional[str]
    final_default: Optional[str]
    target_namespace: Optional[str]
    version: Optional[str]
    xmlns: Optional[str]
    includes: ArrayList[Include] = field(default_factory=list)
    imports: ArrayList[Import] = field(default_factory=list)
    redefineds: ArrayList[Redefined] = field(default_factory=list)
    annotations: ArrayList[Annotation] = field(default_factory=list)
    simple_types: ArrayList[SimpleType] = field(default_factory=list)
    complex_types: ArrayList[ComplexType] = field(default_factory=list)
    groups: ArrayList[Group] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)
    elements: ArrayList[Element] = field(default_factory=list)
    attributes: ArrayList[Attribute] = field(default_factory=list)
    location: Path = field(init=False)

    def sub_schemas(self) -> ArrayList[str]:
        sub = [x.schema_location for x in self.imports if x.schema_location]
        sub.extend(
            [x.schema_location for x in self.includes if x.schema_location]
        )
        return sub
