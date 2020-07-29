from unittest import TestCase

from xsdata.exceptions import DefinitionsValueError
from xsdata.models.wsdl import PortType
from xsdata.models.wsdl import PortTypeOperation


class PortTypeTests(TestCase):
    def test_find_operating(self):
        res = PortTypeOperation(name="foo")
        obj = PortType(operations=[res])

        self.assertEqual(res, obj.find_operation("foo"))

        with self.assertRaises(DefinitionsValueError) as cm:
            obj.find_operation("nope")

        self.assertEqual("Unknown PortTypeOperation name: nope", str(cm.exception))
