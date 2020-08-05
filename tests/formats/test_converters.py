import warnings
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from unittest import mock
from unittest import TestCase

from lxml.etree import QName

from tests.fixtures.books import BookForm
from xsdata.exceptions import ConverterError
from xsdata.formats.converters import to_python
from xsdata.formats.converters import to_xml
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.models.enums import UseType


class ConvertersTestCases(TestCase):
    def test_to_xml(self):
        self.assertEqual(None, to_xml(None))
        self.assertEqual("1", to_xml(1))
        self.assertEqual("1.5", to_xml(1.5))
        self.assertEqual("true", to_xml(True))
        self.assertEqual("false", to_xml(False))
        self.assertEqual("optional", to_xml(UseType.OPTIONAL))
        self.assertEqual("INF", to_xml(float("inf")))
        self.assertEqual("INF", to_xml(float("+inf")))
        self.assertEqual("-INF", to_xml(float("-inf")))
        self.assertEqual("NaN", to_xml(float("nan")))
        self.assertEqual("INF", to_xml(Decimal("inf")))
        self.assertEqual("INF", to_xml(Decimal("+inf")))
        self.assertEqual("-INF", to_xml(Decimal("-inf")))
        self.assertEqual("8.77683E-8", to_xml(Decimal("8.77683E-8")))
        self.assertEqual("8.77683E-08", to_xml(float("8.77683E-8")))
        self.assertEqual("a", to_xml(QName("a")))
        self.assertEqual("a", to_xml(QName("a")))
        self.assertEqual("{a}b", to_xml(QName("a", "b")))
        self.assertEqual("1 2", to_xml([1, 2]))
        self.assertEqual("INF optional", to_xml([float("inf"), UseType.OPTIONAL]))

        namespaces = Namespaces()
        namespaces.add("a", "aa")
        self.assertEqual("aa:b", to_xml(QName("a", "b"), namespaces))
        self.assertEqual("b", to_xml(QName("b"), namespaces))

        with self.assertRaises(ConverterError):
            to_xml(BookForm())

    def test_to_python_integer(self):
        self.assertEqual(1, to_python("1", [int]))
        self.assertEqual(1, to_python("1", [int, str]))
        self.assertEqual("1", to_python("1", [str, int]))

        with warnings.catch_warnings(record=True):
            self.assertEqual("a", to_python("a", [int]))

    def test_to_python_float(self):
        self.assertEqual(1.0, to_python("1", [float]))
        self.assertEqual(1.0, to_python("1", [float, str]))
        self.assertEqual("1", to_python("1", [str, float]))

        with warnings.catch_warnings(record=True):
            self.assertEqual("a", to_python("a", [float]))

    def test_to_python_decimal(self):
        self.assertEqual(1.0, to_python("1", [Decimal]))
        self.assertEqual(1.0, to_python("1", [Decimal, str]))
        self.assertEqual("1", to_python("1", [str, Decimal]))

        with warnings.catch_warnings(record=True):
            self.assertEqual("a", to_python("a", [Decimal]))

    def test_to_python_boolean(self):
        """str > float in the ordering for now :("""
        for val in ("1", "true"):
            self.assertEqual(True, to_python(val, [bool]))
            self.assertEqual(True, to_python(val, [bool, str]))
            self.assertEqual(val, to_python(val, [str, bool]))

        for val in ("0", "false"):
            self.assertEqual(False, to_python(val, [bool]))
            self.assertEqual(False, to_python(val, [bool, str]))
            self.assertEqual(val, to_python(val, [str, bool]))

        self.assertEqual(True, to_python("1 ", [bool]))
        self.assertEqual(False, to_python("false ", [bool]))

        with warnings.catch_warnings(record=True):
            self.assertEqual("a", to_python("a", [bool]))

    def test_to_python_enum(self):
        self.assertEqual(UseType.OPTIONAL, to_python("optional", [UseType]))
        self.assertEqual("optional", to_python("optional", [str, UseType]))

    def test_to_python_enum_qname(self):
        class QNameType(Enum):
            a = QName("a")
            b = QName("b")

        self.assertEqual(QNameType.a, to_python("a", [QNameType]))

    def test_to_python_enum_tokens(self):
        class Tokens(Enum):
            a = "a a a"

        self.assertEqual(Tokens.a, to_python("a   a  \n a", [Tokens]))

    def test_to_python_qname(self):
        ns_map = {"foo": "bar"}
        self.assertIsNone(to_python(None, [QName], ns_map))
        self.assertEqual(QName("bar", "x"), to_python("foo:x", [QName], ns_map))
        self.assertEqual(QName("bar"), to_python("bar", [QName], None))

    def test_to_python_single_value_dataclass(self):
        @dataclass
        class Foo:
            value: int

        self.assertEqual(Foo("1"), to_python("1", [Foo]))
        self.assertEqual(1.0, to_python("1", [float, UseType]))

    def test_to_python_unhandled_type(self):
        class Foo:
            pass

        with warnings.catch_warnings(record=True) as w:
            self.assertEqual("1", to_python("1", [Foo]))

            self.assertEqual(
                f"Failed to convert value `1` to one of {[Foo]}", str(w[-1].message)
            )
