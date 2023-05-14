from unittest import TestCase

from xsdata.models.xsd import Alternative


class AlternativeTests(TestCase):
    def test_property_real_name(self):
        obj = Alternative()
        self.assertEqual("value", obj.real_name)

        obj.id = "foo"
        self.assertEqual("foo", obj.real_name)

        obj.test = "@type='text'"
        self.assertEqual("type_text", obj.real_name)

    def test_property_bases(self):
        obj = Alternative()
        self.assertEqual([], list(obj.bases))

        obj.type = "foo"
        self.assertEqual(["foo"], list(obj.bases))

    def test_get_restrictions(self):
        obj = Alternative()
        self.assertEqual({"path": [("alt", id(obj), 0, 1)]}, obj.get_restrictions())
