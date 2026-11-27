from types import SimpleNamespace
from unittest import TestCase
from xml.etree.ElementTree import QName

from xsdata.utils import objects


class ObjectsTests(TestCase):
    def test_update(self) -> None:
        obj = SimpleNamespace()
        obj.foo = SimpleNamespace()
        obj.foo.bar = 2
        obj.bar = 1

        kwargs = {"foo.bar": 1, "bar": 2}
        objects.update(obj, **kwargs)
        self.assertEqual(1, obj.foo.bar)
        self.assertEqual(2, obj.bar)

    def test_literal_value_escapes_qname(self) -> None:
        self.assertEqual(
            'QName("{urn:a\\"}b")', objects.literal_value(QName('{urn:a"}b'))
        )
