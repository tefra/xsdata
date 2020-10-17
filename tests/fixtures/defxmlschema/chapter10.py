from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


class ApplicableSizesType(Enum):
    """
    :cvar SMALL_MEDIUM_LARGE:
    :cvar VALUE_2_4_6_8_10_12_14_16_18:
    """
    SMALL_MEDIUM_LARGE = "small medium large"
    VALUE_2_4_6_8_10_12_14_16_18 = "2 4 6 8 10 12 14 16 18"


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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 2,
            "max_inclusive": 18,
        }
    )
    small_size: List[SmallSizeType] = field(
        default_factory=list,
        metadata={
            "name": "smallSize",
            "type": "Element",
            "namespace": "",
        }
    )
    international_size: List[Union[int, "SizesType.Value"]] = field(
        default_factory=list,
        metadata={
            "name": "internationalSize",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 24,
            "max_inclusive": 54,
        }
    )
    available_sizes: List[List[Union[int, "SizesType.Value"]]] = field(
        default_factory=list,
        metadata={
            "name": "availableSizes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 2,
            "max_inclusive": 18,
            "tokens": True,
        }
    )
    applicable_sizes: List[ApplicableSizesType] = field(
        default_factory=list,
        metadata={
            "name": "applicableSizes",
            "type": "Element",
            "namespace": "",
        }
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
