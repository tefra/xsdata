from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "urn:docs"


@dataclass(kw_only=True)
class DoubleQuotesDescription:
    """
    Let's trip.

    Dont trip on quotes: "A", "B", "C", "D" My\\Ipsum.
    """

    class Meta:
        namespace = "urn:docs"


@dataclass(kw_only=True)
class DoubleQuotesSummary:
    """
    Dont trip on quotes: "A", "B", "C", "D" My\\Ipsum.
    """

    class Meta:
        namespace = "urn:docs"


class RootEnum(Enum):
    A = "A"
    B = "B"


RootEnum.A.__doc__ = "Lorem ipsum dolor"
RootEnum.B.__doc__ = (
    "Lorem ipsum dolor '''sit''' amet, consectetur adipiscing elit. Morbi "
    "dapibus. My\\Ipsum"
)


class RootB(Enum):
    YES = "Yes"
    NO = "No"


RootB.YES.__doc__ = (
    "This is an inner enum member documentation. Lorem ipsum dolor sit amet, "
    "consectetur adipiscing elit. Etiam mollis."
)
RootB.NO.__doc__ = "Lorem ipsum dolor\nMy\\Ipsum"


class RootD(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass(kw_only=True)
class Root:
    """
    This is the root type documentation. '''Lorem ipsum''' dolor sit amet,
    consectetur adipiscing elit.

    Morbi dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Donec imperdiet lacus sed sagittis scelerisque. Ut sodales metus:
    "sit", "amet", "lectus" My\\Ipsum.
    """

    class Meta:
        namespace = "urn:docs"

    a: Root.A = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "doc": (
                "This is an inner type '''field''' documentation.\nLorem ipsum"
                " dolor sit amet, consectetur adipiscing elit. Aliquam "
                "nec.\nMy\\Ipsum"
            ),
        }
    )
    b: RootB = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "doc": "This is a second root type field documentation.",
        }
    )
    c: RootEnum = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d: RootD = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class A:
        """
        This is an inner type documentation.
        """

        sub_a: str = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "doc": (
                    "This is an inner type '''field''' documentation.\nLorem ipsum"
                    " dolor sit amet, consectetur adipiscing elit. Vivamus "
                    "efficitur.\nMy\\Ipsum"
                ),
            }
        )
