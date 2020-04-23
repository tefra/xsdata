from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "http://www.w3.org/XML/1998/namespace"


@dataclass
class Base:
    """
    :ivar value:
    """
    class Meta:
        name = "base"
        namespace = "http://www.w3.org/XML/1998/namespace"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Id:
    """
    :ivar value:
    """
    class Meta:
        name = "id"
        namespace = "http://www.w3.org/XML/1998/namespace"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Lang:
    """
    :ivar value:
    """
    class Meta:
        name = "lang"
        namespace = "http://www.w3.org/XML/1998/namespace"

    value: Optional[Union[str, "Lang.Value"]] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE:
        """
        VALUE = ""


@dataclass
class Space:
    """
    :ivar value:
    """
    class Meta:
        name = "space"
        namespace = "http://www.w3.org/XML/1998/namespace"

    value: Optional["Space.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar DEFAULT:
        :cvar PRESERVE:
        """
        DEFAULT = "default"
        PRESERVE = "preserve"


@dataclass
class SpecialAttrs:
    """
    :ivar base:
    :ivar lang:
    :ivar space:
    :ivar id:
    """
    class Meta:
        name = "specialAttrs"

    base: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    space: Optional["SpecialAttrs.Value"] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )

    class Value(Enum):
        """
        :cvar DEFAULT:
        :cvar PRESERVE:
        """
        DEFAULT = "default"
        PRESERVE = "preserve"
