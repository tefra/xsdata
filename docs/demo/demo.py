from pathlib import Path

from tests.fixtures.primer import PurchaseOrder
from xsdata.formats.dataclass.parsers import XmlParser

parser = XmlParser()
filepath = Path("tests/fixtures/primer/order.xml")
order = parser.from_path(filepath, PurchaseOrder)

order.bill_to
