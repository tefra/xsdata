from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.org/ord"


@dataclass
class CustomerType:
    """
    :ivar name:
    :ivar number:
    """
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
