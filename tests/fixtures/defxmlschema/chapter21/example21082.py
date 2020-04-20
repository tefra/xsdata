from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://datypic.com/all"


@dataclass
class ProductType:
    """
    :ivar number:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/all",
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
            type="Element",
            namespace="http://datypic.com/all",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
