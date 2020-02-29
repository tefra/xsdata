import sys
from unittest import TestCase

from xsdata.models.elements import All
from xsdata.models.elements import Any
from xsdata.models.elements import Attribute
from xsdata.models.elements import Choice
from xsdata.models.elements import ComplexContent
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Extension
from xsdata.models.elements import MinLength
from xsdata.models.elements import Pattern
from xsdata.models.elements import Restriction
from xsdata.models.elements import Sequence
from xsdata.models.elements import SimpleContent
from xsdata.models.elements import SimpleType
from xsdata.models.enums import FormType
from xsdata.models.enums import ProcessType
from xsdata.models.enums import UseType
from xsdata.parser import SchemaParser


def wrap(string: str, **kwargs):
    attributes = {
        "elementFormDefault": "qualified",
        "attributeFormDefault": "unqualified",
    }
    attributes.update(kwargs)

    attrs = " ".join([f'{key}="{value}"' for key, value in attributes.items()])
    return f"""<?xml version="1.0" encoding="utf-8"?>
    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" {attrs}>
        {string}
</xs:schema>"""


class ParserTests(TestCase):
    def setUp(self) -> None:
        self.parser = SchemaParser()
        super(ParserTests, self).setUp()

    def test_with_mixed_content(self):
        xsd = """<xs:simpleType name="CountryType">
                    <xs:annotation>
                      <xs:documentation>
                        <keyword>country</keyword>
                      </xs:documentation>
                    </xs:annotation>
                  </xs:simpleType>"""
        schema = self.parser.from_xsd_string(wrap(xsd))

        expected = "<keyword>country</keyword>"
        self.assertEqual(expected, schema.simple_types[0].display_help)

    def test_with_unknown_tags_raise_exception(self):
        xsd = "<xs:foobar />"
        with self.assertRaises(ValueError) as cm:
            self.parser.from_xsd_string(wrap(xsd))

        msg = (
            "{http://www.w3.org/2001/XMLSchema}schema does not support "
            "mixed content: {http://www.w3.org/2001/XMLSchema}foobar"
        )
        self.assertEqual(msg, str(cm.exception))

    def test_schema_nsmap_with_target_and_default_namespace(self):
        xsd = """<?xml version="1.0" encoding="utf-8"?>
                <xs:schema xmlns="http://www/default"
                targetNamespace="http://www/target"
                xmlns:xs="http://www.w3.org/2001/XMLSchema" />"""

        schema = self.parser.from_xsd_string(xsd)
        expected = {
            None: "http://www/default",
            "xlink": "http://www.w3.org/1999/xlink",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "xs": "http://www.w3.org/2001/XMLSchema",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }

        self.assertEqual(expected, schema.nsmap)
        self.assertEqual("http://www/target", schema.target_namespace)

    def test_schema_nsmap_without_target_namespace(self):
        xsd = """<?xml version="1.0" encoding="utf-8"?>
                <xs:schema xmlns="http://www/default"
                xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1"></xs:schema>"""

        self.parser.target_namespace = "parent"
        schema = self.parser.from_xsd_string(xsd)
        expected = {
            None: "http://www/default",
            "xlink": "http://www.w3.org/1999/xlink",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "xs": "http://www.w3.org/2001/XMLSchema",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }
        self.assertEqual(expected, schema.nsmap)
        self.assertEqual("parent", schema.target_namespace)

    def test_top_level_elements_and_attributes_are_qualified(self):
        xsd = """<xs:element name="a" /><xs:attribute name="b" />"""

        schema = self.parser.from_xsd_string(wrap(xsd))
        self.assertEqual(FormType.QUALIFIED, schema.attributes[0].form)
        self.assertEqual(FormType.QUALIFIED, schema.elements[0].form)

    def test_empty_tags_without_children_are_ignored(self):
        xsd = """<xs:complexType name="foo" /><xs:element />
        <xs:annotation><xs:documentation></xs:documentation></xs:annotation>
        """

        schema = self.parser.from_xsd_string(wrap(xsd))
        self.assertEqual(0, len(schema.elements))
        self.assertEqual(1, len(schema.complex_types))
        self.assertEqual(1, len(schema.annotations))
        self.assertEqual(0, len(schema.annotations[0].documentations))

    def test_complex_type_with_sequence(self):
        xsd = """<xs:complexType name="allowablePointsOfSaleType">
            <xs:sequence maxOccurs="unbounded">
                <xs:element name="PointOfSale">
                    <xs:complexType>
                        <xs:attribute name="id" type="xs:string"/>
                    </xs:complexType>
                </xs:element>
                <xs:any processContents="lax" />
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
                any=[
                    Any.create(
                        index=6,
                        min_occurs=1,
                        max_occurs=9223372036854775807,
                        process_contents=ProcessType.LAX,
                    )
                ],
            ),
        )
        schema = self.parser.from_xsd_string(wrap(xsd))
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
        schema = self.parser.from_xsd_string(wrap(xsd))
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
                                    min_length=MinLength.create(value=1, index=7),
                                ),
                            ),
                        )
                    ],
                ),
            ),
        )
        schema = self.parser.from_xsd_string(wrap(xsd))
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
        schema = self.parser.from_xsd_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_all_resets_elements_max_occurs(self):
        xsd = """<xs:complexType>
                    <xs:all minOccurs="1">
                    <xs:element name="first" maxOccurs="100" />
                    <xs:element name="second" maxOccurs="100" />
                    <xs:any processContents="lax" />
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
                any=Any.create(
                    index=5,
                    min_occurs=1,
                    max_occurs=1,
                    process_contents=ProcessType.LAX,
                ),
            ),
        )
        schema = self.parser.from_xsd_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_schema_with_default_attributes(self):
        xsd = """<xs:complexType>
                    <xs:attributeGroup ref="bar" />
              </xs:complexType>
              <xs:element name="first">
                  <xs:complexType>
                        <xs:attribute name="second" />
                  </xs:complexType>
              </xs:element>
              <xs:element name="third">
                  <xs:complexType defaultAttributesApply="false">
                        <xs:attribute name="w" />
                  </xs:complexType>
              </xs:element>
              """

        attrs = {"defaultAttributes": "foo"}

        schema = self.parser.from_xsd_string(wrap(xsd, **attrs))

        self.assertEqual(2, len(schema.complex_types[0].attribute_groups))
        self.assertEqual("foo", schema.complex_types[0].attribute_groups[0].ref)
        self.assertEqual("bar", schema.complex_types[0].attribute_groups[1].ref)
        self.assertEqual("foo", schema.elements[0].complex_type.attribute_groups[0].ref)
        self.assertEqual(0, len(schema.elements[1].complex_type.attribute_groups))
