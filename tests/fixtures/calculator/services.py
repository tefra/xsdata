from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://tempuri.org/"


@dataclass(kw_only=True)
class Add:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int = field(
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: int = field(
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AddResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    add_result: int = field(
        metadata={
            "name": "AddResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Divide:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int = field(
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: int = field(
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DivideResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    divide_result: int = field(
        metadata={
            "name": "DivideResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Multiply:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int = field(
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: int = field(
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MultiplyResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    multiply_result: int = field(
        metadata={
            "name": "MultiplyResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Subtract:
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: int = field(
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: int = field(
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SubtractResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    subtract_result: int = field(
        metadata={
            "name": "SubtractResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CalculatorSoapAddInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapAddInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        add: Add = field(
            metadata={
                "name": "Add",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass(kw_only=True)
class CalculatorSoapAddOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapAddOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        add_response: None | AddResponse = field(
            default=None,
            metadata={
                "name": "AddResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: None | CalculatorSoapAddOutput.Body.Fault = field(
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
            detail: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass(kw_only=True)
class CalculatorSoapDivideInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapDivideInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        divide: Divide = field(
            metadata={
                "name": "Divide",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass(kw_only=True)
class CalculatorSoapDivideOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapDivideOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        divide_response: None | DivideResponse = field(
            default=None,
            metadata={
                "name": "DivideResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: None | CalculatorSoapDivideOutput.Body.Fault = field(
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
            detail: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass(kw_only=True)
class CalculatorSoapMultiplyInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapMultiplyInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        multiply: Multiply = field(
            metadata={
                "name": "Multiply",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass(kw_only=True)
class CalculatorSoapMultiplyOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapMultiplyOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        multiply_response: None | MultiplyResponse = field(
            default=None,
            metadata={
                "name": "MultiplyResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: None | CalculatorSoapMultiplyOutput.Body.Fault = field(
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
            detail: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass(kw_only=True)
class CalculatorSoapSubtractInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapSubtractInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        subtract: Subtract = field(
            metadata={
                "name": "Subtract",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass(kw_only=True)
class CalculatorSoapSubtractOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculatorSoapSubtractOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        subtract_response: None | SubtractResponse = field(
            default=None,
            metadata={
                "name": "SubtractResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        fault: None | CalculatorSoapSubtractOutput.Body.Fault = field(
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
            detail: None | str = field(
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
