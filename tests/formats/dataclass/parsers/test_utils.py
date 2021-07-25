from unittest import mock

from xsdata.formats.converter import ConverterFactory
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.utils.testing import FactoryTestCase


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

    def test_xsi_nil(self):
        attrs = {}
        self.assertIsNone(ParserUtils.xsi_nil(attrs))

        attrs = {QNames.XSI_NIL: "true"}
        self.assertTrue(ParserUtils.xsi_nil(attrs))

        attrs = {QNames.XSI_NIL: "false"}
        self.assertFalse(ParserUtils.xsi_nil(attrs))

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value(self, mock_deserialize):
        self.assertEqual(1, ParserUtils.parse_value(None, [int], 1))
        self.assertIsNone(ParserUtils.parse_value(None, [int], lambda: 1))

        self.assertTrue(2, ParserUtils.parse_value("1", [int], None))
        mock_deserialize.assert_called_once_with("1", [int], ns_map=None, format=None)

    def test_parse_value_with_tokens_true(self):
        actual = ParserUtils.parse_value(" 1 2 3", [int], list, None, list)
        self.assertEqual([1, 2, 3], actual)

        actual = ParserUtils.parse_value(["1", "2", "3"], [int], list, None, tuple)
        self.assertEqual((1, 2, 3), actual)

        actual = ParserUtils.parse_value(None, [int], lambda: [1, 2, 3], None, list)
        self.assertEqual([1, 2, 3], actual)

    @mock.patch.object(ConverterFactory, "deserialize", return_value=2)
    def test_parse_value_with_ns_map(self, mock_to_python):
        ns_map = dict(a=1)
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
    def test_parse_value_with_format(self, mock_to_python):
        ParserUtils.parse_value(" 1 2 3", [str], list, format="Nope")
        self.assertEqual(1, mock_to_python.call_count)
        mock_to_python.assert_called_once_with(
            " 1 2 3", [str], ns_map=None, format="Nope"
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
