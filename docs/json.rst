============
JSON Binding
============

Binding JSON lacks a bit in features and for edge cases with wildcards and derived
types doing roundtrip conversions is not always possible.

.. testsetup:: *

    from pathlib import Path
    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import JsonParser
    from tests import fixtures_dir
    from tests.fixtures.defxmlschema.chapter05 import Order, ItemsType
    from tests.fixtures.defxmlschema.chapter05prod import Product, SizeType

    json_path = fixtures_dir.joinpath("defxmlschema/chapter05.json")
    parser = JsonParser(context=XmlContext())
    order = Order(
        items=ItemsType(
            product=[
                Product(
                    number=557,
                    name='Short-Sleeved Linen Blouse',
                    size=SizeType(value=None, system=None)
                )
            ]
        )
    )

Parsing JSON
============

From Path
---------

.. doctest::

    >>> from pathlib import Path
    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.parsers import JsonParser
    >>> from tests import fixtures_dir
    >>> from tests.fixtures.defxmlschema.chapter05 import Order
    ...
    >>> json_path = fixtures_dir.joinpath("defxmlschema/chapter05.json")
    >>> parser = JsonParser(context=XmlContext())
    >>> order = parser.from_path(json_path, Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From String
-----------

.. doctest::

    >>> order = parser.from_string(json_path.read_text(), Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From Bytes
----------

.. doctest::

    >>> order = parser.from_bytes(json_path.read_bytes(), Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


Unknown target type
-------------------

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

.. doctest::

    >>> order = parser.from_bytes(json_path.read_bytes())
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


Serializing JSON
================

Render to string
----------------

.. doctest::

    >>> from xsdata.formats.dataclass.serializers import JsonSerializer
    >>> from tests.fixtures.defxmlschema.chapter05 import Order, ItemsType
    >>> from tests.fixtures.defxmlschema.chapter05prod import Product, SizeType
    >>> order = Order(
    ...     items=ItemsType(
    ...         product=[
    ...             Product(
    ...                 number=557,
    ...                 name='Short-Sleeved Linen Blouse',
    ...                 size=SizeType(value=None, system=None)
    ...             )
    ...         ]
    ...     )
    ... )
    >>> serializer = JsonSerializer(indent=2)
    >>> print(serializer.render(order))
    {
      "items": {
        "product": [
          {
            "number": 557,
            "name": "Short-Sleeved Linen Blouse",
            "size": {
              "value": null,
              "system": null
            }
          }
        ]
      }
    }


Custom Dict factory
-------------------

You can override the default dict factory to do extra steps like filtering `None`
values.

.. doctest::

    >>> def filter_none(x):
    ...     return {k: v for k, v in x if v is not None}
    ...
    >>> serializer = JsonSerializer(indent=2, dict_factory=filter_none)
    >>> print(serializer.render(order))
    {
      "items": {
        "product": [
          {
            "number": 557,
            "name": "Short-Sleeved Linen Blouse",
            "size": {}
          }
        ]
      }
    }
