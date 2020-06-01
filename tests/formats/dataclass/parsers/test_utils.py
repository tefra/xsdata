from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase
from unittest.mock import MagicMock

from lxml.etree import Element
from lxml.etree import QName

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter12 import ProductType
from tests.fixtures.defxmlschema.chapter12 import SizeType
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
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

        params = {}
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
        self.assertEqual({}, params)

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
            var.types, element.text, var.default, element.nsmap, var.is_list,
        )

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

    def test_bind_element_wildcard_param_with_dataclass(self):
        params = {}
        var = XmlVar(name="a", qname=QName("a"))
        qname = QName("b")
        value = AnyElement()
        clazz = make_dataclass("Foo", fields=[])
        foo = clazz()

        ParserUtils.bind_element_wildcard_param(params, var, qname, value)
        self.assertEqual(dict(a=value), params)
        self.assertIsNone(value.qname)

        params.clear()
        ParserUtils.bind_element_wildcard_param(params, var, qname, foo)
        self.assertEqual(dict(a=foo), params)
        self.assertEqual(qname, foo.qname)

    def test_bind_element_wild_text_when_find_var_returns_none(self):
        meta = mock.Mock(XmlMeta)
        meta.find_var = MagicMock(return_value=None)
        elem = Element("foo")
        params = {}
        ParserUtils.bind_element_wild_text(params, meta, elem)
        self.assertEqual(0, len(params))

    def test_bind_element_wild_text_when_element_has_no_text_and_tail(self):
        var = XmlVar(name="a", qname=QName("a"))
        meta = mock.Mock(XmlMeta)
        meta.find_var = MagicMock(return_value=var)
        elem = Element("foo")
        params = {}

        ParserUtils.bind_element_wild_text(params, meta, elem)
        self.assertEqual(0, len(params))

    def test_bind_element_wild_text(self):
        var = XmlVar(name="a", qname=QName("a"))
        meta = mock.Mock(XmlMeta)
        meta.find_var = MagicMock(return_value=var)
        elem = Element("foo")
        elem.text = "txt"
        elem.tail = "tail"
        params = {}

        ParserUtils.bind_element_wild_text(params, meta, elem)
        expected = AnyElement(text="txt", tail="tail")
        self.assertEqual(dict(a=expected), params)

        elem.text = "a"
        elem.tail = "b"
        expected = AnyElement(text="a", tail="b")
        ParserUtils.bind_element_wild_text(params, meta, elem)
        self.assertEqual(dict(a=expected), params)

    def test_bind_element_wild_text_when_var_is_list(self):
        var = XmlVar(name="a", qname=QName("a"), default=list)
        meta = mock.Mock(XmlMeta)
        meta.find_var = MagicMock(return_value=var)
        elem = Element("foo")
        elem.text = "txt"
        elem.tail = "tail"
        params = {}

        ParserUtils.bind_element_wild_text(params, meta, elem)
        self.assertEqual(dict(a=["txt", "tail"]), params)

        elem.text = None
        ParserUtils.bind_element_wild_text(params, meta, elem)
        self.assertEqual(dict(a=["txt", "tail", "tail"]), params)

        elem.tail = None
        elem.text = "first"
        ParserUtils.bind_element_wild_text(params, meta, elem)
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
