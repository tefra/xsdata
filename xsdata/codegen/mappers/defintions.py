from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from lxml.etree import QName

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Status
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import BindingMessage
from xsdata.models.wsdl import BindingOperation
from xsdata.models.wsdl import Definitions
from xsdata.models.wsdl import PortType
from xsdata.models.wsdl import PortTypeMessage
from xsdata.models.wsdl import PortTypeOperation
from xsdata.models.wsdl import ServicePort
from xsdata.utils import text


class DefinitionsMapper:
    """Map a definitions instance to message and service classes."""

    @classmethod
    def map(cls, definitions: Definitions) -> List[Class]:
        """Main mapper entry point."""
        return [
            obj
            for service in definitions.services
            for port in service.ports
            for obj in cls.map_port(definitions, port)
        ]

    @classmethod
    def map_port(cls, definitions: Definitions, port: ServicePort) -> Iterator[Class]:
        """Match a ServicePort to a Binding and PortType object and delegate
        the process to the next entry point."""

        binding = definitions.find_binding(text.suffix(port.binding))
        port_type = definitions.find_port_type(text.suffix(binding.type))
        config = cls.attributes(binding.extended)
        config.update(cls.attributes(port.extended))

        yield from cls.map_binding(definitions, binding, port_type, config)

    @classmethod
    def map_binding(
        cls,
        definitions: Definitions,
        binding: Binding,
        port_type: PortType,
        config: Dict,
    ) -> Iterator[Class]:
        """Match every BindingOperation to a PortTypeOperation and delegate the
        process for each operation to the next entry point."""
        for operation in binding.unique_operations():
            cfg = config.copy()
            cfg.update(cls.attributes(operation.extended))
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
        """Convert a BindingOperation to a service class and delegate the
        process of all the message classes to the next entry point."""

        attrs = [
            cls.build_attr(key, DataType.STRING.qname, native=True, default=config[key])
            for key in sorted(config.keys(), key=len)
            if config[key]
        ]

        name = f"{name}_{binding_operation.name}"
        namespace = cls.operation_namespace(config)
        operation_messages = cls.map_binding_operation_messages(
            definitions, binding_operation, port_type_operation, name, namespace
        )
        for message_name, message_class in operation_messages:
            yield message_class
            attrs.append(cls.build_attr(message_name, message_class.qname))

        yield Class(
            qname=QName(definitions.target_namespace, name),
            status=Status.PROCESSED,
            type=type(binding_operation),
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
        namespace: Optional[str],
    ) -> Iterator[Tuple[str, Class]]:
        """Map the BindingOperation messages to classes."""

        messages: List[Tuple[str, BindingMessage, PortTypeMessage]] = []

        if operation.input:
            messages.append(("input", operation.input, port_type_operation.input))

        if operation.output:
            messages.append(("output", operation.output, port_type_operation.output))

        # todo: faults
        for suffix, binding_message, port_type_message in messages:
            yield suffix, cls.map_binding_operation_message(
                definitions,
                binding_message,
                port_type_message,
                name=f"{name}_{suffix}",
                namespace=namespace,
            )

    @classmethod
    def map_binding_operation_message(
        cls,
        definitions: Definitions,
        binding_message: BindingMessage,
        port_type_message: PortTypeMessage,
        name: str,
        namespace: Optional[str],
    ) -> Class:
        """Map a BindingMessage to class instance."""

        target = Class(
            qname=QName(definitions.target_namespace, name),
            meta_name="Envelope",
            type=type(binding_message),
            module=definitions.module,
            ns_map=binding_message.ns_map,
            namespace=namespace,
        )

        message = port_type_message.message
        for ext in binding_message.extended:
            if not isinstance(ext, AnyElement):
                continue

            local_name = QName(ext.qname).localname.title()
            inner = next(
                (inner for inner in target.inner if inner.name == local_name), None
            )
            if not inner:
                inner = Class(
                    qname=QName(local_name),
                    type=BindingMessage,
                    module=definitions.module,
                    ns_map=binding_message.ns_map.copy(),
                )
                attr = cls.build_attr(local_name, inner.qname, forward=True)

                target.inner.append(inner)
                target.attrs.append(attr)

            attrs = cls.map_message_parts(definitions, message, ext, inner.ns_map)
            inner.attrs.extend(attrs)

        return target

    @classmethod
    def map_message_parts(
        cls, definitions: Definitions, message: str, extended: AnyElement, ns_map: Dict
    ) -> Iterator[Attr]:
        """Find a Message instance and map its parts to attributes."""
        parts = []
        message_name = text.suffix(message)

        if "part" in extended.attributes:
            parts.append(extended.attributes["part"])
            message_name = QName(extended.attributes["message"]).localname
        elif "parts" in extended.attributes:
            parts.extend(
                filter(None, map(str.strip, extended.attributes["parts"].split(" ")))
            )

        all_parts = len(parts) == 0
        definition_message = definitions.find_message(message_name)

        for part in definition_message.parts:
            if all_parts or part.name in parts:
                type_name = part.element or part.type or ""
                prefix, name = text.split(type_name)
                namespace = part.ns_map.get(prefix)
                ns_map.update(part.ns_map)
                qname = QName(namespace, name)
                yield cls.build_attr(name, qname, namespace=namespace)

    @classmethod
    def operation_namespace(cls, config: Dict) -> Optional[str]:
        transport = config.get("transport")
        namespace = None
        if transport == "http://schemas.xmlsoap.org/soap/http":
            namespace = "http://schemas.xmlsoap.org/soap/envelope/"

        return namespace

    @classmethod
    def attributes(cls, elements: List) -> Dict:
        """Return all attributes from all extended elements as a dictionary."""
        return {
            QName(qname).localname: value
            for element in elements
            if isinstance(element, AnyElement)
            for qname, value in element.attributes.items()
        }

    @classmethod
    def build_attr(
        cls,
        name: str,
        qname: QName,
        native: bool = False,
        forward: bool = False,
        namespace: Optional[str] = None,
        default: Optional[str] = None,
    ) -> Attr:
        """Builder method for attributes."""
        return Attr(
            tag=Tag.ELEMENT,
            name=name,
            local_name=name,
            namespace=namespace,
            default=default,
            types=[AttrType(qname=qname, forward=forward, native=native)],
        )
