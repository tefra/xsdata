from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from dataclasses import replace
from unittest import mock
from unittest.case import TestCase

from tests.fixtures.books import Books
from tests.fixtures.defxmlschema.chapter12 import ProductType
from tests.fixtures.defxmlschema.chapter12 import SizeType
from xsdata.formats.converter import ConverterAdapter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames


class ParserUtilsTests(TestCase):
    def setUp(self) -> None:
        self.ctx = XmlContext()

    def test_xsi_type(self):
        ns_map = {"bar": "xsdata"}
        attrs = {}
        self.assertIsNone(ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "foo"}
        self.assertEqual("foo", ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "bar:foo"}
        self.assertEqual("{xsdata}foo", ParserUtils.xsi_type(attrs, ns_map))

    def test_data_type(self):
        ns_map = {"bar": "xsdata"}
        attrs = {}
        self.assertEqual(DataType.STRING, ParserUtils.data_type(attrs, ns_map))

        ns_map = {"xs": Namespace.XS.uri}
        attrs = {QNames.XSI_TYPE: "xs:foo"}
        self.assertEqual(DataType.STRING, ParserUtils.data_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "xs:float"}
        self.assertEqual(DataType.FLOAT, ParserUtils.data_type(attrs, ns_map))

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

    def test_bind_objects(self):
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

        params = {}
        ParserUtils.bind_objects(params, meta, 1, objects)
        expected = {
            "x": 1,
            "w": AnyElement(
                children=[AnyElement(qname="w", text=""), AnyElement(qname="foo")]
            ),
        }

        self.assertEqual(expected, params)

    @mock.patch("xsdata.formats.dataclass.parsers.utils.logger.warning")
    def test_bind_objects_with_unassigned_object(self, mock_warning):
        a = make_dataclass("a", [("x", int)])
        meta = XmlContext().build(a)
        params = {}
        objects = [("x", 1), ("y", 2)]

        ParserUtils.bind_objects(params, meta, 0, objects)

        self.assertEqual({"x": 1}, params)
        mock_warning.assert_called_once_with("Unassigned parsed object %s", "y")

    def test_bind_mixed_objects(self):
        generic = AnyElement(qname="foo")
        data_class = make_dataclass("A", fields=[])
        derived = DerivedElement(qname="d", value=data_class)
        objects = [
            ("a", 1),
            ("b", None),
            ("d", data_class),
            ("foo", generic),
            (None, "foo"),
        ]

        var = XmlWildcard(name="foo", qname="{any}foo")
        params = {}
        ParserUtils.bind_mixed_objects(params, var, 1, objects)

        expected = {var.name: [AnyElement(qname="b", text=""), derived, generic, "foo"]}
        self.assertEqual(expected, params)

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_any_attribute")
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_attrs(self, mock_parse_value, mock_parse_any_attribute):
        mock_parse_value.return_value = "2020-03-02"
        mock_parse_any_attribute.return_value = "foobar"
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")

        params = {}
        ns_map = {}
        attrs = {"effDate": "2020-03-01", "foo": "bar"}

        ParserUtils.bind_attrs(params, metadata, attrs, ns_map)
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

    def test_bind_attrs_doesnt_overwrite_values(self):
        metadata = self.ctx.build(ProductType)
        params = dict(eff_date="foo")
        attrs = {"effDate": "2020-03-01"}
        ns_map = {}

        ParserUtils.bind_attrs(params, metadata, attrs, ns_map)

        expected = {"eff_date": "foo", "other_attributes": {"effDate": "2020-03-01"}}
        self.assertEqual(expected, params)

    def test_bind_attrs_ignore_init_false_vars(self):
        metadata = self.ctx.build(ProductType)
        eff_date = metadata.find_var("effDate")
        metadata.vars.remove(eff_date)
        metadata.vars.append(replace(eff_date, init=False))

        params = {}
        attrs = {"effDate": "2020-03-01"}
        ns_map = {}

        ParserUtils.bind_attrs(params, metadata, attrs, ns_map)
        self.assertEqual({"other_attributes": {}}, params)

    @mock.patch.object(XmlMeta, "find_var")
    def test_bind_attrs_skip_empty_attrs(self, mock_find_var):
        metadata = self.ctx.build(ProductType)

        params = {}
        ParserUtils.bind_attrs(params, metadata, {}, {})
        self.assertEqual(0, len(params))
        self.assertEqual(0, mock_find_var.call_count)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_content(self, mock_parse_value):
        metadata = self.ctx.build(SizeType)
        var = metadata.find_var(mode=FindMode.TEXT)
        params = {}
        ns_map = {"a": "b"}

        self.assertFalse(ParserUtils.bind_content(params, metadata, None, ns_map))
        self.assertEqual({}, params)

        self.assertTrue(ParserUtils.bind_content(params, metadata, "foo", ns_map))
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            "foo", var.types, var.default, ns_map, var.is_list
        )

    def test_bind_content_with_no_text_var(self):
        params = {}
        metadata = self.ctx.build(Books)
        self.assertFalse(ParserUtils.bind_content(params, metadata, "foo", {}))
        self.assertEqual({}, params)

    def test_bind_var(self):
        var = XmlVar(name="a", qname="a")
        params = {}

        status = ParserUtils.bind_var(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": 1}, params)

        status = ParserUtils.bind_var(params, var, 2)
        self.assertFalse(status)
        self.assertEqual({"a": 1}, params)

    def test_bind_var_with_list_var(self):
        var = XmlVar(name="a", qname="a", list_element=True)
        params = {}

        status = ParserUtils.bind_var(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": [1]}, params)

        status = ParserUtils.bind_var(params, var, 2)
        self.assertTrue(status)
        self.assertEqual({"a": [1, 2]}, params)

    def test_bind_wild_var(self):
        params = {}
        var = XmlVar(name="a", qname="a")
        qname = "b"
        one = AnyElement(qname=qname, text="one")
        two = AnyElement(qname=qname, text="two")
        three = AnyElement(qname=qname, text="three")
        bind = ParserUtils.bind_wild_var

        self.assertTrue(bind(params, var, qname, "one"))
        self.assertEqual(dict(a=one), params)

        self.assertTrue(bind(params, var, qname, "two"))
        self.assertEqual(dict(a=AnyElement(children=[one, two])), params)

        self.assertTrue(bind(params, var, qname, "three"))
        self.assertEqual(dict(a=AnyElement(children=[one, two, three])), params)

    def test_bind_wild_var_with_list_var(self):
        params = {}
        var = XmlVar(name="a", qname="a", list_element=True)
        qname = "b"
        one = AnyElement(qname=qname, text="one")
        two = AnyElement(qname=qname, text="two")
        three = AnyElement(qname=qname, text="three")
        bind = ParserUtils.bind_wild_var

        self.assertTrue(bind(params, var, qname, "one"))
        self.assertTrue(bind(params, var, qname, "two"))
        self.assertTrue(bind(params, var, qname, "three"))
        self.assertEqual(dict(a=[one, two, three]), params)

    def test_bind_wild_content(self):
        var = XmlVar(name="a", qname="a")
        params = {}
        attrs = {}
        ns_map = {}

        ParserUtils.bind_wild_content(params, var, None, None, attrs, ns_map)
        self.assertEqual(0, len(params))

        params = {}
        ParserUtils.bind_wild_content(params, var, "txt", "tail", attrs, ns_map)
        expected = AnyElement(text="txt", tail="tail")
        self.assertEqual(dict(a=expected), params)

        attrs = {"a": "b"}
        ns_map = {"ns0": "a"}
        ParserUtils.bind_wild_content(params, var, "txt", "tail", attrs, ns_map)
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

        ParserUtils.bind_wild_content(params, var, "txt", "tail", attrs, ns_map)
        self.assertEqual(dict(a=["txt", "tail"]), params)

        ParserUtils.bind_wild_content(params, var, None, "tail", attrs, ns_map)
        self.assertEqual(dict(a=["txt", "tail", "tail"]), params)

        ParserUtils.bind_wild_content(params, var, "first", None, attrs, ns_map)
        self.assertEqual(dict(a=["first", "txt", "tail", "tail"]), params)

    def test_prepare_generic_value(self):
        @dataclass
        class Fixture:
            content: str

        actual = ParserUtils.prepare_generic_value("a", "foo")
        expected = AnyElement(qname="a", text="foo")
        self.assertEqual(expected, actual)

        fixture = Fixture("foo")
        actual = ParserUtils.prepare_generic_value("a", fixture)
        expected = DerivedElement(qname="a", value=fixture)
        self.assertEqual(expected, actual)

        actual = ParserUtils.prepare_generic_value("a", expected)
        self.assertIs(expected, actual)
