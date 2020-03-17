from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.defxmlschema.chapter15.example1515 import (
    CatalogType,
)


@dataclass
class CatalogListType:
    """
    :ivar catalog:
    """
    catalog: List[CatalogType] = field(
        default_factory=list,
        metadata=dict(
            name="catalog",
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
            name="catalog",
            type="Element",
            namespace="",
            required=True
        )
    )
