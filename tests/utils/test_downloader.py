import tempfile
from pathlib import Path
from unittest import mock
from unittest import TestCase
from urllib.request import urlopen

from tests import fixtures_dir
from xsdata.models.xsd import Import
from xsdata.models.xsd import Schema
from xsdata.utils.downloader import Downloader


class DownloaderTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.downloader = Downloader(Path.cwd())

    @mock.patch.object(Downloader, "write_file")
    def test_wget_with_schema(self, mock_write_file):
        path = fixtures_dir.joinpath("books/schema.xsd")
        content = path.read_bytes()
        uri = path.as_uri()

        self.downloader.wget(uri)
        self.downloader.wget(uri)  # once
        mock_write_file.assert_called_once_with(uri, None, content.decode())

    @mock.patch.object(Downloader, "write_file")
    def test_wget_with_definitions(self, mock_write_file):
        wsdl = fixtures_dir.joinpath("hello/hello.wsdl").as_uri()
        xsd = fixtures_dir.joinpath("hello/hello.xsd").as_uri()

        self.downloader.wget(wsdl)
        mock_write_file.assert_has_calls(
            [
                mock.call(xsd, "hello.xsd", urlopen(xsd).read().decode()),
                mock.call(wsdl, None, urlopen(wsdl).read().decode()),
            ]
        )

    @mock.patch.object(Downloader, "wget")
    def test_wget_included(self, mock_wget):
        schema = Schema(
            imports=[
                Import(location="foo.xsd"),
                Import(),
                Import(location="foo.xsd", schema_location="../foo.xsd"),
            ]
        )

        self.downloader.wget_included(schema)
        mock_wget.assert_has_calls(
            [
                mock.call(schema.imports[0].location, None),
                mock.call(
                    schema.imports[2].location, schema.imports[2].schema_location
                ),
            ]
        )

    def test_adjust_base_path(self):
        first = "file:///schemas/air_v48_0/Air.wsdl"
        second = "file:///schemas/air_v48_0/AirAbstract.wsdl"
        third = "file:///schemas/common_v48_0/CommonReqRsp.xsd"
        fourth = "http://www.w3.org/2001/xml.xsd"
        path = Path(first)

        self.downloader.adjust_base_path(first)
        self.assertEqual(path.parent, self.downloader.base_path)

        self.downloader.adjust_base_path(second)
        self.assertEqual(path.parent, self.downloader.base_path)

        self.downloader.adjust_base_path(third)
        self.assertEqual(path.parent.parent, self.downloader.base_path)

        self.downloader.adjust_base_path(fourth)
        self.assertEqual(path.parent.parent, self.downloader.base_path)

    def test_adjust_imports(self):
        content = (
            '<hypothetical location="http://foo.com/bar.xsd" />\n'
            '<hypothetical schemaLocation="http://foo.com/bar/bar.xsd" />\n'
            '<hypothetical location="http://bar.com/foo.xsd" />\n'
            '<hypothetical location="../something.xsd" />\n'
        )

        with tempfile.TemporaryDirectory() as dir:
            dir_path = Path(dir)
            self.downloader.base_path = "http://foo.com/"
            self.downloader.output = dir_path

            self.downloader.downloaded.update(
                {
                    "http://foo.com/bar.xsd": dir_path.joinpath("some/place/bar.xsd"),
                    "http://foo.com/bar/bar.xsd": dir_path.joinpath("other/bar.xsd"),
                }
            )

            result = self.downloader.adjust_imports(dir_path, content)
            expected = (
                '<hypothetical location="some/place/bar.xsd" />\n'
                '<hypothetical schemaLocation="other/bar.xsd" />\n'
                '<hypothetical location="http://bar.com/foo.xsd" />\n'
                '<hypothetical location="../something.xsd" />\n'
            )
            self.assertEqual(expected, result)

            result = self.downloader.adjust_imports(dir_path.joinpath("foo"), content)
            expected = (
                '<hypothetical location="../some/place/bar.xsd" />\n'
                '<hypothetical schemaLocation="../other/bar.xsd" />\n'
                '<hypothetical location="http://bar.com/foo.xsd" />\n'
                '<hypothetical location="../something.xsd" />\n'
            )
            self.assertEqual(expected, result)

    def test_write_external_file(self):
        uri = "http://www.w3.org/2001/xml.xsd"
        content = "foo"

        with tempfile.TemporaryDirectory() as dir:
            output_path = Path(dir)
            file_path = output_path.joinpath("xml.xsd")
            self.downloader.output = output_path
            self.downloader.write_file(uri, "foo", content)

            self.assertEqual(content, file_path.read_text())
            self.assertEqual(file_path, self.downloader.downloaded[uri])
            self.assertEqual(file_path, self.downloader.downloaded["foo"])

    def test_write_relative_file(self):
        uri = "http://www.w3.org/2001/xml.xsd"
        content = "foo"
        self.downloader.base_path = "http://www.w3.org"

        with tempfile.TemporaryDirectory() as dir:
            output_path = Path(dir)
            file_path = output_path.joinpath("2001/xml.xsd")
            self.downloader.output = output_path
            self.downloader.write_file(uri, None, content)

            self.assertEqual(content, file_path.read_text())
            self.assertEqual(file_path, self.downloader.downloaded[uri])
