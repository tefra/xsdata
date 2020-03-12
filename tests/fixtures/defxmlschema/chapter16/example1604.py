from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Number:
    """
    :ivar any_element:
    """
    class Meta:
        name = "number"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


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
