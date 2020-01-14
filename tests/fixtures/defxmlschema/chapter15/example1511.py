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
            name="id",
            type="Attribute",
            required=True
        )
    )
    version: Optional[float] = field(
        default=None,
        metadata=dict(
            name="version",
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
