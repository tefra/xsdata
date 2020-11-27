from dataclasses import dataclass, field
from enum import Enum
from typing import List


class SmlxsizeType(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra large"


class XsmlxsizeType(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra large"
    EXTRA_SMALL = "extra small"


@dataclass
class SizesType:
    dress_size: List[str] = field(
        default_factory=list,
        metadata={
            "name": "dressSize",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "2",
            "max_inclusive": "18",
            "pattern": r"\d{1,2}",
        }
    )
    medium_dress_size: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mediumDressSize",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "8",
            "max_inclusive": "12",
            "pattern": r"\d{1,2}",
        }
    )
    small_dress_size: List[str] = field(
        default_factory=list,
        metadata={
            "name": "smallDressSize",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "2",
            "max_inclusive": "6",
            "pattern": r"\d{1}",
        }
    )
    smlx_size: List[SmlxsizeType] = field(
        default_factory=list,
        metadata={
            "name": "smlxSize",
            "type": "Element",
            "namespace": "",
        }
    )
    xsmlx_size: List[XsmlxsizeType] = field(
        default_factory=list,
        metadata={
            "name": "xsmlxSize",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Sizes(SizesType):
    class Meta:
        name = "sizes"
