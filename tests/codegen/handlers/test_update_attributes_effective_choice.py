from xsdata.codegen.handlers import UpdateAttributesEffectiveChoice
from xsdata.codegen.models import Restrictions
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class UpdateAttributesEffectiveChoiceTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = UpdateAttributesEffectiveChoice()

    def test_process(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.attribute(
                    name="i",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.element(
                    name="a",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.element(
                    name="b",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.element(
                    name="a",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.element(
                    name="b",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
                AttrFactory.element(
                    name="a",
                    namespace="b",
                    restrictions=Restrictions(min_occurs=1, max_occurs=1),
                ),
            ]
        )

        self.processor.process(target)

        self.assertEqual(3, len(target.attrs))

        actual = [
            (
                x.name,
                x.restrictions.choice,
                x.restrictions.min_occurs,
                x.restrictions.max_occurs,
            )
            for x in target.attrs
        ]
        expected = [("i", None, 1, 1), ("a", -1, 3, 3), ("b", -1, 2, 2)]
        self.assertEqual(expected, actual)

    def test_process_symmetrical_sequence(self):
        restrictions = Restrictions(
            sequence=1,
            min_occurs=1,
            max_occurs=1,
            path=[("g", 0, 1, 1), ("s", 1, 1, 1)],
        )
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="a", namespace="b", restrictions=restrictions.clone()
                ),
                AttrFactory.element(
                    name="b", namespace="b", restrictions=restrictions.clone()
                ),
                AttrFactory.element(
                    name="a", namespace="b", restrictions=restrictions.clone()
                ),
                AttrFactory.element(
                    name="b", namespace="b", restrictions=restrictions.clone()
                ),
                AttrFactory.element(name="c", namespace="b"),
                AttrFactory.element(
                    name="d", namespace="b", restrictions=Restrictions(choice=1)
                ),
            ]
        )

        self.processor.process(target)

        self.assertEqual(4, len(target.attrs))

        actual = [
            (
                x.name,
                x.restrictions.choice,
                x.restrictions.sequence,
                x.restrictions.min_occurs,
                x.restrictions.max_occurs,
                x.restrictions.path,
            )
            for x in target.attrs
        ]
        expected = [
            ("a", None, 1, 2, 2, [("g", 0, 1, 1), ("s", 1, 1, 2)]),
            ("b", None, 1, 2, 2, [("g", 0, 1, 1), ("s", 1, 1, 2)]),
            ("c", None, None, None, None, []),
            ("d", 1, None, None, None, []),
        ]
        self.assertEqual(expected, actual)

    def test_process_enumeration(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.enumeration(name="a"),
                AttrFactory.enumeration(name="a"),
                AttrFactory.enumeration(name="a"),
            ]
        )

        self.processor.process(target)

        self.assertEqual(3, len(target.attrs))
