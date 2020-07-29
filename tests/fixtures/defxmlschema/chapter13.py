from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ItemType:
    """
    :ivar routing_num:
    """
    routing_num: Optional[int] = field(
        default=None,
        metadata=dict(
            name="routingNum",
            type="Attribute"
        )
    )


@dataclass
class RestrictedProductType:
    """
    :ivar number:
    :ivar name:
    :ivar description:
    :ivar routing_num:
    :ivar lang:
    :ivar eff_date:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    routing_num: Optional[int] = field(
        default=None,
        metadata=dict(
            name="routingNum",
            type="Attribute",
            required=True
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    eff_date: str = field(
        default="1900-01-01",
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )


@dataclass
class SizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class SmallSizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            min_inclusive=2,
            max_inclusive=6
        )
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class ProductType(ItemType):
    """
    :ivar number:
    :ivar name:
    :ivar description:
    :ivar eff_date:
    :ivar lang:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ShirtType(RestrictedProductType):
    """
    :ivar size:
    :ivar color:
    :ivar sleeve:
    """
    size: List[SmallSizeType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    color: List[ColorType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sleeve: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ItemsType:
    """
    :ivar hat:
    :ivar umbrella:
    :ivar shirt:
    """
    hat: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    umbrella: List[RestrictedProductType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    shirt: List[ShirtType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
