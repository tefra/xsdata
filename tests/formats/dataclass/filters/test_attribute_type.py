from unittest import TestCase

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from xsdata.formats.dataclass.filters import attribute_type


class AttributeTypeTests(TestCase):
    def test_attribute_type_with_default_value(self):
        attr = AttrFactory.create(
            default="foo", types=AttrTypeFactory.list(1, name="foo_bar")
        )

        self.assertEqual("FooBar", attribute_type(attr, []))

    def test_attribute_type_with_optional_value(self):
        attr = AttrFactory.create(types=AttrTypeFactory.list(1, name="foo_bar"))

        self.assertEqual("Optional[FooBar]", attribute_type(attr, []))

    def test_attribute_type_with_circularerence(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, name="foo_bar", circular=True)
        )

        self.assertEqual('Optional["FooBar"]', attribute_type(attr, ["Parent"]))

    def test_attribute_type_with_forwarderence(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, name="foo_bar", forward=True)
        )
        self.assertEqual(
            'Optional["Parent.Inner.FooBar"]', attribute_type(attr, ["Parent", "Inner"])
        )

    def test_attribute_type_with_forward_and_circularerence(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, name="foo_bar", forward=True, circular=True)
        )

        self.assertEqual(
            'Optional["Parent.Inner"]', attribute_type(attr, ["Parent", "Inner"])
        )

    def test_attribute_type_with_list_type(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, name="foo_bar", forward=True)
        )
        attr.restrictions.max_occurs = 2
        self.assertEqual(
            'List["A.Parent.FooBar"]', attribute_type(attr, ["A", "Parent"])
        )

    def test_attribute_type_with_alias(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(
                1, name="foo_bar", forward=True, alias="Boss:Life"
            )
        )
        attr.restrictions.max_occurs = 2
        self.assertEqual(
            'List["A.Parent.BossLife"]', attribute_type(attr, ["A", "Parent"])
        )

    def test_attribute_type_with_multiple_types(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.create(
                    name="thug:life", alias="Boss:Life", forward=True
                ),
                AttrTypeFactory.xs_int(),
            ]
        )
        attr.restrictions.max_occurs = 2

        self.assertEqual(
            'List[Union["A.Parent.BossLife", int]]',
            attribute_type(attr, ["A", "Parent"]),
        )

    def test_attribute_type_with_type_qmap(self):
        attr = AttrFactory.create(types=[AttrTypeFactory.xs_qmap()])

        self.assertEqual("Dict[QName, str]", attribute_type(attr, ["a", "b"]))

    def test_attribute_type_with_native_type(self):
        attr = AttrFactory.create(
            types=[AttrTypeFactory.xs_int(), AttrTypeFactory.xs_positive_int()]
        )
        self.assertEqual("Optional[int]", attribute_type(attr, ["a", "b"]))
