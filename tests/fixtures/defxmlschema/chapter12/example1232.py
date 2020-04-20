from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar id:
    :ivar version:
    :ivar eff_date:
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
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
