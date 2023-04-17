from xsdata.codegen.handlers import MergeAttributes
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class MergeAttributesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = MergeAttributes

    def test_process_with_enumeration(self):
        target = ClassFactory.create()
        target.attrs = [
            AttrFactory.enumeration(default=1),
            AttrFactory.enumeration(default=1),
            AttrFactory.enumeration(default=2),
            AttrFactory.enumeration(default=2),
        ]

        self.processor.process(target)
        self.assertEqual([1, 2], [x.default for x in target.attrs])

    def test_process_with_non_enumeration(self):
        one = AttrFactory.attribute(fixed=True)
        one_clone = one.clone()
        restrictions = Restrictions(min_occurs=10, max_occurs=15)
        two = AttrFactory.element(restrictions=restrictions, fixed=True)
        two_clone = two.clone()
        two_clone.restrictions.min_occurs = 5
        two_clone.restrictions.max_occurs = 5
        two_clone_two = two.clone()
        two_clone_two.restrictions.min_occurs = 4
        two_clone_two.restrictions.max_occurs = 4
        three = AttrFactory.element()
        four = AttrFactory.enumeration()
        four_clone = four.clone()
        five = AttrFactory.element()
        five.types = [AttrTypeFactory.native(DataType.INT)]
        five_clone = five.clone()
        five_clone_two = five.clone()
        five_clone_two.restrictions.sequence = 1
        five_clone_two.types.append(AttrTypeFactory.native(DataType.FLOAT))

        target = ClassFactory.create(
            attrs=[
                one,
                one_clone,
                two,
                two_clone,
                two_clone_two,
                three,
                four,
                four_clone,
                five,
                five_clone,
                five_clone_two,
            ]
        )

        winners = [one, two, three, four, five]

        self.processor.process(target)
        self.assertEqual(winners, target.attrs)

        self.assertTrue(one.fixed)
        self.assertIsNone(one.restrictions.min_occurs)
        self.assertIsNone(one.restrictions.max_occurs)
        self.assertFalse(two.fixed)
        self.assertEqual(4, two.restrictions.min_occurs)
        self.assertEqual(24, two.restrictions.max_occurs)
        self.assertIsNone(three.restrictions.min_occurs)
        self.assertIsNone(three.restrictions.max_occurs)
        self.assertIsNone(four.restrictions.min_occurs)
        self.assertIsNone(four.restrictions.max_occurs)
        self.assertEqual(1, five.restrictions.sequence)
        self.assertEqual(0, five.restrictions.min_occurs)
        self.assertEqual(3, five.restrictions.max_occurs)
        self.assertEqual(["int", "float"], [x.name for x in five.types])
