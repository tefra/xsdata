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
    :ivar dept:
    """
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute"
        )
    )
