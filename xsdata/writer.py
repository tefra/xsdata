from dataclasses import dataclass, field
from typing import Dict, List

from xsdata.codegen.generator import AbstractGenerator
from xsdata.codegen.python.dataclass.generator import DataclassGenerator
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema


@dataclass
class CodeWriter:
    generators: Dict[str, AbstractGenerator] = field(default_factory=dict)

    @property
    def formats(self):
        return list(self.generators.keys())

    def register_generator(self, name, renderer: AbstractGenerator):
        self.generators[name] = renderer

    def get_renderer(self, name):
        if name in self.generators:
            return self.generators[name]
        raise ValueError(f"{name} is not a valid {AbstractGenerator.__name__}")

    def write(
        self, schema: Schema, classes: List[Class], package: str, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for file, output in engine.render(schema, classes, package):
            with open(str(file), "w") as fp:
                fp.write(output)

    def print(
        self, schema: Schema, classes: List[Class], package: str, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for package, item in engine.print(schema, classes, package):
            extensions = sorted(item.extensions)
            extends: str = f"({', '.join(extensions)})" if extensions else ""
            print(f"{package}.{item.name}{extends}")

            for attr in sorted(item.attrs, key=lambda x: x.name):
                print(f"    {attr.name}: {attr.type} = {attr.default}")


writer = CodeWriter()
writer.register_generator("pydata", DataclassGenerator())
