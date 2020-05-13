from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class InternationalSizeType:
    """
    :ivar value:
    """
    value: Optional[Union[int, "InternationalSizeType.Value"]] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=24.0,
            max_inclusive=54.0
        )
    )

    class Value(Enum):
        """
        :cvar SMALL:
        :cvar MEDIUM:
        :cvar LARGE:
        """
        SMALL = "small"
        MEDIUM = "medium"
        LARGE = "large"
