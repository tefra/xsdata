Data Class: pydata
==================


Generate Python Data Classes with type hints grouped in the same modules by the original schema.

This is the default format and also comes with parsers and serializers for both xml and json.


.. admonition:: XSD Types mapping
    :class: hint

    .. code-block:: python

            str:
                anyURI     anySimpleType base                base64Binary
                date       dateTime      derivationControl   duration
                gDay       gMonth        gMonthDay           gYear
                gYearMonth hexBinary     ID                  IDREF
                IDREFS     lang          language            Name
                NCName     NMTOKEN       NMTOKENS            normalizedString
                NOTATION   QName         simpleDerivationSet string
                time       token

            bool:
                boolean

            int:
                byte               ENTITIES        ENTITY          int
                integer            long            negativeInteger nonNegativeInteger
                nonPositiveInteger positiveInteger short           unsignedByte
                unsignedInt        unsignedLong    unsignedShort

            float:
                decimal            double          float


XmlSerializer
^^^^^^^^^^^^^

:class:`xsdata.formats.dataclass.serializers.XmlSerializer`

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


XmlParser
^^^^^^^^^

:class:`xsdata.formats.dataclass.parsers.XmlParser`

.. code-block:: python

    >>> from xsdata.formats.dataclass.parsers import XmlParser

    >>> parser = XmlParser()
    >>> order = parser.from_path("docs/examples/primer.xml", PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=95819.0, country='US')



JsonSerializer
^^^^^^^^^^^^^^

:class:`xsdata.formats.dataclass.serializers.JsonSerializer`


.. code-block:: python

    from xsdata.formats.dataclass.serializers import JsonSerializer

    serializer = JsonSerializer(indent=2, dict_factory=DictFactory.FILTER_NONE)


JsonParser
^^^^^^^^^^

:class:`xsdata.formats.dataclass.parsers.JsonParser`

.. code-block:: python

    from xsdata.formats.dataclass.parsers import JsonParser

    obj = parser.from_path("/some.json, PurchaseOrder)
