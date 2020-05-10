from enum import Enum
from dataclasses import dataclass, field
from typing import List


class SmlxsizeType(Enum):
    """
    :cvar EXTRA_LARGE:
    :cvar LARGE:
    :cvar MEDIUM:
    :cvar SMALL:
    """
    EXTRA_LARGE = "extra large"
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    """
    value: List[SmlxsizeType] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
