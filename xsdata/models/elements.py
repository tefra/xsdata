from dataclasses import dataclass
from dataclasses import field
from dataclasses import MISSING
from pathlib import Path
from typing import Any as Anything
from typing import Dict
from typing import Iterator
from typing import List as ArrayList
from typing import Optional
from typing import Set
from typing import Union as UnionType

from lxml import etree

from xsdata.formats.dataclass.serializers import XmlSerializer
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
    The documentation element is used to enter text comments in a schema.

    Reference: https://www.w3schools.com/xml/el_documentation.asp.
    """

    class Meta:
        mixed = True

    lang: Optional[str] = attribute(default=None)
    source: Optional[str] = attribute(default=None)
    elements: ArrayList[object] = any_element(default_factory=list)

    def tostring(self) -> Optional[str]:
        if not self.elements:
            return None

        root = etree.Element("xsdata")
        namespaces: Set[str] = set()
        XmlSerializer.set_any_children(root, self.elements, namespaces)
        nsmap = {f"ns{index}": ns for index, ns in enumerate(sorted(namespaces))}
        etree.cleanup_namespaces(root, top_nsmap=nsmap)
        xml = etree.tostring(root, pretty_print=True).decode()
        return xml[xml.find(">") + 1 :].replace("</xsdata>", "").strip()


@dataclass
class Appinfo(ElementBase):
    """
    The appinfo element specifies information to be used by the application.

    Reference: https://www.w3schools.com/xml/el_appinfo.asp.
    """

    class Meta:
        mixed = True

    source: Optional[str] = attribute(default=None)
    elements: ArrayList[object] = any_element(default_factory=list)


@dataclass
class Annotation(ElementBase):
    """
    The annotation element is a top level element that specifies schema
    comments.

    Reference: https://www.w3schools.com/xml/el_annotation.asp.
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
class SimpleType(AnnotationBase, NamedField, RestrictedField):
    """
    The simpleType element defines a simple type and specifies the constraints
    and information about the values of attributes or text-only elements.

    XSD Element reference : Reference: https://www.w3schools.com/xml/el_simpletype.asp.
    """

    name: Optional[str] = attribute(default=None)
    restriction: Optional["Restriction"] = element(default=None)
    list: Optional["List"] = element(default=None)
    union: Optional["Union"] = element(default=None)

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
    The union element defines a simple type as a collection (union) of values
    from specified simple data types.

    Reference: https://www.w3schools.com/xml/el_union.asp.
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
    The anyAttribute element enables the author to extend the XML document with
    attributes not specified by the schema.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_anyattribute.asp.
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
    The attribute element defines an attribute.

    Reference: https://www.w3schools.com/xml/el_attribute.asp.
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
    The attributeGroup element is used to group a set of attribute declarations
    so that they can be incorporated as a group into complex type definitions.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_attributegroup.asp.
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


@dataclass
class All(AnnotationBase, OccurrencesMixin):
    """
    The all element specifies that the child elements can appear in any order
    and that each child element can occur zero or one time.

    Reference: https://www.w3schools.com/xml/el_all.asp.
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    elements: ArrayList["Element"] = element(default_factory=list, name="element")


@dataclass
class Sequence(AnnotationBase, OccurrencesMixin):
    """
    The sequence element specifies that the child elements must appear in a
    sequence. Each child element can occur from 0 to any number of times.

    Reference: https://www.w3schools.com/xml/el_sequence.asp.
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
    XML Schema choice element allows only one of the elements contained in the.

    <choice> declaration to be present within the containing element.

    Reference: https://www.w3schools.com/xml/el_choice.asp.
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
    elements: ArrayList["Element"] = element(default_factory=list, name="element")
    groups: ArrayList["Group"] = element(default_factory=list, name="group")
    choices: ArrayList["Choice"] = element(default_factory=list, name="choice")
    sequences: ArrayList[Sequence] = element(default_factory=list, name="sequence")


@dataclass
class Group(AnnotationBase, OccurrencesMixin, NamedField):
    """
    The group element is used to define a group of elements to be used in
    complex type definitions.

    Reference: https://www.w3schools.com/xml/el_group.asp.
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
    The extension element extends an existing simpleType or complexType
    element.

    Reference: https://www.w3schools.com/xml/el_extension.asp.
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
    Specifies the maximum number of decimal places allowed. Must be equal to or
    greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = attribute(default=None)


@dataclass
class Length(AnnotationBase):
    """
    Specifies the exact number of characters or list items allowed. Must be
    equal to or greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = attribute(default=None)


@dataclass
class MaxExclusive(AnnotationBase):
    """
    Specifies the upper bounds for numeric values (the value must be less than
    this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class MaxInclusive(AnnotationBase):
    """
    Specifies the upper bounds for numeric values (the value must be less than
    or equal to this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class MaxLength(AnnotationBase):
    """
    Specifies the maximum number of characters or list items allowed. Must be
    equal to or greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class MinExclusive(AnnotationBase):
    """
    Schema Facet: Reference:

    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class MinInclusive(AnnotationBase):
    """
    Specifies the lower bounds for numeric values (the value must be greater
    than this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class MinLength(AnnotationBase):
    """
    Specifies the lower bounds for numeric values (the value must be greater
    than or equal to this value)

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[float] = attribute(default=None)


@dataclass
class Pattern(AnnotationBase):
    """
    Defines the exact sequence of characters that are acceptable.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[str] = attribute(default=None)


@dataclass
class TotalDigits(AnnotationBase):
    """
    Specifies the exact number of digits allowed. Must be greater than zero.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[int] = attribute(default=None)


@dataclass
class WhiteSpace(AnnotationBase):
    """
    Specifies how white space (line feeds, tabs, spaces, and carriage returns)
    is handled.

    Schema Facet: Reference:
    https://www.w3schools.com/xml/schema_facets.asp.
    """

    value: Optional[str] = attribute(default=None)  # preserve, collapse, replace


@dataclass
class Assertion(AnnotationBase):
    test: Optional[str] = attribute(default=None)


@dataclass
class ExplicitTimezone(AnnotationBase):
    value: Optional[UseType] = attribute(default=None)
    fixed: Optional[str] = attribute(default=None)


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
    The simpleContent element contains extensions or restrictions on a text-
    only complex type or on a simple type as content and contains no elements.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_simplecontent.asp.
    """

    restriction: Optional[Restriction] = element(default=None)
    extension: Optional[Extension] = element(default=None)


@dataclass
class ComplexContent(SimpleContent):
    """
    The complexContent element defines extensions or restrictions on a complex
    type that contains mixed content or elements only.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_complexcontent.asp.
    """

    mixed: bool = attribute(default=False)


@dataclass
class ComplexType(AnnotationBase, NamedField):
    """
    The complexType element defines a complex type. A complex type element is
    an XML element that contains other elements and/or attributes.

     XSD Element reference
    : Reference: https://www.w3schools.com/xml/el_complextype.asp.
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
    """Reference: https://www.w3schools.com/xml/el_field.asp."""

    xpath: Optional[str] = attribute(default=None)


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

    name: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    field: Optional[Field] = element(default=None)


@dataclass
class Key(AnnotationBase):
    """Reference: https://www.w3schools.com/xml/el_key.asp."""

    name: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    fields: ArrayList[Selector] = element(default_factory=list, name="field")


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

    name: Optional[str] = attribute(default=None)
    refer: Optional[str] = attribute(default=None)
    selector: Optional[Selector] = element(default=None)
    fields: ArrayList[Selector] = element(default_factory=list, name="field")


@dataclass
class Element(AnnotationBase, NamedField, OccurrencesMixin):
    """
    The element element defines an element.

    Reference: https://www.w3schools.com/xml/el_element.asp.
    """

    name: Optional[str] = attribute(default=None)
    id: Optional[str] = attribute(default=None)
    ref: Optional[str] = attribute(default=None)
    type: Optional[str] = attribute(default=None)
    substitution_group: Optional[str] = attribute(default=None)
    default: Optional[str] = attribute(default=None)
    fixed: Optional[str] = attribute(default=None)
    form: Optional[FormType] = attribute(default=None)
    block: Optional[List] = attribute(default=None)
    final: Optional[List] = attribute(default=None)
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
class Any(AnnotationBase, OccurrencesMixin, NamedField):
    """
    The any element enables the author to extend the XML document with elements
    not specified by the schema.

    Reference: https://www.w3schools.com/xml/el_any.asp.
    """

    min_occurs: int = attribute(default=1)
    max_occurs: int = attribute(default=1)
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
class Import(AnnotationBase):
    """
    The import element is used to add multiple schemas with different target
    namespace to a document.

    Reference: https://www.w3schools.com/xml/el_import.asp.
    """

    namespace: Optional[str] = attribute(default=None)
    schema_location: Optional[str] = attribute(default=None)


@dataclass
class Include(AnnotationBase):
    """
    The include element is used to add multiple schemas with the same target
    namespace to a document.

    Reference: https://www.w3schools.com/xml/el_include.asp.
    """

    schema_location: Optional[str] = attribute(default=None)

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

    name: Optional[str] = attribute(default=None)
    public: Optional[str] = attribute(default=None)
    system: Optional[str] = attribute(default=None)


@dataclass
class Redefine(AnnotationBase):
    """
    The redefine element redefines simple and complex types, groups, and
    attribute groups from an external schema.

    Reference: https://www.w3schools.com/xml/el_redefine.asp.
    """

    schema_location: Optional[str] = attribute(default=None)
    simple_type: Optional[SimpleType] = element(default=None)
    complex_type: Optional[ComplexType] = element(default=None)
    group: Optional[Group] = element(default=None)
    attribute_group: Optional[AttributeGroup] = element(default=None)


@dataclass
class Schema(AnnotationBase):
    """
    The schema element defines the root element of a schema.

    Reference: https://www.w3schools.com/xml/el_schema.asp.
    """

    class Meta:
        namespace = Namespace.SCHEMA

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
