from dataclasses import dataclass, field


@dataclass
class ProductType:
    """
    :ivar eff_date:
    """
    eff_date: str = field(
        default="2000-12-31",
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
