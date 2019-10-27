from dataclasses import fields
from typing import Any, Dict, Optional

from xsdata.models.elements import (
    Annotation,
    AnnotationBase,
    Attribute,
    Documentation,
    ElementModel,
    Restriction,
    RestrictionType,
)


def get_help(element: AnnotationBase):
    if (
        element.annotation
        and element.annotation.documentation
        and element.annotation.documentation.text
    ):
        return element.annotation.documentation.text
    return None


def get_type(element: ElementModel) -> Optional[str]:
    if isinstance(element, Restriction):
        return element.base
    elif isinstance(element, Attribute):
        if (
            element.simple_type
            and element.simple_type
            and element.simple_type.restriction
            and element.simple_type.restriction.base
        ):
            return element.simple_type.restriction.base

    return getattr(element, "type", None)


def get_restrictions(element: ElementModel) -> Dict[str, Any]:
    if isinstance(element, Restriction):
        return {
            res.name: getattr(element, res.name).value
            for res in fields(element)
            if isinstance(getattr(element, res.name), RestrictionType)
        }
    return dict()


def inject_documentation(element: AnnotationBase, string: str):
    if element.annotation is None:
        element.annotation = Annotation.build()
    if element.annotation.documentation is None:
        element.annotation.documentation = Documentation.build()
    if element.annotation.documentation.text is None:
        element.annotation.documentation.text = ""

    element.annotation.documentation.text = "{}\n{}".format(
        element.annotation.documentation.text, string
    ).strip()
