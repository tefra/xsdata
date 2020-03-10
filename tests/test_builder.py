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
        self.builder = ClassBuilder(schema=self.schema)

    @patch.object(Redefine, "children")
    @patch.object(Override, "children")
    @patch.object(ClassBuilder, "build_class")
    def test_build(
        self, mock_build_class, mock_override_children, mock_redefine_children
    ):
        redefine = Redefine.create(
            simple_type=SimpleType.create(),
            complex_type=ComplexType.create(),
            group=Group.create(),
            attribute_group=AttributeGroup.create(),
        )
        self.builder = ClassBuilder(schema=self.schema, redefine=redefine)

        for _ in range(2):
            self.schema.simple_types.append(SimpleType.create())
            self.schema.attribute_groups.append(AttributeGroup.create())
            self.schema.groups.append(Group.create())
            self.schema.attributes.append(Attribute.create())
            self.schema.complex_types.append(ComplexType.create())
            self.schema.elements.append(Element.create())
            self.schema.redefines.append(
                Redefine.create(complex_type=ComplexType.create())
            )
            self.schema.overrides.append(Override.create())

        override_element = Element.create()
        override_attribute = Attribute.create()
        override_complex_type = ComplexType.create()
        redefine_simple_type = SimpleType.create()
        redefine_attribute_group = AttributeGroup.create()
        mock_redefine_children.return_value = [
            redefine_simple_type,
            redefine_attribute_group,
        ]

        mock_override_children.side_effect = [
            [override_element, override_attribute],
            [override_complex_type],
        ]
        mock_build_class.side_effect = classes = ClassFactory.list(17)

        self.assertEqual(classes, self.builder.build())
        mock_build_class.assert_has_calls(
            [
                call(override_element),
                call(override_attribute),
                call(override_complex_type),
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
                call(redefine_simple_type),
                call(redefine_attribute_group),
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
    @patch.object(Element, "is_abstract", new_callable=PropertyMock)
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class(
        self,
        mock_real_name,
        mock_display_help,
        mock_is_abstract,
        mock_build_class_extensions,
        mock_build_class_attributes,
        mock_element_namespace,
    ):
        mock_real_name.return_value = "name"
        mock_display_help.return_value = "sos"
        mock_is_abstract.return_value = True
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
            is_abstract=True,
            namespace="foo:name",
            nsmap=element.nsmap,
            module=self.schema.module,
            source_namespace=self.schema.target_namespace,
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
            type=some_type, restrictions=Restrictions(required=True)
        )

        item = ClassFactory.create()
        element = Element.create(type="something")
        self.builder.build_class_extensions(element, item)

        self.assertEqual(3, len(item.extensions))
        self.assertIs(double, item.extensions[0])
        self.assertIs(foo, item.extensions[1])
        self.assertEqual(self_ext, item.extensions[2])

    def test_element_children(self):
        complex_type = ComplexType.create(
            attributes=[Attribute.create(), Attribute.create()],
            sequence=Sequence.create(elements=[Element.create(), Element.create()]),
            simple_content=SimpleContent.create(restriction=Restriction.create()),
            complex_content=ComplexContent.create(
                restriction=Restriction.create(
                    enumerations=[Enumeration.create(value=x) for x in "abc"]
                )
            ),
        )

        children = self.builder.element_children(complex_type)
        expected = [
            complex_type.complex_content.restriction.enumerations[0],
            complex_type.complex_content.restriction.enumerations[1],
            complex_type.complex_content.restriction.enumerations[2],
            complex_type.sequence.elements[0],
            complex_type.sequence.elements[1],
            complex_type.attributes[0],
            complex_type.attributes[1],
        ]
        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    def test_children_extensions(self):
        complex_type = ComplexType.create(
            attributes=[Attribute.create(index=i) for i in range(2)],
            sequence=Sequence.create(
                groups=[
                    Group.create(ref="a", index=3, min_occurs=0),
                    Group.create(ref="bk:b", index=4, min_occurs=0),
                    Group.create(ref="c", index=5, min_occurs=0),
                ]
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
                    AttrTypeFactory.create(name="bk:ext", index=7),
                    AttrTypeFactory.create(name="a", index=3),
                    AttrTypeFactory.create(name="bk:b", index=4),
                    AttrTypeFactory.create(name="c", index=5),
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
        item = ClassFactory.create()

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

        attribute = Attribute.create(default="false", index=66)

        self.builder.build_class_attribute(item, attribute)
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
            nsmap=attribute.nsmap,
        )
        self.assertEqual(expected, item.attrs[0])
        mock_build_class_attribute_types.assert_called_once_with(item, attribute)
        mock_element_namespace.assert_called_once_with(attribute)

    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(ClassBuilder, "build_inner_class")
    def test_build_class_attribute_types(self, mock_build_inner_class, mock_real_type):
        mock_real_type.return_value = " xs:int  xs:string "
        mock_build_inner_class.return_value = None

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.create(name="int", native=True),
            AttrTypeFactory.create(name="string", native=True),
        ]

        self.assertEqual(expected, actual)

    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(ClassBuilder, "build_inner_class")
    def test_build_class_attribute_types_when_obj_has_inner_class(
        self, mock_build_inner_class, mock_real_type
    ):
        inner_class = ClassFactory.create(name="foo")
        mock_real_type.return_value = " xs:int  xs:string "
        mock_build_inner_class.return_value = inner_class

        item = ClassFactory.create()
        attribute = Attribute.create(default="false", index=66)
        actual = self.builder.build_class_attribute_types(item, attribute)

        expected = [
            AttrTypeFactory.create(name="int", native=True),
            AttrTypeFactory.create(name="string", native=True),
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
        expected = [AttrTypeFactory.create(name="string", native=True)]

        self.assertEqual(expected, actual)

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
