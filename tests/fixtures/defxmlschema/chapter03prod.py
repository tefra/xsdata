from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter03prod2 import Color

__NAMESPACE__ = "http://example.org/prod"


@dataclass
class ProdNumType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://example.org/prod",
            "required": True,
        }
    )


@dataclass
class SizeType:
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
class ProductType:
    number: Optional[ProdNumType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/prod",
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
    size: Optional[SizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/prod",
            "required": True,
        }
    )
    color: Optional[Color] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/prod2",
            "required": True,
        }
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
        namespace = "http://example.org/prod"
