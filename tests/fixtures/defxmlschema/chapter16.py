from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ColorType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HatSizeType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProductType:
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ShirtSizeType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Umbrella:
    class Meta:
        name = "umbrella"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class ShirtType(ProductType):
    size: Optional[ShirtSizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Hat(ProductType):
    class Meta:
        name = "hat"

    size: Optional[HatSizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"


@dataclass
class ItemsType:
    umbrella: List[Umbrella] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    hat: List[Hat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    shirt: List[Shirt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
