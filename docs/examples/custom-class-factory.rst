====================
Custom class factory
====================


The philosophy behind xsdata is to have plain objects without additional methods and
logic. If you need an entry point to add any pre/post initialization logic or even
validations you can use the parser config to override the default class factory.


.. doctest::

    >>> from dataclasses import dataclass
    >>> from xsdata.formats.dataclass.parsers import JsonParser
    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig
    ...
    >>> def custom_class_factory(clazz, params):
    ...     if clazz.__name__ == "Person":
    ...         return clazz(**{k: v.upper() for k, v in params.items()})
    ...
    ...     return clazz(**params)
    ...

    >>> config = ParserConfig(class_factory=custom_class_factory)
    >>> parser = JsonParser(config=config)
    ...
    >>> @dataclass
    ... class Person:
    ...     first_name: str
    ...     last_name: str
    ...
    >>> json_str = """{"first_name": "chris", "last_name": "foo"}"""
    ...
    ...
    >>> print(parser.from_string(json_str, Person))
    Person(first_name='CHRIS', last_name='FOO')

.. warning::

    It's not recommended to modify the generated models!
