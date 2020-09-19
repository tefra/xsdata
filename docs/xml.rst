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

The cache layer for the binding directives of models and their fields. You may
share a context instance between parser/serializer instances to avoid compiling the
cache more than once.

.. hint::

    it's recommended to use a static or global instance of your parser or serializer
    per document type.


**handler** (:class:`type` of
:class:`~xsdata.formats.dataclass.parsers.mixins.XmlHandler`)

The XmlHandler type to use in order to read the xml source and push element events
to the main parser.

Default: :class:`~xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler`


Handlers
--------

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


Example: from path
------------------

.. literalinclude:: examples/xml_parser.py
   :lines: 3-6,7-17


Example: from memory
--------------------

With support for `XML Inclusions <https://www.w3.org/TR/xinclude-11/>`_

.. literalinclude:: examples/xml_parser.py
   :lines: 19-22


Example: alternative handler
----------------------------

.. literalinclude:: examples/xml_parser.py
   :lines: 24-27


:class:`~xsdata.formats.dataclass.serializers.XmlSerializer`
============================================================

The serializer can also be initialized with a xml context instance, if your use case
needs to parse and serialize the same type of objects you could share the same xml
context instance between them to save on memory and processing.

.. hint::

    The serializer used to add a default namespace if the root object supported it and
    moved all the prefixes to the root node with a performance penalty. This behavior
    was removed in version **20.10** with the new xml writer interface for consistency
    between implementations.

    You can still get the same output if you provide a prefix-URI namespaces mapping,
    see :ref:`examples <Example: custom prefixes>`


Parameters
----------

**encoding** (:class:`str`)

text encoding, default: `UTF-8`


**pretty_print** (:class:`bool`)

Enable pretty output, default: `False`


**context** (:class:`~xsdata.formats.dataclass.context.XmlContext`)

The cache layer for the binding directives of models and their fields. You may
share a context instance between parser/serializer instances to avoid compiling the
cache more than once.


**writer** (:class:`type` of
:class:`~xsdata.formats.dataclass.serializers.mixins.XmlWriter`)

The XmlWriter type to use for serialization.

Default: :class:`~xsdata.formats.dataclass.serializers.writers.LxmlEventWriter`


Writers
-------

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

Example: render
---------------

.. literalinclude:: examples/xml_serializer.py
    :lines: 4-23

.. literalinclude:: examples/xml_serializer.py
    :lines: 26-36
    :language: xml

Example: custom prefixes
------------------------

.. literalinclude:: examples/xml_serializer.py
    :lines: 40

.. literalinclude:: examples/xml_serializer.py
    :lines: 43-45
    :language: xml

Example: default prefix
-----------------------

.. literalinclude:: examples/xml_serializer.py
    :lines: 57

.. literalinclude:: examples/xml_serializer.py
    :lines: 60-63
    :language: xml

Example: native handler
-----------------------

.. literalinclude:: examples/xml_serializer.py
    :lines: 73-75

.. literalinclude:: examples/xml_serializer.py
    :lines: 78-88
    :language: xml

Example: write to stream
------------------------

.. literalinclude:: examples/xml_serializer.py
    :lines: 91

.. literalinclude:: examples/xml_serializer.py
    :lines: 93-94


Benchmarks
==========

The benchmarks run with the `test suite <https://travis-ci.com/tefra/xsdata>`_.

.. code-block::

    ------------------------------------- benchmark 'Parse: 100 books': 4 tests -------------------------------------
    Name (time in ms)                          Min                Max               Mean             Median
    -----------------------------------------------------------------------------------------------------------------
    test_parse_small[XmlEventHandler]      11.6160 (1.0)      12.6287 (1.00)     11.8553 (1.0)      11.7856 (1.0)
    test_parse_small[LxmlEventHandler]     11.7612 (1.01)     12.5831 (1.0)      12.0762 (1.02)     12.0272 (1.02)
    test_parse_small[LxmlSaxHandler]       12.7282 (1.10)     13.8885 (1.10)     12.9998 (1.10)     12.9255 (1.10)
    test_parse_small[XmlSaxHandler]        15.7504 (1.36)     17.0763 (1.36)     15.9986 (1.35)     15.9235 (1.35)
    -----------------------------------------------------------------------------------------------------------------

    --------------------------------------- benchmark 'Parse: 1000 books': 4 tests ---------------------------------------
    Name (time in ms)                            Min                 Max                Mean              Median
    ----------------------------------------------------------------------------------------------------------------------
    test_parse_medium[XmlEventHandler]      111.9098 (1.0)      113.9331 (1.0)      112.5547 (1.0)      112.6175 (1.0)
    test_parse_medium[LxmlEventHandler]     113.8048 (1.02)     116.0534 (1.02)     114.9485 (1.02)     115.0780 (1.02)
    test_parse_medium[LxmlSaxHandler]       126.1686 (1.13)     127.6716 (1.12)     126.9943 (1.13)     127.1551 (1.13)
    test_parse_medium[XmlSaxHandler]        153.4598 (1.37)     155.4510 (1.36)     154.3693 (1.37)     154.2699 (1.37)
    ----------------------------------------------------------------------------------------------------------------------

    ---------------------------------- benchmark 'Parse: 10000 books': 4 tests ----------------------------------
    Name (time in s)                          Min               Max              Mean            Median
    -------------------------------------------------------------------------------------------------------------
    test_parse_large[XmlEventHandler]      1.1246 (1.0)      1.1373 (1.0)      1.1300 (1.0)      1.1262 (1.0)
    test_parse_large[LxmlEventHandler]     1.1360 (1.01)     1.1446 (1.01)     1.1391 (1.01)     1.1383 (1.01)
    test_parse_large[LxmlSaxHandler]       1.2642 (1.12)     1.2809 (1.13)     1.2734 (1.13)     1.2729 (1.13)
    test_parse_large[XmlSaxHandler]        1.5376 (1.37)     1.5614 (1.37)     1.5473 (1.37)     1.5452 (1.37)
    -------------------------------------------------------------------------------------------------------------

    ------------------------------------ benchmark 'Serialize: 100 books': 2 tests -------------------------------------
    Name (time in ms)                             Min                Max               Mean             Median
    --------------------------------------------------------------------------------------------------------------------
    test_serialize_small[LxmlEventWriter]     13.2771 (1.0)      15.2824 (1.02)     14.3202 (1.02)     14.2914 (1.02)
    test_serialize_small[XmlEventWriter]      13.6682 (1.03)     14.9772 (1.0)      14.0417 (1.0)      13.9851 (1.0)
    --------------------------------------------------------------------------------------------------------------------

    --------------------------------------- benchmark 'Serialize: 1000 books': 2 tests --------------------------------------
    Name (time in ms)                               Min                 Max                Mean              Median
    -------------------------------------------------------------------------------------------------------------------------
    test_serialize_medium[LxmlEventWriter]     126.2678 (1.0)      167.3845 (1.27)     133.7267 (1.03)     128.5200 (1.0)
    test_serialize_medium[XmlEventWriter]      127.9384 (1.01)     131.6320 (1.0)      129.4039 (1.0)      129.1908 (1.01)
    -------------------------------------------------------------------------------------------------------------------------

    --------------------------------- benchmark 'Serialize: 10000 books': 2 tests ----------------------------------
    Name (time in s)                             Min               Max              Mean            Median
    ----------------------------------------------------------------------------------------------------------------
    test_serialize_large[XmlEventWriter]      1.2516 (1.0)      1.2590 (1.0)      1.2550 (1.0)      1.2548 (1.0)
    test_serialize_large[LxmlEventWriter]     1.2762 (1.02)     1.2840 (1.02)     1.2793 (1.02)     1.2766 (1.02)
    ----------------------------------------------------------------------------------------------------------------
