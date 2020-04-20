from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar size:
    :ivar eff_date:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
        namespace = "http://datypic.com/prod"
