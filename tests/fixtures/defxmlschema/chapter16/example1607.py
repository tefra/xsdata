from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter22.example2207 import (
    ProductType,
)


@dataclass
class HatType(ProductType):
    """
    :ivar size:
    """
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            required=True
        )
    )


@dataclass
class ShirtType(ProductType):
    """
    :ivar size:
    :ivar color:
    """
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            required=True
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            required=True
        )
    )


@dataclass
class UmbrellaType(ProductType):
    pass
