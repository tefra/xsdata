from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://hello/"


@dataclass
class HelloByeError:
    class Meta:
        namespace = "http://hello/"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class HelloError:
    class Meta:
        namespace = "http://hello/"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetHelloAsString:
    class Meta:
        name = "getHelloAsString"
        namespace = "http://hello/"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetHelloAsStringResponse:
    class Meta:
        name = "getHelloAsStringResponse"
        namespace = "http://hello/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class HelloGetHelloAsStringInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["HelloGetHelloAsStringInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_hello_as_string: Optional[GetHelloAsString] = field(
            default=None,
            metadata={
                "name": "getHelloAsString",
                "type": "Element",
                "namespace": "http://hello/",
            }
        )


@dataclass
class HelloGetHelloAsStringOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["HelloGetHelloAsStringOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_hello_as_string_response: Optional[GetHelloAsStringResponse] = field(
            default=None,
            metadata={
                "name": "getHelloAsStringResponse",
                "type": "Element",
                "namespace": "http://hello/",
            }
        )
        fault: Optional["HelloGetHelloAsStringOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["HelloGetHelloAsStringOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                hello_error: Optional[HelloError] = field(
                    default=None,
                    metadata={
                        "name": "HelloError",
                        "type": "Element",
                        "namespace": "http://hello/",
                    }
                )
                hello_bye_error: Optional[HelloByeError] = field(
                    default=None,
                    metadata={
                        "name": "HelloByeError",
                        "type": "Element",
                        "namespace": "http://hello/",
                    }
                )


class HelloGetHelloAsString:
    style = "rpc"
    location = "http://localhost:9999/ws/hello"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = HelloGetHelloAsStringInput
    output = HelloGetHelloAsStringOutput
