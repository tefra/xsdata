from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.defxmlschema.chapter15.example1515 import (
    CatalogType,
)

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class CatalogListType:
    """
    :ivar catalog:
    """
    catalog: List[CatalogType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class RestrictedCatalogListType:
    """
    :ivar catalog:
    """
    catalog: Optional[CatalogType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
