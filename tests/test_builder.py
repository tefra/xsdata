from pathlib import Path
from types import GeneratorType
from unittest.mock import call
from unittest.mock import patch
from unittest.mock import PropertyMock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.builder import ClassBuilder
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import Attribute
from xsdata.models.elements import AttributeGroup
from xsdata.models.elements import ComplexContent
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Enumeration
from xsdata.models.elements import Extension
from xsdata.models.elements import Group
from xsdata.models.elements import Override
from xsdata.models.elements import Redefine
from xsdata.models.elements import Restriction
from xsdata.models.elements import Schema
from xsdata.models.elements import Sequence
from xsdata.models.elements import SimpleContent
from xsdata.models.elements import SimpleType
from xsdata.models.elements import Union
from xsdata.models.enums import FormType


class ClassBuilderTests(FactoryTestCase):
    def setUp(self) -> None:
        super(ClassBuilderTests, self).setUp()
        self.schema = Schema.create(location=Path(__file__), target_namespace="builder")
        self.builder = ClassBuilder(schema=self.schema, package="tests")

    @patch.object(Redefine, "children")
    @patch.object(Override, "children")
    @patch.object(ClassBuilder, "build_class")
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
            [redefine_simple_type, redefine_group],
            [redefine_attribute_group],
        ]

        mock_override_children.side_effect = [
            [override_element, override_attribute],
            [override_complex_type],
        ]
        mock_build_class.side_effect = classes = ClassFactory.list(18)

        self.assertEqual(classes, self.builder.build())
        mock_build_class.assert_has_calls(
            [
                call(override_element),
                call(override_attribute),
                call(override_complex_type),
                call(redefine_simple_type),
                call(redefine_group),
                call(redefine_attribute_group),
                call(self.schema.simple_types[0]),
                call(self.schema.simple_types[1]),
                call(self.schema.attribute_groups[0]),
                call(self.schema.attribute_groups[1]),
                call(self.schema.groups[0]),
                call(self.schema.groups[1]),
                call(self.schema.attributes[0]),
                call(self.schema.attributes[1]),
                call(self.schema.complex_types[0]),
                call(self.schema.complex_types[1]),
                call(self.schema.elements[0]),
                call(self.schema.elements[1]),
            ]
        )

    def test_element_namespace(self):
        self.schema.target_namespace = "foobar"

        element = Element.create(ref="foo:something")
        element.nsmap["foo"] = "bar"

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

    @patch.object(ClassBuilder, "element_namespace")
    @patch.object(ClassBuilder, "build_class_attributes")
    @patch.object(ClassBuilder, "build_class_extensions")
    @patch.object(Element, "substitutions", new_callable=PropertyMock)
    @patch.object(Element, "is_abstract", new_callable=PropertyMock)
    @patch.object(Element, "is_nillable", new_callable=PropertyMock)
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
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
            nsmap=element.nsmap,
            package=self.builder.package,
            module=self.schema.module,
            source_namespace=self.schema.target_namespace,
            substitutions=["foo", "bar"],
        )
        self.assertEqual(expected, result)

    @patch.object(ClassBuilder, "children_extensions")
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

    @patch.object(ClassBuilder, "build_class_attribute_types")
    @patch.object(ClassBuilder, "element_namespace")
    @patch.object(Attribute, "get_restrictions")
    @patch.object(Attribute, "is_wildcard", new_callable=PropertyMock)
    @patch.object(Attribute, "is_fixed", new_callable=PropertyMock)
    @patch.object(Attribute, "default_value", new_callable=PropertyMock)
    @patch.object(Attribute, "prefix", new_callable=PropertyMock)
    @patch.object(Attribute, "display_help", new_callable=PropertyMock)
    @patch.object(Attribute, "real_name", new_callable=PropertyMock)
    def test_build_class_attribute(
        self,
        mock_real_name,
        mock_display_help,
        mock_prefix,
        mock_default_value,
        mock_is_fixed,
        mock_is_wildcard,
        mock_get_restrictions,
        mock_element_namespace,
        mock_build_class_attribute_types,
    ):
        item = ClassFactory.create(nsmap={"bar": "foo"})

        mock_build_class_attribute_types.return_value = AttrTypeFactory.list(
            1, name="xs:int"
        )
        mock_real_name.return_value = item.name
        mock_display_help.return_value = "sos"
        mock_prefix.return_value = "com"
        mock_default_value.return_value = "default"
        mock_is_fixed.return_value = True
        mock_is_wildcard.return_value = True
        mock_element_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"required": True}

        attribute = Attribute.create(default="false", index=66, nsmap={"foo": "bar"})

        self.builder.build_class_attribute(item, attribute, Restrictions())
        expected = AttrFactory.create(
            name=mock_real_name.return_value,
            types=mock_build_class_attribute_types.return_value,
            local_type=Attribute.__name__,
            namespace=mock_element_namespace.return_value,
            help=mock_display_help.return_value,
            default=mock_default_value.return_value,
            fixed=mock_is_fixed.return_value,
            wildcard=mock_is_wildcard.return_value,
            index=66,
            restrictions=Restrictions(required=True),
        )
        self.assertEqual(expected, item.attrs[0])
        self.assertEqual({"bar": "foo", "foo": "bar"}, item.nsmap)
        mock_build_class_attribute_types.assert_called_once_with(item, attribute)
        mock_element_namespace.assert_called_once_with(attribute)

    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(ClassBuilder, "build_inner_class")
    def test_build_class_attribute_types(self, mock_build_inner_class, mock_real_type):
        mock_real_type.return_value = " xs:integer  xs:string "
        mock_build_inner_class.return_value = None

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [AttrTypeFactory.xs_int(), AttrTypeFactory.xs_string()]

        self.assertEqual(expected, actual)

    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(ClassBuilder, "build_inner_class")
    def test_build_class_attribute_types_when_obj_has_inner_class(
        self, mock_build_inner_class, mock_real_type
    ):
        inner_class = ClassFactory.create(name="foo")
        mock_real_type.return_value = " xs:integer  xs:string "
        mock_build_inner_class.return_value = inner_class

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.xs_int(),
            AttrTypeFactory.xs_string(),
            AttrTypeFactory.create(name="foo", forward_ref=True),
        ]

        self.assertEqual(expected, actual)
        self.assertEqual([inner_class], item.inner)

    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(ClassBuilder, "build_inner_class")
    def test_build_class_attribute_types_when_obj_has_no_types(
        self, mock_build_inner_class, mock_real_type
    ):
        mock_real_type.return_value = None
        mock_build_inner_class.return_value = None

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66, name="attr")
        actual = self.builder.build_class_attribute_types(item, attribute)

        self.assertEqual(1, len(actual))
        self.assertEqual(AttrTypeFactory.xs_string(), actual[0])

    @patch.object(ClassBuilder, "build_class")
    @patch.object(ClassBuilder, "has_anonymous_class")
    def test_build_inner_class_when_has_anonymous_class(
        self, mock_has_anonymous_class, mock_build_class
    ):
        inner_class = ClassFactory.create()
        mock_build_class.return_value = inner_class
        mock_has_anonymous_class.return_value = True

        complex_type = ComplexType.create()
        element = Element.create(name="foo", complex_type=complex_type)

        self.assertEqual(inner_class, self.builder.build_inner_class(element))
        self.assertIsNone(element.complex_type)
        self.assertEqual("foo", complex_type.name)

    @patch.object(ClassBuilder, "build_class")
    @patch.object(ClassBuilder, "has_anonymous_enumeration")
    @patch.object(ClassBuilder, "has_anonymous_class")
    def test_build_inner_class_when_has_anonymous_enumeration(
        self, mock_has_anonymous_class, mock_has_anonymous_enumeration, mock_build_class
    ):
        inner_class = ClassFactory.create()
        mock_build_class.return_value = inner_class
        mock_has_anonymous_class.return_value = False
        mock_has_anonymous_enumeration.return_value = True

        simple_type = SimpleType.create()
        element = Element.create(name="foo", simple_type=simple_type, type="xs:int")

        self.assertEqual(inner_class, self.builder.build_inner_class(element))
        self.assertIsNone(element.simple_type)
        self.assertIsNone(element.type)
        self.assertEqual("foo", simple_type.name)

    @patch.object(ClassBuilder, "build_class")
    @patch.object(ClassBuilder, "has_anonymous_enumeration")
    @patch.object(ClassBuilder, "has_anonymous_class")
    def test_build_inner_class_when_is_anonymous_enumeration(
        self, mock_has_anonymous_class, mock_has_anonymous_enumeration, mock_build_class
    ):
        inner_class = ClassFactory.create()
        mock_build_class.return_value = inner_class
        mock_has_anonymous_class.return_value = False
        mock_has_anonymous_enumeration.return_value = False

        simple_type = SimpleType.create(restriction=Restriction.create())
        simple_type.restriction.enumerations.append(Enumeration.create())

        self.assertEqual(inner_class, self.builder.build_inner_class(simple_type))
        self.assertEqual("value", simple_type.name)
        self.assertIsNone(simple_type.restriction)

    @patch.object(ClassBuilder, "build_class")
    @patch.object(ClassBuilder, "has_anonymous_enumeration")
    @patch.object(ClassBuilder, "has_anonymous_class")
    def test_build_inner_class_when_union_has_anonymous_enumeration(
        self, mock_has_anonymous_class, mock_has_anonymous_enumeration, mock_build_class
    ):
        inner_class = ClassFactory.create()
        mock_build_class.return_value = inner_class
        mock_has_anonymous_class.return_value = False
        mock_has_anonymous_enumeration.return_value = False

        union = Union.create(name="foo", type="xs:int")
        simple_type_a = SimpleType.create(
            restriction=Restriction.create(enumerations=[Enumeration.create(value="a")])
        )
        simple_type_b = SimpleType.create(
            restriction=Restriction.create(enumerations=[Enumeration.create(value="b")])
        )
        union.simple_types = [simple_type_a, simple_type_b]

        self.assertEqual(inner_class, self.builder.build_inner_class(union))
        self.assertEqual([simple_type_a], union.simple_types)
        mock_build_class.assert_called_once_with(simple_type_b)

    def test_has_anonymous_class(self):
        obj = Element.create()
        self.assertFalse(self.builder.has_anonymous_class(obj))

        obj = Element.create(type="foo")
        self.assertFalse(self.builder.has_anonymous_class(obj))

        obj = Element.create(complex_type=ComplexType.create())
        self.assertTrue(self.builder.has_anonymous_class(obj))

        obj = Attribute.create()
        self.assertFalse(self.builder.has_anonymous_class(obj))

    def test_has_anonymous_enumeration(self):
        for clazz in [Element, Attribute]:
            obj = clazz.create()
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj = clazz.create(simple_type=SimpleType.create())
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj.simple_type.restriction = Restriction.create()
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj.simple_type.restriction.enumerations.append(Enumeration.create())
            self.assertTrue(self.builder.has_anonymous_enumeration(obj))

            obj.type = "foo"
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))
