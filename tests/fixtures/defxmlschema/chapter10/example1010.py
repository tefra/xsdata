from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter08.example0810 import (
    SmlsizeType,
)


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    """
    value: Optional[SmlsizeType] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            max_length=3.0
        )
    )
