from dataclasses import dataclass, field
from typing import List
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
    shirt: List[ShirtType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    umbrella: List[UmbrellaType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hat: List[HatType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
