from dataclasses import dataclass, field


@dataclass
class ProductType:
    """
    :ivar eff_date:
    """
    eff_date: str = field(
        default="1900-01-01",
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
