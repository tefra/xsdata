===========
XML Binding
===========


:class:`~xsdata.formats.dataclass.parsers.XmlParser`
====================================================

You may initialize the alter the default parser behaviour with a config and xml
context instances.

The :class:`~xsdata.formats.dataclass.context.XmlContext` is a cache layer for the
models and the field definitions and how they should be mapped to xml document elements
and attributes. You can share this between xml parser instances to avoid compiling the
models metadata more than once. Although it makes for sense to have a static instance
of the parser per document type.

The parser instance has three input methods `from_string`, `from_bytes` and `from_path`,
to parse from memory or to let the parser load the input document, All of them require
the target class Type to bind the input data.

Example: from path
------------------

.. code-block:: python

    >>> from xsdata.formats.dataclass.parsers import XmlParser
    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig

    >>> config = ParserConfig(fail_on_unknown_properties=True)
    >>> parser = XmlParser(config=config)
    >>> order = parser.from_path("docs/examples/primer.xml", PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=95819.0, country='US')


Example: from memory
--------------------

With support for `XML Inclusions <https://www.w3.org/TR/xinclude-11/>`_

.. code-block:: python

    >>> path = fixtures_dir.joinpath("books/books-xinclude.xml")
    >>> config = ParserConfig(process_xinclude=True, base_url=path.as_uri())
    >>> parser = XmlParser(config=config)
    >>> actual = parser.from_bytes(path.read_bytes(), Books)



:class:`~xsdata.formats.dataclass.parsers.config.ParserConfig`
--------------------------------------------------------------

.. csv-table::
   :header: "Name", "Type", "Description"
   :widths: 20, 10, 200

    "base_url", "str", "A base URL for when parsing from memory and you want support for relative links eg xinclude, default: ``None``"
    "process_xinclude", "bool", "Process xinclude statements. , default: ``False``"
    "fail_on_unknown_properties", "bool", "Should fail on unknown properties that can't be mapped to any wildcard field, default: ``True``"


:class:`~xsdata.formats.dataclass.serializers.XmlSerializer`
============================================================

The serializer can also me initialized with a xml context instance, if your use case
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
