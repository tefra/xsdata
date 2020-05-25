from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
    TelExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt030000_uv04 import (
    CoctMt030000Uv04NonPersonLivingSubject,
    CoctMt030000Uv04Person,
)
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.coct_mt150000_uv02 import (
    CoctMt150000Uv02Organization,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    XAccommodationRequestorRole,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt050000Uv01Patient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar addr:
    :ivar telecom:
    :ivar status_code:
    :ivar effective_time:
    :ivar confidentiality_code:
    :ivar very_important_person_code:
    :ivar patient_person:
    :ivar patient_non_person_living_subject:
    :ivar provider_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "COCT_MT050000UV01.Patient"

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
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    addr: List[AdExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    telecom: List[TelExplicit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata=dict(
            name="statusCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
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
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="confidentialityCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    very_important_person_code: Optional[Ce] = field(
        default=None,
        metadata=dict(
            name="veryImportantPersonCode",
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    patient_person: Optional[CoctMt030000Uv04Person] = field(
        default=None,
        metadata=dict(
            name="patientPerson",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient_non_person_living_subject: Optional[CoctMt030000Uv04NonPersonLivingSubject] = field(
        default=None,
        metadata=dict(
            name="patientNonPersonLivingSubject",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    provider_organization: Optional[CoctMt150000Uv02Organization] = field(
        default=None,
        metadata=dict(
            name="providerOrganization",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "CoctMt050000Uv01Patient.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PAT,
        metadata=dict(
            name="classCode",
            type="Attribute",
            required=True,
            pattern=r"[^\s]+"
        )
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"
