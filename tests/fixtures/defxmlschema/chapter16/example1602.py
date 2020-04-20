from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter16.chapter16 import (
    HatSizeType,
    ProductType,
    ShirtSizeType,
)


@dataclass
class Umbrella:
    """
    :ivar any_element:
    """
    class Meta:
        name = "umbrella"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class ShirtType(ProductType):
    """
    :ivar size:
    :ivar color:
    """
    size: Optional[ShirtSizeType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Hat(ProductType):
    """
    :ivar size:
    """
    class Meta:
        name = "hat"

    size: Optional[HatSizeType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"
