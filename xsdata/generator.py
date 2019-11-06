import copy
import logging
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Union

from xsdata.models.elements import (
    Attribute,
    ComplexType,
    Element,
    ElementBase,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.templates import Attr, Class
from xsdata.utils.element import append_documentation
from xsdata.utils.text import pascal_case, safe_snake, snake_case

logger = logging.getLogger(__name__)

BaseElement = Union[List[Element], List[ComplexType], List[SimpleType]]


@dataclass
class CodeGenerator:
    INNER_COMPLEX_TYPE_GENERATED = "Inner ComplexType name auto generated"
    schema: Schema
    recovered: int = field(default=0, init=False)
    queue: List[ElementBase] = field(default_factory=list, init=False)
    deck: List[Class] = field(default_factory=list, init=False)
    generators: Dict[type, Callable] = field(default_factory=dict, init=False)

    def generate(self) -> List[Class]:
        """Generate class properties from schema elements and simple/complex
        types."""
        self.generate_elements(self.schema.simple_types)
        self.generate_elements(self.schema.complex_types)
        self.generate_elements(self.schema.elements)

        return self.deck

    def resolve_generator(self, obj: ElementBase) -> Callable:
        """Resolve and cache generator method from object type."""
        clazz = type(obj)
        if clazz not in self.generators:
            method = "generate_{}".format(snake_case(clazz.__name__))
            self.generators[clazz] = getattr(self, method)
        return self.generators[clazz]

    def generate_elements(self, items: BaseElement):
        """Clone and the list of elements and start processing it, use a queue
        because the list can grow for inner types without a standard
        reference."""
        self.queue = copy.deepcopy(list(items))
        while len(self.queue):
            obj = self.queue.pop()
            generator = self.resolve_generator(obj)
            self.deck.append(generator(obj))

    def generate_simple_type(self, obj: SimpleType) -> Class:
        """
        Generate a class property from a SimpleType element.

        Todo:
            * Add support for Union(s)
            * Add support for List(s)
            * Merge all class property generators
        """
        assert obj.restriction is not None

        return Class(
            name=obj.pascal_name,
            attrs=self.generate_class_fields(obj.restriction),
            metadata=obj.restriction.get_restrictions(),
            help=obj.display_help,
        )

    def generate_complex_type(self, obj: ComplexType) -> Class:
        """
        Generate a class property from a ComplexType element.

        Todo:
            * Merge all class property generators
        """
        return Class(
            name=obj.pascal_name,
            extends=obj.extends,
            attrs=self.generate_class_fields(obj),
            help=obj.display_help,
        )

    def generate_element(self, obj: Element):
        """
        Generate a class property from an Element element.

        Todo:
            * Merge all class property generators
        """
        attributes: List[Attr] = []
        if obj.complex_type:
            attributes = self.generate_class_fields(obj.complex_type)
        elif obj.simple_type:
            attributes = self.generate_class_fields(obj.simple_type)

        return Class(
            name=obj.pascal_name,
            extends=obj.extends,
            attrs=attributes,
            help=obj.display_help,
        )

    def generate_class_fields(self, obj: ElementBase) -> List[Attr]:
        result = []
        if (
            isinstance(obj, Attribute)
            or isinstance(obj, Element)
            or isinstance(obj, Restriction)
        ):
            result.append(self.generate_class_field(obj))
        else:
            for child in obj.children():
                result.extend(self.generate_class_fields(child))

        return list(filter(None, result))

    def generate_class_field(
        self, obj: Union[Attribute, Element, Restriction]
    ) -> Optional[Attr]:
        name = obj.raw_name

        metadata = obj.get_restrictions()
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

        return Attr(
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
