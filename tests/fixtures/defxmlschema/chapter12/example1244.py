from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar local_element:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##local",
            required=True
        )
    )


@dataclass
class Something:
    """
    :ivar value:
    """
    class Meta:
        name = "something"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True
        )
    )


@dataclass
class CatalogType:
    """
    :ivar product:
    :ivar local_element:
    """
    product: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##local",
            required=True
        )
    )


@dataclass
class Catalog(CatalogType):
    class Meta:
        name = "catalog"
