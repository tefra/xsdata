from collections.abc import Generator
from typing import Any
from unittest import mock

from xsdata.codegen.mappers import DefinitionsMapper
from xsdata.codegen.models import Attr, Class, Status
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType, Namespace, Tag
from xsdata.models.wsdl import (
    Binding,
    BindingMessage,
    BindingOperation,
    Definitions,
    Message,
    Part,
    PortType,
    PortTypeMessage,
    PortTypeOperation,
    Service,
    ServicePort,
)
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import AttrFactory, ClassFactory, FactoryTestCase


def mock_create_inner(target: Class, name: str) -> Class:
    for inner in target.inner:
        if inner.name == name:
            return inner

    inner = ClassFactory.create(qname=name)
    target.inner.append(inner)
    return inner


def mock_create_attr(*args: Any, **kwargs: Any) -> list[Attr]:
    return AttrFactory.list(1)


class DefinitionsMapperTests(FactoryTestCase):
    @mock.patch.object(DefinitionsMapper, "map_port")
    def test_map(self, mock_map_port) -> None:
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
        self, mock_find_binding, mock_find_port_type, mock_attributes, mock_map_binding
    ) -> None:
        definitions = Definitions()
        service_port = ServicePort(binding="zaa:port", extended=[AnyElement()])
        port_type = PortType(name="Calc")
        binding = Binding(
            type="zaa:zoo",
            extended=[AnyElement()],
            operations=[BindingOperation(name="ADD"), BindingOperation(name="SUB")],
        )
        classes = ClassFactory.list(2)
        cfg = {
            "style": "document",
            "location": "http://endpoint.stub/action",
            "transport": "public",
        }

        mock_find_binding.return_value = binding
        mock_find_port_type.return_value = port_type
        mock_map_binding.return_value = classes
        mock_attributes.return_value = cfg

        result = DefinitionsMapper.map_port(definitions, service_port)
        self.assertIsInstance(result, Generator)
        self.assertEqual(classes, list(result))

        mock_find_binding.assert_called_once_with("port")
        mock_find_port_type.assert_called_once_with("zoo")

        self.assertEqual(2, len(list(mock_attributes.call_args[0][0])))
        self.assertEqual(1, mock_attributes.call_count)

        mock_map_binding.assert_called_once_with(definitions, binding, port_type, cfg)

    @mock.patch.object(DefinitionsMapper, "map_binding_operation")
    @mock.patch.object(PortType, "find_operation")
    @mock.patch.object(DefinitionsMapper, "attributes")
    def test_map_binding(
        self, mock_attributes, mock_find_operation, mock_map_binding_operation
    ) -> None:
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
        self.assertEqual(2, mock_attributes.call_count)

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
    ) -> None:
        definitions = Definitions(target_namespace="xsdata")
        operation = BindingOperation(name="Add", location="foo.wsdl")
        operation.ns_map["foo"] = "bar"
        port_operation = PortTypeOperation()
        config = {"a": "one", "b": "two", "style": "rpc"}
        name = "Calc"
        namespace = "SomeNS"
        first = ClassFactory.create(qname="some_name_first", meta_name="Envelope")
        second = ClassFactory.create(qname="some_name_second", meta_name="Envelope")
        other = ClassFactory.create()
        service = ClassFactory.create(
            qname=build_qname("xsdata", "Calc_Add"),
            status=Status.FLATTENED,
            tag=Tag.BINDING_OPERATION,
            location="foo.wsdl",
            module=None,
            ns_map={"foo": "bar"},
            attrs=[
                DefinitionsMapper.build_attr(
                    "a", str(DataType.STRING), native=True, default="one"
                ),
                DefinitionsMapper.build_attr(
                    "b", str(DataType.STRING), native=True, default="two"
                ),
                DefinitionsMapper.build_attr(
                    "style", str(DataType.STRING), native=True, default="rpc"
                ),
                DefinitionsMapper.build_attr("first", first.qname),
                DefinitionsMapper.build_attr("second", second.qname),
            ],
        )
        mock_operation_namespace.return_value = namespace
        mock_map_binding_operation_messages.return_value = [first, second, other]

        result = DefinitionsMapper.map_binding_operation(
            definitions, operation, port_operation, config, name
        )
        expected = [first, second, other, service]

        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))
        mock_operation_namespace.assert_called_once_with(config)
        mock_map_binding_operation_messages.assert_called_once_with(
            definitions, operation, port_operation, service.name, "rpc", namespace
        )

    @mock.patch.object(DefinitionsMapper, "build_envelope_fault")
    @mock.patch.object(DefinitionsMapper, "build_envelope_class")
    def test_map_binding_operation_messages(
        self, mock_build_envelope_class, mock_build_envelope_fault
    ) -> None:
        definitions = Definitions()
        operation = BindingOperation()
        port_operation = PortTypeOperation()
        name = "Add"
        namespace = "someNS"
        target = ClassFactory.create()
        style = "document"

        mock_build_envelope_class.return_value = target

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, style, namespace
        )
        self.assertIsInstance(result, Generator)
        self.assertEqual(0, len(list(result)))

        operation.input = BindingMessage()
        port_operation.input = PortTypeMessage()

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, style, namespace
        )
        self.maxDiff = None
        self.assertEqual([target], list(result))

        operation.output = BindingMessage()
        port_operation.output = PortTypeMessage()

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, style, namespace
        )

        self.assertEqual([target, target], list(result))

        mock_build_envelope_class.assert_has_calls(
            [
                mock.call(
                    definitions,
                    operation.input,
                    port_operation.input,
                    f"{name}_input",
                    style,
                    namespace,
                    None,
                ),
                mock.call(
                    definitions,
                    operation.input,
                    port_operation.input,
                    f"{name}_input",
                    style,
                    namespace,
                    None,
                ),
                mock.call(
                    definitions,
                    operation.output,
                    port_operation.output,
                    f"{name}_output",
                    style,
                    namespace,
                    None,
                ),
            ]
        )
        mock_build_envelope_fault.assert_called_once_with(
            definitions, port_operation, target
        )

    @mock.patch.object(DefinitionsMapper, "build_message_class")
    @mock.patch.object(DefinitionsMapper, "build_envelope_class")
    def test_map_binding_operation_messages_with_style_rpc(
        self, mock_build_envelope_class, mock_build_message_class
    ) -> None:
        definitions = Definitions()
        operation = BindingOperation()
        port_operation = PortTypeOperation()
        name = "Add"
        namespace = "someNS"
        target = ClassFactory.create()
        message = ClassFactory.create()
        style = "rpc"

        mock_build_message_class.return_value = message
        mock_build_envelope_class.return_value = target

        operation.input = BindingMessage()
        operation.name = "Add"
        port_operation.input = PortTypeMessage()

        result = DefinitionsMapper.map_binding_operation_messages(
            definitions, operation, port_operation, name, style, namespace
        )
        self.maxDiff = None
        self.assertEqual([message, target], list(result))

        mock_build_message_class.assert_called_once_with(
            definitions, port_operation.input
        )
        mock_build_envelope_class.assert_called_once_with(
            definitions,
            operation.input,
            port_operation.input,
            f"{name}_input",
            style,
            namespace,
            "Add",
        )

    @mock.patch.object(DefinitionsMapper, "map_port_type_message")
    @mock.patch.object(DefinitionsMapper, "map_binding_message_parts")
    @mock.patch.object(DefinitionsMapper, "build_inner_class")
    def test_build_envelope_class(
        self,
        mock_get_or_create_inner_class,
        mock_map_binding_message_parts,
        mock_map_port_type_message,
    ) -> None:
        mock_get_or_create_inner_class.side_effect = mock_create_inner
        mock_map_binding_message_parts.side_effect = mock_create_attr

        name = "some_operation_bindings"
        style = "document"
        namespace = "xsdata"
        definitions = Definitions(target_namespace="bar")
        port_type_message = PortTypeMessage(
            message="some_operation", location="foo.wsdl"
        )
        binding_message = BindingMessage(
            extended=[
                AnyElement(qname="body"),
                AnyElement(qname="header"),
                AnyElement(qname="header"),
            ],
            location="foo.wsdl",
        )
        binding_message.ns_map["foo"] = "bar"

        result = DefinitionsMapper.build_envelope_class(
            definitions,
            binding_message,
            port_type_message,
            name,
            style,
            namespace,
            None,
        )

        expected = Class(
            qname=build_qname("bar", name),
            meta_name="Envelope",
            tag=Tag.BINDING_MESSAGE,
            location="foo.wsdl",
            ns_map={"foo": "bar"},
            namespace="xsdata",
        )
        self.assertEqual(2, len(result.inner))
        self.assertEqual(1, len(result.inner[0].attrs))
        self.assertEqual(2, len(result.inner[1].attrs))
        self.assertEqual(0, mock_map_port_type_message.call_count)
        mock_map_binding_message_parts.assert_has_calls(
            [
                mock.call(
                    definitions,
                    port_type_message.message,
                    binding_message.extended[0],
                    result.inner[0].ns_map,
                ),
                mock.call(
                    definitions,
                    port_type_message.message,
                    binding_message.extended[1],
                    result.inner[1].ns_map,
                ),
                mock.call(
                    definitions,
                    port_type_message.message,
                    binding_message.extended[2],
                    result.inner[1].ns_map,
                ),
            ]
        )
        mock_get_or_create_inner_class.assert_has_calls(
            [
                mock.call(mock.ANY, "Body"),
                mock.call(mock.ANY, "Header"),
                mock.call(mock.ANY, "Header"),
            ]
        )

        result.inner.clear()
        self.assertEqual(expected, result)

    @mock.patch.object(DefinitionsMapper, "map_port_type_message")
    @mock.patch.object(DefinitionsMapper, "map_binding_message_parts")
    @mock.patch.object(DefinitionsMapper, "build_inner_class")
    def test_build_envelope_class_with_style_rpc(
        self,
        mock_get_or_create_inner_class,
        mock_map_binding_message_parts,
        mock_map_port_type_message,
    ) -> None:
        mock_get_or_create_inner_class.side_effect = mock_create_inner
        mock_map_binding_message_parts.side_effect = mock_create_attr
        mock_map_port_type_message.side_effect = mock_create_attr

        name = "some_operation_bindings"
        style = "rpc"
        namespace = "xsdata"
        definitions = Definitions(target_namespace="bar")
        port_type_message = PortTypeMessage(
            message="some_operation", location="foo.wsdl"
        )
        binding_message = BindingMessage(
            extended=[
                AnyElement(qname="body", attributes={"namespace": "bodyns"}),
                AnyElement(qname="header"),
                AnyElement(qname="header"),
            ],
            location="foo.wsdl",
        )
        binding_message.ns_map["foo"] = "bar"

        result = DefinitionsMapper.build_envelope_class(
            definitions,
            binding_message,
            port_type_message,
            name,
            style,
            namespace,
            None,
        )

        expected = Class(
            qname=build_qname("bar", name),
            meta_name="Envelope",
            tag=Tag.BINDING_MESSAGE,
            location="foo.wsdl",
            ns_map={"foo": "bar"},
            namespace="xsdata",
        )
        self.assertEqual(2, len(result.inner))
        self.assertEqual(1, len(result.inner[0].attrs))
        self.assertEqual(2, len(result.inner[1].attrs))
        self.maxDiff = None
        mock_map_port_type_message.assert_called_once_with(
            None, port_type_message, "bodyns"
        )

        mock_map_binding_message_parts.assert_has_calls(
            [
                mock.call(
                    definitions,
                    port_type_message.message,
                    binding_message.extended[1],
                    result.inner[1].ns_map,
                ),
                mock.call(
                    definitions,
                    port_type_message.message,
                    binding_message.extended[2],
                    result.inner[1].ns_map,
                ),
            ]
        )
        mock_get_or_create_inner_class.assert_has_calls(
            [
                mock.call(mock.ANY, "Body"),
                mock.call(mock.ANY, "Header"),
                mock.call(mock.ANY, "Header"),
            ]
        )

        result.inner.clear()
        self.assertEqual(expected, result)

    def test_build_envelope_fault(self) -> None:
        body = ClassFactory.create(qname="Body")
        target = ClassFactory.create()
        target.inner.append(body)

        port_type_operation = PortTypeOperation()
        definitions = Definitions()

        DefinitionsMapper.build_envelope_fault(definitions, port_type_operation, target)
        expected_fault_attr = DefinitionsMapper.build_attr(
            "Fault", body.inner[0].qname, forward=True, namespace=target.namespace
        )
        str_qname = str(DataType.STRING)
        expected_fault_attrs = [
            DefinitionsMapper.build_attr(name, str_qname, native=True, namespace="")
            for name in ["faultcode", "faultstring", "faultactor", "detail"]
        ]

        self.assertEqual(1, len(body.attrs))
        self.assertEqual(expected_fault_attr, body.attrs[0])
        self.assertEqual(expected_fault_attrs, body.inner[0].attrs)

        for attr in body.attrs:
            self.assertTrue(attr.is_optional)

    def test_build_envelope_fault_with_detail_messages(self) -> None:
        body = ClassFactory.create(qname="Body")
        target = ClassFactory.create()
        target.inner.append(body)

        port_type_operation = PortTypeOperation()
        port_type_operation.faults.append(PortTypeMessage(message="x:foo"))
        port_type_operation.faults.append(PortTypeMessage(message="x:bar"))

        definitions = Definitions()
        definitions.messages.append(Message(name="foo", parts=[Part(element="fooEl")]))
        definitions.messages.append(Message(name="bar", parts=[Part(element="barEl")]))

        DefinitionsMapper.build_envelope_fault(definitions, port_type_operation, target)
        expected_fault_attr = DefinitionsMapper.build_attr(
            "Fault", body.inner[0].qname, forward=True, namespace=target.namespace
        )
        str_qname = str(DataType.STRING)
        expected_fault_attrs = [
            DefinitionsMapper.build_attr(name, str_qname, native=True, namespace="")
            for name in ["faultcode", "faultstring", "faultactor"]
        ]

        expected_fault_attrs.append(
            DefinitionsMapper.build_attr(
                "detail", body.inner[0].inner[0].qname, forward=True, namespace=""
            )
        )

        expected_fault_detail_attrs = [
            DefinitionsMapper.build_attr(
                name, qname=name, namespace=target.namespace, native=False
            )
            for name in ["fooEl", "barEl"]
        ]

        self.assertEqual(1, len(body.attrs))
        self.assertEqual(expected_fault_attr, body.attrs[0])
        self.assertEqual(expected_fault_attrs, body.inner[0].attrs)
        self.assertEqual(expected_fault_detail_attrs, body.inner[0].inner[0].attrs)

    def test_build_envelope_fault_raises_error_if_missing_inner_body(self) -> None:
        target = ClassFactory.create()
        operation = PortTypeOperation()
        definitions = Definitions()

        with self.assertRaises(StopIteration):
            DefinitionsMapper.build_envelope_fault(definitions, operation, target)

    @mock.patch.object(DefinitionsMapper, "build_parts_attributes")
    @mock.patch.object(Definitions, "find_message")
    def test_map_binding_message_parts_with_part_token(
        self, mock_find_message, mock_create_message_attributes
    ) -> None:
        definitions = Definitions()
        message_name = "session"
        ns_map = {}
        message = Message(
            name="session",
            parts=[
                Part(name="token", element="foo:token"),
                Part(name="messageId", type="id"),
            ],
        )
        extended = AnyElement(attributes={"part": "token", "message": "{bar}session"})
        mock_create_message_attributes.return_value = AttrFactory.list(2)
        mock_find_message.return_value = message

        actual = DefinitionsMapper.map_binding_message_parts(
            definitions, message_name, extended, ns_map
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual(2, len(list(actual)))

        mock_create_message_attributes.assert_called_once_with(
            message.parts[0:1], ns_map
        )

    @mock.patch.object(DefinitionsMapper, "build_parts_attributes")
    @mock.patch.object(Definitions, "find_message")
    def test_map_binding_message_parts_with_token_parts(
        self, mock_find_message, mock_create_message_attributes
    ) -> None:
        definitions = Definitions()
        message_name = "session"
        ns_map = {}
        message = Message(
            name="session",
            parts=[
                Part(name="token", element="foo:token"),
                Part(name="messageId", type="id"),
                Part(name="another", type="id"),
            ],
        )
        extended = AnyElement(
            attributes={"parts": "token messageId", "message": "{bar}session"}
        )
        mock_create_message_attributes.return_value = AttrFactory.list(2)
        mock_find_message.return_value = message

        actual = DefinitionsMapper.map_binding_message_parts(
            definitions, message_name, extended, ns_map
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual(2, len(list(actual)))

        mock_create_message_attributes.assert_called_once_with(
            message.parts[0:2], ns_map
        )

    @mock.patch.object(DefinitionsMapper, "build_parts_attributes")
    @mock.patch.object(Definitions, "find_message")
    def test_map_binding_message_parts_with_all_parts(
        self, mock_find_message, mock_create_message_attributes
    ) -> None:
        definitions = Definitions()
        message_name = "session"
        ns_map = {}
        message = Message(
            name="session",
            parts=[
                Part(name="token", element="foo:token"),
                Part(name="messageId", type="id"),
                Part(name="another", type="id"),
            ],
        )
        extended = AnyElement(attributes={"message": "{bar}session"})
        mock_create_message_attributes.return_value = AttrFactory.list(2)
        mock_find_message.return_value = message

        actual = DefinitionsMapper.map_binding_message_parts(
            definitions, message_name, extended, ns_map
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual(2, len(list(actual)))

        mock_find_message.assert_called_once_with("session")
        mock_create_message_attributes.assert_called_once_with(message.parts, ns_map)

    @mock.patch.object(DefinitionsMapper, "build_parts_attributes")
    @mock.patch.object(Definitions, "find_message")
    def test_map_binding_message_parts_with_original_message(
        self, mock_find_message, mock_create_message_attributes
    ) -> None:
        definitions = Definitions
        message_name = "foo:bar"
        ns_map = {}
        message = Message(
            name="session",
            parts=[
                Part(name="token", element="foo:token"),
                Part(name="messageId", type="id"),
                Part(name="another", type="id"),
            ],
        )
        extended = AnyElement()
        mock_create_message_attributes.return_value = AttrFactory.list(2)
        mock_find_message.return_value = message

        actual = DefinitionsMapper.map_binding_message_parts(
            definitions, message_name, extended, ns_map
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual(2, len(list(actual)))

        mock_create_message_attributes.assert_called_once_with(message.parts, ns_map)
        mock_find_message.assert_called_once_with("bar")

    @mock.patch("xsdata.codegen.mappers.definitions.logger.warning")
    def test_build_parts_attributes(self, mock_warning) -> None:
        p_one = Part(element="a:bar")
        p_one.ns_map["a"] = "great"
        p_two = Part(name="arg0", type="xs:string")
        p_two.ns_map["xs"] = Namespace.XS.uri
        p_three = Part(name="arg1", type="b:cafe")
        p_three.ns_map["b"] = "boo"
        p_four = Part(name="arg2")

        ns_map = {}
        parts = [p_one, p_two, p_three, p_four]
        result = DefinitionsMapper.build_parts_attributes(parts, ns_map)
        expected = [
            DefinitionsMapper.build_attr(
                "bar", build_qname("great", "bar"), namespace="great", native=False
            ),
            DefinitionsMapper.build_attr(
                "arg0", str(DataType.STRING), namespace="", native=True
            ),
            DefinitionsMapper.build_attr(
                "arg1", build_qname("boo", "cafe"), namespace="##lazy", native=False
            ),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))
        mock_warning.assert_called_once_with("Skip untyped message part %s", "arg2")

    @mock.patch.object(DefinitionsMapper, "build_parts_attributes")
    def test_build_message_class(self, mock_create_message_attributes) -> None:
        message = Message(name="bar", parts=[Part()])
        message.ns_map["foo"] = "bar"
        definitions = Definitions(messages=[message], target_namespace="xsdata")
        port_type_message = PortTypeMessage(message="foo:bar", location="foo.wsdl")

        attrs = AttrFactory.list(2)
        mock_create_message_attributes.return_value = attrs
        actual = DefinitionsMapper.build_message_class(definitions, port_type_message)
        expected = Class(
            qname=build_qname("bar", "bar"),
            status=Status.RAW,
            tag=Tag.ELEMENT,
            location="foo.wsdl",
            namespace="bar",
            ns_map=message.ns_map,
            attrs=attrs,
        )
        self.assertEqual(expected, actual)

    def test_get_or_create_inner_class(self) -> None:
        target = ClassFactory.create(
            location="foo", package=None, ns_map={"foo": "bar"}
        )

        actual = DefinitionsMapper.build_inner_class(target, "body")
        expected = ClassFactory.create(
            qname="{xsdata}body",
            tag=Tag.BINDING_MESSAGE,
            location=target.location,
            module=None,
            ns_map=target.ns_map,
        )
        self.assertEqual(expected, actual)
        self.assertIn(actual, target.inner)

        self.assertIsNot(actual.ns_map, target.ns_map)

        expected_attr = DefinitionsMapper.build_attr("body", "body", forward=True)
        self.assertEqual(expected_attr, target.attrs[0])

        repeat = DefinitionsMapper.build_inner_class(target, "body")
        self.assertIs(repeat, actual)

    def test_map_port_type_message(self) -> None:
        port_type_message = PortTypeMessage(message="foo:bar")
        port_type_message.ns_map["foo"] = "foobar"
        target_namespace = "xsdata"

        actual = DefinitionsMapper.map_port_type_message(
            None, port_type_message, target_namespace
        )
        expected = DefinitionsMapper.build_attr(
            "bar", qname=build_qname("foobar", "bar"), namespace=target_namespace
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual([expected], list(actual))

        actual = DefinitionsMapper.map_port_type_message(
            "Add", port_type_message, target_namespace
        )
        expected = DefinitionsMapper.build_attr(
            "Add", qname=build_qname("foobar", "bar"), namespace=target_namespace
        )

        self.assertIsInstance(actual, Generator)
        self.assertEqual([expected], list(actual))

    def test_operation_namespace(self) -> None:
        self.assertIsNone(DefinitionsMapper.operation_namespace({}))
        self.assertIsNone(DefinitionsMapper.operation_namespace({"transport": "foo"}))
        self.assertEqual(
            "http://schemas.xmlsoap.org/soap/envelope/",
            DefinitionsMapper.operation_namespace(
                {"transport": "http://schemas.xmlsoap.org/soap/http"}
            ),
        )

    def test_attributes(self) -> None:
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
