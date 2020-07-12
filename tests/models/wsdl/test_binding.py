from unittest import TestCase

from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import BindingOperation


class BindingTests(TestCase):
    def test_unique_operations(self):
        binding = Binding(
            type="foo",
            operations=[
                BindingOperation(name="bar"),
                BindingOperation(name="bar"),
                BindingOperation(name="bar"),
                BindingOperation(name="foo"),
            ],
        )

        operations = list(binding.unique_operations())
        self.assertEqual(2, len(operations))
        self.assertEqual(binding.operations[2], operations[0])
        self.assertEqual(binding.operations[3], operations[1])
