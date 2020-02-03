from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LetterType:
    """
    :ivar cust_name:
    :ivar prod_name:
    :ivar prod_size:
    """
    class Meta:
        mixed = True

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
class RestrictedLetterType(LetterType):
    """
    :ivar cust_name:
    :ivar prod_name:
    """
    class Meta:
        mixed = True

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
