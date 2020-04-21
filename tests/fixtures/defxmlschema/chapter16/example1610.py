from dataclasses import dataclass
from tests.fixtures.defxmlschema.chapter16.example1607 import (
    HatType,
)
from tests.fixtures.defxmlschema.chapter22.example2207 import (
    ProductType,
)


@dataclass
class Hat(HatType):
    class Meta:
        name = "hat"


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
