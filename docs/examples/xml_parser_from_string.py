from docs.examples.xml_context import parser
from docs.examples.xml_parser_from_path import xml_path
from tests.fixtures.primer import PurchaseOrder

order = parser.from_bytes(xml_path.read_text(), PurchaseOrder)
