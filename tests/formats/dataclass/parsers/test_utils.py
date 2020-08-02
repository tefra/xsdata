from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from lxml.etree import Element
from lxml.etree import QName
from lxml.etree import SubElement

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter12 import ProductType
from tests.fixtures.defxmlschema.chapter12 import SizeType
from tests.fixtures.defxmlschema.chapter16 import Umbrella
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames


class ParserUtilsTests(TestCase):
    def setUp(self) -> None:
        self.ctx = XmlContext()

    def test_parse_xsi_type(self):
        ele = Element("foo")
        self.assertIsNone(ParserUtils.parse_xsi_type(ele))

        ele.set(QNames.XSI_TYPE, "foo")
        self.assertEqual(QName("foo"), ParserUtils.parse_xsi_type(ele))

        ele = Element("foo", nsmap=dict(bar="xsdata"))
        ele.set(QNames.XSI_TYPE, "bar:foo")
        self.assertEqual(QName("xsdata", "foo"), ParserUtils.parse_xsi_type(ele))

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value(self, mock_to_python):
        self.assertEqual(1, ParserUtils.parse_value(None, [int], 1))
        self.assertIsNone(ParserUtils.parse_value(None, [int], lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value("1", [int], None))
        mock_to_python.assert_called_once_with("1", [int], None)

    def test_parse_value_with_tokens_true(self):
        actual = ParserUtils.parse_value(" 1 2 3", [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(["1", "2", "3"], [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch("xsdata.formats.dataclass.parsers.utils.to_python", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
        ParserUtils.parse_value(" 1 2 3", [int], list, ns_map, True)
        ParserUtils.parse_value(" 1 2 3", [str], None, ns_map, False)

        self.assertEqual(4, mock_to_python.call_count)
        mock_to_python.assert_has_calls(
            [
                mock.call("1", [int], ns_map),
                mock.call("2", [int], ns_map),
                mock.call("3", [int], ns_map),
                mock.call(" 1 2 3", [str], ns_map),
            ]
        )

    @mock.patch.object(ParserUtils, "bind_element_wildcard_param")
    @mock.patch.object(ParserUtils, "find_eligible_wildcard")
    @mock.patch.object(ParserUtils, "bind_element_param")
    def test_bind_element_children(
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

        params = {}
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

    def test_bind_mixed_content(self):
        generic = AnyElement(qname="foo")
        data_class = make_dataclass("A", fields=[])
        objects = [
            (QName("a"), 1),
            (QName("b"), None),
            (QName("d"), data_class),
            (QName("foo"), generic),
        ]

        var = XmlWildcard(name="foo", qname=QName("any", "foo"))
        params = {}
        ParserUtils.bind_mixed_content(params, var, 1, objects)

        expected = {
            var.name: [AnyElement(qname=QName("b"), text=""), data_class, generic]
        }
        self.assertEqual(expected, params)
        self.assertEqual(QName("d"), data_class.qname)

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_any_type")
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_element_attrs(self, mock_parse_value, mock_parse_any_type):
        mock_parse_value.return_value = "2020-03-02"
        mock_parse_any_type.return_value = "bar"
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")
        element = Element("foo")
        element.set("effDate", "2020-03-01")
        element.set("whatever", "foo")

        params = {}
        ParserUtils.bind_element_attrs(params, metadata, element)
        expected = {
            "eff_date": "2020-03-02",
            "other_attributes": {QName("whatever"): "bar"},
        }
        self.assertEqual(expected, params)
        mock_parse_any_type.assert_called_once_with("foo", element.nsmap)
        mock_parse_value.assert_called_once_with(
            "2020-03-01",
            eff_date.types,
            eff_date.default,
            element.nsmap,
            eff_date.is_list,
        )

    def test_parse_any_type(self):
        self.assertEqual(
            "http://foo", ParserUtils.parse_any_type("http://foo", {"http": "h"})
        )
        self.assertEqual("a:foo", ParserUtils.parse_any_type("a:foo", {}))
        self.assertEqual(
            QName("b", "foo"), ParserUtils.parse_any_type("a:foo", {"a": "b"})
        )

    def test_bind_element_attrs_doesnt_overwrite_values(self):
        metadata = self.ctx.build(ProductType)
        element = Element("foo")
        element.set("effDate", "2020-03-01")

        params = dict(eff_date="foo")

        ParserUtils.bind_element_attrs(params, metadata, element)
        expected = {"eff_date": "foo", "other_attributes": {"effDate": "2020-03-01"}}
        self.assertEqual(expected, params)

    def test_bind_elements_attrs_ignore_init_false_vars(self):
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")
        metadata.vars.remove(eff_date)
        metadata.vars.append(replace(eff_date, init=False))

        element = Element("foo")
        element.set("effDate", "2020-03-01")

        params = {}
        ParserUtils.bind_element_attrs(params, metadata, element)
        self.assertEqual({"other_attributes": {}}, params)

    @mock.patch.object(XmlMeta, "find_var")
    def test_bind_element_attrs_skip_element_without_attributes(self, mock_find_var):
        metadata = self.ctx.build(ProductType)
        element = Element("foo")

        params = {}
        ParserUtils.bind_element_attrs(params, metadata, element)
        self.assertEqual(0, len(params))
        self.assertEqual(0, mock_find_var.call_count)

    def test_bind_element_text_with_no_text_var(self):
        element = Element("foo")
        element.text = "foo"

        params = {}
        metadata = self.ctx.build(Books)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_element_text_with_text_var(self, mock_parse_value):
        element = Element("foo")
        params = {}
        metadata = self.ctx.build(SizeType)
        var = metadata.find_var(mode=FindMode.TEXT)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

        element.text = "foo"
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            element.text, var.types, var.default, element.nsmap, var.is_list,
        )

        params.clear()
        SubElement(element, "foo")  # Element with children
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

    def test_bind_element_text_with_wildcard_var(self):
        element = Element("foo")
        params = {}
        metadata = self.ctx.build(Umbrella)
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({}, params)

        element.text = "foo"
        ParserUtils.bind_element_text(params, metadata, element)
        self.assertEqual({"any_element": AnyElement(text="foo")}, params)

    def test_bind_element_param(self):
        var = XmlVar(name="a", qname=QName("a"))
        params = {}

        status = ParserUtils.bind_element_param(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": 1}, params)

        status = ParserUtils.bind_element_param(params, var, 2)
        self.assertFalse(status)
        self.assertEqual({"a": 1}, params)

    def test_bind_element_param_with_list_var(self):
        var = XmlVar(name="a", qname=QName("a"), default=list)
        params = {}

        status = ParserUtils.bind_element_param(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": [1]}, params)

        status = ParserUtils.bind_element_param(params, var, 2)
        self.assertTrue(status)
        self.assertEqual({"a": [1, 2]}, params)

    def test_bind_element_wildcard_param(self):
        params = {}
        var = XmlVar(name="a", qname=QName("a"))
        qname = QName("b")
        one = AnyElement(qname=qname, text="one")
        two = AnyElement(qname=qname, text="two")
        three = AnyElement(qname=qname, text="three")

        ParserUtils.bind_element_wildcard_param(params, var, qname, "one")
        self.assertEqual(dict(a=one), params)

        ParserUtils.bind_element_wildcard_param(params, var, qname, "two")
        self.assertEqual(dict(a=AnyElement(children=[one, two])), params)

        ParserUtils.bind_element_wildcard_param(params, var, qname, "three")
        self.assertEqual(dict(a=AnyElement(children=[one, two, three])), params)

    def test_bind_wildcard_text(self):
        var = XmlVar(name="a", qname=QName("a"))
        elem = Element("foo")
        params = {}

        ParserUtils.bind_wildcard_text(params, var, elem)
        self.assertEqual(0, len(params))

        elem = Element("foo")
        elem.text = "txt"
        elem.tail = "tail"
        params = {}

        ParserUtils.bind_wildcard_text(params, var, elem)
        expected = AnyElement(text="txt", tail="tail")
        self.assertEqual(dict(a=expected), params)

        ParserUtils.bind_wildcard_text(params, var, elem)
        expected = AnyElement(text="txt", tail="tail", children=[expected])
        self.assertEqual(dict(a=expected), params)

    def test_bind_wildcard_text_when_var_is_list(self):
        var = XmlVar(name="a", qname=QName("a"), default=list)
        elem = Element("foo")
        elem.text = "txt"
        elem.tail = "tail"
        params = {}

        ParserUtils.bind_wildcard_text(params, var, elem)
        self.assertEqual(dict(a=["txt", "tail"]), params)

        elem.text = None
        ParserUtils.bind_wildcard_text(params, var, elem)
        self.assertEqual(dict(a=["txt", "tail", "tail"]), params)

        elem.tail = None
        elem.text = "first"
        ParserUtils.bind_wildcard_text(params, var, elem)
        self.assertEqual(dict(a=["first", "txt", "tail", "tail"]), params)

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
                QName("a"): "1",
                QName("b"): "2",
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
