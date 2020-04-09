from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Description:
    """
    :ivar value:
    """
    class Meta:
        name = "description"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
