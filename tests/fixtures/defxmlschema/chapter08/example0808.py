from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class DressSize:
    """
    :ivar value:
    """
    value: Optional[Union[int, "DressSize.Value"]] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union",
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )

    class Value(Enum):
        """
        :cvar VALUE:
        """
        VALUE = ""
