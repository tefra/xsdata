from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar description:
    :ivar comment:
    :ivar number:
    :ivar name:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element"
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
