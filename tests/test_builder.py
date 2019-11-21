from types import GeneratorType
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock, call, patch

from lxml import etree

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
    @patch.object(ClassBuilder, "add_common_types")
    def test_build(self, mock_add_common_types, mock_build_classes):
        class_list = [Class(name="foo")]
        mock_build_classes.return_value = [Class(name="foo")]
        schema = Schema.create()

        result = self.builder.build(schema)

        mock_add_common_types.assert_called_once_with(schema)
        self.assertEqual(class_list, result)

    @patch.object(ClassBuilder, "flatten_common_types")
    @patch.object(ClassBuilder, "build_class")
    def test_add_common_types(
        self, mock_build_class, mock_flatten_common_types
    ):
        class_list = [Class(name=x) for x in "abcd"]
        mock_build_class.side_effect = class_list
        mock_flatten_common_types.side_effect = lambda x, y: x

        schema = Schema.create(
            nsmap={"other": "http://namespace/other"},
            target_namespace="http://namespace/common",
            simple_types=[SimpleType.create(name=x) for x in "ab"],
            attribute_groups=[AttributeGroup.create(name=x) for x in "cd"],
        )
        self.builder.add_common_types(schema)

        expected = {
            etree.QName(schema.target_namespace, obj.name).text: obj
            for obj in class_list
        }
        self.assertEqual(expected, self.builder.common_types)

        mock_build_class.assert_has_calls(
            [call(item) for item in schema.simple_types]
            + [call(item) for item in schema.attribute_groups]
        )
        mock_flatten_common_types.assert_has_calls(
            [call(obj, schema.nsmap) for obj in class_list]
        )

    @patch.object(ClassBuilder, "flatten_common_types")
    @patch.object(ClassBuilder, "build_class")
    def test_build_classes(self, mock_build_class, mock_flatten_common_types):
        attributes = [Attribute.create(name=name) for name in "ab"]
        attribute_groups = [AttributeGroup.create(name=name) for name in "cd"]
        complex_types = [ComplexType.create(name=name) for name in "ef"]
        elements = [Element.create(name=name) for name in "gh"]

        schema = Schema.create(
            nsmap={None: "http://namespace/target"},
            attributes=attributes,
            attribute_groups=attribute_groups,
            complex_types=complex_types,
            elements=elements,
        )

        side_effect = [Class(name=x.name) for x in attributes]
        side_effect.extend([Class(name=x.name) for x in complex_types])
        side_effect.extend([Class(name=x.name) for x in elements])
        mock_build_class.side_effect = side_effect

        calls = [call(x) for x in attributes]
        calls.extend([call(x) for x in complex_types])
        calls.extend([call(x) for x in elements])

        class_list = self.builder.build_classes(schema)
        self.assertEqual(side_effect, class_list)
        mock_build_class.assert_has_calls(calls)
        mock_flatten_common_types.assert_has_calls(
            [call(x, schema.nsmap) for x in side_effect]
        )

    def test_find_common_type(self):
        nsmap = {
            None: "http://namespace/target",
            "other": "http://namespace/other",
        }

        self.builder.common_types.update(
            {etree.QName(nsmap[None], x).text: Class(name=x) for x in "ab"}
        )
        self.builder.common_types.update(
            {etree.QName(nsmap["other"], x).text: Class(name=x) for x in "cd"}
        )

        common_keys = list(self.builder.common_types.keys())
        common_values = list(self.builder.common_types.values())

        actual = self.builder.find_common_type("a", nsmap)
        self.assertEqual(0, common_values.index(actual))
        self.assertEqual("{http://namespace/target}a", common_keys[0])

        self.assertIsNone(self.builder.find_common_type("d", nsmap))
        actual = self.builder.find_common_type("other:d", nsmap)
        self.assertEqual(3, common_values.index(actual))
        self.assertEqual("{http://namespace/other}d", common_keys[3])

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

        expected = Class(name="name", extensions=["foo", "bar"], help="sos")
        self.assertEqual(expected, result)

    @patch("xsdata.builder.logger.warning")
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
        mock_warning,
    ):
        mock_real_name.return_value = "name"
        mock_extensions.return_value = []
        mock_display_help.return_value = "sos"
        mock_element_children.return_value = []

        element = Element.create()
        result = self.builder.build_class(element)

        mock_build_class_attribute.assert_not_called()
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


class ClassBuilderFlattenCommonTypesTests(TestCase):
    def setUp(self) -> None:
        self.builder = ClassBuilder()
        self.nsmap = {
            None: "http://namespace/target",
            "other": "http://namespace/other",
        }
        self.super_int = Class(
            name="SuperInt",
            attrs=[
                Attr(
                    name="number",
                    type="int",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                ),
                Attr(
                    name="decimals",
                    type="int",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                ),
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
        self.super_float = Class(
            name="SuperFloat",
            attrs=[
                Attr(
                    name="text",
                    type="float",
                    restrictions={},
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                )
            ],
        )

        self.builder.common_types = {
            "{http://namespace/target}SuperInt": self.super_int,
            "{http://namespace/target}SuperFloat": self.super_float,
            "{http://namespace/other}SuperStr": self.super_str,
        }

    def test_add_class_attributes(self):
        item = Class(name="parent")
        item.extensions = ["SuperInt"]

        self.builder.flatten_common_types(item, nsmap=self.nsmap)
        self.assertEqual([], item.extensions)
        self.assertEqual(self.super_int.attrs, item.attrs)
        self.assertIsNot(self.super_int.attrs[0], item.attrs[0])
        self.assertIsNot(self.super_int.attrs[1], item.attrs[1])

    def test_update_class_attributes(self):
        item = Class(
            name="parent",
            attrs=[
                Attr(
                    name="text",
                    type="SuperFloat",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                    restrictions={"fraction_digits": 3},
                ),
                Attr(
                    name="text",
                    type="other:SuperStr",
                    local_type="Attribute",
                    help=None,
                    namespace=None,
                    restrictions={"length": 3},
                ),
            ],
        )

        self.builder.flatten_common_types(item, nsmap=self.nsmap)
        self.assertEqual("float", item.attrs[0].type)
        self.assertEqual({"fraction_digits": 3}, item.attrs[0].restrictions)
        self.assertEqual("str", item.attrs[1].type)
        self.assertEqual(
            {"length": 3, "required": True}, item.attrs[1].restrictions
        )

    def test_update_inner_classes(self):
        item = Class(
            name="parent",
            inner=[
                Class(name="foo", extensions=["SuperInt"]),
                Class(name="bar", extensions=["other:SuperStr"]),
            ],
        )

        self.builder.flatten_common_types(item, nsmap=self.nsmap)
        self.assertEqual([], item.extensions)
        self.assertEqual(self.super_int.attrs[0], item.inner[0].attrs[0])
        self.assertIsNot(self.super_int.attrs[0], item.inner[1].attrs[0])
