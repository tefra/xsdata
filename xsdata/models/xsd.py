import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as Array
from typing import Optional
from typing import Union as UnionType

from lxml.html.clean import clean_html

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.enums import ProcessType
from xsdata.models.enums import UseType
from xsdata.models.mixins import array_any_element
from xsdata.models.mixins import array_element
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element
from xsdata.models.mixins import ElementBase
from xsdata.models.mixins import ModuleMixin
from xsdata.utils import text
from xsdata.utils.collections import unique_sequence
from xsdata.utils.namespaces import clean_uri

docstring_serializer = XmlSerializer(pretty_print=True)


@dataclass(frozen=True)
class Docstring:
    elements: Array[object] = array_any_element()


@dataclass
class Documentation(ElementBase):
    """
    Model representation of a schema xs:documentation element.

    :param lang: language
    :param source: anyURI
    :param elements: ({any})*
    :param attributes: any attributes with non-schema namespace
    """

    lang: Optional[str] = attribute()
    source: Optional[str] = attribute()
    elements: Array[object] = array_any_element(mixed=True)
    attributes: Optional["AnyAttribute"] = element()

    def tostring(self) -> Optional[str]:
        xml = docstring_serializer.render(Docstring(self.elements)).split("\n", 1)
        return clean_html(xml[1])[5:-7].strip()


@dataclass
class Appinfo(ElementBase):
    """
    Model representation of a schema xs:appinfo element.

    :param lang: language
    :param source: anyURI
    :param attributes: any attributes with non-schema namespace
    """

    class Meta:
        mixed = True

    source: Optional[str] = attribute()
    elements: Array[object] = array_any_element()
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")


@dataclass
class Annotation(ElementBase):
    """
    Model representation of a schema xs:annotation element.

    :param appinfo:
    :param documentations:
    :param any_attribute: any attributes with non-schema namespace
    """

    appinfo: Optional[Appinfo] = element()
    documentations: Array[Documentation] = array_element(name="documentation")
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")


@dataclass
class AnnotationBase(ElementBase):
    """
    Base Class for elements that can contain annotations.

    :param id: ID
    :param annotations:
    :param any_attribute: any attributes with non-schema namespace
    """

    id: Optional[str] = attribute()
    annotations: Array[Annotation] = array_element(name="annotation")
    any_attribute: Optional["AnyAttribute"] = element(name="anyAttribute")

    @property
    def display_help(self) -> Optional[str]:
        help_str = "\n".join(
            documentation.tostring() or ""
            for annotation in self.annotations
            for documentation in annotation.documentations
        ).strip()

        return help_str or None


@dataclass
class AnyAttribute(AnnotationBase):
    """
    Model representation of a schema xs:anyAttribute element.

    :param namespace: ##any | ##other) | List of anyURI | (##targetNamespace | ##local)
    :param process_contents: (lax | skip | strict) : strict
    """

    namespace: str = attribute(default="##any")
    process_contents: Optional[ProcessType] = attribute(name="processContents")

    def __post_init__(self):
        self.namespace = " ".join(unique_sequence(self.namespace.split()))

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def raw_namespace(self) -> Optional[str]:
        return self.namespace

    @property
    def real_name(self) -> str:
        clean_ns = "_".join(map(clean_uri, self.namespace.split()))
        return f"{clean_ns}_attributes"

    @property
    def real_type(self) -> str:
        return self.data_type_ref(DataType.ANY_TYPE)


@dataclass
class Assertion(AnnotationBase):
    """
    Model representation of a schema xs:assertion element.

    :param test: an XPath expression
    """

    test: Optional[str] = attribute()


@dataclass
class SimpleType(AnnotationBase):
    """
    Model representation of a schema xs:simpleType element.

    :param name: NCName
    :param restriction:
    :param list:
    :param union:
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
        return self.restriction is not None and len(self.restriction.enumerations) > 0

    @property
    def real_name(self) -> str:
        if self.name:
            return self.name
        return "value"

    @property
    def real_type(self) -> str:
        if not self.is_enumeration and self.restriction:
            return self.restriction.real_type
        if self.list:
            return self.list.real_type
        if self.union and self.union.member_types:
            return self.union.member_types

        return ""

    def get_restrictions(self) -> Dict[str, Anything]:
        if self.restriction:
            return self.restriction.get_restrictions()
        if self.list:
            return self.list.get_restrictions()
        return {}


@dataclass
class List(AnnotationBase):
    """
    Model representation of a schema xs:list element.

    :param simple_type:
    :param item_type: QName
    """

    simple_type: Optional[SimpleType] = element(name="simpleType")
    item_type: str = attribute(name="itemType", default="")

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> str:
        return self.item_type

    def get_restrictions(self) -> Dict[str, Anything]:
        return {"tokens": True}


@dataclass
class Union(AnnotationBase):
    """
    Model representation of a schema xs:union element.

    :param member_types: List of QName
    :param simple_types:
    """

    member_types: Optional[str] = attribute(name="memberTypes")
    simple_types: Array[SimpleType] = array_element(name="simpleType")

    @property
    def extensions(self) -> Iterator[str]:
        if self.member_types:
            yield from self.member_types.split()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def real_type(self) -> str:
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
            types.extend(self.member_types.split())

        return " ".join(types)

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = {}
        for simple_type in self.simple_types:
            restrictions.update(simple_type.get_restrictions())
        return restrictions


@dataclass
class Attribute(AnnotationBase):
    """
    Model representation of a schema xs:attribute element.

    :param default: string
    :param fixed: string
    :param form: qualified | unqualified
    :param name: NCName
    :param ref: QName
    :param type: QName
    :param target_namespace: anyURI
    :param simple_type:
    :param use: (optional | prohibited | required) : optional
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
    def real_type(self) -> str:
        if self.simple_type:
            return self.simple_type.real_type
        if self.type:
            return self.type
        if self.ref:
            return self.ref

        return ""

    def get_restrictions(self) -> Dict[str, Anything]:
        restrictions = {}
        if self.use == UseType.REQUIRED:
            restrictions.update({"min_occurs": 1, "max_occurs": 1, "required": True})
        elif self.use == UseType.PROHIBITED:
            restrictions.update({"prohibited": True})

        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        if self.type and self.type in self.token_types:
            restrictions["tokens"] = True

        return restrictions


@dataclass
class AttributeGroup(AnnotationBase):
    """
    Model representation of a schema xs:attributeGroup element.

    :param name: NCName
    :param ref: QName
    :param attributes: any attributes with non-schema namespace
    :param attribute_groups:
    """

    ref: str = attribute(default="")
    name: Optional[str] = attribute()
    attributes: Array[Attribute] = array_element(name="attribute")
    attribute_groups: Array["AttributeGroup"] = array_element(name="attributeGroup")

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> str:
        return self.ref


@dataclass
class Any(AnnotationBase):
    """
    Model representation of a schema xs:any element.

    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param namespace: List of (anyURI | (##targetNamespace | ##local))
    :param process_contents: (lax | skip | strict) : strict
    """

    namespace: str = attribute(default="##any")
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    process_contents: Optional[ProcessType] = attribute(name="processContents")

    def __post_init__(self):
        self.namespace = " ".join(unique_sequence(self.namespace.split()))

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_name(self) -> str:
        clean_ns = "_".join(map(clean_uri, self.namespace.split()))
        return f"{clean_ns}_element"

    @property
    def raw_namespace(self) -> Optional[str]:
        return self.namespace

    @property
    def real_type(self) -> str:
        return self.data_type_ref(DataType.ANY_TYPE)

    def get_restrictions(self) -> Dict[str, Anything]:
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }


@dataclass
class All(AnnotationBase):
    """
    Model representation of a schema xs:all element.

    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param any:
    :param elements:
    :param groups:
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    any: Array[Any] = array_element(name="any")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")

    def get_restrictions(self) -> Dict[str, Anything]:
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }


@dataclass
class Sequence(AnnotationBase):
    """
    Model representation of a schema xs:sequence element.

    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param elements:
    :param groups:
    :param choices:
    :param sequences:
    :param any:
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array["Sequence"] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "sequential": True,
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }


@dataclass
class Choice(AnnotationBase):
    """
    Model representation of a schema xs:choice element.

    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param elements:
    :param groups:
    :param choices:
    :param sequences:
    :param any:
    """

    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    elements: Array["Element"] = array_element(name="element")
    groups: Array["Group"] = array_element(name="group")
    choices: Array["Choice"] = array_element(name="choice")
    sequences: Array[Sequence] = array_element(name="sequence")
    any: Array["Any"] = array_element()

    def get_restrictions(self) -> Dict[str, Anything]:
        min_occurs = self.min_occurs if self.min_occurs > 1 else 0
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "choice": str(id(self)),
            "min_occurs": min_occurs,
            "max_occurs": max_occurs,
        }


@dataclass
class Group(AnnotationBase):
    """
    Model representation of a schema xs:group element.

    :param name: NCName
    :param ref: QName
    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param all:
    :param choice:
    :param sequence:
    """

    name: Optional[str] = attribute()
    ref: str = attribute(default="")
    min_occurs: int = attribute(default=1, name="minOccurs")
    max_occurs: UnionType[int, str] = attribute(default=1, name="maxOccurs")
    all: Optional[All] = element()
    choice: Optional[Choice] = element()
    sequence: Optional[Sequence] = element()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> str:
        return self.ref

    def get_restrictions(self) -> Dict[str, Anything]:
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        return {
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }


@dataclass
class OpenContent(AnnotationBase):
    """
    Model representation of a schema xs:openContent element.

    :param applies_to_empty: default false
    :param mode: (none | interleave | suffix) : interleave
    :param any:
    """

    applies_to_empty: bool = attribute(default=False, name="appliesToEmpty")
    mode: Mode = attribute(default=Mode.INTERLEAVE)
    any: Any = element()


@dataclass
class DefaultOpenContent(OpenContent):
    """Model representation of a schema xs:defaultOpenContent element."""


@dataclass
class Extension(AnnotationBase):
    """
    Model representation of a schema xs:extension element.

    :param base: QName
    :param group:
    :param all:
    :param choice:
    :param sequence:
    :param any_attribute: any attributes with non-schema namespace
    :param open_content:
    :param attributes:
    :param attribute_groups:
    :param assertions:
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
    def extensions(self) -> Iterator[str]:
        if self.base:
            yield self.base


@dataclass
class Enumeration(AnnotationBase):
    """
    Model representation of a schema xs:enumeration element.

    :param value: anySimpleType
    """

    value: str = attribute()

    @property
    def is_attribute(self) -> bool:
        return True

    @property
    def real_type(self) -> str:
        return ""

    @property
    def real_name(self) -> str:
        return self.value

    @property
    def default(self) -> str:
        return self.value


@dataclass
class FractionDigits(AnnotationBase):
    """
    Model representation of a schema xs:fractionDigits element.

    :param value: nonNegativeInteger
    """

    value: int = attribute()


@dataclass
class Length(AnnotationBase):
    """
    Model representation of a schema xs:length element.

    :param value: nonNegativeInteger
    """

    value: int = attribute()


@dataclass
class MaxExclusive(AnnotationBase):
    """
    Model representation of a schema xs:maxExclusive element.

    :param value: anySimpleType
    """

    value: str = attribute()


@dataclass
class MaxInclusive(AnnotationBase):
    """
    Model representation of a schema xs:maxInclusive element.

    :param value: anySimpleType
    """

    value: str = attribute()


@dataclass
class MaxLength(AnnotationBase):
    """
    Model representation of a schema xs:maxLength element.

    :param value: nonNegativeInteger
    """

    value: int = attribute()


@dataclass
class MinExclusive(AnnotationBase):
    """
    Model representation of a schema xs:minExclusive element.

    :param value: anySimpleType
    """

    value: str = attribute()


@dataclass
class MinInclusive(AnnotationBase):
    """
    Model representation of a schema xs:minInclusive element.

    :param value: anySimpleType
    """

    value: str = attribute()


@dataclass
class MinLength(AnnotationBase):
    """
    Model representation of a schema xs:minLength element.

    :param value: nonNegativeInteger
    """

    value: int = attribute()


@dataclass
class Pattern(AnnotationBase):
    """
    Model representation of a schema xs:pattern element.

    :param value: string
    """

    value: str = attribute()


@dataclass
class TotalDigits(AnnotationBase):
    """
    Model representation of a schema xs:totalDigits element.

    :param value: positiveInteger
    """

    value: int = attribute()


@dataclass
class WhiteSpace(AnnotationBase):
    """
    Model representation of a schema xs:whiteSpace element.

    :param value: (collapse | preserve | replace)
    """

    value: str = attribute()


@dataclass
class ExplicitTimezone(AnnotationBase):
    """
    Model representation of a schema xs:explicitTimezone element.

    :param value: NCName
    :param fixed: default false
    """

    value: str = attribute()
    fixed: bool = attribute(default=False)


@dataclass
class Restriction(AnnotationBase):
    """
    Model representation of a schema xs:restriction element.

    :param base: QName
    :param group:
    :param all:
    :param choice:
    :param sequence:
    :param open_content:
    :param attributes:
    :param attribute_groups:
    :param enumerations:
    :param asserts:
    :param assertions:
    :param any_element:
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
    :param patterns:
    :param explicit_timezone:
    :param simple_type:
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
    def real_type(self) -> str:
        if self.simple_type:
            return self.simple_type.real_type
        if self.enumerations:
            return ""
        if self.base:
            return self.base

        return ""

    @property
    def real_name(self) -> str:
        return "value"

    @property
    def extensions(self) -> Iterator[str]:
        if self.base:
            yield self.base

    def get_restrictions(self) -> Dict[str, Anything]:
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
                [pattern.value for pattern in self.patterns]
            )

        if self.base and self.base in self.token_types:
            restrictions["tokens"] = True

        return restrictions


@dataclass
class SimpleContent(AnnotationBase):
    """
    Model representation of a schema xs:simpleContent element.

    :param restriction:
    :param extension:
    """

    restriction: Optional[Restriction] = element()
    extension: Optional[Extension] = element()


@dataclass
class ComplexContent(SimpleContent):
    """
    Model representation of a schema xs:complexContent element.

    :param fixed:
    """

    mixed: bool = attribute(default=False)


@dataclass
class ComplexType(AnnotationBase):
    """
    Model representation of a schema xs:complexType element.

    :param name: NCName
    :param block: (#all | List of (extension | restriction))
    :param final: (#all | List of (extension | restriction))
    :param simple_content:
    :param complex_content:
    :param group:
    :param all:
    :param choice:
    :param sequence:
    :param any_attribute:
    :param open_content:
    :param attributes:
    :param attribute_groups:
    :param assertion:
    :param abstract:
    :param mixed:
    :param default_attributes_apply:
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
    Model representation of a schema xs:field element.

    :param xpath: a subset of XPath expression
    """

    xpath: Optional[str] = attribute()


@dataclass
class Selector(Field):
    """Schema Model representation of a schema xs:selectorModel element.."""


@dataclass
class Unique(AnnotationBase):
    """
    Model representation of a schema xs:unique element.

    :param name: NCName
    :param ref: QName
    :param selector:
    :param fields:
    """

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Field] = array_element(name="field")


@dataclass
class Key(AnnotationBase):
    """
    Model representation of a schema xs:key element.

    :param name: NCName
    :param ref: QName
    :param selector:
    :param fields:
    """

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Keyref(AnnotationBase):
    """
    Model representation of a schema xs:keyref element.

    :param name: NCName
    :param ref: QName
    :param refer: QName
    :param selector:
    :param fields:
    """

    name: Optional[str] = attribute()
    ref: Optional[str] = attribute()
    refer: Optional[str] = attribute()
    selector: Optional[Selector] = element()
    fields: Array[Selector] = array_element(name="field")


@dataclass
class Alternative(AnnotationBase):
    """
    Model representation of a schema xs:alternative element.

    :param type: QName
    :param test: an XPath expression
    :param simple_type:
    :param complex_type:
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
    Model representation of a schema xs:element element.

    :param name: NCName
    :param ref: QName
    :param type: QName
    :param substitution_group: List of QName
    :param default:
    :param fixed:
    :param form: qualified | unqualified
    :param block: (#all | List of (extension | restriction | substitution))
    :param final: (#all | List of (extension | restriction))
    :param target_namespace: anyURI
    :param simple_type:
    :param complex_type:
    :param alternatives:
    :param uniques:
    :param keys:
    :param keyrefs:
    :param min_occurs: nonNegativeInteger : 1
    :param max_occurs: (nonNegativeInteger | unbounded)  : 1
    :param nillable:
    :param abstract:
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
    def default_type(self) -> str:
        return self.data_type_ref(DataType.ANY_TYPE)

    @property
    def raw_type(self) -> Optional[str]:
        if self.type:
            return self.type

        if self.has_children:
            return None

        return self.data_type_ref(DataType.ANY_TYPE)

    @property
    def real_type(self) -> str:

        types = {
            alternative.type for alternative in self.alternatives if alternative.type
        }
        if self.type:
            types.add(self.type)
        elif self.ref:
            types.add(self.ref)
        elif self.simple_type and self.simple_type.real_type:
            types.add(self.simple_type.real_type)

        return " ".join(sorted(types))

    @property
    def substitutions(self) -> Array[str]:
        return self.substitution_group.split() if self.substitution_group else []

    def get_restrictions(self) -> Dict[str, Anything]:
        max_occurs = sys.maxsize if self.max_occurs == "unbounded" else self.max_occurs

        restrictions = {
            "min_occurs": self.min_occurs,
            "max_occurs": max_occurs,
        }

        if self.simple_type:
            restrictions.update(self.simple_type.get_restrictions())

        if self.nillable:
            restrictions.update(nillable=True)

        if self.type and self.type in self.token_types:
            restrictions["tokens"] = True

        return restrictions


@dataclass
class Notation(AnnotationBase):
    """
    Model representation of a schema xs:notation element.

    :param name: NCName
    :param public: token
    :param system: anyURI
    """

    name: Optional[str] = attribute()
    public: Optional[str] = attribute()
    system: Optional[str] = attribute()


@dataclass
class SchemaLocation(AnnotationBase):
    """
    Model representation of a schema xs:schemaLocation element. Base schema
    location.

    :param location: any url with a urllib supported scheme file: http:
    """

    location: Optional[str] = field(default=None)


@dataclass
class Import(SchemaLocation):
    """
    Model representation of a schema xs:import element.

    :param namespace: anyURI
    :param schema_location: anyURI
    """

    namespace: Optional[str] = attribute()
    schema_location: Optional[str] = attribute(name="schemaLocation")


@dataclass
class Include(SchemaLocation):
    """
    Model representation of a schema xs:include element.

    :param schema_location: anyURI
    """

    schema_location: Optional[str] = attribute(name="schemaLocation")


@dataclass
class Redefine(SchemaLocation):
    """
    Model representation of a schema xs:redefine element.

    :param schema_location: anyURI
    :param simple_types:
    :param complex_types:
    :param groups:
    :param attribute_groups:
    """

    schema_location: Optional[str] = attribute(name="schemaLocation")
    simple_types: Array[SimpleType] = array_element(name="simpleType")
    complex_types: Array[ComplexType] = array_element(name="complexType")
    groups: Array[Group] = array_element(name="group")
    attribute_groups: Array[AttributeGroup] = array_element(name="attributeGroup")


@dataclass
class Override(SchemaLocation):
    """
    Model representation of a schema xs:override element.

    :param schema_location: anyURI
    :param simple_types:
    :param complex_types:
    :param groups:
    :param attribute_groups:
    :param elements:
    :param attributes:
    :param notations:
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
class Schema(SchemaLocation, ModuleMixin):
    """
    Model representation of a schema xs:schema element.

    :param target:
    :param block_default: (#all | List of (extension | restriction | substitution))
    :param default_attributes: QName
    :param final_default: (#all | List of extension | restriction | list | union) : ''
    :param target_namespace: anyURI
    :param version: token
    :param xmlns:
    :param element_form_default: (qualified | unqualified) : unqualified
    :param attribute_form_default:  (qualified | unqualified) : unqualified
    :param default_open_content:
    :param imports:
    :param redefines:
    :param overrides:
    :param annotations:
    :param simple_types:
    :param complex_types:
    :param groups:
    :param attribute_groups:
    :param elements:
    :param attributes:
    :param notations:
    """

    class Meta:
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
        yield from self.imports

        yield from self.includes

        yield from self.redefines

        yield from self.overrides
