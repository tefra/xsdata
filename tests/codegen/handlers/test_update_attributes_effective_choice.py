from xsdata.codegen.handlers import UpdateAttributesEffectiveChoice
from xsdata.codegen.models import Restrictions
from xsdata.models.config import ChoiceMaxOccursStrategy, CompoundFields, GeneratorOutput
from xsdata.utils.testing import AttrFactory, ClassFactory, FactoryTestCase


class UpdateAttributesEffectiveChoiceTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        # Create a mock container for the processor
        from xsdata.codegen.container import ClassContainer
        from xsdata.models.config import GeneratorConfig, GeneratorOutput
        
        config = GeneratorConfig(
            output=GeneratorOutput()
        )
        container = ClassContainer(config)
        self.processor = UpdateAttributesEffectiveChoice(container)

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

    def test_choice_max_occurs_strategy_sum(self) -> None:
        """Test that SUM strategy (default) adds max_occurs values."""
        # Create processor with SUM strategy (default)
        from xsdata.codegen.container import ClassContainer
        from xsdata.models.config import GeneratorConfig
        
        config = GeneratorConfig()
        container = ClassContainer(config)
        processor = UpdateAttributesEffectiveChoice(container)
        
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="linkerCommandFile",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
                AttrFactory.element(
                    name="linkerCommandFile",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
            ]
        )

        processor.process(target)

        self.assertEqual(1, len(target.attrs))
        attr = target.attrs[0]
        self.assertEqual("linkerCommandFile", attr.name)
        self.assertEqual(0, attr.restrictions.min_occurs)  # 0 + 0
        self.assertEqual(2, attr.restrictions.max_occurs)  # 1 + 1 (SUM strategy)

    def test_choice_max_occurs_strategy_max(self) -> None:
        """Test that MAX strategy uses maximum max_occurs value."""
        # Create a mock container with MAX strategy config
        from xsdata.codegen.container import ClassContainer
        from xsdata.models.config import GeneratorConfig
        
        config = GeneratorConfig(
            output=GeneratorOutput(
                compound_fields=CompoundFields(
                    choice_max_occurs_strategy=ChoiceMaxOccursStrategy.MAX
                )
            )
        )
        container = ClassContainer(config)
        
        # Create processor with MAX strategy
        processor = UpdateAttributesEffectiveChoice(container)
        
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="linkerCommandFile",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
                AttrFactory.element(
                    name="linkerCommandFile",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
            ]
        )

        processor.process(target)

        self.assertEqual(1, len(target.attrs))
        attr = target.attrs[0]
        self.assertEqual("linkerCommandFile", attr.name)
        self.assertEqual(0, attr.restrictions.min_occurs)  # 0 + 0
        self.assertEqual(1, attr.restrictions.max_occurs)  # max(1, 1) (MAX strategy)

    def test_choice_max_occurs_strategy_max_different_values(self) -> None:
        """Test that MAX strategy works with different max_occurs values."""
        # Create a mock container with MAX strategy config
        from xsdata.codegen.container import ClassContainer
        from xsdata.models.config import GeneratorConfig
        
        config = GeneratorConfig(
            output=GeneratorOutput(
                compound_fields=CompoundFields(
                    choice_max_occurs_strategy=ChoiceMaxOccursStrategy.MAX
                )
            )
        )
        container = ClassContainer(config)
        
        # Create processor with MAX strategy
        processor = UpdateAttributesEffectiveChoice(container)
        
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(
                    name="element",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=1),
                ),
                AttrFactory.element(
                    name="element",
                    namespace="",
                    restrictions=Restrictions(min_occurs=0, max_occurs=3),
                ),
            ]
        )

        processor.process(target)

        self.assertEqual(1, len(target.attrs))
        attr = target.attrs[0]
        self.assertEqual("element", attr.name)
        self.assertEqual(0, attr.restrictions.min_occurs)  # 0 + 0
        self.assertEqual(3, attr.restrictions.max_occurs)  # max(1, 3) (MAX strategy)
