from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:ndov:cdm:trein:reisinformatie:data:2"


class Iso6391LanguageCodeContentType(Enum):
    """
    ISO 6391 taalcodes.

    :cvar NL: Dutch; Flemish
    :cvar EN: English
    """

    NL = "nl"
    EN = "en"


class NietInstappenType(Enum):
    """Als er bij een treinstop op een station alleen uitgestapt mag worden, dan
    bevat dit element de waarde 'J'.

    Als er alleen ingestapt of in- en uitgestapt mag worden, dan bevat
    dit element de waarde 'N'. Het element in het bericht is niet
    aanwezig wanneer de trein niet stopt.
    """

    J = "J"
    N = "N"


@dataclass
class RipadministratieType:
    """
    De gegevens benodigd voor de identificatie van het bericht met een
    reisinformatieproduct.
    """

    class Meta:
        name = "RIPAdministratieType"

    reis_informatie_product_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReisInformatieProductID",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    abonnement_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AbonnementId",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    reis_informatie_tijdstip: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReisInformatieTijdstip",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    geldig_tot: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "GeldigTot",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
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


class ReisTipCodeType(Enum):
    """
    Code van de reistip.
    """

    STNS = "STNS"
    STO = "STO"
    STVA = "STVA"
    STNVA = "STNVA"
    STT = "STT"
    STNT = "STNT"
    STAL = "STAL"
    STN = "STN"


@dataclass
class SpoorType:
    """Het gedeelte van een perron dat aan de rails ligt, waar een trein stopt en
    reizigers kunnen in- en uitstappen.

    Het spoor datatype bevat een spoornummer en een optioneel spoorfase
    element.
    """

    spoor_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpoorNummer",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    spoor_fase: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpoorFase",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 1,
            "pattern": r"[a-d]",
        },
    )


class StationnementTypeType(Enum):
    """Dit element geeft het stationnementtype aan.

    U = alleen uitstappen, I = alleen instappen, D = doorkomst, " " =
    In- en uitstappen..
    """

    U = "U"
    I = "I"
    D = "D"
    X = "X"


@dataclass
class TreinSoortType:
    """Geeft de commerciële benaming van de soort trein aan.

    De maxLength van InstapTipTreinSoort kan niet door de XSD worden
    afgedwongen, omdat een beperking op een element dat tevens een
    attribuut heeft niet toegestaan is bij de constructie van een XSD.
    De stamtabel TreinSoort bevat de toegestane waarden.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )


class TypeType(Enum):
    """Het element Type geeft een type-aanduiding van een station.

    0 = stoptreinstation, 1 = knooppunt stoptreinstation, 2 =
    Sneltreinstation, 3 = knooppunt sneltreinstation, 4 =
    Intercitystation, 5 = knooppunt intercitystation, 6 = Megastation, 7
    = facultatief station.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"


@dataclass
class UitingType:
    """
    Uiting met prioriteit, referentie en referentiewaarde.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    prioriteit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prioriteit",
            "type": "Attribute",
        },
    )
    referentie_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferentieType",
            "type": "Attribute",
        },
    )
    referentie_waarde: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferentieWaarde",
            "type": "Attribute",
        },
    )


class Indicatie(Enum):
    """Een ja/nee indicator.

    Kan de waarde "J" (ja) en "N" (nee) aannemen.
    """

    N = "N"
    J = "J"


class InfoStatus(Enum):
    """Geeft de actualiteitsstatus aan van informatie.

    Voorbeeld: "Actueel"
    """

    GEPLAND = "Gepland"
    ACTUEEL = "Actueel"


@dataclass
class AankomstOfVertrekTijdType:
    """Het element AankomstTijd geeft een tijdstip weer, waarop een trein van een
    station aankomst.

    Het attribuut InfoStatus geeft aan of het de geplande of de actuele
    aankomsttijd is.
    """

    value: Optional[XmlDateTime] = field(
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
class SpoorPlannedActueelType(SpoorType):
    """
    Spoor waarop een MaterieelDeel vertrekt.
    """

    info_status: Optional[InfoStatus] = field(
        default=None,
        metadata={
            "name": "InfoStatus",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StationType:
    """Gedeelte van de spoorweg, bestemd (en ingericht) om treinen te doen stoppen,
    beginnen, eindigen, inhalen of kruisen en voorzien van ten minste één wissel en
    tevens bestemd (en ingericht) om reizigers te laten in- of uitstappen en/of
    goederen aan te nemen en /of af te leveren.

    Het station datatype bevat elementen met informatie over een
    station.
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
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    korte_naam: Optional[str] = field(
        default=None,
        metadata={
            "name": "KorteNaam",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    middel_naam: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddelNaam",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    lange_naam: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangeNaam",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    uiccode: Optional[str] = field(
        default=None,
        metadata={
            "name": "UICCode",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 7,
        },
    )


@dataclass
class TaalCodesType:
    """
    Taalcodes die opgevraagd kunnen worden.
    """

    taal_code: List[Iso6391LanguageCodeContentType] = field(
        default_factory=list,
        metadata={
            "name": "TaalCode",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )


@dataclass
class UitingenType:
    """
    Taal specifieke uiting.
    """

    uiting: List[UitingType] = field(
        default_factory=list,
        metadata={
            "name": "Uiting",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )
    taal: Optional[Iso6391LanguageCodeContentType] = field(
        default=None,
        metadata={
            "name": "Taal",
            "type": "Attribute",
        },
    )


@dataclass
class MeertaligeUitingenType:
    """
    De meertalige uitingen van een presentatieelement.
    """

    uitingen: List[UitingenType] = field(
        default_factory=list,
        metadata={
            "name": "Uitingen",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_occurs": 1,
        },
    )


@dataclass
class StationPlannedActueelType(StationType):
    """Geeft een beschrijving van het station.

    Middels het InfoStatus attribuut wordt de actualiteitsstatus
    weergegeven (bijv. "Actueel").
    """

    info_status: Optional[InfoStatus] = field(
        default=None,
        metadata={
            "name": "InfoStatus",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReisTipType:
    """Het element ReisTip bevat reistipinformatie.

    Geldt bij afwijkend stopgedrag ten opzichte van de de treinformule.
    Voorbeeld: "De stoptrein richting Amsterdam stopt niet in Bussum-
    Zuid".
    """

    reis_tip_station: List[StationType] = field(
        default_factory=list,
        metadata={
            "name": "ReisTipStation",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "max_occurs": 3,
        },
    )
    reis_tip_code: Optional[ReisTipCodeType] = field(
        default=None,
        metadata={
            "name": "ReisTipCode",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
        },
    )
    presentatie_reis_tip: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieReisTip",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )


@dataclass
class WijzigingType:
    """
    Dit element bevat informatie over een wijziging van een trein ten opzichte van
    de dienstregeling richting eindbestemming van de rit.
    """

    wijziging_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "WijzigingType",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "required": True,
            "length": 2,
            "pattern": r"[0-9][0-9]",
        },
    )
    wijziging_oorzaak_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "WijzigingOorzaakCode",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    wijziging_oorzaak_kort: Optional[str] = field(
        default=None,
        metadata={
            "name": "WijzigingOorzaakKort",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 25,
        },
    )
    wijziging_oorzaak_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "WijzigingOorzaakLang",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    wijziging_station: List[StationType] = field(
        default_factory=list,
        metadata={
            "name": "WijzigingStation",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
    presentatie_wijziging: Optional[MeertaligeUitingenType] = field(
        default=None,
        metadata={
            "name": "PresentatieWijziging",
            "type": "Element",
            "namespace": "urn:ndov:cdm:trein:reisinformatie:data:2",
        },
    )
