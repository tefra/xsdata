import sys

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeMixedContentHandler
from xsdata.models.enums import Tag


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
            types=[AttrTypeFactory.xs_any()],
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
