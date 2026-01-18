from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "xsdata"


@dataclass(kw_only=True)
class Alphas:
    class Meta:
        name = "alphas"
        namespace = "xsdata"

    alpha: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
    lang: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Wrapper:
    class Meta:
        name = "wrapper"
        namespace = "xsdata"

    alpha: str = field(
        metadata={
            "wrapper": "alphas",
            "type": "Element",
            "required": True,
        }
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
