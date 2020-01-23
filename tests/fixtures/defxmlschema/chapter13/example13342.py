from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter13.example13341 import (
    ProductType,
    Name,
    Number,
)


@dataclass
class RestrictedProductType(ProductType):
    """
    :ivar number:
    :ivar name:
    :ivar dept:
    """
    number: Optional[Number] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
