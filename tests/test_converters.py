from dataclasses import dataclass
from decimal import Decimal
from unittest import TestCase

from xsdata.formats.converters import to_python
from xsdata.formats.converters import to_xml
from xsdata.models.enums import UseType


class ConvertersTestCases(TestCase):
    def test_to_xml(self):
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
        self.assertEqual(UseType.OPTIONAL, to_python([UseType], "optional"))
        self.assertEqual("optional", to_python([str, UseType], "optional"))
        self.assertEqual(
            UseType.OPTIONAL, to_python([str, UseType], "optional", in_order=False)
        )

    def test_to_python_single_value_dataclass(self):
        @dataclass
        class Foo:
            value: int

        self.assertEqual(Foo("1"), to_python([Foo], "1"))
        self.assertEqual(1.0, to_python([float, UseType], "1"))
        self.assertEqual(Foo("1"), to_python([Foo], "1", in_order=False))
