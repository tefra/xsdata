import sys
from pathlib import Path
from unittest import mock
from unittest import TestCase

from xsdata.models.elements import All
from xsdata.models.elements import Any
from xsdata.models.elements import Attribute
from xsdata.models.elements import Choice
from xsdata.models.elements import ComplexContent
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Extension
from xsdata.models.elements import Import
from xsdata.models.elements import Include
from xsdata.models.elements import MinLength
from xsdata.models.elements import Override
from xsdata.models.elements import Pattern
from xsdata.models.elements import Redefine
from xsdata.models.elements import Restriction
from xsdata.models.elements import Schema
from xsdata.models.elements import Sequence
from xsdata.models.elements import SimpleContent
from xsdata.models.elements import SimpleType
from xsdata.models.enums import FormType
from xsdata.models.enums import Namespace
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


class SchemaParserTests(TestCase):
    nsmap = {
        "xs": "http://www.w3.org/2001/XMLSchema",
        "xml": "http://www.w3.org/XML/1998/namespace",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xlink": "http://www.w3.org/1999/xlink",
    }

    def setUp(self) -> None:
        self.parser = SchemaParser()
        super(SchemaParserTests, self).setUp()

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
            nsmap=self.nsmap,
            sequence=Sequence.create(
                index=2,
                nsmap=self.nsmap,
                max_occurs=sys.maxsize,
                elements=[
                    Element.create(
                        index=3,
                        nsmap=self.nsmap,
                        name="PointOfSale",
                        form=FormType.QUALIFIED,
                        max_occurs=sys.maxsize,
                        min_occurs=1,
                        complex_type=ComplexType.create(
                            index=4,
                            nsmap=self.nsmap,
                            attributes=[
                                Attribute.create(
                                    index=5,
                                    nsmap=self.nsmap,
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
                        nsmap=self.nsmap,
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
            nsmap=self.nsmap,
            name="priceCurrencyType",
            simple_content=SimpleContent.create(
                index=2,
                nsmap=self.nsmap,
                extension=Extension.create(
                    index=3,
                    nsmap=self.nsmap,
                    base="priceType",
                    attributes=[
                        Attribute.create(
                            index=4,
                            nsmap=self.nsmap,
                            name="currency",
                            use=UseType.REQUIRED,
                            form=FormType.UNQUALIFIED,
                            simple_type=SimpleType.create(
                                nsmap=self.nsmap,
                                index=5,
                                restriction=Restriction.create(
                                    nsmap=self.nsmap,
                                    index=6,
                                    base="xs:string",
                                    pattern=Pattern.create(
                                        index=7,
                                        value="[A-Z][A-Z][A-Z]",
                                        nsmap=self.nsmap,
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
            nsmap=self.nsmap,
            name="UserRateConditionType",
            complex_content=ComplexContent.create(
                index=2,
                nsmap=self.nsmap,
                extension=Extension.create(
                    index=3,
                    nsmap=self.nsmap,
                    base="UserRateConditionBaseType",
                    attributes=[
                        Attribute.create(
                            index=4,
                            nsmap=self.nsmap,
                            name="id",
                            use=UseType.REQUIRED,
                            form=FormType.QUALIFIED,
                            simple_type=SimpleType.create(
                                index=5,
                                nsmap=self.nsmap,
                                restriction=Restriction.create(
                                    index=6,
                                    nsmap=self.nsmap,
                                    base="xs:string",
                                    min_length=MinLength.create(
                                        value=1, index=7, nsmap=self.nsmap
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

    def test_complex_type_with_choice_resets_elements_min_occurs(self):
        xsd = """<xs:complexType>
                <xs:choice minOccurs="1">
                    <xs:element name="first" minOccurs="1" />
                    <xs:element name="second" minOccurs="1" />
                </xs:choice>
            </xs:complexType>"""

        expected = ComplexType.create(
            index=1,
            nsmap=self.nsmap,
            choice=Choice.create(
                index=2,
                nsmap=self.nsmap,
                min_occurs=1,
                elements=[
                    Element.create(
                        name="first",
                        min_occurs=0,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=3,
                        nsmap=self.nsmap,
                    ),
                    Element.create(
                        name="second",
                        min_occurs=0,
                        max_occurs=1,
                        form=FormType.QUALIFIED,
                        index=4,
                        nsmap=self.nsmap,
                    ),
                ],
            ),
        )
        schema = self.parser.from_xsd_string(wrap(xsd))
        self.assertEqual(expected, schema.complex_types[0])

    def test_complex_type_with_all_resets_elements_max_occurs(self):
        xsd = """<xs:complexType>
                    <xs:all minOccurs="0">
                    <xs:element name="first" maxOccurs="100" />
                    <xs:element name="second" maxOccurs="100" />
                    <xs:any processContents="lax" />
                    </xs:all>
              </xs:complexType>"""

        expected = ComplexType.create(
            index=1,
            nsmap=self.nsmap,
            all=All.create(
                index=2,
                nsmap=self.nsmap,
                min_occurs=0,
                elements=[
                    Element.create(
                        name="first",
                        min_occurs=0,
                        max_occurs=100,
                        form=FormType.QUALIFIED,
                        index=3,
                        nsmap=self.nsmap,
                    ),
                    Element.create(
                        name="second",
                        min_occurs=0,
                        max_occurs=100,
                        form=FormType.QUALIFIED,
                        index=4,
                        nsmap=self.nsmap,
                    ),
                ],
                any=[
                    Any.create(
                        index=5,
                        nsmap=self.nsmap,
                        min_occurs=0,
                        max_occurs=1,
                        process_contents=ProcessType.LAX,
                    )
                ],
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

    @mock.patch.object(SchemaParser, "resolve_schemas_locations")
    @mock.patch.object(SchemaParser, "add_default_imports")
    @mock.patch.object(SchemaParser, "set_schema_namespaces")
    @mock.patch.object(SchemaParser, "set_schema_forms")
    def test_end_schema(
        self,
        mock_set_schema_forms,
        mock_set_schema_namespaces,
        mock_add_default_imports,
        mock_resolve_schemas_locations,
    ):
        schema = Schema.create()
        element = Element("schema")

        self.parser.end_schema(schema, element)
        mock_set_schema_forms.assert_called_once_with(schema)
        mock_set_schema_namespaces.assert_called_once_with(schema, element)
        mock_add_default_imports.assert_called_once_with(schema)
        mock_resolve_schemas_locations.assert_called_once_with(schema)

    def test_add_default_imports(self):
        schema = Schema.create()
        schema.imports.append(Import.create(namespace="foo"))

        self.parser.add_default_imports(schema)
        self.assertEqual(1, len(schema.imports))

        xsi = Namespace.XSI.value
        schema.nsmap["foo"] = xsi
        self.parser.add_default_imports(schema)
        self.assertEqual(2, len(schema.imports))
        self.assertEqual(Import.create(namespace=xsi), schema.imports[0])

    @mock.patch.object(SchemaParser, "resolve_local_path")
    @mock.patch.object(SchemaParser, "resolve_path")
    def test_resolve_schemas_locations(
        self, mock_resolve_path, mock_resolve_local_path
    ):
        schema = Schema.create()
        self.parser.resolve_schemas_locations(schema)

        self.parser.schema_location = Path.cwd()

        mock_resolve_path.side_effect = lambda x: Path.cwd().joinpath(x)
        mock_resolve_local_path.side_effect = lambda x, y: Path.cwd().joinpath(x)

        schema.overrides.append(Override.create(schema_location="o1"))
        schema.overrides.append(Override.create(schema_location="o2"))
        schema.redefines.append(Redefine.create(schema_location="r1"))
        schema.redefines.append(Redefine.create(schema_location="r2"))
        schema.includes.append(Include.create(schema_location="i1"))
        schema.includes.append(Include.create(schema_location="i2"))
        schema.imports.append(Import.create(schema_location="i3", namespace="ns_i3"))
        schema.imports.append(Import.create(schema_location="i4", namespace="ns_i4"))

        self.parser.resolve_schemas_locations(schema)

        mock_resolve_path.assert_has_calls(
            [
                mock.call("o1"),
                mock.call("o2"),
                mock.call("r1"),
                mock.call("r2"),
                mock.call("i1"),
                mock.call("i2"),
            ]
        )

        mock_resolve_local_path.assert_has_calls(
            [mock.call("i3", "ns_i3"), mock.call("i4", "ns_i4")]
        )

        for sub in schema.included():
            self.assertEqual(Path.cwd().joinpath(sub.schema_location), sub.location)

    def test_resolve_path(self):
        self.assertIsNone(self.parser.resolve_path("foo"))
        iam = Path(__file__)

        self.parser.schema_location = iam
        self.assertIsNone(self.parser.resolve_path(""))
        self.assertIsNone(self.parser.resolve_path(None))
        self.assertIsNone(self.parser.resolve_path("a"))

        actual = self.parser.resolve_path(iam.name)
        self.assertEqual(iam, actual)

    def test_resolve_local_path(self):
        self.assertIsNone(self.parser.resolve_local_path("foo", "bar"))
        self.assertIsNone(self.parser.resolve_local_path("foo", None))
        self.assertIsNone(self.parser.resolve_local_path(None, None))
        self.assertIsNone(self.parser.resolve_local_path(None, "bar"))

        self.assertEqual(
            Namespace.XSI.location,
            self.parser.resolve_local_path(None, Namespace.XSI.value),
        )

        self.assertEqual(
            Namespace.XSI.location,
            self.parser.resolve_local_path("http://something", Namespace.XSI.value),
        )
        iam = Path(__file__)
        self.parser.schema_location = iam
        self.assertEqual(
            iam, self.parser.resolve_local_path(iam.name, Namespace.XSI.value)
        )
