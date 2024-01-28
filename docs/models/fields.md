# Fields

The [dataclasses][] fields come with a useful metadata mapping that is provided as a
third-party extension mechanism. This mechanism is used by xsdata to support advance xml
features.

## Metadata

### `name`

The local name of the XML/JSON field.

```python show_lines="11:"
>>> import datetime
>>> from typing import Optional, List, Union
>>> from dataclasses import dataclass, field
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>> parser = XmlParser()
>>> serializer = XmlSerializer()
>>> serializer.config.pretty_print = True
>>> serializer.config.xml_declaration = False
>>>
>>> @dataclass
... class Root:
...     first: str = field(metadata={"name": "one"})
...     second: str = field(metadata={"name": "two"})
...
>>> root = Root(first="xml", second="json")
>>> print(serializer.render(root))
<Root>
  <one>xml</one>
  <two>json</two>
</Root>

```

**Type:** `srt`

**Default:** `The field name`

### `namespace`

The namespace name of the XML element or attribute.

```python
>>> @dataclass
... class Root:
...     attr: str = field(metadata={"type": "Attribute", "namespace": "a"})
...     child: str = field(metadata={"type": "Element", "namespace": "c"})
...
>>> print(serializer.render(Root(attr="a", child="c")))
<Root xmlns:ns0="a" ns0:attr="a">
  <ns1:child xmlns:ns1="c">c</ns1:child>
</Root>

```

**Type:** `str`

**Default:** `None`

### `nillable`

Specify if the field has to be present in the serialized result even when it doesn't
have any meaningful content.

```python
>>> @dataclass
... class Root:
...     first: Optional[str] = field(metadata={"nillable": True}, default=None)
...     second: Optional[str] = field(default=None)
...
>>> print(serializer.render(Root()))
<Root>
  <first xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
</Root>

```

**Type:** `bool`

**Default:** `False`

### `sequence`

Fields will the same sequence number are rendered sequentially.

```python
>>> @dataclass
... class Root:
...     a: List[int] = field(metadata={"sequence": 1})
...     b: int = field(metadata={"sequence": 1})
...     c: List[int] = field(metadata={"sequence": 1})
...
>>> root = Root(a=[1, 2, 3], b=4, c=[6, 7, 8])
>>> print(serializer.render(root))
<Root>
  <a>1</a>
  <b>4</b>
  <c>6</c>
  <a>2</a>
  <c>7</c>
  <a>3</a>
  <c>8</c>
</Root>

```

**Type:** `int | None`

**Default:** `None`

### `tokens`

Specify if the field value is a whitespace concatenated sequence.

```python
>>> @dataclass
... class Root:
...     child: List[int] = field(metadata={"type": "Element", "tokens": True})
...
>>> root = Root([1, 2, 3])
>>> print(serializer.render(root))
<Root>
  <child>1 2 3</child>
</Root>

```

**Type:** `bool`

**Default:** `False`

### `format`

The field format option for types like datetime, or bytes.

```python
>>> @dataclass
... class Root:
...     base16: bytes = field(metadata={"format": "base16"})
...     base64: bytes = field(metadata={"format": "base64"})
...     date: datetime.date = field(metadata=dict(format="%d/%m/%Y"))
...
>>> root = Root(
...     base16="xsdata".encode(),
...     base64="xsdata".encode(),
...     date=datetime.date(2024, 1, 15)
...  )
>>> print(serializer.render(root))
<Root>
  <base16>787364617461</base16>
  <base64>eHNkYXRh</base64>
  <date>15/01/2024</date>
</Root>

```

**Type:** `str`

**Default:** `None`

### `type`

The type property allows to change how a field should behave during data binding.

#### Text

Represents a xml value node.

```python
>>> @dataclass
... class Root:
...     value: str = field(metadata={"type": "Text"}, default="abc")
...
>>> print(serializer.render(Root()))
<Root>abc</Root>

```

#### Element

Represents a xml element node.

```python
>>> @dataclass
... class Root:
...     value: str = field(metadata={"type": "Element"}, default="abc")
...
>>> print(serializer.render(Root()))
<Root>
  <value>abc</value>
</Root>

```

#### Attribute

Represents a xml attribute.

```python
>>> @dataclass
... class Root:
...     value: str = field(metadata={"type": "Attribute"}, default="abc")
...
>>> print(serializer.render(Root()))
<Root value="abc"/>

```

#### Elements

Elements type represents repeatable choice elements. It's more commonly referred as
`Compound Fields`.

```python
>>> @dataclass
... class Root:
...     value: List[Union[str, int, bool]] = field(
...         metadata={
...             "type": "Elements",
...             "choices": (
...                 {"name": "string", "type": str},
...                 {"name": "integer", "type": int},
...                 {"name": "bool", "type": bool}
...             )
...         }
...     )
...
>>> root = Root(value=[1, True, "a", "b", True])
>>> print(serializer.render(root))
<Root>
  <integer>1</integer>
  <bool>true</bool>
  <string>a</string>
  <string>b</string>
  <bool>true</bool>
</Root>

```

**Choice elements properties**

| Property        | type | The real name of the element this choice represents.               |
| --------------- | ---- | ------------------------------------------------------------------ |
| name            | str  | The local name of the XML/JSON field.                              |
| type            | str  | The type hint.                                                     |
| nillable        | bool | Specify if the choice has to be serialized when it has no content. |
| wildcard        | bool | Wildcard element to match any xml string.                          |
| tokens          | bool | Specify if the choice value is a whitespace concatenated sequence. |
| namespace       | str  | The namespace name of the XML element.                             |
| format          | str  | The value format for types like datetime, or bytes.                |
| default         | Any  | Default value.                                                     |
| default_factory | Any  | Default value factory.                                             |

!!! Warning

    If a compound field includes ambiguous types, you need to use
    `~xsdata.formats.dataclass.models.generics.DerivedElement` to wrap
    your values, otherwise your object can be assigned to the wrong element.

#### Wildcard

This type represents `xs:any` elements or elements with type `xs:AnyType`.

This type optionally can have a list of acceptable choices similar to compound fields,
otherwise during binding the parsers will try to find a suitable model automatically, if
everything fails, the parser will use the generic `AnyElement`.

Wildcards can have a normal uri namespace or use one of xml schema generics.

- `##any`: element from any namespace is allowed
- `##other`: element from any namespace other than the parent’s namespace
- `##local`: element must come from no namespace
- `##targetNamespace`: element from the namespace of the parent can be present

```python
>>> @dataclass
... class Root:
...     any: object = field(metadata={"type": "Wildcard"})
...
>>> xml = '<Root><child a="b">foo</child></Root>'
>>> parser.from_string(xml, clazz=Root)
Root(any=AnyElement(qname='child', text='foo', tail=None, children=[], attributes={'a': 'b'}))

```

#### Attributes

This type represents `xs:anyAttribute` elements and can practically absorb any attribute
that it is not defined in the class, but it has to be defined as a dictionary.

Similar to Wildcard, this type can have a normal uri namespace or use one of xml schema
generics.

- `##any`: attributes from any namespace is allowed
- `##other`: attributes from any namespace other than the parent’s namespace
- `##local`: attributes must come from no namespace
- `##targetNamespace`: attributes from the namespace of the parent can be present

```python
>>> @dataclass
... class Root:
...     known: int = field(metadata={"type": "Attribute"})
...     attrs: dict = field(metadata={"type": "Attributes"})
...
>>> xml = '<Root known="1" unknown="2" />'
>>> xml = '<Root known="1" unknown="2" />'
>>> parser.from_string(xml, clazz=Root)
Root(known=1, attrs={'unknown': '2'})

```

#### Ignore

This type will force the binding context to ignore the field. Make sure your field is
declared with `init=False` or with a default value otherwise data binding will fail.

```python
>>> @dataclass
... class Root:
...     index: int = field(default_factory=int, metadata={"type": "Ignore"})
...
>>> print(serializer.render(Root()))
<Root/>

```

### `wrapper`

The element name to wrap a collection of elements or primitives, in order to avoid
having a dedicated wrapper class.

```python
>>> from dataclasses import dataclass, field
>>> from typing import List
>>>
>>> @dataclass
... class Library:
...     books: List[str] = field(
...         metadata={
...             "wrapper": "Books",
...             "name": "Title",
...             "type": "Element",
...         }
...     )
...
>>> obj = Library(
...     books = [
...         "python for beginners",
...         "beautiful xml",
...     ]
... )
>>>
>>> print(serializer.render(obj))
<Library>
  <Books>
    <Title>python for beginners</Title>
    <Title>beautiful xml</Title>
  </Books>
</Library>

```

**Type:** `Optional[str]`

**Default:** `None`

### `mixed`

Specifies whether the field supports mixed content. The flag is indented for `Wildcard`
types and indicates that the parser should attempt to grab any text/tail content from
the xml element.

```python
>>> @dataclass
... class Root:
...     content: object = field(metadata={"type": "Wildcard", "mixed": True})
...
>>> xml = '<Root><p>Paragraph</p> Tail</Root>'
>>> parser.from_string(xml, clazz=Root)
Root(content=[AnyElement(qname='p', text='Paragraph', tail=' Tail', children=[], attributes={})])

```

**Type:** `bool`

**Default:** `False`

### `process_contents`

Specifies how `Wildcard` fields should behave, when they don't have a predefined list of
choices. If `strict` is enabled, binding context will try to auto-locate a class that
matches the qualified name, of the xml element, before trying using the
[`AnyElement`][xsdata.formats.dataclass.models.generics.AnyElement] generic.

**Type:** `strict | skip`

**Default:** `strict`
