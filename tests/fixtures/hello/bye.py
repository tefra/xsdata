from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.hello.envelope import (
    HelloError,
    GetHelloAsString,
    GetHelloAsStringResponse,
)
from tests.fixtures.hello.hello import HelloByeError

__NAMESPACE__ = "http://hello/"


@dataclass
class GetByeAsString:
    class Meta:
        name = "getByeAsString"
        namespace = "http://hello/"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GetByeAsStringResponse:
    class Meta:
        name = "getByeAsStringResponse"
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
class ByeGetByeAsStringInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ByeGetByeAsStringInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_bye_as_string: Optional[GetByeAsString] = field(
            default=None,
            metadata={
                "name": "getByeAsString",
                "type": "Element",
                "namespace": "http://hello/",
            }
        )


@dataclass
class ByeGetByeAsStringOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ByeGetByeAsStringOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_bye_as_string_response: Optional[GetByeAsStringResponse] = field(
            default=None,
            metadata={
                "name": "getByeAsStringResponse",
                "type": "Element",
                "namespace": "http://hello/",
            }
        )
        fault: Optional["ByeGetByeAsStringOutput.Body.Fault"] = field(
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
            detail: Optional["ByeGetByeAsStringOutput.Body.Fault.Detail"] = field(
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


class ByeGetByeAsString:
    style = "rpc"
    location = "http://localhost:9999/ws/bye"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ByeGetByeAsStringInput
    output = ByeGetByeAsStringOutput


class HelloGetHelloAsString:
    style = "rpc"
    location = "http://localhost:9999/ws/hello"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = HelloGetHelloAsStringInput
    output = HelloGetHelloAsStringOutput
