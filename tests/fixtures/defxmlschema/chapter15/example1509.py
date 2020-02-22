from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


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
