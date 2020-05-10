from dataclasses import dataclass, field
from typing import List
from tests.fixtures.defxmlschema.chapter08.example0810 import (
    SmlsizeType,
)


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    """
    value: List[SmlsizeType] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
