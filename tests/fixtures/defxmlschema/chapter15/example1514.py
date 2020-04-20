from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class HeaderGroup:
    """
    :ivar id:
    :ivar version:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
