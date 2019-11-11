import inspect
from typing import Type
from unittest import TestCase

from xsdata.models import elements as el
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
