import sys
from unittest import TestCase

import pytest

from xsdata.models.elements import (
    Attribute,
    Choice,
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    MinLength,
    Pattern,
    Restriction,
    Sequence,
    SimpleContent,
    SimpleType,
)
from xsdata.models.enums import FormType
from xsdata.parser import SchemaParser


def wrap(str, element_form="qualified", attribute_form="unqualified"):
    return f"""<?xml version="1.0" encoding="utf-8"?>
    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
        elementFormDefault="{element_form}"
        attributeFormDefault="{attribute_form}">
        {str}
</xs:schema>"""


class ParserTests(TestCase):
    def test_with_unknown_tags_raise_exception(self):
        xsd = "<xs:assert />"
        with self.assertRaises(NotImplementedError) as cm:
            SchemaParser.from_string(wrap(xsd))

        self.assertEqual(
            "Unsupported tag `{http://www.w3.org/2001/XMLSchema}assert`",
            str(cm.exception),
        )

    def test_with_empty_tags_are_ignored(self):
        xsd = """<xs:complexType name="foo" />
        <xs:element />
        """

        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(0, len(schema.elements))
        self.assertEqual(1, len(schema.complex_types))

    @pytest.mark.parametrize
    def test_complex_type_with_sequence(self):
        xsd = """<xs:complexType name="allowablePointsOfSaleType">
        <xs:sequence maxOccurs="unbounded">
            <xs:element name="PointOfSale">
                <xs:complexType>
                    <xs:attribute name="id" type="xs:string"/>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>"""

        expected = ComplexType.build(
            name="allowablePointsOfSaleType",
            sequence=Sequence.build(
                max_occurs=sys.maxsize,
                elements=[
                    Element.build(
                        name="PointOfSale",
                        form=FormType.QUALIFIED,
                        complex_type=ComplexType.build(
                            attributes=[
                                Attribute.build(
                                    name="id",
                                    type="xs:string",
                                    form=FormType.UNQUALIFIED,
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_simple_content_and_extension(self):
        xsd = """<xs:complexType name="priceCurrencyType">
        <xs:simpleContent>
            <xs:extension base="priceType">
                <xs:attribute name="currency" use="required">
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:pattern value="[A-Z][A-Z][A-Z]"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>"""

        expected = ComplexType.build(
            name="priceCurrencyType",
            simple_content=SimpleContent.build(
                extension=Extension.build(
                    base="priceType",
                    attributes=[
                        Attribute.build(
                            name="currency",
                            use="required",
                            form=FormType.UNQUALIFIED,
                            simple_type=SimpleType.build(
                                restriction=Restriction.build(
                                    base="xs:string",
                                    pattern=Pattern.build(
                                        value="[A-Z][A-Z][A-Z]"
                                    ),
                                )
                            ),
                        )
                    ],
                )
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_complex_content(self):
        xsd = """<xs:complexType name="UserRateConditionType">
                  <xs:complexContent>
                      <xs:extension base="UserRateConditionBaseType">
                          <xs:attribute name="id" use="required" form="qualified">
                              <xs:simpleType>
                                  <xs:restriction base='xs:string'>
                                      <xs:minLength value="1"/>
                                  </xs:restriction>
                              </xs:simpleType>
                          </xs:attribute>
                      </xs:extension>
                  </xs:complexContent>
                </xs:complexType>"""

        expected = ComplexType.build(
            name="UserRateConditionType",
            complex_content=ComplexContent.build(
                extension=Extension.build(
                    base="UserRateConditionBaseType",
                    attributes=[
                        Attribute.build(
                            name="id",
                            use="required",
                            form=FormType.QUALIFIED,
                            simple_type=SimpleType.build(
                                restriction=Restriction.build(
                                    base="xs:string",
                                    min_length=MinLength.build(value=1),
                                )
                            ),
                        )
                    ],
                )
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_choice_resets_elements_min_occurs(self):
        xsd = """<xs:complexType>
                <xs:choice minOccurs="1">
                    <xs:element name="first" minOccurs="1" />
                    <xs:element name="second" minOccurs="1" />
                </xs:choice>
            </xs:complexType>"""

        expected = ComplexType.build(
            choice=Choice.build(
                min_occurs=1,
                elements=[
                    Element.build(
                        name="first", min_occurs=0, form=FormType.QUALIFIED
                    ),
                    Element.build(
                        name="second", min_occurs=0, form=FormType.QUALIFIED
                    ),
                ],
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])
