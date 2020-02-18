from unittest.case import TestCase

from xsdata.formats.dataclass.utils import safe_snake


class SafeSnakeTests(TestCase):
    def test_output(self):
        self.assertEqual("value_1", safe_snake("1"))
        self.assertEqual("value_minus_-1", safe_snake("-1"))
        self.assertEqual("value_--1", safe_snake("--1"))
        self.assertEqual("value", safe_snake(""))
        self.assertEqual("value_1 0-2e", safe_snake("1.0-2e"))
        self.assertEqual("value", safe_snake("τσου!!"))
        self.assertEqual("chris", safe_snake("chris"))

    def test_with_stop_words(self):
        self.assertEqual("def_value", safe_snake("def"))
