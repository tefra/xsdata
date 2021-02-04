from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "urn:docs"


@dataclass
class DoubleQuotesDescription:
    """Let's trip.

    Dont trip on quotes: "A", "B", "C", "D"
    """
    class Meta:
        namespace = "urn:docs"


@dataclass
class DoubleQuotesSummary:
    """
    Dont trip on quotes: "A", "B", "C", "D".
    """
    class Meta:
        namespace = "urn:docs"


class RootEnum(Enum):
    """
    Attributes
        A: Lorem ipsum dolor
        B: Lorem ipsum dolor '''sit''' amet, consectetur adipiscing
            elit. Morbi dapibus.
    """
    A = "A"
    B = "B"


class RootB(Enum):
    """
    Attributes
        YES: This is an inner enum member documentation. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit. Etiam mollis.
        NO: Lorem ipsum dolor
    """
    YES = "Yes"
    NO = "No"


class RootD(Enum):
    TRUE_VALUE = "true"
    FALSE_VALUE = "false"


@dataclass
class Root:
    """This is the root type documentation. '''Lorem ipsum''' dolor sit amet,
    consectetur adipiscing elit. Morbi dapibus.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
    imperdiet lacus sed sagittis scelerisque. Ut sodales metus: "sit",
    "amet", "lectus"

    Attributes
        a: This is an inner type '''field''' documentation. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit. Aliquam nec.
        b: This is a second root type field documentation.
        c:
        d:
    """
    class Meta:
        namespace = "urn:docs"

    a: Optional["Root.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[RootB] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: Optional[RootEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d: Optional[RootD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class A:
        """
        This is an inner type documentation.

        Attributes
            sub_a: This is an inner type '''field''' documentation.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Vivamus efficitur.
        """
        sub_a: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
