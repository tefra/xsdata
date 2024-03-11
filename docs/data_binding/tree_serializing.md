# Element Tree Serializer

The element tree serializers will render an object into an element tree, that you can
use to run XPATH evaluations or XSLT transformations.

There are two implementations based on lxml
[LxmlTreeSerializer][xsdata.formats.dataclass.serializers.LxmlTreeSerializer] and native
python [XmlTreeSerializer][xsdata.formats.dataclass.serializers.XmlTreeSerializer].

## xml.etree.ElementTree.Element

```python
>>> from xml.etree import ElementTree
>>> from tests.fixtures.books.fixtures import books
>>> from xsdata.formats.dataclass.serializers import XmlTreeSerializer
...
>>> serializer = XmlTreeSerializer()
>>> result = serializer.render(books)
...
>>> result.find(".//title").text
'The First Book'

```

## lxml.etree.Element

```python
>>> from lxml import etree
>>> from tests.fixtures.books.fixtures import books
>>> from xsdata.formats.dataclass.serializers import LxmlTreeSerializer
...
>>> serializer = LxmlTreeSerializer()
>>> result = serializer.render(books)
...
>>> etree.indent(result)
>>> actual = etree.tostring(result)
>>> print(actual.decode())
<ns0:books xmlns:ns0="urn:books">
  <book>
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
  <book>
    <author>Nagata, Suanne</author>
    <title>Becoming Somebody</title>
    <genre>Biography</genre>
    <price>33.95</price>
    <pub_date>2001-01-10</pub_date>
    <review>A masterpiece of the fine art of gossiping.</review>
  </book>
</ns0:books>

```
