from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/cust"


@dataclass
class CustomerType:
    """
    :ivar name:
    """
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/cust",
            required=True
        )
    )
