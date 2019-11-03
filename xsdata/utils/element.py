from dataclasses import fields
from typing import Any, Dict, Optional

from xsdata.models.elements import (
    Annotation,
    AnnotationBase,
    Attribute,
    ComplexType,
    Documentation,
    ElementBase,
    Restriction,
    RestrictionType,
)
from xsdata.utils import text

XSD_TYPES = {
    "xs:string": "str",
    "xs:decimal": "float",
    "xs:integer": "int",
    "xs:boolean": "bool",
    "xs:date": "str",
    "xs:time": "str",
}


def get_help(element: AnnotationBase):
    if (
        element.annotation
        and element.annotation.documentation
        and element.annotation.documentation.text
    ):
        return element.annotation.documentation.text
    return None


def get_type(element: ElementBase) -> Optional[str]:
    type_var = None
    if isinstance(element, Restriction):
        type_var = element.base
    elif isinstance(element, Attribute):
        if (
            element.simple_type
            and element.simple_type
            and element.simple_type.restriction
            and element.simple_type.restriction.base
        ):
            type_var = element.simple_type.restriction.base

    if type_var is None:
        type_var = getattr(element, "type", None)

    if type_var:
        type_var = XSD_TYPES.get(type_var) or text.pascal_case(type_var)

    return type_var


def get_restrictions(element: ElementBase) -> Dict[str, Any]:
    if isinstance(element, Restriction):
        return {
            res.name: getattr(element, res.name).value
            for res in fields(element)
            if isinstance(getattr(element, res.name), RestrictionType)
        }
    return dict()


def get_extension_base(element: ComplexType) -> Optional[str]:
    if (
        element.complex_content
        and element.complex_content.extension
        and element.complex_content.extension.base
    ):
        return text.pascal_case(element.complex_content.extension.base)
    return None


def append_documentation(element: AnnotationBase, string: str):
    if element.annotation is None:
        element.annotation = Annotation.build()
    if element.annotation.documentation is None:
        element.annotation.documentation = Documentation.build()
    if element.annotation.documentation.text is None:
        element.annotation.documentation.text = ""

    element.annotation.documentation.text = "{}\n{}".format(
        element.annotation.documentation.text, string
    ).strip()
