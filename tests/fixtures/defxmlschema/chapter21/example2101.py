from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Catalog:
    """
    :ivar product:
    """
    class Meta:
        name = "catalog"
        namespace = "http://datypic.com/prod"

    product: List["Catalog.Product"] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Product:
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
                required=True
            )
        )
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="name",
                type="Element",
                required=True
            )
        )
        size: Optional[int] = field(
            default=None,
            metadata=dict(
                name="size",
                type="Element",
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
