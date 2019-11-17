from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterator, List, Tuple

from jinja2 import Environment, FileSystemLoader, Template
from lxml import etree

from xsdata.models.elements import Schema
from xsdata.models.render import Class
from xsdata.render.python.dataclass.filters import filters
from xsdata.render.python.renderer import PythonRenderer
from xsdata.utils.text import snake_case


class DataclassRenderer(PythonRenderer):
    def __init__(self):
        templates_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            extensions=["jinja2.ext.do"],
        )
        self.env.filters.update(filters)
        self.processed = {}

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    def render_module(self, output: str, imports: List[str]) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:

        module = snake_case(schema.module)
        package_arr = list(map(snake_case, package.split(".")))
        package_arr.append(module)
        package = ".".join(package_arr)

        target = Path.cwd().joinpath(*package_arr)
        class_list = self.list_dependencies(classes)
        class_map = {obj.name: obj for obj in classes}

        # This has to run first, to extract imports and remove them from list
        imports, overrides = self.extract_imports(
            schema, class_list, class_map
        )

        out = []
        for name in class_list:
            obj = class_map[name]
            self.process_class(obj, overrides, parents=[])

            qname = etree.QName(schema.target_namespace, obj.name)
            self.processed[qname.text] = package

            out.append(self.render_class(obj=obj))

        target.mkdir(parents=True, exist_ok=True)
        file_path = target.joinpath(f"{module}.py")
        output = "\n".join(out)

        yield file_path, self.render_module(output=output, imports=imports)

    def extract_imports(self, schema: Schema, class_list, class_map):
        overrides: Dict[str, str] = dict()
        imports: Dict[str, List] = defaultdict(list)
        for name in [c for c in class_list if c not in class_map]:
            class_list.remove(name)
            parts = name.split(":")
            prefix, suffix = parts if len(parts) == 2 else (None, parts[0])

            if suffix in class_list:
                suffix = self.class_name(suffix)
                import_class = "{} as {}".format(suffix, self.class_name(name))
            else:
                suffix = import_class = self.class_name(suffix)

            namespace = schema.nsmap.get(prefix)
            qname = etree.QName(namespace, suffix)
            from_package = self.processed.get(qname.text)
            imports[from_package].append(import_class)

        return imports, overrides
