from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from unittest import mock

from tests.fixtures.artists import Gender
from tests.fixtures.books import Books
from xsdata.formats.converter import ConverterFactory
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.utils.testing import FactoryTestCase
from xsdata.utils.testing import XmlVarFactory


class ParserUtilsTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.ctx = XmlContext()

    def test_xsi_type(self):
        ns_map = {"bar": "xsdata"}
        attrs = {}
        self.assertIsNone(ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "foo"}
        self.assertEqual("foo", ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "bar:foo"}
        self.assertEqual("{xsdata}foo", ParserUtils.xsi_type(attrs, ns_map))

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value(self, mock_deserialize):
        self.assertEqual(1, ParserUtils.parse_value(None, [int], 1))
        self.assertIsNone(ParserUtils.parse_value(None, [int], lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value("1", [int], None))
        mock_deserialize.assert_called_once_with("1", [int], ns_map=None, format=None)

    def test_parse_value_with_tokens_true(self):
        actual = ParserUtils.parse_value(" 1 2 3", [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(["1", "2", "3"], [int], list, None, True)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(None, [int], lambda: [1, 2, 3], None, True)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
        ParserUtils.parse_value(" 1 2 3", [int], list, ns_map, True)
        ParserUtils.parse_value(" 1 2 3", [str], None, ns_map, False)

        self.assertEqual(4, mock_to_python.call_count)
        mock_to_python.assert_has_calls(
            [
                mock.call("1", [int], ns_map=ns_map, format=None),
                mock.call("2", [int], ns_map=ns_map, format=None),
                mock.call("3", [int], ns_map=ns_map, format=None),
                mock.call(" 1 2 3", [str], ns_map=ns_map, format=None),
            ]
        )

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value_with_format(self, mock_to_python):
        ParserUtils.parse_value(" 1 2 3", [str], list, _format="Nope")
        self.assertEqual(1, mock_to_python.call_count)
        mock_to_python.assert_called_once_with(
            " 1 2 3", [str], ns_map=None, format="Nope"
        )

    @mock.patch("xsdata.formats.dataclass.parsers.utils.logger.warning")
    def test_bind_objects(self, mock_warning):
        x = make_dataclass("x", [("a", int), ("c", float)])
        objects = [("a", 1), ("b", 2), ("c", 3.0)]

        params = {}
        ctx = XmlContext()
        meta = ctx.build(x)

        ParserUtils.bind_objects(params, meta, 0, objects)
        self.assertEqual({"a": 1, "c": 3.0}, params)

        mock_warning.assert_called_once_with("Unassigned parsed object %s", "b")

    def test_bind_object_with_matching_wildcard(self):
        x = make_dataclass(
            "x",
            [("a", int), ("any", object, field(metadata={"type": XmlType.WILDCARD}))],
        )
        ctx = XmlContext()
        meta = ctx.build(x)
        params = {}

        result = ParserUtils.bind_object(params, meta, "whatever", "foo")

        self.assertTrue(result)
        self.assertEqual({"any": AnyElement(qname="whatever", text="foo")}, params)

    def test_bind_object_with_matching_element(self):
        x = make_dataclass(
            "x", [("a", int), ("a1", int, field(metadata={"name": "a"}))]
        )
        ctx = XmlContext()
        meta = ctx.build(x)
        params = {"a": 1}

        result = ParserUtils.bind_object(params, meta, "a", 2)

        self.assertTrue(result)
        self.assertEqual({"a": 1, "a1": 2}, params)

    def test_bind_object_failure(self):
        x = make_dataclass(
            "x",
            [
                ("a", int),
            ],
        )
        ctx = XmlContext()
        meta = ctx.build(x)
        params = {}

        result = ParserUtils.bind_object(params, meta, "b", 1)

        self.assertFalse(result)
        self.assertEqual({}, params)

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

        var = XmlVarFactory.create(
            xml_type=XmlType.WILDCARD, name="foo", qname="{any}foo"
        )
        params = {}
        ParserUtils.bind_mixed_objects(params, var, 1, objects)

        expected = {
            var.name: [AnyElement(qname="b", text=None), derived, generic, "foo"]
        }
        self.assertEqual(expected, params)

    def test_fetch_any_children(self):
        objects = [(x, x) for x in "abc"]
        self.assertEqual(["b", "c"], ParserUtils.fetch_any_children(1, objects))

    @mock.patch.object(ParserUtils, "parse_any_attribute")
    @mock.patch.object(ParserUtils, "parse_value")
    def test_bind_attrs(self, mock_parse_value, mock_parse_any_attribute):
        mock_parse_value.return_value = "2020-03-02"
        mock_parse_any_attribute.return_value = "foobar"
        metadata = self.ctx.build(Attributes)
        attr = metadata.find_attribute("simple")

        params = {}
        ns_map = {}
        attrs = {"simple": "2020-03-01", "foo": "bar"}

        ParserUtils.bind_attrs(params, metadata, attrs, ns_map)
        expected = {
            "simple": "2020-03-02",
            "any_attributes": {"foo": "foobar"},
        }
        self.assertEqual(expected, params)
        mock_parse_any_attribute.assert_called_once_with("bar", ns_map)
        mock_parse_value.assert_called_once_with(
            "2020-03-01",
            attr.types,
            attr.default,
            ns_map,
            attr.tokens,
            attr.format,
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
        metadata = self.ctx.build(Attributes)
        params = {"simple": "exists"}
        attrs = {"simple": "new", "a": "b"}
        ns_map = {}

        ParserUtils.bind_attrs(params, metadata, attrs, ns_map)

        expected = {"any_attributes": {"a": "b", "simple": "new"}, "simple": "exists"}
        self.assertEqual(expected, params)

    def test_bind_attrs_ignore_init_false_vars(self):
        metadata = self.ctx.build(Attributes)
        simple = metadata.find_attribute("simple")
        simple.init = False

        metadata.attributes[simple.qname] = simple
        params = {}
        attrs = {"simple": "2020-03-01"}

        ParserUtils.bind_attrs(params, metadata, attrs, {})
        self.assertEqual({}, params)

    @mock.patch.object(XmlMeta, "find_attribute")
    def test_bind_attrs_skip_empty_attrs(self, mock_find_attribute):
        metadata = self.ctx.build(Attributes)

        params = {}
        ParserUtils.bind_attrs(params, metadata, {}, {})
        self.assertEqual(0, len(params))
        self.assertEqual(0, mock_find_attribute.call_count)

    def test_bind_unknown_attrs(self):
        metadata = self.ctx.build(Attributes)
        params = {}
        ParserUtils.bind_attrs(params, metadata, {"a": "b"}, {})

        self.assertEqual({"any_attributes": {"a": "b"}}, params)

    @mock.patch.object(ParserUtils, "parse_value", return_value="yes!")
    def test_bind_content(self, mock_parse_value):
        metadata = self.ctx.build(Gender)
        var = metadata.text
        params = {}
        ns_map = {"a": "b"}

        self.assertFalse(ParserUtils.bind_content(params, metadata, None, ns_map))
        self.assertEqual({}, params)

        self.assertTrue(ParserUtils.bind_content(params, metadata, "foo", ns_map))
        self.assertEqual({"value": "yes!"}, params)
        mock_parse_value.assert_called_once_with(
            "foo", var.types, var.default, ns_map, var.tokens, var.format
        )

    def test_bind_content_with_no_text_var(self):
        params = {}
        metadata = self.ctx.build(Books)
        self.assertFalse(ParserUtils.bind_content(params, metadata, "foo", {}))
        self.assertEqual({}, params)

    def test_bind_var(self):
        var = XmlVarFactory.create(name="a", qname="a", xml_type=XmlType.ELEMENT)
        params = {}

        status = ParserUtils.bind_var(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": 1}, params)

        status = ParserUtils.bind_var(params, var, 2)
        self.assertFalse(status)
        self.assertEqual({"a": 1}, params)

        var.init = False
        params.clear()
        status = ParserUtils.bind_var(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({}, params)

    def test_bind_var_with_list_var(self):
        var = XmlVarFactory.create(
            name="a", qname="a", list_element=True, xml_type=XmlType.ELEMENT
        )
        params = {}

        status = ParserUtils.bind_var(params, var, 1)
        self.assertTrue(status)
        self.assertEqual({"a": [1]}, params)

        status = ParserUtils.bind_var(params, var, 2)
        self.assertTrue(status)
        self.assertEqual({"a": [1, 2]}, params)

    def test_bind_wild_var(self):
        params = {}
        var = XmlVarFactory.create(name="a", qname="a", xml_type=XmlType.WILDCARD)
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
        var = XmlVarFactory.create(
            name="a", qname="a", list_element=True, xml_type=XmlType.ELEMENT
        )
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
        var = XmlVarFactory.create(name="a", qname="a", xml_type=XmlType.WILDCARD)
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
            text="txt", tail="tail", children=[expected], attributes=attrs
        )
        self.assertEqual(dict(a=expected), params)

    def test_bind_wildcard_when_var_is_list(self):
        var = XmlVarFactory.create(
            name="a",
            qname="a",
            default=list,
            list_element=True,
            xml_type=XmlType.WILDCARD,
        )
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
        actual = ParserUtils.prepare_generic_value(None, 1)
        self.assertEqual(1, actual)

        actual = ParserUtils.prepare_generic_value("a", 1)
        expected = AnyElement(qname="a", text="1")
        self.assertEqual(expected, actual)

        actual = ParserUtils.prepare_generic_value("a", "foo")
        expected = AnyElement(qname="a", text="foo")
        self.assertEqual(expected, actual)

        fixture = make_dataclass("Fixture", [("content", str)])
        actual = ParserUtils.prepare_generic_value("a", fixture("foo"))
        expected = DerivedElement(qname="a", value=fixture("foo"))
        self.assertEqual(expected, actual)

        actual = ParserUtils.prepare_generic_value("a", expected)
        self.assertIs(expected, actual)

    def test_score_object(self):
        self.assertEqual(-1.0, ParserUtils.score_object(None))

        cls = make_dataclass("b", [("x", int), ("y", str), ("z", Any)])
        self.assertEqual(2.5, ParserUtils.score_object(cls(1, "1", None)))

        self.assertEqual(-1, ParserUtils.score_object(None))
        self.assertEqual(1.0, ParserUtils.score_object("a"))
        self.assertEqual(1.5, ParserUtils.score_object(2.9))


@dataclass
class Attributes:

    simple: str = field(metadata={"type": "Attribute"})
    any_attributes: Dict[str, str] = field(metadata={"type": "Attributes"})
