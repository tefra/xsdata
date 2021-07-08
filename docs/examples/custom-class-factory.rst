====================
Custom class factory
====================


It's not recommended to modify the generated models. If you need to add any pre/post
initialization logic or even validations you can use the parser config to override the
default class factory.

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
