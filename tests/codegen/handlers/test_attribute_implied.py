from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeImpliedHandler
from xsdata.codegen.models import AttrType
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag


class AttributeImpliedHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.processor = AttributeImpliedHandler

    def test_process(self):
        item = ClassFactory.create()
        self.processor.process(item)
        self.assertEqual(0, len(item.attrs))

        item = ClassFactory.elements(2, mixed=True)
        self.processor.process(item)
        expected = AttrFactory.create(
            name="content",
            index=0,
            types=[AttrTypeFactory.xs_any()],
            tag=Tag.ANY,
            namespace="##any",
        )

        self.assertEqual(expected, item.attrs[0])
        self.assertEqual(3, len(item.attrs))

        self.processor.process(item)
        self.assertEqual(3, len(item.attrs))
