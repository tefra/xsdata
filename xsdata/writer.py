from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from xsdata.models.elements import Schema
from xsdata.models.render import Class, Renderer
from xsdata.render.python.dataclass.renderer import DataclassRenderer


@dataclass
class CodeWriter:
    renderers: Dict[str, Renderer] = field(default_factory=dict)

    @property
    def formats(self):
        return list(self.renderers.keys())

    def register_renderer(self, name, renderer: Renderer):
        self.renderers[name] = renderer

    def get_renderer(self, name):
        if name in self.renderers:
            return self.renderers[name]
        raise ValueError(f"{name} is not a valid {Renderer.__name__}")

    def write(
        self, schema: Schema, classes: List[Class], target: Path, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for file, output in engine.render(schema, classes, target):
            with open(str(file), "w") as fp:
                fp.write(output)

    @staticmethod
    def adjust_target(target: Path, xsd_path: Path, schema: Schema) -> Path:
        """
        From the number of parent directories in the path of the schema import
        location attempt to figure how many levels of the origin xsd path to
        include in the target path.

        Example:
            target: ./
            schema: ./v20/air/Air.xsd imports
                        ../common/CommonTypes.xsd
                        ../../security/Header.xsd
            adjusted target: ./v20/air/

        :param target: The original requested target path
        :type target: :class:`pathlib.Path`
        :param xsd_path: The file path of the xsd
        :type xsd_path: :class:`pathlib.Path`
        :param schema: The parsed Schema instance
        :type schema: :class:`xsdata.models.elements.Schema`
        :return: The adjusted target path
        :rtype: :class:`pathlib.Path`
        """
        sub: List[str] = []
        for _import in schema.imports:
            if _import.schema_location is None:
                continue

            spp = (
                xsd_path.parent.joinpath(_import.schema_location)
                .resolve()
                .parent.parts
            )
            ppp = xsd_path.parent.parts

            i = 0
            while i < len(ppp) and i < len(spp) and ppp[i] == spp[i]:
                i += 1

            if len(ppp[i:]) > len(sub):
                sub = list(ppp[i:])

        if len(sub):
            return target.joinpath(*sub)
        return target


writer = CodeWriter()
writer.register_renderer("pydata", DataclassRenderer())
