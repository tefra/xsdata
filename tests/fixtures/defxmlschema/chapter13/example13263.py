from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter13.example13261 import (
    BaseType,
)


@dataclass
class IlegalDerivedType(BaseType):
    """
    :ivar elements:
    :ivar a:
    """
    elements: Optional[object] = field(
        default=None,
        metadata=dict(
            name="elements",
            type="Any",
            required=True
        )
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Element",
            namespace=""
        )
    )
