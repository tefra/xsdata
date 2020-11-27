from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.org/ord"


@dataclass
class CustomerType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
