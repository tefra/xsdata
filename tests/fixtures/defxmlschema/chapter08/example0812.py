from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union
from tests.fixtures.defxmlschema.chapter08.example0809 import (
    SmlxsizeType,
)


@dataclass
class XsmlxsizeType:
    """
    :ivar value:
    """
    class Meta:
        name = "XSMLXSizeType"

    value: Optional[Union[SmlxsizeType, "XsmlxsizeType.Value"]] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar EXTRA_SMALL:
        """
        EXTRA_SMALL = "extra small"
