from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate


@dataclass
class Usaddress:
    class Meta:
        name = "USAddress"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    street: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    city: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    zip: Decimal | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    country: str = field(
        init=False,
        default="US",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Comment:
    class Meta:
        name = "comment"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Items:
    item: list[Items.Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Item:
        """
        Parameters
        ----------
        product_name
        quantity
        usprice
            Price amount in USD
        comment
        ship_date
        part_num
            Stock Keeping Unit
        """

        product_name: str | None = field(
            default=None,
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        quantity: int | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_exclusive": 100,
            },
        )
        usprice: Decimal | None = field(
            default=None,
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        comment: Comment | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ship_date: XmlDate | None = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "",
            },
        )
        part_num: str | None = field(
            default=None,
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "required": True,
                "pattern": r"\d{3}-[A-Z]{2}",
            },
        )


@dataclass
class PurchaseOrderType:
    """
    Purchase order schema for Example.com.

    Copyright 2000 Example.com. All rights reserved.

    Parameters
    ----------
    ship_to
        Shipping Address
    bill_to
        Billing Address
    comment
    items
    order_date
    """

    ship_to: Usaddress | None = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    bill_to: Usaddress | None = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    comment: Comment | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    items: Items | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    order_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
        },
    )


@dataclass
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
