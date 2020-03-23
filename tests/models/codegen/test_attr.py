from tests.factories import AttrFactory
from tests.factories import FactoryTestCase
from xsdata.models.codegen import Attr


class AttrTests(FactoryTestCase):
    def test__post_init__(self):
        attr = Attr(name="foo", local_type="bar", index=0)
        self.assertEqual("foo", attr.local_name)

    def test__eq__(self):
        attr = AttrFactory.element()
        clone = attr.clone()

        self.assertIsNot(attr, clone)
        self.assertEqual(attr, clone)

        attr.default = "foo"
        self.assertEqual(attr, clone)

        attr.restrictions.length = 10
        self.assertEqual(attr, clone)

        attr.index = -1
        self.assertEqual(attr, clone)

        attr.namespace = __file__
        self.assertNotEqual(attr, clone)

    def test_property_is_attribute(self):
        self.assertTrue(AttrFactory.attribute().is_attribute)
        self.assertTrue(AttrFactory.any_attribute().is_attribute)
        self.assertFalse(AttrFactory.element().is_attribute)

    def test_property_is_enumeration(self):
        self.assertTrue(AttrFactory.enumeration().is_enumeration)
        self.assertFalse(AttrFactory.element().is_enumeration)

    def test_property_is_factory(self):
        self.assertTrue(AttrFactory.any_attribute().is_factory)

        element = AttrFactory.element()
        self.assertFalse(element.is_factory)

        element.restrictions.max_occurs = 2
        self.assertTrue(element.is_factory)

    def test_property_is_group(self):
        self.assertTrue(AttrFactory.group().is_group)
        self.assertTrue(AttrFactory.attribute_group().is_group)
        self.assertFalse(AttrFactory.element().is_group)
