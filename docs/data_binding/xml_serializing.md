# XML Serializing

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig

>>> config = SerializerConfig(indent="  ")
>>> context = XmlContext()
>>> serializer = XmlSerializer()
>>> serializer = XmlSerializer(context=context, config=config)

```

## Return as string

```python
>>> from tests.fixtures.books import Books, BookForm
...
>>> books = Books(
...     book=[
...         BookForm(
...             id="bk001",
...             author="Hightower, Kim",
...             title="The First Book",
...             genre="Fiction",
...             price=44.95,
...             pub_date="2000-10-01",
...             review="An amazing story of nothing.",
...         )
...     ]
... )
...
>>> print(serializer.render(books))
<?xml version="1.0" encoding="UTF-8"?>
<ns0:books xmlns:ns0="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</ns0:books>

```

## Write to file-like objects

```python
>>> from pathlib import Path
...
>>> path = Path("output.xml")
>>> with path.open("w") as fp:
...     serializer.write(fp, books)
...
>>> print(path.read_text())
<?xml version="1.0" encoding="UTF-8"?>
<ns0:books xmlns:ns0="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</ns0:books>

>>> path.unlink()

```

## Custom namespace prefixes

```python
>>> print(serializer.render(books, ns_map={"bk": "urn:books"}))
<?xml version="1.0" encoding="UTF-8"?>
<bk:books xmlns:bk="urn:books">
  <book id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</bk:books>

```

## Default namespace

```python
>>> print(serializer.render(books, ns_map={None: "urn:books"}))
<?xml version="1.0" encoding="UTF-8"?>
<books xmlns="urn:books">
  <book xmlns="" id="bk001" lang="en">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</books>

```

## Skip attributes with default values

Attributes are allowed to have default or fixed values and be marked as optional. The
default behaviour is to write them explicitly during serialization, but you can disable
them through config.

```python
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
...
>>> serializer = XmlSerializer(config=SerializerConfig(
...     indent="  ",
...     xml_declaration=False,
...     ignore_default_attributes=True,
...     schema_location="urn books.xsd",
...     no_namespace_schema_location=None,
... ))
>>> print(serializer.render(books))
<ns0:books xmlns:ns0="urn:books" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn books.xsd">
  <book id="bk001">
    <author>Hightower, Kim</author>
    <title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
</ns0:books>

```

## Custom serialization for specific data types

If you wish to specify some custom serialization function, for example to change the way
a datetime is formatted, you can register a custom converter.

```python
>>> from dataclasses import dataclass
>>> from typing import Any, Optional
>>>
>>> from xsdata.formats.converter import Converter, converter
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
>>> from xsdata.models.datatype import XmlDateTime
>>>
>>> parser = XmlParser()
>>> serializer = XmlSerializer(config=SerializerConfig(xml_declaration=False))
>>>
>>>
>>> @dataclass
... class DateTimeObject:
...     datetime: XmlDateTime
>>>
>>>
>>> xml_obj = parser.from_string(
...     "<datetime>2023-11-24T10:38:56.123</datetime>", DateTimeObject
... )
>>>
>>> print(serializer.render(xml_obj))
<DateTimeObject>2023-11-24T10:38:56.123</DateTimeObject>
>>>
>>>
>>> class MyXmlDateTimeConverter(Converter):
...
...     def deserialize(self, value: Any, **kwargs: Any) -> Any:
...         return XmlDateTime.from_string(value)
...
...     def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
...        if isinstance(value, XmlDateTime):
...            # Can be anything you like
...            return (
...                 f"{value.day}-{value.month}-{value.year}"
...                 f"T{value.hour}:{value.minute}:{value.second}"
...             )
>>>
>>>
>>> converter.register_converter(XmlDateTime, MyXmlDateTimeConverter())
>>> print(serializer.render(xml_obj))
<DateTimeObject>24-11-2023T10:38:56</DateTimeObject>
>>>
>>> converter.unregister_converter(XmlDateTime)

```

## Alternative writers

There are two writers based on lxml and native python that may vary in performance in
some cases. The output of all them is consistent with a few exceptions when handling
mixed content and enabled indentation.

!!! Hint

    If you installed xsdata with lxml the default writer is set to
    [`LxmlEventWriter`][xsdata.formats.dataclass.serializers.writers.LxmlEventWriter] otherwise
    [`XmlEventWriter`][xsdata.formats.dataclass.serializers.writers.XmlEventWriter] will be used.

```python

>>> from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
>>> from xsdata.formats.dataclass.serializers.writers import LxmlEventWriter
...
>>> serializer = XmlSerializer(config=config, writer=XmlEventWriter)
>>> serializer = XmlSerializer(config=config, writer=LxmlEventWriter)

```

## Working with wildcards

One of the xml schema traits is to support any extensions with wildcards.

```xml
    <xs:complexType name="MetadataType" mixed="false">
        <xs:sequence>
            <xs:any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>
```

The generator will roughly create this class for you.

```python
>>> from dataclasses import dataclass
>>> from dataclasses import field
>>> from typing import Dict
>>> from typing import List
...
>>> @dataclass
... class MetadataType:
...     any_element: List[object] = field(
...         default_factory=list,
...         metadata={
...              "type": "Wildcard",
...              "namespace": "##any",
...          }
...     )
...     other_attributes: Dict[str, str] = field(
...          default_factory=dict,
...          metadata={
...              "type": "Attributes",
...              "namespace": "##other",
...          }
...      )

```

### Generics

xsdata comes with two generic models that are used during parsing and you can also use
to generate any custom xml element.

- [`AnyElement`][xsdata.formats.dataclass.models.generics.AnyElement]: Used to represent
  any xml structure, resembles a DOM Element
- [`DerivedElement`][xsdata.formats.dataclass.models.generics.DerivedElement]: Wrapper
  for type substitution elements eg `<b xsi:type="a">...</b>`

```python
>>> from xsdata.formats.dataclass.models.generics import AnyElement
>>> from xsdata.formats.dataclass.models.generics import DerivedElement
...
>>> obj = MetadataType(
...     any_element=[
...         AnyElement(
...             qname="bar",
...             children=[
...                 AnyElement(qname="first", text="1st", attributes={"a": "1"}),
...                 AnyElement(qname="second", text="2nd", attributes={"b": "2"}),
...                 AnyElement(qname="{http://xsdata}third", text="2nd", attributes={"b": "2"}),
...                 DerivedElement(
...                     qname="fourth",
...                     value=MetadataType(other_attributes={"c": "3"})
...                 )
...             ]
...         )
...     ]
... )
>>> print(serializer.render(obj))
<?xml version="1.0" encoding="UTF-8"?>
<MetadataType>
  <bar>
    <first a="1">1st</first>
    <second b="2">2nd</second>
    <ns0:third xmlns:ns0="http://xsdata" b="2">2nd</ns0:third>
    <fourth xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" c="3" xsi:type="MetadataType"/>
  </bar>
</MetadataType>

```

### Mixed content

For mixed content with known choices you can skip wrapping your instances with a generic
model. During data binding xsdata will try first to match one of the qualified choices.

```python
>>> @dataclass
... class Beta:
...     class Meta:
...         name = "beta"
...
>>> @dataclass
... class Alpha:
...     class Meta:
...         name = "alpha"
...
>>> @dataclass
... class Doc:
...     class Meta:
...         name = "doc"
...
...     content: List[object] = field(
...         default_factory=list,
...         metadata={
...             "type": "Wildcard",
...             "namespace": "##any",
...             "mixed": True,
...             "choices": (
...                 {
...                     "name": "a",
...                     "type": Alpha,
...                     "namespace": "",
...                 },
...                 {
...                     "name": "b",
...                     "type": Beta,
...                     "namespace": "",
...                 },
...             ),
...         }
...     )
...
>>> obj = Doc(
...     content=[
...         Alpha(),
...         Beta(),
...     ]
... )
...
>>> print(serializer.render(obj))
<?xml version="1.0" encoding="UTF-8"?>
<doc>
  <a/>
  <b/>
</doc>

```
