from pathlib import Path
from typing import Iterator, List, Set, Tuple

from jinja2 import Environment, FileSystemLoader, Template
from toposort import toposort_flatten

from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.models.render import Class, Renderer
from xsdata.render.python.dataclass.filters import arguments
from xsdata.render.python.dataclass.utils import replace_words
from xsdata.utils import text
from xsdata.utils.text import snake_case, strip_prefix


class DataclassRenderer(Renderer):
    def __init__(self):
        templates_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(loader=FileSystemLoader(str(templates_dir)),)
        self.env.filters["arguments"] = arguments

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    def render(
        self, schema: Schema, classes: List[Class], target: Path
    ) -> Iterator[Tuple[Path, str]]:
        assert schema.location is not None

        classes = self.prepare_classes(classes)
        imports = self.get_schema_imports(schema)

        module = snake_case(schema.location.stem)
        target.mkdir(parents=True, exist_ok=True)
        file_path = target.joinpath(f"{module}.py")

        output = "\n".join(map(self.render_class, classes))
        yield file_path, self.render_module(output=output, imports=imports)

    def render_module(self, output: str, imports: List[str]) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    @staticmethod
    def get_schema_imports(schema: Schema):
        result = []
        for location in schema.sub_schemas():
            path = Path(location)
            parts = list(path.parent.parts)
            parts.append(path.stem)
            result.append(
                "from .{} import *".format(".".join(map(snake_case, parts)))
            )
        return result

    @classmethod
    def prepare_classes(cls, classes: List[Class]):
        cls.convert_names(classes)
        classes = cls.sort_classes(classes)
        return classes

    @classmethod
    def convert_names(cls, classes: List[Class]):
        for obj in classes:
            cls.convert_names(obj.inner)
            obj.name = cls.class_name(obj.name)

            if obj.extends:
                obj.extends = cls.type_name(obj.extends)

            for attr in obj.attrs:
                attr.name = cls.attribute_name(attr.name)
                attr.type = cls.type_name(attr.type)
                attr.local_name = strip_prefix(attr.local_name)

    @classmethod
    def class_name(cls, name: str) -> str:
        return text.pascal_case(name)

    @classmethod
    def type_name(cls, name: str) -> str:
        return XSDType.get_local(name) or cls.class_name(strip_prefix(name))

    @classmethod
    def attribute_name(cls, name: str) -> str:
        name = strip_prefix(name)
        return text.snake_case(replace_words.get(name.lower(), name))

    @classmethod
    def sort_classes(cls, classes: List[Class]) -> List[Class]:
        index = {obj.name: obj for obj in classes}
        deps = {obj.name: cls.collect_deps(obj) for obj in classes}

        return [index[name] for name in toposort_flatten(deps) if name in deps]

    @classmethod
    def collect_deps(cls, obj: Class) -> Set[str]:
        dependencies = {attr.type for attr in obj.attrs}
        if obj.extends:
            dependencies.add(obj.extends)
        for inner in obj.inner:
            dependencies.update(cls.collect_deps(inner))
        return dependencies
