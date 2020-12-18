from tests.fixtures.books import Books, BookForm
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

books = Books(
    book=[
        BookForm(
            id="bk001",
            author="Hightower, Kim",
            title="The First Book",
            genre="Fiction",
            price=44.95,
            pub_date="2000-10-01",
            review="An amazing story of nothing.",
        )
    ]
)

config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=config)
xml = serializer.render(books)
assert xml == """
<?xml version="1.0" encoding="UTF-8"?>
<ns0:books xmlns:ns0="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</ns0:books>
""".lstrip()