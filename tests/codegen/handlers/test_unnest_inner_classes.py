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
    def setUp(self):
        super().setUp()
        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = UnnestInnerClasses(container=self.container)

    def test_process(self):
        self.container.config.output.unnest_classes = False

        enumeration = ClassFactory.enumeration(2)
        local_type = ClassFactory.elements(2)
        target = ClassFactory.create()

        target.inner.append(enumeration)
        target.inner.append(local_type)
        self.container.add(target)

        self.processor.process(target)

        self.assertEqual(1, len(target.inner))
        self.assertTrue(local_type in target.inner)

        self.container.config.output.unnest_classes = True
        self.processor.process(target)
        self.assertEqual(0, len(target.inner))

    def test_promote_with_orphan_inner(self):
        inner = ClassFactory.elements(2)
        target = ClassFactory.create()
        target.inner.append(inner)
        self.container.add(target)

        self.processor.promote(target, inner)

        self.assertEqual(0, len(target.inner))
        self.assertEqual(1, len(self.container.data))

    def test_promote_updates_forward_attr_types(self):
        inner = ClassFactory.elements(2)
        attr = AttrFactory.reference(inner.qname, forward=True)
        target = ClassFactory.create()
        target.attrs.append(attr)
        target.inner.append(inner)
        self.container.add(target)

        self.processor.promote(target, inner)

        self.assertEqual(0, len(target.inner))
        self.assertEqual(2, len(self.container.data))
        self.assertFalse(attr.types[0].forward)
        self.assertEqual("{xsdata}class_C_class_B", attr.types[0].qname)

    def test_clone_class(self):
        target = ClassFactory.create(qname="{a}b")
        actual = self.processor.clone_class(target, "parent")

        self.assertIsNot(target, actual)
        self.assertTrue(actual.local_type)
        self.assertEqual("{a}parent_b", actual.qname)

    def test_clone_class_with_circular_reference(self):
        target = ClassFactory.create(qname="{a}b")
        target.attrs.append(
            AttrFactory.create(
                name="self",
                types=[AttrTypeFactory.create(qname=target.qname, circular=True)],
            )
        )

        actual = self.processor.clone_class(target, "parent")

        self.assertIsNot(target, actual)
        self.assertTrue(actual.local_type)
        self.assertEqual("{a}parent_b", actual.qname)

        self.assertTrue(actual.attrs[0].types[0].circular)
        self.assertEqual(actual.ref, actual.attrs[0].types[0].reference)
        self.assertEqual(actual.qname, actual.attrs[0].types[0].qname)

    def test_update_types(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.create(qname="a", forward=True),
                AttrTypeFactory.create(qname="a", forward=False),
                AttrTypeFactory.create(qname="b", forward=False),
            ]
        )
        source = ClassFactory.create()

        self.processor.update_types(attr, "a", source)

        self.assertEqual(source.qname, attr.types[0].qname)
        self.assertFalse(attr.types[0].forward)
        self.assertEqual(source.ref, attr.types[0].reference)

        self.assertEqual("a", attr.types[1].qname)
        self.assertFalse(attr.types[1].forward)
        self.assertEqual("b", attr.types[2].qname)
        self.assertFalse(attr.types[2].forward)

    def test_find_forward_attr(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create("a", forward=False),
                        AttrTypeFactory.create("b", forward=False),
                    ]
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create("a", forward=True),
                        AttrTypeFactory.create("b", forward=True),
                    ]
                ),
                AttrFactory.create(),
            ]
        )

        actual = self.processor.find_forward_attr(target, "a")
        self.assertEqual(target.attrs[1], actual)

        actual = self.processor.find_forward_attr(target, "b")
        self.assertEqual(target.attrs[1], actual)

        actual = self.processor.find_forward_attr(target, "c")
        self.assertIsNone(actual)
