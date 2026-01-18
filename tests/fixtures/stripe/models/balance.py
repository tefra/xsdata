from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class ConnectReserved:
    class Meta:
        name = "connect_reserved"

    amount: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: None | str = field(
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

    bank_account: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    card: None | int = field(
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

    amount: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source_types: None | SourceTypes = field(
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

    amount: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source_types: None | SourceTypes = field(
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

    object_value: None | str = field(
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
    livemode: None | bool = field(
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
