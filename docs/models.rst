***************
Models Metadata
***************

The code generator's default output format is python :mod:`python:dataclasses` and ships
with its own modules for xml and json marshalling.

The generated models don't depend on the xsdata library, except for specific xsd
data types that can't be mapped directly to python's builtin types. They only include
some metadata properties in order to control how the data structures are transferred
during data binding.


.. testsetup:: *

    from dataclasses import dataclass
    from dataclasses import field
    from decimal import Decimal
    from typing import List
    from xsdata.formats.dataclass.parsers import XmlParser


Basic Model
===========

.. testcode::

    @dataclass
    class Currency:
        id: int = field(metadata=dict(type="Attribute", name="ID"))
        name: str = field(metadata=dict(name="Name"))
        num_code: int = field(metadata=dict(name="NumCode"))
        iso_code: str = field(metadata=dict(name="CharCode"))
        nominal: int = field(metadata=dict(name="Nominal"))
        value: Decimal = field(metadata=dict(name="Value"))


    @dataclass
    class Currencies:
        class Meta:
            name = "ValCurs"

        date: str = field(metadata=dict(type="Attribute", name="Date"))
        name: str = field(metadata=dict(type="Attribute"))
        values: List[Currency] = field(default_factory=list, metadata=dict(name="Valute"))


    xml = """
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
    """

    obj = XmlParser().from_string(xml, Currencies)
    print(obj.values[1])

.. testoutput::

    Currency(id=44, name='US Dollar', num_code=840, iso_code='USD', nominal=1, value=Decimal('17.7177'))

Class Metadata
==============

Through the Meta class you can control the model's behaviour during data binding
procedures.

.. list-table::
   :widths: 20 10 300
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - name
     - str
     - The real/local name of the element this class represents.
   * - nillable
     - bool
     - Specifies whether this class can be initialized with no values
   * - namespace
     - str
     - The element xml namespace.
   * - target_namespace
     - str
     - Specify the element target namespace for auto type locator, if module namespace
       is not available or the type is not qualified.
   * - global_type
     - bool
     - Specify if the class represents a global discoverable type or that it can be used
       only as another class dependency, default: True
   * - element_name_generator
     - Callable
     - Element name generator
   * - attribute_name_generator
     - Callable
     - Attribute name generator


Field Typing
============

Simply follow the Python lib :mod:`python:dataclasses` documentation.

.. warning::

    Currently only List, Tuple, Dict and Union annotations are supported.
    Everything else will raise an exception as unsupported.



Support for generics in standard collections and the new union type was added
in v23.6


.. warning::

    You will get false positive errors from mypy if you are using compound fields.

    Mypy `issue <https://github.com/python/mypy/issues/13026>`_

    .. code-block::

        Value of type "Type[type]" is not indexable  [index]


Field Metadata
==============

Through the metadata properties you can control the field's behaviour during data
binding procedures.

.. list-table::
   :widths: 20 10 250
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - name
     - str
     - The real/local name of the element or attribute this field represents.
   * - type
     - str
     - The field xml type:
       ``Ignore | Text | Element | Elements | Attribute | Wildcard | Attributes``,
       default: ``Text`` or ``Element``
   * - nillable
     - bool
     - Specifies whether an explicit ``None`` value is allowed, default: False
   * - mixed
     - bool
     - Specifies whether the field supports mixed content. [#M1]_
   * - sequence
     - int
     - Specifies the sequence identifier of sibling fields
       eg ``<a /><b /><a /><b />``
   * - tokens
     - bool
     - Map the field value to a python sequence, [#M2]_
   * - namespace
     - str
     - Specifies the field xml namespace. [#M3]_
   * - format
     - str
     - Format option for types like datetime, or bytes, see :ref:`Data Types`


The code generator adds also the field restrictions like `minLength` or `required` flag
but currently they are only used to troubleshoot the code generator.

.. [#M1] Mixed content must be combined ``Wildcard`` fields with type ``List[object]``.
    `w3schools <https://www.w3schools.com/xml/schema_complex_mixed.asp>`_

.. [#M2] Declaration: ``List[Union[int, bool, str]]``

    Serialized value: ``<element>1 a true</element>``

    Parsed value: ``[1, "a", True]``

.. [#M3] It's a common practice in schema definitions to require elements to be
    qualified and attributes to be unqualified.

    ``Element`` fields with an omitted namespace inherit the namespace from the parent
    class/element and ``Attribute`` fields don't.

    If you need to break the namespace inheritance for ``Element`` fields set the
    namespace to an empty string ``namespace=""``.


Type: Ignore
~~~~~~~~~~~~

This type will force the internal xml context instance to ignore the field during
binding. Make sure your field is declared with `init=False` or with a default value
otherwise data binding will fail.


.. code-block:: python

    index: int = field(
        default_factory=int,
        init=False,
        metadata={"type": "Ignore"},
    )


Type: Element
~~~~~~~~~~~~~

This type represents a traditional xml element and can be the building block and
container for other elements, attributes, text or any combination of them.

.. code-block:: python

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "name": "annotation",
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2004/xml-schema-test-suite/",
        }
    )

.. code-block:: xml

    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
    <annotation xmlns="http://www.w3.org/2001/XMLSchema">...</annotation>
   ...

Type: Elements
~~~~~~~~~~~~~~

This type represents repeating xs:choice elements. It's a compound list field for
elements and wildcards that can be used to preserve elements ordering between data
marshalling.


.. code-block:: python

    node_or_id_or_idref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": Type["Node"],
                },
                {
                    "name": "e1",
                    "type": str,
                    "nillable": True,
                },
                {
                    "name": "e2",
                    "type": int,
                    "namespace": "xsdata",
                },
            ),
        }
    )

.. code-block:: xml

    <e1 xmlns="xsdata">a</e1>
    <e1 xmlns="xsdata">b</e1>
    <e2 xmlns="xsdata">1</e2>
    <e1 xmlns="xsdata">c</e1>
    <e2 xmlns="xsdata">2</e2>
   ...


**Choice Metadata**

.. list-table::
   :widths: 20 10 250
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - name
     - str
     - The real name of the element this choice represents.
   * - type
     - str
     - The field type hint.
   * - nillable
     - bool
     - Specifies whether an explicit empty value can be assigned.
   * - wildcard
     - bool
     - Specifies whether this is a ``Wildcard`` that can match any tag.
   * - tokens
     - bool
     - Map the field value to a python sequence
   * - namespace
     - str
     - Specifies the field xml namespace.
   * - format
     - str
     - Format option for types like datetime, or bytes, see :ref:`Data Types`
   * - default
     - Any
     - Default value
   * - default_factory
     - Any
     - Default value factory
   * - wrapper
     - str
     - The element name to wrap a collection of elements or primitives


.. warning::

    Compound fields preserve elements ordering but instead the direct element name
    association is lost during marshalling. If the choices include multiple elements
    with the same type then it's actually impossible to map correctly values to
    elements.

    For that reason the xml parser will use the generic class
    :class:`~xsdata.formats.dataclass.models.generics.DerivedElement` to wrap values
    in order to maintain the original qualified name as well.

    If your compound field includes only unique types and you are working with a
    dataclass instance manually you can skip the usage of the wrapper as the xml
    serializer will try to match a type to a choice as well.

    ``obj.node_or_id_or_idref.extend(("a", "b", 1, "c", "2"))``


Type: Attribute
~~~~~~~~~~~~~~~

This type represents a traditional xml attribute.

.. code-block:: python

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "lang",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace"
        }
    )

.. code-block:: xml

    <root xmlns:xml="http://www.w3.org/XML/1998/namespace" xml:lang="en">


Type: Wildcard
~~~~~~~~~~~~~~

This type represents ``xs:any`` elements or elements with type ``xs:AnyType``.
Wildcards can have a normal uri namespace or use one of xml schema generics.

.. list-table::
   :widths: 25 220
   :header-rows: 1

   * - Namespace
     - Description
   * - ##any
     - element from any namespace is allowed
   * - ##other
     - element from any namespace other than the parent's namespace
   * - ##local
     - element must come from no namespace
   * - ##targetNamespace
     - element from the namespace of the parent can be present


.. code-block:: python

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )

This type of field accepts any primitive value or an another dataclass instance or a
generic :class:`~xsdata.formats.dataclass.models.generics.AnyElement` instance.

This type optionally can have a list of acceptable elements similar to compound fields,
otherwise during binding the parsers will try to find a suitable model automatically.

Type: Attributes
~~~~~~~~~~~~~~~~

This type represents ``xs:anyAttribute`` elements. It needs to be defined as
a dictionary of. The wildcard namespace features also apply.

.. code-block:: python

    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other"
        }
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


.. hint::

    Check the :ref:`examples <Examples>` for more advanced topics.
