from tests import fixtures_dir
from tests.fixtures.books import Books
from tests.fixtures.primer import PurchaseOrder, Usaddress
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

config = ParserConfig(fail_on_unknown_properties=True)
parser = XmlParser(config=config)
order = parser.from_path(fixtures_dir.joinpath("primer/order.xml"), PurchaseOrder)

assert order.bill_to == Usaddress(
    name='Robert Smith',
    street='8 Oak Avenue',
    city='Old Town',
    state='PA',
    zip=95819.0
)

path = fixtures_dir.joinpath("books/books-xinclude.xml")
config = ParserConfig(process_xinclude=True, base_url=path.as_uri())
parser = XmlParser(config=config)
actual = parser.from_bytes(path.read_bytes(), Books)

from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler

parser = XmlParser(handler=XmlEventHandler)
order = parser.from_path(fixtures_dir.joinpath("primer/order.xml"), PurchaseOrder)