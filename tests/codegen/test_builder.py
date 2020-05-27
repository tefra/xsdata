from types import GeneratorType
from typing import Iterator
from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.builder import ClassBuilder
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import FormType
from xsdata.models.enums import Tag
from xsdata.models.xsd import Alternative
from xsdata.models.xsd import Annotation
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import AttributeGroup
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


class ClassBuilderTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.schema = Schema.create(location="file://foo.xsd")
        self.builder = ClassBuilder(schema=self.schema)

    @mock.patch.object(Redefine, "children")
    @mock.patch.object(Override, "children")
    @mock.patch.object(ClassBuilder, "build_class")
    def test_build(
        self, mock_build_class, mock_override_children, mock_redefine_children
    ):

        for _ in range(2):
            self.schema.simple_types.append(SimpleType.create())
            self.schema.attribute_groups.append(AttributeGroup.create())
            self.schema.groups.append(Group.create())
            self.schema.attributes.append(Attribute.create())
            self.schema.complex_types.append(ComplexType.create())
            self.schema.elements.append(Element.create())
            self.schema.redefines.append(Redefine.create())
            self.schema.overrides.append(Override.create())

        override_element = Element.create()
        override_attribute = Attribute.create()
        override_complex_type = ComplexType.create()
        redefine_simple_type = SimpleType.create()
        redefine_group = Group.create()
        redefine_attribute_group = AttributeGroup.create()
        mock_redefine_children.side_effect = [
            [redefine_simple_type, redefine_group, Annotation.create()],
            [redefine_attribute_group, Annotation.create()],
        ]

        mock_override_children.side_effect = [
            [override_element, Annotation.create(), override_attribute],
            [Annotation.create(), override_complex_type],
        ]
        mock_build_class.side_effect = classes = ClassFactory.list(18)

        self.assertEqual(classes, self.builder.build())
        mock_build_class.assert_has_calls(
            [
                mock.call(override_element),
                mock.call(override_attribute),
                mock.call(override_complex_type),
                mock.call(redefine_simple_type),
                mock.call(redefine_group),
                mock.call(redefine_attribute_group),
                mock.call(self.schema.simple_types[0]),
                mock.call(self.schema.simple_types[1]),
                mock.call(self.schema.attribute_groups[0]),
                mock.call(self.schema.attribute_groups[1]),
                mock.call(self.schema.groups[0]),
                mock.call(self.schema.groups[1]),
                mock.call(self.schema.attributes[0]),
                mock.call(self.schema.attributes[1]),
                mock.call(self.schema.complex_types[0]),
                mock.call(self.schema.complex_types[1]),
                mock.call(self.schema.elements[0]),
                mock.call(self.schema.elements[1]),
            ]
        )

    def test_element_namespace(self):
        self.schema.target_namespace = "foobar"

        element = Element.create(ref="foo:something")
        element.ns_map["foo"] = "bar"

        self.assertEqual("bar", self.builder.element_namespace(element))

        element = Element.create(form=FormType.QUALIFIED)
        self.assertEqual("foobar", self.builder.element_namespace(element))

        element = Element.create()
        self.assertEqual("", self.builder.element_namespace(element))

        element.target_namespace = "tns"
        self.assertEqual("tns", self.builder.element_namespace(element))

        attribute = Attribute.create()
        self.assertIsNone(self.builder.element_namespace(attribute))

        attribute.target_namespace = "tns"
        self.assertEqual("tns", self.builder.element_namespace(attribute))

    @mock.patch.object(ClassBuilder, "element_namespace")
    @mock.patch.object(ClassBuilder, "build_class_attributes")
    @mock.patch.object(ClassBuilder, "build_class_extensions")
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
        mock_substitutions.return_value = ["foo", "bar"]
        mock_element_namespace.return_value = "foo:name"

        element = Element.create()
        result = self.builder.build_class(element)

        mock_build_class_attributes.assert_called_once_with(element, result)
        mock_build_class_extensions.assert_called_once_with(element, result)
        mock_element_namespace.assert_called_once_with(element)

        expected = ClassFactory.create(
            name="name",
            type=Element,
            help="sos",
            abstract=True,
            nillable=True,
            namespace="foo:name",
            ns_map=element.ns_map,
            package=None,
            module=self.schema.module,
            source_namespace=self.schema.target_namespace,
            substitutions=["foo", "bar"],
        )
        self.assertEqual(expected, result)

    @mock.patch.object(ClassBuilder, "children_extensions")
    def test_build_class_extensions(self, mock_children_extensions):
        bar_type = AttrTypeFactory.create(name="bar", index=3)
        foo_type = AttrTypeFactory.create(name="foo", index=1)
        some_type = AttrTypeFactory.create(name="something", index=0)

        bar = ExtensionFactory.create(type=bar_type)
        double = ExtensionFactory.create(type=bar_type)
        foo = ExtensionFactory.create(type=foo_type)

        mock_children_extensions.return_value = [bar, double, foo]
        self_ext = ExtensionFactory.create(
            type=some_type, restrictions=Restrictions(min_occurs=1, max_occurs=1)
        )

        item = ClassFactory.create()
        element = Element.create(type="something")
        self.builder.build_class_extensions(element, item)

        self.assertEqual(3, len(item.extensions))
        self.assertEqual(self_ext, item.extensions[0])
        self.assertIs(foo, item.extensions[1])
        self.assertIs(double, item.extensions[2])

    def test_element_children(self):
        sequence_one = Sequence.create(elements=[Element.create(), Element.create()])
        sequence_two = Sequence.create(
            max_occurs=2, elements=[Element.create(), Element.create()]
        )
        restriction = Restriction.create(
            enumerations=[Enumeration.create(value=x) for x in "abc"],
            sequence=sequence_two,
        )
        complex_type = ComplexType.create(
            attributes=[Attribute.create(), Attribute.create()],
            sequence=sequence_one,
            simple_content=SimpleContent.create(restriction=Restriction.create()),
            complex_content=ComplexContent.create(restriction=restriction,),
        )

        children = self.builder.element_children(complex_type)
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

    def test_children_extensions(self):
        complex_type = ComplexType.create(
            attributes=[Attribute.create(index=i) for i in range(2)],
            simple_content=SimpleContent.create(
                restriction=Restriction.create(base="bk:b", index=4)
            ),
            complex_content=ComplexContent.create(
                extension=Extension.create(base="bk:ext", index=7)
            ),
        )

        item = ClassFactory.create()
        children = self.builder.children_extensions(complex_type, item)
        expected = list(
            map(
                ExtensionFactory.create,
                [
                    AttrTypeFactory.create(name="bk:b", index=4),
                    AttrTypeFactory.create(name="bk:ext", index=7),
                ],
            )
        )

        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    @mock.patch.object(ClassBuilder, "build_class_attribute_types")
    @mock.patch.object(ClassBuilder, "element_namespace")
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
            1, name="xs:int"
        )
        mock_real_name.return_value = item.name
        mock_display_help.return_value = "sos"
        mock_prefix.return_value = "com"
        mock_default_value.return_value = "default"
        mock_is_fixed.return_value = True
        mock_element_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"required": True}

        attribute = Attribute.create(default="false", index=66, ns_map={"foo": "bar"})

        self.builder.build_class_attribute(item, attribute, Restrictions())
        expected = AttrFactory.create(
            name=mock_real_name.return_value,
            types=mock_build_class_attribute_types.return_value,
            tag=Tag.ATTRIBUTE,
            namespace=mock_element_namespace.return_value,
            help=mock_display_help.return_value,
            default=mock_default_value.return_value,
            fixed=mock_is_fixed.return_value,
            index=66,
            restrictions=Restrictions(required=True),
        )
        self.assertEqual(expected, item.attrs[0])
        self.assertEqual({"bar": "foo", "foo": "bar"}, item.ns_map)
        mock_build_class_attribute_types.assert_called_once_with(item, attribute)
        mock_element_namespace.assert_called_once_with(attribute)

    @mock.patch.object(Attribute, "real_type", new_callable=mock.PropertyMock)
    @mock.patch.object(ClassBuilder, "build_inner_classes")
    def test_build_class_attribute_types(
        self, mock_build_inner_classes, mock_real_type
    ):
        mock_real_type.return_value = " xs:integer  xs:string "
        mock_build_inner_classes.return_value = []

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [AttrTypeFactory.xs_int(), AttrTypeFactory.xs_string()]

        self.assertEqual(expected, actual)

    @mock.patch.object(Attribute, "real_type", new_callable=mock.PropertyMock)
    @mock.patch.object(ClassBuilder, "build_inner_classes")
    def test_build_class_attribute_types_when_obj_has_inner_class(
        self, mock_build_inner_classes, mock_real_type
    ):
        inner_class = ClassFactory.create(name="foo")
        mock_real_type.return_value = " xs:integer  xs:string "
        mock_build_inner_classes.return_value = [inner_class]

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.xs_int(),
            AttrTypeFactory.xs_string(),
            AttrTypeFactory.create(name="foo", forward=True),
        ]

        self.assertEqual(expected, actual)
        self.assertEqual([inner_class], item.inner)

    @mock.patch.object(Attribute, "default_type", new_callable=mock.PropertyMock)
    @mock.patch.object(Attribute, "real_type", new_callable=mock.PropertyMock)
    @mock.patch.object(ClassBuilder, "build_inner_classes")
    def test_build_class_attribute_types_when_obj_has_no_types(
        self, mock_build_inner_classes, mock_real_type, mock_default_type
    ):
        mock_real_type.return_value = None
        mock_build_inner_classes.return_value = []
        mock_default_type.return_value = DataType.STRING

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66, name="attr")
        actual = self.builder.build_class_attribute_types(item, attribute)

        self.assertEqual(1, len(actual))
        self.assertEqual(AttrTypeFactory.xs_string(), actual[0])

    @mock.patch.object(ClassBuilder, "build_class")
    def test_build_inner_classes(self, mock_build_class):
        inner_classes = ClassFactory.list(2)
        mock_build_class.side_effect = inner_classes

        simple_type = SimpleType.create()
        complex_type = ComplexType.create()
        enumeration = SimpleType.create(
            restriction=Restriction.create(enumerations=[Enumeration.create(value="a")])
        )

        element = Element.create(
            alternatives=[
                Alternative.create(complex_type=complex_type, id="a"),
                Alternative.create(simple_type=simple_type, id="b"),
                Alternative.create(simple_type=enumeration, id="c"),
            ]
        )
        result = self.builder.build_inner_classes(element)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(inner_classes, list(result))
        self.assertEqual("a", complex_type.name)
        self.assertEqual("c", enumeration.name)

        mock_build_class.assert_has_calls(
            [mock.call(complex_type), mock.call(enumeration)]
        )

    @mock.patch.object(ClassBuilder, "build_class")
    def test_build_inner_classes_with_enumeration(self, mock_build_class):
        inner = ClassFactory.enumeration(2)
        mock_build_class.return_value = inner

        enumeration = SimpleType.create(
            restriction=Restriction.create(enumerations=[Enumeration.create(value="a")])
        )

        result = self.builder.build_inner_classes(enumeration)
        self.assertIsInstance(result, Iterator)
        self.assertEqual([inner], list(result))
        self.assertIsNone(enumeration.name)
