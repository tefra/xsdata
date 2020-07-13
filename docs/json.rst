============
JSON Binding
============

The json implementation lacks a bit in maturity and code coverage but it has a similar
interface to the xml implementation.


:class:`~xsdata.formats.dataclass.parsers.JsonParser`
=====================================================

The parser also uses the :class:`~xsdata.formats.dataclass.context.XmlContext`
for model metadata caching which can be shared across instances.

.. code-block:: python

    >>> from xsdata.formats.dataclass.parsers import JsonParser
    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from tests.fixtures.defxmlschema.chapter05 import Order
    >>> from pathlib import Path
    >>>
    >>> parser = JsonParser(context=XmlContext())
    >>> parser.from_path(Path("../tests/fixtures/defxmlschema/chapter04.json"), Order)
    Order(items=ItemsType(product=[Product(number=557, name='Short-Sleeved Linen Blouse', size=SizeType(value=10, system='US-DRESS'))]))



:class:`~xsdata.formats.dataclass.serializers.JsonSerializer`
=============================================================

The serializer besides the `indent` option can be initialized with a custom encoder
that needs to extends :py:class:`json.JSONEncoder` and a dict_factory with any custom
logic.


Example: dict factory that filters None values.

.. code-block:: python

    >>> from xsdata.formats.dataclass.serializers import JsonSerializer
    >>>
    >>> serializer = JsonSerializer(indent=2, dict_factory=lambda x: {k: v for k, v in x if v is not None})
    >>> pprint.pprint(serializer.render(obj))
    >>> ('{\n'
    >>>  '  "items": {\n'
    >>>  '    "product": [\n'
    >>>  '      {\n'
    >>>  '        "number": 557,\n'
    >>>  '        "name": "Short-Sleeved Linen Blouse",\n'
    >>>  '        "size": {\n'
    >>>  '          "value": 10,\n'
    >>>  '          "system": "US-DRESS"\n'
    >>>  '        }\n'
    >>>  '      }\n'
    >>>  '    ]\n'
    >>>  '  }\n'
    >>>  '}')
