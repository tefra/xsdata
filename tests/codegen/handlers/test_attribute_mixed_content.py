import sys

from xsdata.codegen.handlers import AttributeMixedContentHandler
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeMixedContentHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = AttributeMixedContentHandler

    def test_process(self):
        item = ClassFactory.create()
        self.processor.process(item)
        self.assertEqual(0, len(item.attrs))

        item = ClassFactory.elements(2, mixed=True)
        self.processor.process(item)
        expected = AttrFactory.create(
            name="content",
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            tag=Tag.ANY,
            namespace="##any",
        )

        # Wildcard is not defined
        self.assertEqual(expected, item.attrs[0])
        self.assertTrue(item.attrs[0].is_list)
        self.assertEqual(3, len(item.attrs))
        self.assertTrue(item.attrs[0].mixed)

        # Wildcard is defined and is list
        item.attrs[0].restrictions.max_occurs = 3
        item.attrs[0].mixed = False
        self.processor.process(item)
        self.assertEqual(3, len(item.attrs))
        self.assertTrue(item.attrs[0].mixed)
        self.assertEqual(3, item.attrs[0].restrictions.max_occurs)

        # Wildcard is defined but not list
        item.attrs[0].restrictions.max_occurs = 1
        self.processor.process(item)
        self.assertTrue(item.attrs[0].is_list)
        self.assertEqual(sys.maxsize, item.attrs[0].restrictions.max_occurs)
