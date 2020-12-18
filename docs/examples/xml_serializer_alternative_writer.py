from docs.examples.xml_serializer_basic import books, config
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

serializer = XmlSerializer(config=config, writer=XmlEventWriter)
xml = serializer.render(books)