from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TextType:
    """
    :ivar elements:
    :ivar lang:
    """
    class Meta:
        mixed = True

    elements: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="elements",
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
