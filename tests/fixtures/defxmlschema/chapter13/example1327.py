from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LetterType:
    """
    :ivar content:
    :ivar cust_name:
    :ivar prod_name:
    :ivar prod_size:
    """
    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    cust_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="custName",
            type="Element",
            namespace="",
            required=True
        )
    )
    prod_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="prodName",
            type="Element",
            namespace="",
            required=True
        )
    )
    prod_size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="prodSize",
            type="Element",
            namespace=""
        )
    )


@dataclass
class RestrictedLetterType:
    """
    :ivar content:
    :ivar cust_name:
    :ivar prod_name:
    :ivar prod_size:
    """
    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    cust_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="custName",
            type="Element",
            namespace="",
            required=True
        )
    )
    prod_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="prodName",
            type="Element",
            namespace="",
            required=True
        )
    )
    prod_size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="prodSize",
            type="Element",
            namespace=""
        )
    )
