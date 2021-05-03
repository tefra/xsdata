from xsdata.codegen.handlers import AttributeRestrictionsHandler
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
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

    def test_reset_sequential(self):
        def len_sequential(target: Class):
            return len([attr for attr in target.attrs if attr.restrictions.sequential])

        restrictions = Restrictions(max_occurs=2, sequential=True)
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(restrictions=restrictions.clone()),
                AttrFactory.create(restrictions=restrictions.clone()),
            ]
        )

        attrs_clone = [attr.clone() for attr in target.attrs]

        self.processor.reset_sequential(target, 0)
        self.assertEqual(2, len_sequential(target))

        target.attrs[0].restrictions.sequential = False
        self.processor.reset_sequential(target, 0)
        self.assertEqual(1, len_sequential(target))

        self.processor.reset_sequential(target, 1)
        self.assertEqual(0, len_sequential(target))

        target.attrs = attrs_clone
        target.attrs[1].restrictions.sequential = False
        self.processor.reset_sequential(target, 0)
        self.assertEqual(0, len_sequential(target))

        target.attrs[0].restrictions.sequential = True
        target.attrs[0].restrictions.max_occurs = 0
        target.attrs[1].restrictions.sequential = True
        self.processor.reset_sequential(target, 0)
        self.assertEqual(1, len_sequential(target))
