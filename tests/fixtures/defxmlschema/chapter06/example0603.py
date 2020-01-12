from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar name:
    :ivar size:
    """
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element"
        )
    )
