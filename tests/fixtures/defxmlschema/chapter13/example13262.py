from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LegalDerivedType:
    """
    :ivar a:
    :ivar datypic_com_ord_element:
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
    datypic_com_ord_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="http://datypic.com/prod http://datypic.com/ord",
            required=True
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
