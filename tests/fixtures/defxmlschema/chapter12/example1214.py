from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace=""
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace=""
        )
    )
