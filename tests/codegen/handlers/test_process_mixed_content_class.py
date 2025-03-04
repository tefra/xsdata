import sys

from xsdata.codegen.handlers import ProcessMixedContentClass
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType, NamespaceType
from xsdata.utils.testing import AttrFactory, ClassFactory, FactoryTestCase


class ProcessMixedContentClassTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.processor = ProcessMixedContentClass()

    def test_process(self) -> None:
        res = Restrictions(min_occurs=1, max_occurs=1, sequence=1)
        attrs = [
            AttrFactory.attribute(),  # keep
            AttrFactory.reference("foo", restrictions=res.clone()),  # choice
            AttrFactory.native(DataType.INT, restrictions=res.clone()),  # choice
            AttrFactory.native(DataType.ANY_TYPE, restrictions=res.clone()),  # drop
            AttrFactory.any(),  # drop
        ]
        item = ClassFactory.create(attrs=attrs)

        self.processor.process(item)
        self.assertEqual(5, len(item.attrs))

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
        for attr in attrs[1:-2]:
            choice = attr.clone()
            choice.restrictions.min_occurs = None
            choice.restrictions.max_occurs = None
            choice.restrictions.sequence = None
            choices.append(choice)

        self.assertEqual(expected, item.attrs[1])
        self.assertEqual(choices, item.attrs[1].choices)
