from dataclasses import dataclass, field, fields
from typing import Iterator, List

from xsdata.models.elements import (
    AnnotationBase,
    Attribute,
    ComplexType,
    Element,
    ElementBase,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.templates import ClassProperty, FieldProperty
from xsdata.utils.element import (
    append_documentation,
    get_extension_base,
    get_help,
    get_restrictions,
    get_type,
)
from xsdata.utils.text import pascal_case, snake_case


@dataclass
class CodeGenerator:
    INNER_COMPLEX_TYPE_GENERATED = "Inner ComplexType name auto generated"

    schema: Schema
    recovered: int = field(default=0, init=False)

    def generate(self):
        classes = []
        classes.extend(self.generate_simple_types())
        classes.extend(self.generate_complex_types())
        return classes

    def generate_simple_types(self) -> Iterator[ClassProperty]:
        for item in self.schema.simple_types:
            yield self.generate_simple_type(item)

    def generate_simple_type(self, simple_type: SimpleType) -> ClassProperty:
        assert simple_type.restriction is not None

        return ClassProperty(
            name=pascal_case(simple_type.name),
            extends=None,
            fields=self.generate_class_fields(simple_type.restriction),
            metadata=get_restrictions(simple_type.restriction),
            help=get_help(simple_type),
        )

    def generate_complex_types(self) -> Iterator[ClassProperty]:
        while len(self.schema.complex_types):
            complex_type = self.schema.complex_types.pop()
            yield self.generate_complex_type(complex_type)

    def generate_complex_type(self, obj: ComplexType) -> ClassProperty:
        return ClassProperty(
            name=pascal_case(obj.name),
            extends=get_extension_base(obj),
            fields=self.generate_class_fields(obj),
            metadata=dict(),
            help=get_help(obj),
        )

    def generate_class_fields(self, obj: ElementBase) -> List[FieldProperty]:
        result = []
        if (
            isinstance(obj, Attribute)
            or isinstance(obj, Element)
            or isinstance(obj, Restriction)
        ):
            result.append(self.generate_class_field(obj))
        elif isinstance(obj, ElementBase):
            for f in fields(obj):
                value = getattr(obj, f.name)
                if not isinstance(value, list):
                    value = [value]

                for v in value:
                    if isinstance(v, ElementBase):
                        result.extend(self.generate_class_fields(v))
        return result

    def generate_class_field(self, obj: AnnotationBase) -> FieldProperty:
        name = getattr(obj, "name", None)
        metadata = get_restrictions(obj)
        metadata.update(
            dict(name=name, type=obj.__class__.__name__, help=get_help(obj))
        )

        type_ = get_type(obj)
        if not type_ and isinstance(obj, Element) and obj.complex_type:
            self.recover_complex_type(obj)
            type_ = get_type(obj)

        return FieldProperty(
            name=snake_case(name) if name else "value",
            default=getattr(obj, "default", None),
            metadata=metadata,
            type=type_ or "str",
        )

    def recover_complex_type(self, obj: Element):
        assert obj.complex_type is not None
        self.recovered += 1
        obj.type = "{}Type{}".format(pascal_case(obj.name), self.recovered)
        obj.complex_type.name = obj.type
        append_documentation(
            obj.complex_type, self.INNER_COMPLEX_TYPE_GENERATED
        )
        self.schema.complex_types.insert(0, obj.complex_type)
        obj.complex_type = None
