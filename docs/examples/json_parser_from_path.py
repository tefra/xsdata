from pathlib import Path

from tests.fixtures.defxmlschema.chapter05 import Order
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser

root_path = Path(__file__).parent.parent.parent
json_path = root_path.joinpath("tests/fixtures/defxmlschema/chapter05.json")

parser = JsonParser(context=XmlContext())
result = parser.from_path(json_path, Order)
#  Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))
