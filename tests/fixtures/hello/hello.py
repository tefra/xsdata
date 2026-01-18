from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://hello/"


@dataclass
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


@dataclass
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


@dataclass
class GetHelloAsString:
    class Meta:
        name = "getHelloAsString"
        namespace = "http://hello/"

    arg0: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GetHelloAsStringResponse:
    class Meta:
        name = "getHelloAsStringResponse"
        namespace = "http://hello/"

    return_value: None | str = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class HelloGetHelloAsStringInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HelloGetHelloAsStringInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        get_hello_as_string: None | GetHelloAsString = field(
            default=None,
            metadata={
                "name": "getHelloAsString",
                "type": "Element",
                "namespace": "http://hello/",
            },
        )


@dataclass
class HelloGetHelloAsStringOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HelloGetHelloAsStringOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
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

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
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

            @dataclass
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
