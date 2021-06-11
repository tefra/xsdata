from unittest import TestCase

from tests.fixtures.models import TypeC
from xsdata.formats.dataclass.compat import CrossCompat


class CrossCompatTests(TestCase):
    def test_score_object(self):
        self.assertEqual(-1.0, CrossCompat.score_object(None))

        obj = TypeC(1, "1", 1.1)
        self.assertEqual(5.0, CrossCompat.score_object(obj))

        self.assertEqual(-1, CrossCompat.score_object(None))
        self.assertEqual(1.0, CrossCompat.score_object("a"))
        self.assertEqual(1.5, CrossCompat.score_object(2.9))
