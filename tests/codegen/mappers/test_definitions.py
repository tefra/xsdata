from typing import Generator
from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.mappers.defintions import DefinitionsMapper
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType
from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import BindingMessage
from xsdata.models.wsdl import BindingOperation
from xsdata.models.wsdl import Definitions
from xsdata.models.wsdl import Message
from xsdata.models.wsdl import Part
from xsdata.models.wsdl import PortType
from xsdata.models.wsdl import PortTypeMessage
from xsdata.models.wsdl import PortTypeOperation
from xsdata.models.wsdl import Service
from xsdata.models.wsdl import ServicePort


class DefinitionsMapperTests(FactoryTestCase):
    @mock.patch.object(DefinitionsMapper, "map_port")
    def test_map(self, mock_map_port):
        classes = [
            ClassFactory.list(2),
            ClassFactory.list(3),
        ]
        mock_map_port.side_effect = classes
        definitions = Definitions()
        service = Service(ports=[ServicePort() for _ in range(2)])

        definitions.services.append(service)

        result = DefinitionsMapper.map(definitions)
        self.assertEqual(classes[0] + classes[1], result)

        mock_map_port.assert_has_calls(
            [mock.call(definitions, port) for port in service.ports]
        )

    @mock.patch.object(DefinitionsMapper, "map_binding")
    @mock.patch.object(DefinitionsMapper, "attributes")
    @mock.patch.object(Definitions, "find_port_type")
    @mock.patch.object(Definitions, "find_binding")
    def test_map_port(
        self, mock_find_binding, mock_find_port_type, mock_attributes, mock_map_binding,
    ):
        definitions = Definitions()
        service_port = ServicePort(binding="zaa:port")
        port_type = PortType(name="Calc")
        binding = Binding(
            type="zaa:zoo",
            operations=[BindingOperation(name="ADD"), BindingOperation(name="SUB")],
        )
        classes = ClassFactory.list(2)
        mock_find_binding.return_value = binding
        mock_find_port_type.return_value = port_type
        mock_map_binding.return_value = classes
        mock_attributes.side_effect = [
            {"style": "document", "transport": "public"},
            {"location": "http://endpoint.stub/action"},
        ]

        result = DefinitionsMapper.map_port(definitions, service_port)
        self.assertIsInstance(result, Generator)
        self.assertEqual(classes, list(result))

        mock_find_binding.assert_called_once_with("port")
        mock_find_port_type.assert_called_once_with("zoo")
        mock_attributes.assert_has_calls(
            [mock.call(binding.extended), mock.call(service_port.extended),]
        )

        cfg = {
            "style": "document",
            "location": "http://endpoint.stub/action",
            "transport": "public",
        }
        mock_map_binding.assert_called_once_with(definitions, binding, port_type, cfg)

    @mock.patch.object(DefinitionsMapper, "map_binding_operation")
    @mock.patch.object(PortType, "find_operation")
    @mock.patch.object(DefinitionsMapper, "attributes")
    def test_map_binding(
        self, mock_attributes, mock_find_operation, mock_map_binding_operation,
    ):
        definitions = Definitions()
        port_type = PortType(name="Calc")
        binding = Binding(
            type="zaa:zoo",
            operations=[BindingOperation(name="ADD"), BindingOperation(name="SUB")],
        )
        port_type_add = PortTypeOperation(name="PortAdd")
        port_type_sub = PortTypeOperation(name="PortSub")

        classes = [
            ClassFactory.list(2),
            ClassFactory.list(2),
        ]
        mock_map_binding_operation.side_effect = classes
        mock_find_operation.side_effect = [port_type_add, port_type_sub]
        mock_attributes.side_effect = [
            {"soapAction": "add"},
            {"soapAction": "sub"},
        ]
        config = {"foo": "bar"}
        result = DefinitionsMapper.map_binding(definitions, binding, port_type, config)
        self.assertIsInstance(result, Generator)
        self.assertEqual(classes[0] + classes[1], list(result))

        mock_find_operation.assert_has_calls([mock.call("ADD"), mock.call("SUB")])
        mock_attributes.assert_has_calls(
            [mock.call(x.extended) for x in binding.operations]
        )

        config_add = {"soapAction": "add", **config}
        config_sub = {"soapAction": "sub", **config}

        mock_map_binding_operation.assert_has_calls(
            [
                mock.call(
                    definitions,
                    binding.operations[0],
                    port_type_add,
                    config_add,
                    "Calc",
                ),
                mock.call(
                    definitions,
                    binding.operations[1],
                    port_type_sub,
                    config_sub,
                    "Calc",
                ),
            ]
        )

    @mock.patch.object(DefinitionsMapper, "map_binding_operation_messages")
    @mock.patch.object(DefinitionsMapper, "operation_namespace")
    def test_map_binding_operation(
        self, mock_operation_namespace, mock_map_binding_operation_messages
    ):
        definitions = Definitions(location="foo.wsdl", target_namespace="xsdata")
        operation = BindingOperation(name="Add", ns_map={"foo": "bar"})
        port_operation = PortTypeOperation()
        config = {"a": "one", "b": "two"}
        name = "Calc"
        namespace = "SomeNS"
        first = ClassFactory.create()
        second = ClassFactory.create()
        service = ClassFactory.create(
            qname=QName("xsdata", "Calc_Add"),
            status=Status.PROCESSED,
            type=BindingOperation,
            module="foo",
            package=None,
            ns_map={"foo": "bar"},
            attrs=[
                DefinitionsMapper.build_attr(
                    "a", DataType.STRING.qname, native=True, default="one"
                ),
                DefinitionsMapper.build_attr(
                    "b", DataType.STRING.qname, native=True, default="two"
                ),
                DefinitionsMapper.build_attr("first", first.qname),
                DefinitionsMapper.build_attr("second", second.qname),
            ],
        )
        mock_operation_namespace.return_value = namespace
        mock_map_binding_operation_messages.return_value = [
            ("first", first),
            ("second", second),
        ]

        result = DefinitionsMapper.map_binding_operation(
            definitions, operation, port_operation, config, name
        )
        expected = [first, second, service]

        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))
        mock_operation_namespace.assert_called_once_with(config)
        mock_map_binding_operation_messages.assert_called_once_with(
            definitions, operation, port_operation, service.name, namespace
        )

    @mock.patch.object(DefinitionsMapper, "map_binding_operation_message")
    def test_map_binding_operation_messages(self, mock_map_binding_operation_message):
        definitions = Definitions()
        operation = BindingOperation()
        port_operation = PortTypeOperation()
        name = "Add"
        namespace = "someNS"
        target = ClassFactory.create()

        mock_map_binding_operation_message.return_value = target

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, namespace
        )
        self.assertIsInstance(result, Generator)
        self.assertEqual(0, len(list(result)))

        operation.input = BindingMessage()
        port_operation.input = PortTypeMessage()

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, namespace
        )

        self.assertEqual([("input", target)], list(result))

        operation.output = BindingMessage()
        port_operation.output = PortTypeMessage()

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, namespace
        )

        self.assertEqual([("input", target), ("output", target)], list(result))

        mock_map_binding_operation_message.assert_has_calls(
            [
                mock.call(
                    definitions,
                    operation.input,
                    port_operation.input,
                    name=f"{name}_input",
                    namespace=namespace,
                ),
                mock.call(
                    definitions,
                    operation.input,
                    port_operation.input,
                    name=f"{name}_input",
                    namespace=namespace,
                ),
                mock.call(
                    definitions,
                    operation.output,
                    port_operation.output,
                    name=f"{name}_output",
                    namespace=namespace,
                ),
            ]
        )

    @mock.patch.object(DefinitionsMapper, "map_message_parts")
    def test_map_binding_operation_message(self, mock_map_message_parts):
        definitions = Definitions(location="foo.wsdl", target_namespace="xsdata")
        binding_message = BindingMessage(ns_map={"foo": "bar"})
        port_message = PortTypeMessage(message="message")
        name = "Add"
        namespace = "someNS"

        result = DefinitionsMapper.map_binding_operation_message(
            definitions, binding_message, port_message, name, namespace
        )
        expected = Class(
            qname=QName(definitions.target_namespace, name),
            meta_name="Envelope",
            type=BindingMessage,
            module=definitions.module,
            ns_map=binding_message.ns_map,
            namespace=namespace,
        )

        self.assertEqual(expected, result)

        binding_message.extended = [
            AnyElement(qname="{someNS}header"),
            "NotAnyElement",
            AnyElement(qname="{someNS}header"),
            AnyElement(qname="{someNS}body"),
        ]

        inner_attrs = AttrFactory.list(4)
        mock_map_message_parts.side_effect = [
            inner_attrs[:2],
            inner_attrs[2:3],
            inner_attrs[3:],
        ]

        result = DefinitionsMapper.map_binding_operation_message(
            definitions, binding_message, port_message, name, namespace
        )

        main_attrs = [
            DefinitionsMapper.build_attr("Header", QName("Header"), forward=True),
            DefinitionsMapper.build_attr("Body", QName("Body"), forward=True),
        ]
        inner_classes = [
            Class(
                qname=QName("Header"),
                type=BindingMessage,
                module=definitions.module,
                ns_map={"foo": "bar"},
                attrs=inner_attrs[:3],
            ),
            Class(
                qname=QName("Body"),
                type=BindingMessage,
                module=definitions.module,
                ns_map={"foo": "bar"},
                attrs=inner_attrs[3:],
            ),
        ]

        self.assertEqual(main_attrs, result.attrs)
        self.assertEqual(2, len(result.inner))
        self.assertEqual(inner_classes, result.inner)

        mock_map_message_parts.assert_has_calls(
            [
                mock.call(
                    definitions,
                    port_message.message,
                    binding_message.extended[0],
                    inner_classes[0].ns_map,
                ),
                mock.call(
                    definitions,
                    port_message.message,
                    binding_message.extended[2],
                    inner_classes[0].ns_map,
                ),
                mock.call(
                    definitions,
                    port_message.message,
                    binding_message.extended[3],
                    inner_classes[1].ns_map,
                ),
            ]
        )

    @mock.patch.object(Definitions, "find_message")
    def test_map_message_parts(self, mock_find_message):
        definitions = Definitions
        message = Message(
            name="session",
            parts=[
                Part(name="token", element="foo:token", ns_map={"foo": "bar"}),
                Part(name="messageId", type="id", ns_map={"bar": "foo"}),
            ],
        )
        extended = AnyElement(attributes={"part": "token", "message": "{bar}session"})
        message_name = "foo:bar"
        mock_find_message.return_value = message

        expected = [
            DefinitionsMapper.build_attr(
                "token", QName("bar", "token"), namespace="bar"
            )
        ]
        ns_map = {}
        result = DefinitionsMapper.map_message_parts(
            definitions, message_name, extended, ns_map
        )
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))
        self.assertEqual({"foo": "bar"}, ns_map)

        mock_find_message.assert_called_once_with("session")

        extended = AnyElement(
            attributes={"parts": "token messageId", "message": "{bar}session"}
        )
        result = DefinitionsMapper.map_message_parts(
            definitions, message_name, extended, ns_map
        )

        expected = [
            DefinitionsMapper.build_attr(
                "token", QName("bar", "token"), namespace="bar"
            ),
            DefinitionsMapper.build_attr("id", QName("id"), namespace=None),
        ]

        result = DefinitionsMapper.map_message_parts(
            definitions, message_name, extended, ns_map
        )
        self.assertEqual(expected, list(result))
        self.assertEqual({"foo": "bar", "bar": "foo"}, ns_map)

        extended = AnyElement()
        result = DefinitionsMapper.map_message_parts(
            definitions, message_name, extended, ns_map
        )
        self.assertEqual(expected, list(result))

    def test_operation_namespace(self):

        self.assertIsNone(DefinitionsMapper.operation_namespace({}))
        self.assertIsNone(DefinitionsMapper.operation_namespace({"transport": "foo"}))
        self.assertEqual(
            "http://schemas.xmlsoap.org/soap/envelope/",
            DefinitionsMapper.operation_namespace(
                {"transport": "http://schemas.xmlsoap.org/soap/http"}
            ),
        )

    def test_attributes(self):
        elements = [
            None,
            "string",
            AnyElement(qname="{foo}bar", attributes={"foo": "bar"}),
            AnyElement(qname="{foo}bar", attributes={"{foo}bar": "foo"}),
            AnyElement(qname="{foo}bar", attributes={"{foo}foo": "bar2"}),
        ]

        self.assertEqual(
            {"foo": "bar2", "bar": "foo"}, DefinitionsMapper.attributes(elements)
        )
