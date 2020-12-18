===========
XML Binding
===========

All binding modules rely on a :class:`~xsdata.formats.dataclass.context.XmlContext`
instance to cache marshalling information.

It's recommended to either reuse the same parser/serializer instance or reuse the
context instance.

.. literalinclude:: examples/xml_context.py


Parsing XML
===========


From Path
---------

.. literalinclude:: examples/xml_parser_from_path.py


From string
-----------

.. literalinclude:: examples/xml_parser_from_string.py


From bytes
----------

.. literalinclude:: examples/xml_parser_from_bytes.py


Unknown target type
-------------------

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

.. literalinclude:: examples/xml_parser_unknown_target.py


Parser Config
-------------

.. literalinclude:: examples/xml_parser_config.py

API :ref:`Reference <ParserConfig>`.


Alternative handlers
--------------------

XmlHandlers read the xml source and push build events to create the target class.
xsData ships with multiple handlers based on lxml and native python that vary in
performance and features.

.. literalinclude:: examples/xml_parser_alternative_handler.py

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


Serializing XML
===============


Render to string
----------------

.. literalinclude:: examples/xml_serializer_basic.py
    :lines: 1-21

.. literalinclude:: examples/xml_serializer_basic.py
    :lines: 23-33
    :language: xml


Set custom prefixes
--------------------

.. literalinclude:: examples/xml_serializer_custom_prefixes.py
    :lines: 1-3

.. literalinclude:: examples/xml_serializer_custom_prefixes.py
    :lines: 5-15
    :language: xml


Set a default namespace
-----------------------

.. literalinclude:: examples/xml_serializer_default_namespace.py
    :lines: 3

.. literalinclude:: examples/xml_serializer_default_namespace.py
    :lines: 5-15
    :language: xml


Write to stream
---------------

.. literalinclude:: examples/xml_serializer_write_to_stream.py


Serializer Config
-----------------

.. literalinclude:: examples/xml_serializer_config.py

API :ref:`Reference <SerializerConfig>`.


Alternative Writers
-------------------

xsData ships with multiple writers based on lxml and native python.

.. literalinclude:: examples/xml_serializer_alternative_writer.py

:class:`~xsdata.formats.dataclass.serializers.writers.LxmlEventWriter`

It's based on the lxml `ElementTreeContentHandler`, which means your object tree
will first be converted to an lxml ElementTree and then to string. Despite that since
it's lxml it's still pretty fast and supports special characters and encodings a bit
better than the native python writer.

:class:`~xsdata.formats.dataclass.serializers.writers.XmlEventWriter`

It's based on the native python :class:`xml.sax.saxutils.XMLGenrator` with support for
indentation. The object tree is converted directly to string without any intermediate
steps, which makes it's slightly faster than the lxml implementation and more memory
efficient if you write directly to an output stream.

The pretty print output is identical to the lxml's except for some mixed content cases,
because of the nature of a sax content handler.


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
