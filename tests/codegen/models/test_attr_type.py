from tests.factories import AttrTypeFactory
from tests.factories import FactoryTestCase
from xsdata.models.enums import DataType


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
