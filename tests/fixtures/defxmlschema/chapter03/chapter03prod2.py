from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Attribute",
            namespace="http://example.org/prod2"
        )
    )


@dataclass
class Color(ColorType):
    class Meta:
        name = "color"
        namespace = "http://example.org/prod2"
