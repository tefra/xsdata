from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter16.example1607 import (
    HatType,
    ShirtType,
    UmbrellaType,
)


@dataclass
class ItemsType:
    """
    :ivar shirt:
    :ivar umbrella:
    :ivar hat:
    """
    shirt: Optional[ShirtType] = field(
        default=None,
        metadata=dict(
            name="shirt",
            type="Element"
        )
    )
    umbrella: Optional[UmbrellaType] = field(
        default=None,
        metadata=dict(
            name="umbrella",
            type="Element"
        )
    )
    hat: Optional[HatType] = field(
        default=None,
        metadata=dict(
            name="hat",
            type="Element"
        )
    )
