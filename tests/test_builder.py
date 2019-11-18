from types import GeneratorType
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock, call, patch

from xsdata.builder import ClassBuilder
from xsdata.models.codegen import Attr, Class
from xsdata.models.elements import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    Restriction,
    Schema,
    SimpleType,
)


class ClassBuilderTests(TestCase):
    def setUp(self) -> None:
        self.builder = ClassBuilder()

    @patch.object(ClassBuilder, "build_classes")
    @patch.object(ClassBuilder, "register_simple_types")
    def test_build(self, mock_register_simple_types, mock_build_classes):
        class_list = [Class(name="foo")]
        mock_build_classes.return_value = [Class(name="foo")]
        schema = Schema.create(simple_types=[SimpleType.create()])

        result = self.builder.build(schema)

        mock_register_simple_types.assert_called_once_with(schema.simple_types)
        self.assertEqual(class_list, result)

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "build_class")
    def test_register_simple_types(self, mock_build_class, mock_warning):
        class_list = [Class(name="a"), Class(name="a"), Class(name="b")]
        mock_build_class.side_effect = class_list

        simple_types = [SimpleType.create(name=x) for x in "aab"]
        schema = Schema.create(simple_types=simple_types)
        expected = {x.name: x for x in class_list}

        self.builder.register_simple_types(schema.simple_types)
        self.assertEqual(expected, self.builder.simple_types)
        mock_build_class.assert_has_calls(
            [call(item) for item in simple_types]
        )
        mock_warning.assert_called_once_with(
            "Name conflict for simple type: a"
        )

    @patch.object(ClassBuilder, "build_class")
    def test_build_classes(self, mock_build_class):
        attributes = [Attribute.create(name=name) for name in "ab"]
        attribute_groups = [AttributeGroup.create(name=name) for name in "cd"]
        complex_types = [ComplexType.create(name=name) for name in "ef"]
        elements = [Element.create(name=name) for name in "gh"]

        schema = Schema.create(
            attributes=attributes,
            attribute_groups=attribute_groups,
            complex_types=complex_types,
            elements=elements,
        )

        side_effect = [Class(name=x.name) for x in attributes]
        side_effect.extend([Class(name=x.name) for x in attribute_groups])
        side_effect.extend([Class(name=x.name) for x in complex_types])
        side_effect.extend([Class(name=x.name) for x in elements])
        mock_build_class.side_effect = side_effect

        calls = [call(x) for x in attributes]
        calls.extend([call(x) for x in attribute_groups])
        calls.extend([call(x) for x in complex_types])
        calls.extend([call(x) for x in elements])

        class_list = self.builder.build_classes(schema)
        self.assertEqual(side_effect, class_list)
        mock_build_class.assert_has_calls(calls)

    def test_find_simple_type(self):
        classes = {name: Class(name=name) for name in "ab"}
        self.builder.simple_types.update(classes)

        self.assertEqual(classes["a"], self.builder.find_simple_type("ref:a"))
        self.assertEqual(classes["a"], self.builder.find_simple_type("a"))
        self.assertIsNone(self.builder.find_simple_type("c"))

    @patch.object(ClassBuilder, "replace_simple_types", return_value=None)
    @patch.object(ClassBuilder, "build_class_attribute", return_value=None)
    @patch.object(ClassBuilder, "element_children")
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "extensions", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class(
        self,
        mock_real_name,
        mock_extensions,
        mock_display_help,
        mock_element_children,
        mock_build_class_attribute,
        mock_replace_simple_types,
    ):
        mock_real_name.return_value = "name"
        mock_extensions.return_value = ["foo", "bar"]
        mock_display_help.return_value = "sos"
        mock_element_children.return_value = [
            Attribute.create(name=x) for x in "ab"
        ]

        result = self.builder.build_class(Element.create())

        mock_build_class_attribute.assert_has_calls(
            [
                call(result, child)
                for child in mock_element_children.return_value
            ]
        )
        mock_replace_simple_types.assert_called_once_with(result)

        expected = Class(name="name", extensions=["foo", "bar"], help="sos")
        self.assertEqual(expected, result)

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "replace_simple_types", return_value=None)
    @patch.object(ClassBuilder, "build_class_attribute", return_value=None)
    @patch.object(ClassBuilder, "element_children")
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "extensions", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class_with_no_extensions_and_attributes(
        self,
        mock_real_name,
        mock_extensions,
        mock_display_help,
        mock_element_children,
        mock_build_class_attribute,
        mock_replace_simple_types,
        mock_warning,
    ):
        mock_real_name.return_value = "name"
        mock_extensions.return_value = []
        mock_display_help.return_value = "sos"
        mock_element_children.return_value = []

        element = Element.create()
        result = self.builder.build_class(element)

        mock_build_class_attribute.assert_not_called()
        mock_replace_simple_types.assert_not_called()
        mock_warning.assert_called_once_with("Empty class: `name`")

        expected = Class(name="name", help="sos")
        self.assertEqual(expected, result)

    def test_element_children_recursively_return_all_non_container_children(
        self,
    ):
        element_a = Element.create()
        element_b = Element.create()
        attribute_a = Attribute.create()
        attribute_b = Attribute.create()
        restriction = Restriction.create()
        complex_type = ComplexType.create()
        complex_type.children = MagicMock(
            return_value=[element_b, attribute_b]
        )

        input_element = Element.create()
        input_element.children = MagicMock(
            return_value=[element_a, attribute_a, complex_type, restriction]
        )

        children = self.builder.element_children(input_element)
        expected = [
            element_a,
            attribute_a,
            element_b,
            attribute_b,
            restriction,
        ]
        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "has_inner_type")
    @patch.object(Attribute, "get_restrictions")
    @patch.object(Attribute, "namespace", new_callable=PropertyMock)
    @patch.object(Attribute, "display_help", new_callable=PropertyMock)
    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(Attribute, "real_name", new_callable=PropertyMock)
    def test_build_class_attribute(
        self,
        mock_real_name,
        mock_real_type,
        mock_display_help,
        mock_namespace,
        mock_get_restrictions,
        has_inner_type,
        mock_warning,
    ):
        mock_real_name.return_value = "name"
        mock_real_type.return_value = "xs:int"
        mock_display_help.return_value = "sos"
        mock_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"required": True}
        has_inner_type.return_value = False

        item = Class(name="foo")
        attribute = Attribute.create(default="false")

        self.builder.build_class_attribute(item, attribute)
        expected = Attr(
            name=mock_real_name.return_value,
            type=mock_real_type.return_value,
            local_type=Attribute.__name__,
            namespace=mock_namespace.return_value,
            help=mock_display_help.return_value,
            forward_ref=False,
            restrictions=mock_get_restrictions.return_value,
            default="false",
        )
        self.assertEqual(expected, item.attrs[0])
        has_inner_type.assert_called_once_with(attribute)
        mock_warning.assert_not_called()

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "has_inner_type")
    @patch.object(Element, "real_type", new_callable=PropertyMock)
    def test_build_class_attribute_when_failed_to_detect_real_type(
        self, mock_real_type, has_inner_type, mock_warning,
    ):
        mock_real_type.return_value = None
        has_inner_type.return_value = False

        item = Class(name="foo")
        attribute = Element.create(name="foo", type="bar")
        self.builder.build_class_attribute(item, attribute)

        has_inner_type.assert_called_once_with(attribute)
        mock_warning.assert_called_once_with(
            "Failed to detect type for element: foo"
        )

    @patch.object(ClassBuilder, "build_inner_class")
    @patch.object(ClassBuilder, "has_inner_type")
    def test_build_class_attribute_with_inner_type(
        self, has_inner_type, build_inner_class,
    ):
        has_inner_type.return_value = True

        item = Class(name="foo")
        attribute = Attribute.create(ref="foo")
        self.builder.build_class_attribute(item, attribute)

        self.assertEqual(True, item.attrs[0].forward_ref)
        has_inner_type.assert_called_once_with(attribute)
        build_inner_class.assert_called_once_with(item, attribute)

    def test_has_inner_type(self):
        self.assertFalse(self.builder.has_inner_type(Element.create()))
        self.assertFalse(
            self.builder.has_inner_type(Element.create(type="foo"))
        )
        self.assertTrue(
            self.builder.has_inner_type(
                Element.create(complex_type=ComplexType.create())
            )
        )

        attribute = Attribute.create()
        self.assertFalse(self.builder.has_inner_type(attribute))

    @patch.object(ClassBuilder, "build_class")
    def test_build_inner_class(self, mock_build_class):

        mock_build_class.return_value = Class(name="inner")
        element = Element.create(name="foo", complex_type=ComplexType.create())
        parent = Class(name="parent")

        self.builder.build_inner_class(parent, element)
        self.assertEqual(mock_build_class.return_value, parent.inner[0])


class ClassBuilderReplaceSimpleTypesTests(TestCase):
    def setUp(self) -> None:
        self.builder = ClassBuilder()
        self.super_int = Class(
            name="SuperInt",
            attrs=[
                Attr(
                    name="number",
                    type="int",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                )
            ],
        )
        self.super_str = Class(
            name="SuperStr",
            attrs=[
                Attr(
                    name="text",
                    type="str",
                    restrictions={"required": True},
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                )
            ],
        )
        self.builder.simple_types = {
            "SuperInt": self.super_int,
            "SuperStr": self.super_str,
        }

    def test_add_class_attributes(self):
        item = Class(name="parent")
        item.extensions = ["SuperInt"]

        self.builder.replace_simple_types(item)
        self.assertEqual([], item.extensions)
        self.assertEqual(self.super_int.attrs[0], item.attrs[0])
        self.assertIsNot(self.super_int.attrs[0], item.attrs[0])

    def test_update_class_attributes(self):
        item = Class(
            name="parent",
            attrs=[
                Attr(
                    name="number",
                    type="SuperInt",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                    restrictions={"min": 1},
                ),
                Attr(
                    name="text",
                    type="SuperStr",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                    restrictions={"length": 3},
                ),
            ],
        )

        self.builder.replace_simple_types(item)
        self.assertEqual("int", item.attrs[0].type)
        self.assertEqual({"min": 1}, item.attrs[0].restrictions)
        self.assertEqual("str", item.attrs[1].type)
        self.assertEqual(
            {"length": 3, "required": True}, item.attrs[1].restrictions
        )

    def test_update_inner_classes(self):
        item = Class(
            name="parent",
            inner=[
                Class(name="foo", extensions=["SuperInt"]),
                Class(name="bar", extensions=["SuperStr"]),
            ],
        )

        self.builder.replace_simple_types(item)
        self.assertEqual([], item.extensions)
        self.assertEqual(self.super_int.attrs[0], item.inner[0].attrs[0])
        self.assertIsNot(self.super_int.attrs[0], item.inner[1].attrs[0])
