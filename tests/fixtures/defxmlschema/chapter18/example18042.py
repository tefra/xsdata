from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionGroup:
    """
    :ivar description:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            namespace="",
            required=True
        )
    )
