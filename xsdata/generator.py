import copy
from dataclasses import dataclass, field, fields
from typing import Callable, Dict, Iterator, List

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
    queue: List[ElementBase] = field(default_factory=list, init=False)
    generators: Dict[type, Callable] = field(default_factory=dict, init=False)

    def generate(self):
        classes = []
        classes.extend(self.generate_elements(self.schema.simple_types))
        classes.extend(self.generate_elements(self.schema.complex_types))
        classes.extend(self.generate_elements(self.schema.elements))
        return classes

    def resolve_generator(self, obj: ElementBase) -> Callable:
        clazz = type(obj)
        if clazz not in self.generators:
            method = "generate_{}".format(snake_case(clazz.__name__))
            self.generators[clazz] = getattr(self, method)
        return self.generators[clazz]

    def generate_elements(
        self, elements: List[ElementBase]
    ) -> Iterator[ClassProperty]:
        self.queue = copy.deepcopy(elements)
        while len(self.queue):
            obj = self.queue.pop()
            generator = self.resolve_generator(obj)
            yield generator(obj)

    def generate_simple_type(self, obj: SimpleType) -> ClassProperty:
        assert obj.restriction is not None

        return ClassProperty(
            name=pascal_case(obj.name),
            extends=None,
            fields=self.generate_class_fields(obj.restriction),
            metadata=get_restrictions(obj.restriction),
            help=get_help(obj),
        )

    def generate_complex_type(self, obj: ComplexType) -> ClassProperty:
        return ClassProperty(
            name=pascal_case(obj.name),
            extends=get_extension_base(obj),
            fields=self.generate_class_fields(obj),
            metadata=dict(),
            help=get_help(obj),
        )

    def generate_element(self, obj: Element):
        if obj.complex_type:
            _fields = self.generate_class_fields(obj.complex_type)
            _extends = get_extension_base(obj.complex_type)
        elif obj.simple_type:
            _fields = self.generate_class_fields(obj.simple_type)
            _extends = None
        else:
            raise NotImplementedError(
                "Class property from element without complex or simple type"
            )

        return ClassProperty(
            name=pascal_case(obj.name),
            extends=_extends,
            fields=_fields,
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
        self.queue.insert(0, obj.complex_type)
        obj.complex_type = None
