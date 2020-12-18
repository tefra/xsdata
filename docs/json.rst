============
JSON Binding
============

Binding JSON lacks a bit in features and for edge cases with wildcards and derived
types doing roundtrip conversions is not always possible.

Parsing JSON
============

From Path
---------

.. literalinclude:: examples/json_parser_from_path.py

From String
-----------

.. literalinclude:: examples/json_parser_from_string.py

From Bytes
----------

.. literalinclude:: examples/json_parser_from_bytes.py

Unknown target type
-------------------

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

.. literalinclude:: examples/json_parser_unknown_target.py

Serializing JSON
================

Render to string
----------------

.. literalinclude:: examples/json_serializer_basic.py
    :lines: 1-5

.. literalinclude:: examples/json_serializer_basic.py
    :language: json
    :lines: 7-20

Custom Dict factory
-------------------

You can override the default dict factory to do extra steps like filtering `None`
values.

.. literalinclude:: examples/json_serializer_custom_factory.py
    :lines: 7-12

.. literalinclude:: examples/json_serializer_custom_factory.py
    :language: json
    :lines: 14-24
