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


From json filename
------------------

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


From json file object
---------------------

.. doctest::

    >>> json_path = fixtures_dir.joinpath("defxmlschema/chapter05.json")
    >>> with json_path.open("rb") as fp:
    ...     order = parser.parse(fp, Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From json stream
----------------

.. doctest::

    >>> import io
    >>> order = parser.parse(io.BytesIO(json_path.read_bytes()), Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From json string
----------------

.. doctest::

    >>> order = parser.from_string(json_path.read_text(), Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From json bytes
---------------

.. doctest::

    >>> order = parser.from_bytes(json_path.read_bytes(), Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


From json path
--------------

.. doctest::

    >>> order = parser.from_path(json_path, Order)
    >>> order.items.product[0]
    Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=None, system=None))


Unknown json target type
------------------------

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

.. doctest::

    >>> from tests.fixtures.books import *  # Import all classes
    >>> json_string = """{
    ...   "author": "Hightower, Kim",
    ...   "title": "The First Book",
    ...   "genre": "Fiction",
    ...   "price": 44.95,
    ...   "pub_date": "2000-10-01",
    ...   "review": "An amazing story of nothing.",
    ...   "id": "bk001"
    ... }"""
    >>> parser = JsonParser()
    >>> parser.from_string(json_string)
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


List of Objects
---------------

Specify the target binding type to ``List[ModelName]``

.. doctest::

    >>> from typing import List
    >>>
    >>> json_string = """[
    ...     {
    ...       "author": "Hightower, Kim",
    ...       "title": "The First Book",
    ...       "genre": "Fiction",
    ...       "price": 44.95,
    ...       "pub_date": "2000-10-01",
    ...       "review": "An amazing story of nothing.",
    ...       "id": "bk001"
    ...     },
    ...     {
    ...       "author": "Nagata, Suanne",
    ...       "title": "Becoming Somebody",
    ...       "genre": "Biography",
    ...       "price": null,
    ...       "pub_date": null,
    ...       "review": "A masterpiece of the fine art of gossiping.",
    ...       "id": "bk002"
    ...     }
    ...   ]"""
    >>> parser = JsonParser()
    >>> books = parser.from_string(json_string, List[BookForm])
    >>> books[1].author
    'Nagata, Suanne'


Custom json load factory
------------------------

The default factory is python's builtin :func:`python:json.load` but you can use any
other implementation as long as it's has a compatible signature.

.. code-block:: python

    import ujson

    parser = JsonParser(load_factory=ujson.load)


Serializing JSON
================


Render json string
------------------

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


Write to json stream
--------------------

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
