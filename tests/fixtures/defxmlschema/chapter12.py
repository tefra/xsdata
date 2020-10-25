from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DescriptionType:
    """
    :ivar w3_org_1999_xhtml_element:
    """
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
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size_or_color_or_description:
    :ivar eff_date:
    :ivar other_attributes:
    """
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
    eff_date: str = field(
        default="1900-01-01",
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
    """
    :ivar shirt_or_hat_or_umbrella:
    """
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
