import os
import re
from pathlib import Path
from typing import Dict, Optional, Union

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

    __slots__ = ("output", "base_path", "downloaded")

    def __init__(self, output: Path):
        self.output = output
        self.base_path: Optional[Path] = None
        self.downloaded: Dict = {}

    def wget(self, uri: str, location: Optional[str] = None):
        """Download handler for any uri input with circular protection."""
        if not (uri in self.downloaded or (location and location in self.downloaded)):
            self.downloaded[uri] = None
            self.downloaded[location] = None
            self.adjust_base_path(uri)

            logger.info("Fetching %s", uri)

            input_stream = opener.open(uri).read()  # nosec
            if uri.endswith("wsdl"):
                self.parse_definitions(uri, input_stream)
            else:
                self.parse_schema(uri, input_stream)

            self.write_file(uri, location, input_stream.decode())

    def parse_schema(self, uri: str, content: bytes):
        """Convert content to a schema instance and process all sub imports."""
        parser = SchemaParser(location=uri)
        schema = parser.from_bytes(content, Schema)
        self.wget_included(schema)

    def parse_definitions(self, uri: str, content: bytes):
        """Convert content to a definitions instance and process all sub imports."""
        parser = DefinitionsParser(location=uri)
        definitions = parser.from_bytes(content, Definitions)
        self.wget_included(definitions)

        for schema in definitions.schemas:
            self.wget_included(schema)

    def wget_included(self, definition: Union[Schema, Definitions]):
        """Download the definitions included resources."""
        for included in definition.included():
            if included.location:
                schema_location = getattr(included, "schema_location", None)
                self.wget(included.location, schema_location)

    def adjust_base_path(self, uri: str):
        """Adjust base path for every new uri loaded.

        Example runs:
            - file:///schemas/air_v48_0/Air.wsdl -> file:///schemas/air_v48_0
            - file:///schemas/common_v48_0/CommonReqRsp.xsd -> file:///schemas

        Args:
            uri: A resource location URI
        """
        if not self.base_path:
            self.base_path = Path(uri).parent
            logger.info("Setting base path to %s", self.base_path)
        else:
            common_path = os.path.commonpath((str(self.base_path) or "", uri))

            if common_path:
                common_path_path = Path(common_path)
                if common_path_path < self.base_path:
                    self.base_path = Path(common_path)
                    logger.info("Adjusting base path to %s", self.base_path)

    def adjust_imports(self, path: Path, content: str) -> str:
        """Update the location of the imports to point to the downloaded files."""
        matches = re.findall(r"ocation=\"(.*)\"", content)
        for match in matches:
            if isinstance(self.downloaded.get(match), Path):
                location = os.path.relpath(self.downloaded[match], path)
                replace = str(location).replace("\\", "/")
                content = content.replace(f'ocation="{match}"', f'ocation="{replace}"')

        return content

    def write_file(self, uri: str, location: Optional[str], content: str):
        """Write the downloaded uri to a local file.

        Keep track of all the written file paths, in case we have to
        modify the location attribute in an upcoming schema/definition
        import.

        Args:
            uri: The resource URI
            location: The import location of the resource
            content: The raw content string
        """
        common_path = os.path.commonpath((self.base_path or "", uri))
        if common_path:
            file_path = self.output.joinpath(Path(uri).relative_to(common_path))
        else:
            file_path = self.output.joinpath(Path(uri).name)

        content = self.adjust_imports(file_path.parent, content)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

        logger.info("Writing %s", file_path)
        self.downloaded[uri] = file_path

        if location:
            self.downloaded[location] = file_path
