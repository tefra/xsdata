import sys

from xsdata.codegen.handlers import AttributeMixedContentHandler
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeMixedContentHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = AttributeMixedContentHandler()

    def test_process(self):
        attrs = [
            AttrFactory.attribute(),  # keep
            AttrFactory.reference("foo"),  # choice
            AttrFactory.native(DataType.INT),  # choice
            AttrFactory.any(),  # drop
        ]
        item = ClassFactory.create(attrs=attrs)

        self.processor.process(item)
        self.assertEqual(4, len(item.attrs))

        item.mixed = True
        self.processor.process(item)

        self.assertEqual(2, len(item.attrs))
        self.assertEqual(attrs[0], item.attrs[0])

        expected = AttrFactory.any(
            mixed=True, name="content", namespace=NamespaceType.ANY_NS
        )
        expected.restrictions.min_occurs = 0
        expected.restrictions.max_occurs = sys.maxsize
        expected.choices = attrs[1:]

        self.assertEqual(expected, item.attrs[1])
