import sys
import warnings
from datetime import date
from datetime import datetime
from datetime import time
from decimal import Decimal
from enum import Enum
from typing import Any
from unittest import TestCase
from xml.etree.ElementTree import QName

import pytest

from tests.fixtures.datatypes import Telephone
from xsdata.exceptions import ConverterError
from xsdata.formats.converter import Converter
from xsdata.formats.converter import converter
from xsdata.formats.converter import ProxyConverter
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.enums import UseType


class ConverterFactoryTests(TestCase):
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
        self.assertEqual("0.0000000877683", converter.serialize(Decimal("8.77683E-8")))
        self.assertEqual("8.77683E-08", converter.serialize(float("8.77683E-8")))

    def test_test(self):
        self.assertTrue(converter.test("1", [int]))
        self.assertTrue(converter.test("1", [float]))
        self.assertFalse(converter.test("1", [float], strict=True))
        self.assertFalse(converter.test(None, [int]))

        self.assertFalse(converter.test("a", [int]))
        self.assertTrue(converter.test("01", [int]))
        self.assertFalse(converter.test("01", [int], strict=True))
        self.assertTrue(converter.test("1", [int]))

        self.assertTrue(converter.test("0", [float]))
        self.assertFalse(converter.test("0", [float], strict=True))
        self.assertTrue(converter.test(".0", [float]))
        self.assertFalse(converter.test(".0", [float], strict=True))
        self.assertTrue(converter.test("1.0", [float]))

    def test_unknown_converter(self):
        class A:
            pass

        class B(A):
            pass

        with warnings.catch_warnings(record=True) as w:
            converter.serialize(B())

        self.assertEqual(f"No converter registered for `{B}`", str(w[-1].message))

    def test_register_converter(self):
        class MinusOneInt(int):
            pass

        class MinusOneIntConverter(Converter):
            def deserialize(self, value: str, **kwargs: Any) -> Any:
                return int(value) - 1

            def serialize(self, value: Any, **kwargs: Any) -> str:
                return str(value)

        self.assertEqual(1, converter.deserialize("1", [MinusOneInt]))

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


class StringConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(str)

    def test_deserialize(self):
        string = "foo"
        self.assertIs(string, self.converter.deserialize(string))
        self.assertEqual("1", self.converter.deserialize(1))

    def test_serialize(self):
        string = "foo"
        self.assertIs(string, self.converter.serialize(string))
        self.assertEqual("1", self.converter.serialize(1))


class BoolConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(bool)

    def test_deserialize(self):
        for invalid in ("True", "False", 1, 0):
            with self.assertRaises(ConverterError):
                self.converter.deserialize(invalid)

        self.assertTrue(self.converter.deserialize("true"))
        self.assertTrue(self.converter.deserialize("1"))
        self.assertFalse(self.converter.deserialize("false"))
        self.assertFalse(self.converter.deserialize("0"))
        self.assertTrue(self.converter.deserialize(True))
        self.assertFalse(self.converter.deserialize(False))

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

        self.assertEqual("Input value must be 'str' got 'int'", str(cm.exception))

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
        self.assertEqual(
            "0.0000000877683", self.converter.serialize(Decimal("8.77683E-8"))
        )


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


class QNameConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(QName)

    def test_deserialize(self):
        convert = self.converter.deserialize

        invalid = ["a:b", "", " ", "{a}1b", "{a} b", "{|}b", "a a"]

        for inv in invalid:
            with self.assertRaises(ConverterError):
                convert(inv)

        self.assertEqual(QName("{a}b"), convert("{a}b"))
        self.assertEqual(QName("a"), convert("a", ns_map={}))
        self.assertEqual(QName("aa", "b"), convert("a:b", ns_map={"a": "aa"}))

    def test_serialize(self):
        ns_map = {"c_prefix": "c"}
        convert = self.converter.serialize

        self.assertEqual("a", convert(QName("a"), ns_map=ns_map))
        self.assertEqual("a", convert(QName("a")))
        self.assertEqual("ns1:b", convert(QName("a", "b"), ns_map=ns_map))
        self.assertEqual("{a}b", convert(QName("a", "b")))
        self.assertEqual("c_prefix:c", convert(QName("c", "c"), ns_map=ns_map))
        self.assertEqual("{c}c", convert(QName("c", "c")))


class EnumA(Enum):
    A = QName("a", "b")
    B = Decimal("+inf")
    C = 2.1
    D = (2.1, "a")
    E = (2.1, "a", float("nan"))
    F = (2.1, "a", 2)
    G = "x y z"
    H = Telephone(1, 2, 3)
    J = (Telephone(1, 2, 3), Telephone(4, 5, 6))


class EnumConverterTests(TestCase):
    def setUp(self):
        self.converter = converter.type_converter(Enum)

    @pytest.mark.skipif(
        sys.version_info == (3, 11, 1, "final", 0),
        reason="https://github.com/python/cpython/issues/100098",
    )
    def test_deserialize(self):
        convert = self.converter.deserialize
        self.assertEqual(EnumA.C, convert("2.1", data_type=EnumA))
        self.assertEqual(EnumA.C, convert(2.1, data_type=EnumA))
        self.assertEqual(EnumA.E, convert(["2.1", "a", "NaN"], data_type=EnumA))
        self.assertEqual(EnumA.F, convert([2.1, "a", 2], data_type=EnumA))
        self.assertEqual(EnumA.D, convert("  2.1  a ", data_type=EnumA))
        self.assertEqual(EnumA.G, convert("  x \n y z ", data_type=EnumA))
        self.assertEqual(EnumA.H, convert("1-2-3", data_type=EnumA))
        self.assertEqual(EnumA.J, convert(("1-2-3", "4-5-6"), data_type=EnumA))

        with self.assertRaises(ConverterError) as cm:
            convert(["2.1", "a", "NaN"], data_type=int)

        self.assertEqual("'<class 'int'>' is not an enum", str(cm.exception))

        with self.assertRaises(ConverterError):
            convert("nope", data_type=EnumA)

    def test_serialize(self):
        ns_map = {}
        self.assertEqual("ns0:b", self.converter.serialize(EnumA.A, ns_map=ns_map))
        self.assertEqual("INF", self.converter.serialize(EnumA.B))
        self.assertEqual("2.1", self.converter.serialize(EnumA.C))


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
