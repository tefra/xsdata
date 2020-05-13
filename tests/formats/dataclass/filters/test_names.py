from unittest import TestCase

from tests.factories import AttrTypeFactory
from xsdata.formats.dataclass.filters import attribute_name
from xsdata.formats.dataclass.filters import class_name
from xsdata.formats.dataclass.filters import constant_name
from xsdata.formats.dataclass.filters import type_name


class NameTests(TestCase):
    def test_class_name(self):
        self.assertEqual("XsString", class_name("xs:string"))
        self.assertEqual("FooBarBam", class_name("foo:bar_bam"))
        self.assertEqual("ListType", class_name("List"))
        self.assertEqual("Type", class_name(".*"))

    def test_attribute_name(self):
        self.assertEqual("foo", attribute_name("foo"))
        self.assertEqual("bar", attribute_name("foo:bar"))
        self.assertEqual("foo_bar", attribute_name("FooBar"))
        self.assertEqual("none_value", attribute_name("None"))
        self.assertEqual("br_eak_value", attribute_name("BrEak"))
        self.assertEqual("value_1", attribute_name("1"))

    def test_constant_name(self):
        self.assertEqual("FOO", constant_name("foo"))
        self.assertEqual("FOO_BAR", constant_name("foo:bar"))
        self.assertEqual("FOO_BAR", constant_name("FooBar"))
        self.assertEqual("NONE_VALUE", constant_name("None"))
        self.assertEqual("BR_EAK_VALUE", constant_name("BrEak"))
        self.assertEqual("VALUE_1", constant_name("1"))

    def test_type_name(self):
        type_str = AttrTypeFactory.xs_string()
        self.assertEqual("str", type_name(type_str))

        type_foo_bar_bam = AttrTypeFactory.create(name="foo:bar_bam")
        self.assertEqual("BarBam", type_name(type_foo_bar_bam))
