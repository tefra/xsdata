from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class ProductType:
    """
    :ivar other_attributes:
    """
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
