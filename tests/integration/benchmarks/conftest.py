import logging

from tests import xsdata_temp_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.logger import logger
from xsdata.models.datatype import XmlDate

xsdata_temp_dir.mkdir(parents=True, exist_ok=True)
context = XmlContext()


def pytest_unconfigure(config):
    for tmp_file in xsdata_temp_dir.glob("*"):
        tmp_file.unlink()

    xsdata_temp_dir.rmdir()


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


if __name__ == "__main__":
    import argparse
    import statistics
    from xsdata.formats.dataclass.serializers import writers
    from xsdata.formats.dataclass.parsers import handlers
    from timeit import Timer

    components = [
        "LxmlEventHandler",
        "LxmlSaxHandler",
        "XmlEventHandler",
        "XmlSaxHandler",
        "LxmlEventWriter",
        "XmlEventWriter",
        "JsonParser",
        "JsonSerializer",
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--component", choices=components, required=True)
    parser.add_argument("-n", "--number", default=1000, type=int)
    parser.add_argument("-r", "--repeat", default=10, type=int)
    args = parser.parse_args()

    if args.component in writers.__all__:
        component = getattr(writers, args.component)
        books = make_books(args.number)
        t = Timer(lambda: write(args.number, books, component))
    elif args.component in handlers.__all__:
        fixture = xsdata_temp_dir.joinpath(f"benchmark_{args.number}.xml")
        if not fixture.exists():
            write(args.number, make_books(args.number), writers.XmlEventWriter)

        component = getattr(handlers, args.component)
        t = Timer(lambda: parse(fixture.read_bytes(), component))
    elif args.component == "JsonParser":
        component = JsonParser
        fixture = xsdata_temp_dir.joinpath(f"benchmark_{args.number}.json")
        if not fixture.exists():
            write_json(args.number, make_books(args.number))

        t = Timer(lambda: parse_json(fixture.read_bytes()))
    elif args.component == "JsonSerializer":
        component = JsonSerializer
        books = make_books(args.number)
        t = Timer(lambda: write_json(args.number, books))

    print(f"Benchmark {component.__name__} - n{args.number}/r{args.repeat}")
    result = t.repeat(repeat=args.repeat, number=1)
    print("avg {}".format(statistics.mean(result)))
    print("med {}".format(statistics.median(result)))
    print("stdev {}".format(statistics.stdev(result)))
