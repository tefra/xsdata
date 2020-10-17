from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class SizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ShirtType:
    """
    :ivar description:
    :ivar comment:
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar id:
    :ivar version:
    :ivar eff_date:
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    size: Optional[SizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "effDate",
            "type": "Attribute",
        }
    )


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"
