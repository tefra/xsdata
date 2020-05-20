from enum import Enum
from dataclasses import dataclass, field
from typing import List


class SmlxsizeType(Enum):
    """
    :cvar SMALL:
    :cvar MEDIUM:
    :cvar LARGE:
    :cvar EXTRA_LARGE:
    """
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra large"


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
