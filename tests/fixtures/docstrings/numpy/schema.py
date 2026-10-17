from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

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


class RootEnum(StrEnum):
    """
    Properties
    ----------
    A
        Lorem ipsum dolor
    B
        Lorem ipsum dolor '''sit''' amet, consectetur adipiscing elit. Morbi
        dapibus. My\\Ipsum
    """

    A = "A"
    B = "B"


class RootB(StrEnum):
    """
    Properties
    ----------
    YES
        This is an inner enum member documentation. Lorem ipsum dolor sit
        amet, consectetur adipiscing elit. Etiam mollis.
    NO
        Lorem ipsum dolor My\\Ipsum
    """

    YES = "Yes"
    NO = "No"


class RootD(StrEnum):
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

    Parameters
    ----------
    a
        This is an inner type '''field''' documentation. Lorem ipsum dolor
        sit amet, consectetur adipiscing elit. Aliquam nec. My\\Ipsum
    b
        This is a second root type field documentation.
    c
    d
    """

    class Meta:
        namespace = "urn:docs"

    a: Root.A = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: RootB = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: RootEnum = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    d: RootD = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class A:
        """
        This is an inner type documentation.

        Parameters
        ----------
        sub_a
            This is an inner type '''field''' documentation. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit. Vivamus efficitur.
            My\\Ipsum
        """

        sub_a: str = field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
