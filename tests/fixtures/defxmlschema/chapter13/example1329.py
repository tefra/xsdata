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
class RestrictedItemType:
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
