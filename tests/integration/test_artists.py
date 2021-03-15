import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.utils.testing import load_class

os.chdir(root)


def test_xml_documents():
    filepath = fixtures_dir.joinpath("artists")
    package = "tests.fixtures.artists"
    runner = CliRunner()
    result = runner.invoke(cli, [str(filepath), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Metadata")

    parser = XmlParser()
    serializer = XmlSerializer(writer=XmlEventWriter)
    serializer.config.pretty_print = True
    serializer.config.xml_declaration = False
    ns_map = {None: "http://musicbrainz.org/ns/mmd-2.0#"}

    for i in range(1, 4):
        ap = filepath.joinpath(f"art00{i}.xml")
        obj = parser.from_path(ap, clazz)
        actual = serializer.render(obj, ns_map)

        assert ap.read_bytes().splitlines() == actual.encode().splitlines()
