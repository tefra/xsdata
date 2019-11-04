import copy
import logging
from dataclasses import dataclass, field, fields
from typing import Callable, Dict, Iterator, List, Optional, Union

from xsdata.models.elements import (
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
    get_restrictions,
)
from xsdata.utils.text import pascal_case, safe_snake, snake_case

logger = logging.getLogger(__name__)


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

        name = obj.pascal_name

        assert name is not None

        return ClassProperty(
            name=name,
            extends=None,
            fields=self.generate_class_fields(obj.restriction),
            metadata=get_restrictions(obj.restriction),
            help=obj.display_help,
        )

    def generate_complex_type(self, obj: ComplexType) -> ClassProperty:
        return ClassProperty(
            name=pascal_case(obj.name),
            extends=get_extension_base(obj),
            fields=self.generate_class_fields(obj),
            metadata=dict(),
            help=obj.display_help,
        )

    def generate_element(self, obj: Element):
        name = obj.pascal_name

        if not name:
            raise NotImplementedError(
                "Failed to detect name for element: {}".format(obj)
            )

        if obj.complex_type is not None:
            _fields = self.generate_class_fields(obj.complex_type)
            _extends = get_extension_base(obj.complex_type)
        elif obj.simple_type is not None:
            _fields = self.generate_class_fields(obj.simple_type)
            _extends = None
        elif obj.type is not None:
            _fields = []
            _extends = obj.display_type
        else:
            raise NotImplementedError(
                "Failed to generate class property from element {}".format(
                    obj.name
                )
            )

        return ClassProperty(
            name=name,
            extends=_extends,
            fields=_fields,
            metadata=dict(),
            help=obj.display_help,
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
        return list(filter(None, result))

    def generate_class_field(
        self, obj: Union[Attribute, Element, Restriction]
    ) -> Optional[FieldProperty]:
        name = obj.raw_name

        if not name:
            logger.warning("Failed to detect name for element: {}".format(obj))
            return None

        metadata = get_restrictions(obj)
        metadata.update(
            dict(name=name, type=obj.__class__.__name__, help=obj.display_help)
        )
        display_type = obj.display_type

        if not display_type and isinstance(obj, Element) and obj.complex_type:
            self.recover_complex_type(obj)
            display_type = obj.display_type

        if not display_type:
            logger.warning(
                "Failed to detect type for element: {}".format(name)
            )
            return None

        return FieldProperty(
            name=safe_snake(name),
            default=getattr(obj, "default", None),
            metadata=metadata,
            type=display_type,
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
