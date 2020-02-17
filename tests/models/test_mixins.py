import inspect
from typing import Type
from unittest import mock
from unittest import TestCase
from unittest.mock import PropertyMock

from xsdata.models import elements as el
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

        data = dict(min_occurs=1, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(dict(required=True), obj.get_restrictions())

        data = dict(min_occurs=0, max_occurs=1)
        for clazz in self.subclasses:
            obj = clazz.create(**data)
            self.assertEqual(dict(), obj.get_restrictions())


class NamedFieldTests(TestCase):
    def test_property_prefix_with_no_ref_type(self):
        obj = el.Element.create(name="foo")
        self.assertIsNone(obj.prefix)

    def test_property_prefix_with_unknown_ref_type(self):
        obj = el.Element.create(ref="ns:foo")
        self.assertEqual("ns", obj.prefix)

    def test_property_prefix_with_known_ref_type(self):
        obj = el.Element.create(ref="ns:foo")
        self.assertEqual("ns", obj.prefix)

    def test_property_is_abstract(self):
        obj = el.Element.create(abstract=True)
        self.assertTrue(obj.is_abstract)

        obj = el.Element.create(abstract=False)
        self.assertFalse(obj.is_abstract)

        obj = el.Group.create()
        self.assertFalse(obj.is_abstract)


class ElementBaseTests(TestCase):
    def test_property_is_attribute(self):
        obj = ElementBase.create()
        self.assertFalse(obj.is_attribute)

    def test_property_default_value(self):
        obj = ElementBase.create()
        self.assertIsNone(obj.default_value)

        obj = el.Element.create(default="a")
        self.assertEqual("a", obj.default_value)
        self.assertFalse(obj.is_fixed)

        obj.default = None
        obj.fixed = 2
        self.assertEqual(2, obj.default_value)
        self.assertTrue(obj.is_fixed)

    @mock.patch.object(ElementBase, "extends", new_callable=PropertyMock)
    def test_extensions(self, mock_extends_property):
        mock_extends_property.side_effect = [None, "", "foo  bar"]
        obj = ElementBase.create()
        self.assertEqual([], list(obj.extensions))
        self.assertEqual([], list(obj.extensions))
        self.assertEqual(["foo", "bar"], list(obj.extensions))
