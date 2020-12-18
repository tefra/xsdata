from docs.examples.xml_parser_from_path import xml_path
from tests.fixtures.primer import PurchaseOrder
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler

parser = XmlParser(handler=XmlEventHandler)
order = parser.from_path(xml_path, PurchaseOrder)