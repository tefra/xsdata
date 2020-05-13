from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar color:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    size: Optional[Union[int, "ProductType.Value"]] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
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
