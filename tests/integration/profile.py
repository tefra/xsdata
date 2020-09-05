from tests import xsdata_temp_dir
from tests.fixtures.books import Books
from tests.integration.conftest import pytest_configure
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

fixture = xsdata_temp_dir.joinpath("benchmark_large.xml")
if not fixture.exists():
    pytest_configure(None)


context = XmlContext()
parser = XmlParser(context=context)
parser.from_bytes(fixture.read_bytes(), Books)
