from dataclasses import dataclass, field
from typing import Dict, List

from xsdata.models.elements import Schema
from xsdata.models.render import Class
from xsdata.render.python.dataclass.renderer import DataclassRenderer
from xsdata.render.renderer import AbstractRenderer


@dataclass
class CodeWriter:
    renderers: Dict[str, AbstractRenderer] = field(default_factory=dict)

    @property
    def formats(self):
        return list(self.renderers.keys())

    def register_renderer(self, name, renderer: AbstractRenderer):
        self.renderers[name] = renderer

    def get_renderer(self, name):
        if name in self.renderers:
            return self.renderers[name]
        raise ValueError(f"{name} is not a valid {AbstractRenderer.__name__}")

    def write(
        self, schema: Schema, classes: List[Class], package: str, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for file, output in engine.render(schema, classes, package):
            with open(str(file), "w") as fp:
                fp.write(output)


writer = CodeWriter()
writer.register_renderer("pydata", DataclassRenderer())
