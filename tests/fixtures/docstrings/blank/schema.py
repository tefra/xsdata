from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "urn:docs"


@dataclass
class DoubleQuotesDescription:
    class Meta:
        namespace = "urn:docs"


@dataclass
class DoubleQuotesSummary:
    class Meta:
        namespace = "urn:docs"


class RootEnum(Enum):
    A = "A"
    B = "B"


class RootB(Enum):
    YES = "Yes"
    NO = "No"


class RootD(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass
class Root:
    class Meta:
        namespace = "urn:docs"

    a: Optional["Root.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[RootB] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: Optional[RootEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d: Optional[RootD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class A:
        sub_a: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
