from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Usaddress:
    class Meta:
        name = "USAddress"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    state: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    zip: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    country: str = field(
        init=False,
        default="US",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Comment:
    class Meta:
        name = "comment"

    value: str = field()


@dataclass(kw_only=True)
class Items:
    item: list[Items.Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
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

        product_name: str = field(
            metadata={
                "name": "productName",
                "type": "Element",
                "namespace": "",
            }
        )
        quantity: int = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "max_exclusive": 100,
            }
        )
        usprice: Decimal = field(
            metadata={
                "name": "USPrice",
                "type": "Element",
                "namespace": "",
            }
        )
        comment: None | Comment = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ship_date: None | XmlDate = field(
            default=None,
            metadata={
                "name": "shipDate",
                "type": "Element",
                "namespace": "",
            },
        )
        part_num: str = field(
            metadata={
                "name": "partNum",
                "type": "Attribute",
                "pattern": r"\d{3}-[A-Z]{2}",
            }
        )


@dataclass(kw_only=True)
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

    ship_to: Usaddress = field(
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "",
        }
    )
    bill_to: Usaddress = field(
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "",
        }
    )
    comment: None | Comment = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    items: Items = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    order_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "orderDate",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PurchaseOrder(PurchaseOrderType):
    class Meta:
        name = "purchaseOrder"
