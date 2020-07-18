import copy
from dataclasses import replace
from typing import Generator
from unittest import TestCase

from xsdata.exceptions import DefinitionsValueError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import Message
from xsdata.models.wsdl import PortType
from xsdata.models.wsdl import PortTypeOperation
from xsdata.models.wsdl import Service
from xsdata.models.wsdl import Types
from xsdata.models.xsd import Schema


class PortTypeTests(TestCase):
    def test_find_operating(self):
        res = PortTypeOperation(name="foo")
        obj = PortType(operations=[res])

        self.assertEqual(res, obj.find_operation("foo"))

        with self.assertRaises(DefinitionsValueError) as cm:
            obj.find_operation("nope")

        self.assertEqual("Unknown PortTypeOperation name: nope", str(cm.exception))
