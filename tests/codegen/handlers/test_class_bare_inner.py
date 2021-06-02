from xsdata.codegen.handlers import ClassBareInnerHandler
from xsdata.models.enums import DataType
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassBareInnerHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = ClassBareInnerHandler()

    def test_process(self):
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
