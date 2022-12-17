from types import SimpleNamespace
from unittest import TestCase

from xsdata.utils import objects


class ObjectsTests(TestCase):
    def test_update(self):
        obj = SimpleNamespace()
        obj.foo = SimpleNamespace()
        obj.foo.bar = 2
        obj.bar = 1

        kwargs = {"foo.bar": 1, "bar": 2}
        objects.update(obj, **kwargs)
        self.assertEqual(1, obj.foo.bar)
        self.assertEqual(2, obj.bar)
