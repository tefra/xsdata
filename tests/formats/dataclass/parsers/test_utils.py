from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter12 import ProductType
from tests.fixtures.defxmlschema.chapter12 import SizeType
from tests.fixtures.defxmlschema.chapter16 import Umbrella
from xsdata.formats.converter import ConverterAdapter
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
        ns_map = {"bar": "xsdata"}
        attrs = {}
        self.assertIsNone(ParserUtils.parse_xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "foo"}
        self.assertEqual("foo", ParserUtils.parse_xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "bar:foo"}
        self.assertEqual("{xsdata}foo", ParserUtils.parse_xsi_type(attrs, ns_map))

    @mock.patch.object(ConverterAdapter, "from_string", return_value=2)
    def test_parse_value(self, mock_from_string):
        self.assertEqual(1, ParserUtils.parse_value(None, [int], 1))
        self.assertIsNone(ParserUtils.parse_value(None, [int], lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value("1", [int], None))
        mock_from_string.assert_called_once_with("1", [int], ns_map=None)

    def test_parse_value_with_tokens_true(self):
        actual = ParserUtils.parse_value(" 1 2 3", [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(["1", "2", "3"], [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch.object(ConverterAdapter, "from_string", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
        ParserUtils.parse_value(" 1 2 3", [int], list, ns_map, True)
        ParserUtils.parse_value(" 1 2 3", [str], None, ns_map, False)

        self.assertEqual(4, mock_to_python.call_count)
        mock_to_python.assert_has_calls(
            [
                mock.call("1", [int], ns_map=ns_map),
                mock.call("2", [int], ns_map=ns_map),
                mock.call("3", [int], ns_map=ns_map),
                mock.call(" 1 2 3", [str], ns_map=ns_map),
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
        x = meta.find_var("x")
        y = meta.find_var("y")
        w = meta.find_var("wild")
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
            [mock.call(meta, w.qname, params), mock.call(meta, "foo", params)]
        )

        mock_bind_element_wildcard_param.assert_called_once_with(
            params, w, w.qname, wild_element
        )

    def test_bind_mixed_content(self):
        generic = AnyElement(qname="foo")
        data_class = make_dataclass("A", fields=[])
        objects = [
            ("a", 1),
            ("b", None),
            ("d", data_class),
            ("foo", generic),
        ]

        var = XmlWildcard(name="foo", qname="{any}foo")
        params = {}
        ParserUtils.bind_mixed_content(params, var, 1, objects)

        expected = {var.name: [AnyElement(qname="b", text=""), data_class, generic]}
        self.assertEqual(expected, params)
        self.assertEqual("d", data_class.qname)

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_any_attribute")
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_element_attrs(self, mock_parse_value, mock_parse_any_attribute):
        mock_parse_value.return_value = "2020-03-02"
        mock_parse_any_attribute.return_value = "foobar"
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")

        params = {}
        ns_map = {}
        attrs = {"effDate": "2020-03-01", "foo": "bar"}

        ParserUtils.bind_element_attrs(params, metadata, attrs, ns_map)
        expected = {
            "eff_date": "2020-03-02",
            "other_attributes": {"foo": "foobar"},
        }
        self.assertEqual(expected, params)
        mock_parse_any_attribute.assert_called_once_with("bar", ns_map)
        mock_parse_value.assert_called_once_with(
            "2020-03-01", eff_date.types, eff_date.default, ns_map, eff_date.is_list
        )

    def test_parse_any_attributes(self):
        attrs = {QNames.XSI_TYPE: "xsd:string", "a": "b"}
        ns_map = {"xsi": Namespace.XSI.uri, "xsd": Namespace.XS.uri}

        result = ParserUtils.parse_any_attributes(attrs, ns_map)
        expected = {
            QNames.XSI_TYPE: "{http://www.w3.org/2001/XMLSchema}string",
            "a": "b",
        }
        self.assertEqual(expected, result)

    def test_parse_any_attribute(self):
        ns_map = {"xsi": Namespace.XSI.uri, "xsd": Namespace.XS.uri}
        value = ParserUtils.parse_any_attribute("xsd:string", ns_map)
        self.assertEqual("{http://www.w3.org/2001/XMLSchema}string", value)

        ns_map["http"] = "happens"
        value = ParserUtils.parse_any_attribute("http://www.com", ns_map)
        self.assertEqual("http://www.com", value)

    def test_bind_element_attrs_doesnt_overwrite_values(self):
        metadata = self.ctx.build(ProductType)
        params = dict(eff_date="foo")
        attrs = {"effDate": "2020-03-01"}
        ns_map = {}

        ParserUtils.bind_element_attrs(params, metadata, attrs, ns_map)

        expected = {"eff_date": "foo", "other_attributes": {"effDate": "2020-03-01"}}
        self.assertEqual(expected, params)

    def test_bind_elements_attrs_ignore_init_false_vars(self):
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")
        metadata.vars.remove(eff_date)
        metadata.vars.append(replace(eff_date, init=False))

        params = {}
        attrs = {"effDate": "2020-03-01"}
        ns_map = {}

        ParserUtils.bind_element_attrs(params, metadata, attrs, ns_map)
        self.assertEqual({"other_attributes": {}}, params)

    @mock.patch.object(XmlMeta, "find_var")
    def test_bind_element_attrs_skip_empty_attrs(self, mock_find_var):
        metadata = self.ctx.build(ProductType)

        params = {}
        ParserUtils.bind_element_attrs(params, metadata, {}, {})
        self.assertEqual(0, len(params))
        self.assertEqual(0, mock_find_var.call_count)

    def test_bind_element_with_no_text_var(self):
        params = {}
        metadata = self.ctx.build(Books)
        ParserUtils.bind_element(params, metadata, "foo", None, {}, {})
        self.assertEqual({}, params)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_element_with_text_var(self, mock_parse_value):
        metadata = self.ctx.build(SizeType)
        var = metadata.find_var(mode=FindMode.TEXT)
        params = {}
        ns_map = {"a": "b"}

        ParserUtils.bind_element(params, metadata, None, None, {}, ns_map)
        self.assertEqual({}, params)

        ParserUtils.bind_element(params, metadata, "foo", None, {}, ns_map)
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            "foo", var.types, var.default, ns_map, var.is_list
        )

    def test_bind_element_with_wildcard_var(self):
        metadata = self.ctx.build(Umbrella)
        params = {}
        attrs = {"a": "b"}
        ns_map = {"a": "b"}

        ParserUtils.bind_element(params, metadata, None, None, attrs, ns_map)
        self.assertEqual({}, params)

        ParserUtils.bind_element(params, metadata, "foo", "bar", attrs, ns_map)

        expected = AnyElement(text="foo", tail="bar", attributes=attrs, ns_map=ns_map)
        self.assertEqual(expected, params["any_element"])

    def test_bind_element_param(self):
        var = XmlVar(name="a", qname="a")
        params = {}

        status = ParserUtils.bind_element_param(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": 1}, params)

        status = ParserUtils.bind_element_param(params, var, 2)
        self.assertFalse(status)
        self.assertEqual({"a": 1}, params)

    def test_bind_element_param_with_list_var(self):
        var = XmlVar(name="a", qname="a", list_element=True)
        params = {}

        status = ParserUtils.bind_element_param(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": [1]}, params)

        status = ParserUtils.bind_element_param(params, var, 2)
        self.assertTrue(status)
        self.assertEqual({"a": [1, 2]}, params)

    def test_bind_element_wildcard_param(self):
        params = {}
        var = XmlVar(name="a", qname="a")
        qname = "b"
        one = AnyElement(qname=qname, text="one")
        two = AnyElement(qname=qname, text="two")
        three = AnyElement(qname=qname, text="three")

        ParserUtils.bind_element_wildcard_param(params, var, qname, "one")
        self.assertEqual(dict(a=one), params)

        ParserUtils.bind_element_wildcard_param(params, var, qname, "two")
        self.assertEqual(dict(a=AnyElement(children=[one, two])), params)

        ParserUtils.bind_element_wildcard_param(params, var, qname, "three")
        self.assertEqual(dict(a=AnyElement(children=[one, two, three])), params)

    def test_bind_wildcard_element(self):
        var = XmlVar(name="a", qname="a")
        params = {}
        attrs = {}
        ns_map = {}

        ParserUtils.bind_wildcard_element(params, var, None, None, attrs, ns_map)
        self.assertEqual(0, len(params))

        params = {}
        ParserUtils.bind_wildcard_element(params, var, "txt", "tail", attrs, ns_map)
        expected = AnyElement(text="txt", tail="tail")
        self.assertEqual(dict(a=expected), params)

        attrs = {"a": "b"}
        ns_map = {"ns0": "a"}
        ParserUtils.bind_wildcard_element(params, var, "txt", "tail", attrs, ns_map)
        expected = AnyElement(
            text="txt",
            tail="tail",
            children=[expected],
            attributes=attrs,
            ns_map=ns_map,
        )
        self.assertEqual(dict(a=expected), params)

    def test_bind_wildcard_when_var_is_list(self):
        var = XmlVar(name="a", qname="a", default=list, list_element=True)
        params = {}
        attrs = {"a", "b"}
        ns_map = {"ns0", "a"}

        ParserUtils.bind_wildcard_element(params, var, "txt", "tail", attrs, ns_map)
        self.assertEqual(dict(a=["txt", "tail"]), params)

        ParserUtils.bind_wildcard_element(params, var, None, "tail", attrs, ns_map)
        self.assertEqual(dict(a=["txt", "tail", "tail"]), params)

        ParserUtils.bind_wildcard_element(params, var, "first", None, attrs, ns_map)
        self.assertEqual(dict(a=["first", "txt", "tail", "tail"]), params)

    def test_prepare_generic_value(self):
        @dataclass
        class Fixture:
            content: str

        actual = ParserUtils.prepare_generic_value(None, "foo")
        self.assertEqual("foo", actual)

        actual = ParserUtils.prepare_generic_value("a", "foo")
        self.assertEqual(AnyElement(qname="a", text="foo"), actual)

        fixture = Fixture("foo")
        ParserUtils.prepare_generic_value("a", fixture)
        self.assertEqual("a", fixture.qname)
