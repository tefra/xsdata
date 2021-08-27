========================
Customize property names
========================

Through the model and field metadata you can explicitly specify the serialized
names. You can also provide callables to set the real/local names per model or
per binding context.


**Ordered by priority**

.. tab:: Explicit names

    Explicit model and field names is the most straight forward way to customize
    the real/local names for elements and attributes. It can become tedious though
    when you have to do this for models with a lot of fields.

    .. doctest::

        >>> from dataclasses import dataclass, field
        >>> from datetime import date
        >>> from xsdata.formats.dataclass.serializers import XmlSerializer
        >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
        ...
        >>> config = SerializerConfig(pretty_print=True, xml_declaration=False)
        >>> serializer = XmlSerializer(config=config)
        ...
        >>> @dataclass
        ... class Person:
        ...
        ...     class Meta:
        ...         name = "Person"  # Explicit name
        ...
        ...     first_name: str = field(metadata=dict(name="firstName"))
        ...     last_name: str = field(metadata=dict(name="lastName"))
        ...     birth_date: date = field(
        ...         metadata=dict(
        ...             type="Attribute",
        ...             format="%Y-%m-%d",
        ...             name="dob"  # Explicit name
        ...         )
        ...     )
        ...
        >>> obj = Person(
        ...     first_name="Chris",
        ...     last_name="T",
        ...     birth_date=date(1986, 9, 25),
        ... )
        >>> print(serializer.render(obj))
        <Person dob="1986-09-25">
          <firstName>Chris</firstName>
          <lastName>T</lastName>
        </Person>
        <BLANKLINE>


.. tab:: Model name generators

    Through the Meta class you can provide callables to apply a naming scheme for all
    the model fields. The :mod:`xsdata.utils.text` has various helpers that you can
    reuse.

    .. doctest::

        >>> from xsdata.utils import text
        ...
        >>> @dataclass
        ... class person:
        ...
        ...     class Meta:
        ...         element_name_generator = text.pascal_case
        ...         attribute_name_generator = text.camel_case
        ...
        ...     first_name: str
        ...     last_name: str
        ...     birth_date: date = field(
        ...         metadata=dict(
        ...             type="Attribute",
        ...             format="%Y-%m-%d"
        ...         )
        ...     )
        ...
        >>> obj = person(
        ...     first_name="Chris",
        ...     last_name="T",
        ...     birth_date=date(1986, 9, 25),
        ... )
        >>> print(serializer.render(obj))
        <Person birthDate="1986-09-25">
          <FirstName>Chris</FirstName>
          <LastName>T</LastName>
        </Person>
        <BLANKLINE>


.. tab:: Context name generators

    Through the :class:`~xsdata.formats.dataclass.context.XmlContext` instance you can
    provide callables to apply a naming scheme for all models and their fields. This way
    you can avoid declaring them for every model but you have to use the same context
    whenever you want to use a parser/serializer.

    .. doctest::

        >>> from xsdata.formats.dataclass.context import XmlContext
        ...
        >>> @dataclass
        ... class Person:
        ...
        ...     first_name: str
        ...     last_name: str
        ...     birth_date: date = field(
        ...         metadata=dict(
        ...             type="Attribute",
        ...             format="%Y-%m-%d"
        ...         )
        ...     )
        ...
        >>> obj = Person(
        ...     first_name="Chris",
        ...     last_name="T",
        ...     birth_date=date(1986, 9, 25),
        ... )
        ...
        >>> context = XmlContext(
        ...     element_name_generator=text.camel_case,
        ...     attribute_name_generator=text.kebab_case
        ... )
        >>> serializer = XmlSerializer(context=context, config=config)
        >>> print(serializer.render(obj))
        <person birth-date="1986-09-25">
          <firstName>Chris</firstName>
          <lastName>T</lastName>
        </person>
        <BLANKLINE>
