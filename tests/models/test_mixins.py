import inspect
from typing import Optional, Type
from unittest import TestCase

from attr import dataclass

from xsdata.models import elements as el
from xsdata.models.mixins import (
    ExtendsMixin,
    NamedField,
    OccurrencesMixin,
    RestrictedField,
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

    def test_attribute_raw_type_property(self):
        obj = el.Attribute.build()

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.raw_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.raw_type)

        obj.simple_type = el.SimpleType.build()
        self.assertIsNone(obj.raw_type)

        obj.simple_type.restriction = el.Restriction.build(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.raw_type)

    def test_element_raw_type_property(self):
        obj = el.Element.build()

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.raw_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.raw_type)

    def test_restriction_raw_type_property(self):
        obj = el.Restriction.build()

        obj.base = "foo"
        self.assertEqual(obj.base, obj.raw_type)

    def test_simple_type_raw_type_property(self):
        obj = el.SimpleType.build()

        self.assertIsNone(obj.raw_type)

        obj.restriction = el.Restriction.build(base="thug")
        self.assertEqual(obj.restriction.base, obj.raw_type)


class NamedFieldTests(TestCase):
    def test_pascal_name(self):
        self.assertEqual("FooBar", NamedFieldImpl("foo_bar").pascal_name)

    def test_snake_name(self):
        self.assertEqual("foo_bar", NamedFieldImpl("FooBar").snake_name)
        self.assertEqual("for_value", NamedFieldImpl("for").snake_name)

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

    def test_attribute_raw_name(self):
        obj = el.Attribute.build(ref="bar")
        self.assertEqual("bar", obj.raw_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            el.Attribute.build().raw_name

    def test_element_raw_name(self):
        obj = el.Element.build(ref="bar")
        self.assertEqual("bar", obj.raw_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            el.Element.build().raw_name

    def test_simple_type_raw_name(self):
        obj = el.SimpleType.build(name="foo")
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            obj = el.SimpleType.build()
            self.assertFalse(hasattr(obj, "ref"))
            obj.raw_name

    def test_restriction_raw_name(self):
        obj = el.Restriction.build()
        self.assertEqual("value", obj.raw_name)


class RestrictedFieldTests(TestCase):
    def test_subclasses(self):
        subclasses = [clazz for name, clazz in get_subclasses(RestrictedField)]
        expected = [
            el.Attribute,
            el.Restriction,
        ]
        self.assertListEqual(expected, subclasses)

    def test_attribute_get_restrictions(self):
        obj = el.Attribute.build()
        self.assertDictEqual({}, obj.get_restrictions())

        obj.use = "required"
        self.assertDictEqual(dict(required=1), obj.get_restrictions())

    def test_restriction_get_restrictions(self):
        self.assertDictEqual({}, el.Restriction.build().get_restrictions())

        obj = el.Restriction.build(
            min_exclusive=el.MinExclusive.build(value=1),
            min_inclusive=el.MinInclusive.build(value=2),
            min_length=el.MinLength.build(value=3),
            max_exclusive=el.MaxExclusive.build(value=4),
            max_inclusive=el.MaxInclusive.build(value=5),
            max_length=el.MaxLength.build(value=6),
            total_digits=el.TotalDigits.build(value=7),
            fraction_digits=el.FractionDigits.build(value=8),
            length=el.Length.build(value=9),
            white_space=el.WhiteSpace.build(value="collapse"),
            pattern=el.Pattern.build(value=".*"),
            enumerations=el.Enumeration.build(value="str"),
        )
        expected = {
            "enumerations": "str",
            "fraction_digits": 8,
            "length": 9,
            "max_exclusive": 4,
            "max_inclusive": 5,
            "max_length": 6,
            "min_exclusive": 1,
            "min_inclusive": 2,
            "min_length": 3,
            "pattern": ".*",
            "total_digits": 7,
            "white_space": "collapse",
        }

        self.assertDictEqual(expected, obj.get_restrictions())


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
            el.ComplexType,
            el.Element,
            el.SimpleType,
        ]
        self.assertListEqual(expected, subclasses)

    def test_complex_type_extends_property(self):
        obj = el.ComplexType.build()
        self.assertIsNone(obj.extends)

        obj.complex_content = el.ComplexContent.build()
        self.assertIsNone(obj.extends)

        obj.complex_content.extension = el.Extension.build()
        self.assertIsNone(obj.extends)

        obj.complex_content.extension.base = "foo_bar"
        self.assertEqual("FooBar", obj.extends)

    def test_element_extends_property(self):
        obj = el.Element.build()
        self.assertIsNone(obj.extends)

        obj.type = "foo_bar"
        self.assertEqual("FooBar", obj.extends)

        obj.complex_type = el.ComplexType.build()
        self.assertIsNone(obj.extends)

        obj.complex_type.complex_content = el.ComplexContent.build(
            extension=el.Extension.build(base="thug_life")
        )
        self.assertEqual("ThugLife", obj.extends)

    def test_simple_type_extends_property(self):
        self.assertIsNone(el.SimpleType.build().extends)
