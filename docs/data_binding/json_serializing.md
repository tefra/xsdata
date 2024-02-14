# JSON Serializing

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.serializers import JsonSerializer
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig

>>> config = SerializerConfig(pretty_print=True)
>>> context = XmlContext()
>>> serializer = JsonSerializer()
>>> serializer = JsonSerializer(context=context, config=config)

```

## Return as string

```python
>>> from xsdata.models.datatype import XmlDate
>>> from tests.fixtures.books import Books, BookForm
>>>
>>> books = Books(
...    book=[
...        BookForm(
...            id="bk001",
...            author="Hightower, Kim",
...            title="The First Book",
...            genre="Fiction",
...            price=44.95,
...            review="An amazing story of nothing.",
...        ),
...        BookForm(
...            id="bk002",
...            author="Nagata, Suanne",
...            title="Becoming Somebody",
...            price=33.95,
...            pub_date=XmlDate(2001, 1, 10),
...            review="A masterpiece of the fine art of gossiping.",
...        ),
...    ]
... )
>>> print(serializer.render(books))
{
  "book": [
    {
      "author": "Hightower, Kim",
      "title": "The First Book",
      "genre": "Fiction",
      "price": 44.95,
      "pub_date": null,
      "review": "An amazing story of nothing.",
      "id": "bk001",
      "lang": "en"
    },
    {
      "author": "Nagata, Suanne",
      "title": "Becoming Somebody",
      "genre": null,
      "price": 33.95,
      "pub_date": "2001-01-10",
      "review": "A masterpiece of the fine art of gossiping.",
      "id": "bk002",
      "lang": "en"
    }
  ]
}

```

## Write to file-like objects

```python
>>> from pathlib import Path
...
>>> path = Path("output.json")
>>> with path.open("w") as fp:
...     serializer.write(fp, books)
...
>>> print(path.read_text())
{
  "book": [
    {
      "author": "Hightower, Kim",
      "title": "The First Book",
      "genre": "Fiction",
      "price": 44.95,
      "pub_date": null,
      "review": "An amazing story of nothing.",
      "id": "bk001",
      "lang": "en"
    },
    {
      "author": "Nagata, Suanne",
      "title": "Becoming Somebody",
      "genre": null,
      "price": 33.95,
      "pub_date": "2001-01-10",
      "review": "A masterpiece of the fine art of gossiping.",
      "id": "bk002",
      "lang": "en"
    }
  ]
}

>>> path.unlink()

```

## Custom dict factory

By using a custom dict factory you can change the output behaviour, like filter out
`None` values.

```python
>>> from typing import Dict, Tuple
>>>
>>> def filter_none(x: Tuple) -> Dict:
...     return {k: v for k, v in x if v is not None}
>>>
>>> books.book[0].genre = None
>>> serializer = JsonSerializer(dict_factory=filter_none, config=config)
>>> print(serializer.render(books.book[0]))
{
  "author": "Hightower, Kim",
  "title": "The First Book",
  "price": 44.95,
  "review": "An amazing story of nothing.",
  "id": "bk001",
  "lang": "en"
}

```

or conveniently

```python
>>> from xsdata.formats.dataclass.serializers import DictFactory
>>>
>>> serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)

```

## Custom json dump factory

The default factory is python's builtin :func:`python:json.dump` but you can use any
other implementation as long as it's has a compatible signature.

```python
import ujson

serializer = JsonSerializer(dump_factory=ujson.dump)
```
