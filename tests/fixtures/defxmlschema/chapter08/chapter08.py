from enum import Enum
from dataclasses import dataclass, field
from typing import List, Union


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
class SizesType:
    """
    :ivar dress_size:
    :ivar medium_dress_size:
    :ivar small_dress_size:
    :ivar smlx_size:
    :ivar xsmlx_size:
    """
    dress_size: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dressSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0,
            pattern=r"\d{1,2}"
        )
    )
    medium_dress_size: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="mediumDressSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=8.0,
            max_inclusive=12.0,
            pattern=r"\d{1,2}"
        )
    )
    small_dress_size: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="smallDressSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=6.0,
            pattern=r"\d{1}"
        )
    )
    smlx_size: List[SmlxsizeType] = field(
        default_factory=list,
        metadata=dict(
            name="smlxSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    xsmlx_size: List[Union[SmlxsizeType, "SizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            name="xsmlxSize",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    class Value(Enum):
        """
        :cvar EXTRA_SMALL:
        """
        EXTRA_SMALL = "extra small"


@dataclass
class Sizes(SizesType):
    class Meta:
        name = "sizes"
