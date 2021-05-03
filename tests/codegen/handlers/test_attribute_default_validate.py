from xsdata.codegen.handlers import AttributeDefaultValidateHandler
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeDefaultValidateHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeDefaultValidateHandler()

    def test_process(self):
        target = ClassFactory.create(
            default="4",
            fixed=True,
            nillable=True,
            attrs=[
                AttrFactory.native(DataType.STRING, tag=Tag.SIMPLE_TYPE),
                AttrFactory.native(DataType.STRING, tag=Tag.SIMPLE_TYPE, default="1"),
                AttrFactory.native(DataType.STRING, tag=Tag.ELEMENT),
            ],
        )

        self.processor.process(target)

        for attr in target.attrs:
            self.assertNotEqual("4", attr.default)
            self.assertFalse(attr.fixed)

        target.nillable = False
        self.processor.process(target)

        # Xml text field with no default value
        self.assertEqual("4", target.attrs[0].default)
        self.assertEqual(True, target.attrs[0].fixed)

        # The rest are untouched.
        self.assertEqual("1", target.attrs[1].default)
        self.assertFalse(target.attrs[1].fixed)
        self.assertIsNone(target.attrs[2].default)
        self.assertFalse(target.attrs[2].fixed)

    def test_reset_unsupported_types_ignore_user_types(self):
        attr_type = AttrTypeFactory.create(qname="foo")
        attr = AttrFactory.create(types=[attr_type], fixed=True, default="123")
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)
        self.assertEqual(attr_type, attr.types[0])

    def test_reset_unsupported_types_with_failed_deserialize(self):
        attr = AttrFactory.native(DataType.FLOAT, default="aaa", fixed=True)
        attr.restrictions.format = "base16"
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)

        self.assertEqual(DataType.STRING, attr.types[0].datatype)
        self.assertIsNone(attr.restrictions.format)

    def test_reset_unsupported_types_with_successful_deserialize(self):
        attr = AttrFactory.native(DataType.FLOAT, default=" 0 2.0 3.0", fixed=True)
        attr.restrictions.format = "base16"
        attr.restrictions.tokens = True
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)

        self.assertEqual(DataType.STRING, attr.types[0].datatype)
        self.assertIsNone(None, attr.restrictions.format)
        self.assertTrue(attr.restrictions.tokens)

        attr.default = "0"
        attr.tag = Tag.ENUMERATION
        self.processor.process(target)
        self.assertFalse(attr.restrictions.tokens)

    def test_reset_unsupported_types_with_successful_token_deserialize(self):
        attr = AttrFactory.native(DataType.FLOAT, default="aaa", fixed=True)
        attr.restrictions.format = "something"
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)

        self.assertEqual(DataType.STRING, attr.types[0].datatype)
        self.assertIsNone(attr.restrictions.format)

    def test_reset_unsupported_types_with_different_float_lexical_repr(self):
        attr = AttrFactory.native(DataType.FLOAT, default=" 1e4 ", fixed=True)
        attr.restrictions.format = "base16"
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)

        self.assertEqual(DataType.STRING, attr.types[0].datatype)
        self.assertIsNone(attr.restrictions.format)

    def test_reset_unsupported_types_with_different_bytes_lexical_repr(self):
        attr = AttrFactory.native(DataType.HEX_BINARY, default="abcd EFGH", fixed=True)
        attr.restrictions.format = "base16"
        attr.restrictions.tokens = True
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.processor.process(target)

        self.assertEqual(DataType.STRING, attr.types[0].datatype)
        self.assertIsNone(attr.restrictions.format)
        self.assertTrue(attr.restrictions.tokens)
