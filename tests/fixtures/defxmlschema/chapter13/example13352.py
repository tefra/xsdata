from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter13.example13351 import (
    ProductType,
)


@dataclass
class RestrictedProductType(ProductType):
    """
    :ivar number:
    :ivar name:
    :ivar dept:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute",
            namespace="http://datypic.com/ord",
            required=True
        )
    )
