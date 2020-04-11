from dataclasses import dataclass, field
from typing import List, Union
from tests.fixtures.defxmlschema.chapter08.example0810 import (
    SmlsizeType,
)


@dataclass
class ApplicableSizesType:
    """
    :ivar value:
    :ivar small_medium_large:
    :ivar value_2_4_6_8_10_12_14_16_18:
    """
    value: List[Union[int, SmlsizeType]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    small_medium_large: str = field(
        default="small medium large",
        metadata=dict(
            required=True
        )
    )
    value_2_4_6_8_10_12_14_16_18: str = field(
        default="2 4 6 8 10 12 14 16 18",
        metadata=dict(
            required=True
        )
    )
