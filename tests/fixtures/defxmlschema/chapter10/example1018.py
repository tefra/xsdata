from dataclasses import dataclass, field
from typing import List, Union
from tests.fixtures.defxmlschema.chapter08.example0809 import (
    SmlxsizeType,
)


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    """
    value: List[Union[int, SmlxsizeType]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
