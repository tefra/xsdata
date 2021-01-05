from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.handlers import AttributeMismatchHandler
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag


class AttributeMismatchHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = AttributeMismatchHandler

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

    def test_reset_unsupported_types(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.native(
                    DataType.NMTOKENS,
                    tag=Tag.ENUMERATION,
                    restrictions=Restrictions(tokens=True),
                ),
                AttrFactory.native(
                    DataType.IDREFS,
                    tag=Tag.ENUMERATION,
                    restrictions=Restrictions(tokens=True),
                ),
                AttrFactory.native(
                    DataType.HEX_BINARY, tag=Tag.ENUMERATION, default="abc"
                ),
                AttrFactory.native(
                    DataType.HEX_BINARY,
                    default="abc",
                    fixed=True,
                    restrictions=Restrictions(format="base16"),
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.native(DataType.INT),
                        AttrTypeFactory.native(DataType.NMTOKENS),
                        AttrTypeFactory.native(DataType.HEX_BINARY),
                    ],
                    restrictions=Restrictions(tokens=True, format="base16"),
                ),
            ]
        )
        self.processor.process(target)

        for attr in target.attrs[:-1]:
            self.assertIsNone(attr.restrictions.format)
            self.assertNotEqual(True, attr.restrictions.tokens)
            self.assertEqual(DataType.STRING, attr.types[0].datatype)

        self.assertEqual("base16", target.attrs[-1].restrictions.format)
        self.assertTrue(target.attrs[-1].restrictions.tokens)

        for attr_type in target.attrs[-1].types:
            self.assertNotEqual(DataType.STRING, attr_type.datatype)
