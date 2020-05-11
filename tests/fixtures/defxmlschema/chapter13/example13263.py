from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IlegalDerivedType:
    """
    :ivar any_element:
    :ivar a:
    :ivar datypic_com_prod_http_datypic_com_ord_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    datypic_com_prod_http_datypic_com_ord_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://datypic.com/prod http://datypic.com/ord",
            required=True
        )
    )
