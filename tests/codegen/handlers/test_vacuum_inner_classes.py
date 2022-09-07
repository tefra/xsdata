from typing import Generator

from xsdata.codegen.handlers import VacuumInnerClasses
from xsdata.models.enums import DataType
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class VacuumInnerClassesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = VacuumInnerClasses()

    def test_remove_duplicate_inners(self):
        target = ClassFactory.elements(3)

        inner_1 = ClassFactory.elements(2)
        inner_2 = inner_1.clone()

        target.inner.extend([inner_1, inner_2])

        target.attrs[1].types[0].qname = inner_1.qname
        target.attrs[1].types[0].forward = True
        target.attrs[1].types[0].reference = 4

        target.attrs[2].types[0].qname = inner_2.qname
        target.attrs[2].types[0].forward = True
        target.attrs[2].types[0].circular = True
        target.attrs[2].types[0].reference = 5

        self.processor.process(target)
        self.assertEqual(1, len(target.inner))

    def test_remove_inner(self):
        target = ClassFactory.elements(3)

        inner_1 = ClassFactory.elements(2)
        inner_2 = ClassFactory.create(extensions=ExtensionFactory.list(2))

        inner_3 = ClassFactory.create()
        inner_4 = ClassFactory.create(
            extensions=[ExtensionFactory.reference("foo", reference=15)]
        )

        target.inner.extend([inner_1, inner_2, inner_3, inner_4])

        target.attrs[1].types[0].qname = inner_3.qname
        target.attrs[1].types[0].forward = True
        target.attrs[1].types[0].reference = 4

        target.attrs[2].types[0].qname = inner_4.qname
        target.attrs[2].types[0].forward = True
        target.attrs[2].types[0].circular = True
        target.attrs[2].types[0].reference = 5

        self.processor.process(target)

        self.assertEqual(2, len(target.inner))

        # Not bare: has attrs
        self.assertIn(inner_1, target.inner)
        # Not bare: has more than one extension
        self.assertIn(inner_2, target.inner)

        self.assertEqual(str(DataType.ANY_SIMPLE_TYPE), target.attrs[1].types[0].qname)
        self.assertEqual(0, target.attrs[1].types[0].reference)
        self.assertFalse(target.attrs[1].types[0].forward)
        self.assertFalse(target.attrs[1].types[0].circular)
        self.assertTrue(target.attrs[1].types[0].native)

        self.assertEqual(
            inner_4.extensions[0].type.qname, target.attrs[2].types[0].qname
        )
        self.assertEqual(
            inner_4.extensions[0].type.reference, target.attrs[2].types[0].reference
        )
        self.assertFalse(target.attrs[2].types[0].forward)
        self.assertFalse(target.attrs[2].types[0].circular)
        self.assertFalse(target.attrs[2].types[0].native)

    def test_rename_inner(self):
        outer = ClassFactory.create(qname="{xsdata}foo")
        inner = ClassFactory.elements(1, qname="{xsdata}foo")
        outer.attrs.append(AttrFactory.reference(inner.qname, forward=True))
        outer.inner.append(inner)

        self.assertEqual("{xsdata}foo", outer.attrs[0].types[0].qname)
        self.assertEqual("{xsdata}foo", outer.inner[0].qname)

        self.processor.process(outer)

        self.assertEqual("{xsdata}foo_Inner", outer.attrs[0].types[0].qname)
        self.assertEqual("{xsdata}foo_Inner", outer.inner[0].qname)

    def test_find_attr_types_with_attr_choices(self):
        choices = [
            AttrFactory.create(
                types=[
                    AttrTypeFactory.create("bar", forward=True),
                    AttrTypeFactory.create("foo", forward=True),
                ]
            ),
            AttrFactory.reference("foo"),
            AttrFactory.reference("foo", forward=True),
            AttrFactory.reference("bar", forward=True),
        ]
        choice = AttrFactory.create(
            name="attr_B_Or_attr_C",
            tag="Choice",
            index=0,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            choices=choices,
        )
        target = ClassFactory.create()
        target.attrs.append(choice)

        result = self.processor.find_attr_types(target, "foo")
        self.assertIsInstance(result, Generator)

        self.assertEqual(choices[0].types[1], next(result))
        self.assertEqual(choices[2].types[0], next(result))
        self.assertIsNone(next(result, None))

        result = self.processor.find_attr_types(target, "bar")
        self.assertEqual(choices[0].types[0], next(result))
        self.assertEqual(choices[3].types[0], next(result))
        self.assertIsNone(next(result, None))
