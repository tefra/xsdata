from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar version:
    :ivar id:
    :ivar version:
    """
    version: Optional[float] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
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
