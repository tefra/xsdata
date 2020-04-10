from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderDetails:
    """
    :ivar any_element:
    """
    class Meta:
        name = "orderDetails"
        namespace = "http://datypic.com/ord"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
