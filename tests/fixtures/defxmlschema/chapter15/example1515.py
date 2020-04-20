from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class CatalogType:
    """
    :ivar catalog_number:
    """
    catalog_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="catalogNumber",
            type="Attribute"
        )
    )


@dataclass
class ProductType:
    """
    :ivar id:
    :ivar version:
    :ivar dept:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
