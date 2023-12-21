import argparse
import statistics
from timeit import Timer

from tests import xsdata_temp_dir
from tests.integration.benchmarks.utils import (
    make_books,
    parse,
    parse_json,
    write,
    write_json,
)
from xsdata.formats.dataclass.parsers import JsonParser, handlers
from xsdata.formats.dataclass.serializers import JsonSerializer, writers

if __name__ == "__main__":
    components = [
        "LxmlEventHandler",
        "XmlEventHandler",
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
    print(f"avg {statistics.mean(result)}")
    print(f"med {statistics.median(result)}")
    print(f"stdev {statistics.stdev(result)}")
