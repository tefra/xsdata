from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LetterType:
    """
    :ivar cust_name:
    :ivar prod_name:
    :ivar prod_size:
    """
    cust_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="custName",
            type="Element"
        )
    )
    prod_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="prodName",
            type="Element"
        )
    )
    prod_size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="prodSize",
            type="Element"
        )
    )


@dataclass
class RestrictedLetterType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction"
        )
    )
