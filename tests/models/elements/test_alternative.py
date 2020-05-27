from unittest import TestCase

from xsdata.models.xsd import Alternative


class AlternativeTests(TestCase):
    def test_property_real_name(self):
        obj = Alternative.create()
        self.assertEqual("value", obj.real_name)

        obj.id = "foo"
        self.assertEqual("foo", obj.real_name)

        obj.test = "@type='text'"
        self.assertEqual("type_text", obj.real_name)
