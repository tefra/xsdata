import random

import pytest

from tests import xsdata_temp_dir
from tests.integration.benchmarks.utils import make_books, parse, write
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, XmlEventHandler
from xsdata.formats.dataclass.serializers.writers import LxmlEventWriter, XmlEventWriter

context = XmlContext()
readers_list = [
    LxmlEventHandler,
    XmlEventHandler,
]
writers_list = [
    XmlEventWriter,
    LxmlEventWriter,
]

random.shuffle(readers_list)
random.shuffle(writers_list)

numbers = [100, 1000, 10000]

fixtures = {number: make_books(number) for number in numbers}


@pytest.mark.benchmark(disable_gc=True, group="Serialize")
@pytest.mark.parametrize("number", numbers)
@pytest.mark.parametrize("writer", writers_list)
def test_serialize(benchmark, writer, number):
    benchmark(write, number, fixtures[number], writer)


@pytest.mark.benchmark(disable_gc=True, group="Parse")
@pytest.mark.parametrize("number", numbers)
@pytest.mark.parametrize("handler", readers_list)
def test_parse(benchmark, handler, number):
    src = xsdata_temp_dir.joinpath(f"benchmark_{number}.xml").read_bytes()
    benchmark(parse, src, handler)
