import sys

from xsdata.codegen.handlers import ProcessMixedContentClass
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ProcessMixedContentClassTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = ProcessMixedContentClass()

    def test_process(self):
        res = Restrictions(min_occurs=1, max_occurs=1, sequence=1)
        attrs = [
            AttrFactory.attribute(),  # keep
            AttrFactory.reference("foo", restrictions=res.clone()),  # choice
            AttrFactory.native(DataType.INT, restrictions=res.clone()),  # choice
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
        choices = []
        for attr in attrs[1:-1]:
            choice = attr.clone()
            choice.restrictions.min_occurs = None
            choice.restrictions.max_occurs = None
            choice.restrictions.sequence = None
            choices.append(choice)

        self.assertEqual(expected, item.attrs[1])
        self.assertEqual(choices, item.attrs[1].choices)
