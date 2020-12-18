from docs.examples.xml_context import parser
from docs.examples.xml_parser_from_path import xml_path
from tests.fixtures.primer import PurchaseOrder


order = parser.from_path(xml_path)
assert isinstance(order, PurchaseOrder)