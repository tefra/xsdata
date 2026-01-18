from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "urn:docs"


@dataclass(kw_only=True)
class DoubleQuotesDescription:
    class Meta:
        namespace = "urn:docs"


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Root:
    class Meta:
        namespace = "urn:docs"

    a: Root.A = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: RootB = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: RootEnum = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d: RootD = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class A:
        sub_a: str = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
