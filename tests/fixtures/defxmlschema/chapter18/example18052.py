from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionGroup:
    """
    :ivar notes:
    """
    notes: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notes",
            type="Element",
            namespace="",
            required=True
        )
    )
