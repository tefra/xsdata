from decimal import Decimal
from unittest import TestCase
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime
from xsdata.models.enums import DataType


class DataTypeTests(TestCase):
    def test_from_value_int(self):
        self.assertEqual(DataType.SHORT, DataType.from_value(-32768))
        self.assertEqual(DataType.SHORT, DataType.from_value(32767))

        self.assertEqual(DataType.INT, DataType.from_value(-32769))
        self.assertEqual(DataType.INT, DataType.from_value(32768))
        self.assertEqual(DataType.INT, DataType.from_value(-2147483648))
        self.assertEqual(DataType.INT, DataType.from_value(2147483647))

        self.assertEqual(DataType.LONG, DataType.from_value(-2147483649))
        self.assertEqual(DataType.LONG, DataType.from_value(2147483648))
        self.assertEqual(DataType.LONG, DataType.from_value(-9223372036854775808))
        self.assertEqual(DataType.LONG, DataType.from_value(9223372036854775807))

        self.assertEqual(DataType.INTEGER, DataType.from_value(-9223372036854775809))
        self.assertEqual(DataType.INTEGER, DataType.from_value(9223372036854775808))

    def test_from_value_float(self):
        self.assertEqual(DataType.FLOAT, DataType.from_value(-1.175494351e-38))
        self.assertEqual(DataType.FLOAT, DataType.from_value(3.402823466e38))

        self.assertEqual(DataType.DOUBLE, DataType.from_value(-1.175494352e-38))
        self.assertEqual(DataType.DOUBLE, DataType.from_value(3.402823467e38))

    def test_from_value_period(self):

        g_day = XmlPeriod("---20-02:44")
        self.assertEqual(DataType.G_DAY, DataType.from_value(g_day))

        g_month_day = XmlPeriod("--12-20-02:44")
        self.assertEqual(DataType.G_MONTH_DAY, DataType.from_value(g_month_day))

        g_month = XmlPeriod("--12")
        self.assertEqual(DataType.G_MONTH, DataType.from_value(g_month))

        g_year_month = XmlPeriod("2021-01")
        self.assertEqual(DataType.G_YEAR_MONTH, DataType.from_value(g_year_month))

        g_year = XmlPeriod("2021")
        self.assertEqual(DataType.G_YEAR, DataType.from_value(g_year))

    def test_from_value_simple(self):
        self.assertEqual(DataType.BOOLEAN, DataType.from_value(True))
        self.assertEqual(DataType.DECIMAL, DataType.from_value(Decimal(1.1)))
        self.assertEqual(DataType.QNAME, DataType.from_value(QName("a")))
        self.assertEqual(DataType.STRING, DataType.from_value("a"))
        self.assertEqual(DataType.DATE, DataType.from_value(XmlDate(2021, 1, 1)))
        self.assertEqual(DataType.TIME, DataType.from_value(XmlTime(12, 1, 1)))
        self.assertEqual(
            DataType.DATE_TIME, DataType.from_value(XmlDateTime(2002, 1, 1, 12, 1, 1))
        )
        self.assertEqual(DataType.STRING, DataType.from_value(self))
