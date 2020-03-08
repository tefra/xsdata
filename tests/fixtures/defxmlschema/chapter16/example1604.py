from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Number:
    class Meta:
        name = "number"



@dataclass
class ProductId:
    """
    :ivar value:
    """
    class Meta:
        name = "productID"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True
        )
    )


@dataclass
class SkuNumber:
    """
    :ivar value:
    """
    class Meta:
        name = "skuNumber"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True
        )
    )
