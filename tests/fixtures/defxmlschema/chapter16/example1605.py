from dataclasses import dataclass
from tests.fixtures.defxmlschema.chapter16.example1607 import (
    HatType,
    ShirtType,
    UmbrellaType,
)
from tests.fixtures.defxmlschema.chapter22.example2207 import (
    ProductType,
)


@dataclass
class DiscontinuedProduct(ProductType):
    class Meta:
        name = "discontinuedProduct"


@dataclass
class Hat(HatType):
    class Meta:
        name = "hat"


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"


@dataclass
class Umbrella(UmbrellaType):
    class Meta:
        name = "umbrella"
