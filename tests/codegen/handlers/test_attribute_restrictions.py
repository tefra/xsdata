from xsdata.codegen.handlers import AttributeRestrictionsHandler
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeRestrictionsHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeRestrictionsHandler()

    def test_reset_occurrences(self):
        required = Restrictions(min_occurs=1, max_occurs=1)
        attr = AttrFactory.attribute(restrictions=required.clone())
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        tokens = Restrictions(required=True, tokens=True, min_occurs=1, max_occurs=1)
        attr = AttrFactory.element(restrictions=tokens.clone())
        self.processor.reset_occurrences(attr)
        self.assertFalse(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        attr = AttrFactory.element(restrictions=tokens.clone())
        attr.restrictions.max_occurs = 2
        self.processor.reset_occurrences(attr)
        self.assertFalse(attr.restrictions.required)
        self.assertIsNotNone(attr.restrictions.min_occurs)
        self.assertIsNotNone(attr.restrictions.max_occurs)

        multiple = Restrictions(min_occurs=0, max_occurs=2)
        attr = AttrFactory.create(tag=Tag.EXTENSION, restrictions=multiple)
        self.processor.reset_occurrences(attr)
        self.assertTrue(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        multiple = Restrictions(max_occurs=2, required=True)
        attr = AttrFactory.element(restrictions=multiple, fixed=True)
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.required)
        self.assertEqual(0, attr.restrictions.min_occurs)
        self.assertFalse(attr.fixed)

        attr = AttrFactory.element(restrictions=required.clone())
        self.processor.reset_occurrences(attr)
        self.assertTrue(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)

        restrictions = Restrictions(required=True, min_occurs=0, max_occurs=1)
        attr = AttrFactory.element(restrictions=restrictions, default="A", fixed=True)
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.required)
        self.assertIsNone(attr.restrictions.min_occurs)
        self.assertIsNone(attr.restrictions.max_occurs)
        self.assertIsNone(attr.default)
        self.assertFalse(attr.fixed)

        attr = AttrFactory.element(restrictions=required.clone(), default="A")
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.required)

        attr = AttrFactory.element(restrictions=required.clone(), fixed=True)
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.required)

        attr = AttrFactory.element(restrictions=required.clone())
        attr.restrictions.nillable = True
        self.processor.reset_occurrences(attr)
        self.assertIsNone(attr.restrictions.required)
