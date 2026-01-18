from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class Add:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int | None = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        },
    )
    int_b: int | None = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AddResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    add_result: int | None = field(
        default=None,
        metadata={
            "name": "AddResult",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Divide:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int | None = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        },
    )
    int_b: int | None = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DivideResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    divide_result: int | None = field(
        default=None,
        metadata={
            "name": "DivideResult",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Multiply:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int | None = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        },
    )
    int_b: int | None = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MultiplyResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    multiply_result: int | None = field(
        default=None,
        metadata={
            "name": "MultiplyResult",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Subtract:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int | None = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        },
    )
    int_b: int | None = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubtractResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    subtract_result: int | None = field(
        default=None,
        metadata={
            "name": "SubtractResult",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CalculatorSoapAddInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapAddInput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        add: Add | None = field(
            default=None,
            metadata={
                "name": "Add",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class CalculatorSoapAddOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapAddOutput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        add_response: AddResponse | None = field(
            default=None,
            metadata={
                "name": "AddResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: CalculatorSoapAddOutput.Body.Fault | None = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class CalculatorSoapDivideInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapDivideInput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        divide: Divide | None = field(
            default=None,
            metadata={
                "name": "Divide",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class CalculatorSoapDivideOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapDivideOutput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        divide_response: DivideResponse | None = field(
            default=None,
            metadata={
                "name": "DivideResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: CalculatorSoapDivideOutput.Body.Fault | None = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class CalculatorSoapMultiplyInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapMultiplyInput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        multiply: Multiply | None = field(
            default=None,
            metadata={
                "name": "Multiply",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class CalculatorSoapMultiplyOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapMultiplyOutput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        multiply_response: MultiplyResponse | None = field(
            default=None,
            metadata={
                "name": "MultiplyResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: CalculatorSoapMultiplyOutput.Body.Fault | None = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class CalculatorSoapSubtractInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapSubtractInput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        subtract: Subtract | None = field(
            default=None,
            metadata={
                "name": "Subtract",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class CalculatorSoapSubtractOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapSubtractOutput.Body | None = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        subtract_response: SubtractResponse | None = field(
            default=None,
            metadata={
                "name": "SubtractResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: CalculatorSoapSubtractOutput.Body.Fault | None = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class CalculatorSoapAdd:
    style = "document"
    location = "http://www.dneonline.com/calculator.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/Add"
    input = CalculatorSoapAddInput
    output = CalculatorSoapAddOutput


class CalculatorSoapDivide:
    style = "document"
    location = "http://www.dneonline.com/calculator.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/Divide"
    input = CalculatorSoapDivideInput
    output = CalculatorSoapDivideOutput


class CalculatorSoapMultiply:
    style = "document"
    location = "http://www.dneonline.com/calculator.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/Multiply"
    input = CalculatorSoapMultiplyInput
    output = CalculatorSoapMultiplyOutput


class CalculatorSoapSubtract:
    style = "document"
    location = "http://www.dneonline.com/calculator.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/Subtract"
    input = CalculatorSoapSubtractInput
    output = CalculatorSoapSubtractOutput
