from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CustomerType:
    """
    :ivar name:
    """
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
