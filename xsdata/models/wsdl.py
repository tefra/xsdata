from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional, TypeVar

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import get_name
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import Namespace
from xsdata.models.mixins import array_any_element, array_element, attribute, element
from xsdata.models.xsd import Schema
from xsdata.utils import collections


@dataclass
class Documentation:
    """WSDL Documentation model representation.

    Args:
        elements: A list of generic any elements
    """

    elements: List[object] = array_any_element()


@dataclass
class WsdlElement:
    """WSDL Base element model representation.

    Args:
        name: The element name
        documentation: The element documentation
        location: The element location
        ns_map: The element namespace prefix-URI map
    """

    name: str = attribute()
    documentation: Optional[Documentation] = element()
    location: Optional[str] = field(default=None, metadata={"type": "Ignore"})
    ns_map: Dict[str, str] = field(
        default_factory=dict, init=False, metadata={"type": "Ignore"}
    )


@dataclass
class ExtensibleElement(WsdlElement):
    """WSDL Extensible element model representation.

    Args:
        name: The element name
        documentation: The element documentation
        location: The element location
        ns_map: The element namespace prefix-URI map
        extended: A list of generic elements
    """

    extended: List[object] = array_any_element()

    @property
    def extended_elements(self) -> Iterator[AnyElement]:
        """Yields all generic element instances."""
        yield from (ext for ext in self.extended if isinstance(ext, AnyElement))


@dataclass
class Types:
    """WSDL Types model representation.

    Args:
        schemas: Inline xml schema definitions
        documentation: The type documentation
    """

    schemas: List[Schema] = array_element(name="schema", namespace=Namespace.XS.uri)
    documentation: Optional[Documentation] = element()


@dataclass
class Import:
    """WSDL Import model representation.

    Args:
        location: The location URI
        namespace: The namespace URI
    """

    location: Optional[str] = attribute()
    namespace: Optional[str] = attribute()


@dataclass
class Part(WsdlElement):
    """WSDL Part model representation.

    Args:
        name: The part name
        documentation: The part documentation
        location: The part location
        ns_map: The part namespace prefix-URI map
        type: The part type
        element: The part element
    """

    type: Optional[str] = attribute()
    element: Optional[str] = attribute()


@dataclass
class Message(WsdlElement):
    """WSDL Message model representation.

    Args:
        name: The message name
        documentation: The message documentation
        location: The message location
        ns_map: The message namespace prefix-URI map
        parts: The message parts
    """

    parts: List[Part] = array_element(name="part")


@dataclass
class PortTypeMessage(WsdlElement):
    """WSDL Port type message model representation.

    Args:
    Args:
        name: The port type name
        documentation: The port type documentation
        location: The port type location
        ns_map: The port type namespace prefix-URI map
        message: The port type message
    """

    message: str = attribute()


@dataclass
class PortTypeOperation(WsdlElement):
    """WSDL Port type operation model representation.

    Args:
        input: The input port type message instance
        output: The output port type message instance
        faults: The list of error port type message instances
    """

    input: PortTypeMessage = element()
    output: PortTypeMessage = element()
    faults: List[PortTypeMessage] = array_element(name="fault")


@dataclass
class PortType(ExtensibleElement):
    """WSDL Port type model representation.

    Args:
        name: The port type name
        documentation: The port type documentation
        location: The port type location
        ns_map: The port type namespace prefix-URI map
        extended: The port type extended elements
        operations: The port type operations
    """

    operations: List[PortTypeOperation] = array_element(name="operation")

    def find_operation(self, name: str) -> PortTypeOperation:
        """Find an operation by name or raise an error."""
        return find_or_die(self.operations, name, "PortTypeOperation")


@dataclass
class BindingMessage(ExtensibleElement):
    """WSDL Binding message model representation.

    Args:
        name: The message name
        documentation: The message documentation
        location: The message location
        ns_map: The message namespace prefix-URI map
        extended: The message extended elements
    """


@dataclass
class BindingOperation(ExtensibleElement):
    """WSDL Binding operation model representation.

    Args:
        input: The input binding message instance
        output: The output binding message instance
        faults: The list of error binding message instances
        name: The operation name
        documentation: The operation documentation
        location: The operation location
        ns_map: The operation namespace prefix-URI map
        extended: The operation extended elements
    """

    input: BindingMessage = element()
    output: BindingMessage = element()
    faults: List[BindingMessage] = array_element(name="fault")


@dataclass
class Binding(ExtensibleElement):
    """WSDL Binding model representation.

    Args:
        name: The binding name
        documentation: The binding documentation
        location: The binding location
        ns_map: The binding namespace prefix-URI map
        extended: The binding extended elements
        type: The binding type
        operations: The binding operations
    """

    type: str = attribute()
    operations: List[BindingOperation] = array_element(name="operation")

    def unique_operations(self) -> Iterator[BindingOperation]:
        """Yields all unique operation instances."""
        grouped_operations = collections.group_by(self.operations, key=get_name)

        for operations in grouped_operations.values():
            yield operations[-1]


@dataclass
class ServicePort(ExtensibleElement):
    """WSDL Service port model representation.

    Args:
        name: The port name
        documentation: The port documentation
        location: The port location
        ns_map: The port namespace prefix-URI map
        extended: The port extended elements
        binding: The port binding
    """

    binding: str = attribute()


@dataclass
class Service(WsdlElement):
    """WSDL Service model representation.

    Args:
        name: The service name
        documentation: The service documentation
        location: The service location
        ns_map: The service namespace prefix-URI map
        ports: The service ports
    """

    ports: List[ServicePort] = array_element(name="port")


@dataclass
class Definitions(ExtensibleElement):
    """WSDL Definitions model representation.

    Args:
        name: The definition name
        documentation: The definition documentation
        location: The definition location
        ns_map: The definition namespace prefix-URI map
        extended: A list of generic elements
        types: The definition types
        imports: The definition imports
        messages: The definition messages
        port_types: The definition port types
        bindings: The definition bindings
        services: The definition services
        extended: The definition extended elements
    """

    class Meta:
        """Metadata options."""

        name = "definitions"
        namespace = "http://schemas.xmlsoap.org/wsdl/"

    target_namespace: Optional[str] = attribute(name="targetNamespace")
    types: Optional[Types] = element()
    imports: List[Import] = array_element(name="import")
    messages: List[Message] = array_element(name="message")
    port_types: List[PortType] = array_element(name="portType")
    bindings: List[Binding] = array_element(name="binding")
    services: List[Service] = array_element(name="service")

    @property
    def schemas(self) -> Iterator[Schema]:
        """Yield all schema definitions."""
        if self.types:
            yield from self.types.schemas

    def find_binding(self, name: str) -> Binding:
        """Find a binding by name or raise an error."""
        return find_or_die(self.bindings, name, "Binding")

    def find_message(self, name: str) -> Message:
        """Find a message by name or raise an error."""
        return find_or_die(self.messages, name, "Message")

    def find_port_type(self, name: str) -> PortType:
        """Find a port type by name or raise an error."""
        return find_or_die(self.port_types, name, "PortType")

    def merge(self, source: "Definitions"):
        """Merge the source instance with this instance."""
        if not self.types:
            self.types = source.types
        elif source.types:
            self.types.schemas.extend(source.types.schemas)

        self.messages.extend(source.messages)
        self.port_types.extend(source.port_types)
        self.bindings.extend(source.bindings)
        self.services.extend(source.services)
        self.extended.extend(source.extended)

    def included(self) -> Iterator[Import]:
        """Yield all imports."""
        yield from self.imports


T = TypeVar("T", bound=WsdlElement)


def find_or_die(items: List[T], name: str, type_name: str) -> T:
    """Find an item by name or raise an error."""
    for msg in items:
        if msg.name == name:
            return msg

    raise CodegenError("Unknown WSDL Type", type=type_name, name=name)
