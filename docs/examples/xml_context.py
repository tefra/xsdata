from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

context = XmlContext()
parser = XmlParser(context=context)
serializer = XmlSerializer(context=context)