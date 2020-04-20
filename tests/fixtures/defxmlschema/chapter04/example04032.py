from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter02.example0210 import (
    ProductType,
)

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class ItemsType:
    """
    :ivar product:
    """
    product: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
