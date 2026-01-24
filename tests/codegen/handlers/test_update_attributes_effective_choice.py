from xsdata.codegen.handlers import UpdateAttributesEffectiveChoice
from xsdata.codegen.models import Restrictions
from xsdata.utils.testing import AttrFactory, ClassFactory, FactoryTestCase


class UpdateAttributesEffectiveChoiceTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.processor = UpdateAttributesEffectiveChoice()

    def test_process(self) -> None:
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

    def test_process_symmetrical_sequence(self) -> None:
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

    def test_process_enumeration(self) -> None:
        target = ClassFactory.create(
            attrs=[
                AttrFactory.enumeration(name="a"),
                AttrFactory.enumeration(name="a"),
                AttrFactory.enumeration(name="a"),
            ]
        )

        self.processor.process(target)

        self.assertEqual(3, len(target.attrs))

    def test_reset_effective_choice_for_coverage(self) -> None:
        paths = [("g", 0, 1, 1), ("g", 1, 1, 1)]
        self.processor.reset_effective_choice(paths, 3, 4)

        self.assertEqual([("g", 0, 1, 1), ("g", 1, 1, 1)], paths)

    def test_process_elements_in_different_choice_blocks(self) -> None:
        """Test that elements in different choice blocks are not merged."""
        choice1_id = 12345
        choice2_id = 67890

        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="configOption",
                    namespace="",
                    restrictions=Restrictions(
                        min_occurs=0, max_occurs=1, choice=choice1_id
                    ),
                ),
                AttrFactory.element(
                    name="optionA",
                    namespace="",
                    restrictions=Restrictions(
                        min_occurs=0, max_occurs=1, choice=choice1_id
                    ),
                ),
                AttrFactory.element(
                    name="configOption",
                    namespace="",
                    restrictions=Restrictions(
                        min_occurs=0, max_occurs=1, choice=choice2_id
                    ),
                ),
                AttrFactory.element(
                    name="optionB",
                    namespace="",
                    restrictions=Restrictions(
                        min_occurs=0, max_occurs=1, choice=choice2_id
                    ),
                ),
            ]
        )

        self.processor.process(target)

        # Should not merge configOption elements since they're in different choice blocks
        self.assertEqual(4, len(target.attrs))
        self.assertEqual(
            ["configOption", "optionA", "configOption", "optionB"],
            [x.name for x in target.attrs],
        )

    def test_process_elements_in_same_choice_different_branches(self) -> None:
        """Test that elements in same choice but different branches are not merged.

        This tests the case where an element appears in multiple branches of the
        same choice, but at different nesting levels (different path lengths).
        Example XSD pattern:
            <xs:choice>
                <xs:sequence>
                    <xs:element name="a"/>
                    <xs:element name="b" minOccurs="0"/>
                </xs:sequence>
                <xs:element name="b"/>
            </xs:choice>
        The two 'b' elements are mutually exclusive (different branches of the
        same choice) and should not be grouped as repeating elements.
        """
        choice_id = 12345
        outer_seq_id = 11111
        inner_seq_id = 22222

        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="a",
                    namespace="ns",
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        choice=choice_id,
                        sequence=outer_seq_id,
                        path=[
                            ("s", outer_seq_id, 0, 1),
                            ("c", choice_id, 1, 1),
                            ("s", inner_seq_id, 1, 1),
                        ],
                    ),
                ),
                AttrFactory.element(
                    name="b",
                    namespace="ns",
                    restrictions=Restrictions(
                        min_occurs=0,
                        max_occurs=1,
                        choice=choice_id,
                        sequence=outer_seq_id,
                        path=[
                            ("s", outer_seq_id, 0, 1),
                            ("c", choice_id, 1, 1),
                            ("s", inner_seq_id, 1, 1),
                        ],
                    ),
                ),
                AttrFactory.element(
                    name="b",
                    namespace="ns",
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        choice=choice_id,
                        sequence=outer_seq_id,
                        path=[
                            ("s", outer_seq_id, 0, 1),
                            ("c", choice_id, 1, 1),
                        ],
                    ),
                ),
            ]
        )

        self.processor.process(target)

        # Should not merge 'b' elements since they have different path lengths
        # (different nesting levels within the same choice)
        self.assertEqual(3, len(target.attrs))
        self.assertEqual(["a", "b", "b"], [x.name for x in target.attrs])
        # Both 'b' elements should retain their original max_occurs=1
        self.assertEqual(1, target.attrs[1].restrictions.max_occurs)
        self.assertEqual(1, target.attrs[2].restrictions.max_occurs)
