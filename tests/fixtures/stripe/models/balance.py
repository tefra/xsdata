from dataclasses import dataclass, field
from typing import Optional, Tuple


@dataclass(order=True, frozen=True)
class ConnectReserved:
    class Meta:
        name = "connect_reserved"

    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True, frozen=True)
class SourceTypes:
    class Meta:
        name = "source_types"

    bank_account: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True, frozen=True)
class Available:
    class Meta:
        name = "available"

    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    source_types: Optional[SourceTypes] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True, frozen=True)
class Pending:
    class Meta:
        name = "pending"

    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    source_types: Optional[SourceTypes] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(order=True, frozen=True)
class Balance:
    class Meta:
        name = "balance"

    object_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    available: Tuple[Available, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
        }
    )
    connect_reserved: Tuple[ConnectReserved, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
        }
    )
    livemode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pending: Tuple[Pending, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
        }
    )
