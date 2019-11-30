from unittest import TestCase

from xsdata.models.elements import ComplexType


class ComplexTypeTests(TestCase):
    def test_property_extends(self):
        obj = ComplexType.create()
        self.assertIsNone(obj.extends)
