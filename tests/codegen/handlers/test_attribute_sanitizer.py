from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeSanitizerHandler
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeSanitizerHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeSanitizerHandler(container=container)

    def test_cascade_default_value(self):
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

    def test_remove_inherited_fields(self):
        target = ClassFactory.elements(2)
        source = target.clone()
        source.qname = "BaseClass"
        target.extensions.append(ExtensionFactory.reference(source.qname))
        original = target.clone()

        self.processor.container.add(source)
        source.attrs[1].restrictions.choice = "1234"
        source.attrs[1].restrictions.max_length = 1
        source.attrs[1].default = "1"
        source.attrs[1].mixed = True
        source.attrs[1].fixed = True

        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))

        target = original.clone()
        source.attrs[1].fixed = False
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))

        target = original.clone()
        source.attrs[1].mixed = False
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))

        target = original.clone()
        source.attrs[1].default = None
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))

        target = original.clone()
        target.attrs.append(AttrFactory.create())
        source.attrs[1].restrictions.max_length = None
        self.processor.process(target)
        self.assertEqual(1, len(target.attrs))

    def test_remove_inherited_fields_with_lists_type(self):
        target = ClassFactory.elements(2)
        target.attrs[0].restrictions.min_occurs = 1
        target.attrs[0].restrictions.max_occurs = 3

        source = target.clone()
        source.qname = "BaseClass"
        target.attrs[0].restrictions.min_occurs = 0
        target.attrs[1].restrictions.max_occurs = 10

        target.extensions.append(ExtensionFactory.reference(source.qname))
        self.processor.container.add(source)

        self.processor.process(target)
        self.assertEqual(2, len(target.attrs))  # min/max occurs didn't match

        self.processor.container.config.output.compound_fields = True
        self.processor.process(target)
        self.assertEqual(2, len(target.attrs))  # The are not part of a choice group

        target.attrs[0].restrictions.choice = "123"
        target.attrs[1].restrictions.choice = "123"
        source.attrs[0].restrictions.choice = "456"
        source.attrs[1].restrictions.choice = "456"
        self.processor.process(target)
        self.assertEqual(0, len(target.attrs))

    def test_set_effective_choices(self):
        target = ClassFactory.create()
        attrs = [
            AttrFactory.any(),
            AttrFactory.any(),
            # first group
            AttrFactory.any(restrictions=Restrictions(sequential=True)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            # break attr
            AttrFactory.any(),
            # second group
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=1)),
            AttrFactory.any(restrictions=Restrictions(sequential=True, max_occurs=2)),
        ]
        target.attrs.extend(attrs)

        self.processor.process(target)

        self.assertIsNone(attrs[0].restrictions.choice)
        self.assertIsNone(attrs[1].restrictions.choice)

        # Part of the group but precedes list siblings
        self.assertIsNone(attrs[2].restrictions.choice)
        # Part of the group but both are lists
        self.assertIsNone(attrs[3].restrictions.choice)
        self.assertIsNone(attrs[4].restrictions.choice)

        # break attr
        self.assertIsNone(attrs[5].restrictions.choice)

        # Second group, mixed list non list sequential elements
        self.assertEqual("effective_1", attrs[6].restrictions.choice)
        self.assertEqual("effective_1", attrs[7].restrictions.choice)
        self.assertEqual("effective_1", attrs[8].restrictions.choice)
