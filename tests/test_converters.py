from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
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
        self.assertEqual(1, to_python([int], "1"))
        self.assertEqual(1, to_python([int, str], "1"))
        self.assertEqual("1", to_python([str, int], "1"))
        self.assertEqual(1, to_python([str, int], "1", in_order=False))
        self.assertEqual("a", to_python([int], "a"))

    def test_to_python_float(self):
        """str > float in the ordering for now :("""
        self.assertEqual(1.0, to_python([float], "1"))
        self.assertEqual(1.0, to_python([float, str], "1"))
        self.assertEqual("1", to_python([str, float], "1"))
        self.assertEqual("1", to_python([str, float], "1", in_order=False))
        self.assertEqual("a", to_python([float], "a"))

    def test_to_python_boolean(self):
        """str > float in the ordering for now :("""
        for val in ("1", "true"):
            self.assertEqual(True, to_python([bool], val))
            self.assertEqual(True, to_python([bool, str], val))
            self.assertEqual(val, to_python([str, bool], val))
            self.assertEqual(True, to_python([str, bool], val, in_order=False))

        for val in ("0", "false"):
            self.assertEqual(False, to_python([bool], val))
            self.assertEqual(False, to_python([bool, str], val))
            self.assertEqual(val, to_python([str, bool], val))
            self.assertEqual(False, to_python([str, bool], val, in_order=False))

        self.assertEqual("a", to_python([bool], "a"))
        self.assertEqual(True, to_python([bool], "1 "))
        self.assertEqual(False, to_python([bool], "false "))

    def test_to_python_enum(self):
        class QNameType(Enum):
            a = QName("a")
            b = QName("b")

        self.assertEqual(UseType.OPTIONAL, to_python([UseType], "optional"))
        self.assertEqual("optional", to_python([str, UseType], "optional"))
        self.assertEqual(
            UseType.OPTIONAL, to_python([str, UseType], "optional", in_order=False)
        )
        self.assertEqual(QNameType.a, to_python([QNameType], "a"))

    def test_to_python_qname(self):
        ns_map = {"foo": "bar"}
        self.assertIsNone(to_python([QName], None, ns_map))
        self.assertEqual(QName("bar", "x"), to_python([QName], "foo:x", ns_map))
        self.assertEqual(QName("bar"), to_python([QName], "bar", None))

    def test_to_python_single_value_dataclass(self):
        @dataclass
        class Foo:
            value: int

        self.assertEqual(Foo("1"), to_python([Foo], "1"))
        self.assertEqual(1.0, to_python([float, UseType], "1"))
        self.assertEqual(Foo("1"), to_python([Foo], "1", in_order=False))

    def test_to_python_unhandled_type(self):
        class Foo:
            pass

        self.assertEqual("1", to_python([Foo], "1"))
