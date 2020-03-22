from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IlegalDerivedType:
    """
    :ivar any_element:
    :ivar datypic_com_prod_http_datypic_com_ord_element:
    :ivar a:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##any",
            required=True
        )
    )
    datypic_com_prod_http_datypic_com_ord_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="http://datypic.com/prod http://datypic.com/ord",
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
