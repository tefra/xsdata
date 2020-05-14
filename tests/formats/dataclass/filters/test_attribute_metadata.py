from unittest import TestCase

from tests.factories import AttrFactory
from tests.factories import FactoryTestCase
from xsdata.formats.dataclass.filters import attribute_metadata
from xsdata.models.enums import Tag


class AttributeMetadataTests(FactoryTestCase):
    def test_attribute_metadata(self):
        attr = AttrFactory.element()
        expected = {"name": "attr_B", "type": "Element"}
        self.assertEqual(expected, attribute_metadata(attr, None))
        self.assertEqual(expected, attribute_metadata(attr, "foo"))

    def test_attribute_metadata_namespace(self):
        attr = AttrFactory.element(namespace="foo")
        expected = {"name": "attr_B", "namespace": "foo", "type": "Element"}

        self.assertEqual(expected, attribute_metadata(attr, None))
        self.assertNotIn("namespace", attribute_metadata(attr, "foo"))

        attr = AttrFactory.attribute(namespace="foo")
        expected = {"name": "attr_C", "namespace": "foo", "type": "Attribute"}

        self.assertEqual(expected, attribute_metadata(attr, None))
        self.assertIn("namespace", attribute_metadata(attr, "foo"))

    def test_attribute_metadata_name(self):
        attr = AttrFactory.element(local_name="foo", name="bar")
        actual = attribute_metadata(attr, None)
        self.assertEqual("foo", actual["name"])

        attr = AttrFactory.element(local_name="foo", name="Foo")
        self.assertNotIn("name", attribute_metadata(attr, None))

        attr = AttrFactory.create(tag=Tag.ANY, local_name="foo", name="bar")
        self.assertNotIn("name", attribute_metadata(attr, None))

    def test_attribute_metadata_restrictions(self):
        attr = AttrFactory.create(tag=Tag.RESTRICTION)
        attr.restrictions.max_occurs = 2
        attr.restrictions.required = False

        expected = {"max_occurs": 2}
        self.assertEqual(expected, attribute_metadata(attr, None))
