from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TextType:
    """
    :ivar lang:
    """
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute"
        )
    )
