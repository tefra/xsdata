from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    ActClass,
    ActMood,
    NullFlavor,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Cd,
    Cs,
    Ii,
    IvlTsExplicit,
    Mo,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes import (
    RtoMoPq,
    RtoPqPq,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt440001UvValuedItem:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar effective_time:
    :ivar unit_quantity:
    :ivar unit_price_amt:
    :ivar net_amt:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT440001UV.ValuedItem"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata=dict(
            name="realmCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="typeId",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            name="templateId",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    code: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            name="effectiveTime",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    unit_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata=dict(
            name="unitQuantity",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    unit_price_amt: Optional[RtoMoPq] = field(
        default=None,
        metadata=dict(
            name="unitPriceAmt",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    net_amt: Optional[Mo] = field(
        default=None,
        metadata=dict(
            name="netAmt",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.INVE,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True
        )
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF_VALUE,
        metadata=dict(
            name="moodCode",
            type="Attribute",
            required=True
        )
    )
