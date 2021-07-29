from xsdata.codegen.handlers import AttributeNormalizeHandler
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeDefaultValidateHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeNormalizeHandler()

    def test_cascade_properties(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.native(DataType.STRING, tag=Tag.EXTENSION),
                AttrFactory.native(DataType.STRING, tag=Tag.SIMPLE_TYPE, default="1"),
                AttrFactory.native(DataType.STRING, tag=Tag.ATTRIBUTE, default="2"),
                AttrFactory.native(DataType.STRING, tag=Tag.ELEMENT),
            ],
        )

        self.processor.process(target)

        self.assertIsNone(target.attrs[0].default)
        self.assertFalse(target.attrs[0].fixed)
        self.assertFalse(target.attrs[0].restrictions.nillable)

        self.assertEqual("1", target.attrs[1].default)
        self.assertFalse(target.attrs[1].fixed)
        self.assertFalse(target.attrs[1].restrictions.nillable)

        self.assertEqual("2", target.attrs[2].default)
        self.assertFalse(target.attrs[2].fixed)
        self.assertFalse(target.attrs[2].restrictions.nillable)

        self.assertIsNone(target.attrs[3].default)
        self.assertFalse(target.attrs[3].fixed)
        self.assertFalse(target.attrs[3].restrictions.nillable)

        target.default = "0"
        target.fixed = True
        target.nillable = True
        self.processor.process(target)

        # text value field inherits default/fixed/nillable if they are not set
        self.assertEqual("0", target.attrs[0].default)
        self.assertTrue(target.attrs[0].fixed)
        self.assertTrue(target.attrs[0].restrictions.nillable)

        # text value field inherits only nillable the rest are already set
        self.assertEqual("1", target.attrs[1].default)
        self.assertFalse(target.attrs[1].fixed)
        self.assertTrue(target.attrs[1].restrictions.nillable)

        # attribute field ignored
        self.assertEqual("2", target.attrs[2].default)
        self.assertFalse(target.attrs[2].fixed)
        self.assertFalse(target.attrs[2].restrictions.nillable)

        # element field ignored
        self.assertIsNone(target.attrs[3].default)
        self.assertFalse(target.attrs[3].fixed)
        self.assertFalse(target.attrs[3].restrictions.nillable)

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

    def test_process_reset_min_occurs(self):
        first = AttrFactory.native(DataType.ANY_TYPE)
        first.restrictions.min_occurs = 1
        first.restrictions.max_occurs = 2
        second = AttrFactory.native(DataType.ANY_TYPE)
        second.restrictions.min_occurs = 1
        second.default = "foo"
        third = AttrFactory.native(DataType.ANY_TYPE)
        third.restrictions.min_occurs = 1

        target = ClassFactory.create(attrs=[first, second, third])

        self.processor.process(target)

        self.assertEqual(1, first.restrictions.min_occurs)
        self.assertEqual(2, first.restrictions.max_occurs)
        self.assertEqual(1, second.restrictions.min_occurs)
        self.assertEqual(0, third.restrictions.min_occurs)
