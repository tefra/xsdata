============
Wrapped List
============

XML data structures commonly wrap element and primitive collections.
For instance, a library may have several books and and other stuff as well.
In terms of `OpenAPI 3 <https://swagger.io/specification/#xml-object>`_,
these data structures are `wrapped`. Hence, xsdata has the field parameter `wrapper`,
which wraps any element/primitive collection into a custom xml element without the
need of a dedicated wrapper class.

.. doctest::

    >>> from dataclasses import dataclass, field
    >>> from typing import List
    >>> from xsdata.formats.dataclass.serializers import XmlSerializer
    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    >>>
    >>> config = SerializerConfig(pretty_print=True, xml_declaration=False)
    >>> serializer = XmlSerializer(config=config)
    >>>
    >>> @dataclass
    ... class Library:
    ...     books: List[str] = field(
    ...         metadata={
    ...             "wrapper": "Books",
    ...             "name": "Title",
    ...             "type": "Element",
    ...         }
    ...     )
    ...
    >>> obj = Library(
    ...     books = [
    ...         "python for beginners",
    ...         "beautiful xml",
    ...     ]
    ... )
    >>>
    >>> print(serializer.render(obj))
    <Library>
      <Books>
        <Title>python for beginners</Title>
        <Title>beautiful xml</Title>
      </Books>
    </Library>
    <BLANKLINE>
