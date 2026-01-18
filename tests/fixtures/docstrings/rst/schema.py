from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "urn:docs"


@dataclass
class DoubleQuotesDescription:
    """
    Let's trip.

    Dont trip on quotes: "A", "B", "C", "D" My\\Ipsum.
    """

    class Meta:
        namespace = "urn:docs"


@dataclass
class DoubleQuotesSummary:
    """
    Dont trip on quotes: "A", "B", "C", "D" My\\Ipsum.
    """

    class Meta:
        namespace = "urn:docs"


class RootEnum(Enum):
    """
    :cvar A: Lorem ipsum dolor
    :cvar B: Lorem ipsum dolor '''sit''' amet, consectetur adipiscing
        elit. Morbi dapibus. My\\Ipsum
    """

    A = "A"
    B = "B"


class RootB(Enum):
    """
    :cvar YES: This is an inner enum member documentation. Lorem ipsum
        dolor sit amet, consectetur adipiscing elit. Etiam mollis.
    :cvar NO: Lorem ipsum dolor My\\Ipsum
    """

    YES = "Yes"
    NO = "No"


class RootD(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass
class Root:
    """
    This is the root type documentation. '''Lorem ipsum''' dolor sit amet,
    consectetur adipiscing elit.

    Morbi dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Donec imperdiet lacus sed sagittis scelerisque. Ut sodales metus:
    "sit", "amet", "lectus" My\\Ipsum.

    :ivar a: This is an inner type '''field''' documentation. Lorem
        ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec.
        My\\Ipsum
    :ivar b: This is a second root type field documentation.
    :ivar c:
    :ivar d:
    """

    class Meta:
        namespace = "urn:docs"

    a: None | Root.A = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    b: None | RootB = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c: None | RootEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    d: None | RootD = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class A:
        """
        This is an inner type documentation.

        :ivar sub_a: This is an inner type '''field''' documentation.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus efficitur. My\\Ipsum
        """

        sub_a: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
