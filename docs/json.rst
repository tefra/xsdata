============
JSON Binding
============


:class:`~xsdata.formats.dataclass.parsers.JsonParser`
=====================================================

The parser has three instance methods `from_string`, `from_bytes` and `from_path`,
to parse from memory or to let the parser load the input document.

.. hint::

    You can optionally specify the target binding class or let the context instance
    to scan all imported modules for a matching dataclass.

**Parameters**
    **context** (:class:`~xsdata.formats.dataclass.context.XmlContext`)

    The cache layer for the binding directives of models and their fields. You may
    share a context instance between parser/serializer instances to avoid compiling the
    cache more than once.

    .. hint::

        it's recommended to use a static or global instance of your parser or serializer
        per document type.

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
that needs to extends :py:class:`json.JSONEncoder` and a dict_factory with your custom
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
