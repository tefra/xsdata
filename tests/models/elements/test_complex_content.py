from unittest import TestCase

from xsdata.models.xsd import ComplexContent
from xsdata.models.xsd import SimpleContent


class ComplexContentTests(TestCase):
    def test_class(self):
        obj = ComplexContent()
        self.assertIsInstance(obj, SimpleContent)

        self.assertFalse(obj.mixed)
