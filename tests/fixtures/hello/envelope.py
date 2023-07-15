from dataclasses import dataclass, field
from typing import Optional


@dataclass
class HelloError:
    class Meta:
        namespace = "http://hello/"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "required": True,
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
            "required": True,
        }
    )


@dataclass
class Detail:
    class Meta:
        name = "detail"
        namespace = ""

    hello_error: Optional[HelloError] = field(
        default=None,
        metadata={
            "name": "HelloError",
            "type": "Element",
            "namespace": "http://hello/",
            "required": True,
        }
    )


@dataclass
class Fault:
    class Meta:
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    faultcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    faultstring: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    detail: Optional[Detail] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Body:
    class Meta:
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    get_hello_as_string: Optional[GetHelloAsString] = field(
        default=None,
        metadata={
            "name": "getHelloAsString",
            "type": "Element",
            "namespace": "http://hello/",
        }
    )
    get_hello_as_string_response: Optional[GetHelloAsStringResponse] = field(
        default=None,
        metadata={
            "name": "getHelloAsStringResponse",
            "type": "Element",
            "namespace": "http://hello/",
        }
    )
    fault: Optional[Fault] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
        }
    )


@dataclass
class Envelope:
    class Meta:
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[Body] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
            "required": True,
        }
    )
