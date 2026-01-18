from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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

    a: None | Root.A = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    b: None | RootB = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c: None | RootEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    d: None | RootD = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class A:
        sub_a: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
