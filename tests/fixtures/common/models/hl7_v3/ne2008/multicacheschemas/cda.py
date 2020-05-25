from dataclasses import dataclass
from tests.fixtures.common.models.hl7_v3.ne2008.multicacheschemas.pocd_mt000040 import (
    PocdMt000040ClinicalDocument,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ClinicalDocument(PocdMt000040ClinicalDocument):
    class Meta:
        namespace = "urn:hl7-org:v3"
