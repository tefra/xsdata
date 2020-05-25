from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201306_uv02 import (
    PrpaIn201306Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RespondingGatewayPrpaIn201306Uv02RequestType:
    """
    :ivar prpa_in201306_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02RequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201306UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02SecuredRequestType:
    """
    :ivar prpa_in201306_uv02:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02SecuredRequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201306UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    nhin_target_communities: Optional[NhinTargetCommunitiesType] = field(
        default=None,
        metadata=dict(
            name="NhinTargetCommunities",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02Request(RespondingGatewayPrpaIn201306Uv02RequestType):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class RespondingGatewayPrpaIn201306Uv02SecuredRequest(RespondingGatewayPrpaIn201306Uv02SecuredRequestType):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02SecuredRequest"
        namespace = "urn:hl7-org:v3"
