======================
Working with wildcards
======================


One of the xml schema traits is to support any extensions with wildcards.

.. code-block:: xml

    <xs:complexType name="MetadataType" mixed="false">
        <xs:sequence>
            <xs:any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>

The generator will roughly create this class for you.

.. doctest::

    >>> from dataclasses import dataclass
    >>> from dataclasses import field
    >>> from typing import Dict
    >>> from typing import List
    ...
    >>> @dataclass
    ... class MetadataType:
    ...     any_element: List[object] = field(
    ...         default_factory=list,
    ...         metadata={
    ...              "type": "Wildcard",
    ...              "namespace": "##any",
    ...          }
    ...     )
    ...     other_attributes: Dict[str, str] = field(
    ...          default_factory=dict,
    ...          metadata={
    ...              "type": "Attributes",
    ...              "namespace": "##other",
    ...          }
    ...      )


Generics
========

xsdata comes with two generic models that are used during parsing and you can also use
to generate any custom xml element.

.. list-table::
   :widths: 20 250
   :header-rows: 1

   * - Model
     - Description
   * - :class:`~xsdata.formats.dataclass.models.generics.AnyElement`
     - Used to represent any xml structure, resembles a DOM Element
   * - :class:`~xsdata.formats.dataclass.models.generics.DerivedElement`
     - Wrapper for type substitution elements eg `<b xsi:type="a">...</b>`


.. doctest::

    >>> from xsdata.formats.dataclass.models.generics import AnyElement
    >>> from xsdata.formats.dataclass.models.generics import DerivedElement
    >>> from xsdata.formats.dataclass.serializers import XmlSerializer
    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    ...
    >>> obj = MetadataType(
    ...     any_element=[
    ...         AnyElement(
    ...             qname="bar",
    ...             children=[
    ...                 AnyElement(qname="first", text="1st", attributes={"a": "1"}),
    ...                 AnyElement(qname="second", text="2nd", attributes={"b": "2"}),
    ...                 DerivedElement(
    ...                     qname="third",
    ...                     value=MetadataType(other_attributes={"c": "3"})
    ...                 )
    ...             ]
    ...         )
    ...     ]
    ... )
    >>> config = SerializerConfig(pretty_print=True, xml_declaration=False)
    >>> serializer = XmlSerializer(config=config)
    >>> print(serializer.render(obj))
    <MetadataType>
      <bar>
        <first a="1">1st</first>
        <second b="2">2nd</second>
        <third xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" c="3" xsi:type="MetadataType"/>
      </bar>
    </MetadataType>
    <BLANKLINE>


Mixed content
=============

For mixed content with known choices you can skip wrapping your instances with a
generic model. During data binding xsdata will try first to match one of the qualified
choices.

.. doctest::

    >>> @dataclass
    ... class Beta:
    ...     class Meta:
    ...         name = "beta"
    ...
    >>> @dataclass
    ... class Alpha:
    ...     class Meta:
    ...         name = "alpha"
    ...
    >>> @dataclass
    ... class Doc:
    ...     class Meta:
    ...         name = "doc"
    ...
    ...     content: List[object] = field(
    ...         default_factory=list,
    ...         metadata={
    ...             "type": "Wildcard",
    ...             "namespace": "##any",
    ...             "mixed": True,
    ...             "choices": (
    ...                 {
    ...                     "name": "a",
    ...                     "type": Alpha,
    ...                     "namespace": "",
    ...                 },
    ...                 {
    ...                     "name": "b",
    ...                     "type": Beta,
    ...                     "namespace": "",
    ...                 },
    ...             ),
    ...         }
    ...     )
    ...
    >>> obj = Doc(
    ...     content=[
    ...         Alpha(),
    ...         Beta(),
    ...     ]
    ... )
    ...
    >>> print(serializer.render(obj))
    <doc>
      <a/>
      <b/>
    </doc>
    <BLANKLINE>
