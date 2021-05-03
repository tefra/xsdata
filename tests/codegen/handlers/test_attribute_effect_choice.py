from xsdata.codegen.handlers import AttributeEffectiveChoiceHandler
from xsdata.codegen.models import Restrictions
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeEffectiveChoiceHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeEffectiveChoiceHandler()

    def test_process(self):
        target = ClassFactory.create()
        attrs = [
            AttrFactory.any(),
            AttrFactory.any(),
            # first group
            AttrFactory.any(restrictions=Restrictions(sequential=True)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            # break attr
            AttrFactory.any(),
            # second group
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=1)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
        ]
        target.attrs.extend(attrs)

        self.processor.process(target)

        self.assertIsNone(attrs[0].restrictions.choice)
        self.assertIsNone(attrs[1].restrictions.choice)

        # Part of the group but precedes list siblings
        self.assertIsNone(attrs[2].restrictions.choice)
        # Part of the group but both are lists
        self.assertIsNone(attrs[3].restrictions.choice)
        self.assertIsNone(attrs[4].restrictions.choice)

        # break attr
        self.assertIsNone(attrs[5].restrictions.choice)

        # Second group, mixed list non list sequential elements
        self.assertEqual("effective_1", attrs[6].restrictions.choice)
        self.assertEqual("effective_1", attrs[7].restrictions.choice)
        self.assertEqual("effective_1", attrs[8].restrictions.choice)
