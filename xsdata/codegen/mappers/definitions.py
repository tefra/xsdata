import itertools
from typing import Dict, Iterator, List, Optional, Tuple

from xsdata.codegen.models import Attr, AttrType, Class, Restrictions, Status
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.logger import logger
from xsdata.models.enums import DataType, Namespace, Tag
from xsdata.models.wsdl import (
    Binding,
    BindingMessage,
    BindingOperation,
    Definitions,
    Part,
    PortType,
    PortTypeMessage,
    PortTypeOperation,
    ServicePort,
)
from xsdata.utils import collections, namespaces, text


class DefinitionsMapper:
    """Map a definitions instance to message and service classes.

    Currently, only SOAP 1.1 bindings with rpc/document style is
    supported.
    """

    @classmethod
    def map(cls, definitions: Definitions) -> List[Class]:
        """Main entrypoint for this mapper.

        Iterates over their services and their ports and build
        the binding and service classes.

        Args:
            definitions: The definitions instance to map.

        Returns:
            The generated class instances
        """
        return [
            obj
            for service in definitions.services
            for port in service.ports
            for obj in cls.map_port(definitions, port)
        ]

    @classmethod
    def map_port(cls, definitions: Definitions, port: ServicePort) -> Iterator[Class]:
        """Map a service port into binding and service classes.

        Match a ServicePort to a Binding and PortType object and
        delegate the process to the next entry point.

        Args:
            definitions: The definitions instance
            port: The service port instance

        Yields:
            An iterator of class instances.
        """
        binding = definitions.find_binding(text.suffix(port.binding))
        port_type = definitions.find_port_type(text.suffix(binding.type))

        elements = itertools.chain(binding.extended_elements, port.extended_elements)
        config = cls.attributes(elements)

        yield from cls.map_binding(definitions, binding, port_type, config)

    @classmethod
    def map_binding(
        cls,
        definitions: Definitions,
        binding: Binding,
        port_type: PortType,
        config: Dict,
    ) -> Iterator[Class]:
        """Map binding operations into binding and service classes.

        Match every BindingOperation to a PortTypeOperation and
        delegate the process for each operation to the next entry point.

        Args:
            definitions: The definitions instance
            binding: The binding instance
            port_type: The port type instance
            config: Configuration dictionary

        Yields:
            An iterator of class instances.
        """
        for operation in binding.unique_operations():
            cfg = config.copy()
            cfg.update(cls.attributes(operation.extended_elements))
            port_operation = port_type.find_operation(operation.name)

            yield from cls.map_binding_operation(
                definitions, operation, port_operation, cfg, port_type.name
            )

    @classmethod
    def map_binding_operation(
        cls,
        definitions: Definitions,
        binding_operation: BindingOperation,
        port_type_operation: PortTypeOperation,
        config: Dict,
        name: str,
    ) -> Iterator[Class]:
        """Map a binding operation to a service and binding classes.

        Convert a BindingOperation to a service class and delegate
        the process of all the message classes to the next entry point.

        Args:
            definitions: The definitions instance
            binding_operation: The binding operation instance
            port_type_operation: The port type operation instance
            config: Configuration dictionary
            name: The operation name

        Yields:
            An iterator of class instances.
        """
        attrs = [
            cls.build_attr(key, str(DataType.STRING), native=True, default=config[key])
            for key in sorted(config.keys(), key=len)
            if config[key]
        ]

        style = config.get("style", "document")
        name = f"{name}_{binding_operation.name}"
        namespace = cls.operation_namespace(config)
        operation_messages = cls.map_binding_operation_messages(
            definitions,
            binding_operation,
            port_type_operation,
            name,
            style,
            namespace,
        )
        for message_class in operation_messages:
            yield message_class
            # Only Envelope classes need to be added in service input/output
            if message_class.meta_name:
                message_type = message_class.name.split("_")[-1]
                attrs.append(
                    cls.build_attr(
                        message_type, message_class.qname, reference=id(message_class)
                    )
                )

        assert binding_operation.location is not None

        yield Class(
            qname=namespaces.build_qname(definitions.target_namespace, name),
            status=Status.FLATTENED,
            tag=type(binding_operation).__name__,
            location=binding_operation.location,
            ns_map=binding_operation.ns_map,
            attrs=attrs,
        )

    @classmethod
    def map_binding_operation_messages(
        cls,
        definitions: Definitions,
        binding_operation: BindingOperation,
        port_type_operation: PortTypeOperation,
        name: str,
        style: str,
        namespace: Optional[str],
    ) -> Iterator[Class]:
        """Map the binding operation messages to binding classes.

        Args:
            definitions: The definitions instance
            binding_operation: The binding operation instance
            port_type_operation: The port type operation instance
            name: The operation name
            style: The operation style
            namespace: The operation namespace

        Yields:
            An iterator of class instances.
        """
        messages: List[Tuple[str, BindingMessage, PortTypeMessage, Optional[str]]] = []

        if binding_operation.input:
            messages.append(
                (
                    "input",
                    binding_operation.input,
                    port_type_operation.input,
                    binding_operation.name,
                )
            )

        if binding_operation.output:
            messages.append(
                ("output", binding_operation.output, port_type_operation.output, None)
            )

        for suffix, binding_message, port_type_message, operation_name in messages:
            if style == "rpc":
                yield cls.build_message_class(definitions, port_type_message)

            target = cls.build_envelope_class(
                definitions,
                binding_message,
                port_type_message,
                f"{name}_{suffix}",
                style,
                namespace,
                operation_name,
            )

            if suffix == "output":
                cls.build_envelope_fault(definitions, port_type_operation, target)

            yield target

    @classmethod
    def build_envelope_fault(
        cls,
        definitions: Definitions,
        port_type_operation: PortTypeOperation,
        target: Class,
    ):
        """Add an inner message fault class with default fields.

        Args:
            definitions: The definitions instance
            port_type_operation: The port type operation instance
            target: The target class instance
        """
        ns_map: Dict = {}
        body = next(inner for inner in target.inner if inner.name == "Body")
        fault_class = cls.build_inner_class(body, "Fault", target.namespace)

        detail_attrs: List[Attr] = []
        for fault in port_type_operation.faults:
            message = definitions.find_message(text.suffix(fault.message))
            detail_attrs.extend(cls.build_parts_attributes(message.parts, ns_map))

        default_fields = ["faultcode", "faultstring", "faultactor"]
        if detail_attrs:
            detail = cls.build_inner_class(fault_class, "detail", namespace="")
            detail.attrs.extend(detail_attrs)
        else:
            default_fields.append("detail")

        collections.prepend(
            fault_class.attrs,
            *(
                cls.build_attr(f, str(DataType.STRING), native=True, namespace="")
                for f in default_fields
            ),
        )

    @classmethod
    def build_envelope_class(
        cls,
        definitions: Definitions,
        binding_message: BindingMessage,
        port_type_message: PortTypeMessage,
        name: str,
        style: str,
        namespace: Optional[str],
        operation: Optional[str],
    ) -> Class:
        """Map the binding message to an envelope class.

        Args:
            definitions: The definitions instance
            binding_message: The port type message instance
            port_type_message: The port type message instance
            name: The class name
            style: The operation style e.g. rpc
            namespace: The operation namespace
            operation: The custom operation name, if it's empty
                the message name will be used instead

        Returns:
            The class instance.
        """
        assert binding_message.location is not None

        target = Class(
            qname=namespaces.build_qname(definitions.target_namespace, name),
            meta_name="Envelope",
            tag=Tag.BINDING_MESSAGE,
            location=binding_message.location,
            ns_map=binding_message.ns_map,
            namespace=namespace,
        )
        message = port_type_message.message

        for ext in binding_message.extended_elements:
            assert ext.qname is not None
            class_name = namespaces.local_name(ext.qname).title()
            inner = cls.build_inner_class(target, class_name)

            if style == "rpc" and class_name == "Body":
                namespace = ext.attributes.get("namespace")
                attrs = cls.map_port_type_message(
                    operation, port_type_message, namespace
                )
            else:
                attrs = cls.map_binding_message_parts(
                    definitions, message, ext, inner.ns_map
                )

            inner.attrs.extend(attrs)

        return target

    @classmethod
    def build_message_class(
        cls,
        definitions: Definitions,
        port_type_message: PortTypeMessage,
    ) -> Class:
        """Map the input/output message of a rpc style operation.

        Args:
            definitions: The definitions instance
            port_type_message: The port type message instance

        Returns:
            The class instance.
        """
        prefix, name = text.split(port_type_message.message)

        definition_message = definitions.find_message(name)
        ns_map = definition_message.ns_map.copy()
        source_namespace = ns_map.get(prefix)

        assert port_type_message.location is not None

        return Class(
            qname=namespaces.build_qname(source_namespace, name),
            namespace=source_namespace,
            status=Status.RAW,
            tag=Tag.ELEMENT,
            location=port_type_message.location,
            ns_map=ns_map,
            attrs=list(cls.build_parts_attributes(definition_message.parts, ns_map)),
        )

    @classmethod
    def build_inner_class(
        cls, target: Class, name: str, namespace: Optional[str] = None
    ) -> Class:
        """Build or retrieve an inner class.

        This helper will also create a forward reference attribute for
        the parent class.

        Args:
            target: The parent class instance
            name: The inner class name
            namespace: The inner class namespace

        Returns:
            The inner class instance.
        """
        inner = collections.first(inner for inner in target.inner if inner.name == name)
        if not inner:
            inner = Class(
                qname=namespaces.build_qname(target.target_namespace, name),
                tag=Tag.BINDING_MESSAGE,
                location=target.location,
                ns_map=target.ns_map.copy(),
            )
            attr = cls.build_attr(name, inner.qname, forward=True, namespace=namespace)

            target.inner.append(inner)
            target.attrs.append(attr)

        return inner

    @classmethod
    def map_port_type_message(
        cls,
        operation: Optional[str],
        message: PortTypeMessage,
        namespace: Optional[str],
    ) -> Iterator[Attr]:
        """Build an attribute for the given port type message.

        Args:
            operation: The operation name, use the message name
                if it's empty
            message: The port type message instance
            namespace: The operation namespace

        Yields:
            An iterator of class attrs.
        """
        prefix, name = text.split(message.message)
        source_namespace = message.ns_map.get(prefix)

        if operation is None:
            operation = name

        yield cls.build_attr(
            operation,
            qname=namespaces.build_qname(source_namespace, name),
            namespace=namespace,
        )

    @classmethod
    def map_binding_message_parts(
        cls, definitions: Definitions, message: str, extended: AnyElement, ns_map: Dict
    ) -> Iterator[Attr]:
        """Find a Message instance and map its parts to attrs.

        Args:
            definitions: The definitions instance
            message: The message qualified name
            extended: The related extended element
            ns_map: The namespace prefix-URI map

        Yields:
            An iterator of class attrs.
        """
        parts = []
        if "part" in extended.attributes:
            parts.append(extended.attributes["part"])
        elif "parts" in extended.attributes:
            parts.extend(extended.attributes["parts"].split())

        if "message" in extended.attributes:
            message_name = namespaces.local_name(extended.attributes["message"])
        else:
            message_name = text.suffix(message)

        definition_message = definitions.find_message(message_name)
        message_parts = definition_message.parts

        if parts:
            message_parts = [part for part in message_parts if part.name in parts]

        yield from cls.build_parts_attributes(message_parts, ns_map)

    @classmethod
    def build_parts_attributes(cls, parts: List[Part], ns_map: Dict) -> Iterator[Attr]:
        """Build attributes for the given list of parts.

        Args:
            parts: A list of part instances
            ns_map: The namespace prefix-URI map

        Yields:
            An iterator of class attrs.
        """
        for part in parts:
            if part.element:
                prefix, type_name = text.split(part.element)
                name = type_name
            elif part.type:
                prefix, type_name = text.split(part.type)
                name = part.name
            else:
                logger.warning("Skip untyped message part %s", part.name)
                continue

            ns_map.update(part.ns_map)
            namespace = part.ns_map.get(prefix)
            type_qname = namespaces.build_qname(namespace, type_name)
            native = namespace == Namespace.XS.uri
            # If part has a type it could reference an element or a complex type or
            # a simple type, we can't make that detection yet, postpone it till the
            # classes processing.
            namespace = "##lazy" if part.type else namespace
            yield cls.build_attr(name, type_qname, namespace=namespace, native=native)

    @classmethod
    def operation_namespace(cls, config: Dict) -> Optional[str]:
        """Return the operation namespace by the operation transport.

        Args:
            config: The operation configuration

        Returns:
            The operation namespace string or None if transport is not soap.
        """
        transport = config.get("transport")
        namespace = None
        if transport == "http://schemas.xmlsoap.org/soap/http":
            namespace = "http://schemas.xmlsoap.org/soap/envelope/"

        return namespace

    @classmethod
    def attributes(cls, elements: Iterator[AnyElement]) -> Dict:
        """Return all attributes from all extended elements as a dictionary.

        Args:
            elements: An iterator of generic elements

        Returns:
            A key-value mapping of the xml attributes.
        """
        return {
            namespaces.local_name(qname): value
            for element in elements
            if isinstance(element, AnyElement)
            for qname, value in element.attributes.items()
        }

    @classmethod
    def build_attr(
        cls,
        name: str,
        qname: str,
        native: bool = False,
        forward: bool = False,
        namespace: Optional[str] = None,
        default: Optional[str] = None,
        reference: int = 0,
    ) -> Attr:
        """Helper method to build an attr instance.

        Args:
            name: The attr name
            qname: The attr qualified name
            native: Whether the type is native
            forward: Whether the type is a forward reference
            namespace: The attr namespace
            default: The attr default value
            reference: The class id reference, if any

        Returns:
            The new attr instance.
        """
        occurs = 1 if default is not None else None
        if native:
            namespace = ""

        return Attr(
            tag=Tag.ELEMENT,
            name=name,
            namespace=namespace,
            default=default,
            types=[
                AttrType(
                    qname=qname, forward=forward, native=native, reference=reference
                )
            ],
            restrictions=Restrictions(min_occurs=occurs, max_occurs=occurs),
        )
