from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter02.example0210 import (
    ProductType,
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
