from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar number:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )


@dataclass
class ItemsType:
    """
    :ivar product:
    """
    product: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            name="product",
            type="Element",
            required=True
        )
    )
