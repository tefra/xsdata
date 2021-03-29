from dataclasses import dataclass, field
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDate


@dataclass
class ColorType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DescriptionType:
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )


@dataclass
class SizeType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProductType:
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    size_or_color_or_description: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "size",
                    "type": SizeType,
                    "namespace": "",
                },
                {
                    "name": "color",
                    "type": ColorType,
                    "namespace": "",
                },
                {
                    "name": "description",
                    "type": DescriptionType,
                    "namespace": "",
                },
            ),
        }
    )
    eff_date: XmlDate = field(
        default=XmlDate(1900, 1, 1),
        metadata={
            "name": "effDate",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ItemsType:
    shirt_or_hat_or_umbrella: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "shirt",
                    "type": ProductType,
                    "namespace": "",
                },
                {
                    "name": "hat",
                    "type": ProductType,
                    "namespace": "",
                },
                {
                    "name": "umbrella",
                    "type": ProductType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
