from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar size:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
        namespace = "http://datypic.com/prod"
