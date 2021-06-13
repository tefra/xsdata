from unittest import TestCase

from tests.fixtures.models import TypeC
from xsdata.formats.dataclass.compat import ClassType
from xsdata.formats.dataclass.compat import Dataclasses


class ClassTypeTests(TestCase):
    def test_score_object(self):
        class_type = Dataclasses()
        self.assertEqual(-1.0, class_type.score_object(None))

        obj = TypeC(1, "1", 1.1)
        self.assertEqual(5.0, class_type.score_object(obj))

        self.assertEqual(-1, class_type.score_object(None))
        self.assertEqual(1.0, class_type.score_object("a"))
        self.assertEqual(1.5, class_type.score_object(2.9))
