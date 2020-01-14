from dataclasses import dataclass, field
from typing import List


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    :ivar small:
    :ivar medium:
    :ivar large:
    """
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="List",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    small: str = field(
        default="small",
        metadata=dict(
            name="small",
            type="Enumeration"
        )
    )
    medium: str = field(
        default="medium",
        metadata=dict(
            name="medium",
            type="Enumeration"
        )
    )
    large: str = field(
        default="large",
        metadata=dict(
            name="large",
            type="Enumeration"
        )
    )
