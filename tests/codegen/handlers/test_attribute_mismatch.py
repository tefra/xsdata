from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeMismatchHandler
from xsdata.exceptions import AnalyzerError


class AttributeMismatchHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeMismatchHandler

    def test_process(self):
        target = ClassFactory.elements(2)
        self.processor.process(target)

        self.assertEqual(2, len(target.attrs))
        self.assertEqual(0, len(target.inner))

        target = ClassFactory.enumeration(2)
        self.processor.process(target)

        self.assertEqual(2, len(target.attrs))
        self.assertEqual(0, len(target.inner))

        enumerations = list(target.attrs)
        target.attrs.append(AttrFactory.element())
        self.processor.process(target)

        self.assertEqual(1, len(target.attrs))
        self.assertEqual(1, len(target.inner))
        self.assertEqual(enumerations, target.inner[0].attrs)

        target.attrs.append(AttrFactory.enumeration())
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))
        self.assertEqual(1, len(target.inner))
        self.assertEqual(3, len(target.inner[0].attrs))

        target.attrs.append(AttrFactory.element())
        self.processor.process(target)
        self.assertEqual(2, len(target.attrs))
        self.assertEqual(1, len(target.inner))
        self.assertEqual(3, len(target.inner[0].attrs))

        target.attrs.append(AttrFactory.enumeration())

        with self.assertRaises(AnalyzerError) as cm:
            self.processor.process(target)

        self.assertEqual(
            "Mixed enumeration with more than one normal field.", str(cm.exception)
        )
