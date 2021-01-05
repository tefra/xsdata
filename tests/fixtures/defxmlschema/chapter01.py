from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


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
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 18,
        }
    )
    eff_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "effDate",
            "type": "Attribute",
        }
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
