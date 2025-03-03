from unittest import TestCase

from xsdata.models.xsd import ComplexContent, SimpleContent


class ComplexContentTests(TestCase):
    def test_class(self) -> None:
        obj = ComplexContent()
        self.assertIsInstance(obj, SimpleContent)

        self.assertFalse(obj.mixed)
