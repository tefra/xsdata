from unittest import TestCase

from xsdata.models.xsd import SimpleContent


class SimpleContentTests(TestCase):
    def test_property_extension(self):
        obj = SimpleContent.create()
        self.assertIsNone(obj.extends)
