from dataclasses import dataclass, field
from typing import List


@dataclass
class OrderSummary:
    """
    :ivar any_element:
    """
    class Meta:
        name = "orderSummary"
        namespace = "http://datypic.com/ord"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
