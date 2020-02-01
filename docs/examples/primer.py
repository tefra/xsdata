from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Usaddress:
    """
    :ivar name:
    :ivar street:
    :ivar city:
    :ivar state:
    :ivar zip:
    :ivar country:
    """
    class Meta:
        name = "USAddress"

    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    street: Optional[str] = field(
        default=None,
        metadata=dict(
            name="street",
            type="Element",
            namespace="",
            required=True
        )
    )
    city: Optional[str] = field(
        default=None,
        metadata=dict(
            name="city",
            type="Element",
            namespace="",
            required=True
        )
    )
    state: Optional[str] = field(
        default=None,
        metadata=dict(
            name="state",
            type="Element",
            namespace="",
            required=True
        )
    )
    zip: Optional[float] = field(
        default=None,
        metadata=dict(
            name="zip",
            type="Element",
            namespace="",
            required=True
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            name="country",
            type="Attribute"
        )
    )


@dataclass
class Comment:
    """
    :ivar value:
    """
    class Meta:
        name = "comment"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class Items:
    """
    :ivar item:
    """
    item: List["Items.Item"] = field(
        default_factory=list,
        metadata=dict(
            name="item",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Item:
        """
        :ivar product_name:
        :ivar quantity:
        :ivar usprice:
        :ivar comment:
        :ivar ship_date:
        :ivar part_num:
        """
        product_name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="productName",
                type="Element",
                namespace="",
                required=True
            )
        )
        quantity: Optional[int] = field(
            default=None,
            metadata=dict(
                name="quantity",
                type="Element",
                namespace="",
                required=True,
                max_exclusive=100.0
            )
        )
        usprice: Optional[float] = field(
            default=None,
            metadata=dict(
                name="USPrice",
                type="Element",
                namespace="",
                required=True
            )
        )
        comment: Optional[Comment] = field(
            default=None,
            metadata=dict(
                name="comment",
                type="Element",
                namespace=""
            )
        )
        ship_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="shipDate",
                type="Element",
                namespace=""
            )
        )
        part_num: Optional[str] = field(
            default=None,
            metadata=dict(
                name="partNum",
                type="Attribute",
                required=True,
                pattern=r"\d{3}-[A-Z]{2}"
            )
        )


@dataclass
class PurchaseOrderType:
    """
    :ivar ship_to:
    :ivar bill_to:
    :ivar comment:
    :ivar items:
    :ivar order_date:
    """
    ship_to: Optional[Usaddress] = field(
        default=None,
        metadata=dict(
            name="shipTo",
            type="Element",
            namespace="",
            required=True
        )
    )
    bill_to: Optional[Usaddress] = field(
        default=None,
        metadata=dict(
            name="billTo",
            type="Element",
            namespace="",
            required=True
        )
    )
    comment: Optional[Comment] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element",
            namespace=""
        )
    )
    items: Optional[Items] = field(
        default=None,
        metadata=dict(
            name="items",
            type="Element",
            namespace="",
            required=True
        )
    )
    order_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="orderDate",
            type="Attribute"
        )
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
