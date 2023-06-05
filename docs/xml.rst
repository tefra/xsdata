===========
XML Binding
===========

All binding modules rely on a :class:`~xsdata.formats.dataclass.context.XmlContext`
instance to cache model metadata and binding information.

It's recommended to either reuse the same parser/serializer instance or reuse the
context instance.

.. code-block::

    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.serializers import XmlSerializer

    context = XmlContext()
    parser = XmlParser(context=context)
    serializer = XmlSerializer(context=context)

.. testsetup:: *

    import io
    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig
    from tests import fixtures_dir
    from tests.fixtures.books import Books, BookForm
    from tests.fixtures.primer import PurchaseOrder, Usaddress


Parse from xml filename
=======================

.. doctest::

    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.parsers import XmlParser
    >>> from tests import fixtures_dir # pathlib.Path
    >>> from tests.fixtures.primer import PurchaseOrder, Usaddress
    ...
    >>> filename = str(fixtures_dir.joinpath("primer/sample.xml"))
    >>> parser = XmlParser(context=XmlContext())
    >>> order = parser.parse(filename, PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')


Parse from xml file object
==========================

.. doctest::

    >>> xml_path = fixtures_dir.joinpath("primer/sample.xml")
    >>> with xml_path.open("rb") as fp:
    ...     order = parser.parse(fp, PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Parse from xml stream
=====================

.. doctest::

    >>> import io
    >>> order = parser.parse(io.BytesIO(xml_path.read_bytes()), PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Parse from xml string
=====================

.. doctest::

    >>> order = parser.from_string(xml_path.read_text(), PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Parse from xml bytes
====================

.. doctest::

    >>> order = parser.from_bytes(xml_path.read_bytes(), PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Parse from xml Path
===================

.. doctest::

    >>> order = parser.from_path(xml_path, PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Parse from Element or ElementTree
=================================

For selective parsing you can use an Element or ElementTree as source. This way
you can modify the dom or pick from which node to start binding data.

Using lxml and :class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler`

.. doctest::

    >>> import lxml
    >>> from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
    ...
    >>> parser = XmlParser(handler=LxmlEventHandler)
    >>> tree = lxml.etree.parse(str(xml_path))
    >>> bill_to = parser.parse(tree.find('.//billTo'), Usaddress)
    >>> bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')


Using the xml module and
:class:`~xsdata.formats.dataclass.parsers.handlers.XmlEventHandler`

.. doctest::

    >>> from xml.etree import ElementTree as ET
    >>> from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
    ...
    >>> parser = XmlParser(handler=XmlEventHandler)
    >>> tree = ET.parse(str(xml_path))
    >>> ship_to = parser.parse(tree.find('.//shipTo'), Usaddress)
    >>> ship_to
    Usaddress(name='Alice Smith', street='123 Maple Street', city='Mill Valley', state='CA', zip=Decimal('90952'), country='US')


.. note::

    The :mod:`python:xml.etree.ElementTree` api doesn't preserve the namespace prefixes,
    the handler will auto generate new ones.



Parse with unknown xml target type
==================================

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.


.. doctest::

    >>> order = parser.from_bytes(xml_path.read_bytes())
    >>> type(order)
    <class 'tests.fixtures.primer.order.PurchaseOrder'>


Parser Config
=============

The configuration allows to enable/disable various features and failures.

.. doctest::

    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig
    ...
    >>> config = ParserConfig(
    ...     base_url=None,
    ...     load_dtd=False,
    ...     process_xinclude=False,
    ...     fail_on_unknown_properties=False,
    ...     fail_on_unknown_attributes=False,
    ...     fail_on_converter_warnings=False,
    ... )
    >>> parser = XmlParser(config=config)
    >>> order = parser.from_bytes(xml_path.read_bytes())
    >>> order.bill_to.street
    '8 Oak Avenue'

API :ref:`Reference <ParserConfig>`.


Parse xml with alternative handlers
===================================

XmlHandlers read the xml source and push build events to create the target class.
xsData ships with multiple handlers based on lxml and native python that vary in
performance and features.

.. hint::

    If you installed xsdata with lxml the default handler is set to
    :class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler` otherwise
    :class:`~xsdata.formats.dataclass.parsers.handlers.XmlEventHandler` will be used.

.. doctest::

    >>> from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
    ...
    >>> parser = XmlParser(handler=XmlEventHandler)
    >>> order = parser.from_path(xml_path)
    >>> order.bill_to.street
    '8 Oak Avenue'

.. hint::

    It's recommended to give all of them a try, based on your use case you
    might get different results.

    You can also extend one of them if you want to do any optimizations or
    customize the default behaviour.

Read :ref:`more... <XML Handlers>`


Parse xml with xinclude statements
==================================

The :class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler` and
:class:`~xsdata.formats.dataclass.parsers.handlers.XmlEventHandler` both support
processing xinclude directives.

If you are parsing from memory you need to specify the base url in the config in order
to load the children documents.

.. doctest::

    >>> from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler
    ...
    >>> xml = """<?xml version="1.0" encoding="UTF-8"?>
    ... <brk:books xmlns:brk="urn:books" xmlns:xi="http://www.w3.org/2001/XInclude">
    ...   <xi:include href="bk001.xml"/>
    ...   <xi:include href="bk002.xml"/>
    ... </brk:books>"""
    >>> base_url = fixtures_dir.joinpath("books/books-xinclude.xml")
    >>> config = ParserConfig(process_xinclude=True, base_url=str(base_url))
    >>> parser = XmlParser(config=config)
    >>> books = parser.from_string(xml)
    >>> print(books.book[1])
    BookForm(author='Nagata, Suanne', title='Becoming Somebody', genre='Biography', price=33.95, pub_date=XmlDate(2001, 1, 10), review='A masterpiece of the fine art of gossiping.', id='bk002', lang='en')


Serialize xml to string
=======================

.. doctest::

    >>> from tests.fixtures.books import Books, BookForm
    >>> from xsdata.formats.dataclass.serializers import XmlSerializer
    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    ...
    >>> books = Books(
    ...     book=[
    ...         BookForm(
    ...             id="bk001",
    ...             author="Hightower, Kim",
    ...             title="The First Book",
    ...             genre="Fiction",
    ...             price=44.95,
    ...             pub_date="2000-10-01",
    ...             review="An amazing story of nothing.",
    ...         )
    ...     ]
    ... )
    ...
    >>> config = SerializerConfig(pretty_print=True)
    >>> serializer = XmlSerializer(config=config)
    >>> print(serializer.render(books))
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
    <BLANKLINE>


Serialize xml with custom namespace prefixes
============================================

.. doctest::

    >>> print(serializer.render(books, ns_map={"bk": "urn:books"}))
    <?xml version="1.0" encoding="UTF-8"?>
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
    <BLANKLINE>


Serialize xml with default namespace
====================================

.. doctest::

    >>> print(serializer.render(books, ns_map={None: "urn:books"}))
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
    <BLANKLINE>


Serialize xml to stream
=======================

.. doctest::

    >>> from pathlib import Path
    ...
    >>> path = Path("output.xml")
    >>> with path.open("w") as fp:
    ...     serializer.write(fp, books)
    ...
    >>> print(path.read_text())
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
    <BLANKLINE>
    >>> path.unlink()


Serialize xml with alternative writers
======================================

xsData ships with multiple writers based on lxml and native python that may vary
in performance in some cases. The output of all them is consistent with a few
exceptions when handling mixed content with ``pretty_print=True``.

.. hint::

    If you installed xsdata with lxml the default writer is set to
    :class:`~xsdata.formats.dataclass.serializers.writers.LxmlEventWriter` otherwise
    :class:`~xsdata.formats.dataclass.serializers.writers.XmlEventWriter` will be used.

.. doctest::

    >>> from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
    ...
    >>> serializer = XmlSerializer(config=config, writer=XmlEventWriter)
    >>> print(serializer.render(books))
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
    <BLANKLINE>

Read :ref:`more... <XML Writers>`


Serialize with omit default attributes
======================================

Attributes are allowed to have default or fixed values and be marked as optional. The
default behaviour is to write them explicitly during serialization but you can disable
them through config.

.. doctest::

    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    ...
    >>> serializer = XmlSerializer(config=SerializerConfig(
    ...     pretty_print=True,
    ...     xml_declaration=False,
    ...     ignore_default_attributes=True,
    ...     schema_location="urn books.xsd",
    ...     no_namespace_schema_location=None,
    ... ))
    >>> print(serializer.render(books))
    <ns0:books xmlns:ns0="urn:books" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn books.xsd">
      <book id="bk001">
        <author>Hightower, Kim</author>
        <title>The First Book</title>
        <genre>Fiction</genre>
        <price>44.95</price>
        <pub_date>2000-10-01</pub_date>
        <review>An amazing story of nothing.</review>
      </book>
    </ns0:books>
    <BLANKLINE>


Read :ref:`more... <SerializerConfig>`


.. meta::
    :keywords: xml, parse, serialize, python
