import sys
from pathlib import Path
from unittest import mock
from unittest import TestCase

from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.models.enums import FormType
from xsdata.models.enums import Mode
from xsdata.models.enums import Namespace
from xsdata.models.xsd import All
from xsdata.models.xsd import Any
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import AttributeGroup
from xsdata.models.xsd import ComplexContent
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import DefaultOpenContent
from xsdata.models.xsd import Element
from xsdata.models.xsd import Extension
from xsdata.models.xsd import Import
from xsdata.models.xsd import Include
from xsdata.models.xsd import OpenContent
from xsdata.models.xsd import Override
from xsdata.models.xsd import Redefine
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import Schema


class SchemaParserTests(TestCase):
    def setUp(self):
        self.parser = SchemaParser()
        super().setUp()

    def test_complete(self):
        xsd = """<?xml version="1.0" encoding="utf-8"?>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
            <xs:simpleType name="CountryType">
                <xs:annotation>
                  <xs:documentation>
                    <keyword>country</keyword>
                  </xs:documentation>
                </xs:annotation>
              </xs:simpleType>
            </xs:schema>"""

        schema = self.parser.from_string(xsd, Schema)
        expected_namespaces = {
            "xlink": "http://www.w3.org/1999/xlink",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "xs": "http://www.w3.org/2001/XMLSchema",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }

        self.assertIsInstance(schema, Schema)

        self.assertEqual(expected_namespaces, schema.simple_types[0].ns_map)
        self.assertEqual(2, schema.simple_types[0].index)
        self.assertEqual(3, schema.simple_types[0].annotations[0].index)
        self.assertEqual(
            4, schema.simple_types[0].annotations[0].documentations[0].index
        )

    def test_start_schema(self):
        self.parser.start_schema({})

        self.assertIsNone(self.parser.element_form)
        self.assertIsNone(self.parser.attribute_form)
        self.assertIsNone(self.parser.default_attributes)

        attrs = {
            "elementFormDefault": "qualified",
            "attributeFormDefault": "unqualified",
            "defaultAttributes": "tns:attr",
        }
        self.parser.start_schema(attrs)

        self.assertEqual("qualified", self.parser.element_form)
        self.assertEqual("unqualified", self.parser.attribute_form)
        self.assertEqual("tns:attr", self.parser.default_attributes)

    def test_set_schema_forms_default(self):
        schema = Schema()
        schema.elements.append(Element())
        schema.elements.append(Element())
        schema.attributes.append(Element())
        schema.attributes.append(Element())

        self.parser.set_schema_forms(schema)

        self.assertEqual(FormType.UNQUALIFIED, schema.element_form_default)
        self.assertEqual(FormType.UNQUALIFIED, schema.attribute_form_default)

        for child_element in schema.elements:
            self.assertEqual(FormType.QUALIFIED, child_element.form)

        for child_attribute in schema.attributes:
            self.assertEqual(FormType.QUALIFIED, child_attribute.form)

    def test_set_schema_forms(self):
        schema = Schema()
        schema.elements.append(Element())
        schema.elements.append(Element())
        schema.attributes.append(Element())
        schema.attributes.append(Element())

        self.parser.element_form = "unqualified"
        self.parser.attribute_form = "qualified"
        self.parser.set_schema_forms(schema)

        self.assertEqual(FormType.UNQUALIFIED, schema.element_form_default)
        self.assertEqual(FormType.QUALIFIED, schema.attribute_form_default)

        for child_element in schema.elements:
            self.assertEqual(FormType.QUALIFIED, child_element.form)

        for child_attribute in schema.attributes:
            self.assertEqual(FormType.QUALIFIED, child_attribute.form)

    def test_set_schema_namespaces(self):
        schema = Schema()

        self.parser.set_schema_namespaces(schema)
        self.assertIsNone(schema.target_namespace)

        self.parser.target_namespace = "bar"
        self.parser.set_schema_namespaces(schema)
        self.assertEqual("bar", schema.target_namespace)

        schema.target_namespace = "foo"
        self.parser.set_schema_namespaces(schema)
        self.assertEqual("foo", schema.target_namespace)

    def test_set_namespace_map(self):
        schema = Schema()
        ns_map = {}

        self.parser.set_namespace_map(schema, ns_map)

        expected = {
            "xlink": "http://www.w3.org/1999/xlink",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "xs": "http://www.w3.org/2001/XMLSchema",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }
        self.assertEqual(expected, schema.ns_map)

        self.parser.set_namespace_map(schema, None)
        self.assertEqual(expected, schema.ns_map)

        ns_map = {"foo": "bar", "not": "http://www.w3.org/2001/XMLSchema"}
        schema = Schema()
        expected = {
            "foo": "bar",
            "xlink": "http://www.w3.org/1999/xlink",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "not": "http://www.w3.org/2001/XMLSchema",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }

        self.parser.set_namespace_map(schema, ns_map)
        self.assertEqual(expected, schema.ns_map)

        foo = []
        self.parser.set_namespace_map(foo, ns_map)
        self.assertFalse(hasattr(foo, "ns_map"))

    def test_add_default_imports(self):
        schema = Schema()
        schema.imports.append(Import(namespace="foo"))

        self.parser.add_default_imports(schema)
        self.assertEqual(1, len(schema.imports))

        xsi = Namespace.XSI.uri
        schema.ns_map["foo"] = xsi
        self.parser.add_default_imports(schema)
        self.assertEqual(2, len(schema.imports))
        self.assertEqual(Import(namespace=xsi), schema.imports[0])

    @mock.patch.object(SchemaParser, "resolve_local_path")
    @mock.patch.object(SchemaParser, "resolve_path")
    def test_resolve_schemas_locations(
        self, mock_resolve_path, mock_resolve_local_path
    ):
        schema = Schema()
        self.parser.resolve_schemas_locations(schema)

        self.parser.location = Path.cwd()

        mock_resolve_path.side_effect = lambda x: Path.cwd().joinpath(x)
        mock_resolve_local_path.side_effect = lambda x, y: Path.cwd().joinpath(x)

        schema.overrides.append(Override(schema_location="o1"))
        schema.overrides.append(Override(schema_location="o2"))
        schema.redefines.append(Redefine(schema_location="r1"))
        schema.redefines.append(Redefine(schema_location="r2"))
        schema.includes.append(Include(schema_location="i1"))
        schema.includes.append(Include(schema_location="i2"))
        schema.imports.append(Import(schema_location="i3", namespace="ns_i3"))
        schema.imports.append(Import(schema_location="i4", namespace="ns_i4"))

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
            self.assertEqual(Path.cwd().joinpath(sub.location), sub.location)

    def test_resolve_path(self):
        self.assertIsNone(self.parser.resolve_path("foo"))
        iam = Path(__file__)

        self.parser.location = iam.as_uri()
        self.assertIsNone(self.parser.resolve_path(""))
        self.assertIsNone(self.parser.resolve_path(None))

        actual = self.parser.resolve_path(iam.name)
        self.assertEqual(iam.as_uri(), actual)

    def test_resolve_local_path(self):
        self.assertIsNone(self.parser.resolve_local_path("foo", "bar"))
        self.assertIsNone(self.parser.resolve_local_path("foo", None))
        self.assertIsNone(self.parser.resolve_local_path(None, None))
        self.assertIsNone(self.parser.resolve_local_path(None, "bar"))

        self.assertEqual(
            Namespace.XSI.location,
            self.parser.resolve_local_path(None, Namespace.XSI.uri),
        )

        iam = Path(__file__)
        self.parser.location = iam.as_uri()
        self.assertEqual(iam.as_uri(), self.parser.resolve_local_path(iam.name, None))
        self.assertEqual(
            "http://something",
            self.parser.resolve_local_path("http://something", Namespace.XSI.uri),
        )
        self.assertEqual(
            iam.parent.parent.joinpath("xsi.xsd").as_uri(),
            self.parser.resolve_local_path("../xsi.xsd", Namespace.XSI.uri),
        )

    def test_end_attribute(self):
        attribute = Attribute()

        self.parser.end_attribute(attribute)
        self.assertIsNone(attribute.form)

        self.parser.attribute_form = "qualified"
        self.parser.end_attribute(attribute)
        self.assertEqual(FormType.QUALIFIED, attribute.form)

        obj = Element()
        self.parser.end_attribute(obj)
        self.assertIsNone(obj.form)

    def test_end_complex_type(self):
        complex_type = ComplexType()
        not_complex_type = Element()

        self.parser.end_complex_type(not_complex_type)
        self.parser.end_complex_type(complex_type)

        self.assertEqual(0, len(complex_type.attribute_groups))
        self.assertIsNone(complex_type.open_content)

        self.parser.default_attributes = "tns:attrs"
        self.parser.end_complex_type(complex_type)

        expected = AttributeGroup(ref="tns:attrs")
        self.assertEqual([expected], complex_type.attribute_groups)
        self.assertIsNone(complex_type.open_content)

        default_open_content = DefaultOpenContent()
        self.parser.default_attributes = None
        self.parser.default_open_content = default_open_content
        self.parser.end_complex_type(complex_type)
        self.assertIs(default_open_content, complex_type.open_content)

        open_content = OpenContent()
        complex_type.open_content = open_content
        self.parser.end_complex_type(complex_type)
        self.assertIs(open_content, complex_type.open_content)

        complex_type = ComplexType()
        complex_type.complex_content = ComplexContent()
        self.parser.end_complex_type(complex_type)
        self.assertIsNone(complex_type.open_content)

        obj = Extension()
        self.parser.end_complex_type(obj)
        self.assertIsNone(obj.open_content)

    def test_end_default_open_content(self):
        default_open_content = DefaultOpenContent()
        default_open_content.any = Any()

        self.parser.end_default_open_content(default_open_content)
        self.assertEqual(default_open_content, self.parser.default_open_content)
        self.assertEqual(0, default_open_content.any.index)

        default_open_content.mode = Mode.SUFFIX
        self.parser.end_default_open_content(default_open_content)
        self.assertEqual(sys.maxsize, default_open_content.any.index)

        obj = ComplexType()
        self.parser.end_default_open_content(obj)
        self.assertIsNone(obj.open_content)

    def test_end_Element(self):
        obj = Element()
        self.parser.end_element(obj)
        self.assertIsNone(obj.form)

        self.parser.element_form = "qualified"
        self.parser.end_element(obj)
        self.assertEqual(FormType.QUALIFIED, obj.form)

        obj = Attribute()
        self.parser.end_element(obj)
        self.assertIsNone(obj.form)

    def test_end_extension(self):
        extension = Extension()
        not_extension = Element()

        self.parser.end_extension(not_extension)
        self.parser.end_extension(extension)

        default_open_content = DefaultOpenContent()
        self.parser.default_open_content = default_open_content
        self.parser.end_extension(extension)

        self.assertIs(default_open_content, extension.open_content)

        open_content = OpenContent()
        extension.open_content = open_content
        self.parser.end_extension(extension)
        self.assertIs(open_content, extension.open_content)

        obj = ComplexType()
        self.parser.end_extension(obj)
        self.assertIsNone(obj.open_content)

    def test_end_open_content(self):
        open_content = OpenContent()
        open_content.any = Any()

        self.parser.end_open_content(open_content)
        self.assertEqual(0, open_content.any.index)

        open_content.mode = Mode.SUFFIX
        self.parser.end_open_content(open_content)
        self.assertEqual(sys.maxsize, open_content.any.index)

        obj = All(any=Any())
        self.parser.end_open_content(obj)
        self.assertEqual(0, obj.any.index)

    def test_end_restriction(self):
        restriction = Restriction()
        not_restriction = Element()

        self.parser.end_restriction(not_restriction)
        self.parser.end_restriction(restriction)

        default_open_content = DefaultOpenContent()
        self.parser.default_open_content = default_open_content
        self.parser.end_restriction(restriction)

        self.assertIs(default_open_content, restriction.open_content)

        open_content = OpenContent()
        restriction.open_content = open_content
        self.parser.end_restriction(restriction)
        self.assertIs(open_content, restriction.open_content)

        obj = ComplexType()
        self.parser.end_open_content(obj)
        self.assertIsNone(obj.open_content)

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
        schema = Schema()
        schema.elements.append(Element())
        schema.elements.append(Element())
        schema.elements.append(Element())

        for el in schema.elements:
            self.assertEqual(1, el.min_occurs)
            self.assertEqual(1, el.max_occurs)

        self.parser.end_schema(schema)

        for el in schema.elements:
            self.assertIsNone(el.min_occurs)
            self.assertIsNone(el.max_occurs)

        self.parser.end_schema(ComplexType())

        mock_set_schema_forms.assert_called_once_with(schema)
        mock_set_schema_namespaces.assert_called_once_with(schema)
        mock_add_default_imports.assert_called_once_with(schema)
        mock_resolve_schemas_locations.assert_called_once_with(schema)
