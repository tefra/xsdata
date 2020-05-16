from unittest import TestCase

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from xsdata.formats.dataclass.filters import attribute_default
from xsdata.models.enums import Namespace

type_str = AttrTypeFactory.xs_string()
type_int = AttrTypeFactory.xs_int()
type_float = AttrTypeFactory.xs_float()
type_decimal = AttrTypeFactory.xs_decimal()
type_bool = AttrTypeFactory.xs_bool()
type_qname = AttrTypeFactory.xs_qname()
type_qmap = AttrTypeFactory.xs_qmap()
type_tokens = AttrTypeFactory.xs_tokens()


class AttributeDefaultTests(TestCase):
    def test_attribute_default_with_value_none(self):
        attr = AttrFactory.create(types=[type_str])
        self.assertEqual(None, attribute_default(attr))

    def test_attribute_default_with_type_str(self):
        attr = AttrFactory.create(types=[type_str], default="foo")
        self.assertEqual('"foo"', attribute_default(attr))

    def test_attribute_default_with_type_tokens(self):
        attr = AttrFactory.create(types=[type_tokens], default="foo  bar  \n")
        self.assertEqual('"foo bar"', attribute_default(attr))

    def test_attribute_default_with_type_float(self):
        attr = AttrFactory.create(types=[type_float], default="1.5")
        self.assertEqual(1.5, attribute_default(attr))

        attr.default = "inf"
        attr.types = [type_int, type_float]
        self.assertEqual("float('inf')", attribute_default(attr))

        attr.default = "-inf"
        self.assertEqual("float('-inf')", attribute_default(attr))

    def test_attribute_default_with_type_decimal(self):
        attr = AttrFactory.create(types=[type_decimal], default="1.5")
        self.assertEqual("Decimal('1.5')", attribute_default(attr))

        attr.default = "-inf"
        self.assertEqual("Decimal('-Infinity')", attribute_default(attr))

        attr.default = "inf"
        self.assertEqual("Decimal('Infinity')", attribute_default(attr))

    def test_attribute_default_with_type_int(self):
        attr = AttrFactory.create(types=[type_int], default="1")
        self.assertEqual(1, attribute_default(attr))

    def test_attribute_default_with_type_bool(self):
        attr = AttrFactory.create(types=[type_bool], default="true")
        self.assertTrue(attribute_default(attr))

    def test_attribute_default_with_type_enum(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, name="foo"), default="@enum@foo::bar"
        )
        self.assertEqual("Foo.BAR", attribute_default(attr))

        attr.types[0].alias = "foo_bar"
        self.assertEqual("FooBar.BAR", attribute_default(attr))

    def test_attribute_default_with_type_qname(self):
        attr = AttrFactory.create(types=[type_qname], default="xs:anyType")
        ns_map = {"xs": Namespace.XS.uri}
        self.assertEqual(
            'QName("http://www.w3.org/2001/XMLSchema", "anyType")',
            attribute_default(attr, ns_map),
        )

    def test_attribute_default_with_type_qmap(self):
        attr = AttrFactory.create(types=[type_qmap])
        self.assertEqual("dict", attribute_default(attr))

    def test_attribute_default_with_type_list(self):
        attr = AttrFactory.create(types=[type_bool])
        attr.restrictions.max_occurs = 2
        self.assertEqual("list", attribute_default(attr))

    def test_attribute_default_with_multiple_types(self):
        attr = AttrFactory.create(types=[type_bool, type_int, type_float], default="1")
        self.assertEqual(1, attribute_default(attr))

        attr.default = "1.0"
        self.assertEqual(1.0, attribute_default(attr))

        attr.default = "true"
        self.assertTrue(attribute_default(attr))
