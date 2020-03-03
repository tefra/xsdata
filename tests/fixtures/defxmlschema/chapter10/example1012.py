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
            name="value",
            type="List",
            required=True
        )
    )
    small: str = field(
        default="small",
        metadata=dict(
            name="small",
            type="Enumeration",
            required=True
        )
    )
    medium: str = field(
        default="medium",
        metadata=dict(
            name="medium",
            type="Enumeration",
            required=True
        )
    )
    large: str = field(
        default="large",
        metadata=dict(
            name="large",
            type="Enumeration",
            required=True
        )
    )
