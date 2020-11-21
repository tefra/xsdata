import sys
import tempfile

from tests.fixtures.books import Books, BookForm
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

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

serializer = XmlSerializer(pretty_print=True)
xml = serializer.render(books)

assert xml == """
<?xml version='1.0' encoding='UTF-8'?>
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

serializer = XmlSerializer(pretty_print=True)
xml = serializer.render(books, ns_map={"bk": "urn:books"})

assert xml == """
<?xml version='1.0' encoding='UTF-8'?>
<bk:books xmlns:bk="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</bk:books>
""".lstrip()

serializer = XmlSerializer(pretty_print=True)
xml = serializer.render(books, ns_map={None: "urn:books"})

assert xml == """
<?xml version='1.0' encoding='UTF-8'?>
<books xmlns="urn:books">
  <book xmlns="" id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</books>
""".lstrip()

serializer = XmlSerializer(
    pretty_print=True, encoding="US-ASCII", writer=XmlEventWriter
)
xml = serializer.render(books, ns_map={None: "urn:books"})
assert xml == """
<?xml version="1.0" encoding="US-ASCII"?>
<books xmlns="urn:books">
  <book xmlns="" id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</books>
""".lstrip()

serializer.write(sys.stdout, books, ns_map={None: "urn:books"})

with tempfile.TemporaryFile() as fp:
    serializer.write(fp, books)
