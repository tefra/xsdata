from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Size:
    """
    :ivar value:
    """
    value: Optional[Union[int, "Size.Value"]] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union",
            min_inclusive=2.0,
            max_inclusive=18.0,
            pattern=r"\d{1,2}"
        )
    )

    class Value(Enum):
        """
        :cvar LARGE:
        :cvar MEDIUM:
        :cvar SMALL:
        """
        LARGE = "large"
        MEDIUM = "medium"
        SMALL = "small"
