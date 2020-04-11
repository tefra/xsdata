from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter08.example0803 import DressSize
from tests.fixtures.defxmlschema.chapter12.chapter12 import ProductType
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace


class ParserUtilsTests(TestCase):
    def setUp(self) -> None:
        self.ctx = ModelContext()

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value(self, mock_to_python):
        self.assertEqual(1, ParserUtils.parse_value([int], None, 1))
        self.assertIsNone(ParserUtils.parse_value([int], None, lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value([int], "1", None))
        mock_to_python.assert_called_once_with([int], "1", None)

    def test_parse_value_with_is_list_true(self):
        actual = ParserUtils.parse_value([int], " 1 2 3", list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value([int], ["1", "2", "3"], list, None, True)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
        ParserUtils.parse_value([int], " 1 2 3", list, ns_map, True)
        ParserUtils.parse_value([str], " 1 2 3", None, ns_map, False)

        mock_to_python.assert_has_calls(
            [
                mock.call([int], "1", ns_map),
                mock.call([int], "2", ns_map),
                mock.call([int], "3", ns_map),
                mock.call([str], " 1 2 3", ns_map),
            ]
        )

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_element_attrs(self, mock_parse_value):
        mock_parse_value.return_value = "2020-03-02"
        metadata = self.ctx.class_meta(ProductType)
        eff_date = metadata.find_var("effDate")
        element = Element("foo")
        element.set("effDate", "2020-03-01")
        element.set("whatever", "foo")

        params = dict()
        ParserUtils.bind_element_attrs(params, metadata, element)
        expected = {"eff_date": "2020-03-02", "other_attributes": {"whatever": "foo"}}
        self.assertEqual(expected, params)
        mock_parse_value.assert_called_once_with(
            eff_date.types,
            "2020-03-01",
            eff_date.default,
            element.nsmap,
            eff_date.is_list,
        )

    def test_bind_elements_attrs_ignore_init_false_vars(self):
        metadata = self.ctx.class_meta(ProductType)
        eff_date = metadata.find_var("effDate")
        metadata.vars.remove(eff_date)
        metadata.vars.append(replace(eff_date, init=False))

        element = Element("foo")
        element.set("effDate", "2020-03-01")

        params = dict()
        ParserUtils.bind_element_attrs(params, metadata, element)
        self.assertEqual({}, params)

    def test_bind_element_text_with_no_text_var(self):
        element = Element("foo")
        element.text = "foo"

        params = dict()
        metadata = self.ctx.class_meta(Books)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_element_text_with_text_var(self, mock_parse_value):
        element = Element("foo")
        params = dict()
        metadata = self.ctx.class_meta(DressSize)
        var = metadata.any_text
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

        element.text = "foo"
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            metadata.any_text.types,
            element.text,
            metadata.any_text.default,
            element.nsmap,
            var.is_list,
        )

    def test_parse_any_element(self):
        element = Element("foo")
        element.set("a", "1")
        element.set("b", "2")
        element.set(
            QName(Namespace.XSI.uri, "type").text, QName(Namespace.XS.uri, "float").text
        )
        element.text = "yes"
        element.tail = "no"

        actual = ParserUtils.parse_any_element(element)
        expected = AnyElement(
            qname=element.tag,
            text="yes",
            tail="no",
            attributes={
                "a": "1",
                "b": "2",
                QName(Namespace.XSI.uri, "type"): QName(Namespace.XS.uri, "float"),
            },
            ns_map=element.nsmap,
        )
        self.assertEqual(expected, actual)
        actual = ParserUtils.parse_any_element(element, False)
        self.assertIsNone(actual.qname)

    def test_element_text_and_tail(self):
        element = Element("foo")

        text, tail = ParserUtils.element_text_and_tail(element)
        self.assertIsNone(text)
        self.assertIsNone(tail)

        element.text = " \n "
        element.tail = " \n  "
        text, tail = ParserUtils.element_text_and_tail(element)
        self.assertIsNone(text)
        self.assertIsNone(tail)

        element.text = " foo "
        element.tail = " bar "
        text, tail = ParserUtils.element_text_and_tail(element)
        self.assertEqual("foo", text)
        self.assertEqual("bar", tail)
