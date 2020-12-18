from pathlib import Path

from docs.examples.xml_context import parser
from tests.fixtures.primer import PurchaseOrder, Usaddress

xml_path = Path(__file__).joinpath("../../../tests/fixtures/primer/order.xml")
order = parser.from_path(xml_path, PurchaseOrder)

assert order.bill_to == Usaddress(
    name='Robert Smith',
    street='8 Oak Avenue',
    city='Old Town',
    state='PA',
    zip=95819.0
)