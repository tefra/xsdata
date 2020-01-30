from unittest import TestCase

from xsdata.models.elements import ComplexContent
from xsdata.models.elements import SimpleContent


class ComplexContentTests(TestCase):
    def test_class(self):
        obj = ComplexContent.create()
        self.assertIsInstance(obj, SimpleContent)

        self.assertFalse(obj.mixed)
