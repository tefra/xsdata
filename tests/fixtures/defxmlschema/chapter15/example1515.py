from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


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
            name="id",
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute"
        )
    )
