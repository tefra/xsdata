# Pycode Serializer

The pycode serializer will render an object tree into python representation code.

```python
>>> from tests.fixtures.books.fixtures import books
>>> from xsdata.formats.dataclass.serializers import PycodeSerializer
...
>>> serializer = PycodeSerializer()
>>> print(serializer.render(books, var_name="books"))
from tests.fixtures.books.books import BookForm
from tests.fixtures.books.books import Books
from xsdata.models.datatype import XmlDate
<BLANKLINE>
<BLANKLINE>
books = Books(
    book=[
        BookForm(
            author='Hightower, Kim',
            title='The First Book',
            genre='Fiction',
            price=44.95,
            pub_date=XmlDate(2000, 10, 1),
            review='An amazing story of nothing.',
            id='bk001'
        ),
        BookForm(
            author='Nagata, Suanne',
            title='Becoming Somebody',
            genre='Biography',
            price=33.95,
            pub_date=XmlDate(2001, 1, 10),
            review='A masterpiece of the fine art of gossiping.',
            id='bk002'
        ),
    ]
)

```
