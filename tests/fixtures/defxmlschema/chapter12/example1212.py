from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Color:
    """
    :ivar value:
    """
    class Meta:
        name = "color"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


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

    value: Optional[Union[int, "Size.Value"]] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union",
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )

    class Value(Enum):
        """
        :cvar LARGE:
        :cvar MEDIUM:
        :cvar SMALL:
        """
        LARGE = "large"
        MEDIUM = "medium"
        SMALL = "small"


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar color:
    """
    number: Optional[Number] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace=""
        )
    )
    color: Optional[Color] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace=""
        )
    )
