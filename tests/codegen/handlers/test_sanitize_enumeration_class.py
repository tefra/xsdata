from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import SanitizeEnumerationClass
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType, Tag
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    FactoryTestCase,
)


class SanitizeEnumerationClassTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.root_enum = ClassFactory.enumeration(2)
        self.inner_enum = ClassFactory.enumeration(2)
        self.target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="value",
                    tag=Tag.UNION,
                    types=[
                        AttrTypeFactory.create(qname=self.root_enum.qname),
                        AttrTypeFactory.create(
                            qname=self.inner_enum.qname, forward=True
                        ),
                    ],
                ),
            ]
        )
        self.target.inner.append(self.inner_enum)

        self.container = ClassContainer(config=GeneratorConfig())
        self.container.add(self.target)
        self.container.add(self.root_enum)
        self.processor = SanitizeEnumerationClass(container=self.container)

    def test_filter(self) -> None:
        target = ClassFactory.elements(2)
        self.processor.process(target)

        self.assertEqual(2, len(target.attrs))

        target.attrs.append(AttrFactory.enumeration())
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))
        self.assertTrue(target.attrs[0].is_enumeration)

    def test_flatten_skip_if_class_has_more_than_one_attribute(self) -> None:
        self.target.attrs.append(AttrFactory.create())
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)
        self.assertEqual(2, len(self.target.attrs))

    def test_flatten_skip_when_attribute_tag_is_not_union(self) -> None:
        self.target.attrs[0].tag = Tag.ELEMENT
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_flatten_skip_when_types_is_not_enumeration_union(self) -> None:
        self.target.attrs[0].types.append(AttrTypeFactory.native(DataType.INT))
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_flatten_merges_enumeration_unions(self) -> None:
        self.processor.process(self.target)
        self.assertTrue(self.target.is_enumeration)

        expected = self.root_enum.attrs + self.inner_enum.attrs
        self.assertEqual(expected, self.target.attrs)
        self.assertEqual(0, len(self.target.inner))
