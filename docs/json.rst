============
JSON Binding
============

Binding JSON lacks a bit in features and for edge cases with wildcards and derived
types doing roundtrip conversions is not always possible.

.. testsetup:: *

    import io
    from pathlib import Path
    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import JsonParser
    from tests import fixtures_dir
    from tests.fixtures.defxmlschema.chapter05 import Order, ItemsType
    from tests.fixtures.defxmlschema.chapter05prod import Product, SizeType


Parsing JSON
============


From filename
-------------

.. doctest::

    >>> from pathlib import Path
    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.parsers import JsonParser
    >>> from tests import fixtures_dir # pathlib.Path
    >>> from tests.fixtures.defxmlschema.chapter05 import Order
    ...
    >>> filename = str(fixtures_dir.joinpath("defxmlschema/chapter05.json"))
    >>> parser = JsonParser(context=XmlContext())
    >>> order = parser.parse(filename, Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From file object
----------------

.. doctest::

    >>> json_path = fixtures_dir.joinpath("defxmlschema/chapter05.json")
    >>> with json_path.open("rb") as fp:
    ...     order = parser.parse(fp, Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From stream
-----------

.. doctest::

    >>> import io
    >>> order = parser.parse(io.BytesIO(json_path.read_bytes()), Order)
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


From path
---------

.. doctest::

    >>> order = parser.from_path(json_path, Order)
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


Custom json load factory
------------------------

The default factory is python's builtin :func:`python:json.load` but you can use any
other implementation as long as it's has a compatible signature.

.. code-block:: python

    import ujson

    parser = JsonParser(load_factory=ujson.load)


Serializing JSON
================


Render to string
----------------

.. doctest::

    >>> from xsdata.formats.dataclass.context import XmlContext
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
    >>> serializer = JsonSerializer(context=XmlContext(), indent=2)
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


Write to stream
---------------

.. doctest::

    >>> from pathlib import Path
    ...
    >>> path = Path("output.json")
    >>> with path.open("w") as fp:
    ...     serializer.write(fp, order)
    ...
    >>> print(path.read_text())
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
    >>> path.unlink()


Custom Dict factory
-------------------

By using a custom dict factory you can change the output behaviour, like filter out
``None`` values.

.. doctest::

    >>> from typing import Dict, Tuple
    >>>
    >>> def filter_none(x: Tuple) -> Dict:
    ...     return {k: v for k, v in x if v is not None}
    >>>
    >>> order.items.product[0].size = None
    >>> serializer = JsonSerializer(dict_factory=filter_none, indent=2)
    >>> print(serializer.render(order))
    {
      "items": {
        "product": [
          {
            "number": 557,
            "name": "Short-Sleeved Linen Blouse"
          }
        ]
      }
    }

or conveniently

.. doctest::

    >>> from xsdata.formats.dataclass.serializers.json import DictFactory
    >>>
    >>> serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)
    >>> print(serializer.render(order))
    {"items": {"product": [{"number": 557, "name": "Short-Sleeved Linen Blouse"}]}}


Custom json dump factory
------------------------

The default factory is python's builtin :func:`python:json.dump` but you can use any
other implementation as long as it's has a compatible signature.

.. code-block:: python

    import ujson

    serializer = JsonSerializer(dump_factory=ujson.dump, indent=0)
