from unittest import TestCase

from xsdata.models.xsd import List


class ListTests(TestCase):
    def test_is_attribute(self) -> None:
        obj = List()
        self.assertTrue(obj.is_property)

    def test_real_name(self) -> None:
        obj = List()
        self.assertEqual("value", obj.real_name)

    def test_real_type(self) -> None:
        obj = List()
        self.assertEqual([], list(obj.attr_types))

        obj.item_type = "foo"
        self.assertEqual(["foo"], list(obj.attr_types))

    def test_get_restrictions(self) -> None:
        obj = List()
        self.assertEqual({"tokens": True}, obj.get_restrictions())
