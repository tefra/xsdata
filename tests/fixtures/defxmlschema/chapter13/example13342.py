from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter13.example13341 import (
    Name,
    Number,
    Size,
)

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class RestrictedProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar dept:
    """
    number: Optional[Number] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
