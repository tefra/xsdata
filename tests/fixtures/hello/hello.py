from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://hello/"


@dataclass
class GetHelloAsString:
    """
    :ivar arg0:
    """
    class Meta:
        name = "getHelloAsString"

    arg0: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class GetHelloAsStringResponse:
    """
    :ivar return_value:
    """
    class Meta:
        name = "getHelloAsStringResponse"

    return_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="return",
            type="Element",
            namespace=""
        )
    )


@dataclass
class HelloGetHelloAsStringInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["HelloGetHelloAsStringInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar get_hello_as_string:
        """
        get_hello_as_string: Optional[GetHelloAsString] = field(
            default=None,
            metadata=dict(
                name="getHelloAsString",
                type="Element",
                namespace="http://hello/"
            )
        )


@dataclass
class HelloGetHelloAsStringOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["HelloGetHelloAsStringOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar get_hello_as_string_response:
        """
        get_hello_as_string_response: Optional[GetHelloAsStringResponse] = field(
            default=None,
            metadata=dict(
                name="getHelloAsStringResponse",
                type="Element",
                namespace="http://hello/"
            )
        )


class HelloGetHelloAsString:
    style = "rpc"
    location = "http://localhost:9999/ws/hello"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = HelloGetHelloAsStringInput
    output = HelloGetHelloAsStringOutput
