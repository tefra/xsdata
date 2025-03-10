import copy
from collections.abc import Generator
from unittest import TestCase

from xsdata.codegen.exceptions import CodegenError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.wsdl import Binding, Definitions, Message, PortType, Service, Types
from xsdata.models.xsd import Schema


class DefinitionsTests(TestCase):
    def test_property_schemas(self) -> None:
        obj = Definitions()

        self.assertIsInstance(obj.schemas, Generator)
        self.assertEqual([], list(obj.schemas))

        obj.types = Types()
        self.assertEqual([], list(obj.schemas))

        schemas = [Schema(), Schema]
        obj.types.schemas.extend(schemas)

        self.assertEqual(schemas, list(obj.schemas))

    def test_find_binding(self) -> None:
        res = Binding(name="foo")
        obj = Definitions(bindings=[res])

        self.assertEqual(res, obj.find_binding("foo"))

        with self.assertRaises(CodegenError):
            obj.find_binding("nope")

    def test_find_message(self) -> None:
        res = Message(name="foo")
        obj = Definitions(messages=[res])

        self.assertEqual(res, obj.find_message("foo"))

        with self.assertRaises(CodegenError):
            obj.find_message("nope")

    def test_find_port_type(self) -> None:
        res = PortType(name="foo")
        obj = Definitions(port_types=[res])

        self.assertEqual(res, obj.find_port_type("foo"))

        with self.assertRaises(CodegenError):
            obj.find_port_type("nope")

    def test_merge(self) -> None:
        target = Definitions()
        source = Definitions()
        source.types = Types()
        source.messages.append(Message())
        source.port_types.append(PortType())
        source.bindings.append(Binding())
        source.services.append(Service())
        source.extended.append(AnyElement())

        source_two = copy.deepcopy(source)
        source_two.types.schemas.append(Schema())

        target.merge(source)
        self.assertEqual(source.types, target.types)
        self.assertEqual(0, len(target.types.schemas))
        self.assertEqual(1, len(target.messages))
        self.assertEqual(1, len(target.port_types))
        self.assertEqual(1, len(target.bindings))
        self.assertEqual(1, len(target.services))
        self.assertEqual(1, len(target.extended))

        target.merge(source_two)
        target.merge(Definitions())
        self.assertEqual(1, len(target.types.schemas))
        self.assertEqual(2, len(target.messages))
        self.assertEqual(2, len(target.port_types))
        self.assertEqual(2, len(target.bindings))
        self.assertEqual(2, len(target.services))
        self.assertEqual(2, len(target.extended))
