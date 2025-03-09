import json
import os

from click.testing import CliRunner

from tests import fixtures_dir, root
from xsdata.cli import cli
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils.testing import filter_none, load_class

os.chdir(root)


def test_json_documents() -> None:
    filepath = fixtures_dir.joinpath("stripe")
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "generate",
            str(filepath.joinpath("samples")),
            f"--config={filepath.joinpath('.xsdata.xml')!s}",
        ],
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Balance")

    parser = JsonParser()
    config = SerializerConfig(indent="  ")
    serializer = JsonSerializer(config=config)

    for sample in filepath.joinpath("samples").glob("*.json"):
        ori = sample.read_text()
        obj = parser.from_string(ori, clazz)
        actual = serializer.render(obj)

        assert filter_none(json.loads(ori)) == filter_none(json.loads(actual))
