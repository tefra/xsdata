from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import BindingMessage
from xsdata.models.wsdl import BindingOperation
from xsdata.models.wsdl import Definitions
from xsdata.models.wsdl import Part
from xsdata.models.wsdl import PortType
from xsdata.models.wsdl import PortTypeMessage
from xsdata.models.wsdl import PortTypeOperation
from xsdata.models.wsdl import ServicePort
from xsdata.utils import collections
from xsdata.utils import text
from xsdata.utils.collections import first
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import local_name


class DefinitionsMapper:
    """
    Map a definitions instance to message and service classes.

    Currently only SOAP 1.1 bindings with rpc/document style is
    supported.
    """

    @classmethod
    def map(cls, definitions: Definitions) -> List[Class]:
        """Step 1: Main mapper entry point."""
        return [
            obj
            for service in definitions.services
            for port in service.ports
            for obj in cls.map_port(definitions, port)
        ]

    @classmethod
    def map_port(cls, definitions: Definitions, port: ServicePort) -> Iterator[Class]:
        """Step 2: Match a ServicePort to a Binding and PortType object and
        delegate the process to the next entry point."""

        binding = definitions.find_binding(text.suffix(port.binding))
        port_type = definitions.find_port_type(text.suffix(binding.type))

        elements = collections.concat(binding.extended_elements, port.extended_elements)
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
        """Step 3: Match every BindingOperation to a PortTypeOperation and
        delegate the process for each operation to the next entry point."""
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
        """Step 4: Convert a BindingOperation to a service class and delegate
        the process of all the message classes to the next entry point."""

        attrs = [
            cls.build_attr(key, str(DataType.STRING), native=True, default=config[key])
            for key in sorted(config.keys(), key=len)
            if config[key]
        ]

        style = config.get("style", "document")
        name = f"{name}_{binding_operation.name}"
        namespace = cls.operation_namespace(config)
        operation_messages = cls.map_binding_operation_messages(
            definitions, binding_operation, port_type_operation, name, style, namespace
        )
        for message_class in operation_messages:
            yield message_class
            # Only Envelope classes need to be added in service input/output
            if message_class.meta_name:
                message_type = message_class.name.split("_")[-1]
                attrs.append(cls.build_attr(message_type, message_class.qname))

        yield Class(
            qname=build_qname(definitions.target_namespace, name),
            status=Status.PROCESSED,
            tag=type(binding_operation).__name__,
            module=definitions.module,
            ns_map=binding_operation.ns_map,
            attrs=attrs,
        )

    @classmethod
    def map_binding_operation_messages(
        cls,
        definitions: Definitions,
        operation: BindingOperation,
        port_type_operation: PortTypeOperation,
        name: str,
        style: str,
        namespace: Optional[str],
    ) -> Iterator[Class]:
        """Step 5: Map the BindingOperation messages to classes."""

        messages: List[Tuple[str, BindingMessage, PortTypeMessage]] = []

        if operation.input:
            messages.append(("input", operation.input, port_type_operation.input))

        if operation.output:
            messages.append(("output", operation.output, port_type_operation.output))

        for suffix, binding_message, port_type_message in messages:

            if style == "rpc":
                yield cls.build_message_class(definitions, port_type_message)

            target = cls.build_envelope_class(
                definitions,
                binding_message,
                port_type_message,
                f"{name}_{suffix}",
                style,
                namespace,
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
        """Build inner fault class with default fields."""
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
            *[
                cls.build_attr(f, str(DataType.STRING), native=True, namespace="")
                for f in default_fields
            ],
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
    ) -> Class:
        """Step 6.1: Build Envelope class for the given binding message with
        attributes from the port type message."""

        target = Class(
            qname=build_qname(definitions.target_namespace, name),
            meta_name="Envelope",
            tag=Tag.BINDING_MESSAGE,
            module=definitions.module,
            ns_map=binding_message.ns_map,
            namespace=namespace,
        )
        message = port_type_message.message

        for ext in binding_message.extended_elements:
            assert ext.qname is not None
            class_name = local_name(ext.qname).title()
            inner = cls.build_inner_class(target, class_name)

            if style == "rpc" and class_name == "Body":
                namespace = ext.attributes.get("namespace")
                attrs = cls.map_port_type_message(port_type_message, namespace)
            else:
                attrs = cls.map_binding_message_parts(
                    definitions, message, ext, inner.ns_map
                )

            inner.attrs.extend(attrs)

        return target

    @classmethod
    def build_message_class(
        cls, definitions: Definitions, port_type_message: PortTypeMessage
    ) -> Class:
        """Step 6.2: Build the input/output message class of an rpc style
        operation."""
        message_name = text.suffix(port_type_message.message)
        definition_message = definitions.find_message(message_name)
        ns_map = definition_message.ns_map.copy()

        return Class(
            qname=build_qname(definitions.target_namespace, message_name),
            status=Status.PROCESSED,
            tag=Tag.ELEMENT,
            module=definitions.module,
            ns_map=ns_map,
            attrs=list(cls.build_parts_attributes(definition_message.parts, ns_map)),
        )

    @classmethod
    def build_inner_class(
        cls, target: Class, name: str, namespace: Optional[str] = None
    ) -> Class:
        """
        Build or retrieve an inner class for the given target class by the
        given name.

        This helper will also create a forward reference attribute for
        the parent class.
        """
        inner = first(inner for inner in target.inner if inner.name == name)
        if not inner:
            inner = Class(
                qname=build_qname(name),
                tag=Tag.BINDING_MESSAGE,
                module=target.module,
                ns_map=target.ns_map.copy(),
            )
            attr = cls.build_attr(name, inner.qname, forward=True, namespace=namespace)

            target.inner.append(inner)
            target.attrs.append(attr)

        return inner

    @classmethod
    def map_port_type_message(
        cls, message: PortTypeMessage, namespace: Optional[str]
    ) -> Iterator[Attr]:
        """Build an attribute for the given port type message."""
        prefix, name = text.split(message.message)
        source_namespace = message.ns_map.get(prefix)
        yield cls.build_attr(
            name, qname=build_qname(source_namespace, name), namespace=namespace
        )

    @classmethod
    def map_binding_message_parts(
        cls, definitions: Definitions, message: str, extended: AnyElement, ns_map: Dict
    ) -> Iterator[Attr]:
        """Find a Message instance and map its parts to attributes according to
        the the extensible element.."""
        parts = []
        if "part" in extended.attributes:
            parts.append(extended.attributes["part"])
        elif "parts" in extended.attributes:
            parts.extend(extended.attributes["parts"].split())

        if "message" in extended.attributes:
            message_name = local_name(extended.attributes["message"])
        else:
            message_name = text.suffix(message)

        definition_message = definitions.find_message(message_name)
        message_parts = definition_message.parts

        if parts:
            message_parts = [part for part in message_parts if part.name in parts]

        yield from cls.build_parts_attributes(message_parts, ns_map)

    @classmethod
    def build_parts_attributes(cls, parts: List[Part], ns_map: Dict) -> Iterator[Attr]:
        """
        Build attributes for the given list of parts.

        :param parts: List of parts
        :param ns_map: Namespace prefix-URI map
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
            type_qname = build_qname(namespace, type_name)
            native = namespace == Namespace.XS.uri
            namespace = "" if part.type else namespace

            yield cls.build_attr(name, type_qname, namespace=namespace, native=native)

    @classmethod
    def operation_namespace(cls, config: Dict) -> Optional[str]:
        transport = config.get("transport")
        namespace = None
        if transport == "http://schemas.xmlsoap.org/soap/http":
            namespace = "http://schemas.xmlsoap.org/soap/envelope/"

        return namespace

    @classmethod
    def attributes(cls, elements: Iterator[AnyElement]) -> Dict:
        """Return all attributes from all extended elements as a dictionary."""
        return {
            local_name(qname): value
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
    ) -> Attr:
        """Builder method for attributes."""
        occurs = 1 if default is not None else None
        return Attr(
            tag=Tag.ELEMENT,
            name=name,
            namespace=namespace,
            default=default,
            types=[AttrType(qname=qname, forward=forward, native=native)],
            restrictions=Restrictions(min_occurs=occurs, max_occurs=occurs),
        )
