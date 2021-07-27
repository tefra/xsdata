import json
import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils.testing import load_class

os.chdir(root)


def test_json_documents():
    filepath = fixtures_dir.joinpath("series")
    package = "tests.fixtures.series"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(filepath.joinpath("samples")), "--package", package]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Series")

    parser = JsonParser()
    config = SerializerConfig(pretty_print=True)
    serializer = JsonSerializer(config=config)

    for i in range(1, 3):
        ori = filepath.joinpath(f"samples/show{i}.json").read_text()
        obj = parser.from_string(ori, clazz)
        actual = serializer.render(obj)

        assert filter_none(json.loads(ori)) == filter_none(json.loads(actual))


def filter_none(d):
    if isinstance(d, dict):
        return {k: filter_none(v) for k, v in d.items() if v is not None}
    else:
        return d
