from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201305_uv02 import (
    PrpaIn201305Uv02McciMt000100Uv01Message,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in201307_uv02 import (
    PrpaIn201307Uv02McciMt000100Uv01Message,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_in900300_uv02 import (
    PrpaIn900300Uv02McciMt000100Uv01Message,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201303_uv02 import (
    PrpaMt201303Uv02Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt201310_uv02 import (
    PrpaMt201310Uv02Patient,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.prpa_mt900350_uv02 import (
    PrpaMt900350Uv02EncounterEvent,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.qupc_in043100_uv01 import (
    QupcIn043100Uv01McciMt000100Uv01Message,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.qupc_in043200_uv01 import (
    QupcIn043200Uv01MfmiMt700712Uv01Subject1,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01RequestType:
    """
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    :ivar query:
    """
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01RequestType"

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
    query: Optional[QupcIn043100Uv01McciMt000100Uv01Message] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class CareRecordQupcIn043200Uv01ResponseType:
    """
    :ivar care_record:
    """
    class Meta:
        name = "CareRecord_QUPC_IN043200UV01ResponseType"

    care_record: Optional[QupcIn043200Uv01MfmiMt700712Uv01Subject1] = field(
        default=None,
        metadata=dict(
            name="careRecord",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class FindEncountersPrpaIn900300Uv02RequestType:
    """
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    :ivar query:
    """
    class Meta:
        name = "FindEncounters_PRPA_IN900300UV02RequestType"

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
    query: Optional[PrpaIn900300Uv02McciMt000100Uv01Message] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class FindEncountersPrpaMt900350Uv02ResponseType:
    """
    :ivar event:
    """
    class Meta:
        name = "FindEncounters_PRPA_MT900350UV02ResponseType"

    event: List[PrpaMt900350Uv02EncounterEvent] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class FindPatientsPrpaIn201305Uv02RequestType:
    """
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    :ivar query:
    """
    class Meta:
        name = "FindPatients_PRPA_IN201305UV02RequestType"

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
    query: Optional[PrpaIn201305Uv02McciMt000100Uv01Message] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class FindPatientsPrpaMt201310Uv02ResponseType:
    """
    :ivar subject:
    """
    class Meta:
        name = "FindPatients_PRPA_MT201310UV02ResponseType"

    subject: List[PrpaMt201310Uv02Patient] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class PatientDemographicsPrpaIn201307Uv02RequestType:
    """
    :ivar local_device_id:
    :ivar sender_oid:
    :ivar receiver_oid:
    :ivar query:
    """
    class Meta:
        name = "PatientDemographics_PRPA_IN201307UV02RequestType"

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
    query: Optional[PrpaIn201307Uv02McciMt000100Uv01Message] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class PatientDemographicsPrpaMt201303Uv02ResponseType:
    """
    :ivar subject:
    """
    class Meta:
        name = "PatientDemographics_PRPA_MT201303UV02ResponseType"

    subject: Optional[PrpaMt201303Uv02Patient] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )


@dataclass
class CareRecordQupcIn043100Uv01AdmissionsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01AdmissionsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01AllergiesRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01AllergiesRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01AppointmentsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01AppointmentsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01FamilyHistoryRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01FamilyHistoryRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01ImmunizationsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01ImmunizationsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01MedicationsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01MedicationsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01OrdersRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01OrdersRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01ProblemsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01ProblemsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01ProceduresRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01ProceduresRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01Request(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01SocialHistoryRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01SocialHistoryRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01TestResultsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01TestResultsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043100Uv01VitalsRequest(CareRecordQupcIn043100Uv01RequestType):
    class Meta:
        name = "CareRecord_QUPC_IN043100UV01VitalsRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class CareRecordQupcIn043200Uv01Response(CareRecordQupcIn043200Uv01ResponseType):
    class Meta:
        name = "CareRecord_QUPC_IN043200UV01Response"
        namespace = "urn:hl7-org:v3"


@dataclass
class FindEncountersPrpaIn900300Uv02Request(FindEncountersPrpaIn900300Uv02RequestType):
    class Meta:
        name = "FindEncounters_PRPA_IN900300UV02Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class FindEncountersPrpaMt900350Uv02Response(FindEncountersPrpaMt900350Uv02ResponseType):
    class Meta:
        name = "FindEncounters_PRPA_MT900350UV02Response"
        namespace = "urn:hl7-org:v3"


@dataclass
class FindPatientsPrpaIn201305Uv02Request(FindPatientsPrpaIn201305Uv02RequestType):
    class Meta:
        name = "FindPatients_PRPA_IN201305UV02Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class FindPatientsPrpaMt201310Uv02Response(FindPatientsPrpaMt201310Uv02ResponseType):
    class Meta:
        name = "FindPatients_PRPA_MT201310UV02Response"
        namespace = "urn:hl7-org:v3"


@dataclass
class PatientDemographicsPrpaIn201307Uv02Request(PatientDemographicsPrpaIn201307Uv02RequestType):
    class Meta:
        name = "PatientDemographics_PRPA_IN201307UV02Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class PatientDemographicsPrpaMt201303Uv02Response(PatientDemographicsPrpaMt201303Uv02ResponseType):
    class Meta:
        name = "PatientDemographics_PRPA_MT201303UV02Response"
        namespace = "urn:hl7-org:v3"
