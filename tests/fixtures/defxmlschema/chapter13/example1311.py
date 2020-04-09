from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class BaseType:
    """
    :ivar datypic_com_prod_attributes:
    """
    datypic_com_prod_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://datypic.com/prod"
        )
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar www_w3_org_1999_xhtml_attributes:
    """
    www_w3_org_1999_xhtml_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##targetNamespace http://www.w3.org/1999/xhtml"
        )
    )
