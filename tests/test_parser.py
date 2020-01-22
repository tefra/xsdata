import sys
from unittest import TestCase

from xsdata.models.elements import (
    All,
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
from xsdata.models.enums import FormType, UseType
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

    def test_schema_nsmap_with_target_and_default_namespace(self):
        xsd = """<?xml version="1.0" encoding="utf-8"?>
                <xs:schema xmlns="http://www/default"
                targetNamespace="http://www/target"
                xmlns:xs="http://www.w3.org/2001/XMLSchema" />"""

        schema = SchemaParser.from_string(xsd, target_namespace="parent")
        self.assertEqual(
            {
                None: "http://www/default",
                "xs": "http://www.w3.org/2001/XMLSchema",
            },
            schema.nsmap,
        )
        self.assertEqual("http://www/target", schema.target_namespace)

    def test_schema_nsmap_without_target_namespace(self):
        xsd = """<?xml version="1.0" encoding="utf-8"?>
                <xs:schema xmlns="http://www/default"
                xmlns:xs="http://www.w3.org/2001/XMLSchema" />"""

        schema = SchemaParser.from_string(xsd, target_namespace="parent")
        self.assertEqual(
            {
                None: "http://www/default",
                "xs": "http://www.w3.org/2001/XMLSchema",
            },
            schema.nsmap,
        )
        self.assertEqual("parent", schema.target_namespace)

    def test_top_level_elements_and_attributes_are_qualified(self):
        xsd = """<xs:element name="a" /><xs:attribute name="b" />"""

        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(FormType.QUALIFIED, schema.attributes[0].form)
        self.assertEqual(FormType.QUALIFIED, schema.elements[0].form)

    def test_with_empty_tags_are_ignored(self):
        xsd = """<xs:complexType name="foo" />
        <xs:element />
        """

        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(0, len(schema.elements))
        self.assertEqual(1, len(schema.complex_types))

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

        expected = ComplexType.create(
            index=1,
            name="allowablePointsOfSaleType",
            sequence=Sequence.create(
                index=2,
                max_occurs=sys.maxsize,
                elements=[
                    Element.create(
                        index=3,
                        name="PointOfSale",
                        form=FormType.QUALIFIED,
                        max_occurs=sys.maxsize,
                        min_occurs=1,
                        complex_type=ComplexType.create(
                            index=4,
                            attributes=[
                                Attribute.create(
                                    index=5,
                                    name="id",
                                    type="xs:string",
                                    form=FormType.UNQUALIFIED,
                                )
                            ],
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

        expected = ComplexType.create(
            index=1,
            name="priceCurrencyType",
            simple_content=SimpleContent.create(
                index=2,
                extension=Extension.create(
                    index=3,
                    base="priceType",
                    attributes=[
                        Attribute.create(
                            index=4,
                            name="currency",
                            use=UseType.REQUIRED,
                            form=FormType.UNQUALIFIED,
                            simple_type=SimpleType.create(
                                index=5,
                                restriction=Restriction.create(
                                    index=6,
                                    base="xs:string",
                                    pattern=Pattern.create(
                                        index=7, value="[A-Z][A-Z][A-Z]"
                                    ),
                                ),
                            ),
                        )
                    ],
                ),
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

        expected = ComplexType.create(
            index=1,
            name="UserRateConditionType",
            complex_content=ComplexContent.create(
                index=2,
                extension=Extension.create(
                    index=3,
                    base="UserRateConditionBaseType",
                    attributes=[
                        Attribute.create(
                            index=4,
                            name="id",
                            use=UseType.REQUIRED,
                            form=FormType.QUALIFIED,
                            simple_type=SimpleType.create(
                                index=5,
                                restriction=Restriction.create(
                                    index=6,
                                    base="xs:string",
                                    min_length=MinLength.create(
                                        value=1, index=7
                                    ),
                                ),
                            ),
                        )
                    ],
                ),
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

        expected = ComplexType.create(
            index=1,
            choice=Choice.create(
                index=2,
                min_occurs=1,
                elements=[
                    Element.create(
                        name="first",
                        min_occurs=0,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=3,
                    ),
                    Element.create(
                        name="second",
                        min_occurs=0,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=4,
                    ),
                ],
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_all_resets_elements_max_occurs(self):
        xsd = """<xs:complexType>
                    <xs:all minOccurs="1">
                    <xs:element name="first" maxOccurs="100" />
                    <xs:element name="second" maxOccurs="100" />
                    </xs:all>
              </xs:complexType>"""

        expected = ComplexType.create(
            index=1,
            all=All.create(
                index=2,
                min_occurs=1,
                elements=[
                    Element.create(
                        name="first",
                        min_occurs=1,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=3,
                    ),
                    Element.create(
                        name="second",
                        min_occurs=1,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=4,
                    ),
                ],
            ),
        )
        schema = SchemaParser.from_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])
