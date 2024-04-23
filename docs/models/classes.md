# Classes

xsdata is using python's [dataclasses][] as representation models for document entities.
Plugins can extend support for output formats.

## Basic Example

```python exec="true" source="above" result="xml"
from dataclasses import dataclass # markdown-exec: hide
from xsdata.formats.dataclass.serializers import XmlSerializer # markdown-exec: hide
serializer = XmlSerializer() # markdown-exec: hide
serializer.config.indent = "  " # markdown-exec: hide
@dataclass
class Book:
    title: str
    author: str
    year: int

book = Book(title="The Catcher in the Rye", author="J.D. Salinger", year=1951)
print(serializer.render(book))
```

## Metadata

Additional class metadata are required in order to access some of the more advance
features.

### `name`

The local name of the XML/JSON element.

```python show_lines="8:"
>>> from dataclasses import dataclass, field
>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.utils.text import camel_case
>>> serializer = XmlSerializer()
>>> serializer.config.indent = "  "
>>> serializer.config.xml_declaration = False
>>>
>>> @dataclass
... class Root:
...     class Meta:
...         name = "xsdata"
...
>>> print(serializer.render(Root()))
<xsdata/>

```

**Type:** `str`

**Default:** `The class name`

### `namespace`

The namespace name of the XML element

```python
>>> @dataclass
... class Root:
...     class Meta:
...         namespace = "xsdata"
...
>>> print(serializer.render(Root()))
<ns0:Root xmlns:ns0="xsdata"/>

```

**Type:** `str | None`

**Default:** `None`

### `nillable`

Specify if the attribute `xsi:nil="true"` is needed when the class is serialized and it
doesn't have any meaningful content.

```python
>>> @dataclass
... class Child:
...     class Meta:
...         nillable = True
...
>>> @dataclass
... class Root:
...     child: Child
...
>>> root = Root(child=Child())
>>> print(serializer.render(root))
<Root>
  <child xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
</Root>

```

**Type:** `bool`

**Default:** `False`

### `target_namespace`

The namespace name, the XML element was defined under. Used during auto-type discovery
when the element form is `unqualified`.

**Type:** `str | None`

**Default:** `None`

### `global_type`

Specify if the class represents an element that can appear in the document root. When
false the class can be used only another class dependency, and it's excluded from
auto-type discovery.

**Type:** `bool`

**Default:** `True`

### `element_name_generator`

A callable to convert element names when no explicit names are defined.

```python
>>> @dataclass
... class RootType:
...     class Meta:
...         element_name_generator = camel_case
...
>>> print(serializer.render(RootType()))
<rootType/>

```

**Type:** `Callable[[str], str]`

**Default:** `lambda x: x`

### `attribute_name_generator`

A callable to convert attribute names when no explicit names are defined.

```python
>>> @dataclass
... class Root:
...     who_are_you: str = field(default="xsdata", metadata={"type": "Attribute"})
...     class Meta:
...         attribute_name_generator = camel_case
...
>>> print(serializer.render(Root()))
<Root whoAreYou="xsdata"/>

```

**Type:** `Callable[[str], str]`

**Default:** `lambda x: x`
