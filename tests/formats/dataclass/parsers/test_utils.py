from dataclasses import dataclass
from dataclasses import field
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter08.example0803 import DressSize
from tests.fixtures.defxmlschema.chapter12.chapter12 import ProductType
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace


class ParserUtilsTests(TestCase):
    def setUp(self) -> None:
        self.ctx = XmlContext()

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value(self, mock_to_python):
        self.assertEqual(1, ParserUtils.parse_value([int], None, 1))
        self.assertIsNone(ParserUtils.parse_value([int], None, lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value([int], "1", None))
        mock_to_python.assert_called_once_with([int], "1", None)

    def test_parse_value_with_tokens_true(self):
        actual = ParserUtils.parse_value([int], " 1 2 3", list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value([int], ["1", "2", "3"], list, None, True)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
        ParserUtils.parse_value([int], " 1 2 3", list, ns_map, True)
        ParserUtils.parse_value([str], " 1 2 3", None, ns_map, False)

        self.assertEqual(4, mock_to_python.call_count)
        mock_to_python.assert_has_calls(
            [
                mock.call([int], "1", ns_map),
                mock.call([int], "2", ns_map),
                mock.call([int], "3", ns_map),
                mock.call([str], " 1 2 3", ns_map),
            ]
        )

    @mock.patch.object(ParserUtils, "bind_element_wildcard_param")
    @mock.patch.object(ParserUtils, "find_eligible_wildcard")
    @mock.patch.object(ParserUtils, "bind_element_param")
    def test_bind_elements(
        self,
        mock_bind_element_param,
        mock_find_eligible_wildcard,
        mock_bind_element_wildcard_param,
    ):
        @dataclass
        class A:
            x: int
            y: int = field(init=False)
            w: object = field(metadata=dict(type=XmlType.WILDCARD))

        ctx = XmlContext()
        meta = ctx.build(A)
        x = meta.find_var(QName("x"))
        y = meta.find_var(QName("y"))
        w = meta.find_var(QName("wild"))
        wild_element = AnyElement(qname="foo")

        objects = [
            ("foo", 0),
            (x.qname, 1),
            (y.qname, 2),
            (w.qname, None),
            (w.qname, wild_element),
        ]

        mock_bind_element_param.side_effect = [True, False, False]
        mock_find_eligible_wildcard.side_effect = [None, w]

        params = dict()
        ParserUtils.bind_element_children(params, meta, 1, objects)

        mock_bind_element_param.assert_has_calls(
            [
                mock.call(params, x, 1),
                mock.call(params, w, ""),
                mock.call(params, w, wild_element),
            ]
        )
        mock_find_eligible_wildcard.assert_has_calls(
            [mock.call(meta, w.qname, params), mock.call(meta, QName("foo"), params)]
        )

        mock_bind_element_wildcard_param.assert_called_once_with(
            params, w, w.qname, wild_element
        )

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_element_attrs(self, mock_parse_value):
        mock_parse_value.return_value = "2020-03-02"
        metadata = self.ctx.build(ProductType)
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
        metadata = self.ctx.build(ProductType)
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
        metadata = self.ctx.build(Books)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_element_text_with_text_var(self, mock_parse_value):
        element = Element("foo")
        params = dict()
        metadata = self.ctx.build(DressSize)
        var = metadata.find_var(condition=lambda x: x.is_text)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

        element.text = "foo"
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            var.types, element.text, var.default, element.nsmap, var.is_list,
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

    def test_parse_any_attributes(self):
        element = Element("foo", nsmap=dict(foo="bar"))
        element.set("a", QName("bar", "val"))
        element.set("b", "2")
        element.set("c", "what:3")

        actual = ParserUtils.parse_any_attributes(element)
        expected = {
            QName("a"): QName("bar", "val"),
            QName("b"): "2",
            QName("c"): "what:3",
        }

        self.assertEqual("foo:val", element.attrib["a"])
        self.assertEqual(expected, actual)

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
