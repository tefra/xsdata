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
            self.print_class(package, item)

    def print_class(self, package: str, obj: Class, indent: int = 0):

        extensions = ", ".join(sorted([ext.name for ext in obj.extensions]))
        print(f"\n{indent * ' '}{package}.{obj.name}({extensions})")

        for attr in sorted(obj.attrs, key=lambda x: x.name):
            params = [("default", attr.default)]
            params.extend(
                [
                    (key, value)
                    for key, value in sorted(attr.restrictions.items())
                ]
            )
            print(f"{(indent + 4) * ' '}{attr.name}: {attr.type} = {params}")

        for inner in sorted(obj.inner, key=lambda x: x.name):
            self.print_class(f"{package}.{obj.name}", inner, indent + 4)


writer = CodeWriter()
writer.register_generator("pydata", DataclassGenerator())
