from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeEnumUnionHandler
from xsdata.models.enums import Tag
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class AttributeEnumUnionHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.root_enum = ClassFactory.enumeration(2)
        self.inner_enum = ClassFactory.enumeration(2)
        self.target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="value",
                    tag=Tag.UNION,
                    types=[
                        AttrTypeFactory.create(name=self.root_enum.name),
                        AttrTypeFactory.create(name=self.inner_enum.name, forward=True),
                    ],
                ),
            ],
        )
        self.target.inner.append(self.inner_enum)

        container = ClassContainer.from_list([self.target, self.root_enum])
        self.processor = AttributeEnumUnionHandler(container=container)

    def test_process_skip_when_class_has_more_than_one_attribute(self):
        self.target.attrs.append(AttrFactory.create())
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)
        self.assertEqual(2, len(self.target.attrs))

    def test_process_skip_when_attribute_tag_is_not_union(self):
        self.target.attrs[0].tag = Tag.ELEMENT
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_process_skip_when_types_is_not_enumeration_union(self):
        self.target.attrs[0].types.append(AttrTypeFactory.xs_int())
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_process_merges_enumeration_unions(self):
        self.processor.process(self.target)
        self.assertTrue(self.target.is_enumeration)

        expected = self.root_enum.attrs + self.inner_enum.attrs
        self.assertEqual(expected, self.target.attrs)
        self.assertEqual(0, len(self.target.inner))
