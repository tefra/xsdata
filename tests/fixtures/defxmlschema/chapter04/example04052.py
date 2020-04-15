from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class OrderSummary:
    """
    :ivar any_element:
    """
    class Meta:
        name = "orderSummary"
        namespace = "http://datypic.com/ord"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
