from unittest import TestCase

from xsdata.models.xsd import ComplexContent
from xsdata.models.xsd import ComplexType


class ComplexTypeTests(TestCase):
    def test_property_is_mixed(self):
        obj = ComplexType()

        self.assertFalse(obj.is_mixed)

        obj.complex_content = ComplexContent()
        self.assertFalse(obj.is_mixed)

        obj.complex_content.mixed = True
        self.assertTrue(obj.is_mixed)

        obj.complex_content.mixed = False
        obj.mixed = True
        self.assertTrue(obj.is_mixed)
