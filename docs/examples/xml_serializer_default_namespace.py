from docs.examples.xml_serializer_basic import serializer, books

xml = serializer.render(books, ns_map={None: "urn:books"})
assert xml == """
<?xml version="1.0" encoding="UTF-8"?>
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