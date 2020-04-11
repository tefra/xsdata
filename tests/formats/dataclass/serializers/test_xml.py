from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter12.chapter12 import DescriptionType
from tests.fixtures.defxmlschema.chapter12.chapter12 import ProductType
from tests.fixtures.defxmlschema.chapter12.chapter12 import SizeType
from xsdata.exceptions import ModelInspectionError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.utils import SerializeUtils


class XmlSerializerTests(TestCase):
    def setUp(self):
        super(XmlSerializerTests, self).setUp()
        self.serializer = XmlSerializer(pretty_print=True)
        self.namespaces = Namespaces()
        self.books = Books(
            book=[
                BookForm(
                    id="bk001",
                    author="Hightower, Kim",
                    title="The First Book",
                    genre="Fiction",
                    price=44.95,
                    pub_date="2000-10-01",
                    review="An amazing story of nothing.",
                ),
                BookForm(
                    id="bk002",
                    author="Nagata, Suanne",
                    title="Becoming Somebody",
                    genre="Biography",
                    review="A masterpiece of the fine art of gossiping.",
                ),
            ]
        )

    def test_render(self):
        actual = self.serializer.render(self.books)

        expected = (
            "<?xml version='1.0' encoding='UTF-8'?>\n"
            '<ns0:books xmlns:ns0="urn:books">\n'
            '  <book id="bk001" lang="en">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002" lang="en">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</ns0:books>\n"
        )
        self.assertEqual(expected, actual)

    def test_render_with_provided_namespaces(self):
        self.namespaces.add("urn:books", "burn")
        actual = self.serializer.render(self.books, self.namespaces)

        expected = (
            "<?xml version='1.0' encoding='UTF-8'?>\n"
            '<burn:books xmlns:burn="urn:books">\n'
            '  <book id="bk001" lang="en">\n'
            "    <author>Hightower, Kim</author>\n"
            "    <title>The First Book</title>\n"
            "    <genre>Fiction</genre>\n"
            "    <price>44.95</price>\n"
            "    <pub_date>2000-10-01</pub_date>\n"
            "    <review>An amazing story of nothing.</review>\n"
            "  </book>\n"
            '  <book id="bk002" lang="en">\n'
            "    <author>Nagata, Suanne</author>\n"
            "    <title>Becoming Somebody</title>\n"
            "    <genre>Biography</genre>\n"
            "    <review>A masterpiece of the fine art of gossiping.</review>\n"
            "  </book>\n"
            "</burn:books>\n"
        )
        self.assertEqual(expected, actual)

    def test_render_no_dataclass(self):
        with self.assertRaises(ModelInspectionError) as cm:
            self.serializer.render(self)
        self.assertEqual(
            f"Object {self.__class__} is not a dataclass.", str(cm.exception)
        )

    @mock.patch.object(SerializeUtils, "set_nil_attribute")
    @mock.patch.object(SerializeUtils, "set_text")
    @mock.patch.object(SerializeUtils, "set_attributes")
    @mock.patch.object(SerializeUtils, "set_attribute")
    @mock.patch.object(XmlSerializer, "render_sub_node")
    @mock.patch.object(XmlSerializer, "next_value")
    def test_render_node(
        self,
        mock_next_value,
        mock_render_sub_node,
        mock_set_attribute,
        mock_set_attributes,
        mock_set_text,
        mock_set_nil_attribute,
    ):
        root = Element("root")
        prod_meta = self.serializer.class_meta(ProductType)
        size_meta = self.serializer.class_meta(SizeType)
        obj = ProductType()

        attribute = prod_meta.find_var("effDate")
        attributes = prod_meta.find_var("{!}other_attributes")
        text = replace(size_meta.find_var("value"), qname=QName("foo", "bar"))
        sub_node = prod_meta.find_var("name")

        mock_next_value.return_value = [
            (attribute, None),
            (attribute, 1),
            (attributes, dict(a=1)),
            (text, "txt"),
            (sub_node, 1),
            (sub_node, [2, 3]),
        ]

        self.serializer.render_node(obj, root, self.namespaces)
        self.assertEqual({"ns0": "foo"}, self.namespaces.ns_map)
        mock_set_attribute.assert_called_once_with(
            root, attribute.qname, 1, self.namespaces
        )
        mock_set_attributes.assert_called_once_with(root, dict(a=1), self.namespaces)
        mock_set_text.assert_called_once_with(root, "txt", self.namespaces)
        mock_render_sub_node.assert_has_calls(
            [
                mock.call(root, 1, sub_node, self.namespaces),
                mock.call(root, 2, sub_node, self.namespaces),
                mock.call(root, 3, sub_node, self.namespaces),
            ]
        )
        mock_set_nil_attribute.assert_called_once_with(root, False, self.namespaces)

    def test_render_node_without_dataclass(self):
        root = Element("root")
        self.serializer.render_node(1, root, self.namespaces)
        self.assertEqual("1", root.text)

    @mock.patch.object(XmlSerializer, "render_sub_node")
    def test_render_sub_nodes(self, mock_render_sub_node):
        root = Element("root")
        meta = self.serializer.class_meta(ProductType)
        var = meta.find_var("number")

        self.serializer.render_sub_nodes(root, [1, 2, 3], var, self.namespaces)
        self.assertEqual(3, mock_render_sub_node.call_count)
        mock_render_sub_node.assert_has_calls(
            [
                mock.call(root, 1, var, self.namespaces),
                mock.call(root, 2, var, self.namespaces),
                mock.call(root, 3, var, self.namespaces),
            ]
        )

    @mock.patch.object(XmlSerializer, "render_wildcard_node")
    def test_render_sub_node_with_generic_object(self, mock_render_wildcard_node):
        root = Element("root")
        value = AnyElement()
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_sub_node(root, value, var, self.namespaces)
        self.assertEqual(1, mock_render_wildcard_node.call_count)
        mock_render_wildcard_node.assert_called_once_with(
            root, value, var, self.namespaces
        )

    @mock.patch.object(XmlSerializer, "render_element_node")
    def test_render_sub_node_with_xml_element(self, mock_render_element_node):
        root = Element("root")
        value = 1
        meta = self.serializer.class_meta(ProductType)
        var = meta.find_var("number")

        self.serializer.render_sub_node(root, value, var, self.namespaces)
        self.assertEqual(1, mock_render_element_node.call_count)
        mock_render_element_node.assert_called_once_with(
            root, value, var, self.namespaces
        )

    @mock.patch.object(XmlSerializer, "render_element_node")
    def test_render_sub_node_with_dataclass_object(self, mock_render_element_node):
        root = Element("root")
        value = SizeType()
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_sub_node(root, value, var, self.namespaces)
        self.assertEqual(1, mock_render_element_node.call_count)
        mock_render_element_node.assert_called_once_with(
            root, value, var, self.namespaces
        )

    @mock.patch.object(SerializeUtils, "set_tail")
    @mock.patch.object(SerializeUtils, "set_text")
    def test_render_sub_node_with_primitive_value_and_not_xml_element(
        self, mock_set_text, mock_set_tail
    ):
        root = Element("root")
        value = 1
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_sub_node(root, value, var, self.namespaces)
        self.assertEqual(1, mock_set_text.call_count)
        mock_set_text.assert_called_once_with(root, value, self.namespaces)

        root.text = "foo"
        self.serializer.render_sub_node(root, value, var, self.namespaces)
        self.assertEqual(1, mock_set_tail.call_count)
        mock_set_tail.assert_called_once_with(root, value, self.namespaces)

    @mock.patch.object(SerializeUtils, "set_nil_attribute")
    @mock.patch.object(XmlSerializer, "render_node")
    def test_render_element_node(self, mock_render_node, mock_set_nil_attribute):
        root = Element("root")
        value = SizeType()
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_element_node(root, value, var, self.namespaces)

        child = root[0]
        mock_render_node.assert_called_once_with(value, child, self.namespaces)
        mock_set_nil_attribute.assert_called_once_with(
            child, var.nillable, self.namespaces
        )

        self.assertEqual(var.qname, child.tag)
        self.assertEqual(
            {"ns0": "http://www.w3.org/1999/xhtml"}, self.namespaces.ns_map
        )

    @mock.patch.object(SerializeUtils, "set_nil_attribute")
    @mock.patch.object(XmlSerializer, "render_node")
    def test_render_element_node_with_specific_qname(
        self, mock_render_node, mock_set_nil_attribute
    ):
        root = Element("root")
        value = SizeType()
        value.qname = "foo"
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_element_node(root, value, var, self.namespaces)

        child = root[0]
        mock_render_node.assert_called_once_with(value, child, self.namespaces)
        mock_set_nil_attribute.assert_called_once_with(
            child, var.nillable, self.namespaces
        )

        self.assertEqual("foo", child.tag)
        self.assertEqual(0, len(self.namespaces.ns_map))

    @mock.patch.object(XmlSerializer, "render_sub_node")
    @mock.patch.object(SerializeUtils, "set_nil_attribute")
    @mock.patch.object(SerializeUtils, "set_attributes")
    @mock.patch.object(SerializeUtils, "set_tail")
    @mock.patch.object(SerializeUtils, "set_text")
    def test_render_wildcard_node(
        self,
        mock_set_text,
        mock_set_tail,
        mock_set_attributes,
        mock_set_nil_attribute,
        mock_render_sub_node,
    ):
        root = Element("root")
        value = AnyElement(
            text="foo",
            tail="bar",
            attributes=dict(a=1),
            children=[AnyElement(), AnyElement()],
            ns_map={"foo": "bar"},
            qname="foo",
        )
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_wildcard_node(root, value, var, self.namespaces)

        child = root[0]
        self.assertEqual({"foo": "bar"}, self.namespaces.ns_map)
        self.assertEqual(value.qname, child.tag)

        mock_set_text.assert_called_once_with(child, value.text, self.namespaces)
        mock_set_tail.assert_called_once_with(child, value.tail, self.namespaces)
        mock_set_attributes.assert_called_once_with(
            child, value.attributes, self.namespaces
        )
        mock_render_sub_node.assert_has_calls(
            [
                mock.call(child, value.children[0], var, self.namespaces),
                mock.call(child, value.children[1], var, self.namespaces),
            ]
        )
        mock_set_nil_attribute.assert_called_once_with(
            child, var.nillable, self.namespaces
        )

    @mock.patch.object(XmlSerializer, "render_sub_node")
    @mock.patch.object(SerializeUtils, "set_nil_attribute")
    @mock.patch.object(SerializeUtils, "set_attributes")
    @mock.patch.object(SerializeUtils, "set_tail")
    @mock.patch.object(SerializeUtils, "set_text")
    def test_render_wildcard_node_without_qname(
        self,
        mock_set_text,
        mock_set_tail,
        mock_set_attributes,
        mock_set_nil_attribute,
        mock_render_sub_node,
    ):
        root = Element("root")
        value = AnyElement(
            text="foo", tail="bar", attributes=dict(a=1), children=[AnyElement()]
        )
        meta = self.serializer.class_meta(DescriptionType)
        var = meta.any_element

        self.serializer.render_wildcard_node(root, value, var, self.namespaces)

        self.assertEqual(0, len(self.namespaces.ns_map))
        self.assertEqual(0, len(root))

        mock_set_text.assert_called_once_with(root, value.text, self.namespaces)
        mock_set_tail.assert_called_once_with(root, value.tail, self.namespaces)
        mock_set_attributes.assert_called_once_with(
            root, value.attributes, self.namespaces
        )
        mock_render_sub_node.assert_called_once_with(
            root, value.children[0], var, self.namespaces
        )
        mock_set_nil_attribute.assert_called_once_with(
            root, var.nillable, self.namespaces
        )
