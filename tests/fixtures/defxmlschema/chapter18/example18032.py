from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType(ProductType):
    """
    :ivar color:
    :ivar eff_date:
    """
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            required=True
        )
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
