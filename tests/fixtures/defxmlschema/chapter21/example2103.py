from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar dept:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute"
        )
    )


@dataclass
class CatalogType:
    """
    :ivar product:
    """
    product: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            namespace="http://datypic.com/prod",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Catalog(CatalogType):
    class Meta:
        name = "catalog"
        namespace = "http://datypic.com/prod"
