from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

config = ParserConfig(
    base_url=None,
    process_xinclude=False,
    fail_on_unknown_properties=False,
)
parser = XmlParser(config=config)