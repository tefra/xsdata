from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter13.example13261 import (
    BaseType,
)


@dataclass
class LegalDerivedType(BaseType):
    """
    :ivar a:
    :ivar datypic_com_prod_element:
    """
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Element",
            namespace=""
        )
    )
    datypic_com_prod_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
