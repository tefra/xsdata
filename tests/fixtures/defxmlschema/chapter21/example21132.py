from dataclasses import dataclass, field
from typing import List, Optional


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
    product: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
