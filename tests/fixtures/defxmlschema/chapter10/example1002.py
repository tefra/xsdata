from dataclasses import dataclass, field
from typing import Optional, Union
from tests.fixtures.defxmlschema.chapter08.example0810 import (
    SmlsizeType,
)


@dataclass
class SizeType:
    """
    :ivar value:
    """
    value: Optional[Union[int, SmlsizeType]] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
