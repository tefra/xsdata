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
            name="value",
            type="Attribute"
        )
    )


@dataclass
class ProductType:
    """
    :ivar routing_num:
    :ivar number:
    :ivar name:
    :ivar description:
    :ivar eff_date:
    :ivar lang:
    """
    routing_num: Optional[int] = field(
        default=None,
        metadata=dict(
            name="routingNum",
            type="Attribute"
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
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
            name="lang",
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
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute"
        )
    )


@dataclass
class RestrictedProductType(ProductType):
    """
    :ivar number:
    :ivar name:
    :ivar routing_num:
    :ivar eff_date:
    :ivar lang:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
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
    eff_date: str = field(
        default="1900-01-01",
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute"
        )
    )


@dataclass
class SmallSizeType(SizeType):
    """
    :ivar system:
    """
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute",
            required=True
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
            name="size",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    color: List[ColorType] = field(
        default_factory=list,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sleeve: Optional[int] = field(
        default=None,
        metadata=dict(
            name="sleeve",
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
            name="hat",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    umbrella: List[RestrictedProductType] = field(
        default_factory=list,
        metadata=dict(
            name="umbrella",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    shirt: List[ShirtType] = field(
        default_factory=list,
        metadata=dict(
            name="shirt",
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
