from dataclasses import dataclass
from tests.fixtures.defxmlschema.chapter01.example0102 import (
    ProductType,
)


@dataclass
class Product(ProductType):
    """<doc:description>This element represents a product.</doc:description>"""
    class Meta:
        name = "product"
