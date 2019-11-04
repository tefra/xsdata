from dataclasses import fields
from typing import Any as Anything
from typing import Dict, Optional

from xsdata.models.elements import (
    All,
    Annotation,
    AnnotationBase,
    Any,
    Attribute,
    Choice,
    ComplexType,
    Documentation,
    Element,
    ElementBase,
    Group,
    Restriction,
    RestrictionType,
    Sequence,
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


def get_help(obj: AnnotationBase) -> Optional[str]:
    try:
        return obj.annotation.documentation.text  # type: ignore
    except AttributeError:
        return None


def get_type(obj: ElementBase) -> Optional[str]:
    type_var = None
    if isinstance(obj, Restriction):
        type_var = obj.base
    elif isinstance(obj, Attribute):
        try:
            type_var = obj.simple_type.restriction.base  # type: ignore
        except AttributeError:
            pass

    if type_var is None:
        type_var = getattr(obj, "type", None)

    if type_var:
        type_var = XSD_TYPES.get(type_var) or text.pascal_case(type_var)

    return type_var


def get_restrictions(obj: ElementBase) -> Dict[str, Anything]:
    restrictions = {}
    if isinstance(obj, Restriction):
        return {
            res.name: getattr(obj, res.name).value
            for res in fields(obj)
            if isinstance(getattr(obj, res.name), RestrictionType)
        }

    if (
        isinstance(obj, All)
        or isinstance(obj, Sequence)
        or isinstance(obj, Choice)
        or isinstance(obj, Group)
        or isinstance(obj, Element)
        or isinstance(obj, Any)
    ):
        restrictions.update(
            dict(min_occurs=obj.min_occurs, max_occurs=obj.max_occurs)
        )

    return restrictions


def get_extension_base(obj: Optional[ComplexType]) -> Optional[str]:
    try:
        return text.pascal_case(obj.complex_content.extension.base)  # type: ignore
    except AttributeError:
        return None


def append_documentation(obj: AnnotationBase, string: str):
    if obj.annotation is None:
        obj.annotation = Annotation.build()
    if obj.annotation.documentation is None:
        obj.annotation.documentation = Documentation.build()
    if obj.annotation.documentation.text is None:
        obj.annotation.documentation.text = ""

    obj.annotation.documentation.text = "{}\n{}".format(
        obj.annotation.documentation.text, string
    ).strip()
