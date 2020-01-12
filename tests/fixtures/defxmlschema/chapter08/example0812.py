from dataclasses import dataclass, field
from typing import Optional


@dataclass
class XsmlxsizeType:
    """
    :ivar value:
    """
    class Meta:
        name = "XSMLXSizeType"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union"
        )
    )
