===========
XML Binding
===========

All binding modules rely on a :class:`~xsdata.formats.dataclass.context.XmlContext`
instance to cache marshalling information.

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

    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig
    from tests import fixtures_dir
    from tests.fixtures.books import Books, BookForm
    from tests.fixtures.primer import PurchaseOrder, Usaddress

    xml_path = fixtures_dir.joinpath("primer/order.xml")
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

    parser = XmlParser()
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))


Parsing XML
===========


From Path
---------

.. doctest::

    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.parsers import XmlParser
    >>> from tests import fixtures_dir
    >>> from tests.fixtures.primer import PurchaseOrder, Usaddress
    ...
    >>> xml_path = fixtures_dir.joinpath("primer/order.xml")
    >>> parser = XmlParser(context=XmlContext())
    >>> order = parser.from_path(xml_path, PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')


From string
-----------

.. doctest::

    >>> order = parser.from_string(xml_path.read_text(), PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


From bytes
----------

.. doctest::

    >>> order = parser.from_bytes(xml_path.read_bytes(), PurchaseOrder)
    >>> order.bill_to.street
    '8 Oak Avenue'


Unknown target type
-------------------

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

    >>> order = parser.from_bytes(xml_path.read_bytes())
    >>> type(order)
    <class 'tests.fixtures.primer.order.PurchaseOrder'>


Parser Config
-------------

    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig
    ...
    >>> config = ParserConfig(
    ...     base_url=None,
    ...     process_xinclude=False,
    ...     fail_on_unknown_properties=False,
    ... )
    >>> parser = XmlParser(config=config)
    >>> order = parser.from_bytes(xml_path.read_bytes())
    >>> order.bill_to.street
    '8 Oak Avenue'

API :ref:`Reference <ParserConfig>`.


Alternative handlers
--------------------

XmlHandlers read the xml source and push build events to create the target class.
xsData ships with multiple handlers based on lxml and native python that vary in
performance and features.

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


Serializing XML
===============


Render to string
----------------

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


Set custom prefixes
--------------------

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


Set a default namespace
-----------------------

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


Write to stream
---------------

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


Serializer Config
-----------------

.. doctest::

    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    ...
    >>> serializer = XmlSerializer(config=SerializerConfig(
    ...     pretty_print=True,
    ...     encoding="UTF-8",
    ...     xml_version="1.1",
    ...     xml_declaration=False,
    ...     schema_location="urn books.xsd",
    ...     no_namespace_schema_location=None,
    ... ))
    >>> print(serializer.render(books))
    <ns0:books xmlns:ns0="urn:books" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn books.xsd">
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


Read :ref:`more... <SerializerConfig>`


Alternative Writers
-------------------

xsData ships with multiple writers based on lxml and native python that may vary
in performance in some cases. The output of all them is consistent with a few
exceptions when handling mixed content with ``pretty_print=True``.

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
