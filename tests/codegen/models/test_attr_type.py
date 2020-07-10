from tests.factories import AttrTypeFactory
from tests.factories import FactoryTestCase


class AttrTypeTests(FactoryTestCase):
    def test_property_is_dependency(self):

        attr_type = AttrTypeFactory.create(forward=True, native=True, circular=True)
        self.assertFalse(attr_type.is_dependency)

        attr_type.forward = False
        self.assertFalse(attr_type.is_dependency)

        attr_type.native = False
        self.assertFalse(attr_type.is_dependency)

        attr_type.circular = False
        self.assertTrue(attr_type.is_dependency)

    def test_native_property(self):
        attr_type = AttrTypeFactory.xs_int()
        self.assertEqual("int", attr_type.native_name)
        self.assertEqual("integer", attr_type.native_code)
        self.assertEqual(int, attr_type.native_type)

    def test_non_native_property(self):
        attr_type = AttrTypeFactory.create(qname="foo")
        self.assertIsNone(attr_type.native_name)
        self.assertIsNone(attr_type.native_code)
        self.assertIsNone(attr_type.native_type)
