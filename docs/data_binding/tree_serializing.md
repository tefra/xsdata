# Element Tree Serializer

The tree serializer will render an object into an element tree, that you can use to run
XPATH evaluations or XSLT transformations.

The [TreeSerializer][xsdata.formats.dataclass.serializers.TreeSerializer] depends on
lxml. There is no native python ElementTree implementation because of limitations with
namespaces.

## Example

```python
>>> from lxml import etree
>>> from tests.fixtures.books.fixtures import books
>>> from xsdata.formats.dataclass.serializers import TreeSerializer
...
>>> serializer = TreeSerializer()
>>> serializer.config.indent = "  "
>>> result = serializer.render(books, ns_map={'bk': "urn:books"})
...
>>> actual = etree.tostring(result)
>>> print(actual.decode())
<bk:books xmlns:bk="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
  <book id="bk002" lang="en">
    <author>Nagata, Suanne</author>
    <title>Becoming Somebody</title>
    <genre>Biography</genre>
    <price>33.95</price>
    <pub_date>2001-01-10</pub_date>
    <review>A masterpiece of the fine art of gossiping.</review>
  </book>
</bk:books>

```
