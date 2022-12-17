from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import FactoryTestCase


class AttrTypeTests(FactoryTestCase):
    def test_property_is_dependency(self):
        attr_type = AttrTypeFactory.create(forward=True, native=True, circular=True)
        self.assertFalse(attr_type.is_dependency(False))

        attr_type.forward = False
        self.assertFalse(attr_type.is_dependency(False))

        attr_type.native = False
        self.assertFalse(attr_type.is_dependency(False))

        # Allow circular
        self.assertTrue(attr_type.is_dependency(True))

        attr_type.circular = False
        self.assertTrue(attr_type.is_dependency(False))
