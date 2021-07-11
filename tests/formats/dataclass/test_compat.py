from unittest import TestCase

from tests.fixtures.models import TypeA
from tests.fixtures.models import TypeC
from xsdata.exceptions import XmlContextError
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


class DataclassesTests(TestCase):
    def test_is_model(self):
        class_type = Dataclasses()
        self.assertTrue(class_type.is_model(TypeA))
        self.assertTrue(class_type.is_model(TypeA(1)))
        self.assertFalse(class_type.is_model(1))

    def test_verify_model(self):
        class_type = Dataclasses()
        class_type.verify_model(TypeA)

        with self.assertRaises(XmlContextError) as cm:
            class_type.verify_model(int)

        self.assertEqual(f"Type '{int}' is not a dataclass.", str(cm.exception))
