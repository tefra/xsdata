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

API: :ref:`Reference <XML Handlers>`


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


API :ref:`Reference <SerializerConfig>`.


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


API: :ref:`Reference <XML Writers>`


XML Benchmarks
==============

Compare the handlers / writers `performance <https://github.com/tefra/xsdata/actions>`_.

.. code-block::

    ------------------------------------- benchmark 'Parse: 100 books': 4 tests -------------------------------------
    Name (time in ms)                          Min                Max               Mean             Median
    -----------------------------------------------------------------------------------------------------------------
    test_parse_small[XmlEventHandler]      11.0167 (1.0)      11.9290 (1.0)      11.2879 (1.0)      11.2433 (1.0)
    test_parse_small[LxmlEventHandler]     11.2080 (1.02)     12.5390 (1.05)     11.4432 (1.01)     11.3900 (1.01)
    test_parse_small[LxmlSaxHandler]       12.6364 (1.15)     13.3323 (1.12)     12.8680 (1.14)     12.8464 (1.14)
    test_parse_small[XmlSaxHandler]        15.3508 (1.39)     17.4243 (1.46)     15.6225 (1.38)     15.5706 (1.38)
    -----------------------------------------------------------------------------------------------------------------

    --------------------------------------- benchmark 'Parse: 1000 books': 4 tests ---------------------------------------
    Name (time in ms)                            Min                 Max                Mean              Median
    ----------------------------------------------------------------------------------------------------------------------
    test_parse_medium[XmlEventHandler]      109.2143 (1.0)      113.9947 (1.0)      110.3843 (1.0)      109.9962 (1.0)
    test_parse_medium[LxmlEventHandler]     110.9572 (1.02)     118.3406 (1.04)     112.3722 (1.02)     111.6027 (1.01)
    test_parse_medium[LxmlSaxHandler]       124.0605 (1.14)     141.5221 (1.24)     133.6450 (1.21)     136.4759 (1.24)
    test_parse_medium[XmlSaxHandler]        153.4569 (1.41)     155.8310 (1.37)     155.0615 (1.40)     155.1828 (1.41)
    ----------------------------------------------------------------------------------------------------------------------

    ---------------------------------- benchmark 'Parse: 10000 books': 4 tests ----------------------------------
    Name (time in s)                          Min               Max              Mean            Median
    -------------------------------------------------------------------------------------------------------------
    test_parse_large[XmlEventHandler]      1.0975 (1.0)      1.1230 (1.0)      1.1055 (1.0)      1.1034 (1.0)
    test_parse_large[LxmlEventHandler]     1.1199 (1.02)     1.1934 (1.06)     1.1433 (1.03)     1.1370 (1.03)
    test_parse_large[LxmlSaxHandler]       1.2568 (1.15)     1.2955 (1.15)     1.2741 (1.15)     1.2675 (1.15)
    test_parse_large[XmlSaxHandler]        1.5144 (1.38)     1.5603 (1.39)     1.5321 (1.39)     1.5273 (1.38)
    -------------------------------------------------------------------------------------------------------------

    ------------------------------------ benchmark 'Serialize: 100 books': 2 tests -------------------------------------
    Name (time in ms)                             Min                Max               Mean             Median
    --------------------------------------------------------------------------------------------------------------------
    test_serialize_small[XmlEventWriter]      13.5096 (1.0)      15.2481 (1.0)      14.0662 (1.0)      13.9101 (1.0)
    test_serialize_small[LxmlEventWriter]     14.0560 (1.04)     17.7745 (1.17)     14.6972 (1.04)     14.3864 (1.03)
    --------------------------------------------------------------------------------------------------------------------

    --------------------------------------- benchmark 'Serialize: 1000 books': 2 tests --------------------------------------
    Name (time in ms)                               Min                 Max                Mean              Median
    -------------------------------------------------------------------------------------------------------------------------
    test_serialize_medium[XmlEventWriter]      123.7788 (1.0)      125.6158 (1.0)      124.4991 (1.0)      124.4314 (1.0)
    test_serialize_medium[LxmlEventWriter]     125.8150 (1.02)     130.7346 (1.04)     128.4448 (1.03)     128.3278 (1.03)
    -------------------------------------------------------------------------------------------------------------------------

    --------------------------------- benchmark 'Serialize: 10000 books': 2 tests ----------------------------------
    Name (time in s)                             Min               Max              Mean            Median
    ----------------------------------------------------------------------------------------------------------------
    test_serialize_large[XmlEventWriter]      1.2096 (1.0)      1.2278 (1.0)      1.2224 (1.0)      1.2243 (1.0)
    test_serialize_large[LxmlEventWriter]     1.2416 (1.03)     1.3073 (1.06)     1.2751 (1.04)     1.2836 (1.05)
    ----------------------------------------------------------------------------------------------------------------
