from unittest import TestCase

from xsdata.models.elements import Alternative
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Length
from xsdata.models.elements import Restriction
from xsdata.models.elements import SimpleType


class ElementTests(TestCase):
    def test_property_is_attribute(self):
        obj = Element.create()
        self.assertTrue(obj)

    def test_property_real_name(self):
        obj = Element.create(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            obj = Element.create()
            obj.real_name

    def test_property_real_type(self):
        obj = Element.create()
        self.assertIsNone(obj.real_type)

        # Inner classes depend on the this to be None
        obj.complex_type = ComplexType.create()
        self.assertIsNone(obj.real_type)

        restriction = Restriction.create(base="xs:int")
        obj.simple_type = SimpleType.create(restriction=restriction)
        self.assertEqual(restriction.base, obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.alternatives.append(Alternative.create(type="foo"))
        obj.alternatives.append(Alternative.create(type="bar"))
        obj.alternatives.append(Alternative.create(type="thug"))
        self.assertEqual("bar foo thug", obj.real_type)

    def test_property_extends(self):
        obj = Element.create()
        self.assertIsNone(obj.extends)

    def test_property_is_mixed(self):
        obj = Element.create()
        self.assertFalse(obj.is_mixed)

        obj.complex_type = ComplexType.create()
        self.assertFalse(obj.is_mixed)

        obj.complex_type.mixed = True
        self.assertTrue(obj.is_mixed)

    def test_get_restrictions(self):
        obj = Element.create(min_occurs=1, max_occurs=1)
        expected = {"required": True}
        self.assertEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.create(
            restriction=Restriction.create(length=Length.create(value=9))
        )
        expected.update({"length": 9})
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = False
        self.assertEqual(expected, obj.get_restrictions())

        obj.nillable = True
        expected.update({"nillable": True})
        self.assertEqual(expected, obj.get_restrictions())
