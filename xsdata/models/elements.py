import re
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as ArrayList
from typing import Optional
from typing import Union as UnionType

from xsdata.models.enums import FormType
from xsdata.models.enums import ProcessType
from xsdata.models.enums import UseType
from xsdata.models.mixins import ElementBase
from xsdata.models.mixins import NamedField
from xsdata.models.mixins import OccurrencesMixin
from xsdata.models.mixins import RestrictedField


@dataclass
class Documentation(ElementBase):
    """
    The documentation element is used to enter text comments in a schema.

    Reference: https://www.w3schools.com/xml/el_documentation.asp.
    """

    lang: Optional[str] = None
    source: Optional[str] = None
    text: Optional[str] = None


@dataclass
class Appinfo(ElementBase):
    """
    The appinfo element specifies information to be used by the application.

    Reference: https://www.w3schools.com/xml/el_appinfo.asp.
    """

    source: Optional[str] = None
    text: Optional[str] = None


@dataclass
class Annotation(ElementBase):
    """
    The annotation element is a top level element that specifies schema
    comments.

    Reference: https://www.w3schools.com/xml/el_annotation.asp.
    """

    appinfo: Optional[Appinfo] = None
    documentations: ArrayList[Documentation] = field(default_factory=list)


@dataclass
class AnnotationBase(ElementBase):
    """Base Class for elements that can contain annotations."""

    annotation: Optional[Annotation] = None

    @property
    def display_help(self) -> Optional[str]:
        if self.annotation and len(self.annotation.documentations):
            return "\n".join(
                [
                    re.sub(r"[\s+]", " ", doc.text)
                    for doc in self.annotation.documentations
                    if doc.text
                ]
            ).strip()
        return None


@dataclass
class SimpleType(AnnotationBase, NamedField, RestrictedField):
    """
    The simpleType element defines a simple type and specifies the constraints
    and information about the values of attributes or text-only elements.

    XSD Element reference : Reference: https://www.w3schools.com/xml/el_simpletype.asp.
    """

    name: Optional[str] = None
    restriction: Optional["Restriction"] = None
    list: Optional["List"] = None
    union: Optional["Union"] = None

    @property
    def is_enumeration(self):
        return self.restriction and len(self.restriction.enumerations) > 0

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
    The list element defines a simple type element as a list of values of a
    specified data type.

    Reference: https://www.w3schools.com/xml/el_list.asp.
    """

    simple_type: Optional[SimpleType] = None
    item_type: Optional[str] = None

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
    The union element defines a simple type as a collection (union) of values
    from specified simple data types.

    Reference: https://www.w3schools.com/xml/el_union.asp.
    """

    member_types: Optional[str] = None
    simple_types: ArrayList[SimpleType] = field(default_factory=list)

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
class AnyAttribute(AnnotationBase):
    """
    The anyAttribute element enables the author to extend the XML document with
    attributes not specified by the schema.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_anyattribute.asp.
    """

    namespace: Optional[str] = None
    process_contents: Optional[ProcessType] = None
    simple_type: Optional[SimpleType] = None


@dataclass
class Attribute(AnnotationBase, NamedField, RestrictedField):
    """
    The attribute element defines an attribute.

    Reference: https://www.w3schools.com/xml/el_attribute.asp.
    """

    default: Optional[str] = None
    fixed: Optional[str] = None
    form: Optional[FormType] = None
    name: Optional[str] = None
    ref: Optional[str] = None
    type: Optional[str] = None
    simple_type: Optional[SimpleType] = None
    use: Optional[UseType] = field(default=UseType.OPTIONAL)

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
    The attributeGroup element is used to group a set of attribute declarations
    so that they can be incorporated as a group into complex type definitions.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_attributegroup.asp.
    """

    name: Optional[str] = None
    ref: Optional[str] = None
    any_attribute: Optional[AnyAttribute] = None
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList["AttributeGroup"] = field(default_factory=list)

    @property
    def extends(self) -> Optional[str]:
        return self.ref


@dataclass
class All(AnnotationBase, OccurrencesMixin):
    """
    The all element specifies that the child elements can appear in any order
    and that each child element can occur zero or one time.

    Reference: https://www.w3schools.com/xml/el_all.asp.
    """

    elements: ArrayList["Element"] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Sequence(AnnotationBase, OccurrencesMixin):
    """
    The sequence element specifies that the child elements must appear in a
    sequence. Each child element can occur from 0 to any number of times.

    Reference: https://www.w3schools.com/xml/el_sequence.asp.
    """

    elements: ArrayList["Element"] = field(default_factory=list)
    groups: ArrayList["Group"] = field(default_factory=list)
    choices: ArrayList["Choice"] = field(default_factory=list)
    sequences: ArrayList["Sequence"] = field(default_factory=list)
    anys: ArrayList["Any"] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Choice(AnnotationBase, OccurrencesMixin):
    """
    XML Schema choice element allows only one of the elements contained in the.

    <choice> declaration to be present within the containing element.

    Reference: https://www.w3schools.com/xml/el_choice.asp.
    """

    elements: ArrayList["Element"] = field(default_factory=list)
    groups: ArrayList["Group"] = field(default_factory=list)
    choices: ArrayList["Choice"] = field(default_factory=list)
    sequences: ArrayList[Sequence] = field(default_factory=list)
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Group(AnnotationBase, OccurrencesMixin, NamedField):
    """
    The group element is used to define a group of elements to be used in
    complex type definitions.

    Reference: https://www.w3schools.com/xml/el_group.asp.
    """

    name: Optional[str] = None
    ref: Optional[str] = None
    all: Optional[All] = None
    choice: Optional[Choice] = None
    sequence: Optional[Sequence] = None
    max_occurs: int = 1
    min_occurs: int = 1

    @property
    def extends(self) -> Optional[str]:
        return self.ref


@dataclass
class Extension(AnnotationBase):
    """
    The extension element extends an existing simpleType or complexType
    element.

    Reference: https://www.w3schools.com/xml/el_extension.asp.
    """

    base: Optional[str] = None
    group: Optional[Group] = None
    all: Optional[All] = None
    choice: Optional[Choice] = None
    sequence: Optional[Sequence] = None
    any_attribute: Optional[AnyAttribute] = None
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)

    @property
    def extends(self) -> Optional[str]:
        return self.base


@dataclass
class Enumeration(AnnotationBase, NamedField, RestrictedField):
    """
    Defines a list of acceptable values.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[str] = None

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
    Specifies the maximum number of decimal places allowed. Must be equal to or
    greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = None


@dataclass
class Length(AnnotationBase):
    """
    Specifies the exact number of characters or list items allowed. Must be
    equal to or greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = None


@dataclass
class MaxExclusive(AnnotationBase):
    """
    Specifies the upper bounds for numeric values (the value must be less than
    this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class MaxInclusive(AnnotationBase):
    """
    Specifies the upper bounds for numeric values (the value must be less than
    or equal to this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class MaxLength(AnnotationBase):
    """
    Specifies the maximum number of characters or list items allowed. Must be
    equal to or greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class MinExclusive(AnnotationBase):
    """
    Schema Facet: Reference:

    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class MinInclusive(AnnotationBase):
    """
    Specifies the lower bounds for numeric values (the value must be greater
    than this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class MinLength(AnnotationBase):
    """
    Specifies the lower bounds for numeric values (the value must be greater
    than or equal to this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = None


@dataclass
class Pattern(AnnotationBase):
    """
    Defines the exact sequence of characters that are acceptable.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[str] = None


@dataclass
class TotalDigits(AnnotationBase):
    """
    Specifies the exact number of digits allowed. Must be greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = None


@dataclass
class WhiteSpace(AnnotationBase):
    """
    Specifies how white space (line feeds, tabs, spaces, and carriage returns)
    is handled.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[str] = None  # preserve, collapse, replace


@dataclass
class Assertion(AnnotationBase):
    test: Optional[str] = None


@dataclass
class Restriction(RestrictedField, AnnotationBase, NamedField):
    """
    The restriction element defines restrictions on a simpleType,
    simpleContent, or complexContent definition.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_restriction.asp.
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

    base: Optional[str] = None
    group: Optional[Group] = None
    all: Optional[All] = None
    choice: Optional[Choice] = None
    sequence: Optional[Sequence] = None
    any_attribute: Optional[AnyAttribute] = None
    min_exclusive: Optional[MinExclusive] = None
    min_inclusive: Optional[MinInclusive] = None
    min_length: Optional[MinLength] = None
    max_exclusive: Optional[MaxExclusive] = None
    max_inclusive: Optional[MaxInclusive] = None
    max_length: Optional[MaxLength] = None
    total_digits: Optional[TotalDigits] = None
    fraction_digits: Optional[FractionDigits] = None
    length: Optional[Length] = None
    white_space: Optional[WhiteSpace] = None
    pattern: Optional[Pattern] = None
    simple_type: Optional[SimpleType] = None
    enumerations: ArrayList[Enumeration] = field(default_factory=list)
    assertions: ArrayList[Assertion] = field(default_factory=list)
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)

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
    The simpleContent element contains extensions or restrictions on a text-
    only complex type or on a simple type as content and contains no elements.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_simplecontent.asp.
    """

    restriction: Optional[Restriction] = None
    extension: Optional[Extension] = None


@dataclass
class ComplexContent(SimpleContent):
    """
    The complexContent element defines extensions or restrictions on a complex
    type that contains mixed content or elements only.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_complexcontent.asp.
    """

    mixed: bool = False


@dataclass
class ComplexType(AnnotationBase, NamedField):
    """
    The complexType element defines a complex type. A complex type element is
    an XML element that contains other elements and/or attributes.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_complextype.asp.
    """

    name: Optional[str] = None
    block: Optional[str] = None
    final: Optional[str] = None
    simple_content: Optional[SimpleContent] = None
    complex_content: Optional[ComplexContent] = None
    group: Optional[Group] = None
    all: Optional[All] = None
    choice: Optional[Choice] = None
    sequence: Optional[Sequence] = None
    any_attribute: Optional[AnyAttribute] = None
    attributes: ArrayList[Attribute] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)
    abstract: bool = False
    mixed: bool = False


@dataclass
class Field(AnnotationBase):
    """Reference: https://www.w3schools.com/xml/el_field.asp."""

    xpath: Optional[str] = None


@dataclass
class Selector(Field):
    """
    The field element specifies an XPath expression that specifies the value
    used to define an identity constraint.

    Reference: https://www.w3schools.com/xml/el_selector.asp.
    """


@dataclass
class Unique(AnnotationBase):
    """
    The unique element defines that an element or an attribute value must be
    unique within the scope. The unique element MUST contain the following (in
    order):

     * one and only one selector element
     * one or more field elements

    Reference: https://www.w3schools.com/xml/el_unique.asp.
    """

    name: Optional[str] = None
    selector: Optional[Selector] = None
    field: Optional[Field] = None


@dataclass
class Key(AnnotationBase):
    """Reference: https://www.w3schools.com/xml/el_key.asp."""

    name: Optional[str] = None
    selector: Optional[Selector] = None
    fields: ArrayList[Selector] = field(default_factory=list)


@dataclass
class Keyref(AnnotationBase):
    """
    The key element specifies an attribute or element value as a key (unique,
    non-nullable, and always present) within the containing element in an
    instance document.

    The key element MUST contain the following (in order):
     * one and only one selector element
     * one or more field elements

    Reference: https://www.w3schools.com/xml/el_keyref.asp.
    """

    name: Optional[str] = None
    refer: Optional[str] = None
    selector: Optional[Selector] = None
    fields: ArrayList[Selector] = field(default_factory=list)


@dataclass
class Element(AnnotationBase, NamedField, OccurrencesMixin):
    """
    The element element defines an element.

    Reference: https://www.w3schools.com/xml/el_element.asp.
    """

    name: Optional[str] = None
    id: Optional[str] = None
    ref: Optional[str] = None
    type: Optional[str] = None
    substitution_group: Optional[str] = None
    default: Optional[str] = None
    fixed: Optional[str] = None
    form: Optional[FormType] = None
    block: Optional[List] = None
    final: Optional[List] = None
    simple_type: Optional[SimpleType] = None
    complex_type: Optional[ComplexType] = None
    uniques: ArrayList[Unique] = field(default_factory=list)
    keys: ArrayList[Key] = field(default_factory=list)
    keyrefs: ArrayList[Keyref] = field(default_factory=list)
    min_occurs: Optional[int] = None
    max_occurs: Optional[int] = None
    nillable: bool = False
    abstract: bool = False

    @property
    def is_attribute(self) -> bool:
        return True

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
class Any(AnnotationBase, OccurrencesMixin):
    """
    The any element enables the author to extend the XML document with elements
    not specified by the schema.

    Reference: https://www.w3schools.com/xml/el_any.asp.
    """

    namespace: Optional[str] = None
    process_contents: Optional[ProcessType] = None
    annotation: Optional[Annotation] = None
    max_occurs: int = 1
    min_occurs: int = 1


@dataclass
class Import(AnnotationBase):
    """
    The import element is used to add multiple schemas with different target
    namespace to a document.

    Reference: https://www.w3schools.com/xml/el_import.asp.
    """

    namespace: Optional[str] = None
    schema_location: Optional[str] = None


@dataclass
class Include(AnnotationBase):
    """
    The include element is used to add multiple schemas with the same target
    namespace to a document.

    Reference: https://www.w3schools.com/xml/el_include.asp.
    """

    schema_location: Optional[str] = None

    @property
    def namespace(self):
        return None


@dataclass
class Notation(AnnotationBase):
    """
    The notation element describes the format of non-XML data within an XML
    document.

    Reference: https://www.w3schools.com/xml/el_notation.asp.
    """

    name: Optional[str] = None
    public: Optional[str] = None
    system: Optional[str] = None


@dataclass
class Redefine(AnnotationBase):
    """
    The redefine element redefines simple and complex types, groups, and
    attribute groups from an external schema.

    Reference: https://www.w3schools.com/xml/el_redefine.asp.
    """

    schema_location: Optional[str] = None
    simple_type: Optional[SimpleType] = None
    complex_type: Optional[ComplexType] = None
    group: Optional[Group] = None
    attribute_group: Optional[AttributeGroup] = None


@dataclass
class Schema(AnnotationBase):
    """
    The schema element defines the root element of a schema.

    Reference: https://www.w3schools.com/xml/el_schema.asp.
    """

    target: Optional[str] = None
    block_default: Optional[str] = None
    final_default: Optional[str] = None
    target_namespace: Optional[str] = None
    version: Optional[str] = None
    xmlns: Optional[str] = None
    nsmap: Dict = field(default_factory=dict)
    location: Optional[Path] = field(default=None)
    element_form_default: FormType = field(default=FormType.UNQUALIFIED)
    attribute_form_default: FormType = field(default=FormType.UNQUALIFIED)
    includes: ArrayList[Include] = field(default_factory=list)
    imports: ArrayList[Import] = field(default_factory=list)
    redefines: ArrayList[Redefine] = field(default_factory=list)
    annotations: ArrayList[Annotation] = field(default_factory=list)
    simple_types: ArrayList[SimpleType] = field(default_factory=list)
    complex_types: ArrayList[ComplexType] = field(default_factory=list)
    groups: ArrayList[Group] = field(default_factory=list)
    attribute_groups: ArrayList[AttributeGroup] = field(default_factory=list)
    elements: ArrayList[Element] = field(default_factory=list)
    attributes: ArrayList[Attribute] = field(default_factory=list)
    notations: ArrayList[Notation] = field(default_factory=list)

    def sub_schemas(self) -> Iterator[UnionType[Import, Include]]:
        for imp in self.imports:
            yield imp

        for inc in self.includes:
            yield inc

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
