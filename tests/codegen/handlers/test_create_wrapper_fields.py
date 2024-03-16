from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import CreateWrapperFields
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType, Tag
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)


class CreateWrapperFieldsTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.config = GeneratorConfig()
        self.config.output.wrapper_fields = True
        self.container = ClassContainer(config=self.config)
        self.processor = CreateWrapperFields(container=self.container)

        self.target = ClassFactory.create()
        self.target.attrs.append(
            AttrFactory.reference("foo", name="items", tag=Tag.ELEMENT)
        )

        self.source = ClassFactory.create(qname="foo")
        self.source.attrs.append(AttrFactory.native(DataType.STRING, name="item"))
        self.container.extend([self.target, self.source])

    def test_process_skip_with_config_disabled(self):
        self.config.output.wrapper_fields = False
        self.processor.process(self.target)
        self.assertIsNone(self.target.attrs[0].wrapper)

    def test_process_with_valid_attr_wrapper(self):
        self.processor.process(self.target)
        self.assertEqual("items", self.target.attrs[0].wrapper)

    def test_process_with_invalid_attr(self):
        self.target.attrs[0].tag = Tag.EXTENSION
        self.processor.process(self.target)

        self.assertIsNone(self.target.attrs[0].wrapper)

    def test_process_with_invalid_source(self):
        self.source.extensions.append(ExtensionFactory.create())
        self.processor.process(self.target)

        self.assertIsNone(self.target.attrs[0].wrapper)

    def test_wrap_field(self):
        source = AttrFactory.create()
        attr = AttrFactory.create()
        wrapper = attr.local_name

        self.processor.wrap_field(source, attr)
        self.assertEqual(source.name, attr.name)
        self.assertEqual(source.local_name, attr.local_name)
        self.assertEqual(wrapper, attr.wrapper)

    def test_find_source_with_forward_reference(self):
        tp = self.target.attrs[0].types[0]
        tp.forward = True
        self.target.inner.append(self.source)

        actual = self.processor.find_source(self.target, tp)
        self.assertEqual(self.source, actual)

    def test_validate_attr(self):
        # Not an element
        attr = AttrFactory.create(tag=Tag.EXTENSION)
        self.assertFalse(self.processor.validate_attr(attr))

        # Multiple types
        attr.tag = Tag.ELEMENT
        attr.types = AttrTypeFactory.list(2)
        self.assertFalse(self.processor.validate_attr(attr))

        # Native type
        attr.types = [AttrTypeFactory.native(DataType.STRING)]
        self.assertFalse(self.processor.validate_attr(attr))

        # Not any of the above issues
        attr.types = [AttrTypeFactory.create()]
        self.assertTrue(self.processor.validate_attr(attr))

    def test_validate_source(self):
        source = ClassFactory.create()

        # Has extensions
        source.extensions = ExtensionFactory.list(1)
        self.assertFalse(self.processor.validate_source(source, None))

        # Has multiple attrs
        source.extensions.clear()
        source.attrs = AttrFactory.list(2)
        self.assertFalse(self.processor.validate_source(source, None))

        # Has forwarded references
        source.attrs.pop(0)
        source.attrs[0].types[0].forward = True
        self.assertFalse(self.processor.validate_source(source, None))

        # Namespace doesn't match
        source.attrs[0].types[0].forward = False
        self.assertFalse(self.processor.validate_source(source, "bar"))

        # Not any of the above issues
        source.attrs[0].namespace = "bar"
        self.assertTrue(self.processor.validate_source(source, "bar"))
