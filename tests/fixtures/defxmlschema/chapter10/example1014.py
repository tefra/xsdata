from enum import Enum
from dataclasses import dataclass, field
from typing import List, Union
from tests.fixtures.defxmlschema.chapter08.example0810 import (
    SmlsizeType,
)


@dataclass
class ApplicableSizesType:
    """
    :ivar value:
    """
    value: List[Union[int, SmlsizeType, "ApplicableSizesType.Value"]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )

    class Value(Enum):
        """
        :cvar SMALL_MEDIUM_LARGE:
        :cvar VALUE_2_4_6_8_10_12_14_16_18:
        """
        SMALL_MEDIUM_LARGE = "small medium large"
        VALUE_2_4_6_8_10_12_14_16_18 = "2 4 6 8 10 12 14 16 18"
