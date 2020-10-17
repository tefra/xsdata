from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class Add:
    """
    :ivar int_a:
    :ivar int_b:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AddResponse:
    """
    :ivar add_result:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    add_result: Optional[int] = field(
        default=None,
        metadata={
            "name": "AddResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Divide:
    """
    :ivar int_a:
    :ivar int_b:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DivideResponse:
    """
    :ivar divide_result:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    divide_result: Optional[int] = field(
        default=None,
        metadata={
            "name": "DivideResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Multiply:
    """
    :ivar int_a:
    :ivar int_b:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MultiplyResponse:
    """
    :ivar multiply_result:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    multiply_result: Optional[int] = field(
        default=None,
        metadata={
            "name": "MultiplyResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Subtract:
    """
    :ivar int_a:
    :ivar int_b:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    int_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "intA",
            "type": "Element",
            "required": True,
        }
    )
    int_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "intB",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SubtractResponse:
    """
    :ivar subtract_result:
    """
    class Meta:
        namespace = "http://tempuri.org/"

    subtract_result: Optional[int] = field(
        default=None,
        metadata={
            "name": "SubtractResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CalculatorSoapAddInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapAddInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar add:
        """
        add: Optional[Add] = field(
            default=None,
            metadata={
                "name": "Add",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class CalculatorSoapAddOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapAddOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar add_response:
        :ivar fault:
        """
        add_response: Optional[AddResponse] = field(
            default=None,
            metadata={
                "name": "AddResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["CalculatorSoapAddOutput.Body.Fault"] = field(
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
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class CalculatorSoapDivideInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapDivideInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar divide:
        """
        divide: Optional[Divide] = field(
            default=None,
            metadata={
                "name": "Divide",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class CalculatorSoapDivideOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapDivideOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar divide_response:
        :ivar fault:
        """
        divide_response: Optional[DivideResponse] = field(
            default=None,
            metadata={
                "name": "DivideResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["CalculatorSoapDivideOutput.Body.Fault"] = field(
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
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class CalculatorSoapMultiplyInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapMultiplyInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar multiply:
        """
        multiply: Optional[Multiply] = field(
            default=None,
            metadata={
                "name": "Multiply",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class CalculatorSoapMultiplyOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapMultiplyOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar multiply_response:
        :ivar fault:
        """
        multiply_response: Optional[MultiplyResponse] = field(
            default=None,
            metadata={
                "name": "MultiplyResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["CalculatorSoapMultiplyOutput.Body.Fault"] = field(
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
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class CalculatorSoapSubtractInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapSubtractInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar subtract:
        """
        subtract: Optional[Subtract] = field(
            default=None,
            metadata={
                "name": "Subtract",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class CalculatorSoapSubtractOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["CalculatorSoapSubtractOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        """
        :ivar subtract_response:
        :ivar fault:
        """
        subtract_response: Optional[SubtractResponse] = field(
            default=None,
            metadata={
                "name": "SubtractResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["CalculatorSoapSubtractOutput.Body.Fault"] = field(
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
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
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
