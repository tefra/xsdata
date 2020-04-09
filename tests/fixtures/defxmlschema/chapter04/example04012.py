from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderNumType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://datypic.com/ord"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
