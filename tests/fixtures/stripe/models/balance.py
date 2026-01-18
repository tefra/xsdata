from dataclasses import dataclass, field
from typing import Optional


@dataclass(order=True, frozen=True)
class ConnectReserved:
    class Meta:
        name = "connect_reserved"

    amount: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass(order=True, frozen=True)
class SourceTypes:
    class Meta:
        name = "source_types"

    bank_account: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    card: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass(order=True, frozen=True)
class Available:
    class Meta:
        name = "available"

    amount: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source_types: SourceTypes | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass(order=True, frozen=True)
class Pending:
    class Meta:
        name = "pending"

    amount: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source_types: SourceTypes | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass(order=True, frozen=True)
class Balance:
    class Meta:
        name = "balance"

    object_value: str | None = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    available: tuple[Available, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    connect_reserved: tuple[ConnectReserved, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    livemode: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pending: tuple[Pending, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
