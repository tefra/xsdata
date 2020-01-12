from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Name:
    """
    :ivar value:
    """
    class Meta:
        name = "name"

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

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
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
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
