from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pictures:
    """
    :ivar location:
    """
    class Meta:
        name = "pictures"

    location: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
