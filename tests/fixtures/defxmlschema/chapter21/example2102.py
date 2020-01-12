from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Name:
    """
    :ivar value:
    """
    class Meta:
        name = "name"
        namespace = "http://datypic.com/prod"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class Number:
    """
    :ivar value:
    """
    class Meta:
        name = "number"
        namespace = "http://datypic.com/prod"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class Size:
    """
    :ivar value:
    """
    class Meta:
        name = "size"
        namespace = "http://datypic.com/prod"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_inclusive=2.0,
            max_inclusive=18.0
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
    class Meta:
        name = "product"
        namespace = "http://datypic.com/prod"

    number: Optional[Number] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            required=True
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
class Catalog:
    """
    :ivar product:
    """
    class Meta:
        name = "catalog"
        namespace = "http://datypic.com/prod"

    product: List[Product] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
