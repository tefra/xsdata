import warnings
from datetime import date
from datetime import datetime
from datetime import time
from decimal import Decimal
from enum import Enum
from typing import Any
from unittest import TestCase
from xml.etree.ElementTree import QName

from lxml import etree

from xsdata.exceptions import ConverterError
from xsdata.formats.converter import Converter
from xsdata.formats.converter import converter
from xsdata.formats.converter import ProxyConverter
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.enums import UseType


class ConverterAdapterTests(TestCase):
    def test_deserialize(self):
        with warnings.catch_warnings(record=True) as w:
            self.assertEqual("a", converter.deserialize("a", [int]))

        self.assertEqual(
            "Failed to convert value `a` to one of [<class 'int'>]", str(w[-1].message)
        )

        self.assertFalse(converter.deserialize("false", [int, bool]))
        self.assertEqual(1, converter.deserialize("1", [int, bool]))

    def test_serialize(self):
        self.assertEqual(None, converter.serialize(None))
        self.assertEqual("1", converter.serialize(1))
        self.assertEqual("1 2 3", converter.serialize([1, "2", 3]))
        self.assertEqual(None, converter.serialize(None))
        self.assertEqual("1", converter.serialize(1))
        self.assertEqual("1.5", converter.serialize(1.5))
        self.assertEqual("true", converter.serialize(True))
        self.assertEqual("optional", converter.serialize(UseType.OPTIONAL))
        self.assertEqual("8.77683E-8", converter.serialize(Decimal("8.77683E-8")))
        self.assertEqual("8.77683E-08", converter.serialize(float("8.77683E-8")))

    def test_register_converter(self):
        class MinusOneInt(int):
            pass

        class MinusOneIntConverter(Converter):
            def deserialize(self, value: str, **kwargs: Any) -> Any:
                return int(value) - 1

            def serialize(self, value: Any, **kwargs: Any) -> str:
                return str(value)

        with warnings.catch_warnings(record=True) as w:
            self.assertEqual("1", converter.deserialize("1", [MinusOneInt]))

        self.assertEqual(
            f"No converter registered for `{MinusOneInt}`", str(w[-1].message)
        )

        converter.register_converter(MinusOneInt, MinusOneIntConverter())
        self.assertEqual(1, converter.deserialize("2", [MinusOneInt]))
        self.assertEqual(2, converter.deserialize("3", [MinusOneInt]))
        self.assertEqual("3", converter.serialize(MinusOneInt("3")))
        converter.unregister_converter(MinusOneInt)

    def test_register_converter_with_lambda(self):
        class MinusOneInt(int):
            pass

        converter.register_converter(MinusOneInt, lambda x: int(x) - 1)
        self.assertEqual(1, converter.deserialize("2", [MinusOneInt]))
        self.assertEqual(2, converter.deserialize("3", [MinusOneInt]))
        converter.unregister_converter(MinusOneInt)


class StrConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(str)

    def test_deserialize(self):
        self.assertEqual("a", self.converter.deserialize("a"))
        self.assertEqual("1", self.converter.deserialize(1))

    def test_serialize(self):
        self.assertEqual("a", self.converter.serialize("a"))
        self.assertEqual("1", self.converter.serialize(1))


class BoolConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(bool)

    def test_deserialize(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("True")

        self.assertTrue(self.converter.deserialize("true"))
        self.assertTrue(self.converter.deserialize("1"))
        self.assertFalse(self.converter.deserialize("false"))
        self.assertFalse(self.converter.deserialize("0"))
        self.assertTrue(self.converter.deserialize(True))
        self.assertTrue(self.converter.deserialize(1))
        self.assertFalse(self.converter.deserialize(False))
        self.assertFalse(self.converter.deserialize(0))

    def test_serialize(self):
        self.assertEqual("true", self.converter.serialize(True))
        self.assertEqual("false", self.converter.serialize(False))


class IntConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(int)

    def test_deserialize(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("a")

        self.assertEqual(2, self.converter.deserialize("2"))
        self.assertEqual(2, self.converter.deserialize("+2"))
        self.assertEqual(-2, self.converter.deserialize("-2"))

    def test_serialize(self):
        self.assertEqual("2", self.converter.serialize(2))


class FloatConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(float)

    def test_deserialize(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("a")

        self.assertEqual(2.0, self.converter.deserialize("2"))
        self.assertEqual(2.1, self.converter.deserialize("2.1"))

    def test_serialize(self):
        self.assertEqual("2.1", self.converter.serialize(2.1))
        self.assertEqual("INF", self.converter.serialize(float("inf")))
        self.assertEqual("INF", self.converter.serialize(float("+inf")))
        self.assertEqual("-INF", self.converter.serialize(float("-inf")))
        self.assertEqual("NaN", self.converter.serialize(float("nan")))
        self.assertEqual("8.77683E-08", self.converter.serialize(float("8.77683E-8")))


class BytesConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(bytes)

    def test_serialize_with_base16_format(self):
        inputs = [
            ("312d322d33", "312D322D33"),
            ("312D322D33", "312D322D33"),
        ]

        for actual, expected in inputs:
            obj = self.converter.deserialize(actual, format="base16")
            output = self.converter.serialize(obj, format="base16")

            self.assertIsInstance(obj, bytes)
            self.assertEqual(b"1-2-3", obj)
            self.assertEqual(expected, output)

    def test_serialize_with_base64_format(self):
        obj = self.converter.deserialize("MS0yLTM=", format="base64")
        output = self.converter.serialize(obj, format="base64")

        self.assertIsInstance(obj, bytes)
        self.assertEqual(b"1-2-3", obj)
        self.assertEqual("MS0yLTM=", output)

    def test_serialize_raises_exception(self):

        with self.assertRaises(ConverterError) as cm:
            self.converter.deserialize(1, format="foo")

        self.assertEqual("Value must be str", str(cm.exception))

        with self.assertRaises(ConverterError):
            self.converter.deserialize("aaa", format="base16")

    def test_unknown_formats(self):
        with self.assertRaises(ConverterError):
            self.converter.serialize("foo")

        with self.assertRaises(ConverterError) as cm:
            self.converter.serialize("foo", format="foo")

        self.assertEqual("Unknown format 'foo'", str(cm.exception))

        with self.assertRaises(ConverterError):
            self.converter.deserialize("foo")

        with self.assertRaises(ConverterError):
            self.converter.deserialize("foo", format="foo")


class DecimalConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(Decimal)

    def test_deserialize(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("a")

        self.assertEqual(Decimal(1), self.converter.deserialize("1"))

    def test_serialize(self):
        self.assertEqual("2.1", self.converter.serialize(Decimal("2.1")))
        self.assertEqual("INF", self.converter.serialize(Decimal("inf")))
        self.assertEqual("INF", self.converter.serialize(Decimal("+inf")))
        self.assertEqual("-INF", self.converter.serialize(Decimal("-inf")))
        self.assertEqual("8.77683E-8", self.converter.serialize(Decimal("8.77683E-8")))


class DateTimeConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(datetime)

    def test_converter(self):
        original = "21 June 2018 15:40"
        fmt = "%d %B %Y %H:%M"
        obj = self.converter.deserialize(original, format=fmt)

        self.assertEqual(datetime(2018, 6, 21, 15, 40), obj)
        self.assertEqual(original, self.converter.serialize(obj, format=fmt))

    def test_serialize_raises_exception(self):
        with self.assertRaises(ConverterError):
            self.converter.serialize(datetime(2018, 6, 21, 15, 40))

        with self.assertRaises(ConverterError):
            self.converter.serialize(1, format="")

    def test_deserialize_raises_exception(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("21 June 2018 15:40", format="%Y")

        with self.assertRaises(ConverterError):
            self.converter.deserialize(1, format="%Y")

        with self.assertRaises(ConverterError):
            self.converter.deserialize("21 June 2018 15:40")

        with self.assertRaises(ConverterError):
            self.converter.deserialize("21 June 2018 15:40", format="")


class DateConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(date)

    def test_converter(self):
        original = "21 June 2018"
        fmt = "%d %B %Y"
        obj = self.converter.deserialize(original, format=fmt)

        self.assertEqual(date(2018, 6, 21), obj)
        self.assertEqual(original, self.converter.serialize(obj, format=fmt))


class TimeConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(time)

    def test_converter(self):
        original = "1255"
        fmt = "%H%M"
        obj = self.converter.deserialize(original, format=fmt)

        self.assertEqual(time(12, 55), obj)
        self.assertEqual(original, self.converter.serialize(obj, format=fmt))


class LxmlQNameConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(etree.QName)

    def test_deserialize(self):
        convert = self.converter.deserialize
        with self.assertRaises(ConverterError):
            convert("a:b")

        with self.assertRaises(ConverterError):
            self.assertEqual(etree.QName("b"), convert("a:b", ns_map={}))

        self.assertEqual(etree.QName("a"), convert("a", ns_map={}))
        self.assertEqual(etree.QName("aa", "b"), convert("a:b", ns_map={"a": "aa"}))

    def test_serialize(self):
        ns_map = {"c_prefix": "c"}
        convert = self.converter.serialize

        self.assertEqual("a", convert(etree.QName("a"), ns_map=ns_map))
        self.assertEqual("a", convert(etree.QName("a")))
        self.assertEqual("ns1:b", convert(etree.QName("a", "b"), ns_map=ns_map))
        self.assertEqual("{a}b", convert(etree.QName("a", "b")))
        self.assertEqual("c_prefix:c", convert(etree.QName("c", "c"), ns_map=ns_map))
        self.assertEqual("{c}c", convert(etree.QName("c", "c")))


class QNameConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(QName)

    def test_deserialize(self):
        convert = self.converter.deserialize
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
        self.assertEqual("Value is empty", str(cm.exception))

        self.assertEqual(QName("a"), convert("a", ns_map={}))
        self.assertEqual(QName("aa", "b"), convert("a:b", ns_map={"a": "aa"}))
        self.assertEqual(QName("{a}b"), convert("{a}b"))

    def test_serialize(self):
        ns_map = {"c_prefix": "c"}
        convert = self.converter.serialize

        self.assertEqual("a", convert(QName("a"), ns_map=ns_map))
        self.assertEqual("a", convert(QName("a")))
        self.assertEqual("ns1:b", convert(QName("a", "b"), ns_map=ns_map))
        self.assertEqual("{a}b", convert(QName("a", "b")))
        self.assertEqual("c_prefix:c", convert(QName("c", "c"), ns_map=ns_map))
        self.assertEqual("{c}c", convert(QName("c", "c")))


class EnumConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(Enum)

    def test_deserialize(self):
        class Fixture(Enum):
            two_point_one = 2.1

        convert = self.converter.deserialize
        with self.assertRaises(ConverterError):
            with warnings.catch_warnings(record=True) as w:
                convert("a", data_type=Fixture)

        self.assertEqual(0, len(w))

        self.assertEqual(Fixture.two_point_one, convert("2.1", data_type=Fixture))

    def test_deserialize_with_list_derived_enum(self):
        class Fixture(Enum):
            a = "a a a"

        convert = self.converter.deserialize
        self.assertEqual(Fixture.a, convert(" a \na a  ", data_type=Fixture))

    def test_deserialize_with_value_never_equal_to_anything(self):
        class Fixture(Enum):
            a = Decimal("NaN")

        convert = self.converter.deserialize
        self.assertEqual(Fixture.a, convert("NaN", data_type=Fixture))

        with self.assertRaises(ConverterError):
            convert("1.0", data_type=Fixture)

    def test_deserialize_raises_exception_on_missing_data_type(self):
        with self.assertRaises(ConverterError) as cm:
            self.converter.deserialize("a")

        self.assertEqual("Provide a target data type enum class.", str(cm.exception))

    def test_serialize(self):
        ns_map = {}
        fixture = self.Fixture
        self.assertEqual("ns0:b", self.converter.serialize(fixture.a, ns_map=ns_map))
        self.assertEqual("INF", self.converter.serialize(fixture.b))
        self.assertEqual("2.1", self.converter.serialize(fixture.c))

    class Fixture(Enum):
        a = QName("a", "b")
        b = Decimal("+inf")
        c = 2.1


class ProxyConverterTests(TestCase):
    def setUp(self):
        self.converter = ProxyConverter(lambda x: int(x))

    def test_deserialize(self):
        with self.assertRaises(ConverterError):
            self.converter.deserialize("a")

        self.assertEqual(1, self.converter.deserialize("1"))

    def test_serialize(self):
        self.assertEqual("1", self.converter.serialize(1))


class XmlDurationConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(XmlDuration)

    def test_deserialize(self):
        self.assertIsInstance(self.converter.deserialize("P20M"), XmlDuration)

        with self.assertRaises(ConverterError):
            self.converter.deserialize("P-20M")

    def test_serialize(self):
        actual = self.converter.serialize(XmlDuration("PT3S"))
        self.assertEqual("PT3S", actual)
        self.assertNotIsInstance(actual, XmlDuration)


class XmlPeriodConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(XmlPeriod)

    def test_deserialize(self):
        self.assertIsInstance(self.converter.deserialize("---15Z"), XmlPeriod)

        with self.assertRaises(ConverterError):
            self.converter.deserialize("---1Z")

    def test_serialize(self):
        actual = self.converter.serialize(XmlPeriod("---15Z"))
        self.assertEqual("---15Z", actual)
        self.assertNotIsInstance(actual, XmlPeriod)
