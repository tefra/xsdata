from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeMismatchHandler


class AttributeMismatchHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeMismatchHandler

    def test_process(self):
        target = ClassFactory.elements(2)
        self.processor.process(target)

        self.assertEqual(2, len(target.attrs))

        target.attrs.append(AttrFactory.enumeration())
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))
        self.assertTrue(target.attrs[0].is_enumeration)
