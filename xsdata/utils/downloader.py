import os
import re
from pathlib import Path
from urllib.parse import urlparse

from xsdata.codegen import opener
from xsdata.codegen.parsers import DefinitionsParser, SchemaParser
from xsdata.logger import logger
from xsdata.models.wsdl import Definitions
from xsdata.models.xsd import Schema


class Downloader:
    """Remote recursive resource downloader.

    Helper class to download a schema or a definitions with all their imports
    locally. The imports paths will be adjusted if necessary.

    Args:
        output: The output path

    Attributes:
        base_path: The base path for the resources
        downloaded: A cache of the downloaded resources
    """

    __slots__ = ("base_path", "downloaded", "output")

    def __init__(self, output: Path):
        """Initialize the downloader."""
        self.output = output
        self.downloaded: dict = {}

    def wget(self, uri: str, location: str | None = None) -> None:
        """Download handler for any uri input with circular protection."""
        if uri not in self.downloaded:
            self.downloaded[uri] = None
            logger.info("Fetching %s", uri)

            input_stream = opener.open(uri).read()  # nosec
            if uri.endswith("wsdl"):
                self.parse_definitions(uri, input_stream)
            else:
                self.parse_schema(uri, input_stream)

            self.write_file(uri, location, input_stream.decode())

    def parse_schema(self, uri: str, content: bytes) -> None:
        """Convert content to a schema instance and process all sub imports."""
        parser = SchemaParser(location=uri)
        schema = parser.from_bytes(content, Schema)
        self.wget_included(schema)

    def parse_definitions(self, uri: str, content: bytes) -> None:
        """Convert content to a definitions instance and process all sub imports."""
        parser = DefinitionsParser(location=uri)
        definitions = parser.from_bytes(content, Definitions)
        self.wget_included(definitions)

        for schema in definitions.schemas:
            self.wget_included(schema)

    def wget_included(self, definition: Schema | Definitions) -> None:
        """Download the definitions included resources."""
        for included in definition.included():
            if included.location:
                schema_location = getattr(included, "schema_location", None)
                self.wget(included.location, schema_location)

    def write_file(self, uri: str, location: str | None, content: str) -> None:
        """Write the downloaded uri to a local file.

        Keep track of all the written file paths, in case we have to
        modify the location attribute in an upcoming schema/definition
        import.

        Args:
            uri: The resource URI
            location: The import location of the resource
            content: The raw content string
        """
        if uri.startswith("file:"):
            # This happens for bundled schemas (xlink.xsd, xml.xsd)
            # which are intercepted by opener and returned as file://
            if not location or location.startswith("file:"):
                raise ValueError(
                    f"Cannot download local file without HTTP location: {uri}\n"
                )

            parsed = urlparse(location)
        else:
            parsed = urlparse(uri)

        rel_path = parsed.netloc + "/" + parsed.path.lstrip("/")
        file_path = self.output.joinpath(rel_path)

        content = self.adjust_imports(file_path.parent, content)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

        logger.info("Writing %s", file_path)
        self.downloaded[uri] = file_path

    def adjust_imports(self, path: Path, content: str) -> str:
        """Update the location of the imports to point to the downloaded files."""
        matches = re.findall(r"ocation=\"(.*)\"", content)
        for match in matches:
            if isinstance(self.downloaded.get(match), Path):
                location = os.path.relpath(self.downloaded[match], path)
                replace = location.replace("\\", "/")
                content = content.replace(f'ocation="{match}"', f'ocation="{replace}"')

        return content
