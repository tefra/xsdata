# Dict Encoding

The [DictEncoder][xsdata.formats.dataclass.serializers.DictEncoder] converts a data
model instance to a dictionary and encodes all values to make them safe for
serialization.

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.serializers import DictEncoder
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig

>>> config = SerializerConfig(pretty_print=True)
>>> context = XmlContext()
>>> encoder = DictEncoder()
>>> encoder = DictEncoder(context=context, config=config)

```

## Example

```python
>>> import pprint
>>> from tests.fixtures.books import BookForm
>>>
>>> book = BookForm(
...     id="bk001",
...     author="Hightower, Kim",
...     title="The First Book",
...     genre="Fiction",
...     price=44.95,
...     review="An amazing story of nothing.",
... )
>>> pprint.pprint(encoder.encode(book))
{'author': 'Hightower, Kim',
 'genre': 'Fiction',
 'id': 'bk001',
 'lang': 'en',
 'price': 44.95,
 'pub_date': None,
 'review': 'An amazing story of nothing.',
 'title': 'The First Book'}

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
>>> encoder = DictEncoder(dict_factory=filter_none)
>>> pprint.pprint(encoder.encode(book))
{'author': 'Hightower, Kim',
 'genre': 'Fiction',
 'id': 'bk001',
 'lang': 'en',
 'price': 44.95,
 'review': 'An amazing story of nothing.',
 'title': 'The First Book'}

```

or conveniently

```python
>>> from xsdata.formats.dataclass.serializers import DictFactory
>>>
>>> encoder = DictEncoder(dict_factory=DictFactory.FILTER_NONE)

```
