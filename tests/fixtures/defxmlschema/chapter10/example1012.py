from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    :ivar small:
    :ivar medium:
    :ivar large:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
    small: str = field(
        default="small",
        metadata=dict(
            required=True
        )
    )
    medium: str = field(
        default="medium",
        metadata=dict(
            required=True
        )
    )
    large: str = field(
        default="large",
        metadata=dict(
            required=True
        )
    )
