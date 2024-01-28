# XML Parsing

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>> from xsdata.formats.dataclass.parsers.config import ParserConfig

>>> config = ParserConfig()
>>> context = XmlContext()
>>> parser = XmlParser(context=context, config=config)
>>> parser = XmlParser()

```

## Filenames

```python
>>> from tests.fixtures.primer import PurchaseOrder
...
>>> order = parser.parse("tests/fixtures/primer/sample.xml", PurchaseOrder)
>>> order.bill_to
Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')

```

## File-like objects

```python
>>> with open("tests/fixtures/primer/sample.xml", "rb") as fp:
...     order = parser.parse(fp, PurchaseOrder)
>>> order.bill_to.street
'8 Oak Avenue'

```

## String

```python
>>> from pathlib import Path
>>>
>>> xml_string = Path("tests/fixtures/primer/sample.xml").read_text()
>>> order = parser.from_string(xml_string, PurchaseOrder)
>>> order.bill_to.street
'8 Oak Avenue'

```

## Bytes

```python
>>> xml_bytes = Path("tests/fixtures/primer/sample.xml").read_bytes()
>>> order = parser.from_bytes(xml_bytes, PurchaseOrder)
>>> order.bill_to.street
'8 Oak Avenue'

```

## pathlib.Path

```python
>>> file_path = Path("tests/fixtures/primer/sample.xml")
>>> order = parser.from_path(file_path, PurchaseOrder)
>>> order.bill_to.street
'8 Oak Avenue'

```

## lxml.etree.ElementTree

For selective parsing you can use an Element or ElementTree as source. This way you can
modify the dom or pick from which node to start binding data.

Using [`lxml`][] with
[`LxmlEventHandler`][xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler]

```python
>>> import lxml
>>> from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
>>> from tests.fixtures.primer import Usaddress
...
>>> parser = XmlParser(handler=LxmlEventHandler)
>>> tree = lxml.etree.parse("tests/fixtures/primer/sample.xml")
>>> bill_to = parser.parse(tree.find('.//billTo'), Usaddress)
>>> bill_to
Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')

```

## xml.etree.ElementTree

Using the [`xml`][] module with
[`XmlEventHandler`][xsdata.formats.dataclass.parsers.handlers.XmlEventHandler]

```python
>>> from xml.etree import ElementTree
>>> from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
...
>>> parser = XmlParser(handler=XmlEventHandler)
>>> tree = ElementTree.parse("tests/fixtures/primer/sample.xml")
>>> ship_to = parser.parse(tree.find('.//shipTo'), Usaddress)
>>> ship_to
Usaddress(name='Alice Smith', street='123 Maple Street', city='Mill Valley', state='CA', zip=Decimal('90952'), country='US')

```

!!! Note

    The [xml.etree.ElementTree][] api doesn't preserve the namespace prefixes,
    the handler will auto generate new ones.

## Unknown target clazz

It's optimal to provide the target class but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

```python
>>> order = parser.parse("tests/fixtures/primer/sample.xml")
>>> type(order)
<class 'tests.fixtures.primer.order.PurchaseOrder'>

```

## Alternative handlers

XmlHandlers read the xml source and push build events to create the target class. xsData
ships with two handlers based on lxml and native python that vary in performance and
features.

!!! Hint

    If you installed xsdata with lxml the default handler is set to
    [LxmlEventHandler][xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler] otherwise
    [XmlEventHandler][xsdata.formats.dataclass.parsers.handlers.XmlEventHandler] will be used.

```python
>>> from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
...
>>> parser = XmlParser(handler=XmlEventHandler)
>>> order = parser.parse("tests/fixtures/primer/sample.xml")
>>> order.bill_to.street
'8 Oak Avenue'

```

!!! Hint

    It's recommended to give all of them a try, based on your use case you
    might get different results.

    You can also extend one of them if you want to do any optimizations or
    customize the default behaviour.

## XML Inclusions

XML Inclusions (XInclude) is a W3C specification that defines a way to include XML
fragments from different sources into a single document.

If you are parsing from memory you need to specify the base url in the config in order
to load the included documents correctly.

```python
>>> from tests.fixtures.books import Books
>>> xml = """<?xml version="1.0" encoding="UTF-8"?>
... <brk:books xmlns:brk="urn:books" xmlns:xi="http://www.w3.org/2001/XInclude">
...   <xi:include href="bk001.xml"/>
...   <xi:include href="bk002.xml"/>
... </brk:books>"""
>>> config = ParserConfig(process_xinclude=True, base_url="tests/fixtures/books/books-xinclude.xml")
>>> parser = XmlParser(config=config)
>>> books = parser.from_string(xml, Books)
>>> print(books.book[1])
BookForm(author='Nagata, Suanne', title='Becoming Somebody', genre='Biography', price=33.95, pub_date=XmlDate(2001, 1, 10), review='A masterpiece of the fine art of gossiping.', id='bk002', lang='en')

```
