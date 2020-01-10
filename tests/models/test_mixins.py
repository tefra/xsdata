import inspect
from typing import Type
from unittest import TestCase, mock
from unittest.mock import PropertyMock

from xsdata.models import elements as el
from xsdata.models.enums import FormType
from xsdata.models.mixins import ElementBase, OccurrencesMixin, TypedField


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
        expected = [
            el.All,
            el.Any,
            el.Choice,
            el.Element,
            el.Group,
            el.Sequence,
        ]
        self.assertEqual(expected, self.subclasses)

    def test_get_restrictions(self):
        data = dict(min_occurs=1, max_occurs=2)
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


class TypedFieldTests(TestCase):
    def setUp(self) -> None:
        super(TypedFieldTests, self).setUp()
        self.subclasses = [c for _, c in get_subclasses(TypedField)]

    def test_subclasses(self):
        expected = [
            el.Attribute,
            el.Element,
            el.Enumeration,
            el.Restriction,
            el.SimpleType,
            el.Union,
        ]
        self.assertEqual(expected, self.subclasses)


class NamedFieldTests(TestCase):
    def test_property_namespace_with_unqualified_form(self):
        obj = el.Element.create(name="foo", form=FormType.UNQUALIFIED)
        self.assertIsNone(obj.namespace)

    def test_property_namespace_with_no_ref_type(self):
        obj = el.Element.create(name="foo")
        self.assertIsNone(obj.namespace)

    def test_property_namespace_with_unknown_ref_type(self):
        obj = el.Element.create(ref="ns:foo")
        self.assertIsNone(obj.namespace)

    def test_property_namespace_with_known_ref_type(self):
        obj = el.Element.create(ref="ns:foo")
        obj.nsmap["ns"] = "bar"
        self.assertEqual("bar", obj.namespace)

    def test_property_is_abstract(self):
        obj = el.Element.create(abstract=True)
        self.assertTrue(obj.is_abstract)

        obj = el.Element.create(abstract=False)
        self.assertFalse(obj.is_abstract)

        obj = el.Group.create()
        self.assertFalse(obj.is_abstract)


class ElementBaseTests(TestCase):
    def test_is_attribute(self):
        obj = ElementBase.create()
        self.assertFalse(obj.is_attribute)

    @mock.patch.object(ElementBase, "extends", new_callable=PropertyMock)
    def test_extensions(self, mock_extends_property):
        mock_extends_property.side_effect = [None, "", "foo  bar"]
        obj = ElementBase.create()
        self.assertEqual([], list(obj.extensions))
        self.assertEqual([], list(obj.extensions))
        self.assertEqual(["foo", "bar"], list(obj.extensions))
