from xsdata.codegen.handlers import ResetAttributeSequences
from xsdata.codegen.models import Restrictions
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ResetAttributeSequencesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = ResetAttributeSequences()

    def test_process(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(),
                AttrFactory.element(restrictions=Restrictions(sequence=1)),
                AttrFactory.element(
                    restrictions=Restrictions(sequence=2, path=[("s", 2, 1, 1)]),
                ),
                AttrFactory.element(
                    restrictions=Restrictions(sequence=2, path=[("s", 2, 1, 1)]),
                ),
                AttrFactory.element(
                    restrictions=Restrictions(sequence=3, path=[("s", 3, 1, 1)]),
                ),
                # Effective choices
                AttrFactory.element(
                    restrictions=Restrictions(sequence=3, path=[("s", 3, 1, 2)]),
                ),
                AttrFactory.element(
                    restrictions=Restrictions(sequence=3, path=[("s", 3, 1, 2)]),
                ),
                # Nested Group Sequence
                AttrFactory.element(
                    restrictions=Restrictions(
                        sequence=4, path=[("g", 3, 1, 2), ("s", 4, 1, 1)]
                    ),
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        sequence=4, path=[("g", 3, 1, 2), ("s", 4, 1, 1)]
                    ),
                ),
            ]
        )

        self.processor.process(target)

        actual = [x.restrictions.sequence for x in target.attrs]
        expected = [None, None, None, None, None, 3, 3, 4, 4]
        self.assertEqual(expected, actual)

    def test_is_repeatable_sequence(self):
        attr = AttrFactory.create()
        self.assertFalse(self.processor.is_repeatable_sequence(attr))

        attr.restrictions.sequence = 1
        self.assertFalse(self.processor.is_repeatable_sequence(attr))

        attr.restrictions.path.append(("s", 15, 1, 2))
        self.assertTrue(self.processor.is_repeatable_sequence(attr))
