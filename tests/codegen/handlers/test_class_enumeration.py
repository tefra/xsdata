from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import ClassEnumerationHandler
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ClassEnumerationHandlerTests(FactoryTestCase):
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
                        AttrTypeFactory.create(qname=self.root_enum.qname),
                        AttrTypeFactory.create(
                            qname=self.inner_enum.qname, forward=True
                        ),
                    ],
                ),
            ]
        )
        self.target.inner.append(self.inner_enum)

        self.container = ClassContainer()
        self.container.add(self.target)
        self.container.add(self.root_enum)
        self.processor = ClassEnumerationHandler(container=self.container)

    def test_filter(self):
        target = ClassFactory.elements(2)
        self.processor.process(target)

        self.assertEqual(2, len(target.attrs))

        target.attrs.append(AttrFactory.enumeration())
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))
        self.assertTrue(target.attrs[0].is_enumeration)

    def test_flatten_skip_if_class_has_more_than_one_attribute(self):
        self.target.attrs.append(AttrFactory.create())
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)
        self.assertEqual(2, len(self.target.attrs))

    def test_flatten_skip_when_attribute_tag_is_not_union(self):
        self.target.attrs[0].tag = Tag.ELEMENT
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_flatten_skip_when_types_is_not_enumeration_union(self):
        self.target.attrs[0].types.append(AttrTypeFactory.native(DataType.INT))
        self.processor.process(self.target)
        self.assertFalse(self.target.is_enumeration)

    def test_flatten_merges_enumeration_unions(self):
        self.processor.process(self.target)
        self.assertTrue(self.target.is_enumeration)

        expected = self.root_enum.attrs + self.inner_enum.attrs
        self.assertEqual(expected, self.target.attrs)
        self.assertEqual(0, len(self.target.inner))

    def test_promote(self):
        target = ClassFactory.elements(2)
        inner = ClassFactory.enumeration(3)

        target.inner.append(inner)
        target.inner.append(ClassFactory.simple_type())  # Irrelevant
        attr_type = AttrTypeFactory.create(qname=inner.qname, forward=True)

        target.attrs[0].types.append(attr_type.clone())
        target.attrs[1].types.append(attr_type.clone())

        self.container.add(target)
        self.assertEqual(3, len(self.container.data))

        self.processor.process(target)

        new_qname = build_qname(inner.target_namespace, f"{target.name}_{inner.name}")

        self.assertEqual(4, len(self.container.data))
        new_inner = self.container.find(new_qname)

        self.assertEqual(1, len(target.inner))
        self.assertNotEqual(new_inner.qname, inner.qname)
        self.assertEqual(new_inner.attrs, inner.attrs)
        self.assertEqual(new_inner.qname, target.attrs[0].types[1].qname)
        self.assertEqual(new_inner.qname, target.attrs[1].types[1].qname)
        self.assertFalse(target.attrs[0].types[1].forward)
        self.assertFalse(target.attrs[1].types[1].forward)
