from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


class ApplicableSizesType(Enum):
    SMALL_MEDIUM_LARGE = "small medium large"
    VALUE_2_4_6_8_10_12_14_16_18 = "2 4 6 8 10 12 14 16 18"


class SizeTypeValue(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class SmallSizeType(Enum):
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_6 = 6
    SMALL = "small"


@dataclass
class SizesType:
    size: List[Union[int, SizeTypeValue]] = field(
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
    international_size: List[Union[int, SizeTypeValue]] = field(
        default_factory=list,
        metadata={
            "name": "internationalSize",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 24,
            "max_inclusive": 54,
        }
    )
    available_sizes: List[List[Union[int, SizeTypeValue]]] = field(
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


@dataclass
class Sizes(SizesType):
    class Meta:
        name = "sizes"
