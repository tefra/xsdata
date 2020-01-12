from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Product:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    """
    class Meta:
        name = "product"

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
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            required=True
        )
    )
