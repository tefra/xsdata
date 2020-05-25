from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.datatypes_base import (
    Bl,
    Cd,
    Ce,
    Cs,
    Ii,
    IntType,
    IvlTsExplicit,
    PnExplicit,
    TsExplicit,
)
from tests.fixtures.common.models.hl7_v3.ne2008.coreschemas.voc import (
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class QupcMt040300Uv01CareProvisionCode:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.CareProvisionCode"

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
    value: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01CareProvisionReason:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.CareProvisionReason"

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
    value: Optional[Cd] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01CareRecordTimePeriod:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.CareRecordTimePeriod"

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
    value: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01ClinicalStatementTimePeriod:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.ClinicalStatementTimePeriod"

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
    value: Optional[IvlTsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01IncludeCarePlanAttachment:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.IncludeCarePlanAttachment"

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
    value: Optional[Bl] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01MaximumHistoryStatements:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.MaximumHistoryStatements"

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
    value: Optional[IntType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01PatientAdministrativeGender:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.PatientAdministrativeGender"

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
    value: Optional[Ce] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01PatientBirthTime:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.PatientBirthTime"

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
    value: Optional[TsExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01PatientId:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.PatientId"

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
    value: Optional[Ii] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01PatientName:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar value:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.PatientName"

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
    value: Optional[PnExplicit] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata=dict(
            name="nullFlavor",
            type="Attribute"
        )
    )


@dataclass
class QupcMt040300Uv01ParameterList:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar care_provision_code:
    :ivar care_provision_reason:
    :ivar care_record_time_period:
    :ivar clinical_statement_time_period:
    :ivar include_care_plan_attachment:
    :ivar maximum_history_statements:
    :ivar patient_administrative_gender:
    :ivar patient_birth_time:
    :ivar patient_id:
    :ivar patient_name:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUPC_MT040300UV01.ParameterList"

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
    care_provision_code: Optional[QupcMt040300Uv01CareProvisionCode] = field(
        default=None,
        metadata=dict(
            name="careProvisionCode",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    care_provision_reason: List[QupcMt040300Uv01CareProvisionReason] = field(
        default_factory=list,
        metadata=dict(
            name="careProvisionReason",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    care_record_time_period: Optional[QupcMt040300Uv01CareRecordTimePeriod] = field(
        default=None,
        metadata=dict(
            name="careRecordTimePeriod",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    clinical_statement_time_period: Optional[QupcMt040300Uv01ClinicalStatementTimePeriod] = field(
        default=None,
        metadata=dict(
            name="clinicalStatementTimePeriod",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    include_care_plan_attachment: Optional[QupcMt040300Uv01IncludeCarePlanAttachment] = field(
        default=None,
        metadata=dict(
            name="includeCarePlanAttachment",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    maximum_history_statements: Optional[QupcMt040300Uv01MaximumHistoryStatements] = field(
        default=None,
        metadata=dict(
            name="maximumHistoryStatements",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient_administrative_gender: Optional[QupcMt040300Uv01PatientAdministrativeGender] = field(
        default=None,
        metadata=dict(
            name="patientAdministrativeGender",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient_birth_time: Optional[QupcMt040300Uv01PatientBirthTime] = field(
        default=None,
        metadata=dict(
            name="patientBirthTime",
            type="Element",
            namespace="urn:hl7-org:v3",
            nillable=True
        )
    )
    patient_id: Optional[QupcMt040300Uv01PatientId] = field(
        default=None,
        metadata=dict(
            name="patientId",
            type="Element",
            namespace="urn:hl7-org:v3",
            required=True
        )
    )
    patient_name: Optional[QupcMt040300Uv01PatientName] = field(
        default=None,
        metadata=dict(
            name="patientName",
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
