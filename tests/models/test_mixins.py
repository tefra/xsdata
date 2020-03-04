import inspect
from typing import Iterator
from typing import Optional
from typing import Type
from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models import elements as el
from xsdata.models.enums import FormType
from xsdata.models.mixins import ElementBase
from xsdata.models.mixins import OccurrencesMixin


def get_subclasses(clazz: Type):
    def predicate(member):
        return (
            isinstance(member, type)
            and issubclass(member, clazz)
            and not inspect.isabstract(member)
            and member is not clazz
        )

    return inspect.getmembers(el, predicate=predicate)


class OccurrencesMixinTests(TestCase):
    def setUp(self) -> None:
        super(OccurrencesMixinTests, self).setUp()
        self.subclasses = [c for _, c in get_subclasses(OccurrencesMixin)]

    def test_subclasses(self):
        expected = [el.All, el.Any, el.Choice, el.Element, el.Group, el.Sequence]
        self.assertEqual(expected, self.subclasses)

    def test_get_restrictions(self):
        data = dict(min_occurs=1, max_occurs=2)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(data, obj.get_restrictions())

        data = dict(min_occurs=2, max_occurs=2)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(data, obj.get_restrictions())

        data = dict(min_occurs=1, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(dict(required=True), obj.get_restrictions())

        data = dict(min_occurs=0, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(dict(), obj.get_restrictions())


class ElementBaseTests(TestCase):
    def test_property_class_name(self):
        class Foo(ElementBase):
            pass

        self.assertEqual("Foo", Foo().class_name)

    def test_property_default_value(self):
        element = ElementBase()
        self.assertIsNone(element.default_value)

        element.fixed = "foo"
        self.assertEqual("foo", element.default_value)

        element.default = "bar"
        self.assertEqual("bar", element.default_value)

    def test_property_extends(self):
        element = ElementBase()
        self.assertIsNone(element.extends)

    def test_property_extensions(self):
        element = ElementBase()
        self.assertIsInstance(element.extensions, Iterator)
        self.assertEqual([], list(element.extensions))

        class Foo(ElementBase):
            @property
            def extends(self) -> Optional[str]:
                return "a b   c"

        self.assertEqual(["a", "b", "c"], list(Foo().extensions))

    def test_property_has_form(self):
        element = ElementBase()
        self.assertFalse(element.has_form)

        element.form = None
        self.assertTrue(element.has_form)

    def test_property_is_abstract(self):
        element = ElementBase()
        self.assertFalse(element.is_abstract)

        element.abstract = False
        self.assertFalse(element.is_abstract)

        element.abstract = True
        self.assertTrue(element.is_abstract)

    def test_property_is_attribute(self):
        element = ElementBase()
        self.assertFalse(element.is_attribute)

    def test_property_is_fixed(self):
        element = ElementBase()
        self.assertFalse(element.is_fixed)

        element.fixed = None
        self.assertFalse(element.is_fixed)

        element.fixed = "foo"
        self.assertTrue(element.is_fixed)

    def test_property_is_mixed(self):
        element = ElementBase()
        self.assertFalse(element.is_mixed)

    def test_property_is_qualified(self):
        element = ElementBase()
        self.assertFalse(element.is_qualified)

        element.form = None
        self.assertFalse(element.is_qualified)

        element.form = FormType.UNQUALIFIED
        self.assertFalse(element.is_qualified)

        element.form = FormType.QUALIFIED
        self.assertTrue(element.is_qualified)

        element = ElementBase()
        element.form = FormType.UNQUALIFIED
        element.ref = None
        self.assertFalse(element.is_qualified)

        element.ref = "foo"
        self.assertTrue(element.is_qualified)

    def test_property_prefix(self):
        element = ElementBase()
        self.assertIsNone(element.prefix)

        element.ref = "foo"
        self.assertIsNone(element.prefix)

        element.ref = "foo:bar"
        self.assertEqual("foo", element.prefix)

    def test_raw_namespace(self):
        element = ElementBase()
        self.assertIsNone(element.raw_namespace)

        element.target_namespace = "tns"
        self.assertEqual("tns", element.raw_namespace)

    def test_raw_type(self):
        element = ElementBase()
        self.assertIsNone(element.raw_namespace)

        element.type = "xs:int"
        self.assertEqual("xs:int", element.raw_type)

    def test_real_name(self):
        element = ElementBase()

        with self.assertRaises(SchemaValueError):
            element.real_name

        element.ref = "foo"
        self.assertEqual("foo", element.real_name)

        element.name = "bar"
        self.assertEqual("bar", element.real_name)

    def test_real_type(self):
        element = ElementBase()
        with self.assertRaises(SchemaValueError):
            element.real_type
