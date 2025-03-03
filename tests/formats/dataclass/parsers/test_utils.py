import warnings
from unittest import mock

from tests.fixtures.models import TypeA
from xsdata.exceptions import ParserError
from xsdata.formats.converter import ConverterFactory
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace, ProcessType, QNames
from xsdata.utils.testing import FactoryTestCase, XmlMetaFactory, XmlVarFactory


class ParserUtilsTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.ctx = XmlContext()

    def test_xsi_type(self) -> None:
        ns_map = {"bar": "xsdata"}
        attrs = {}
        self.assertIsNone(ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "foo"}
        self.assertEqual("foo", ParserUtils.xsi_type(attrs, ns_map))

        attrs = {QNames.XSI_TYPE: "bar:foo"}
        self.assertEqual("{xsdata}foo", ParserUtils.xsi_type(attrs, ns_map))

    def test_xsi_nil(self) -> None:
        attrs = {}
        self.assertIsNone(ParserUtils.xsi_nil(attrs))

        attrs = {QNames.XSI_NIL: "true"}
        self.assertTrue(ParserUtils.xsi_nil(attrs))

        attrs = {QNames.XSI_NIL: "false"}
        self.assertFalse(ParserUtils.xsi_nil(attrs))

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value(self, mock_deserialize) -> None:
        self.assertEqual(1, ParserUtils.parse_value(None, [int], 1))
        self.assertIsNone(ParserUtils.parse_value(None, [int], lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value("1", [int], None))
        mock_deserialize.assert_called_once_with("1", [int], ns_map=None, format=None)

    def test_parse_value_with_tokens_true(self) -> None:
        actual = ParserUtils.parse_value(" 1 2 3", [int], list, None, list)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(["1", "2", "3"], [int], list, None, tuple)
        self.assertEqual((1, 2, 3), actual)

        actual = ParserUtils.parse_value(None, [int], lambda: [1, 2, 3], None, list)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python) -> None:
        ns_map = {"a": 1}
        ParserUtils.parse_value(" 1 2 3", [int], list, ns_map, list)
        ParserUtils.parse_value(" 1 2 3", [str], None, ns_map)

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
    def test_parse_value_with_format(self, mock_to_python) -> None:
        ParserUtils.parse_value(" 1 2 3", [str], list, format="Nope")
        self.assertEqual(1, mock_to_python.call_count)
        mock_to_python.assert_called_once_with(
            " 1 2 3", [str], ns_map=None, format="Nope"
        )

    def test_parse_any_attributes(self) -> None:
        attrs = {QNames.XSI_TYPE: "xsd:string", "a": "b"}
        ns_map = {"xsi": Namespace.XSI.uri, "xsd": Namespace.XS.uri}

        result = ParserUtils.parse_any_attributes(attrs, ns_map)
        expected = {
            QNames.XSI_TYPE: "{http://www.w3.org/2001/XMLSchema}string",
            "a": "b",
        }
        self.assertEqual(expected, result)

    def test_parse_any_attribute(self) -> None:
        ns_map = {"xsi": Namespace.XSI.uri, "xsd": Namespace.XS.uri}
        value = ParserUtils.parse_any_attribute("xsd:string", ns_map)
        self.assertEqual("{http://www.w3.org/2001/XMLSchema}string", value)

        ns_map["http"] = "happens"
        value = ParserUtils.parse_any_attribute("http://www.com", ns_map)
        self.assertEqual("http://www.com", value)

    def test_validate_fixed_value(self) -> None:
        meta = XmlMetaFactory.create(clazz=TypeA, qname="foo")
        var = XmlVarFactory.create("fixed", default="a")
        with self.assertRaises(ParserError) as cm:
            ParserUtils.validate_fixed_value(meta, var, "b")

        self.assertEqual("Fixed value mismatch foo:fixed, `a != b`", str(cm.exception))

        var = XmlVarFactory.create("fixed", default=lambda: "a")
        with self.assertRaises(ParserError):
            ParserUtils.validate_fixed_value(meta, var, "b")

        var = XmlVarFactory.create("fixed", default=lambda: " a ")
        ParserUtils.validate_fixed_value(meta, var, "  a  ")

        var = XmlVarFactory.create("fixed", default=lambda: float("nan"))
        ParserUtils.validate_fixed_value(meta, var, float("nan"))

        var = XmlVarFactory.create("fixed", default=lambda: ProcessType.LAX)
        ParserUtils.validate_fixed_value(meta, var, "lax")

    def test_parse_var_with_error(self) -> None:
        meta = XmlMetaFactory.create(clazz=TypeA, qname="foo")
        var = XmlVarFactory.create("fixed", default="a")
        config = ParserConfig()

        with warnings.catch_warnings(record=True) as w:
            result = ParserUtils.parse_var(meta, var, config, "a", types=[int, float])

        expected = (
            "Failed to convert value for `TypeA.fixed`\n"
            "  `a` is not a valid `int | float`"
        )
        self.assertEqual("a", result)
        self.assertEqual(expected, str(w[-1].message))

        config.fail_on_converter_warnings = True
        with self.assertRaises(ParserError) as cm:
            ParserUtils.parse_var(meta, var, config, "a", types=[int, float])

        self.assertEqual(expected, str(cm.exception))
