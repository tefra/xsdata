from decimal import Decimal
from tests.fixtures.primer.order import Comment
from tests.fixtures.primer.order import Items
from tests.fixtures.primer.order import PurchaseOrder
from tests.fixtures.primer.order import Usaddress
from xsdata.models.datatype import XmlDate


obj = PurchaseOrder(
    ship_to=Usaddress(
        name='Alice Smith',
        street='123 Maple Street',
        city='Mill Valley',
        state='CA',
        zip=Decimal('90952')
    ),
    bill_to=Usaddress(
        name='Robert Smith',
        street='8 Oak Avenue',
        city='Old Town',
        state='PA',
        zip=Decimal('95819')
    ),
    comment=Comment(
        value='Hurry, my lawn is going wild!'
    ),
    items=Items(
        item=[
            Items.Item(
                product_name='Lawnmower',
                quantity=1,
                usprice=Decimal('148.95'),
                comment=Comment(
                    value='Confirm this is electric'
                ),
                part_num='872-AA'
            ),
            Items.Item(
                product_name='Baby Monitor',
                quantity=1,
                usprice=Decimal('39.98'),
                ship_date=XmlDate(1999, 5, 21),
                part_num='926-AA'
            ),
        ]
    ),
    order_date=XmlDate(1999, 10, 20)
)
