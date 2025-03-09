from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import MergeDuplicateClasses
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import (
    AttrFactory,
    ClassFactory,
    FactoryTestCase,
)


class MergeDuplicateClassesTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = MergeDuplicateClasses(container=self.container)

    def test_run_merges_same_classes(self) -> None:
        first = ClassFactory.create()
        second = first.clone()
        third = first.clone()
        fourth = ClassFactory.create()
        fifth = ClassFactory.create()

        self.container.extend([first, second, third, fourth, fifth])
        self.processor.run()

        self.assertEqual([first, fourth, fifth], list(self.container))
        self.assertEqual(
            {first.ref: third.ref, second.ref: third.ref}, self.processor.merges
        )

    def test_update_references(self) -> None:
        target = ClassFactory.create()
        target.attrs.append(AttrFactory.reference(qname="foo", reference=1))
        target.attrs.append(
            AttrFactory.reference(
                qname="thug",
                reference=2,
            )
        )
        self.processor.merges = {2: 3}
        self.processor.update_references(target)

        self.assertEqual(1, target.attrs[0].types[0].reference)
        self.assertEqual(3, target.attrs[1].types[0].reference)
