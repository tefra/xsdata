***********
Dataclasses
***********

Dataclasses is the default ouput format for the code generator and ships with its own
xml/json modules. If your api doesn't come with a definition you can create these models
easily on your own.

The models are simple python `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_
with some optional metadata properties used for marshalling data.


Basic Model
===========

.. code-block:: python

    @dataclass
    class Currency:
        id: int = field(metadata=dict(type="Attribute", name="ID"))
        name: str = field(metadata=dict(type="Attribute", name="Name"))
        num_code: int = field(metadata=dict(type="Element", name="NumCode"))
        iso_code: str = field(metadata=dict(type="Element", name="CharCode"))
        nominal: int = field(metadata=dict(type="Element", name="Nominal"))
        value: Decimal = field(metadata=dict(type="Element", name="Value"))


    @dataclass
    class Currencies:
        class Meta:
            name = "ValCurs"

        date: str = field(metadata=dict(type="Attribute", name="Date"))
        name: str = field(metadata=dict(type="Attribute"))
        values: List[Currency] = field(default_factory=list, metadata=dict(type="Element", name="Valute"))



.. code-block:: xml

    <ValCurs Date="19.04.2020" name="Official exchange rate">
        <Valute ID="47">
            <NumCode>978</NumCode>
            <CharCode>EUR</CharCode>
            <Nominal>1</Nominal>
            <Name>Euro</Name>
            <Value>19.2743</Value>
        </Valute>
        <Valute ID="44">
            <NumCode>840</NumCode>
            <CharCode>USD</CharCode>
            <Nominal>1</Nominal>
            <Name>US Dollar</Name>
            <Value>17.7177</Value>
        </Valute>
    </ValCurs>


Class Meta
==========

.. csv-table::
   :header: "Property", "Type", "Description"
   :widths: 20, 10, 300

   "name", "str", "The real name of the element this class represents."
   "nillable", "bool", "Enable of disable rendering empty elements, default: False"
   "namespace", "str", "The element xml namespace."


Field Typing
============

Simply follow the Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ documentation.


Field Metadata
==============

.. csv-table::
   :header: "Property", "Type", "Description"
   :widths: 20, 10, 300

   "name", "str", "The real name of the element or attribute this field represents."
   "nillable", "bool", "Enable of disable rendering with an empty value."
   "sequential", "bool", "Enable rendering group of lists values in sequence. eg ``<a /><b /><a /><b />``"
   "namespace", "str", "The element/attribute xml namespace."
   "type", "str", "The field type: Text | Element | Attribute | Wildcard | Attributes, default: Text"

It's a common practice in schema definitions to require elements to be qualified and attributes to be unqualified.

In regards to that when an ``Element`` field has namespace set to ``None`` it will
inherit the class namespace, to override this behaviour set the namespace to an empty
string.

Type: Element
~~~~~~~~~~~~~

This type represents a traditional xml element and can be the building block and
container for other elements, attributes, text or any combination of them.

.. code-block:: python

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            namespace="http://www.w3.org/XML/2004/xml-schema-test-suite/",
        )
    )

.. code-block:: xml

    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
   ...

Type: Attribute
~~~~~~~~~~~~~~~

This type represents a traditional xml attribute.

.. code-block:: python

    language: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )

.. code-block:: xml

    <root xmlns:xml="http://www.w3.org/XML/1998/namespace" xml:lang="en">

Type: Wildcard
~~~~~~~~~~~~~~

This type is used to represent  ``xs:any`` elements or elements with type ``xs:AnyType``.

Wildcards can have normal uri namespace or use one of xml schema generics.


.. csv-table::
   :header: "Namespace", "Description"
   :widths: 20, 200

    "##any", "element from any namespace is allowed"
    "##other", "element from any namespace other than the parent element's namespace"
    "##local", "element must come from no namespace"
    "##targetNamespace", "element from the namespace of the parent element can be present"


.. code-block:: python

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
        )
    )

This type of field accepts any primitive value or an another dataclass instance or a
generic :class:`~xsdata.formats.dataclass.models.generics.AnyElement` instance.


Type: Attributes
~~~~~~~~~~~~~~~~

This type is used to represent ``xs:anyAttribute`` elements. It needs to be defined as
a dictionary with key an :class:`lxml.etree.QName` and string values. The wildcard
namespace features also apply.

.. code-block:: python

    any_attributes: Dict[lxml.etree.QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )

Type: Text
~~~~~~~~~~

This is the default xsdata field type and represents any atomic value. The value of
this field is directly assign as text to elements.



.. code-block:: python

    @dataclass
    class Root:
        class Meta:
            name = "root"

        value: Optional[int] = field(default=None)


.. code-block:: p

    <root>2020</root>


XML Format
==========

The :class:`~xsdata.formats.dataclass.parsers.XmlParser` has three input methods
file path, string or bytes. All of them require the target class Type to bind the input
data.

The parser internally depends on lxml's iterparse event stream to bind the raw input
data to dataclasses and primitive types.

.. code-block:: python

    >>> from xsdata.formats.dataclass.parsers import XmlParser

    >>> parser = XmlParser()
    >>> order = parser.from_path("docs/examples/primer.xml", PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=95819.0, country='US')



The :class:`~xsdata.formats.dataclass.serializers.XmlSerializer`

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


JSON Format
===========

JSON format is mostly used internally for tests because I had a lot of json fixtures.

It's a bit behind in features and maturity compared to the xml format.


:class:`xsdata.formats.dataclass.serializers.JsonSerializer`


.. code-block:: python

    from xsdata.formats.dataclass.serializers import JsonSerializer

    serializer = JsonSerializer(indent=2, dict_factory=DictFactory.FILTER_NONE)



:class:`xsdata.formats.dataclass.parsers.JsonParser`

.. code-block:: python

    from xsdata.formats.dataclass.parsers import JsonParser

    obj = parser.from_path("/some.json, PurchaseOrder)



Data Types
==========

In table below you case find all the xml schema data types and their mapping to
primitive python types.

+---------+------------------------------------------------------------------------------------+
| Python  | XML Schema Types                                                                   |
+---------+----------------------+-----------------+----------------------+--------------------+
| str     |               anyURI |   anySimpleType |                 base |       base64Binary |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |                 date |        dateTime |    derivationControl |           duration |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |                 gDay |          gMonth |            gMonthDay |              gYear |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |          gYearMonth  |              ID |                IDREF |          hexBinary |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |               IDREFS |            lang |             language |               Name |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |               NCName |         NMTOKEN |             NMTOKENS |   normalizedString |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |             NOTATION |           QName | simpleDerivationSet  |             string |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |                 time |           token |                      |                    |
+---------+----------------------+-----------------+----------------------+--------------------+
| bool    |              boolean |                 |                      |                    |
+---------+----------------------+-----------------+----------------------+--------------------+
| int     |                 byte |        ENTITIES |               ENTITY |                int |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |              integer |            long |     negativeInteger  | nonNegativeInteger |
+---------+----------------------+-----------------+----------------------+--------------------+
|         | nonPositiveInteger   | positiveInteger |                short |       unsignedByte |
+---------+----------------------+-----------------+----------------------+--------------------+
| float   |               double |           float |                      |                    |
+---------+----------------------+-----------------+----------------------+--------------------+
| Decimal |              decimal |                 |                      |                    |
+---------+----------------------+-----------------+----------------------+--------------------+
|         |                      |                 |                      |                    |
+---------+----------------------+-----------------+----------------------+--------------------+
