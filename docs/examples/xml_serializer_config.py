from docs.examples.xml_serializer_basic import books
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

serializer = XmlSerializer(config=SerializerConfig(
    pretty_print=True,
    encoding="UTF-8",
    xml_version="1.1",
    schema_location="urn books.xsd",
    no_namespace_schema_location=None,
))
xml = serializer.render(books)