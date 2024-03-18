import unittest
from dataclasses import dataclass
from typing import List

from xsdata.codegen.models import CodegenModel


@dataclass
class Foo(CodegenModel):
    bar: List["Bar"]

    @dataclass
    class Bar(CodegenModel):
        foo: str


class CodegenModelTests(unittest.TestCase):
    def test_clone(self):
        obj = Foo(bar=[Foo.Bar("one"), Foo.Bar("two")])
        actual = obj.clone()

        self.assertIsNot(obj, actual)
        self.assertIsNot(obj.bar, actual.bar)
        self.assertIsNot(obj.bar[0], actual.bar[0])
        self.assertIsNot(obj.bar[1], actual.bar[1])

    def test_swap(self):
        obj = Foo(bar=[Foo.Bar("one")])
        src = Foo(bar=[Foo.Bar("two")])

        obj.swap(src)

        self.assertEqual(src.bar, obj.bar)
        self.assertIsNot(src.bar, obj.bar)
        self.assertIsNot(src.bar[0], obj.bar[0])
