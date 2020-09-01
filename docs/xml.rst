===========
XML Binding
===========


:class:`~xsdata.formats.dataclass.parsers.XmlParser`
====================================================

The parser has three instance methods `from_string`, `from_bytes` and `from_path`,
to parse from memory or to let the parser load the input document. All of them require
the target class Type to bind the input data.


Parameters
----------

**config** (:class:`~xsdata.formats.dataclass.parsers.config.ParserConfig`)

.. list-table::
   :widths: 20 10 220
   :header-rows: 1
   :align: left

   * - Namespace
     - Type
     - Description
   * - base_url
     - str
     - A base URL for when parsing from memory and you want support for relative links
       eg xinclude, default: ``None``
   * - process_xinclude
     - bool
     - Process xinclude statements. , default: ``False``
   * - fail_on_unknown_properties
     - bool
     - Should fail on unknown properties that can't be mapped to any wildcard field,
       default: ``True``


**context** (:class:`~xsdata.formats.dataclass.context.XmlContext`)

It's the cache layer for the binding directives of models and their fields. You may
share a context instance between parser/serializer instances to avoid compiling the
cache more than once.

.. hint::

    it's recommended to use a static or global instance of your parser or serializer
    per document type.


**handler** (:class:`~xsdata.formats.dataclass.parsers.mixins.XmlHandler`)

The XmlHandler type to use in order to read the xml source and push element events
to the main parser.

Default: :class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler`


Xml Handlers
------------

:class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler`

It's based on `lxml.etree.iterparse` incremental parser and offers the best
balance between features and performance. If the xinclude parser config is enabled
the handler will parse the whole tree and then use `iterwalk` to feed the main parser
with element events.


:class:`~xsdata.formats.dataclass.parsers.handlers.LxmlSaxHandler`

It's based on the lxml target parser interface. `xinclude` statements are not supported
and is quite slower than the iterparse implementation.


:class:`~xsdata.formats.dataclass.parsers.handlers.XmlEventHandler`

It's based on the native python xml.etree.ElementTree.interparse incremental parser.
`xinclude` statements are not supported and it doesn't support the newly allowed
characters in XML 1.1. Despite it's drawbacks in some cases it's slightly faster than
the lxml iterparse implementation.


:class:`~xsdata.formats.dataclass.parsers.handlers.XmlSaxHandler`

It's based on the native python xml.sax.ContentHandler and doesn't support `xinclude`
statements and is a lot slower than the iterparse implementation.


.. hint::

    Why keep them all? The hard part was the decouple of the parser from a specific
    implementation. The handlers are quite simple and very easy to test.

    It's also recommended to give all of them a try, based on your use case you
    might get different results.

    You can also extend one of them if you want to do any optimization like skipping
    irrelevant events earlier than the binding process when it's instructed
    to skip unknown properties.


Benchmarks
----------

The benchmarks run with the `test suite <https://travis-ci.com/tefra/xsdata>`_.


.. code-block::

    ----------------------------------- benchmark 'size: 53.21 KB': 4 tests -----------------------------------
    Name (time in ms)                    Min                Max               Mean             Median
    -----------------------------------------------------------------------------------------------------------
    test_small[LxmlEventHandler]     11.9252 (1.0)      24.1855 (1.10)     12.6733 (1.0)      12.2927 (1.0)
    test_small[XmlEventHandler]      11.9761 (1.00)     35.8465 (1.63)     13.7822 (1.09)     12.3014 (1.00)
    test_small[LxmlSaxHandler]       14.4966 (1.22)     21.9954 (1.0)      15.1298 (1.19)     14.9358 (1.22)
    test_small[XmlSaxHandler]        16.4111 (1.38)     36.1555 (1.64)     18.2357 (1.44)     16.9312 (1.38)
    -----------------------------------------------------------------------------------------------------------

    ------------------------------------- benchmark 'size: 531.33 KB': 4 tests -------------------------------------
    Name (time in ms)                      Min                 Max                Mean              Median
    ----------------------------------------------------------------------------------------------------------------
    test_medium[LxmlEventHandler]     122.0357 (1.0)      158.1659 (1.0)      127.5115 (1.0)      123.1530 (1.0)
    test_medium[XmlEventHandler]      122.1189 (1.00)     165.7320 (1.05)     133.0798 (1.04)     125.3347 (1.02)
    test_medium[LxmlSaxHandler]       145.2495 (1.19)     165.9502 (1.05)     149.9644 (1.18)     146.5776 (1.19)
    test_medium[XmlSaxHandler]        166.7054 (1.37)     193.0464 (1.22)     174.3553 (1.37)     172.1119 (1.40)
    ----------------------------------------------------------------------------------------------------------------

    -------------------------------- benchmark 'size: 5312.58 KB': 4 tests --------------------------------
    Name (time in s)                    Min               Max              Mean            Median
    -------------------------------------------------------------------------------------------------------
    test_large[XmlEventHandler]      1.2444 (1.0)      1.3451 (1.0)      1.2795 (1.0)      1.2740 (1.0)
    test_large[LxmlEventHandler]     1.2608 (1.01)     1.4284 (1.06)     1.3385 (1.05)     1.3305 (1.04)
    test_large[LxmlSaxHandler]       1.4625 (1.18)     1.6302 (1.21)     1.5405 (1.20)     1.5478 (1.21)
    test_large[XmlSaxHandler]        1.7173 (1.38)     1.7610 (1.31)     1.7368 (1.36)     1.7334 (1.36)
    -------------------------------------------------------------------------------------------------------


Example: from path
------------------

.. literalinclude:: examples/xml_parser.py
   :lines: 1,6-8,9-20


Example: from memory
--------------------

With support for `XML Inclusions <https://www.w3.org/TR/xinclude-11/>`_

.. literalinclude:: examples/xml_parser.py
   :lines: 21-24


Example: alternative handler
----------------------------

.. literalinclude:: examples/xml_parser.py
   :lines: 26-29



:class:`~xsdata.formats.dataclass.serializers.XmlSerializer`
============================================================

The serializer can also be initialized with a xml context instance, if your use case
needs to parse and serialize the same type of objects you could share the same xml
context instance between them to save on memory and processing.

.. code-block:: python

        >>> import pprint
        >>> from docs.examples.primer import PurchaseOrder, Items, Usaddress
        >>> from xsdata.formats.dataclass.serializers import XmlSerializer

        >>> item = Items.Item(product_name="duct tape", quantity=99, usprice=19.99)
        >>> items = Items()
        >>> items.item.append(item)
        >>>
        >>> address = Usaddress(name="Chris", street="Sesame", city="New York", state="New York", zip="123", country="US")
        >>> order = PurchaseOrder(ship_to=address, bill_to=address, items=items)

        >>> serializer = XmlSerializer(pretty_print=True)
        >>> pprint.pprint(serializer.render(order))
        ("<?xml version='1.0' encoding='UTF-8'?>\n"
         '<purchaseOrder>\n'
         '  <shipTo country="US">\n'
         '    <name>Chris</name>\n'
         '    <street>Sesame</street>\n'
         '    <city>New York</city>\n'
         '    <state>New York</state>\n'
         '    <zip>123</zip>\n'
         '  </shipTo>\n'
         '  <billTo country="US">\n'
         '    <name>Chris</name>\n'
         '    <street>Sesame</street>\n'
         '    <city>New York</city>\n'
         '    <state>New York</state>\n'
         '    <zip>123</zip>\n'
         '  </billTo>\n'
         '  <items>\n'
         '    <item>\n'
         '      <productName>duct tape</productName>\n'
         '      <quantity>99</quantity>\n'
         '      <USPrice>19.99</USPrice>\n'
         '    </item>\n'
         '  </items>\n'
         '</purchaseOrder>\n')
        >>>
