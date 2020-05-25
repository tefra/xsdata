from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.common.models.nhinc.common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Ii,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.mcci_in000002_uv01 import (
    McciIn000002Uv01,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201304_uv02 import (
    PrpaIn201304Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201309_uv02 import (
    PrpaIn201309Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201310_uv02 import (
    PrpaIn201310Uv02,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201301_uv02 import (
    PrpaMt201301Uv02Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201307_uv02 import (
    PrpaMt201307Uv02QueryByParameter,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201310_uv02 import (
    PrpaMt201310Uv02Patient,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CreateFault201310RequestType:
    """
    :ivar sender_oid:
    :ivar receiver_oid:
    """
    sender_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="senderOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    receiver_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="receiverOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class Create201302RequestType:
    """
    :ivar prpa201310_patient:
    :ivar prpa201301_patient:
    :ivar remote_patient_id:
    :ivar remote_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    """
    prpa201310_patient: Optional[PrpaMt201310Uv02Patient] = field(
        default=None,
        metadata=dict(
            name="PRPA201310Patient",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    prpa201301_patient: Optional[PrpaMt201301Uv02Patient] = field(
        default=None,
        metadata=dict(
            name="PRPA201301Patient",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    remote_patient_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="remotePatientId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    remote_device_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="remoteDeviceId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sender_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="senderOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    receiver_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="receiverOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class Create201305RequestType:
    """
    :ivar prpa201301_patient:
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    """
    prpa201301_patient: Optional[PrpaMt201301Uv02Patient] = field(
        default=None,
        metadata=dict(
            name="PRPA201301Patient",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    local_device_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="localDeviceId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sender_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="senderOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    receiver_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="receiverOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class Create201310RequestType:
    """
    :ivar pseudo_patient_id:
    :ivar pseudo_assigning_authority_id:
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    :ivar prpa201307_query_by_parameter:
    """
    pseudo_patient_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pseudoPatientId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    pseudo_assigning_authority_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pseudoAssigningAuthorityId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    local_device_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="localDeviceId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sender_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="senderOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    receiver_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="receiverOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    prpa201307_query_by_parameter: Optional[PrpaMt201307Uv02QueryByParameter] = field(
        default=None,
        metadata=dict(
            name="PRPA201307QueryByParameter",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class CreateAckMsgRequestType:
    """
    :ivar local_device_id:
    :ivar orig_msg_id:
    :ivar msg_text:
    :ivar sender_oid:
    :ivar receiver_oid:
    """
    local_device_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="localDeviceId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    orig_msg_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="origMsgId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    msg_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="msgText",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    sender_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="senderOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    receiver_oid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="receiverOID",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class CreateFault201310Request(CreateFault201310RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerMcciIn000002Uv01RequestType:
    """
    :ivar mcci_in000002_uv01:
    :ivar assertion:
    """
    class Meta:
        name = "PIXConsumer_MCCI_IN000002UV01RequestType"

    mcci_in000002_uv01: Optional[McciIn000002Uv01] = field(
        default=None,
        metadata=dict(
            name="MCCI_IN000002UV01",
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


@dataclass
class PixconsumerPrpaIn201304UvrequestType:
    """
    :ivar prpa_in201304_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVRequestType"

    prpa_in201304_uv02: Optional[PrpaIn201304Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201304UV02",
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
class PixconsumerPrpaIn201304UvsecuredRequestType:
    """
    :ivar prpa_in201304_uv02:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVSecuredRequestType"

    prpa_in201304_uv02: Optional[PrpaIn201304Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201304UV02",
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
class PixconsumerPrpaIn201309UvrequestType:
    """
    :ivar prpa_in201309_uv02:
    :ivar assertion:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVRequestType"

    prpa_in201309_uv02: Optional[PrpaIn201309Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201309UV02",
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
class PixconsumerPrpaIn201309UvresponseType:
    """
    :ivar prpa_in201310_uv02:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVResponseType"

    prpa_in201310_uv02: Optional[PrpaIn201310Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201310UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class PixconsumerPrpaIn201309UvsecuredRequestType:
    """
    :ivar prpa_in201309_uv02:
    :ivar nhin_target_communities:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVSecuredRequestType"

    prpa_in201309_uv02: Optional[PrpaIn201309Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201309UV02",
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
class PixconsumerPrpaIn201310UvrequestType:
    """
    :ivar prpa_in201310_uv02:
    :ivar assertion:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVRequestType"

    prpa_in201310_uv02: Optional[PrpaIn201310Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201310UV02",
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


@dataclass
class PixconsumerPrpaIn201310UvsecuredRequestType:
    """
    :ivar prpa_in201310_uv02:
    """
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVSecuredRequestType"

    prpa_in201310_uv02: Optional[PrpaIn201310Uv02] = field(
        default=None,
        metadata=dict(
            name="PRPA_IN201310UV02",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class Create201302Request(Create201302RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class Create201305Request(Create201305RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class Create201310Request(Create201310RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class CreateAckMsgRequest(CreateAckMsgRequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerMcciIn000002Uv01Request(PixconsumerMcciIn000002Uv01RequestType):
    class Meta:
        name = "PIXConsumer_MCCI_IN000002UV01Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304Uvrequest(PixconsumerPrpaIn201304UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304UvsecuredRequest(PixconsumerPrpaIn201304UvsecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309Uvrequest(PixconsumerPrpaIn201309UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309Uvresponse(PixconsumerPrpaIn201309UvresponseType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVResponse"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309UvsecuredRequest(PixconsumerPrpaIn201309UvsecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201310Uvrequest(PixconsumerPrpaIn201310UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201310UvsecuredRequest(PixconsumerPrpaIn201310UvsecuredRequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVSecuredRequest"
        namespace = "urn:hl7-org:v3"
