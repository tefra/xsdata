import operator
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import TypeVar

from xsdata.exceptions import DefinitionsValueError
from xsdata.models.enums import Namespace
from xsdata.models.mixins import array_any_element
from xsdata.models.mixins import array_element
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element
from xsdata.models.mixins import ModuleMixin
from xsdata.models.xsd import Schema
from xsdata.utils import collections


@dataclass
class Documentation:
    """
    :params elements:
    """

    elements: List[object] = array_any_element()


@dataclass
class WsdlElement:
    """
    :param name:
    :param documentation:
    """

    name: str = attribute()
    documentation: Optional[Documentation] = element()
    ns_map: Dict = field(default_factory=dict)


@dataclass
class Types:
    """
    :param schemas:
    :param documentation:
    """

    schemas: List[Schema] = array_element(name="schema", namespace=Namespace.XS.uri)
    documentation: Optional[Documentation] = element()


@dataclass
class Import:
    """
    :param location:
    :param namespace:
    """

    location: Optional[str] = attribute()
    namespace: Optional[str] = attribute()


@dataclass
class Part(WsdlElement):
    """
    :param type:
    :param element:
    """

    type: Optional[str] = attribute()
    element: Optional[str] = attribute()


@dataclass
class Message(WsdlElement):
    """
    :param part:
    """

    parts: List[Part] = array_element(name="part")


@dataclass
class PortTypeMessage(WsdlElement):
    """
    :param message:
    """

    message: str = attribute()


@dataclass
class PortTypeOperation(WsdlElement):
    """
    :param input:
    :param output:
    :param faults:
    """

    input: PortTypeMessage = element()
    output: PortTypeMessage = element()
    faults: List[PortTypeMessage] = array_element(name="fault")


@dataclass
class PortType(WsdlElement):
    """
    :param operations:
    """

    operations: List[PortTypeOperation] = array_element(name="operation")
    extended: List[object] = array_any_element()

    def find_operation(self, name: str) -> PortTypeOperation:
        return find_or_die(self.operations, name, "PortTypeOperation")


@dataclass
class BindingMessage(WsdlElement):
    """
    :param extended:
    """

    extended: List[object] = array_any_element()


@dataclass
class BindingOperation(WsdlElement):
    """
    :param input:
    :param output:
    :param faults:
    :param extended:
    """

    input: BindingMessage = element()
    output: BindingMessage = element()
    faults: List[BindingMessage] = array_element(name="fault")
    extended: List[object] = array_any_element()


@dataclass
class Binding(WsdlElement):
    """
    :param type:
    :param operations:
    :param extended:
    """

    type: str = attribute()
    operations: List[BindingOperation] = array_element(name="operation")
    extended: List[object] = array_any_element()

    def unique_operations(self) -> Iterator[BindingOperation]:
        name_attr = operator.attrgetter("name")
        grouped_operations = collections.group_by(self.operations, key=name_attr)

        for operations in grouped_operations.values():
            yield operations[-1]


@dataclass
class ServicePort(WsdlElement):
    """
    :param binding:
    :param extended:
    """

    binding: str = attribute()
    extended: List[object] = array_any_element()


@dataclass
class Service(WsdlElement):
    """
    :param ports:
    """

    ports: List[ServicePort] = array_element(name="port")


@dataclass
class Definitions(WsdlElement, ModuleMixin):
    """
    :param types:
    :param imports:
    :param messages:
    :param port_types:
    :param bindings:
    :param services:
    :param extended:
    """

    class Meta:
        name = "definitions"
        namespace = "http://schemas.xmlsoap.org/wsdl/"

    target_namespace: Optional[str] = attribute(name="targetNamespace")
    types: Optional[Types] = element()
    imports: List[Import] = array_element(name="import")
    messages: List[Message] = array_element(name="message")
    port_types: List[PortType] = array_element(name="portType")
    bindings: List[Binding] = array_element(name="binding")
    services: List[Service] = array_element(name="service")
    extended: List[object] = array_any_element()
    location: Optional[str] = field(default=None)

    @property
    def schemas(self):
        if self.types:
            yield from self.types.schemas

    def find_binding(self, name: str) -> Binding:
        return find_or_die(self.bindings, name, "Binding")

    def find_message(self, name: str) -> Message:
        return find_or_die(self.messages, name, "Message")

    def find_port_type(self, name: str) -> PortType:
        return find_or_die(self.port_types, name, "PortType")

    def merge(self, source: "Definitions"):
        if not self.types:
            self.types = source.types
        elif source.types:
            self.types.schemas.extend(source.types.schemas)

        self.messages.extend(source.messages)
        self.port_types.extend(source.port_types)
        self.bindings.extend(source.bindings)
        self.services.extend(source.services)
        self.extended.extend(source.extended)


T = TypeVar("T", bound="WsdlElement")


def find_or_die(items: List[T], name: str, type_name: str) -> T:
    result = next((msg for msg in items if msg.name == name), None)

    if result:
        return result

    raise DefinitionsValueError(f"Unknown {type_name} name: {name}")
