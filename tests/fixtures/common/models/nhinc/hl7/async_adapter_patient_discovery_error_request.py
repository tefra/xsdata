from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201305_uv02 import (
    PrpaIn201305Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201306_uv02 import (
    PrpaIn201306Uv02,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AsyncAdapterPatientDiscoveryErrorRequestType:
    """
    :ivar prpa_in201305_uv02:
    :ivar prpa_in201306_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    :ivar error_msg:
    """
    prpa_in201305_uv02: Optional[PrpaIn201305Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201305UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
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
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    error_msg: Optional[str] = field(
        default=None,
        metadata=dict(
            name="errorMsg",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class AsyncAdapterPatientDiscoveryErrorSecuredRequestType:
    """
    :ivar prpa_in201305_uv02:
    :ivar prpa_in201306_uv02:
    :ivar nhin_target_communities:
    :ivar error_msg:
    """
    prpa_in201305_uv02: Optional[PrpaIn201305Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201305UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
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
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    error_msg: Optional[str] = field(
        default=None,
        metadata=dict(
            name="errorMsg",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class AsyncAdapterPatientDiscoveryErrorRequest(AsyncAdapterPatientDiscoveryErrorRequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class AsyncAdapterPatientDiscoveryErrorSecuredRequest(AsyncAdapterPatientDiscoveryErrorSecuredRequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"
