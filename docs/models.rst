******
Models
******

Dataclasses is the default output format for the code generator and ships with its own
modules for xml and json marshalling. The generated models are simple python
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ with some optional
metadata to control how the data structures are transferred during data binding.

If you are working with xml documents that don't have any schema definition you can
create these models manually.


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

Simply follow the Python lib
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ documentation.


Field Metadata
==============

.. csv-table::
   :header: "Property", "Type", "Description"
   :widths: 20, 10, 300

   "name", "str", "The real name of the element or attribute this field represents."
   "type", "str", "The field type: Text | Element | Attribute | Wildcard | Attributes, default: Text"
   "nillable", "bool", "Enable of disable rendering with an empty value."
   "sequential", "bool", "Enable rendering group of lists values in sequence. eg ``<a /><b /><a /><b />``"
   "namespace", "str", "The element/attribute xml namespace."

It's a common practice in schema definitions to require elements to be qualified and
attributes to be unqualified. ``Element`` fields with an omitted namespace inherit the
namespace from the parent class/element and ``Attribute`` fields don't.

If you need to break the namespace inheritance for ``Element`` fields set the namespace
to an empty string ``namespace=""``.


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

This type is represents ``xs:any`` elements or elements with type ``xs:AnyType``.
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

This type represents ``xs:anyAttribute`` elements. It needs to be defined as
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

This is the default field type and represents any atomic value. The value of this field
is directly assigned as text to elements.



.. code-block:: python

    @dataclass
    class Root:
        class Meta:
            name = "root"

        value: Optional[int] = field(default=None)


.. code-block:: xml

    <root>2020</root>