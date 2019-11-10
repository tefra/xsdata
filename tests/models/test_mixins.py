import inspect
from typing import Optional, Type
from unittest import TestCase

from attr import dataclass

from xsdata.models import elements as el
from xsdata.models.mixins import (
    ExtendsMixin,
    NamedField,
    OccurrencesMixin,
    TypedField,
)


def get_subclasses(clazz: Type):
    def predicate(member):
        return (
            isinstance(member, type)
            and issubclass(member, clazz)
            and not inspect.isabstract(member)
            and member is not clazz
        )

    return inspect.getmembers(el, predicate=predicate)


@dataclass
class TypedFieldImpl(TypedField):
    value: Optional[str]

    @property
    def raw_type(self) -> Optional[str]:
        return self.value


@dataclass
class NamedFieldImpl(NamedField):
    name: Optional[str]


class TypedFieldTests(TestCase):
    def test_display_type_property(self):
        self.assertIsNone(TypedFieldImpl(None).display_type)
        self.assertEqual("FooBar", TypedFieldImpl("_ foo bar !").display_type)
        self.assertEqual("Foo", TypedFieldImpl("common:foo").display_type)
        self.assertEqual("str", TypedFieldImpl("xs:string").display_type)
        self.assertEqual("float", TypedFieldImpl("xs:decimal").display_type)
        self.assertEqual("int", TypedFieldImpl("xs:integer").display_type)
        self.assertEqual("bool", TypedFieldImpl("xs:boolean").display_type)
        self.assertEqual("str", TypedFieldImpl("xs:date").display_type)
        self.assertEqual("str", TypedFieldImpl("xs:time").display_type)

    def test_subclasses(self):
        subclasses = [clazz for name, clazz in get_subclasses(TypedField)]
        expected = [
            el.Attribute,
            el.Element,
            el.Restriction,
            el.SimpleType,
        ]

        self.assertListEqual(expected, subclasses)


class NamedFieldTests(TestCase):
    def test_subclasses(self):
        subclasses = [clazz for name, clazz in get_subclasses(NamedField)]
        expected = [
            el.Attribute,
            el.ComplexType,
            el.Element,
            el.Restriction,
            el.SimpleType,
        ]

        self.assertListEqual(expected, subclasses)

    def test_propeety_pascal_name(self):
        self.assertEqual("FooBar", NamedFieldImpl("foo_bar").pascal_name)

    def test_property_snake_name(self):
        self.assertEqual("foo_bar", NamedFieldImpl("FooBar").snake_name)
        self.assertEqual("for_value", NamedFieldImpl("for").snake_name)


class OccurrencesMixinTests(TestCase):
    def setUp(self) -> None:
        self.subclasses = [c for _, c in get_subclasses(OccurrencesMixin)]

    def test_subclasses(self):
        expected = [
            el.All,
            el.Any,
            el.Choice,
            el.Element,
            el.Group,
            el.Sequence,
        ]
        self.assertListEqual(expected, self.subclasses)

    def test_get_restrictions(self):
        data = dict(min_occurs=1, max_occurs=2)
        for clazz in self.subclasses:
            obj = clazz.build(**data)
            self.assertDictEqual(data, obj.get_restrictions())

        data = dict(min_occurs=1, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.build(**data)
            self.assertDictEqual(dict(required=True), obj.get_restrictions())

        data = dict(min_occurs=0, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.build(**data)
            self.assertDictEqual(dict(), obj.get_restrictions())


class ExtendsMixinTests(TestCase):
    def test_subclasses(self):
        subclasses = [c for _, c in get_subclasses(ExtendsMixin)]
        expected = [
            el.Attribute,
            el.ComplexType,
            el.Element,
            el.SimpleType,
        ]
        self.assertListEqual(expected, subclasses)

    def test_property_display_base(self):
        obj = el.Element.build(type="common:foo_bar")
        self.assertEqual("FooBar", obj.display_base)
