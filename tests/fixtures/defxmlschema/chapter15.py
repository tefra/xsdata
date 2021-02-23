from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class SizeType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ShirtType:
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
    eff_date: Optional[XmlDate] = field(
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
