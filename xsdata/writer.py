import copy
import logging
from dataclasses import fields
from os import path
from typing import List

import black
from jinja2 import Environment, FileSystemLoader, Template
from toposort import toposort_flatten

from xsdata.models.elements import (
    AnnotationBase,
    Attribute,
    ComplexType,
    Element,
    ElementModel,
    Restriction,
    RestrictionType,
    Schema,
    SimpleType,
)
from xsdata.models.templates import ClassItem, FieldItem
from xsdata.utils.elements import (
    get_help,
    get_restrictions,
    get_type,
    inject_documentation,
)
from xsdata.utils.text import pascal_case, snake_case

template_dir = path.join(path.dirname(path.abspath(__file__)), "templates")

logger = logging.getLogger(__name__)


class SchemaWriter:
    types = {
        "xs:string": "str",
        "xs:decimal": "float",
        "xs:integer": "int",
        "xs:boolean": "bool",
        "xs:date": "str",
        "xs:time": "str",
    }

    def __init__(self, schema: Schema, theme: str):
        self.schema = copy.deepcopy(schema)
        self.index = 0
        self.env = Environment(
            loader=FileSystemLoader(path.join(template_dir, theme))
        )

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.tpl".format(name))

    def write(self):
        content = []
        content.extend(
            [
                self.template("class").render(item.as_dict())
                for item in self.build_simple_types()
            ]
        )
        content.extend(
            [
                self.template("class").render(item.as_dict())
                for item in self.build_complex_types()
            ]
        )

        output = self.black_code("\n\n".join(content))
        with open("hello.py", "w") as f:
            f.write(self.template("module").render(output=output))

    def build_simple_types(self) -> List[ClassItem]:
        return [
            self.build_simple_type(item) for item in self.schema.simple_types
        ]

    def build_simple_type(self, item: SimpleType) -> ClassItem:
        assert item.restriction is not None

        metadata = {
            res.name: getattr(item.restriction, res.name).value
            for res in fields(item.restriction)
            if isinstance(getattr(item.restriction, res.name), RestrictionType)
        }

        return ClassItem(
            name=pascal_case(item.name),
            extends=None,
            fields=self.build_class_fields(item.restriction),
            metadata=metadata,
            help=get_help(item),
        )

    def build_complex_types(self) -> List[ClassItem]:

        matrix = {}
        items = {}
        while len(self.schema.complex_types):
            complex_type = self.schema.complex_types.pop()
            class_item = self.build_complex_type(complex_type)
            items[class_item.name] = class_item
            matrix[class_item.name] = set(
                [field.type for field in class_item.fields]
            )

        return [
            items[name] for name in toposort_flatten(matrix) if name in items
        ]

    def build_complex_type(self, item: ComplexType) -> ClassItem:
        extends = (
            "({})".format(pascal_case(item.complex_content.extension.base))
            if (
                item.complex_content
                and item.complex_content.extension
                and item.complex_content.extension.base
            )
            else None
        )

        return ClassItem(
            name=pascal_case(item.name),
            extends=extends,
            fields=self.build_class_fields(item),
            metadata=dict(),
            help=get_help(item),
        )

    def build_class_fields(self, item: ElementModel) -> List[FieldItem]:
        result = []
        if (
            isinstance(item, Attribute)
            or isinstance(item, Element)
            or isinstance(item, Restriction)
        ):
            result.append(self.build_field(item))
        elif isinstance(item, ElementModel):
            for field in fields(item):
                value = getattr(item, field.name)
                if not isinstance(value, list):
                    value = [value]

                for v in value:
                    if isinstance(v, ElementModel):
                        result.extend(self.build_class_fields(v))
        return result

    def build_field(self, item: AnnotationBase) -> FieldItem:
        name = getattr(item, "name", None)
        metadata = dict(
            name=name, type=item.__class__.__name__, help=get_help(item)
        )
        metadata.update(get_restrictions(item))

        typing = get_type(item)
        if typing is None:
            if isinstance(item, Element) and item.complex_type is not None:
                self.inject_complex_type(item)
                typing = get_type(item)
            else:
                typing = "xs:string"

        return FieldItem(
            name=snake_case(name) if name else "value",
            default=getattr(item, "default", None),
            metadata=metadata,
            type=(
                self.types[typing]
                if typing in self.types
                else pascal_case(typing)
            ),
        )

    def inject_complex_type(self, item: Element):
        assert item.complex_type is not None

        self.index += 1
        item.type = "{}Type{}".format(pascal_case(item.name), self.index)
        complex_type = item.complex_type
        complex_type.name = item.type
        inject_documentation(
            complex_type, "Inner ComplexType name auto generated"
        )
        item.complex_type = None
        self.schema.complex_types.insert(0, complex_type)

    @staticmethod
    def black_code(string: str):
        try:
            mode = black.FileMode(
                is_pyi=False, string_normalization=True, line_length=79
            )
            return black.format_file_contents(string, fast=True, mode=mode)
        except Exception as e:
            logger.exception(e)
            return string
