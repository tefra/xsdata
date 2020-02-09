from dataclasses import dataclass
from tests.fixtures.defxmlschema.chapter01.example0102 import (
    ProductType,
)


@dataclass
class Product(ProductType):
    """<ns0:description>This element represents a product.</ns0:description>"""
    class Meta:
        name = "product"
