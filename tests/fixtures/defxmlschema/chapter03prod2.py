from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.org/prod2"


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://example.org/prod2",
        }
    )


@dataclass
class Color(ColorType):
    class Meta:
        name = "color"
        namespace = "http://example.org/prod2"
