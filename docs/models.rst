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

.. literalinclude:: examples/basic_model.py
    :lines: 9-26
    :language: python

.. literalinclude:: examples/basic_model.py
    :lines: 30-45
    :language: xml



Class Meta
==========

.. list-table::
   :widths: 20 10 300
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - name
     - str
     - The real name of the element this class represents.
   * - nillable
     - bool
     - Specifies whether an explicit empty value can be assigned, default: False
   * - namespace
     - str
     - The element xml namespace.


Field Typing
============

Simply follow the Python lib
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ documentation.


Field Metadata
==============

.. list-table::
   :widths: 20 10 250
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - name
     - str
     - The real name of the element or attribute this field represents.
   * - type
     - str
     - The field xml type: ``Text | Element | Attribute | Wildcard | Attributes``,
       default: ``Text`` or ``Element``
   * - nillable
     - bool
     - Specifies whether an explicit empty value can be assigned.
   * - mixed
     - bool
     - Specifies whether the field supports mixed content. ([#M1]_)
   * - sequential
     - bool
     - Specifies whether the field value(s) must appear in sequence with other
       sequential sibling fields. eg ``<a /><b /><a /><b />``
   * - tokens
     - bool
     - Use a list to map simple values.

       eg ``element: List[Union[int, bool, str]]
       -> <element>1 a true</element> -> [1, "a", True]``
   * - namespace
     - str
     - Specifies the field xml namespace. ([#M2]_)


The code generator adds also the field restrictions like `minLength` or `required` flag
but currently they are only used to troubleshoot the code generator.

.. [#M1] Mixed content must be combined ``Wildcard`` fields with type ``List[object]``.
    `w3schools <https://www.w3schools.com/xml/schema_complex_mixed.asp>`_

.. [#M2] It's a common practice in schema definitions to require elements to be
    qualified and attributes to be unqualified.

    ``Element`` fields with an omitted namespace inherit the namespace from the parent
    class/element and ``Attribute`` fields don't.

    If you need to break the namespace inheritance for ``Element`` fields set the
    namespace to an empty string ``namespace=""``.


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
a dictionary of. The wildcard namespace features also apply.

.. code-block:: python

    any_attributes: Dict = field(
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
