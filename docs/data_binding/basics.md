# Basics

## Context

All binding metadata is generated and cached in a
[XmlContext][xsdata.formats.dataclass.context.XmlContext] instance. It's recommended to
either reuse the same parser/serializer instance or reuse the context instance.

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>> from xsdata.formats.dataclass.parsers import JsonParser
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.serializers import JsonSerializer

>>> context = XmlContext()
>>> xml_parser = XmlParser(context=context)
>>> json_parser = JsonParser(context=context)
>>> xml_serializer = XmlSerializer(context=context)
>>> json_serializer = JsonSerializer(context=context)

```

### Global Property Names

Through the [XmlContext][xsdata.formats.dataclass.context.XmlContext] instance you can
provide callables to apply a naming scheme for all models and their fields. This way you
can avoid declaring them for every model, but you have to use the same context whenever
you want to use a parser/serializer.

```python
>>> from dataclasses import dataclass, field
>>> from datetime import date
>>> from xsdata.utils import text
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
>>> serializer = XmlSerializer(context=context)
>>> serializer.config.indent = "  "
>>> print(serializer.render(obj))
<?xml version="1.0" encoding="UTF-8"?>
<person birth-date="1986-09-25">
  <firstName>Chris</firstName>
  <lastName>T</lastName>
</person>

```

## Parser Config

API: [ParserConfig][xsdata.formats.dataclass.parsers.config.ParserConfig]

### `base_url`

Specifies a base URL when parsing from memory and the parser has to import included
documents. e.g. [XML Inclusions](xml_parsing.md#xml-inclusions)

**Type:** `Optional[str]`

**Default:** `None`

### `process_xinclude`

Enable [XML Inclusions](xml_parsing.md#xml-inclusions) processing. The parser will
follow and retrieve the remote documents.

**Type:** `bool`

**Default:** `False`

### `load_dtd`

Enable loading external dtd with
[LxmlEventHandler][xsdata.formats.dataclass.parsers.handlers.LxmlEventHandler].

**Type:** `bool`

**Default:** `False`

### `class_factory`

Override default object instantiation, to apply pre/post-initialization logic.

```python
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

```

**Type:** `Callable[[Type[T], Dict[str, Any]], T]`

**Default:** `lambda: cls, params: return cls(**params)`

### `fail_on_unknown_properties`

Fail if the document includes properties not defined in the model.

**Type:** `bool`

**Default:** `True`

### `fail_on_unknown_attributes`

Fail if the document includes attributes not defined in the model.

**Type:** `bool`

**Default:** `False`

### `fail_on_converter_warnings`

Fail if a document value can't be correctly converted to python.

**Type:** `bool`

**Default:** `False`

## Serializer Config

API: [SerializerConfig][xsdata.formats.dataclass.serializers.config.SerializerConfig]

### `encoding`

The text encoding for the XML header.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

**Type**: `str`

**Default:** `"UTF-8"`

### `xml_version`

The XML version number to render `(1.0|1.1)`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

**Type**: `str`

**Default:** `"1.0"`

### `xml_declaration`

Renders the XML declaration header.

**Type**: `bool`

**Default:** `True`

### `indent`

Indent output by the given string.

**Type**: `Optional[str]`

**Default:** `None`

### `ignore_default_attributes`

Ignore optional attributes with default values.

**Type**: `bool`

**Default:** `False`

### `schema_location`

Render a `xsi:schemaLocation` attribute on the root element.

```xml
<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xsdtesting elemS002.xsd"
```

**Type**: `Optional[str]`

**Default:** `None`

### `no_namespace_schema_location`

Render a `xsi:noNamespaceSchemaLocation` attribute on the root element.

```xml
<doc xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="groupB003.xsd">
```

**Type**: `Optional[str]`

**Default:** `None`

### `globalns`

Dictionary containing global variables to extend or overwrite for typing.

When managing a big collection of models, it is sometimes tricky to split them into
multiple python modules. Even more so if they depend on each other. For the models to be
serializable by xsdata, they need to be able to import all other referenced models,
which might not be possible due to circular imports.

One solution to get around this problem is to fence the imports within the python
modules by using [typing.TYPE_CHECKING][] and use this option to manually define the
types.

=== "city.py"

    ```python
    --8<-- "tests/fixtures/typemapping/city.py"
    ```

=== "street.py"

    ```python
    --8<-- "tests/fixtures/typemapping/street.py"
    ```

=== "house.py"

    ```python
    --8<-- "tests/fixtures/typemapping/house.py"
    ```

```python
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
>>> from tests.fixtures.typemapping.city import City
>>> from tests.fixtures.typemapping.house import House
>>> from tests.fixtures.typemapping.street import Street
>>>
>>> city1 = City(name="footown")
>>> street1 = Street(name="foostreet")
>>> house1 = House(number=23)
>>> city1.streets.append(street1)
>>> street1.houses.append(house1)
>>> type_map = {"City": City, "Street": Street, "House": House}
>>> serializer_config = SerializerConfig(indent="  ", globalns=type_map)
>>> xml_serializer = XmlSerializer(config=serializer_config)
>>> serialized_house = xml_serializer.render(city1)
>>> print(serialized_house)
<?xml version="1.0" encoding="UTF-8"?>
<City>
  <name>footown</name>
  <streets>
    <name>foostreet</name>
    <houses>
      <number>23</number>
    </houses>
  </streets>
</City>

```

**Type**: `Optional[Dict[str, Callable]]` None
