import warnings
from decimal import Decimal
from enum import Enum
from typing import Any
from unittest import TestCase
from xml.etree.ElementTree import QName

from lxml import etree

from xsdata.exceptions import ConverterError
from xsdata.formats.converter import BoolConverter
from xsdata.formats.converter import Converter
from xsdata.formats.converter import converter
from xsdata.formats.converter import DecimalConverter
from xsdata.formats.converter import EnumConverter
from xsdata.formats.converter import FloatConverter
from xsdata.formats.converter import IntConverter
from xsdata.formats.converter import LxmlQNameConverter
from xsdata.formats.converter import ProxyConverter
from xsdata.formats.converter import QNameConverter
from xsdata.formats.converter import StrConverter
from xsdata.models.enums import UseType


class ConverterAdapterTests(TestCase):
    def test_from_string(self):
        with warnings.catch_warnings(record=True) as w:
            self.assertEqual("a", converter.from_string("a", [int]))

        self.assertEqual(
            "Failed to convert value `a` to one of [<class 'int'>]", str(w[-1].message)
        )

        self.assertFalse(converter.from_string("false", [int, bool]))
        self.assertEqual(1, converter.from_string("1", [int, bool]))

    def test_to_string(self):
        self.assertEqual(None, converter.from_string(None, [int]))
        self.assertEqual("1", converter.to_string(1))
        self.assertEqual("1 2 3", converter.to_string([1, "2", 3]))
        self.assertEqual(None, converter.to_string(None))
        self.assertEqual("1", converter.to_string(1))
        self.assertEqual("1.5", converter.to_string(1.5))
        self.assertEqual("true", converter.to_string(True))
        self.assertEqual("optional", converter.to_string(UseType.OPTIONAL))
        self.assertEqual("8.77683E-8", converter.to_string(Decimal("8.77683E-8")))
        self.assertEqual("8.77683E-08", converter.to_string(float("8.77683E-8")))

    def test_register_converter(self):
        class MinusOneInt(int):
            pass

        class MinusOneIntConverter(Converter):
            def from_string(self, value: str, **kwargs: Any) -> Any:
                return int(value) - 1

            def to_string(self, value: Any, **kwargs: Any) -> str:
                return str(value)

        with warnings.catch_warnings(record=True) as w:
            self.assertEqual("1", converter.from_string("1", [MinusOneInt]))

        self.assertEqual(
            f"No converter registered for `{MinusOneInt}`", str(w[-1].message)
        )

        converter.register_converter(MinusOneInt, MinusOneIntConverter())
        self.assertEqual(1, converter.from_string("2", [MinusOneInt]))
        self.assertEqual(2, converter.from_string("3", [MinusOneInt]))
        self.assertEqual("3", converter.to_string(MinusOneInt("3")))
        converter.unregister_converter(MinusOneInt)

    def test_register_converter_with_lambda(self):
        class MinusOneInt(int):
            pass

        converter.register_converter(MinusOneInt, lambda x: int(x) - 1)
        self.assertEqual(1, converter.from_string("2", [MinusOneInt]))
        self.assertEqual(2, converter.from_string("3", [MinusOneInt]))
        converter.unregister_converter(MinusOneInt)


class StrConverterTests(TestCase):
    def setUp(self):
        self.converter = StrConverter()

    def test_from_string(self):
        value = "a"
        self.assertIs(value, self.converter.from_string(value))

    def test_to_string(self):
        value = "a"
        self.assertIs(value, self.converter.to_string(value))


class BoolConverterTests(TestCase):
    def setUp(self):
        self.converter = BoolConverter()

    def test_from_string(self):
        with self.assertRaises(ConverterError):
            self.converter.from_string("True")

        self.assertTrue(self.converter.from_string("true"))
        self.assertTrue(self.converter.from_string("1"))
        self.assertFalse(self.converter.from_string("false"))
        self.assertFalse(self.converter.from_string("0"))

    def test_to_string(self):
        self.assertEqual("true", self.converter.to_string(True))
        self.assertEqual("false", self.converter.to_string(False))


class IntConverterTests(TestCase):
    def setUp(self):
        self.converter = IntConverter()

    def test_from_string(self):
        with self.assertRaises(ConverterError):
            self.converter.from_string("a")

        self.assertEqual(2, self.converter.from_string("2"))
        self.assertEqual(2, self.converter.from_string("+2"))
        self.assertEqual(-2, self.converter.from_string("-2"))

    def test_to_string(self):
        self.assertEqual("2", self.converter.to_string(2))


class FloatConverterTests(TestCase):
    def setUp(self):
        self.converter = FloatConverter()

    def test_from_string(self):
        with self.assertRaises(ConverterError):
            self.converter.from_string("a")

        self.assertEqual(2.0, self.converter.from_string("2"))
        self.assertEqual(2.1, self.converter.from_string("2.1"))

    def test_to_string(self):
        self.assertEqual("2.1", self.converter.to_string(2.1))
        self.assertEqual("INF", self.converter.to_string(float("inf")))
        self.assertEqual("INF", self.converter.to_string(float("+inf")))
        self.assertEqual("-INF", self.converter.to_string(float("-inf")))
        self.assertEqual("NaN", self.converter.to_string(float("nan")))
        self.assertEqual("8.77683E-08", self.converter.to_string(float("8.77683E-8")))


class DecimalConverterTests(TestCase):
    def setUp(self):
        self.converter = DecimalConverter()

    def test_from_string(self):
        with self.assertRaises(ConverterError):
            self.converter.from_string("a")

        self.assertEqual(Decimal(1), self.converter.from_string("1"))

    def test_to_string(self):
        self.assertEqual("2.1", self.converter.to_string(Decimal("2.1")))
        self.assertEqual("INF", self.converter.to_string(Decimal("inf")))
        self.assertEqual("INF", self.converter.to_string(Decimal("+inf")))
        self.assertEqual("-INF", self.converter.to_string(Decimal("-inf")))
        self.assertEqual("8.77683E-8", self.converter.to_string(Decimal("8.77683E-8")))


class LxmlQNameConverterTests(TestCase):
    def setUp(self):
        self.converter = LxmlQNameConverter()

    def test_from_string(self):
        convert = self.converter.from_string
        with self.assertRaises(ConverterError):
            convert("a:b")

        with self.assertRaises(ConverterError):
            self.assertEqual(etree.QName("b"), convert("a:b", ns_map={}))

        self.assertEqual(etree.QName("a"), convert("a", ns_map={}))
        self.assertEqual(etree.QName("aa", "b"), convert("a:b", ns_map={"a": "aa"}))

    def test_to_string(self):
        ns_map = {"c_prefix": "c"}
        convert = self.converter.to_string

        self.assertEqual("a", convert(etree.QName("a"), ns_map=ns_map))
        self.assertEqual("a", convert(etree.QName("a")))
        self.assertEqual("ns1:b", convert(etree.QName("a", "b"), ns_map=ns_map))
        self.assertEqual("{a}b", convert(etree.QName("a", "b")))
        self.assertEqual("c_prefix:c", convert(etree.QName("c", "c"), ns_map=ns_map))
        self.assertEqual("{c}c", convert(etree.QName("c", "c")))


class QNameConverterTests(TestCase):
    def setUp(self):
        self.converter = QNameConverter()

    def test_from_string(self):
        convert = self.converter.from_string
        with self.assertRaises(ConverterError) as cm:
            convert("a:b")

        self.assertEqual(
            "QName converter needs ns_map to support prefixes", str(cm.exception)
        )

        with self.assertRaises(ConverterError) as cm:
            convert("a:b", ns_map={})
        self.assertEqual("Unknown namespace prefix: `a`", str(cm.exception))

        with self.assertRaises(ConverterError) as cm:
            convert("", ns_map={})
        self.assertEqual("Invalid QName", str(cm.exception))

        self.assertEqual(QName("a"), convert("a", ns_map={}))
        self.assertEqual(QName("aa", "b"), convert("a:b", ns_map={"a": "aa"}))
        self.assertEqual(QName("{a}b"), convert("{a}b"))

    def test_to_string(self):
        ns_map = {"c_prefix": "c"}
        convert = self.converter.to_string

        self.assertEqual("a", convert(QName("a"), ns_map=ns_map))
        self.assertEqual("a", convert(QName("a")))
        self.assertEqual("ns1:b", convert(QName("a", "b"), ns_map=ns_map))
        self.assertEqual("{a}b", convert(QName("a", "b")))
        self.assertEqual("c_prefix:c", convert(QName("c", "c"), ns_map=ns_map))
        self.assertEqual("{c}c", convert(QName("c", "c")))


class EnumConverterTests(TestCase):
    def setUp(self):
        self.converter = EnumConverter()

    def test_from_string(self):
        class Fixture(Enum):
            two_point_one = 2.1

        convert = self.converter.from_string
        with self.assertRaises(ConverterError):
            with warnings.catch_warnings(record=True) as w:
                convert("a", data_type=Fixture)

        self.assertEqual(0, len(w))

        self.assertEqual(Fixture.two_point_one, convert("2.1", data_type=Fixture))

    def test_from_string_with_list_derived_enum(self):
        class Fixture(Enum):
            a = "a a a"

        convert = self.converter.from_string
        self.assertEqual(Fixture.a, convert(" a \na a  ", data_type=Fixture))

    def test_from_string_with_value_never_equal_to_anything(self):
        class Fixture(Enum):
            a = Decimal("NaN")

        convert = self.converter.from_string
        self.assertEqual(Fixture.a, convert("NaN", data_type=Fixture))

        with self.assertRaises(ConverterError):
            convert("1.0", data_type=Fixture)

    def test_from_string_raises_exception_on_missing_data_type(self):
        with self.assertRaises(ConverterError) as cm:
            self.converter.from_string("a")

        self.assertEqual("Provide a target data type enum class.", str(cm.exception))

    def test_to_string(self):
        class Fixture(Enum):
            a = QName("a", "b")
            b = Decimal("+inf")
            c = 2.1

        ns_map = {}
        self.assertEqual("ns0:b", self.converter.to_string(Fixture.a, ns_map=ns_map))
        self.assertEqual("INF", self.converter.to_string(Fixture.b))
        self.assertEqual("2.1", self.converter.to_string(Fixture.c))


class ProxyConverterTests(TestCase):
    def setUp(self):
        self.converter = ProxyConverter(lambda x: int(x))

    def test_from_string(self):
        with self.assertRaises(ConverterError):
            self.converter.from_string("a")

        self.assertEqual(1, self.converter.from_string("1"))

    def test_to_string(self):
        self.assertEqual("1", self.converter.to_string(1))
