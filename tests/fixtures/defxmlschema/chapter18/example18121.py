from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionGroup:
    """
    :ivar description:
    :ivar comment:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            namespace="",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element",
            namespace=""
        )
    )


@dataclass
class IdentifierGroup:
    """
    :ivar id:
    :ivar version:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
