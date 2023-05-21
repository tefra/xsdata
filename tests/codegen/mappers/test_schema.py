from types import GeneratorType
from typing import Iterator
from unittest import mock

from xsdata.codegen.mappers.schema import SchemaMapper
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Tag
from xsdata.models.enums import UseType
from xsdata.models.xsd import Alternative
from xsdata.models.xsd import Annotation
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import AttributeGroup
from xsdata.models.xsd import Choice
from xsdata.models.xsd import ComplexContent
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Enumeration
from xsdata.models.xsd import Extension
from xsdata.models.xsd import Group
from xsdata.models.xsd import Override
from xsdata.models.xsd import Redefine
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import Schema
from xsdata.models.xsd import Sequence
from xsdata.models.xsd import SimpleContent
from xsdata.models.xsd import SimpleType
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class SchemaMapperTests(FactoryTestCase):
    @mock.patch.object(SchemaMapper, "build_class")
    @mock.patch.object(SchemaMapper, "root_elements")
    def test_map(self, mock_root_elements, mock_build_class):
        simple_type = ComplexType()
        complex_type = ComplexType()
        schema = Schema(target_namespace="fooNS", location="foo.xsd")

        mock_build_class.side_effect = ClassFactory.list(3)
        mock_root_elements.return_value = [
            (Tag.SCHEMA, Group),
            (Tag.OVERRIDE, simple_type),
            (Tag.REDEFINE, complex_type),
        ]

        actual = SchemaMapper.map(schema)
        self.assertEqual(3, len(actual))
        self.assertIsInstance(actual[0], Class)

        mock_root_elements.assert_called_once_with(schema)

    def test_root_elements(self):
        override = Override()
        redefine = Redefine()

        redefine.annotation = Annotation()
        redefine.complex_types.append(ComplexType())

        override.annotation = Annotation()
        override.groups.append(Group())
        override.simple_types.append(SimpleType())

        schema = Schema()
        schema.simple_types.append(SimpleType())
        schema.attribute_groups.append(AttributeGroup())
        schema.groups.append(Group())
        schema.attributes.append(Attribute())
        schema.complex_types.append(ComplexType())
        schema.elements.append(Element())
        schema.redefines.append(redefine)
        schema.overrides.append(override)

        iterator = SchemaMapper.root_elements(schema)
        expected = [
            ("Override", override.simple_types[0]),
            ("Override", override.groups[0]),
            ("Redefine", redefine.complex_types[0]),
            ("Schema", schema.simple_types[0]),
            ("Schema", schema.complex_types[0]),
            ("Schema", schema.groups[0]),
            ("Schema", schema.attribute_groups[0]),
            ("Schema", schema.elements[0]),
            ("Schema", schema.attributes[0]),
        ]
        self.assertEqual(expected, list(iterator))

    def test_element_namespace(self):
        target_ns = "foobar"

        element = Element(ref="foo:something")
        element.ns_map["foo"] = "bar"

        self.assertEqual("bar", SchemaMapper.element_namespace(element, target_ns))

        element = Element(form=FormType.QUALIFIED)
        self.assertEqual("foobar", SchemaMapper.element_namespace(element, target_ns))

        element = Element()
        self.assertEqual("", SchemaMapper.element_namespace(element, target_ns))

        element.target_namespace = "tns"
        self.assertEqual("tns", SchemaMapper.element_namespace(element, target_ns))

        attribute = Attribute()
        self.assertIsNone(SchemaMapper.element_namespace(attribute, target_ns))

        attribute.target_namespace = "tns"
        self.assertEqual("tns", SchemaMapper.element_namespace(attribute, target_ns))

        element = Element(ref="something")
        self.assertEqual("foobar", SchemaMapper.element_namespace(element, target_ns))

        element.ns_map["foo"] = "foobar"
        self.assertEqual("", SchemaMapper.element_namespace(element, target_ns))

        element.ns_map[None] = "foobar"
        self.assertEqual("foobar", SchemaMapper.element_namespace(element, target_ns))

    @mock.patch.object(SchemaMapper, "element_namespace")
    @mock.patch.object(SchemaMapper, "build_class_attributes")
    @mock.patch.object(SchemaMapper, "build_class_extensions")
    @mock.patch.object(Element, "substitutions", new_callable=mock.PropertyMock)
    @mock.patch.object(Element, "is_abstract", new_callable=mock.PropertyMock)
    @mock.patch.object(Element, "is_nillable", new_callable=mock.PropertyMock)
    @mock.patch.object(Element, "display_help", new_callable=mock.PropertyMock)
    @mock.patch.object(Element, "real_name", new_callable=mock.PropertyMock)
    def test_build_class(
        self,
        mock_real_name,
        mock_display_help,
        mock_is_nillable,
        mock_is_abstract,
        mock_substitutions,
        mock_build_class_extensions,
        mock_build_class_attributes,
        mock_element_namespace,
    ):
        mock_real_name.return_value = "name"
        mock_display_help.return_value = "sos"
        mock_is_abstract.return_value = True
        mock_is_nillable.return_value = True
        mock_substitutions.return_value = ["foo", "sm:bar"]
        mock_element_namespace.return_value = "foo:name"

        element = Element()
        element.ns_map["sm"] = "sm_ns"
        result = SchemaMapper.build_class(element, "container", "tests", "target_ns")

        mock_build_class_attributes.assert_called_once_with(element, result)
        mock_build_class_extensions.assert_called_once_with(element, result)
        mock_element_namespace.assert_called_once_with(element, "target_ns")

        expected = ClassFactory.create(
            qname=build_qname("target_ns", "name"),
            tag=Tag.ELEMENT,
            help="sos",
            abstract=True,
            nillable=True,
            namespace="foo:name",
            ns_map=element.ns_map,
            module=None,
            location="tests",
            substitutions=[
                build_qname("target_ns", "foo"),
                build_qname("sm_ns", "bar"),
            ],
            container="container",
        )
        self.assertEqual(expected, result)

    @mock.patch.object(SchemaMapper, "children_extensions")
    def test_build_class_extensions(self, mock_children_extensions):
        bar_type = AttrTypeFactory.create(qname="bar")
        foo_type = AttrTypeFactory.create(qname="foo")

        bar = ExtensionFactory.create(bar_type, tag=Tag.RESTRICTION)
        double = ExtensionFactory.create(bar_type, tag=Tag.RESTRICTION)
        foo = ExtensionFactory.create(foo_type, tag=Tag.EXTENSION)

        mock_children_extensions.return_value = [bar, double, foo]
        self_ext = ExtensionFactory.reference(
            qname="{xsdata}something",
            tag=Tag.ELEMENT,
            restrictions=Restrictions(min_occurs=1, max_occurs=1),
        )

        item = ClassFactory.create()
        element = Element(type="something")
        SchemaMapper.build_class_extensions(element, item)

        self.assertEqual(3, len(item.extensions))
        self.assertCountEqual([bar, self_ext, foo], item.extensions)

    def test_element_children(self):
        sequence_one = Sequence(elements=[Element(), Element()])
        sequence_one.index = 1
        sequence_two = Sequence(max_occurs=2, elements=[Element(), Element()])
        sequence_two.index = 2
        restriction = Restriction(
            enumerations=[Enumeration(value=x) for x in "abc"], sequence=sequence_two
        )
        complex_type = ComplexType(
            attributes=[Attribute(), Attribute()],
            sequence=sequence_one,
            simple_content=SimpleContent(restriction=Restriction()),
            complex_content=ComplexContent(restriction=restriction),
        )
        restrictions = Restrictions.from_element(complex_type)
        children = SchemaMapper.element_children(complex_type, restrictions)
        expected = [
            (sequence_two.elements[0], Restrictions.from_element(sequence_two)),
            (sequence_two.elements[1], Restrictions.from_element(sequence_two)),
            (restriction.enumerations[0], Restrictions.from_element(restriction)),
            (restriction.enumerations[1], Restrictions.from_element(restriction)),
            (restriction.enumerations[2], Restrictions.from_element(restriction)),
            (sequence_one.elements[0], Restrictions.from_element(sequence_one)),
            (sequence_one.elements[1], Restrictions.from_element(sequence_one)),
            (complex_type.attributes[0], Restrictions.from_element(complex_type)),
            (complex_type.attributes[1], Restrictions.from_element(complex_type)),
        ]
        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    def test_element_children_with_parents_restrictions(self):
        choice = Choice(elements=[Element(name="elem1")])
        complex_type = ComplexType(
            sequence=Sequence(choices=[choice], min_occurs=0, max_occurs=3)
        )
        complex_type.sequence.index = 2
        parent_restrictions = Restrictions.from_element(complex_type)
        children = SchemaMapper.element_children(complex_type, parent_restrictions)

        child, restrictions = next(children)
        expected = Restrictions(
            path=[("s", id(complex_type.sequence), 0, 3), ("c", id(choice), 1, 1)]
        )
        self.assertEqual(expected, restrictions)

    def test_children_extensions(self):
        complex_type = ComplexType(
            attributes=[Attribute() for _ in range(2)],
            simple_content=SimpleContent(restriction=Restriction(base="bk:b")),
            complex_content=ComplexContent(extension=Extension(base="bk:c")),
        )
        complex_type.simple_content.restriction.index = 4
        complex_type.complex_content.extension.index = 7

        item = ClassFactory.create(ns_map={"bk": "book"})
        children = SchemaMapper.children_extensions(complex_type, item)
        expected = [
            ExtensionFactory.create(
                AttrTypeFactory.create(qname=build_qname("book", "b")),
                tag=Tag.RESTRICTION,
            ),
            ExtensionFactory.create(
                AttrTypeFactory.create(qname=build_qname("book", "c")),
                tag=Tag.EXTENSION,
            ),
        ]

        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    @mock.patch.object(SchemaMapper, "build_class_attribute_types")
    @mock.patch.object(SchemaMapper, "element_namespace")
    @mock.patch.object(Attribute, "get_restrictions")
    @mock.patch.object(Attribute, "is_fixed", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "default_value", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "prefix", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "display_help", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "real_name", new_callable=mock.PropertyMock)
    def test_build_class_attribute(
        self,
        mock_real_name,
        mock_display_help,
        mock_prefix,
        mock_default_value,
        mock_is_fixed,
        mock_get_restrictions,
        mock_element_namespace,
        mock_build_class_attribute_types,
    ):
        item = ClassFactory.create(ns_map={"bar": "foo"})

        mock_build_class_attribute_types.return_value = AttrTypeFactory.list(
            1, qname="int"
        )
        mock_real_name.return_value = item.name
        mock_display_help.return_value = "sos"
        mock_prefix.return_value = "com"
        mock_default_value.return_value = "default"
        mock_is_fixed.return_value = True
        mock_element_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"min_occurs": 1, "max_occurs": 1}

        attribute = Attribute(default="false")
        attribute.index = 66
        attribute.ns_map["foo"] = "bar"

        SchemaMapper.build_class_attribute(item, attribute, Restrictions())
        expected = AttrFactory.create(
            name=mock_real_name.return_value,
            types=mock_build_class_attribute_types.return_value,
            tag=Tag.ATTRIBUTE,
            namespace=mock_element_namespace.return_value,
            help=mock_display_help.return_value,
            default=mock_default_value.return_value,
            fixed=mock_is_fixed.return_value,
            index=66,
            restrictions=Restrictions(min_occurs=1, max_occurs=1),
        )
        self.assertEqual(expected, item.attrs[0])
        self.assertEqual({"bar": "foo", "foo": "bar"}, item.ns_map)
        mock_build_class_attribute_types.assert_called_once_with(item, attribute)
        mock_element_namespace.assert_called_once_with(attribute, item.target_namespace)

    @mock.patch.object(Attribute, "attr_types", new_callable=mock.PropertyMock)
    @mock.patch.object(SchemaMapper, "build_inner_classes")
    def test_build_class_attribute_types(
        self, mock_build_inner_classes, mock_attr_types
    ):
        mock_attr_types.return_value = ["xs:integer", "xs:string"]
        mock_build_inner_classes.return_value = []

        item = ClassFactory.create()
        attribute = Attribute(default="false")
        actual = SchemaMapper.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.native(DataType.INTEGER),
            AttrTypeFactory.native(DataType.STRING),
        ]

        self.assertEqual(expected, actual)

    @mock.patch.object(Attribute, "attr_types", new_callable=mock.PropertyMock)
    @mock.patch.object(SchemaMapper, "build_inner_classes")
    def test_build_class_attribute_types_when_obj_has_inner_class(
        self, mock_build_inner_classes, mock_attr_types
    ):
        inner_class = ClassFactory.create(qname="foo")
        mock_attr_types.return_value = ["xs:integer", "xs:string"]
        mock_build_inner_classes.return_value = [inner_class]

        item = ClassFactory.create()
        attribute = Attribute(default="false")
        actual = SchemaMapper.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.native(DataType.INTEGER),
            AttrTypeFactory.native(DataType.STRING),
            AttrTypeFactory.create(qname=inner_class.qname, forward=True),
        ]

        self.assertEqual(expected, actual)
        self.assertEqual([inner_class], item.inner)

    @mock.patch.object(Attribute, "default_type", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "attr_types", new_callable=mock.PropertyMock)
    @mock.patch.object(SchemaMapper, "build_inner_classes")
    def test_build_class_attribute_types_when_obj_has_no_types(
        self, mock_build_inner_classes, mock_attr_types, mock_default_type
    ):
        mock_attr_types.return_value = ""
        mock_build_inner_classes.return_value = []
        mock_default_type.return_value = "xs:string"

        item = ClassFactory.create()
        attribute = Attribute(default="false", name="attr")
        actual = SchemaMapper.build_class_attribute_types(item, attribute)

        self.assertEqual(1, len(actual))
        self.assertEqual(AttrTypeFactory.native(DataType.STRING), actual[0])

    @mock.patch.object(SchemaMapper, "build_class")
    def test_build_inner_classes(self, mock_build_class):
        inner_classes = ClassFactory.list(2)
        mock_build_class.side_effect = inner_classes

        simple_type = SimpleType()
        complex_type = ComplexType()
        enumeration = SimpleType(
            restriction=Restriction(enumerations=[Enumeration(value="a")])
        )

        element = Element(
            alternatives=[
                Alternative(complex_type=complex_type, id="a"),
                Alternative(simple_type=simple_type, id="b"),
                Alternative(simple_type=enumeration, id="c"),
            ]
        )
        result = SchemaMapper.build_inner_classes(element, "module", "target_ns")
        self.assertIsInstance(result, Iterator)
        self.assertEqual(inner_classes, list(result))
        self.assertEqual("a", complex_type.name)
        self.assertEqual("c", enumeration.name)

        mock_build_class.assert_has_calls(
            [
                mock.call(complex_type, Tag.ALTERNATIVE, "module", "target_ns"),
                mock.call(enumeration, Tag.ALTERNATIVE, "module", "target_ns"),
            ]
        )

    @mock.patch.object(SchemaMapper, "build_class")
    def test_build_inner_classes_with_enumeration(self, mock_build_class):
        inner = ClassFactory.enumeration(2)
        mock_build_class.return_value = inner

        enumeration = SimpleType(
            restriction=Restriction(enumerations=[Enumeration(value="a")])
        )

        result = SchemaMapper.build_inner_classes(enumeration, "module", "target_ns")
        self.assertIsInstance(result, Iterator)
        self.assertEqual([inner], list(result))
        self.assertIsNone(enumeration.name)

        mock_build_class.assert_called_once_with(
            enumeration, Tag.SIMPLE_TYPE, "module", "target_ns"
        )
