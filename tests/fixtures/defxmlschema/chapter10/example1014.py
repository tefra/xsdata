from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ApplicableSizesType:
    """
    :ivar value:
    :ivar small_medium_large:
    :ivar value_2_4_6_8_10_12_14_16_18:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="List",
            required=True
        )
    )
    small_medium_large: str = field(
        default="small medium large",
        metadata=dict(
            name="small medium large",
            type="Enumeration",
            required=True
        )
    )
    value_2_4_6_8_10_12_14_16_18: str = field(
        default="2 4 6 8 10 12 14 16 18",
        metadata=dict(
            name="2 4 6 8 10 12 14 16 18",
            type="Enumeration",
            required=True
        )
    )
