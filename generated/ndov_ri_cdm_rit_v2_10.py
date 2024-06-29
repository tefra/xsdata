from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

from generated.ndov_ri_cdm_common_v2_5 import (
    AankomstOfVertrekTijdType,
    Indicatie,
    InfoStatus,
    MeertaligeUitingenType,
    NietInstappenType,
    RipadministratieType,
    SpoorPlannedActueelType,
    StationnementTypeType,
    StationPlannedActueelType,
    StationType,
    TaalCodesType,
    TreinSoortType,
    WijzigingType,
)
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

__NAMESPACE__ = "urn:ndov:cdm:trein:reisinformatie:data:2"


@dataclass
class GewijzigdMaterieelType:
    """
    Dit element geeft het gewijzigde materieel aan.
    """

    materieel_deel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelID",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    materieel_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 17,
        },
    )


@dataclass
class MaterieelDeelVolgendeLogischeRitDeelType:
    """Het volgend TreinNummer van een Trein op een bepaald RitStation voor een
    trein op een bepaalde verkeers-/patroondag.

    Deze kan bepaald worden op basis van de materieelrelatie.
    """

    logische_rit_deel_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "LogischeRitDeelNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    trein_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TreinDatum",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )


class MaterieelWijzigingTypeType(Enum):
    """Dit element geeft aan wat voor soort materieelwijziging er plaatsvind.

    (Combineer, splits, bijplaatsen, aftrappen)
    """

    COMBINEREN = "Combineren"
    SPLITSEN = "Splitsen"
    BIJPLAATSEN = "Bijplaatsen"
    AFTRAPPEN = "Aftrappen"


@dataclass
class GeefActueleRitTijdenRequestMessageType:
    """
    De vraag voor het pull request actuele rittijden.

    :ivar trein_nummer: Startend treinnummer van de actuele rit.
    :ivar trein_datum: Als de TreinDatum niet is ingevuld wordt het
        RitInfo bericht met de huidige datum (lokaal) geretourneerd.
    :ivar taal_codes: Als er het TaalCodes element ontbreekt dan wordt
        de Nederlandse redactie gebruikt.
    :ivar aanvrager: Geeft aan wie de aanvrager is (voor statistieken).
    :ivar time_stamp: Geeft de datum en tijd weer  wanneer deze vraag is
        gesteld.
    """

    trein_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "TreinNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    trein_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TreinDatum",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    taal_codes: Optional[TaalCodesType] = field(
        default=None,
        metadata={
            "name": "TaalCodes",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    aanvrager: Optional[str] = field(
        default=None,
        metadata={
            "name": "Aanvrager",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MaterieelDeelRitinfoType:
    """
    Beschrijving van een fysiek stuk materieel dat deelneemt aan de beschreven rit.

    :ivar materieel_deel_id:
    :ivar materieel_deel_soort:
    :ivar materieel_deel_aanduiding:
    :ivar materieel_deel_lengte:
    :ivar materieel_deel_vertrek_positie:
    :ivar materieel_deel_volgorde_vertrek:
    :ivar materieel_nummer:
    :ivar materieel_deel_toegankelijk:
    :ivar presentatie_materieel_deel_toegankelijk:
    :ivar materieel_deel_eind_bestemming:
    :ivar presentatie_materieel_deel_eind_bestemming:
    :ivar achter_blijven_materieel_deel:
    :ivar materieel_deel_volgende_logische_rit_deel: Het volgend
        TreinNummer waar het genoemde materieeldeel onder verder rijdt.
        Wordt alleen vermeld op het RitStation waar sprake is van een
        doorgaandeverbinding voor de trein.
    """

    class Meta:
        name = "MaterieelDeelRITInfoType"

    materieel_deel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelID",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    materieel_deel_soort: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelSoort",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 9,
        },
    )
    materieel_deel_aanduiding: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelAanduiding",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    materieel_deel_lengte: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelLengte",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    materieel_deel_vertrek_positie: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelVertrekPositie",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    materieel_deel_volgorde_vertrek: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelVolgordeVertrek",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    materieel_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterieelNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 17,
        },
    )
    materieel_deel_toegankelijk: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelToegankelijk",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_materieel_deel_toegankelijk: Optional[
        MeertaligeUitingenType
    ] = field(
        default=None,
        metadata={
            "name": "PresentatieMaterieelDeelToegankelijk",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    materieel_deel_eind_bestemming: List[StationPlannedActueelType] = field(
        default_factory=list,
        metadata={
            "name": "MaterieelDeelEindBestemming",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    presentatie_materieel_deel_eind_bestemming: Optional[
        MeertaligeUitingenType
    ] = field(
        default=None,
        metadata={
            "name": "PresentatieMaterieelDeelEindBestemming",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    achter_blijven_materieel_deel: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "AchterBlijvenMaterieelDeel",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    materieel_deel_volgende_logische_rit_deel: Optional[
        MaterieelDeelVolgendeLogischeRitDeelType
    ] = field(
        default=None,
        metadata={
            "name": "MaterieelDeelVolgendeLogischeRitDeel",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )


@dataclass
class MaterieelWijzigingType:
    """
    Dit element geeft aan welke materieel wijzigingen er op dit station
    plaatsvinden.
    """

    materieel_wijziging_type: Optional[MaterieelWijzigingTypeType] = field(
        default=None,
        metadata={
            "name": "MaterieelWijzigingType",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    gewijzigd_materieel: Optional[GewijzigdMaterieelType] = field(
        default=None,
        metadata={
            "name": "GewijzigdMaterieel",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )


@dataclass
class StoptType:
    """Indicatie of de trein wel (=”J”) of niet (=”N”) op het desbetreffende
    ritstation stopt.

    Het element komt zowel gepland als actueel voor. Het attribuut
    InfoStatus bevat hiertoe de waarde 'Actueel' en 'Gepland'
    """

    value: Optional[Indicatie] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    info_status: Optional[InfoStatus] = field(
        default=None,
        metadata={
            "name": "InfoStatus",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class VertragingStationType:
    """
    Het station waar gewijzigde aankomst en vertrektijden naar doorberekend zijn.
    """

    station_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StationCode",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    aankomst_tijd: List[AankomstOfVertrekTijdType] = field(
        default_factory=list,
        metadata={
            "name": "AankomstTijd",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 2,
        },
    )
    exacte_aankomst_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExacteAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_aankomst_vertraging: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    gedempte_aankomst_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "GedempteAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    vertrek_tijd: List[AankomstOfVertrekTijdType] = field(
        default_factory=list,
        metadata={
            "name": "VertrekTijd",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 2,
        },
    )
    exacte_vertrek_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExacteVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_vertrek_vertraging: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    gedempte_vertrek_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "GedempteVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )


@dataclass
class GeefActueleRitTijdenFaultMessageType:
    """
    Foutbericht van een pull request actuele rittijden.

    :ivar foutnummer:
    :ivar omschrijving:
    :ivar geef_actuele_rit_tijden_request_message:
    :ivar time_stamp: Geeft de datum en tijd weer  wanneer het antwoord
        is samengesteld.
    """

    foutnummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Foutnummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    omschrijving: Optional[str] = field(
        default=None,
        metadata={
            "name": "Omschrijving",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    geef_actuele_rit_tijden_request_message: Optional[
        GeefActueleRitTijdenRequestMessageType
    ] = field(
        default=None,
        metadata={
            "name": "GeefActueleRitTijdenRequestMessage",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RitStationsType:
    """
    De verzameling van stations waar één of meerdere logische ritten langs gaan
    volgens de planning inclusief eventuele extra ritstations.

    :ivar station:
    :ivar station_toegankelijk:
    :ivar presentatie_station_toegankelijk:
    :ivar station_reis_assistentie:
    :ivar presentatie_station_reis_assistentie:
    :ivar trein_eind_bestemming:
    :ivar presentatie_trein_eind_bestemming:
    :ivar stopt: Indicatie of de trein wel (=”J”) of niet (=”N”) op het
        desbetreffende ritstation stopt. Het element komt niet voor of
        het komt zowel gepland als actueel voor. Het attribuut
        InfoStatus bevat hiertoe de waarde 'Actueel' en 'Gepland'
    :ivar aankomst_tijd:
    :ivar exacte_aankomst_vertraging:
    :ivar presentatie_aankomst_vertraging:
    :ivar gedempte_aankomst_vertraging:
    :ivar trein_aankomst_spoor:
    :ivar presentatie_trein_aankomst_spoor:
    :ivar vertrek_tijd:
    :ivar exacte_vertrek_vertraging:
    :ivar presentatie_vertrek_vertraging:
    :ivar gedempte_vertrek_vertraging:
    :ivar trein_vertrek_spoor:
    :ivar presentatie_trein_vertrek_spoor:
    :ivar stationnement_type:
    :ivar materieel_deel:
    :ivar niet_instappen:
    :ivar presentatie_niet_instappen:
    :ivar trein_rangeert_volledig_af:
    :ivar materieel_wijziging:
    :ivar wijziging:
    :ivar other_element:
    """

    station: Optional[StationType] = field(
        default=None,
        metadata={
            "name": "Station",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    station_toegankelijk: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "StationToegankelijk",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_station_toegankelijk: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieStationToegankelijk",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    station_reis_assistentie: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "StationReisAssistentie",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_station_reis_assistentie: Optional[MeertaligeUitingenType] = (
        field(
            default=None,
            metadata={
                "name": "PresentatieStationReisAssistentie",
                "type": "Element",
                "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            },
        )
    )
    trein_eind_bestemming: List[StationPlannedActueelType] = field(
        default_factory=list,
        metadata={
            "name": "TreinEindBestemming",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_trein_eind_bestemming: Optional[MeertaligeUitingenType] = (
        field(
            default=None,
            metadata={
                "name": "PresentatieTreinEindBestemming",
                "type": "Element",
                "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            },
        )
    )
    stopt: List[StoptType] = field(
        default_factory=list,
        metadata={
            "name": "Stopt",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 2,
        },
    )
    aankomst_tijd: List[AankomstOfVertrekTijdType] = field(
        default_factory=list,
        metadata={
            "name": "AankomstTijd",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 2,
        },
    )
    exacte_aankomst_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExacteAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_aankomst_vertraging: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    gedempte_aankomst_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "GedempteAankomstVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    trein_aankomst_spoor: List[SpoorPlannedActueelType] = field(
        default_factory=list,
        metadata={
            "name": "TreinAankomstSpoor",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 4,
        },
    )
    presentatie_trein_aankomst_spoor: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieTreinAankomstSpoor",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    vertrek_tijd: List[AankomstOfVertrekTijdType] = field(
        default_factory=list,
        metadata={
            "name": "VertrekTijd",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 2,
        },
    )
    exacte_vertrek_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExacteVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_vertrek_vertraging: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    gedempte_vertrek_vertraging: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "GedempteVertrekVertraging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    trein_vertrek_spoor: List[SpoorPlannedActueelType] = field(
        default_factory=list,
        metadata={
            "name": "TreinVertrekSpoor",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 4,
        },
    )
    presentatie_trein_vertrek_spoor: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieTreinVertrekSpoor",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    stationnement_type: Optional[StationnementTypeType] = field(
        default=None,
        metadata={
            "name": "StationnementType",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    materieel_deel: List[MaterieelDeelRitinfoType] = field(
        default_factory=list,
        metadata={
            "name": "MaterieelDeel",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    niet_instappen: Optional[NietInstappenType] = field(
        default=None,
        metadata={
            "name": "NietInstappen",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_niet_instappen: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieNietInstappen",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    trein_rangeert_volledig_af: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "TreinRangeertVolledigAf",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    materieel_wijziging: List[MaterieelWijzigingType] = field(
        default_factory=list,
        metadata={
            "name": "MaterieelWijziging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    wijziging: List[WijzigingType] = field(
        default_factory=list,
        metadata={
            "name": "Wijziging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )


@dataclass
class LogischeRitDeelType:
    """
    Een deel van een logische rit en bestaat uit een (deel van) logistieke rit.
    """

    logische_rit_deel_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "LogischeRitDeelNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    logische_rit_deel_station: List[RitStationsType] = field(
        default_factory=list,
        metadata={
            "name": "LogischeRitDeelStation",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )
    wijziging: List[WijzigingType] = field(
        default_factory=list,
        metadata={
            "name": "Wijziging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )


@dataclass
class LogischeRitType:
    """Een logische rit begint bij het begin van een logistieke rit.

    Een logische rit is de langste rit die met één gepland materieeldeel
    kan worden uitgevoerd. Een logische rit kan bestaan uit meerdere
    (delen van) logistieke ritten als er sprake is van een of meerdere
    doorgaande verbindingen.
    """

    logische_rit_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogischeRitNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    logische_rit_deel: List[LogischeRitDeelType] = field(
        default_factory=list,
        metadata={
            "name": "LogischeRitDeel",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )
    wijziging: List[WijzigingType] = field(
        default_factory=list,
        metadata={
            "name": "Wijziging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )


@dataclass
class TreinRitType:
    """
    Het element TreinRit bevat informatie over de trein en alle logische ritten die
    met het materieel van deze trein afgelegd worden.
    """

    trein_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "TreinNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    trein_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TreinDatum",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    trein_naam: Optional[str] = field(
        default=None,
        metadata={
            "name": "TreinNaam",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 30,
        },
    )
    trein_soort: Optional[TreinSoortType] = field(
        default=None,
        metadata={
            "name": "TreinSoort",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    lijn_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "LijnNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 9,
        },
    )
    vervoerder: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vervoerder",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 10,
        },
    )
    reserveren: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "Reserveren",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    presentatie_reserveren: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieReserveren",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    toeslag: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "Toeslag",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    presentatie_toeslag: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieToeslag",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    speciaal_kaartje: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "SpeciaalKaartje",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    presentatie_speciaal_kaartje: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieSpeciaalKaartje",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    reisplanner: Optional[Indicatie] = field(
        default=None,
        metadata={
            "name": "Reisplanner",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    logische_rit: List[LogischeRitType] = field(
        default_factory=list,
        metadata={
            "name": "LogischeRit",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )


@dataclass
class ActueleRitTijdenType:
    """
    Het element ActueleRitTijden bevat de geplande en actuele gegevens van één
    gehele rit op één bepaalde geldigheidsdatum.
    """

    reis_informatie_product_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReisInformatieProductID",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    rit_info: Optional[TreinRitType] = field(
        default=None,
        metadata={
            "name": "RitInfo",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReisInformatieProductRitInfoType:
    """
    Het element RITInfo bevat de geplande en actuele gegevens van één gehele rit op
    één bepaalde geldigheidsdatum.
    """

    ripadministratie: Optional[RipadministratieType] = field(
        default=None,
        metadata={
            "name": "RIPAdministratie",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    rit_info: Optional[TreinRitType] = field(
        default=None,
        metadata={
            "name": "RitInfo",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    versie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Versie",
            "type": "Attribute",
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
            "required": True,
        },
    )
    applicatie_versie: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicatieVersie",
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass
class GeefActueleRitTijdenResponseMessageType:
    """
    Response van het pull request van actuele rittijden.

    :ivar bericht_status: Status van het antwoord. 10=succesvolle
        afhandeling, 20=geen actuele reisinformatie beschikbaar. 30=geen
        reisinformatie beschikbaar.
    :ivar geef_actuele_rit_tijden_request_message:
    :ivar actuele_rit_tijden:
    :ivar time_stamp: Geeft de datum en tijd weer  wanneer het antwoord
        is samengesteld.
    """

    bericht_status: Optional[int] = field(
        default=None,
        metadata={
            "name": "BerichtStatus",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    geef_actuele_rit_tijden_request_message: Optional[
        GeefActueleRitTijdenRequestMessageType
    ] = field(
        default=None,
        metadata={
            "name": "GeefActueleRitTijdenRequestMessage",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    actuele_rit_tijden: Optional[ActueleRitTijdenType] = field(
        default=None,
        metadata={
            "name": "ActueleRitTijden",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReisInformatieProductRitInfo(ReisInformatieProductRitInfoType):
    """Een reisinformatieProduct van CRIS met als inhoud een RitInfo.

    Deze wordt door CRIS aangemaakt en uitgestuurd.
    """

    class Meta:
        namespace = "urn:ndov:cdm:trein:reisinformatie:data:2"
