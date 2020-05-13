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
            required=True
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
            required=True
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
            required=True
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
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )

    class Value(Enum):
        """
        :cvar SMALL:
        :cvar MEDIUM:
        :cvar LARGE:
        """
        SMALL = "small"
        MEDIUM = "medium"
        LARGE = "large"


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
            type="Element",
            required=True
        )
    )
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    color: Optional[Color] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
