from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "urn:docs"


@dataclass(kw_only=True)
class DoubleQuotesDescription:
    class Meta:
        namespace = "urn:docs"


@dataclass(kw_only=True)
class DoubleQuotesSummary:
    class Meta:
        namespace = "urn:docs"


class RootEnum(StrEnum):
    A = "A"
    B = "B"


class RootB(StrEnum):
    YES = "Yes"
    NO = "No"


class RootD(StrEnum):
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
        }
    )
    b: RootB = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: RootEnum = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    d: RootD = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class A:
        sub_a: str = field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
