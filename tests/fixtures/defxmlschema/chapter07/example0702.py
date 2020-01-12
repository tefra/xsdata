from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SizeType:
    """
    :ivar system:
    :ivar dim:
    """
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute",
            required=True
        )
    )
    dim: Optional[int] = field(
        default=None,
        metadata=dict(
            name="dim",
            type="Attribute"
        )
    )
