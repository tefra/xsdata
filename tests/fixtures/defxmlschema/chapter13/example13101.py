from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ItemType:
    """
    :ivar id:
    :ivar lang:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )


@dataclass
class ProductType(ItemType):
    """
    :ivar eff_date:
    :ivar lang:
    """
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
