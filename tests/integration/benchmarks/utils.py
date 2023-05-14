from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.integration.benchmarks.conftest import context
from tests.integration.benchmarks.conftest import xsdata_temp_dir
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.models.datatype import XmlDate


def make_books(how_many: int):
    return Books(
        book=[
            BookForm(
                author="Arne Dahl",
                title="Misterioso: A Crime Novel",
                genre="Thrillers & Suspense",
                price=15.95,
                pub_date=XmlDate(1999, 10, 5),
                review=(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Integer at erat sagittis, accumsan mauris eu, egestas "
                    "quam. Nam tristique felis justo, vel iaculis ipsum cursus "
                    "at. Praesent varius enim ac nunc interdum placerat. "
                    "Integer porttitor, nibh at viverra vehicula, leo dui "
                    "suscipit nisi, ornare laoreet eros neque nec mi. Proin."
                ),
                id="9788831796781",
            )
            for _ in range(how_many)
        ]
    )


def parse(source, handler):
    parser = XmlParser(context=context, handler=handler)
    parser.from_bytes(source, Books)


def parse_json(source):
    parser = JsonParser(context=context)
    parser.from_bytes(source, Books)


def write(size, obj, writer):
    with xsdata_temp_dir.joinpath(f"benchmark_{size}.xml").open("w") as f:
        serializer = XmlSerializer(writer=writer, context=context)
        serializer.write(f, obj)


def write_json(size, obj):
    with xsdata_temp_dir.joinpath(f"benchmark_{size}.json").open("w") as f:
        serializer = JsonSerializer(context=context)
        serializer.write(f, obj)
