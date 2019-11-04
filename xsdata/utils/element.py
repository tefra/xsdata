from dataclasses import fields
from typing import Any as Anything
from typing import Dict, Optional

from xsdata.models.elements import (
    All,
    Annotation,
    AnnotationBase,
    Any,
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
