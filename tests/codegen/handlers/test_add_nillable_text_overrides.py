from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AddNillableTextOverrides
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import (
    AttrFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)


class AddNillableTextOverridesTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = AddNillableTextOverrides(container=self.container)

    def test_process(self) -> None:
        base = ClassFactory.create(
            attrs=[AttrFactory.extension(), AttrFactory.attribute()]
        )
        target = ClassFactory.create(
            nillable=True, extensions=[ExtensionFactory.reference(base.qname)]
        )
        self.container.extend([base, target])

        self.processor.process(target)

        self.assertEqual(1, len(target.attrs))
        self.assertEqual(base.attrs[0].name, target.attrs[0].name)
        self.assertTrue(target.attrs[0].is_nillable)
        self.assertFalse(base.attrs[0].is_nillable)

    def test_process_with_nillable_base_text(self) -> None:
        base = ClassFactory.create(attrs=[AttrFactory.extension()])
        base.attrs[0].restrictions.nillable = True
        target = ClassFactory.create(
            nillable=True, extensions=[ExtensionFactory.reference(base.qname)]
        )
        self.container.extend([base, target])

        self.processor.process(target)

        self.assertEqual(0, len(target.attrs))

    def test_process_with_own_text(self) -> None:
        base = ClassFactory.create(attrs=[AttrFactory.extension()])
        target = ClassFactory.create(
            nillable=True,
            attrs=[AttrFactory.extension()],
            extensions=[ExtensionFactory.reference(base.qname)],
        )
        self.container.extend([base, target])

        self.processor.process(target)

        self.assertEqual(1, len(target.attrs))

    def test_process_not_nillable(self) -> None:
        base = ClassFactory.create(attrs=[AttrFactory.extension()])
        target = ClassFactory.create(
            extensions=[ExtensionFactory.reference(base.qname)]
        )
        self.container.extend([base, target])

        self.processor.process(target)

        self.assertEqual(0, len(target.attrs))

    def test_process_without_base_text(self) -> None:
        base = ClassFactory.create(attrs=[AttrFactory.attribute()])
        target = ClassFactory.create(
            nillable=True, extensions=[ExtensionFactory.reference(base.qname)]
        )
        self.container.extend([base, target])

        self.processor.process(target)

        self.assertEqual(0, len(target.attrs))
