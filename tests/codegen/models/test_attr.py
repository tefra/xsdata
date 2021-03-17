import sys

from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import FactoryTestCase


class AttrTests(FactoryTestCase):
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

    def test_property_is_list(self):
        attr = AttrFactory.create(restrictions=Restrictions(max_occurs=2))
        self.assertTrue(attr.is_list)

        attr.restrictions.max_occurs = 1
        self.assertFalse(attr.is_list)

    def test_property_is_optional(self):
        attr = AttrFactory.create(restrictions=Restrictions(min_occurs=0))
        self.assertTrue(attr.is_optional)

        attr.restrictions.min_occurs = 1
        self.assertFalse(attr.is_optional)

    def test_property_is_suffix(self):
        attr = AttrFactory.create()
        self.assertFalse(attr.is_suffix)

        attr.index = sys.maxsize
        self.assertTrue(attr.is_suffix)

    def test_property_is_wild_attr(self):
        attr = AttrFactory.create()
        self.assertFalse(attr.is_wildcard)

        attr = AttrFactory.any()
        self.assertTrue(attr.is_wildcard)

    def test_property_is_xsi_type(self):
        attr = AttrFactory.create()
        self.assertFalse(attr.is_xsi_type)

        attr.namespace = Namespace.XSI.uri
        self.assertFalse(attr.is_xsi_type)

        attr.name = "type"
        self.assertTrue(attr.is_xsi_type)

    def test_property_is_nameless(self):
        self.assertFalse(AttrFactory.create(tag=Tag.ELEMENT).is_nameless)
        self.assertFalse(AttrFactory.create(tag=Tag.ATTRIBUTE).is_nameless)
        self.assertTrue(AttrFactory.create(tag=Tag.ANY).is_nameless)

    def test_property_native_types(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.create(qname="foo"),
                AttrTypeFactory.native(DataType.INT),
                AttrTypeFactory.native(DataType.SHORT),
                AttrTypeFactory.native(DataType.INTEGER),
                AttrTypeFactory.native(DataType.FLOAT),
            ]
        )

        self.assertCountEqual([float, int], attr.native_types)

    def test_property_xml_type(self):
        attr = AttrFactory.create(tag=Tag.ELEMENT)
        self.assertEqual("Element", attr.xml_type)

        attr = AttrFactory.create(tag=Tag.ATTRIBUTE)
        self.assertEqual("Attribute", attr.xml_type)

        attr = AttrFactory.create(tag=Tag.ANY_ATTRIBUTE)
        self.assertEqual("Attributes", attr.xml_type)

        attr = AttrFactory.create(tag=Tag.ANY)
        self.assertEqual("Wildcard", attr.xml_type)

        attr = AttrFactory.create(tag=Tag.RESTRICTION)
        self.assertIsNone(attr.xml_type)
