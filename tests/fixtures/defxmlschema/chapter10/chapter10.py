from enum import Enum
from dataclasses import dataclass, field
from typing import List, Union


class SmallSizeType(Enum):
    """
    :cvar VALUE_2:
    :cvar VALUE_4:
    :cvar VALUE_6:
    :cvar SMALL:
    """
    VALUE_2 = "2"
    VALUE_4 = "4"
    VALUE_6 = "6"
    SMALL = "small"


@dataclass
class SizesType:
    """
    :ivar size:
    :ivar small_size:
    :ivar international_size:
    :ivar available_sizes:
    :ivar applicable_sizes:
    """
    size: List[Union[int, "SizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    small_size: List[SmallSizeType] = field(
        default_factory=list,
        metadata=dict(
            name="smallSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    international_size: List[Union[int, "SizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            name="internationalSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=24.0,
            max_inclusive=54.0
        )
    )
    available_sizes: List[Union[int, "SizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            name="availableSizes",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    applicable_sizes: List[Union[int, "SizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            name="applicableSizes",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
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


@dataclass
class Sizes(SizesType):
    class Meta:
        name = "sizes"
