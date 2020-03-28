from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionGroup:
    """
    :ivar description:
    :ivar comment:
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
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element",
            namespace=""
        )
    )
