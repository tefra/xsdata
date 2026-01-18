from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://hello/"


@dataclass(kw_only=True)
class HelloByeError:
    class Meta:
        namespace = "http://hello/"

    message: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class HelloError:
    class Meta:
        namespace = "http://hello/"

    message: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class GetHelloAsString:
    class Meta:
        name = "getHelloAsString"
        namespace = "http://hello/"

    arg0: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class GetHelloAsStringResponse:
    class Meta:
        name = "getHelloAsStringResponse"
        namespace = "http://hello/"

    return_value: str = field(
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class HelloGetHelloAsStringInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HelloGetHelloAsStringInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        get_hello_as_string: GetHelloAsString = field(
            metadata={
                "name": "getHelloAsString",
                "type": "Element",
                "namespace": "http://hello/",
            }
        )


@dataclass(kw_only=True)
class HelloGetHelloAsStringOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HelloGetHelloAsStringOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        get_hello_as_string_response: None | GetHelloAsStringResponse = field(
            default=None,
            metadata={
                "name": "getHelloAsStringResponse",
                "type": "Element",
                "namespace": "http://hello/",
            },
        )
        fault: None | HelloGetHelloAsStringOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class Fault:
            faultcode: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: None | HelloGetHelloAsStringOutput.Body.Fault.Detail = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    },
                )
            )

            @dataclass(kw_only=True)
            class Detail:
                hello_error: None | HelloError = field(
                    default=None,
                    metadata={
                        "name": "HelloError",
                        "type": "Element",
                        "namespace": "http://hello/",
                    },
                )
                hello_bye_error: None | HelloByeError = field(
                    default=None,
                    metadata={
                        "name": "HelloByeError",
                        "type": "Element",
                        "namespace": "http://hello/",
                    },
                )


class HelloGetHelloAsString:
    style = "rpc"
    location = "http://localhost:9999/ws/hello"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = HelloGetHelloAsStringInput
    output = HelloGetHelloAsStringOutput
