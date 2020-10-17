from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://hello/"


@dataclass
class HelloByeError:
    """
    :ivar message:
    """
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
    """
    :ivar message:
    """
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
    """
    :ivar arg0:
    """
    class Meta:
        name = "getHelloAsString"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
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
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
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
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar get_hello_as_string:
        """
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
    """
    :ivar body:
    """
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
        """
        :ivar get_hello_as_string_response:
        :ivar fault:
        """
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
            """
            :ivar faultcode:
            :ivar faultstring:
            :ivar faultactor:
            :ivar detail:
            """
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
                """
                :ivar hello_error:
                :ivar hello_bye_error:
                """
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
