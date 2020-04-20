from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Picture:
    """
    :ivar location:
    """
    class Meta:
        name = "picture"

    location: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
