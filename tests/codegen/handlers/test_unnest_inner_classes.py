from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import UnnestInnerClasses
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class UnnestInnerClassesTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = UnnestInnerClasses(container=self.container)

    def test_process_with_config_enabled(self) -> None:
        self.container.config.output.unnest_classes = True
        a = ClassFactory.create()
        b = ClassFactory.create()
        c = ClassFactory.create()

        a.attrs.append(AttrFactory.reference(b.qname, forward=True))
        b.attrs.append(AttrFactory.reference(c.qname, forward=True))
        c.attrs.append(AttrFactory.reference(b.qname, forward=True))

        a.inner.append(b)
        b.inner.append(c)
        b.parent = a
        c.parent = b

        self.container.add(a)
        self.processor.process(a)
        self.assertEqual(3, len(list(self.container)))

        self.assertEqual(b.qname, a.attrs[0].types[0].qname)
        self.assertEqual(c.qname, b.attrs[0].types[0].qname)
        self.assertEqual(b.qname, c.attrs[0].types[0].qname)

    def test_process_with_config_disabled_promotes_only_enumerations(self) -> None:
        self.container.config.output.unnest_classes = False
        a = ClassFactory.create()
        b = ClassFactory.create()
        c = ClassFactory.enumeration(2)

        a.attrs.append(AttrFactory.reference(b.qname, forward=True))
        b.attrs.append(AttrFactory.reference(c.qname, forward=True))

        a.inner.append(b)
        b.inner.append(c)
        b.parent = a
        c.parent = b

        self.container.add(a)
        self.processor.process(a)

        self.assertEqual(2, len(list(self.container)))
        self.assertEqual(c.qname, b.attrs[0].types[0].qname)
        self.assertEqual(1, len(a.inner))
        self.assertEqual(0, len(b.inner))

    def test_process_with_orphan_nested_class(self) -> None:
        self.container.config.output.unnest_classes = True
        a = ClassFactory.create()
        b = ClassFactory.create()
        c = ClassFactory.create()

        a.inner.append(b)
        b.inner.append(c)
        b.parent = a
        c.parent = b

        self.container.add(a)
        self.processor.process(a)
        self.assertEqual(1, len(list(self.container)))
        self.assertEqual(0, len(a.inner))
        self.assertEqual(1, len(b.inner))

    def test_update_inner_class(self) -> None:
        a = ClassFactory.create(qname="a")
        b = ClassFactory.create(qname="b")
        c = ClassFactory.create(qname="c")
        a.inner.append(b)
        b.inner.append(c)
        b.parent = a
        c.parent = b

        self.processor.update_inner_class(c)

        self.assertEqual("b_c", c.qname)
        self.assertTrue(c.local_type)
        self.assertIsNone(c.parent)
        self.assertEqual(0, len(b.inner))

    def test_update_types(self) -> None:
        types = [
            AttrTypeFactory.create(qname="a", forward=True),
            AttrTypeFactory.create(qname="a", forward=True),
        ]
        inner = ClassFactory.create()

        self.processor.update_types(types, inner)

        for tp in types:
            self.assertEqual(inner.qname, tp.qname)
            self.assertEqual(inner.ref, tp.reference)
            self.assertFalse(tp.forward)
