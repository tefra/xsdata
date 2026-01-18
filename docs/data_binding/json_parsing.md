# JSON Parsing

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.parsers import JsonParser
>>> from xsdata.formats.dataclass.parsers.config import ParserConfig

>>> config = ParserConfig()
>>> context = XmlContext()
>>> parser = JsonParser(context=context, config=config)
>>> parser = JsonParser()

```

## Filenames

```python
>>> from tests.fixtures.books.books import Books
...
>>> books = parser.parse("tests/fixtures/books/books.json", Books)
>>> books.book[0]
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')

```

## File-like objects

```python
>>> with open("tests/fixtures/books/books.json", "rb") as fp:
...     books = parser.parse(fp, Books)
>>> books.book[0]
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')

```

## String

```python
>>> from pathlib import Path
>>>
>>> json_string = Path("tests/fixtures/books/books.json").read_text()
>>> books = parser.from_string(json_string, Books)
>>> books.book[0]
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


```

## Bytes

```python
>>> json_bytes = Path("tests/fixtures/books/books.json").read_bytes()
>>> books = parser.from_bytes(json_bytes, Books)
>>> books.book[0]
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')

```

## pathlib.Path

```python
>>> file_path = Path("tests/fixtures/books/books.json")
>>> books = parser.from_path(file_path, Books)
>>> books.book[0]
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')

```

## Unknown target clazz

It's optimal to provide the target class but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

```python
>>> order = parser.parse("tests/fixtures/books/books.json")
>>> type(order)
<class 'tests.fixtures.books.books.Books'>

```

!!! Warning

    The class locator searches for a dataclass that includes all the input object
    properties. This process doesn't work for documents with unknown properties even
    if the configuration option is disabled!

## List of objects

Specify the target binding type to `List[ModelName]`

```python

>>> from typing import List
>>> from tests.fixtures.books.books import BookForm
>>>
>>> json_string = """[
...     {
...       "author": "Hightower, Kim",
...       "title": "The First Book",
...       "genre": "Fiction",
...       "price": 44.95,
...       "pub_date": "2000-10-01",
...       "review": "An amazing story of nothing.",
...       "id": "bk001"
...     },
...     {
...       "author": "Nagata, Suanne",
...       "title": "Becoming Somebody",
...       "genre": "Biography",
...       "price": null,
...       "pub_date": null,
...       "review": "A masterpiece of the fine art of gossiping.",
...       "id": "bk002"
...     }
...   ]"""
>>> booklist = parser.from_string(json_string, List[BookForm])
>>> booklist[1].author
'Nagata, Suanne'

```

## Ignore unknown properties

By default the parser will fail on unknown properties, but you can disable these errors
through configuration.

```python
>>> config = ParserConfig(
...     fail_on_unknown_properties=False,
...     fail_on_unknown_attributes=False,
... )
>>> json_string = """{
...   "author": "Hightower, Kim",
...   "title": "The First Book",
...   "genre": "Fiction",
...   "price": 44.95,
...   "pub_date": "2000-10-01",
...   "review": "An amazing story.",
...   "unknown_property": "I will be ignored"
... }"""
>>> parser = JsonParser(config=config)
>>> parser.from_string(json_string, BookForm)
BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story.', id=None, lang='en')

```

## Custom json load factory

The default factory is python's builtin :func:`python:json.load` but you can use any
other implementation as long as it has a compatible signature.

```python
import ujson

parser = JsonParser(load_factory=ujson.load)
```
