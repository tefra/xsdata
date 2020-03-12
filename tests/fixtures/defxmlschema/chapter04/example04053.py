from dataclasses import dataclass, field
from typing import List


@dataclass
class OrderDetails:
    """
    :ivar any_element:
    """
    class Meta:
        name = "orderDetails"
        namespace = "http://datypic.com/ord"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
