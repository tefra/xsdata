from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "xsdata"


@dataclass
class Alphas:
    class Meta:
        name = "alphas"
        namespace = "xsdata"

    alpha: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Bravos:
    class Meta:
        name = "bravos"
        namespace = "xsdata"

    bravo: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Charlie:
    class Meta:
        name = "charlie"
        namespace = "xsdata"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Charlies:
    class Meta:
        name = "charlies"
        namespace = "xsdata"

    charlie: list[Charlie] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Wrapper:
    class Meta:
        name = "wrapper"
        namespace = "xsdata"

    alpha: str | None = field(
        default=None,
        metadata={
            "wrapper": "alphas",
            "type": "Element",
            "required": True,
        },
    )
    bravo: list[int] = field(
        default_factory=list,
        metadata={
            "wrapper": "bravos",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    charlie: list[Charlie] = field(
        default_factory=list,
        metadata={
            "wrapper": "charlies",
            "type": "Element",
            "min_occurs": 1,
        },
    )
