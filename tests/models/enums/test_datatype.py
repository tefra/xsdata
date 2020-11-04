from decimal import Decimal
from unittest import TestCase
from xml.etree.ElementTree import QName

from xsdata.models.enums import DataType


class DataTypeTests(TestCase):
    def test_from_value(self):
        self.assertEqual(DataType.BOOLEAN, DataType.from_value(True))
        self.assertEqual(DataType.INT, DataType.from_value(1))
        self.assertEqual(DataType.FLOAT, DataType.from_value(1.1))
        self.assertEqual(DataType.DECIMAL, DataType.from_value(Decimal(1.1)))
        self.assertEqual(DataType.QNAME, DataType.from_value(QName("a")))
        self.assertEqual(DataType.STRING, DataType.from_value("a"))
