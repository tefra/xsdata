from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ItemType:
    """
    :ivar routing_num:
    """
    routing_num: Optional[int] = field(
        default=None,
        metadata=dict(
            name="routingNum",
            type="Attribute"
        )
    )


@dataclass
class ProductType(ItemType):
    """
    :ivar number:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
