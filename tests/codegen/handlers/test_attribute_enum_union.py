from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeEnumUnionClassHandler
from xsdata.models.elements import Element
from xsdata.models.elements import SimpleType


class AttributeEnumUnionHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.root_enum = ClassFactory.enumeration(2)
        self.inner_enum = ClassFactory.enumeration(2)
        self.target = ClassFactory.create(
            type=SimpleType,
            attrs=[
                AttrFactory.create(
                    name="value",
                    types=[
                        AttrTypeFactory.create(name=self.root_enum.name),
                        AttrTypeFactory.create(name=self.inner_enum.name, forward=True),
                        AttrTypeFactory.xs_int(),
                    ],
                ),
            ],
        )
        self.target.inner.append(self.inner_enum)

        container = ClassContainer.from_list([self.target, self.root_enum])
        self.processor = AttributeEnumUnionClassHandler(container=container)

    def test_process_skip_class_with_more_than_one_attribute(self):
        self.target.attrs.append(AttrFactory.create())
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)
        self.assertEqual(2, len(self.target.attrs))

    def test_process_skip_class_with_a_non_simple_type(self):
        self.target.type = Element
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_process_skip_class_with_non_enumerations_union(self):
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_process_merges_enumeration_unions(self):
        self.target.attrs[0].types.pop()
        self.processor.process(self.target)
        self.assertTrue(self.target.is_enumeration)

        expected = self.root_enum.attrs + self.inner_enum.attrs
        self.assertEqual(expected, self.target.attrs)
        self.assertEqual(0, len(self.target.inner))
