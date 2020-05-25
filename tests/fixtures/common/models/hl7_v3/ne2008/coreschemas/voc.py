from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class Abenakian(Enum):
    """
    abstDomain: A18174 (C-0-T18130-A18131-A18132-A18171-A18174-cpt)
    :cvar X_AAQ:
    :cvar X_MAC:
    :cvar X_ABE:
    """
    X_AAQ = "x-AAQ"
    X_MAC = "x-MAC"
    X_ABE = "x-ABE"


class AcknowledgementCondition(Enum):
    """
    vocSet: T155 (C-0-T155-cpt)
    :cvar AL:
    :cvar ER:
    :cvar NE:
    """
    AL = "AL"
    ER = "ER"
    NE = "NE"


class AcknowledgementDetailCode(Enum):
    """
    vocSet: T19638 (C-0-T19638-cpt)
    :cvar NS260:
    :cvar NS261:
    :cvar NS200:
    :cvar NS250:
    :cvar NS202:
    :cvar NS203:
    :cvar SYN:
    :cvar SYN102:
    :cvar SYN104:
    :cvar SYN110:
    :cvar SYN112:
    :cvar SYN100:
    :cvar SYN101:
    :cvar SYN103:
    :cvar RTUDEST:
    :cvar INTERR:
    :cvar RTEDEST:
    :cvar RTWDEST:
    :cvar NOSTORE:
    """
    NS260 = "NS260"
    NS261 = "NS261"
    NS200 = "NS200"
    NS250 = "NS250"
    NS202 = "NS202"
    NS203 = "NS203"
    SYN = "SYN"
    SYN102 = "SYN102"
    SYN104 = "SYN104"
    SYN110 = "SYN110"
    SYN112 = "SYN112"
    SYN100 = "SYN100"
    SYN101 = "SYN101"
    SYN103 = "SYN103"
    RTUDEST = "RTUDEST"
    INTERR = "INTERR"
    RTEDEST = "RTEDEST"
    RTWDEST = "RTWDEST"
    NOSTORE = "NOSTORE"


class AcknowledgementDetailNotSupportedCode(Enum):
    """
    abstDomain: A19640 (C-0-T19638-A19640-cpt)
    :cvar NS260:
    :cvar NS261:
    :cvar NS200:
    :cvar NS250:
    :cvar NS202:
    :cvar NS203:
    """
    NS260 = "NS260"
    NS261 = "NS261"
    NS200 = "NS200"
    NS250 = "NS250"
    NS202 = "NS202"
    NS203 = "NS203"


class AcknowledgementDetailSyntaxErrorCode(Enum):
    """
    specDomain: S22075 (C-0-T19638-S22075-cpt)
    :cvar SYN:
    :cvar SYN102:
    :cvar SYN104:
    :cvar SYN110:
    :cvar SYN112:
    :cvar SYN100:
    :cvar SYN101:
    :cvar SYN103:
    """
    SYN = "SYN"
    SYN102 = "SYN102"
    SYN104 = "SYN104"
    SYN110 = "SYN110"
    SYN112 = "SYN112"
    SYN100 = "SYN100"
    SYN101 = "SYN101"
    SYN103 = "SYN103"


class AcknowledgementDetailType(Enum):
    """
    vocSet: T19358 (C-0-T19358-cpt)
    :cvar E:
    :cvar I:
    :cvar W:
    """
    E = "E"
    I = "I"
    W = "W"


class AcknowledgementType(Enum):
    """
    vocSet: T8 (C-0-T8-cpt)
    :cvar CA:
    :cvar CE:
    :cvar CR:
    :cvar AA:
    :cvar AE:
    :cvar AR:
    """
    CA = "CA"
    CE = "CE"
    CR = "CR"
    AA = "AA"
    AE = "AE"
    AR = "AR"


class ActAccommodationReason(Enum):
    """
    abstDomain: A17425 (C-0-T14878-A17425-cpt)
    :cvar ACCREQNA:
    :cvar FLRCNV:
    :cvar MEDNEC:
    :cvar PAT:
    """
    ACCREQNA = "ACCREQNA"
    FLRCNV = "FLRCNV"
    MEDNEC = "MEDNEC"
    PAT = "PAT"


class ActAccountCode(Enum):
    """
    abstDomain: A14809 (C-0-T13953-A13954-A14809-cpt)
    :cvar AE:
    :cvar DN:
    :cvar DV:
    :cvar MC:
    :cvar V:
    :cvar CASH:
    :cvar ACCTRECEIVABLE:
    :cvar PBILLACCT:
    """
    AE = "AE"
    DN = "DN"
    DV = "DV"
    MC = "MC"
    V = "V"
    CASH = "CASH"
    ACCTRECEIVABLE = "ACCTRECEIVABLE"
    PBILLACCT = "PBILLACCT"


class ActAdjudicationCode(Enum):
    """
    abstDomain: A17616 (C-0-T13953-A13954-A17616-cpt)
    :cvar AA:
    :cvar ANF:
    :cvar AR:
    :cvar AS_VALUE:
    """
    AA = "AA"
    ANF = "ANF"
    AR = "AR"
    AS_VALUE = "AS"


class ActAdjudicationGroupCode(Enum):
    """
    abstDomain: A17968 (C-0-T13953-A13954-A17968-cpt)
    :cvar CONT:
    :cvar DAY:
    :cvar LOC:
    :cvar MONTH:
    :cvar PERIOD:
    :cvar PROV:
    :cvar WEEK:
    :cvar YEAR:
    """
    CONT = "CONT"
    DAY = "DAY"
    LOC = "LOC"
    MONTH = "MONTH"
    PERIOD = "PERIOD"
    PROV = "PROV"
    WEEK = "WEEK"
    YEAR = "YEAR"


class ActAdjudicationResultActionCode(Enum):
    """
    abstDomain: A17472 (C-0-T13953-A13954-A17472-cpt)
    :cvar DISPLAY:
    :cvar FORM:
    """
    DISPLAY = "DISPLAY"
    FORM = "FORM"


class ActAdministrativeAuthorizationDetectedIssueCode(Enum):
    """
    abstDomain: A19620 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-cpt)
    :cvar CODE_INVAL:
    :cvar CODE_DEPREC:
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    :cvar COMPLY:
    :cvar PLYDOC:
    :cvar PLYPHRM:
    :cvar ABUSE:
    :cvar FRAUD:
    :cvar DOSE:
    :cvar DOSEDUR:
    :cvar DOSEIVL:
    :cvar DOSEH:
    :cvar DOSEL:
    :cvar DOSECOND:
    :cvar MDOSE:
    :cvar LEN_RANGE:
    :cvar LEN_LONG:
    :cvar LEN_SHORT:
    :cvar OBSA:
    :cvar AGE:
    :cvar COND:
    :cvar GEND:
    :cvar GEN:
    :cvar LAB:
    :cvar REACT:
    :cvar RREACT:
    :cvar CREACT:
    :cvar REP_RANGE:
    :cvar MAXOCCURS:
    :cvar MINOCCURS:
    :cvar VALIDAT:
    :cvar KEY205:
    :cvar KEY204:
    :cvar BUS:
    :cvar MISSCOND:
    :cvar NODUPS:
    :cvar ILLEGAL:
    :cvar FORMAT:
    :cvar MISSMAND:
    :cvar NAT:
    """
    CODE_INVAL = "CODE_INVAL"
    CODE_DEPREC = "CODE_DEPREC"
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"
    COMPLY = "COMPLY"
    PLYDOC = "PLYDOC"
    PLYPHRM = "PLYPHRM"
    ABUSE = "ABUSE"
    FRAUD = "FRAUD"
    DOSE = "DOSE"
    DOSEDUR = "DOSEDUR"
    DOSEIVL = "DOSEIVL"
    DOSEH = "DOSEH"
    DOSEL = "DOSEL"
    DOSECOND = "DOSECOND"
    MDOSE = "MDOSE"
    LEN_RANGE = "LEN_RANGE"
    LEN_LONG = "LEN_LONG"
    LEN_SHORT = "LEN_SHORT"
    OBSA = "OBSA"
    AGE = "AGE"
    COND = "COND"
    GEND = "GEND"
    GEN = "GEN"
    LAB = "LAB"
    REACT = "REACT"
    RREACT = "RREACT"
    CREACT = "CREACT"
    REP_RANGE = "REP_RANGE"
    MAXOCCURS = "MAXOCCURS"
    MINOCCURS = "MINOCCURS"
    VALIDAT = "VALIDAT"
    KEY205 = "KEY205"
    KEY204 = "KEY204"
    BUS = "BUS"
    MISSCOND = "MISSCOND"
    NODUPS = "NODUPS"
    ILLEGAL = "ILLEGAL"
    FORMAT = "FORMAT"
    MISSMAND = "MISSMAND"
    NAT = "NAT"


class ActAdministrativeRuleDetectedIssueCode(Enum):
    """
    abstDomain: A19621 (C-0-T14878-A19692-A19781-A16124-A19429-A19621-cpt)
    :cvar KEY205:
    :cvar KEY204:
    """
    KEY205 = "KEY205"
    KEY204 = "KEY204"


class ActBillableModifierCode(Enum):
    """
    abstDomain: A19821 (C-0-T13953-A13954-A19821-cpt)
    :cvar CPTM:
    :cvar HCPCSA:
    """
    CPTM = "CPTM"
    HCPCSA = "HCPCSA"


class ActBillingArrangementCode(Enum):
    """
    abstDomain: A17478 (C-0-T13953-A13954-A17478-cpt)
    :cvar FFS:
    :cvar FFCS:
    :cvar TFS:
    :cvar FFPS:
    :cvar BLK:
    :cvar CAP:
    :cvar CONTF:
    :cvar FINBILL:
    :cvar ROST:
    :cvar SESS:
    """
    FFS = "FFS"
    FFCS = "FFCS"
    TFS = "TFS"
    FFPS = "FFPS"
    BLK = "BLK"
    CAP = "CAP"
    CONTF = "CONTF"
    FINBILL = "FINBILL"
    ROST = "ROST"
    SESS = "SESS"


class ActBoundedRoicode(Enum):
    """
    abstDomain: A17896 (C-0-T13953-A13954-A17896-cpt)
    :cvar ROIFS:
    :cvar ROIPS:
    """
    ROIFS = "ROIFS"
    ROIPS = "ROIPS"


class ActClass(Enum):
    """
    vocSet: T11527 (C-0-T11527-cpt)
    :cvar PCPR:
    :cvar ENC:
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    :cvar DOC:
    :cvar COMPOSITION:
    :cvar ENTRY:
    :cvar CLUSTER:
    :cvar BATTERY:
    :cvar EXTRACT:
    :cvar EHR:
    :cvar ORGANIZER:
    :cvar CATEGORY:
    :cvar DOCBODY:
    :cvar DOCSECT:
    :cvar TOPIC:
    :cvar FOLDER:
    :cvar FCNTRCT:
    :cvar COV:
    :cvar CNTRCT:
    :cvar CACT:
    :cvar ACTN:
    :cvar INFO:
    :cvar STC:
    :cvar EXPOS:
    :cvar AEXPOS:
    :cvar TEXPOS:
    :cvar CASE:
    :cvar OUTB:
    :cvar COND:
    :cvar GEN:
    :cvar SEQ:
    :cvar SEQVAR:
    :cvar DETPOL:
    :cvar EXP:
    :cvar LOC:
    :cvar PHN:
    :cvar POL:
    :cvar OBSSER:
    :cvar OBSCOR:
    :cvar POS:
    :cvar POSACC:
    :cvar POSCOORD:
    :cvar ROIBND:
    :cvar ROIOVL:
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    :cvar SFWL:
    :cvar LLD:
    :cvar PRN:
    :cvar RLD:
    :cvar SIT:
    :cvar STN:
    :cvar IMAGING_SUBJECT_ORIENTATION:
    :cvar OBS:
    :cvar CNOD:
    :cvar VERIF:
    :cvar CLNTRL:
    :cvar ALRT:
    :cvar DGIMG:
    :cvar INVSTG:
    :cvar SPCOBS:
    :cvar POLICY:
    :cvar JURISPOL:
    :cvar ORGPOL:
    :cvar SCOPOL:
    :cvar STDPOL:
    :cvar PROC:
    :cvar SPECCOLLECT:
    :cvar SPLY:
    :cvar DIET:
    :cvar ACT:
    :cvar SUBST:
    :cvar ACSN:
    :cvar ACCM:
    :cvar ACCT:
    :cvar CTTEVENT:
    :cvar CONS:
    :cvar CONTREG:
    :cvar DISPACT:
    :cvar ADJUD:
    :cvar XACT:
    :cvar INC:
    :cvar INFRM:
    :cvar INVE:
    :cvar MPROT:
    :cvar REG:
    :cvar REV:
    :cvar SPCTRT:
    :cvar SBADM:
    :cvar TRFR:
    :cvar TRNS:
    :cvar LIST_VALUE:
    """
    PCPR = "PCPR"
    ENC = "ENC"
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"
    EXPOS = "EXPOS"
    AEXPOS = "AEXPOS"
    TEXPOS = "TEXPOS"
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"
    POLICY = "POLICY"
    JURISPOL = "JURISPOL"
    ORGPOL = "ORGPOL"
    SCOPOL = "SCOPOL"
    STDPOL = "STDPOL"
    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"
    SPLY = "SPLY"
    DIET = "DIET"
    ACT = "ACT"
    SUBST = "SUBST"
    ACSN = "ACSN"
    ACCM = "ACCM"
    ACCT = "ACCT"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    CONTREG = "CONTREG"
    DISPACT = "DISPACT"
    ADJUD = "ADJUD"
    XACT = "XACT"
    INC = "INC"
    INFRM = "INFRM"
    INVE = "INVE"
    MPROT = "MPROT"
    REG = "REG"
    REV = "REV"
    SPCTRT = "SPCTRT"
    SBADM = "SBADM"
    TRFR = "TRFR"
    TRNS = "TRNS"
    LIST_VALUE = "LIST"


class ActClassCareProvision(Enum):
    """
    specDomain: S18964 (C-0-T11527-S13856-S18964-cpt)
    :cvar PCPR:
    :cvar ENC:
    """
    PCPR = "PCPR"
    ENC = "ENC"


class ActClassClinicalDocument(Enum):
    """
    specDomain: S13948 (C-0-T11527-S13856-A19445-S20083-S18938-S13948-cpt)
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    """
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"


class ActClassComposition(Enum):
    """
    specDomain: S20083 (C-0-T11527-S13856-A19445-S20083-cpt)
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    :cvar DOC:
    :cvar COMPOSITION:
    """
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"


class ActClassCondition(Enum):
    """
    specDomain: S18862 (C-0-T11527-S13856-S11529-S18862-cpt)
    :cvar CASE:
    :cvar OUTB:
    :cvar COND:
    """
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"


class ActClassContainer(Enum):
    """
    abstDomain: A19445 (C-0-T11527-S13856-A19445-cpt)
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    :cvar DOC:
    :cvar COMPOSITION:
    :cvar ENTRY:
    :cvar CLUSTER:
    :cvar BATTERY:
    :cvar EXTRACT:
    :cvar EHR:
    :cvar ORGANIZER:
    :cvar CATEGORY:
    :cvar DOCBODY:
    :cvar DOCSECT:
    :cvar TOPIC:
    :cvar FOLDER:
    """
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"


class ActClassContract(Enum):
    """
    specDomain: S14002 (C-0-T11527-S13856-S14002-cpt)
    :cvar FCNTRCT:
    :cvar COV:
    :cvar CNTRCT:
    """
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"


class ActClassControlAct(Enum):
    """
    specDomain: S11534 (C-0-T11527-S13856-S11534-cpt)
    :cvar CACT:
    :cvar ACTN:
    :cvar INFO:
    :cvar STC:
    """
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"


class ActClassDocument(Enum):
    """
    specDomain: S18938 (C-0-T11527-S13856-A19445-S20083-S18938-cpt)
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    :cvar DOC:
    """
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"


class ActClassEntry(Enum):
    """
    specDomain: S20087 (C-0-T11527-S13856-A19445-S20087-cpt)
    :cvar ENTRY:
    :cvar CLUSTER:
    :cvar BATTERY:
    """
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"


class ActClassExposure(Enum):
    """
    specDomain: S21980 (C-0-T11527-S13856-S21980-cpt)
    :cvar EXPOS:
    :cvar AEXPOS:
    :cvar TEXPOS:
    """
    EXPOS = "EXPOS"
    AEXPOS = "AEXPOS"
    TEXPOS = "TEXPOS"


class ActClassExtract(Enum):
    """
    specDomain: S20080 (C-0-T11527-S13856-A19445-S20080-cpt)
    :cvar EXTRACT:
    :cvar EHR:
    """
    EXTRACT = "EXTRACT"
    EHR = "EHR"


class ActClassFinancialContract(Enum):
    """
    specDomain: S14003 (C-0-T11527-S13856-S14002-S14003-cpt)
    :cvar FCNTRCT:
    :cvar COV:
    """
    FCNTRCT = "FCNTRCT"
    COV = "COV"


class ActClassGenomicObservation(Enum):
    """
    specDomain: S21997 (C-0-T11527-S13856-S11529-S21997-cpt)
    :cvar GEN:
    :cvar SEQ:
    :cvar SEQVAR:
    :cvar DETPOL:
    :cvar EXP:
    :cvar LOC:
    :cvar PHN:
    :cvar POL:
    """
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"


class ActClassObservation(Enum):
    """
    specDomain: S11529 (C-0-T11527-S13856-S11529-cpt)
    :cvar CASE:
    :cvar OUTB:
    :cvar COND:
    :cvar GEN:
    :cvar SEQ:
    :cvar SEQVAR:
    :cvar DETPOL:
    :cvar EXP:
    :cvar LOC:
    :cvar PHN:
    :cvar POL:
    :cvar OBSSER:
    :cvar OBSCOR:
    :cvar POS:
    :cvar POSACC:
    :cvar POSCOORD:
    :cvar ROIBND:
    :cvar ROIOVL:
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    :cvar SFWL:
    :cvar LLD:
    :cvar PRN:
    :cvar RLD:
    :cvar SIT:
    :cvar STN:
    :cvar IMAGING_SUBJECT_ORIENTATION:
    :cvar OBS:
    :cvar CNOD:
    :cvar VERIF:
    :cvar CLNTRL:
    :cvar ALRT:
    :cvar DGIMG:
    :cvar INVSTG:
    :cvar SPCOBS:
    """
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"


class ActClassObservationSeries(Enum):
    """
    specDomain: S18875 (C-0-T11527-S13856-S11529-S18875-cpt)
    :cvar OBSSER:
    :cvar OBSCOR:
    """
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"


class ActClassOrganizer(Enum):
    """
    specDomain: S20084 (C-0-T11527-S13856-A19445-S20084-cpt)
    :cvar ORGANIZER:
    :cvar CATEGORY:
    :cvar DOCBODY:
    :cvar DOCSECT:
    :cvar TOPIC:
    """
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"


class ActClassPolicy(Enum):
    """
    specDomain: S21981 (C-0-T11527-S13856-S21981-cpt)
    :cvar POLICY:
    :cvar JURISPOL:
    :cvar ORGPOL:
    :cvar SCOPOL:
    :cvar STDPOL:
    """
    POLICY = "POLICY"
    JURISPOL = "JURISPOL"
    ORGPOL = "ORGPOL"
    SCOPOL = "SCOPOL"
    STDPOL = "STDPOL"


class ActClassPosition(Enum):
    """
    specDomain: S21646 (C-0-T11527-S13856-S11529-S21646-cpt)
    :cvar POS:
    :cvar POSACC:
    :cvar POSCOORD:
    """
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"


class ActClassProcedure(Enum):
    """
    specDomain: S11532 (C-0-T11527-S13856-S11532-cpt)
    :cvar PROC:
    :cvar SPECCOLLECT:
    """
    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"


class ActClassPublicHealthCase(Enum):
    """
    specDomain: S11530 (C-0-T11527-S13856-S11529-S18862-S11530-cpt)
    :cvar CASE:
    :cvar OUTB:
    """
    CASE = "CASE"
    OUTB = "OUTB"


class ActClassRoi(Enum):
    """
    abstDomain: A17893 (C-0-T11527-S13856-S11529-A17893-cpt)
    :cvar ROIBND:
    :cvar ROIOVL:
    """
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"


class ActClassRoot(Enum):
    """
    specDomain: S13856 (C-0-T11527-S13856-cpt)
    :cvar PCPR:
    :cvar ENC:
    :cvar DOCCLIN:
    :cvar CDALVLONE:
    :cvar DOC:
    :cvar COMPOSITION:
    :cvar ENTRY:
    :cvar CLUSTER:
    :cvar BATTERY:
    :cvar EXTRACT:
    :cvar EHR:
    :cvar ORGANIZER:
    :cvar CATEGORY:
    :cvar DOCBODY:
    :cvar DOCSECT:
    :cvar TOPIC:
    :cvar FOLDER:
    :cvar FCNTRCT:
    :cvar COV:
    :cvar CNTRCT:
    :cvar CACT:
    :cvar ACTN:
    :cvar INFO:
    :cvar STC:
    :cvar EXPOS:
    :cvar AEXPOS:
    :cvar TEXPOS:
    :cvar CASE:
    :cvar OUTB:
    :cvar COND:
    :cvar GEN:
    :cvar SEQ:
    :cvar SEQVAR:
    :cvar DETPOL:
    :cvar EXP:
    :cvar LOC:
    :cvar PHN:
    :cvar POL:
    :cvar OBSSER:
    :cvar OBSCOR:
    :cvar POS:
    :cvar POSACC:
    :cvar POSCOORD:
    :cvar ROIBND:
    :cvar ROIOVL:
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    :cvar SFWL:
    :cvar LLD:
    :cvar PRN:
    :cvar RLD:
    :cvar SIT:
    :cvar STN:
    :cvar IMAGING_SUBJECT_ORIENTATION:
    :cvar OBS:
    :cvar CNOD:
    :cvar VERIF:
    :cvar CLNTRL:
    :cvar ALRT:
    :cvar DGIMG:
    :cvar INVSTG:
    :cvar SPCOBS:
    :cvar POLICY:
    :cvar JURISPOL:
    :cvar ORGPOL:
    :cvar SCOPOL:
    :cvar STDPOL:
    :cvar PROC:
    :cvar SPECCOLLECT:
    :cvar SPLY:
    :cvar DIET:
    :cvar ACT:
    :cvar SUBST:
    :cvar ACSN:
    :cvar ACCM:
    :cvar ACCT:
    :cvar CTTEVENT:
    :cvar CONS:
    :cvar CONTREG:
    :cvar DISPACT:
    :cvar ADJUD:
    :cvar XACT:
    :cvar INC:
    :cvar INFRM:
    :cvar INVE:
    :cvar MPROT:
    :cvar REG:
    :cvar REV:
    :cvar SPCTRT:
    :cvar SBADM:
    :cvar TRFR:
    :cvar TRNS:
    :cvar LIST_VALUE:
    """
    PCPR = "PCPR"
    ENC = "ENC"
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"
    EXPOS = "EXPOS"
    AEXPOS = "AEXPOS"
    TEXPOS = "TEXPOS"
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"
    POLICY = "POLICY"
    JURISPOL = "JURISPOL"
    ORGPOL = "ORGPOL"
    SCOPOL = "SCOPOL"
    STDPOL = "STDPOL"
    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"
    SPLY = "SPLY"
    DIET = "DIET"
    ACT = "ACT"
    SUBST = "SUBST"
    ACSN = "ACSN"
    ACCM = "ACCM"
    ACCT = "ACCT"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    CONTREG = "CONTREG"
    DISPACT = "DISPACT"
    ADJUD = "ADJUD"
    XACT = "XACT"
    INC = "INC"
    INFRM = "INFRM"
    INVE = "INVE"
    MPROT = "MPROT"
    REG = "REG"
    REV = "REV"
    SPCTRT = "SPCTRT"
    SBADM = "SBADM"
    TRFR = "TRFR"
    TRNS = "TRNS"
    LIST_VALUE = "LIST"


class ActClassSubjectBodyPosition(Enum):
    """
    abstDomain: A19798 (C-0-T11527-S13856-S11529-A19796-A19798-cpt)
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    :cvar SFWL:
    :cvar LLD:
    :cvar PRN:
    :cvar RLD:
    :cvar SIT:
    :cvar STN:
    """
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"


class ActClassSubjectPhysicalPosition(Enum):
    """
    abstDomain: A19796 (C-0-T11527-S13856-S11529-A19796-cpt)
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    :cvar SFWL:
    :cvar LLD:
    :cvar PRN:
    :cvar RLD:
    :cvar SIT:
    :cvar STN:
    :cvar IMAGING_SUBJECT_ORIENTATION:
    """
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"


class ActClassSupine(Enum):
    """
    specDomain: S21935 (C-0-T11527-S13856-S11529-A19796-A19798-S21935-cpt)
    :cvar SUP:
    :cvar RTRD:
    :cvar TRD:
    """
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"


class ActClassSupply(Enum):
    """
    specDomain: S11535 (C-0-T11527-S13856-S11535-cpt)
    :cvar SPLY:
    :cvar DIET:
    """
    SPLY = "SPLY"
    DIET = "DIET"


class ActConditionList(Enum):
    """
    specDomain: S21322 (C-0-T13953-A13954-A19364-A19370-S21322-cpt)
    :cvar CONDLIST:
    :cvar INTOLIST:
    :cvar PROBLIST:
    :cvar RISKLIST:
    """
    CONDLIST = "CONDLIST"
    INTOLIST = "INTOLIST"
    PROBLIST = "PROBLIST"
    RISKLIST = "RISKLIST"


class ActConsentInformationAccessOverrideReason(Enum):
    """
    abstDomain: A19894 (C-0-T14878-A19894-cpt)
    :cvar OVRER:
    :cvar OVRPJ:
    :cvar OVRPS:
    :cvar OVRTPS:
    """
    OVRER = "OVRER"
    OVRPJ = "OVRPJ"
    OVRPS = "OVRPS"
    OVRTPS = "OVRTPS"


class ActConsentType(Enum):
    """
    abstDomain: A19897 (C-0-T13953-A19897-cpt)
    :cvar INFA:
    :cvar INFASO:
    :cvar INFAO:
    :cvar RESEARCH:
    :cvar RSDID:
    :cvar RSREID:
    :cvar ICOL:
    :cvar IDSCL:
    :cvar IRDSCL:
    """
    INFA = "INFA"
    INFASO = "INFASO"
    INFAO = "INFAO"
    RESEARCH = "RESEARCH"
    RSDID = "RSDID"
    RSREID = "RSREID"
    ICOL = "ICOL"
    IDSCL = "IDSCL"
    IRDSCL = "IRDSCL"


class ActContainerRegistrationCode(Enum):
    """
    abstDomain: A14058 (C-0-T13953-A13954-A14058-cpt)
    :cvar X:
    :cvar ID:
    :cvar IP:
    :cvar O:
    :cvar L:
    :cvar M:
    :cvar R:
    """
    X = "X"
    ID = "ID"
    IP = "IP"
    O = "O"
    L = "L"
    M = "M"
    R = "R"


class ActCoverageAuthorizationConfirmationCode(Enum):
    """
    abstDomain: A17491 (C-0-T13953-A13954-A17487-A17491-cpt)
    :cvar AUTH:
    :cvar NAUTH:
    """
    AUTH = "AUTH"
    NAUTH = "NAUTH"


class ActCoverageMaximaCodes(Enum):
    """
    specDomain: S22239 (C-0-T13953-A13954-A17496-S22239-cpt)
    :cvar COVMX:
    :cvar LFEMX:
    :cvar PRDMX:
    """
    COVMX = "COVMX"
    LFEMX = "LFEMX"
    PRDMX = "PRDMX"


class ActCoverageQuantityLimitCode(Enum):
    """
    abstDomain: A19933 (C-0-T13953-A13954-A17496-A19933-cpt)
    :cvar NETAMT:
    :cvar UNITPRICE:
    :cvar UNITQTY:
    :cvar COVPRD:
    :cvar LFEMX:
    :cvar PRDMX:
    """
    NETAMT = "NETAMT"
    UNITPRICE = "UNITPRICE"
    UNITQTY = "UNITQTY"
    COVPRD = "COVPRD"
    LFEMX = "LFEMX"
    PRDMX = "PRDMX"


class ActCredentialedCareProvisionPersonCode(Enum):
    """
    abstDomain: A19791 (C-0-T13953-A19789-A19790-A19791-cpt)
    :cvar CPGC:
    :cvar CAMC:
    :cvar CAIC:
    :cvar CACC:
    :cvar CAPC:
    :cvar CANC:
    :cvar CBGC:
    :cvar CCCC:
    :cvar CCGC:
    :cvar CMGC:
    :cvar CCPC:
    :cvar CCSC:
    :cvar CDEC:
    :cvar CDRC:
    :cvar CEMC:
    :cvar CFPC:
    :cvar CIMC:
    :cvar CNSC:
    :cvar CNEC:
    :cvar CNQC:
    :cvar CNMC:
    :cvar COGC:
    :cvar COMC:
    :cvar COPC:
    :cvar COSC:
    :cvar COTC:
    :cvar CPEC:
    :cvar CPRC:
    :cvar CPSC:
    :cvar CPYC:
    :cvar CPHC:
    :cvar CROC:
    :cvar CRPC:
    :cvar CSUC:
    :cvar CTSC:
    :cvar CURC:
    :cvar CVSC:
    :cvar LGPC:
    """
    CPGC = "CPGC"
    CAMC = "CAMC"
    CAIC = "CAIC"
    CACC = "CACC"
    CAPC = "CAPC"
    CANC = "CANC"
    CBGC = "CBGC"
    CCCC = "CCCC"
    CCGC = "CCGC"
    CMGC = "CMGC"
    CCPC = "CCPC"
    CCSC = "CCSC"
    CDEC = "CDEC"
    CDRC = "CDRC"
    CEMC = "CEMC"
    CFPC = "CFPC"
    CIMC = "CIMC"
    CNSC = "CNSC"
    CNEC = "CNEC"
    CNQC = "CNQC"
    CNMC = "CNMC"
    COGC = "COGC"
    COMC = "COMC"
    COPC = "COPC"
    COSC = "COSC"
    COTC = "COTC"
    CPEC = "CPEC"
    CPRC = "CPRC"
    CPSC = "CPSC"
    CPYC = "CPYC"
    CPHC = "CPHC"
    CROC = "CROC"
    CRPC = "CRPC"
    CSUC = "CSUC"
    CTSC = "CTSC"
    CURC = "CURC"
    CVSC = "CVSC"
    LGPC = "LGPC"


class ActCredentialedCareProvisionProgramCode(Enum):
    """
    abstDomain: A19792 (C-0-T13953-A19789-A19790-A19792-cpt)
    :cvar AAMC:
    :cvar AALC:
    :cvar ABHC:
    :cvar ACAC:
    :cvar AHOC:
    :cvar ACHC:
    :cvar ALTC:
    :cvar AOSC:
    :cvar CACS:
    :cvar CAMI:
    :cvar CAST:
    :cvar CBAR:
    :cvar CCAR:
    :cvar COPD:
    :cvar CCAD:
    :cvar CDEP:
    :cvar CDIA:
    :cvar CDGD:
    :cvar CEPI:
    :cvar CFEL:
    :cvar CHFC:
    :cvar CHRO:
    :cvar CHYP:
    :cvar CMIH:
    :cvar CMSC:
    :cvar CONC:
    :cvar CORT:
    :cvar COJR:
    :cvar CPAD:
    :cvar CPND:
    :cvar CPST:
    :cvar CSIC:
    :cvar CSLD:
    :cvar CSPT:
    :cvar CSDM:
    :cvar CTBU:
    :cvar CVDC:
    :cvar CWOH:
    :cvar CWMA:
    """
    AAMC = "AAMC"
    AALC = "AALC"
    ABHC = "ABHC"
    ACAC = "ACAC"
    AHOC = "AHOC"
    ACHC = "ACHC"
    ALTC = "ALTC"
    AOSC = "AOSC"
    CACS = "CACS"
    CAMI = "CAMI"
    CAST = "CAST"
    CBAR = "CBAR"
    CCAR = "CCAR"
    COPD = "COPD"
    CCAD = "CCAD"
    CDEP = "CDEP"
    CDIA = "CDIA"
    CDGD = "CDGD"
    CEPI = "CEPI"
    CFEL = "CFEL"
    CHFC = "CHFC"
    CHRO = "CHRO"
    CHYP = "CHYP"
    CMIH = "CMIH"
    CMSC = "CMSC"
    CONC = "CONC"
    CORT = "CORT"
    COJR = "COJR"
    CPAD = "CPAD"
    CPND = "CPND"
    CPST = "CPST"
    CSIC = "CSIC"
    CSLD = "CSLD"
    CSPT = "CSPT"
    CSDM = "CSDM"
    CTBU = "CTBU"
    CVDC = "CVDC"
    CWOH = "CWOH"
    CWMA = "CWMA"


class ActDietCode(Enum):
    """
    abstDomain: A10376 (C-0-T13953-A13954-A10376-cpt)
    :cvar BR:
    :cvar DM:
    :cvar FAST:
    :cvar GF:
    :cvar LQ:
    :cvar LF:
    :cvar LP:
    :cvar LS:
    :cvar VLI:
    :cvar NF:
    :cvar N:
    :cvar PAR:
    :cvar PAF:
    :cvar RD:
    :cvar SCH:
    :cvar T:
    """
    BR = "BR"
    DM = "DM"
    FAST = "FAST"
    GF = "GF"
    LQ = "LQ"
    LF = "LF"
    LP = "LP"
    LS = "LS"
    VLI = "VLI"
    NF = "NF"
    N = "N"
    PAR = "PAR"
    PAF = "PAF"
    RD = "RD"
    SCH = "SCH"
    T = "T"


class ActEncounterCode(Enum):
    """
    abstDomain: A13955 (C-0-T13953-A19820-A13955-cpt)
    :cvar IMP:
    :cvar ACUTE:
    :cvar NONAC:
    :cvar ALC:
    :cvar CARD:
    :cvar CHR:
    :cvar DNTL:
    :cvar DRGRHB:
    :cvar GENRL:
    :cvar MED:
    :cvar OBS:
    :cvar ONC:
    :cvar PALL:
    :cvar PED:
    :cvar PHAR:
    :cvar PHYRHB:
    :cvar PSYCH:
    :cvar SURG:
    :cvar AMB:
    :cvar EMER:
    :cvar FLD:
    :cvar HH:
    :cvar SS:
    :cvar VR:
    """
    IMP = "IMP"
    ACUTE = "ACUTE"
    NONAC = "NONAC"
    ALC = "ALC"
    CARD = "CARD"
    CHR = "CHR"
    DNTL = "DNTL"
    DRGRHB = "DRGRHB"
    GENRL = "GENRL"
    MED = "MED"
    OBS = "OBS"
    ONC = "ONC"
    PALL = "PALL"
    PED = "PED"
    PHAR = "PHAR"
    PHYRHB = "PHYRHB"
    PSYCH = "PSYCH"
    SURG = "SURG"
    AMB = "AMB"
    EMER = "EMER"
    FLD = "FLD"
    HH = "HH"
    SS = "SS"
    VR = "VR"


class ActExposureCode(Enum):
    """
    abstDomain: A19938 (C-0-T13953-A13954-A19938-cpt)
    :cvar HOMECARE:
    :cvar CONVEYNC:
    :cvar PLACE:
    :cvar SUBSTNCE:
    :cvar TRAVINT:
    :cvar CHLDCARE:
    :cvar HLTHCARE:
    :cvar PTNTCARE:
    :cvar HOSPPTNT:
    :cvar HOSPVSTR:
    :cvar HOUSEHLD:
    :cvar INMATE:
    :cvar INTIMATE:
    :cvar LTRMCARE:
    :cvar SCHOOL2:
    :cvar SOCIAL2:
    :cvar WORK2:
    """
    HOMECARE = "HOMECARE"
    CONVEYNC = "CONVEYNC"
    PLACE = "PLACE"
    SUBSTNCE = "SUBSTNCE"
    TRAVINT = "TRAVINT"
    CHLDCARE = "CHLDCARE"
    HLTHCARE = "HLTHCARE"
    PTNTCARE = "PTNTCARE"
    HOSPPTNT = "HOSPPTNT"
    HOSPVSTR = "HOSPVSTR"
    HOUSEHLD = "HOUSEHLD"
    INMATE = "INMATE"
    INTIMATE = "INTIMATE"
    LTRMCARE = "LTRMCARE"
    SCHOOL2 = "SCHOOL2"
    SOCIAL2 = "SOCIAL2"
    WORK2 = "WORK2"


class ActExposureLevelCode(Enum):
    """
    vocSet: T19939 (C-0-T19939-cpt)
    :cvar HIGH:
    :cvar LOW:
    :cvar MEDIUM:
    """
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class ActFinancialTransactionCode(Enum):
    """
    abstDomain: A14804 (C-0-T13953-A13954-A14804-cpt)
    :cvar CHRG:
    :cvar REV:
    """
    CHRG = "CHRG"
    REV = "REV"


class ActHealthInsuranceTypeCode(Enum):
    """
    abstDomain: A19857 (C-0-T13953-A13954-A19855-A19856-A19857-cpt)
    :cvar MCPOL:
    :cvar HMO:
    :cvar POS:
    :cvar PPO:
    :cvar DENTAL:
    :cvar DISEASE:
    :cvar DRUGPOL:
    :cvar EHCPOL:
    :cvar HIP:
    :cvar HSAPOL:
    :cvar LTC:
    :cvar MENTPOL:
    :cvar SUBPOL:
    :cvar VISPOL:
    """
    MCPOL = "MCPOL"
    HMO = "HMO"
    POS = "POS"
    PPO = "PPO"
    DENTAL = "DENTAL"
    DISEASE = "DISEASE"
    DRUGPOL = "DRUGPOL"
    EHCPOL = "EHCPOL"
    HIP = "HIP"
    HSAPOL = "HSAPOL"
    LTC = "LTC"
    MENTPOL = "MENTPOL"
    SUBPOL = "SUBPOL"
    VISPOL = "VISPOL"


class ActIneligibilityReason(Enum):
    """
    abstDomain: A19355 (C-0-T14878-A19871-A19694-A19355-cpt)
    :cvar COVSUS:
    :cvar DECSD:
    :cvar REGERR:
    """
    COVSUS = "COVSUS"
    DECSD = "DECSD"
    REGERR = "REGERR"


class ActInformationAccess(Enum):
    """
    specDomain: S22200 (C-0-T13953-A19897-S22200-cpt)
    :cvar INFA:
    :cvar INFASO:
    :cvar INFAO:
    """
    INFA = "INFA"
    INFASO = "INFASO"
    INFAO = "INFAO"


class ActInformationAccessCode(Enum):
    """
    abstDomain: A19910 (C-0-T13953-A19910-cpt)
    :cvar ACADR:
    :cvar ACALLG:
    :cvar ACOBS:
    :cvar ACDEMO:
    :cvar ACIMMUN:
    :cvar ACLAB:
    :cvar ACMEDC:
    :cvar ACMED:
    :cvar ACPOLPRG:
    :cvar ACPSERV:
    :cvar ACPROV:
    """
    ACADR = "ACADR"
    ACALLG = "ACALLG"
    ACOBS = "ACOBS"
    ACDEMO = "ACDEMO"
    ACIMMUN = "ACIMMUN"
    ACLAB = "ACLAB"
    ACMEDC = "ACMEDC"
    ACMED = "ACMED"
    ACPOLPRG = "ACPOLPRG"
    ACPSERV = "ACPSERV"
    ACPROV = "ACPROV"


class ActInformationAccessContextCode(Enum):
    """
    abstDomain: A19928 (C-0-T13953-A13954-A19928-cpt)
    :cvar INFCON:
    :cvar INFDNG:
    :cvar INFPWR:
    :cvar INFEMER:
    :cvar INFCRT:
    """
    INFCON = "INFCON"
    INFDNG = "INFDNG"
    INFPWR = "INFPWR"
    INFEMER = "INFEMER"
    INFCRT = "INFCRT"


class ActInformationCategoryCode(Enum):
    """
    abstDomain: A19752 (C-0-T13953-A19752-cpt)
    :cvar ALLGCAT:
    :cvar COBSCAT:
    :cvar DEMOCAT:
    :cvar DICAT:
    :cvar IMMUCAT:
    :cvar LABCAT:
    :cvar MEDCCAT:
    :cvar RXCAT:
    :cvar PSVCCAT:
    """
    ALLGCAT = "ALLGCAT"
    COBSCAT = "COBSCAT"
    DEMOCAT = "DEMOCAT"
    DICAT = "DICAT"
    IMMUCAT = "IMMUCAT"
    LABCAT = "LABCAT"
    MEDCCAT = "MEDCCAT"
    RXCAT = "RXCAT"
    PSVCCAT = "PSVCCAT"


class ActInpatientEncounterCode(Enum):
    """
    specDomain: S16847 (C-0-T13953-A19820-A13955-S16847-cpt)
    :cvar IMP:
    :cvar ACUTE:
    :cvar NONAC:
    """
    IMP = "IMP"
    ACUTE = "ACUTE"
    NONAC = "NONAC"


class ActInsurancePolicyCode(Enum):
    """
    abstDomain: A19350 (C-0-T13953-A13954-A19855-A19350-cpt)
    :cvar AUTOPOL:
    :cvar COL:
    :cvar UNINSMOT:
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    :cvar PUBLICPOL:
    :cvar DENTPRG:
    :cvar MANDPOL:
    :cvar MENTPRG:
    :cvar SAFNET:
    :cvar SUBPRG:
    :cvar EHCPOL:
    :cvar HSAPOL:
    :cvar WCBPOL:
    """
    AUTOPOL = "AUTOPOL"
    COL = "COL"
    UNINSMOT = "UNINSMOT"
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"
    PUBLICPOL = "PUBLICPOL"
    DENTPRG = "DENTPRG"
    MANDPOL = "MANDPOL"
    MENTPRG = "MENTPRG"
    SAFNET = "SAFNET"
    SUBPRG = "SUBPRG"
    EHCPOL = "EHCPOL"
    HSAPOL = "HSAPOL"
    WCBPOL = "WCBPOL"


class ActInsurancePolicyCodeAutomobileByBot(Enum):
    """
    specDomain: S19721 (C-0-T13953-A13954-A19855-A19350-S19721-cpt)
    :cvar AUTOPOL:
    :cvar COL:
    :cvar UNINSMOT:
    """
    AUTOPOL = "AUTOPOL"
    COL = "COL"
    UNINSMOT = "UNINSMOT"


class ActInsurancePolicyCodeDiseaseProgramByBot(Enum):
    """
    specDomain: S22133 (C-0-T13953-A13954-A19855-A19350-S19718-S22133-cpt)
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    """
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"


class ActInsurancePolicyCodePublicHealthcareByBot(Enum):
    """
    specDomain: S19718 (C-0-T13953-A13954-A19855-A19350-S19718-cpt)
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    :cvar PUBLICPOL:
    :cvar DENTPRG:
    :cvar MANDPOL:
    :cvar MENTPRG:
    :cvar SAFNET:
    :cvar SUBPRG:
    """
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"
    PUBLICPOL = "PUBLICPOL"
    DENTPRG = "DENTPRG"
    MANDPOL = "MANDPOL"
    MENTPRG = "MENTPRG"
    SAFNET = "SAFNET"
    SUBPRG = "SUBPRG"


class ActInsurancePolicyCodeSubsidizedHealthProgramByBot(Enum):
    """
    specDomain: S22137 (C-0-T13953-A13954-A19855-A19350-S19718-S22137-cpt)
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    """
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"


class ActInsuranceTypeCode(Enum):
    """
    abstDomain: A19856 (C-0-T13953-A13954-A19855-A19856-cpt)
    :cvar MCPOL:
    :cvar HMO:
    :cvar POS:
    :cvar PPO:
    :cvar DENTAL:
    :cvar DISEASE:
    :cvar DRUGPOL:
    :cvar EHCPOL:
    :cvar HIP:
    :cvar HSAPOL:
    :cvar LTC:
    :cvar MENTPOL:
    :cvar SUBPOL:
    :cvar VISPOL:
    :cvar AUTOPOL:
    :cvar COL:
    :cvar UNINSMOT:
    :cvar LIFE:
    :cvar ANNU:
    :cvar TLIFE:
    :cvar ULIFE:
    :cvar DIS:
    :cvar EWB:
    :cvar FLEXP:
    :cvar PNC:
    :cvar REI:
    :cvar SURPL:
    :cvar UMBRL:
    """
    MCPOL = "MCPOL"
    HMO = "HMO"
    POS = "POS"
    PPO = "PPO"
    DENTAL = "DENTAL"
    DISEASE = "DISEASE"
    DRUGPOL = "DRUGPOL"
    EHCPOL = "EHCPOL"
    HIP = "HIP"
    HSAPOL = "HSAPOL"
    LTC = "LTC"
    MENTPOL = "MENTPOL"
    SUBPOL = "SUBPOL"
    VISPOL = "VISPOL"
    AUTOPOL = "AUTOPOL"
    COL = "COL"
    UNINSMOT = "UNINSMOT"
    LIFE = "LIFE"
    ANNU = "ANNU"
    TLIFE = "TLIFE"
    ULIFE = "ULIFE"
    DIS = "DIS"
    EWB = "EWB"
    FLEXP = "FLEXP"
    PNC = "PNC"
    REI = "REI"
    SURPL = "SURPL"
    UMBRL = "UMBRL"


class ActInvoiceAdjudicationPaymentSummaryCode(Enum):
    """
    abstDomain: A19413 (C-0-T13953-A13954-A19397-A19412-A19413-cpt)
    :cvar CONT:
    :cvar DAY:
    :cvar INVTYPE:
    :cvar LOC:
    :cvar MONTH:
    :cvar PAYEE:
    :cvar PAYOR:
    :cvar PERIOD:
    :cvar PROV:
    :cvar SENDAPP:
    :cvar WEEK:
    :cvar YEAR:
    """
    CONT = "CONT"
    DAY = "DAY"
    INVTYPE = "INVTYPE"
    LOC = "LOC"
    MONTH = "MONTH"
    PAYEE = "PAYEE"
    PAYOR = "PAYOR"
    PERIOD = "PERIOD"
    PROV = "PROV"
    SENDAPP = "SENDAPP"
    WEEK = "WEEK"
    YEAR = "YEAR"


class ActInvoiceDetailGenericAdjudicatorCode(Enum):
    """
    abstDomain: A19411 (C-0-T13953-A13954-A19397-A19401-A19415-A19407-A19411-cpt)
    :cvar COIN:
    :cvar DEDUCTIBLE:
    :cvar COPAYMENT:
    :cvar PAY:
    :cvar SPEND:
    """
    COIN = "COIN"
    DEDUCTIBLE = "DEDUCTIBLE"
    COPAYMENT = "COPAYMENT"
    PAY = "PAY"
    SPEND = "SPEND"


class ActInvoiceDetailGenericModifierCode(Enum):
    """
    abstDomain: A19410 (C-0-T13953-A13954-A19397-A19401-A19415-A19407-A19410-cpt)
    :cvar ISOL:
    :cvar AFTHRS:
    :cvar OOO:
    """
    ISOL = "ISOL"
    AFTHRS = "AFTHRS"
    OOO = "OOO"


class ActInvoiceDetailGenericProviderCode(Enum):
    """
    abstDomain: A19408 (C-0-T13953-A13954-A19397-A19401-A19415-A19407-A19408-cpt)
    :cvar CANCAPT:
    :cvar DSC:
    :cvar ESA:
    :cvar FFSTOP:
    :cvar FNLFEE:
    :cvar FRSTFEE:
    :cvar MARKUP:
    :cvar MISSAPT:
    :cvar PERMBNS:
    :cvar PERFEE:
    :cvar RESTOCK:
    :cvar TRAVEL:
    :cvar URGENT:
    """
    CANCAPT = "CANCAPT"
    DSC = "DSC"
    ESA = "ESA"
    FFSTOP = "FFSTOP"
    FNLFEE = "FNLFEE"
    FRSTFEE = "FRSTFEE"
    MARKUP = "MARKUP"
    MISSAPT = "MISSAPT"
    PERMBNS = "PERMBNS"
    PERFEE = "PERFEE"
    RESTOCK = "RESTOCK"
    TRAVEL = "TRAVEL"
    URGENT = "URGENT"


class ActInvoiceDetailTaxCode(Enum):
    """
    abstDomain: A19409 (C-0-T13953-A13954-A19397-A19401-A19415-A19407-A19409-cpt)
    :cvar FST:
    :cvar HST:
    :cvar PST:
    """
    FST = "FST"
    HST = "HST"
    PST = "PST"


class ActInvoiceElementModifier(Enum):
    """
    vocSet: T17704 (C-0-T17704-cpt)
    :cvar EFORM:
    :cvar FAX:
    :cvar LINV:
    :cvar PAPER:
    """
    EFORM = "EFORM"
    FAX = "FAX"
    LINV = "LINV"
    PAPER = "PAPER"


class ActInvoiceInterGroupCode(Enum):
    """
    abstDomain: A19400 (C-0-T13953-A13954-A19397-A19398-A19400-cpt)
    :cvar CPNDDRGING:
    :cvar CPNDINDING:
    :cvar CPNDSUPING:
    :cvar DRUGING:
    :cvar FRAMEING:
    :cvar LENSING:
    :cvar PRDING:
    """
    CPNDDRGING = "CPNDDRGING"
    CPNDINDING = "CPNDINDING"
    CPNDSUPING = "CPNDSUPING"
    DRUGING = "DRUGING"
    FRAMEING = "FRAMEING"
    LENSING = "LENSING"
    PRDING = "PRDING"


class ActInvoiceOverrideCode(Enum):
    """
    abstDomain: A17590 (C-0-T13953-A13954-A17590-cpt)
    :cvar COVGE:
    :cvar PYRDELAY:
    :cvar EFORM:
    :cvar FAX:
    :cvar GFTH:
    :cvar LATE:
    :cvar MANUAL:
    :cvar ORTHO:
    :cvar OOJ:
    :cvar PAPER:
    :cvar PIE:
    :cvar REFNR:
    :cvar REPSERV:
    :cvar UNRELAT:
    :cvar VERBAUTH:
    """
    COVGE = "COVGE"
    PYRDELAY = "PYRDELAY"
    EFORM = "EFORM"
    FAX = "FAX"
    GFTH = "GFTH"
    LATE = "LATE"
    MANUAL = "MANUAL"
    ORTHO = "ORTHO"
    OOJ = "OOJ"
    PAPER = "PAPER"
    PIE = "PIE"
    REFNR = "REFNR"
    REPSERV = "REPSERV"
    UNRELAT = "UNRELAT"
    VERBAUTH = "VERBAUTH"


class ActInvoicePaymentCode(Enum):
    """
    abstDomain: A19673 (C-0-T13953-A19673-cpt)
    :cvar BONUS:
    :cvar CFWD:
    :cvar EPYMT:
    :cvar EDU:
    :cvar GARN:
    :cvar PINV:
    :cvar PPRD:
    :cvar PROA:
    :cvar RECOV:
    :cvar RETRO:
    :cvar INVOICE:
    :cvar TRAN:
    """
    BONUS = "BONUS"
    CFWD = "CFWD"
    EPYMT = "EPYMT"
    EDU = "EDU"
    GARN = "GARN"
    PINV = "PINV"
    PPRD = "PPRD"
    PROA = "PROA"
    RECOV = "RECOV"
    RETRO = "RETRO"
    INVOICE = "INVOICE"
    TRAN = "TRAN"


class ActInvoiceRootGroupCode(Enum):
    """
    abstDomain: A19399 (C-0-T13953-A13954-A19397-A19398-A19399-cpt)
    :cvar RXCINV:
    :cvar RXDINV:
    :cvar CPINV:
    :cvar CSPINV:
    :cvar CSINV:
    :cvar FININV:
    :cvar OHSINV:
    :cvar PAINV:
    :cvar SBFINV:
    :cvar VRXINV:
    """
    RXCINV = "RXCINV"
    RXDINV = "RXDINV"
    CPINV = "CPINV"
    CSPINV = "CSPINV"
    CSINV = "CSINV"
    FININV = "FININV"
    OHSINV = "OHSINV"
    PAINV = "PAINV"
    SBFINV = "SBFINV"
    VRXINV = "VRXINV"


class ActMedicalServiceCode(Enum):
    """
    abstDomain: A17449 (C-0-T13953-A19820-A13955-A17449-cpt)
    :cvar ALC:
    :cvar CARD:
    :cvar CHR:
    :cvar DNTL:
    :cvar DRGRHB:
    :cvar GENRL:
    :cvar MED:
    :cvar OBS:
    :cvar ONC:
    :cvar PALL:
    :cvar PED:
    :cvar PHAR:
    :cvar PHYRHB:
    :cvar PSYCH:
    :cvar SURG:
    """
    ALC = "ALC"
    CARD = "CARD"
    CHR = "CHR"
    DNTL = "DNTL"
    DRGRHB = "DRGRHB"
    GENRL = "GENRL"
    MED = "MED"
    OBS = "OBS"
    ONC = "ONC"
    PALL = "PALL"
    PED = "PED"
    PHAR = "PHAR"
    PHYRHB = "PHYRHB"
    PSYCH = "PSYCH"
    SURG = "SURG"


class ActMedicationList(Enum):
    """
    specDomain: S19976 (C-0-T13953-A13954-A19364-S19976-cpt)
    :cvar MEDLIST:
    :cvar CURMEDLIST:
    :cvar DISCMEDLIST:
    :cvar HISTMEDLIST:
    """
    MEDLIST = "MEDLIST"
    CURMEDLIST = "CURMEDLIST"
    DISCMEDLIST = "DISCMEDLIST"
    HISTMEDLIST = "HISTMEDLIST"


class ActMedicationTherapyDurationWorkingListCode(Enum):
    """
    abstDomain: A19788 (C-0-T13953-A13954-A19364-A19710-A19788-cpt)
    :cvar PRN:
    :cvar CHRON:
    :cvar ONET:
    :cvar ACU:
    """
    PRN = "PRN"
    CHRON = "CHRON"
    ONET = "ONET"
    ACU = "ACU"


class ActMood(Enum):
    """
    vocSet: T10196 (C-0-T10196-cpt)
    :cvar PRP:
    :cvar RMD:
    :cvar INT_VALUE:
    :cvar APT:
    :cvar ARQ:
    :cvar PRMS:
    :cvar RQO:
    :cvar SLOT:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar CRT:
    :cvar EVN_CRT:
    :cvar GOL:
    :cvar EXPEC:
    :cvar OPT:
    :cvar PERM:
    :cvar PERMRQ:
    :cvar RSK:
    """
    PRP = "PRP"
    RMD = "RMD"
    INT_VALUE = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    CRT = "CRT"
    EVN_CRT = "EVN.CRT"
    GOL = "GOL"
    EXPEC = "EXPEC"
    OPT = "OPT"
    PERM = "PERM"
    PERMRQ = "PERMRQ"
    RSK = "RSK"


class ActMoodCompletionTrack(Enum):
    """
    abstDomain: A10197 (C-0-T10196-A10197-cpt)
    :cvar PRP:
    :cvar RMD:
    :cvar INT_VALUE:
    :cvar APT:
    :cvar ARQ:
    :cvar PRMS:
    :cvar RQO:
    :cvar SLOT:
    :cvar DEF_VALUE:
    :cvar EVN:
    """
    PRP = "PRP"
    RMD = "RMD"
    INT_VALUE = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"
    DEF_VALUE = "DEF"
    EVN = "EVN"


class ActMoodCriterion(Enum):
    """
    specDomain: S22042 (C-0-T10196-A10202-S22042-cpt)
    :cvar CRT:
    :cvar EVN_CRT:
    """
    CRT = "CRT"
    EVN_CRT = "EVN.CRT"


class ActMoodIntent(Enum):
    """
    specDomain: S10199 (C-0-T10196-A10197-S10199-cpt)
    :cvar PRP:
    :cvar RMD:
    :cvar INT_VALUE:
    :cvar APT:
    :cvar ARQ:
    :cvar PRMS:
    :cvar RQO:
    :cvar SLOT:
    """
    PRP = "PRP"
    RMD = "RMD"
    INT_VALUE = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"


class ActMoodPredicate(Enum):
    """
    abstDomain: A10202 (C-0-T10196-A10202-cpt)
    :cvar CRT:
    :cvar EVN_CRT:
    :cvar GOL:
    :cvar EXPEC:
    :cvar OPT:
    :cvar PERM:
    :cvar PERMRQ:
    :cvar RSK:
    """
    CRT = "CRT"
    EVN_CRT = "EVN.CRT"
    GOL = "GOL"
    EXPEC = "EXPEC"
    OPT = "OPT"
    PERM = "PERM"
    PERMRQ = "PERMRQ"
    RSK = "RSK"


class ActMoodProposal(Enum):
    """
    specDomain: S16726 (C-0-T10196-A10197-S10199-S16726-cpt)
    :cvar PRP:
    :cvar RMD:
    """
    PRP = "PRP"
    RMD = "RMD"


class ActNoImmunizationReason(Enum):
    """
    abstDomain: A19717 (C-0-T14878-A19717-cpt)
    :cvar IMMUNE:
    :cvar MEDPREC:
    :cvar OSTOCK:
    :cvar PATOBJ:
    :cvar PHILISOP:
    :cvar RELIG:
    :cvar VACEFF:
    :cvar VACSAF:
    """
    IMMUNE = "IMMUNE"
    MEDPREC = "MEDPREC"
    OSTOCK = "OSTOCK"
    PATOBJ = "PATOBJ"
    PHILISOP = "PHILISOP"
    RELIG = "RELIG"
    VACEFF = "VACEFF"
    VACSAF = "VACSAF"


class ActNonObservationIndicationCode(Enum):
    """
    abstDomain: A19778 (C-0-T13953-A19778-cpt)
    :cvar IND02:
    :cvar IND01:
    :cvar IND05:
    :cvar IND03:
    :cvar IND04:
    """
    IND02 = "IND02"
    IND01 = "IND01"
    IND05 = "IND05"
    IND03 = "IND03"
    IND04 = "IND04"


class ActObservationList(Enum):
    """
    abstDomain: A19370 (C-0-T13953-A13954-A19364-A19370-cpt)
    :cvar CONDLIST:
    :cvar INTOLIST:
    :cvar PROBLIST:
    :cvar RISKLIST:
    :cvar CARELIST:
    :cvar GOALLIST:
    """
    CONDLIST = "CONDLIST"
    INTOLIST = "INTOLIST"
    PROBLIST = "PROBLIST"
    RISKLIST = "RISKLIST"
    CARELIST = "CARELIST"
    GOALLIST = "GOALLIST"


class ActPatientTransportationModeCode(Enum):
    """
    abstDomain: A19733 (C-0-T13953-A19820-A19732-A19733-cpt)
    :cvar AMBT:
    :cvar AMBAIR:
    :cvar AMBGRND:
    :cvar AMBHELO:
    :cvar LAWENF:
    :cvar AFOOT:
    :cvar PRVTRN:
    :cvar PUBTRN:
    """
    AMBT = "AMBT"
    AMBAIR = "AMBAIR"
    AMBGRND = "AMBGRND"
    AMBHELO = "AMBHELO"
    LAWENF = "LAWENF"
    AFOOT = "AFOOT"
    PRVTRN = "PRVTRN"
    PUBTRN = "PUBTRN"


class ActPaymentCode(Enum):
    """
    abstDomain: A17610 (C-0-T13953-A13954-A17610-cpt)
    :cvar ACH:
    :cvar CHK:
    :cvar DDP:
    :cvar NON:
    """
    ACH = "ACH"
    CHK = "CHK"
    DDP = "DDP"
    NON = "NON"


class ActPharmacySupplyType(Enum):
    """
    abstDomain: A16208 (C-0-T13953-A13954-A16208-cpt)
    :cvar EM:
    :cvar SO:
    :cvar FFC:
    :cvar FFCS:
    :cvar FFS:
    :cvar TFS:
    :cvar FFPS:
    :cvar FF:
    :cvar FFP:
    :cvar TF:
    :cvar RFC:
    :cvar RFCS:
    :cvar RFF:
    :cvar RFFS:
    :cvar RFP:
    :cvar RFPS:
    :cvar TB:
    :cvar TBS:
    :cvar RF:
    :cvar DF:
    :cvar UD:
    :cvar RFS:
    :cvar FS:
    :cvar MS:
    """
    EM = "EM"
    SO = "SO"
    FFC = "FFC"
    FFCS = "FFCS"
    FFS = "FFS"
    TFS = "TFS"
    FFPS = "FFPS"
    FF = "FF"
    FFP = "FFP"
    TF = "TF"
    RFC = "RFC"
    RFCS = "RFCS"
    RFF = "RFF"
    RFFS = "RFFS"
    RFP = "RFP"
    RFPS = "RFPS"
    TB = "TB"
    TBS = "TBS"
    RF = "RF"
    DF = "DF"
    UD = "UD"
    RFS = "RFS"
    FS = "FS"
    MS = "MS"


class ActPolicyType(Enum):
    """
    abstDomain: A19886 (C-0-T13953-A13954-A19886-cpt)
    :cvar COVPOL:
    """
    COVPOL = "COVPOL"


class ActPriority(Enum):
    """
    vocSet: T16866 (C-0-T16866-cpt)
    :cvar CS:
    :cvar CSP:
    :cvar CSR:
    :cvar EL:
    :cvar EM:
    :cvar R:
    :cvar UR:
    :cvar A:
    :cvar PRN:
    :cvar CR:
    :cvar P:
    :cvar RR:
    :cvar S:
    :cvar T:
    :cvar UD:
    """
    CS = "CS"
    CSP = "CSP"
    CSR = "CSR"
    EL = "EL"
    EM = "EM"
    R = "R"
    UR = "UR"
    A = "A"
    PRN = "PRN"
    CR = "CR"
    P = "P"
    RR = "RR"
    S = "S"
    T = "T"
    UD = "UD"


class ActPriorityCallback(Enum):
    """
    specDomain: S16871 (C-0-T16866-S16871-cpt)
    :cvar CS:
    :cvar CSP:
    :cvar CSR:
    """
    CS = "CS"
    CSP = "CSP"
    CSR = "CSR"


class ActProgramTypeCode(Enum):
    """
    abstDomain: A19858 (C-0-T13953-A13954-A19855-A19858-cpt)
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    :cvar PUBLICPOL:
    :cvar DENTPRG:
    :cvar MANDPOL:
    :cvar MENTPRG:
    :cvar SAFNET:
    :cvar SUBPRG:
    :cvar CHAR:
    :cvar CRIME:
    :cvar EAP:
    :cvar GOVEMP:
    :cvar HIRISK:
    :cvar IND:
    :cvar MILITARY:
    :cvar RETIRE:
    :cvar SOCIAL:
    :cvar VET:
    :cvar WCBPOL:
    """
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"
    PUBLICPOL = "PUBLICPOL"
    DENTPRG = "DENTPRG"
    MANDPOL = "MANDPOL"
    MENTPRG = "MENTPRG"
    SAFNET = "SAFNET"
    SUBPRG = "SUBPRG"
    CHAR = "CHAR"
    CRIME = "CRIME"
    EAP = "EAP"
    GOVEMP = "GOVEMP"
    HIRISK = "HIRISK"
    IND = "IND"
    MILITARY = "MILITARY"
    RETIRE = "RETIRE"
    SOCIAL = "SOCIAL"
    VET = "VET"
    WCBPOL = "WCBPOL"


class ActRelationshipCheckpoint(Enum):
    """
    vocSet: T10349 (C-0-T10349-cpt)
    :cvar B:
    :cvar E:
    :cvar S:
    :cvar X:
    :cvar T:
    """
    B = "B"
    E = "E"
    S = "S"
    X = "X"
    T = "T"


class ActRelationshipConditional(Enum):
    """
    abstDomain: A18977 (C-0-T10317-A18977-cpt)
    :cvar MITGT:
    :cvar RCVY:
    :cvar RSON:
    :cvar BLOCK:
    :cvar CURE_ADJ:
    :cvar MTGT_ADJ:
    :cvar CURE:
    :cvar DIAG:
    :cvar SYMP:
    :cvar CIND:
    :cvar PRCN:
    :cvar TRIG:
    """
    MITGT = "MITGT"
    RCVY = "RCVY"
    RSON = "RSON"
    BLOCK = "BLOCK"
    CURE_ADJ = "CURE.ADJ"
    MTGT_ADJ = "MTGT.ADJ"
    CURE = "CURE"
    DIAG = "DIAG"
    SYMP = "SYMP"
    CIND = "CIND"
    PRCN = "PRCN"
    TRIG = "TRIG"


class ActRelationshipCostTracking(Enum):
    """
    abstDomain: A19610 (C-0-T10317-S10329-A14900-A19610-cpt)
    :cvar CHRG:
    :cvar COST:
    """
    CHRG = "CHRG"
    COST = "COST"


class ActRelationshipExcerpt(Enum):
    """
    specDomain: S18660 (C-0-T10317-S10337-S18660-cpt)
    :cvar XCRPT:
    :cvar VRXCRPT:
    """
    XCRPT = "XCRPT"
    VRXCRPT = "VRXCRPT"


class ActRelationshipFulfills(Enum):
    """
    specDomain: S10342 (C-0-T10317-S10337-S10342-cpt)
    :cvar FLFS:
    :cvar OCCR:
    :cvar OREF:
    :cvar SCH:
    """
    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"


class ActRelationshipHasComponent(Enum):
    """
    specDomain: S10318 (C-0-T10317-S10318-cpt)
    :cvar COMP:
    :cvar ARR:
    :cvar DEP:
    :cvar CTRLV:
    """
    COMP = "COMP"
    ARR = "ARR"
    DEP = "DEP"
    CTRLV = "CTRLV"


class ActRelationshipHasSupport(Enum):
    """
    specDomain: S10330 (C-0-T10317-S10329-S10330-cpt)
    :cvar SPRT:
    :cvar SPRTBND:
    """
    SPRT = "SPRT"
    SPRTBND = "SPRTBND"


class ActRelationshipJoin(Enum):
    """
    vocSet: T10360 (C-0-T10360-cpt)
    :cvar D:
    :cvar X:
    :cvar K:
    :cvar W:
    """
    D = "D"
    X = "X"
    K = "K"
    W = "W"


class ActRelationshipMitigates(Enum):
    """
    specDomain: S19986 (C-0-T10317-A18977-S10321-S19986-cpt)
    :cvar MITGT:
    :cvar RCVY:
    """
    MITGT = "MITGT"
    RCVY = "RCVY"


class ActRelationshipObjective(Enum):
    """
    abstDomain: A19617 (C-0-T10317-S10324-A19617-cpt)
    :cvar OBJC:
    :cvar OBJF:
    """
    OBJC = "OBJC"
    OBJF = "OBJF"


class ActRelationshipOutcome(Enum):
    """
    specDomain: S10324 (C-0-T10317-S10324-cpt)
    :cvar OBJC:
    :cvar OBJF:
    :cvar OUTC:
    :cvar GOAL:
    :cvar RISK:
    """
    OBJC = "OBJC"
    OBJF = "OBJF"
    OUTC = "OUTC"
    GOAL = "GOAL"
    RISK = "RISK"


class ActRelationshipPosting(Enum):
    """
    abstDomain: A19609 (C-0-T10317-S10329-A14900-A19609-cpt)
    :cvar CREDIT:
    :cvar DEBIT:
    """
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


class ActRelationshipReason(Enum):
    """
    specDomain: S10321 (C-0-T10317-A18977-S10321-cpt)
    :cvar MITGT:
    :cvar RCVY:
    :cvar RSON:
    :cvar BLOCK:
    :cvar CURE_ADJ:
    :cvar MTGT_ADJ:
    :cvar CURE:
    :cvar DIAG:
    :cvar SYMP:
    """
    MITGT = "MITGT"
    RCVY = "RCVY"
    RSON = "RSON"
    BLOCK = "BLOCK"
    CURE_ADJ = "CURE.ADJ"
    MTGT_ADJ = "MTGT.ADJ"
    CURE = "CURE"
    DIAG = "DIAG"
    SYMP = "SYMP"


class ActRelationshipSequel(Enum):
    """
    specDomain: S10337 (C-0-T10317-S10337-cpt)
    :cvar XCRPT:
    :cvar VRXCRPT:
    :cvar FLFS:
    :cvar OCCR:
    :cvar OREF:
    :cvar SCH:
    :cvar SEQL:
    :cvar DOC:
    :cvar GEVL:
    :cvar GEN:
    :cvar OPTN:
    :cvar INST:
    :cvar APND:
    :cvar MTCH:
    :cvar MOD:
    :cvar RCHAL:
    :cvar RPLC:
    :cvar REV:
    :cvar SUCC:
    :cvar XFRM:
    :cvar UPDT:
    """
    XCRPT = "XCRPT"
    VRXCRPT = "VRXCRPT"
    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"
    SEQL = "SEQL"
    DOC = "DOC"
    GEVL = "GEVL"
    GEN = "GEN"
    OPTN = "OPTN"
    INST = "INST"
    APND = "APND"
    MTCH = "MTCH"
    MOD = "MOD"
    RCHAL = "RCHAL"
    RPLC = "RPLC"
    REV = "REV"
    SUCC = "SUCC"
    XFRM = "XFRM"
    UPDT = "UPDT"


class ActRelationshipSplit(Enum):
    """
    vocSet: T10355 (C-0-T10355-cpt)
    :cvar E1:
    :cvar EW:
    :cvar I1:
    :cvar IW:
    """
    E1 = "E1"
    EW = "EW"
    I1 = "I1"
    IW = "IW"


class ActRelationshipSubset(Enum):
    """
    vocSet: T19613 (C-0-T19613-cpt)
    :cvar FUTURE:
    :cvar LAST:
    :cvar NEXT:
    :cvar FUTSUM:
    :cvar PAST:
    :cvar FIRST:
    :cvar RECENT:
    :cvar PREVSUM:
    :cvar SUM:
    :cvar MAX:
    :cvar MIN:
    """
    FUTURE = "FUTURE"
    LAST = "LAST"
    NEXT = "NEXT"
    FUTSUM = "FUTSUM"
    PAST = "PAST"
    FIRST = "FIRST"
    RECENT = "RECENT"
    PREVSUM = "PREVSUM"
    SUM = "SUM"
    MAX = "MAX"
    MIN = "MIN"


class ActRelationshipTemporallyPertains(Enum):
    """
    abstDomain: A19587 (C-0-T10317-S10329-A19587-cpt)
    :cvar SAE:
    :cvar SAS:
    """
    SAE = "SAE"
    SAS = "SAS"


class ActResearchInformationAccess(Enum):
    """
    specDomain: S22206 (C-0-T13953-A19897-S22206-cpt)
    :cvar RESEARCH:
    :cvar RSDID:
    :cvar RSREID:
    """
    RESEARCH = "RESEARCH"
    RSDID = "RSDID"
    RSREID = "RSREID"


class ActSpecObsCode(Enum):
    """
    abstDomain: A13957 (C-0-T13953-A13954-A13957-cpt)
    :cvar DILUTION:
    :cvar AUTO_HIGH:
    :cvar AUTO_LOW:
    :cvar PRE:
    :cvar RERUN:
    :cvar INTFR:
    :cvar FIBRIN:
    :cvar HEMOLYSIS:
    :cvar ICTERUS:
    :cvar LIPEMIA:
    :cvar VOLUME:
    :cvar AVAILABLE:
    :cvar CONSUMPTION:
    :cvar CURRENT:
    :cvar INITIAL:
    :cvar ARTBLD:
    :cvar EVNFCTS:
    """
    DILUTION = "DILUTION"
    AUTO_HIGH = "AUTO-HIGH"
    AUTO_LOW = "AUTO-LOW"
    PRE = "PRE"
    RERUN = "RERUN"
    INTFR = "INTFR"
    FIBRIN = "FIBRIN"
    HEMOLYSIS = "HEMOLYSIS"
    ICTERUS = "ICTERUS"
    LIPEMIA = "LIPEMIA"
    VOLUME = "VOLUME"
    AVAILABLE = "AVAILABLE"
    CONSUMPTION = "CONSUMPTION"
    CURRENT = "CURRENT"
    INITIAL = "INITIAL"
    ARTBLD = "ARTBLD"
    EVNFCTS = "EVNFCTS"


class ActSpecObsDilutionCode(Enum):
    """
    specDomain: S14352 (C-0-T13953-A13954-A13957-S14352-cpt)
    :cvar DILUTION:
    :cvar AUTO_HIGH:
    :cvar AUTO_LOW:
    :cvar PRE:
    :cvar RERUN:
    """
    DILUTION = "DILUTION"
    AUTO_HIGH = "AUTO-HIGH"
    AUTO_LOW = "AUTO-LOW"
    PRE = "PRE"
    RERUN = "RERUN"


class ActSpecObsInterferenceCode(Enum):
    """
    specDomain: S14382 (C-0-T13953-A13954-A13957-S14382-cpt)
    :cvar INTFR:
    :cvar FIBRIN:
    :cvar HEMOLYSIS:
    :cvar ICTERUS:
    :cvar LIPEMIA:
    """
    INTFR = "INTFR"
    FIBRIN = "FIBRIN"
    HEMOLYSIS = "HEMOLYSIS"
    ICTERUS = "ICTERUS"
    LIPEMIA = "LIPEMIA"


class ActSpecObsVolumeCode(Enum):
    """
    specDomain: S14369 (C-0-T13953-A13954-A13957-S14369-cpt)
    :cvar VOLUME:
    :cvar AVAILABLE:
    :cvar CONSUMPTION:
    :cvar CURRENT:
    :cvar INITIAL:
    """
    VOLUME = "VOLUME"
    AVAILABLE = "AVAILABLE"
    CONSUMPTION = "CONSUMPTION"
    CURRENT = "CURRENT"
    INITIAL = "INITIAL"


class ActSpecimenTransportCode(Enum):
    """
    abstDomain: A19663 (C-0-T13953-A19656-A19663-cpt)
    :cvar SSTOR:
    :cvar STRAN:
    :cvar SREC:
    """
    SSTOR = "SSTOR"
    STRAN = "STRAN"
    SREC = "SREC"


class ActSpecimenTreatmentCode(Enum):
    """
    abstDomain: A14040 (C-0-T13953-A13954-A14040-cpt)
    :cvar ACID:
    :cvar ALK:
    :cvar DEFB:
    :cvar FILT:
    :cvar LDLP:
    :cvar NEUT:
    :cvar RECA:
    :cvar UFIL:
    """
    ACID = "ACID"
    ALK = "ALK"
    DEFB = "DEFB"
    FILT = "FILT"
    LDLP = "LDLP"
    NEUT = "NEUT"
    RECA = "RECA"
    UFIL = "UFIL"


class ActStatus(Enum):
    """
    vocSet: T15933 (C-0-T15933-cpt)
    :cvar NORMAL:
    :cvar ABORTED:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar COMPLETED:
    :cvar HELD:
    :cvar NEW:
    :cvar SUSPENDED:
    :cvar OBSOLETE:
    :cvar NULLIFIED:
    """
    NORMAL = "normal"
    ABORTED = "aborted"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    HELD = "held"
    NEW = "new"
    SUSPENDED = "suspended"
    OBSOLETE = "obsolete"
    NULLIFIED = "nullified"


class ActStatusNormal(Enum):
    """
    specDomain: S15936 (C-0-T15933-S15936-cpt)
    :cvar NORMAL:
    :cvar ABORTED:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar COMPLETED:
    :cvar HELD:
    :cvar NEW:
    :cvar SUSPENDED:
    """
    NORMAL = "normal"
    ABORTED = "aborted"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    HELD = "held"
    NEW = "new"
    SUSPENDED = "suspended"


class ActSubstanceAdminSubstitutionCode(Enum):
    """
    abstDomain: A16621 (C-0-T13953-A13954-A16621-cpt)
    :cvar G:
    :cvar TE:
    :cvar F:
    :cvar N:
    """
    G = "G"
    TE = "TE"
    F = "F"
    N = "N"


class ActSubstanceAdministrationCode(Enum):
    """
    abstDomain: A19708 (C-0-T13953-A13954-A19708-cpt)
    :cvar IMMUNIZ:
    :cvar BOOSTER:
    :cvar INITIMMUNIZ:
    :cvar DRUG:
    """
    IMMUNIZ = "IMMUNIZ"
    BOOSTER = "BOOSTER"
    INITIMMUNIZ = "INITIMMUNIZ"
    DRUG = "DRUG"


class ActSubstanceAdministrationImmunizationCode(Enum):
    """
    specDomain: S21519 (C-0-T13953-A13954-A19708-S21519-cpt)
    :cvar IMMUNIZ:
    :cvar BOOSTER:
    :cvar INITIMMUNIZ:
    """
    IMMUNIZ = "IMMUNIZ"
    BOOSTER = "BOOSTER"
    INITIMMUNIZ = "INITIMMUNIZ"


class ActSupplyFulfillmentRefusalReason(Enum):
    """
    abstDomain: A19718 (C-0-T14878-A19718-cpt)
    :cvar FRR05:
    :cvar FRR03:
    :cvar FRR01:
    :cvar FRR04:
    :cvar FRR02:
    :cvar FRR06:
    """
    FRR05 = "FRR05"
    FRR03 = "FRR03"
    FRR01 = "FRR01"
    FRR04 = "FRR04"
    FRR02 = "FRR02"
    FRR06 = "FRR06"


class ActTaskClinicalNoteEntryCode(Enum):
    """
    specDomain: S22068 (C-0-T13953-A19846-S22067-S22068-cpt)
    :cvar CLINNOTEE:
    :cvar DIAGLISTE:
    :cvar DISCHSUME:
    :cvar PATREPE:
    :cvar PROBLISTE:
    :cvar RADREPE:
    """
    CLINNOTEE = "CLINNOTEE"
    DIAGLISTE = "DIAGLISTE"
    DISCHSUME = "DISCHSUME"
    PATREPE = "PATREPE"
    PROBLISTE = "PROBLISTE"
    RADREPE = "RADREPE"


class ActTaskClinicalNoteReviewCode(Enum):
    """
    specDomain: S22065 (C-0-T13953-A19846-S22051-S22065-cpt)
    :cvar CLINNOTEREV:
    :cvar DISCHSUMREV:
    """
    CLINNOTEREV = "CLINNOTEREV"
    DISCHSUMREV = "DISCHSUMREV"


class ActTaskMedicationListReviewCode(Enum):
    """
    specDomain: S22053 (C-0-T13953-A19846-S22051-S22053-cpt)
    :cvar MLREV:
    :cvar MARWLREV:
    """
    MLREV = "MLREV"
    MARWLREV = "MARWLREV"


class ActTaskMicrobiologyResultsReviewCode(Enum):
    """
    specDomain: S22056 (C-0-T13953-A19846-S22051-S22056-cpt)
    :cvar MICRORREV:
    :cvar MICROORGRREV:
    :cvar MICROSENSRREV:
    """
    MICRORREV = "MICRORREV"
    MICROORGRREV = "MICROORGRREV"
    MICROSENSRREV = "MICROSENSRREV"


class ActTaskOrderEntryCode(Enum):
    """
    specDomain: S22048 (C-0-T13953-A19846-S22048-cpt)
    :cvar OE:
    :cvar LABOE:
    :cvar MEDOE:
    """
    OE = "OE"
    LABOE = "LABOE"
    MEDOE = "MEDOE"


class ActTaskPatientDocumentationCode(Enum):
    """
    specDomain: S22067 (C-0-T13953-A19846-S22067-cpt)
    :cvar CLINNOTEE:
    :cvar DIAGLISTE:
    :cvar DISCHSUME:
    :cvar PATREPE:
    :cvar PROBLISTE:
    :cvar RADREPE:
    :cvar PATDOC:
    """
    CLINNOTEE = "CLINNOTEE"
    DIAGLISTE = "DIAGLISTE"
    DISCHSUME = "DISCHSUME"
    PATREPE = "PATREPE"
    PROBLISTE = "PROBLISTE"
    RADREPE = "RADREPE"
    PATDOC = "PATDOC"


class ActTaskPatientInformationReviewCode(Enum):
    """
    specDomain: S22051 (C-0-T13953-A19846-S22051-cpt)
    :cvar CLINNOTEREV:
    :cvar DISCHSUMREV:
    :cvar MLREV:
    :cvar MARWLREV:
    :cvar MICRORREV:
    :cvar MICROORGRREV:
    :cvar MICROSENSRREV:
    :cvar RISKASSESS:
    :cvar FALLRISK:
    :cvar PATINFO:
    :cvar DIAGLISTREV:
    :cvar LABRREV:
    :cvar OREV:
    :cvar PATREPREV:
    :cvar PROBLISTREV:
    :cvar RADREPREV:
    """
    CLINNOTEREV = "CLINNOTEREV"
    DISCHSUMREV = "DISCHSUMREV"
    MLREV = "MLREV"
    MARWLREV = "MARWLREV"
    MICRORREV = "MICRORREV"
    MICROORGRREV = "MICROORGRREV"
    MICROSENSRREV = "MICROSENSRREV"
    RISKASSESS = "RISKASSESS"
    FALLRISK = "FALLRISK"
    PATINFO = "PATINFO"
    DIAGLISTREV = "DIAGLISTREV"
    LABRREV = "LABRREV"
    OREV = "OREV"
    PATREPREV = "PATREPREV"
    PROBLISTREV = "PROBLISTREV"
    RADREPREV = "RADREPREV"


class ActTaskRiskAssessmentInstrumentCode(Enum):
    """
    specDomain: S22063 (C-0-T13953-A19846-S22051-S22063-cpt)
    :cvar RISKASSESS:
    :cvar FALLRISK:
    """
    RISKASSESS = "RISKASSESS"
    FALLRISK = "FALLRISK"


class ActUncertainty(Enum):
    """
    vocSet: T16899 (C-0-T16899-cpt)
    :cvar N:
    :cvar U:
    """
    N = "N"
    U = "U"


class ActiveEditStatus(Enum):
    """
    specDomain: S11042 (C-0-T11040-S11042-cpt)
    :cvar A:
    """
    A = "A"


class AdditionalLocator(Enum):
    """
    specDomain: S10651 (C-0-T10642-S10651-cpt)
    :cvar ADL:
    :cvar UNIT:
    :cvar UNID:
    """
    ADL = "ADL"
    UNIT = "UNIT"
    UNID = "UNID"


class AddressPartType(Enum):
    """
    vocSet: T10642 (C-0-T10642-cpt)
    :cvar ADL:
    :cvar UNIT:
    :cvar UNID:
    :cvar DAL:
    :cvar DINSTA:
    :cvar DINSTQ:
    :cvar DINST:
    :cvar DMOD:
    :cvar DMODID:
    :cvar BNS:
    :cvar POB:
    :cvar BNR:
    :cvar BNN:
    :cvar STR_VALUE:
    :cvar STB:
    :cvar STTYP:
    :cvar SAL:
    :cvar DIR:
    :cvar CAR:
    :cvar CEN:
    :cvar CNT:
    :cvar CPA:
    :cvar DEL_VALUE:
    :cvar CTY:
    :cvar ZIP:
    :cvar PRE:
    :cvar STA:
    """
    ADL = "ADL"
    UNIT = "UNIT"
    UNID = "UNID"
    DAL = "DAL"
    DINSTA = "DINSTA"
    DINSTQ = "DINSTQ"
    DINST = "DINST"
    DMOD = "DMOD"
    DMODID = "DMODID"
    BNS = "BNS"
    POB = "POB"
    BNR = "BNR"
    BNN = "BNN"
    STR_VALUE = "STR"
    STB = "STB"
    STTYP = "STTYP"
    SAL = "SAL"
    DIR = "DIR"
    CAR = "CAR"
    CEN = "CEN"
    CNT = "CNT"
    CPA = "CPA"
    DEL_VALUE = "DEL"
    CTY = "CTY"
    ZIP = "ZIP"
    PRE = "PRE"
    STA = "STA"


class AddressUse(Enum):
    """
    abstDomain: A190 (C-0-T201-A190-cpt)
    :cvar H:
    :cvar HP:
    :cvar HV:
    :cvar WP:
    :cvar DIR:
    :cvar PUB:
    :cvar BAD:
    :cvar TMP:
    """
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"


class AdjudicatedWithAdjustments(Enum):
    """
    specDomain: S19347 (C-0-T13953-A13954-A17616-S19347-cpt)
    :cvar AA:
    :cvar ANF:
    """
    AA = "AA"
    ANF = "ANF"


class AdministrableDrugForm(Enum):
    """
    abstDomain: A14570 (C-0-T19651-A14411-A14570-cpt)
    :cvar DROP:
    :cvar NDROP:
    :cvar OPDROP:
    :cvar ORDROP:
    :cvar OTDROP:
    :cvar APPFUL:
    :cvar PUFF:
    :cvar SCOOP:
    :cvar SPRY:
    """
    DROP = "DROP"
    NDROP = "NDROP"
    OPDROP = "OPDROP"
    ORDROP = "ORDROP"
    OTDROP = "OTDROP"
    APPFUL = "APPFUL"
    PUFF = "PUFF"
    SCOOP = "SCOOP"
    SPRY = "SPRY"


class AdministrationDetectedIssueCodeDuplicateTherapyAlertByBot(Enum):
    """
    specDomain: S16688 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16688-cpt)
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    """
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"


class AdministrationMedicalDevice(Enum):
    """
    abstDomain: A16189 (C-0-T16040-A16041-A19867-A16188-A16189-cpt)
    :cvar INH:
    :cvar DSKUNH:
    :cvar DSKS:
    :cvar TRBINH:
    :cvar AINJ:
    :cvar PEN:
    :cvar SYR:
    :cvar APLCTR:
    :cvar PMP:
    """
    INH = "INH"
    DSKUNH = "DSKUNH"
    DSKS = "DSKS"
    TRBINH = "TRBINH"
    AINJ = "AINJ"
    PEN = "PEN"
    SYR = "SYR"
    APLCTR = "APLCTR"
    PMP = "PMP"


class AdministrativeContactRoleType(Enum):
    """
    abstDomain: A17622 (C-0-T12206-A15920-A17622-cpt)
    :cvar BILL:
    :cvar PAYOR:
    :cvar ORG:
    """
    BILL = "BILL"
    PAYOR = "PAYOR"
    ORG = "ORG"


class AdministrativeGender(Enum):
    """
    vocSet: T1 (C-0-T1-cpt)
    :cvar F:
    :cvar M:
    :cvar UN:
    """
    F = "F"
    M = "M"
    UN = "UN"


class AdoptedChild(Enum):
    """
    specDomain: S11564 (C-0-T12206-A19563-S17926-S16360-S11564-cpt)
    :cvar CHLDADOPT:
    :cvar DAUADOPT:
    :cvar SONADOPT:
    """
    CHLDADOPT = "CHLDADOPT"
    DAUADOPT = "DAUADOPT"
    SONADOPT = "SONADOPT"


class AerosolDrugForm(Enum):
    """
    specDomain: S14551 (C-0-T19651-A14411-A14412-A14545-S14551-cpt)
    :cvar AER:
    :cvar BAINHL:
    :cvar INHLSOL:
    :cvar MDINHL:
    :cvar NASSPRY:
    """
    AER = "AER"
    BAINHL = "BAINHL"
    INHLSOL = "INHLSOL"
    MDINHL = "MDINHL"
    NASSPRY = "NASSPRY"


class AgeDetectedIssueCode(Enum):
    """
    specDomain: S16669 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16669-cpt)
    :cvar AGE:
    :cvar DOSEHINDA:
    :cvar DOSELINDA:
    """
    AGE = "AGE"
    DOSEHINDA = "DOSEHINDA"
    DOSELINDA = "DOSELINDA"


class AgenciesProviderCodes(Enum):
    """
    specDomain: S20669 (C-0-T19465-S20669-cpt)
    :cvar VALUE_250000000_X:
    :cvar VALUE_251_B00000_X:
    :cvar VALUE_251_C00000_X:
    :cvar VALUE_251_E00000_X:
    :cvar VALUE_251_F00000_X:
    :cvar VALUE_251_G00000_X:
    :cvar VALUE_251_J00000_X:
    :cvar VALUE_251_K00000_X:
    :cvar VALUE_251_V00000_X:
    """
    VALUE_250000000_X = "250000000X"
    VALUE_251_B00000_X = "251B00000X"
    VALUE_251_C00000_X = "251C00000X"
    VALUE_251_E00000_X = "251E00000X"
    VALUE_251_F00000_X = "251F00000X"
    VALUE_251_G00000_X = "251G00000X"
    VALUE_251_J00000_X = "251J00000X"
    VALUE_251_K00000_X = "251K00000X"
    VALUE_251_V00000_X = "251V00000X"


class Aleut(Enum):
    """
    abstDomain: A18221 (C-0-T18130-A18191-A18221-cpt)
    :cvar X_ALW:
    """
    X_ALW = "x-ALW"


class AlgorithmicDecisionObservationMethod(Enum):
    """
    specDomain: S19992 (C-0-T14079-A19378-S19992-cpt)
    :cvar ALGM:
    :cvar BYCL:
    """
    ALGM = "ALGM"
    BYCL = "BYCL"


class AllergyandImmunologyProviderCodes(Enum):
    """
    specDomain: S20097 (C-0-T19465-S20096-S20097-cpt)
    :cvar VALUE_207_K00000_X:
    :cvar VALUE_207_KA0200_X:
    :cvar VALUE_207_KI0005_X:
    """
    VALUE_207_K00000_X = "207K00000X"
    VALUE_207_KA0200_X = "207KA0200X"
    VALUE_207_KI0005_X = "207KI0005X"


class AllopathicandOsteopathicPhysiciansProviderCodes(Enum):
    """
    specDomain: S20096 (C-0-T19465-S20096-cpt)
    :cvar VALUE_207_K00000_X:
    :cvar VALUE_207_KA0200_X:
    :cvar VALUE_207_KI0005_X:
    :cvar VALUE_207_L00000_X:
    :cvar VALUE_207_LA0401_X:
    :cvar VALUE_207_LC0200_X:
    :cvar VALUE_207_LP2900_X:
    :cvar VALUE_207_N00000_X:
    :cvar VALUE_207_NI0002_X:
    :cvar VALUE_207_NS0135_X:
    :cvar VALUE_207_ND0900_X:
    :cvar VALUE_207_ND0101_X:
    :cvar VALUE_207_NP0225_X:
    :cvar VALUE_207_P00000_X:
    :cvar VALUE_207_PE0004_X:
    :cvar VALUE_207_PT0002_X:
    :cvar VALUE_207_PP0204_X:
    :cvar VALUE_207_PS0010_X:
    :cvar VALUE_207_PE0005_X:
    :cvar VALUE_207_Q00000_X:
    :cvar VALUE_207_QA0401_X:
    :cvar VALUE_207_QA0000_X:
    :cvar VALUE_207_QA0505_X:
    :cvar VALUE_207_QG0300_X:
    :cvar VALUE_207_QS0010_X:
    :cvar VALUE_207_R00000_X:
    :cvar VALUE_207_RA0401_X:
    :cvar VALUE_207_RA0000_X:
    :cvar VALUE_207_RA0201_X:
    :cvar VALUE_207_RC0000_X:
    :cvar VALUE_207_RI0001_X:
    :cvar VALUE_207_RC0001_X:
    :cvar VALUE_207_RC0200_X:
    :cvar VALUE_207_RE0101_X:
    :cvar VALUE_207_RG0100_X:
    :cvar VALUE_207_RG0300_X:
    :cvar VALUE_207_RH0000_X:
    :cvar VALUE_207_RH0003_X:
    :cvar VALUE_207_RI0008_X:
    :cvar VALUE_207_RI0200_X:
    :cvar VALUE_207_RI0011_X:
    :cvar VALUE_207_RM1200_X:
    :cvar VALUE_207_RX0202_X:
    :cvar VALUE_207_RN0300_X:
    :cvar VALUE_207_RP1001_X:
    :cvar VALUE_207_RR0500_X:
    :cvar VALUE_207_RS0010_X:
    :cvar VALUE_207_S00000_X:
    :cvar VALUE_207_SG0202_X:
    :cvar VALUE_207_SC0300_X:
    :cvar VALUE_207_SG0201_X:
    :cvar VALUE_207_SG0203_X:
    :cvar VALUE_207_SM0001_X:
    :cvar VALUE_207_SG0205_X:
    :cvar VALUE_207_U00000_X:
    :cvar VALUE_207_UN0903_X:
    :cvar VALUE_207_UN0901_X:
    :cvar VALUE_207_UN0902_X:
    :cvar VALUE_207_V00000_X:
    :cvar VALUE_207_VC0200_X:
    :cvar VALUE_207_VX0201_X:
    :cvar VALUE_207_VG0400_X:
    :cvar VALUE_207_VM0101_X:
    :cvar VALUE_207_VX0000_X:
    :cvar VALUE_207_VE0102_X:
    :cvar VALUE_207_X00000_X:
    :cvar VALUE_207_XS0114_X:
    :cvar VALUE_207_XX0004_X:
    :cvar VALUE_207_XS0106_X:
    :cvar VALUE_207_XS0117_X:
    :cvar VALUE_207_XX0801_X:
    :cvar VALUE_207_XX0005_X:
    :cvar VALUE_207_Y00000_X:
    :cvar VALUE_207_YS0123_X:
    :cvar VALUE_207_YX0602_X:
    :cvar VALUE_207_YX0905_X:
    :cvar VALUE_207_YX0901_X:
    :cvar VALUE_207_YP0228_X:
    :cvar VALUE_207_YX0007_X:
    :cvar VALUE_208_V00000_X:
    :cvar VALUE_208_VP0014_X:
    :cvar VALUE_208_VP0000_X:
    :cvar VALUE_207_Z00000_X:
    :cvar VALUE_207_ZP0101_X:
    :cvar VALUE_207_ZP0102_X:
    :cvar VALUE_207_ZB0001_X:
    :cvar VALUE_207_ZP0104_X:
    :cvar VALUE_207_ZP0105_X:
    :cvar VALUE_207_ZC0500_X:
    :cvar VALUE_207_ZD0900_X:
    :cvar VALUE_207_ZF0201_X:
    :cvar VALUE_207_ZH0000_X:
    :cvar VALUE_207_ZI0100_X:
    :cvar VALUE_207_ZM0300_X:
    :cvar VALUE_207_ZP0007_X:
    :cvar VALUE_207_ZN0500_X:
    :cvar VALUE_207_ZP0213_X:
    :cvar VALUE_208000000_X:
    :cvar VALUE_2080_A0000_X:
    :cvar VALUE_2080_I0007_X:
    :cvar VALUE_2080_P0006_X:
    :cvar VALUE_2080_T0002_X:
    :cvar VALUE_2080_N0001_X:
    :cvar VALUE_2080_P0008_X:
    :cvar VALUE_2080_P0201_X:
    :cvar VALUE_2080_P0202_X:
    :cvar VALUE_2080_P0203_X:
    :cvar VALUE_2080_P0204_X:
    :cvar VALUE_2080_P0205_X:
    :cvar VALUE_2080_P0206_X:
    :cvar VALUE_2080_P0207_X:
    :cvar VALUE_2080_P0208_X:
    :cvar VALUE_2080_P0210_X:
    :cvar VALUE_2080_P0214_X:
    :cvar VALUE_2080_P0216_X:
    :cvar VALUE_2080_S0010_X:
    :cvar VALUE_208100000_X:
    :cvar VALUE_2081_P2900_X:
    :cvar VALUE_2081_P0010_X:
    :cvar VALUE_2081_P0004_X:
    :cvar VALUE_2081_S0010_X:
    :cvar VALUE_208200000_X:
    :cvar VALUE_2082_S0099_X:
    :cvar VALUE_2082_S0105_X:
    :cvar VALUE_208300000_X:
    :cvar VALUE_2083_A0100_X:
    :cvar VALUE_2083_T0002_X:
    :cvar VALUE_2083_X0100_X:
    :cvar VALUE_2083_P0500_X:
    :cvar VALUE_2083_P0901_X:
    :cvar VALUE_2083_S0010_X:
    :cvar VALUE_2083_P0011_X:
    :cvar VALUE_208400000_X:
    :cvar VALUE_2084_A0401_X:
    :cvar VALUE_2084_P0802_X:
    :cvar VALUE_2084_P0804_X:
    :cvar VALUE_2084_N0600_X:
    :cvar VALUE_2084_F0202_X:
    :cvar VALUE_2084_P0805_X:
    :cvar VALUE_2084_P0005_X:
    :cvar VALUE_2084_N0400_X:
    :cvar VALUE_2084_N0402_X:
    :cvar VALUE_2084_P2900_X:
    :cvar VALUE_2084_P0800_X:
    :cvar VALUE_2084_S0010_X:
    :cvar VALUE_2084_V0102_X:
    :cvar VALUE_208500000_X:
    :cvar VALUE_2085_B0100_X:
    :cvar VALUE_2085_R0202_X:
    :cvar VALUE_2085_U0001_X:
    :cvar VALUE_2085_N0700_X:
    :cvar VALUE_2085_N0904_X:
    :cvar VALUE_2085_P0229_X:
    :cvar VALUE_2085_R0001_X:
    :cvar VALUE_2085_R0205_X:
    :cvar VALUE_2085_R0203_X:
    :cvar VALUE_2085_R0204_X:
    :cvar VALUE_208600000_X:
    :cvar VALUE_2086_S0120_X:
    :cvar VALUE_2086_S0122_X:
    :cvar VALUE_2086_S0105_X:
    :cvar VALUE_2086_S0102_X:
    :cvar VALUE_2086_X0206_X:
    :cvar VALUE_208_G00000_X:
    :cvar VALUE_204_F00000_X:
    :cvar VALUE_2086_S0127_X:
    :cvar VALUE_2086_S0129_X:
    :cvar VALUE_200000000_X:
    :cvar VALUE_208_U00000_X:
    :cvar VALUE_208_C00000_X:
    :cvar VALUE_208_D00000_X:
    :cvar VALUE_208_M00000_X:
    :cvar VALUE_209800000_X:
    :cvar VALUE_207_T00000_X:
    :cvar VALUE_204_D00000_X:
    :cvar VALUE_204_C00000_X:
    :cvar VALUE_207_W00000_X:
    :cvar VALUE_204_E00000_X:
    :cvar VALUE_208800000_X:
    """
    VALUE_207_K00000_X = "207K00000X"
    VALUE_207_KA0200_X = "207KA0200X"
    VALUE_207_KI0005_X = "207KI0005X"
    VALUE_207_L00000_X = "207L00000X"
    VALUE_207_LA0401_X = "207LA0401X"
    VALUE_207_LC0200_X = "207LC0200X"
    VALUE_207_LP2900_X = "207LP2900X"
    VALUE_207_N00000_X = "207N00000X"
    VALUE_207_NI0002_X = "207NI0002X"
    VALUE_207_NS0135_X = "207NS0135X"
    VALUE_207_ND0900_X = "207ND0900X"
    VALUE_207_ND0101_X = "207ND0101X"
    VALUE_207_NP0225_X = "207NP0225X"
    VALUE_207_P00000_X = "207P00000X"
    VALUE_207_PE0004_X = "207PE0004X"
    VALUE_207_PT0002_X = "207PT0002X"
    VALUE_207_PP0204_X = "207PP0204X"
    VALUE_207_PS0010_X = "207PS0010X"
    VALUE_207_PE0005_X = "207PE0005X"
    VALUE_207_Q00000_X = "207Q00000X"
    VALUE_207_QA0401_X = "207QA0401X"
    VALUE_207_QA0000_X = "207QA0000X"
    VALUE_207_QA0505_X = "207QA0505X"
    VALUE_207_QG0300_X = "207QG0300X"
    VALUE_207_QS0010_X = "207QS0010X"
    VALUE_207_R00000_X = "207R00000X"
    VALUE_207_RA0401_X = "207RA0401X"
    VALUE_207_RA0000_X = "207RA0000X"
    VALUE_207_RA0201_X = "207RA0201X"
    VALUE_207_RC0000_X = "207RC0000X"
    VALUE_207_RI0001_X = "207RI0001X"
    VALUE_207_RC0001_X = "207RC0001X"
    VALUE_207_RC0200_X = "207RC0200X"
    VALUE_207_RE0101_X = "207RE0101X"
    VALUE_207_RG0100_X = "207RG0100X"
    VALUE_207_RG0300_X = "207RG0300X"
    VALUE_207_RH0000_X = "207RH0000X"
    VALUE_207_RH0003_X = "207RH0003X"
    VALUE_207_RI0008_X = "207RI0008X"
    VALUE_207_RI0200_X = "207RI0200X"
    VALUE_207_RI0011_X = "207RI0011X"
    VALUE_207_RM1200_X = "207RM1200X"
    VALUE_207_RX0202_X = "207RX0202X"
    VALUE_207_RN0300_X = "207RN0300X"
    VALUE_207_RP1001_X = "207RP1001X"
    VALUE_207_RR0500_X = "207RR0500X"
    VALUE_207_RS0010_X = "207RS0010X"
    VALUE_207_S00000_X = "207S00000X"
    VALUE_207_SG0202_X = "207SG0202X"
    VALUE_207_SC0300_X = "207SC0300X"
    VALUE_207_SG0201_X = "207SG0201X"
    VALUE_207_SG0203_X = "207SG0203X"
    VALUE_207_SM0001_X = "207SM0001X"
    VALUE_207_SG0205_X = "207SG0205X"
    VALUE_207_U00000_X = "207U00000X"
    VALUE_207_UN0903_X = "207UN0903X"
    VALUE_207_UN0901_X = "207UN0901X"
    VALUE_207_UN0902_X = "207UN0902X"
    VALUE_207_V00000_X = "207V00000X"
    VALUE_207_VC0200_X = "207VC0200X"
    VALUE_207_VX0201_X = "207VX0201X"
    VALUE_207_VG0400_X = "207VG0400X"
    VALUE_207_VM0101_X = "207VM0101X"
    VALUE_207_VX0000_X = "207VX0000X"
    VALUE_207_VE0102_X = "207VE0102X"
    VALUE_207_X00000_X = "207X00000X"
    VALUE_207_XS0114_X = "207XS0114X"
    VALUE_207_XX0004_X = "207XX0004X"
    VALUE_207_XS0106_X = "207XS0106X"
    VALUE_207_XS0117_X = "207XS0117X"
    VALUE_207_XX0801_X = "207XX0801X"
    VALUE_207_XX0005_X = "207XX0005X"
    VALUE_207_Y00000_X = "207Y00000X"
    VALUE_207_YS0123_X = "207YS0123X"
    VALUE_207_YX0602_X = "207YX0602X"
    VALUE_207_YX0905_X = "207YX0905X"
    VALUE_207_YX0901_X = "207YX0901X"
    VALUE_207_YP0228_X = "207YP0228X"
    VALUE_207_YX0007_X = "207YX0007X"
    VALUE_208_V00000_X = "208V00000X"
    VALUE_208_VP0014_X = "208VP0014X"
    VALUE_208_VP0000_X = "208VP0000X"
    VALUE_207_Z00000_X = "207Z00000X"
    VALUE_207_ZP0101_X = "207ZP0101X"
    VALUE_207_ZP0102_X = "207ZP0102X"
    VALUE_207_ZB0001_X = "207ZB0001X"
    VALUE_207_ZP0104_X = "207ZP0104X"
    VALUE_207_ZP0105_X = "207ZP0105X"
    VALUE_207_ZC0500_X = "207ZC0500X"
    VALUE_207_ZD0900_X = "207ZD0900X"
    VALUE_207_ZF0201_X = "207ZF0201X"
    VALUE_207_ZH0000_X = "207ZH0000X"
    VALUE_207_ZI0100_X = "207ZI0100X"
    VALUE_207_ZM0300_X = "207ZM0300X"
    VALUE_207_ZP0007_X = "207ZP0007X"
    VALUE_207_ZN0500_X = "207ZN0500X"
    VALUE_207_ZP0213_X = "207ZP0213X"
    VALUE_208000000_X = "208000000X"
    VALUE_2080_A0000_X = "2080A0000X"
    VALUE_2080_I0007_X = "2080I0007X"
    VALUE_2080_P0006_X = "2080P0006X"
    VALUE_2080_T0002_X = "2080T0002X"
    VALUE_2080_N0001_X = "2080N0001X"
    VALUE_2080_P0008_X = "2080P0008X"
    VALUE_2080_P0201_X = "2080P0201X"
    VALUE_2080_P0202_X = "2080P0202X"
    VALUE_2080_P0203_X = "2080P0203X"
    VALUE_2080_P0204_X = "2080P0204X"
    VALUE_2080_P0205_X = "2080P0205X"
    VALUE_2080_P0206_X = "2080P0206X"
    VALUE_2080_P0207_X = "2080P0207X"
    VALUE_2080_P0208_X = "2080P0208X"
    VALUE_2080_P0210_X = "2080P0210X"
    VALUE_2080_P0214_X = "2080P0214X"
    VALUE_2080_P0216_X = "2080P0216X"
    VALUE_2080_S0010_X = "2080S0010X"
    VALUE_208100000_X = "208100000X"
    VALUE_2081_P2900_X = "2081P2900X"
    VALUE_2081_P0010_X = "2081P0010X"
    VALUE_2081_P0004_X = "2081P0004X"
    VALUE_2081_S0010_X = "2081S0010X"
    VALUE_208200000_X = "208200000X"
    VALUE_2082_S0099_X = "2082S0099X"
    VALUE_2082_S0105_X = "2082S0105X"
    VALUE_208300000_X = "208300000X"
    VALUE_2083_A0100_X = "2083A0100X"
    VALUE_2083_T0002_X = "2083T0002X"
    VALUE_2083_X0100_X = "2083X0100X"
    VALUE_2083_P0500_X = "2083P0500X"
    VALUE_2083_P0901_X = "2083P0901X"
    VALUE_2083_S0010_X = "2083S0010X"
    VALUE_2083_P0011_X = "2083P0011X"
    VALUE_208400000_X = "208400000X"
    VALUE_2084_A0401_X = "2084A0401X"
    VALUE_2084_P0802_X = "2084P0802X"
    VALUE_2084_P0804_X = "2084P0804X"
    VALUE_2084_N0600_X = "2084N0600X"
    VALUE_2084_F0202_X = "2084F0202X"
    VALUE_2084_P0805_X = "2084P0805X"
    VALUE_2084_P0005_X = "2084P0005X"
    VALUE_2084_N0400_X = "2084N0400X"
    VALUE_2084_N0402_X = "2084N0402X"
    VALUE_2084_P2900_X = "2084P2900X"
    VALUE_2084_P0800_X = "2084P0800X"
    VALUE_2084_S0010_X = "2084S0010X"
    VALUE_2084_V0102_X = "2084V0102X"
    VALUE_208500000_X = "208500000X"
    VALUE_2085_B0100_X = "2085B0100X"
    VALUE_2085_R0202_X = "2085R0202X"
    VALUE_2085_U0001_X = "2085U0001X"
    VALUE_2085_N0700_X = "2085N0700X"
    VALUE_2085_N0904_X = "2085N0904X"
    VALUE_2085_P0229_X = "2085P0229X"
    VALUE_2085_R0001_X = "2085R0001X"
    VALUE_2085_R0205_X = "2085R0205X"
    VALUE_2085_R0203_X = "2085R0203X"
    VALUE_2085_R0204_X = "2085R0204X"
    VALUE_208600000_X = "208600000X"
    VALUE_2086_S0120_X = "2086S0120X"
    VALUE_2086_S0122_X = "2086S0122X"
    VALUE_2086_S0105_X = "2086S0105X"
    VALUE_2086_S0102_X = "2086S0102X"
    VALUE_2086_X0206_X = "2086X0206X"
    VALUE_208_G00000_X = "208G00000X"
    VALUE_204_F00000_X = "204F00000X"
    VALUE_2086_S0127_X = "2086S0127X"
    VALUE_2086_S0129_X = "2086S0129X"
    VALUE_200000000_X = "200000000X"
    VALUE_208_U00000_X = "208U00000X"
    VALUE_208_C00000_X = "208C00000X"
    VALUE_208_D00000_X = "208D00000X"
    VALUE_208_M00000_X = "208M00000X"
    VALUE_209800000_X = "209800000X"
    VALUE_207_T00000_X = "207T00000X"
    VALUE_204_D00000_X = "204D00000X"
    VALUE_204_C00000_X = "204C00000X"
    VALUE_207_W00000_X = "207W00000X"
    VALUE_204_E00000_X = "204E00000X"
    VALUE_208800000_X = "208800000X"


class Ambulance(Enum):
    """
    specDomain: S21547 (C-0-T13953-A19820-A19732-A19733-S21547-cpt)
    :cvar AMBT:
    :cvar AMBAIR:
    :cvar AMBGRND:
    :cvar AMBHELO:
    """
    AMBT = "AMBT"
    AMBAIR = "AMBAIR"
    AMBGRND = "AMBGRND"
    AMBHELO = "AMBHELO"


class AmbulanceHipaa(Enum):
    """
    abstDomain: A13850 (C-0-T13129-A13715-A13849-A13850-cpt)
    :cvar VALUE_3416_A0800_N:
    :cvar VALUE_3416_L0300_N:
    :cvar VALUE_3416_S0300_N:
    """
    VALUE_3416_A0800_N = "3416A0800N"
    VALUE_3416_L0300_N = "3416L0300N"
    VALUE_3416_S0300_N = "3416S0300N"


class AmbulanceProviderCodes(Enum):
    """
    specDomain: S20789 (C-0-T19465-S20788-S20789-cpt)
    :cvar VALUE_341600000_X:
    :cvar VALUE_3416_A0800_X:
    :cvar VALUE_3416_L0300_X:
    :cvar VALUE_3416_S0300_X:
    """
    VALUE_341600000_X = "341600000X"
    VALUE_3416_A0800_X = "3416A0800X"
    VALUE_3416_L0300_X = "3416L0300X"
    VALUE_3416_S0300_X = "3416S0300X"


class AmbulatoryClinicOrCenterHipaa(Enum):
    """
    abstDomain: A13726 (C-0-T13129-A13715-A13725-A13726-cpt)
    :cvar CARD:
    :cvar PEDCARD:
    :cvar RADDX:
    :cvar RNEU:
    :cvar VALUE_261_QX0203_N:
    :cvar RADO:
    :cvar VALUE_261_QA0600_N:
    :cvar VALUE_261_QA1903_N:
    :cvar VALUE_261_QB0400_N:
    :cvar VALUE_261_QC1500_N:
    :cvar VALUE_261_QC1800_N:
    :cvar VALUE_261_QD0000_N:
    :cvar VALUE_261_QE0002_N:
    :cvar VALUE_261_QE0700_N:
    :cvar VALUE_261_QF0400_N:
    :cvar VALUE_261_QH0100_N:
    :cvar VALUE_261_QI0500_N:
    :cvar VALUE_261_QL0400_N:
    :cvar VALUE_261_QM1200_N:
    :cvar VALUE_261_QM0801_N:
    :cvar VALUE_261_QM1000_N:
    :cvar VALUE_261_QM1100_N:
    :cvar VALUE_261_QM1101_N:
    :cvar VALUE_261_QM1102_N:
    :cvar VALUE_261_QM1300_N:
    :cvar VALUE_261_QX0100_N:
    :cvar VALUE_261_QP2000_N:
    :cvar VALUE_261_QP2400_N:
    :cvar VALUE_261_QP0904_N:
    :cvar VALUE_261_QP0905_N:
    :cvar VALUE_261_QR0206_N:
    :cvar VALUE_261_QR0208_N:
    :cvar VALUE_261_QR0207_N:
    :cvar VALUE_261_QR0800_N:
    :cvar VALUE_261_QR0400_N:
    :cvar VALUE_261_QR0401_N:
    :cvar VALUE_261_QR0405_N:
    :cvar VALUE_261_QR1100_N:
    :cvar VALUE_261_QR1300_N:
    :cvar VALUE_261_QS1200_N:
    :cvar VALUE_261_QS1000_N:
    :cvar VALUE_261_QS0132_N:
    :cvar VALUE_261_QU0200_N:
    :cvar VALUE_261_QV0200_N:
    :cvar ENDOS:
    :cvar OMS:
    :cvar PAINCL:
    :cvar POD:
    :cvar PC:
    """
    CARD = "CARD"
    PEDCARD = "PEDCARD"
    RADDX = "RADDX"
    RNEU = "RNEU"
    VALUE_261_QX0203_N = "261QX0203N"
    RADO = "RADO"
    VALUE_261_QA0600_N = "261QA0600N"
    VALUE_261_QA1903_N = "261QA1903N"
    VALUE_261_QB0400_N = "261QB0400N"
    VALUE_261_QC1500_N = "261QC1500N"
    VALUE_261_QC1800_N = "261QC1800N"
    VALUE_261_QD0000_N = "261QD0000N"
    VALUE_261_QE0002_N = "261QE0002N"
    VALUE_261_QE0700_N = "261QE0700N"
    VALUE_261_QF0400_N = "261QF0400N"
    VALUE_261_QH0100_N = "261QH0100N"
    VALUE_261_QI0500_N = "261QI0500N"
    VALUE_261_QL0400_N = "261QL0400N"
    VALUE_261_QM1200_N = "261QM1200N"
    VALUE_261_QM0801_N = "261QM0801N"
    VALUE_261_QM1000_N = "261QM1000N"
    VALUE_261_QM1100_N = "261QM1100N"
    VALUE_261_QM1101_N = "261QM1101N"
    VALUE_261_QM1102_N = "261QM1102N"
    VALUE_261_QM1300_N = "261QM1300N"
    VALUE_261_QX0100_N = "261QX0100N"
    VALUE_261_QP2000_N = "261QP2000N"
    VALUE_261_QP2400_N = "261QP2400N"
    VALUE_261_QP0904_N = "261QP0904N"
    VALUE_261_QP0905_N = "261QP0905N"
    VALUE_261_QR0206_N = "261QR0206N"
    VALUE_261_QR0208_N = "261QR0208N"
    VALUE_261_QR0207_N = "261QR0207N"
    VALUE_261_QR0800_N = "261QR0800N"
    VALUE_261_QR0400_N = "261QR0400N"
    VALUE_261_QR0401_N = "261QR0401N"
    VALUE_261_QR0405_N = "261QR0405N"
    VALUE_261_QR1100_N = "261QR1100N"
    VALUE_261_QR1300_N = "261QR1300N"
    VALUE_261_QS1200_N = "261QS1200N"
    VALUE_261_QS1000_N = "261QS1000N"
    VALUE_261_QS0132_N = "261QS0132N"
    VALUE_261_QU0200_N = "261QU0200N"
    VALUE_261_QV0200_N = "261QV0200N"
    ENDOS = "ENDOS"
    OMS = "OMS"
    PAINCL = "PAINCL"
    POD = "POD"
    PC = "PC"


class AmbulatoryHealthCareFacilitiesProviderCodes(Enum):
    """
    specDomain: S20678 (C-0-T19465-S20678-cpt)
    :cvar VALUE_261_Q00000_X:
    :cvar VALUE_261_QM0855_X:
    :cvar VALUE_261_QA0600_X:
    :cvar VALUE_261_QM0850_X:
    :cvar VALUE_261_QA0005_X:
    :cvar VALUE_261_QA0006_X:
    :cvar VALUE_261_QA1903_X:
    :cvar VALUE_261_QA0900_X:
    :cvar VALUE_261_QA3000_X:
    :cvar VALUE_261_QB0400_X:
    :cvar VALUE_261_QC1500_X:
    :cvar VALUE_261_QC1800_X:
    :cvar VALUE_261_QC0050_X:
    :cvar VALUE_261_QD0000_X:
    :cvar VALUE_261_QD1600_X:
    :cvar VALUE_261_QE0002_X:
    :cvar VALUE_261_QE0700_X:
    :cvar VALUE_261_QE0800_X:
    :cvar VALUE_261_QF0050_X:
    :cvar VALUE_261_QF0400_X:
    :cvar VALUE_261_QG0250_X:
    :cvar VALUE_261_QH0100_X:
    :cvar VALUE_261_QH0700_X:
    :cvar VALUE_261_QI0500_X:
    :cvar VALUE_261_QL0400_X:
    :cvar VALUE_261_QM1200_X:
    :cvar VALUE_261_QR0206_X:
    :cvar VALUE_261_QM2500_X:
    :cvar VALUE_261_QM3000_X:
    :cvar VALUE_261_QM0801_X:
    :cvar VALUE_261_QM2800_X:
    :cvar VALUE_261_QM1000_X:
    :cvar VALUE_261_QM1100_X:
    :cvar VALUE_261_QM1101_X:
    :cvar VALUE_261_QM1102_X:
    :cvar VALUE_261_QR0208_X:
    :cvar VALUE_261_QR0207_X:
    :cvar VALUE_261_QM1300_X:
    :cvar VALUE_261_QX0100_X:
    :cvar VALUE_261_QX0200_X:
    :cvar VALUE_261_QX0203_X:
    :cvar VALUE_261_QS0132_X:
    :cvar VALUE_261_QS0112_X:
    :cvar VALUE_261_QP3300_X:
    :cvar VALUE_261_QP2000_X:
    :cvar VALUE_261_QP1100_X:
    :cvar VALUE_261_QP2300_X:
    :cvar VALUE_261_QP2400_X:
    :cvar VALUE_261_QP0904_X:
    :cvar VALUE_261_QP0905_X:
    :cvar VALUE_261_QR0200_X:
    :cvar VALUE_261_QR0800_X:
    :cvar VALUE_261_QR0400_X:
    :cvar VALUE_261_QR0401_X:
    :cvar VALUE_261_QR0405_X:
    :cvar VALUE_261_QR0404_X:
    :cvar VALUE_261_QR1100_X:
    :cvar VALUE_261_QR1300_X:
    :cvar VALUE_261_QS1200_X:
    :cvar VALUE_261_QS1000_X:
    :cvar VALUE_261_QU0200_X:
    :cvar VALUE_261_QV0200_X:
    :cvar VALUE_260000000_X:
    """
    VALUE_261_Q00000_X = "261Q00000X"
    VALUE_261_QM0855_X = "261QM0855X"
    VALUE_261_QA0600_X = "261QA0600X"
    VALUE_261_QM0850_X = "261QM0850X"
    VALUE_261_QA0005_X = "261QA0005X"
    VALUE_261_QA0006_X = "261QA0006X"
    VALUE_261_QA1903_X = "261QA1903X"
    VALUE_261_QA0900_X = "261QA0900X"
    VALUE_261_QA3000_X = "261QA3000X"
    VALUE_261_QB0400_X = "261QB0400X"
    VALUE_261_QC1500_X = "261QC1500X"
    VALUE_261_QC1800_X = "261QC1800X"
    VALUE_261_QC0050_X = "261QC0050X"
    VALUE_261_QD0000_X = "261QD0000X"
    VALUE_261_QD1600_X = "261QD1600X"
    VALUE_261_QE0002_X = "261QE0002X"
    VALUE_261_QE0700_X = "261QE0700X"
    VALUE_261_QE0800_X = "261QE0800X"
    VALUE_261_QF0050_X = "261QF0050X"
    VALUE_261_QF0400_X = "261QF0400X"
    VALUE_261_QG0250_X = "261QG0250X"
    VALUE_261_QH0100_X = "261QH0100X"
    VALUE_261_QH0700_X = "261QH0700X"
    VALUE_261_QI0500_X = "261QI0500X"
    VALUE_261_QL0400_X = "261QL0400X"
    VALUE_261_QM1200_X = "261QM1200X"
    VALUE_261_QR0206_X = "261QR0206X"
    VALUE_261_QM2500_X = "261QM2500X"
    VALUE_261_QM3000_X = "261QM3000X"
    VALUE_261_QM0801_X = "261QM0801X"
    VALUE_261_QM2800_X = "261QM2800X"
    VALUE_261_QM1000_X = "261QM1000X"
    VALUE_261_QM1100_X = "261QM1100X"
    VALUE_261_QM1101_X = "261QM1101X"
    VALUE_261_QM1102_X = "261QM1102X"
    VALUE_261_QR0208_X = "261QR0208X"
    VALUE_261_QR0207_X = "261QR0207X"
    VALUE_261_QM1300_X = "261QM1300X"
    VALUE_261_QX0100_X = "261QX0100X"
    VALUE_261_QX0200_X = "261QX0200X"
    VALUE_261_QX0203_X = "261QX0203X"
    VALUE_261_QS0132_X = "261QS0132X"
    VALUE_261_QS0112_X = "261QS0112X"
    VALUE_261_QP3300_X = "261QP3300X"
    VALUE_261_QP2000_X = "261QP2000X"
    VALUE_261_QP1100_X = "261QP1100X"
    VALUE_261_QP2300_X = "261QP2300X"
    VALUE_261_QP2400_X = "261QP2400X"
    VALUE_261_QP0904_X = "261QP0904X"
    VALUE_261_QP0905_X = "261QP0905X"
    VALUE_261_QR0200_X = "261QR0200X"
    VALUE_261_QR0800_X = "261QR0800X"
    VALUE_261_QR0400_X = "261QR0400X"
    VALUE_261_QR0401_X = "261QR0401X"
    VALUE_261_QR0405_X = "261QR0405X"
    VALUE_261_QR0404_X = "261QR0404X"
    VALUE_261_QR1100_X = "261QR1100X"
    VALUE_261_QR1300_X = "261QR1300X"
    VALUE_261_QS1200_X = "261QS1200X"
    VALUE_261_QS1000_X = "261QS1000X"
    VALUE_261_QU0200_X = "261QU0200X"
    VALUE_261_QV0200_X = "261QV0200X"
    VALUE_260000000_X = "260000000X"


class AmnioticFluidSacRoute(Enum):
    """
    abstDomain: A17022 (C-0-T14581-A17021-A17022-cpt)
    :cvar AMNINJ:
    """
    AMNINJ = "AMNINJ"


class AnesthesiologyProviderCodes(Enum):
    """
    specDomain: S20100 (C-0-T19465-S20096-S20100-cpt)
    :cvar VALUE_207_L00000_X:
    :cvar VALUE_207_LA0401_X:
    :cvar VALUE_207_LC0200_X:
    :cvar VALUE_207_LP2900_X:
    """
    VALUE_207_L00000_X = "207L00000X"
    VALUE_207_LA0401_X = "207LA0401X"
    VALUE_207_LC0200_X = "207LC0200X"
    VALUE_207_LP2900_X = "207LP2900X"


class Apachean(Enum):
    """
    abstDomain: A18399 (C-0-T18130-A18352-A18356-A18358-A18399-cpt)
    :cvar X_APJ:
    :cvar X_APL:
    :cvar X_NAV:
    :cvar X_APM:
    :cvar X_APW:
    :cvar X_APK:
    """
    X_APJ = "x-APJ"
    X_APL = "x-APL"
    X_NAV = "x-NAV"
    X_APM = "x-APM"
    X_APW = "x-APW"
    X_APK = "x-APK"


class ApplicationMediaType(Enum):
    """
    abstDomain: A14832 (C-0-T14824-A14832-cpt)
    :cvar APPLICATION_DICOM:
    :cvar APPLICATION_MSWORD:
    :cvar APPLICATION_PDF:
    """
    APPLICATION_DICOM = "application/dicom"
    APPLICATION_MSWORD = "application/msword"
    APPLICATION_PDF = "application/pdf"


class ArapahoGrosVentre(Enum):
    """
    abstDomain: A18143 (C-0-T18130-A18131-A18132-A18142-A18143-cpt)
    :cvar X_ARP:
    :cvar X_ATS:
    """
    X_ARP = "x-ARP"
    X_ATS = "x-ATS"


class ArtificialDentition(Enum):
    """
    abstDomain: A19345 (C-0-T16537-A16538-A19346-A19345-cpt)
    :cvar TID10A:
    :cvar TID10I:
    :cvar TID10P:
    :cvar TID10PD:
    :cvar TID10PM:
    :cvar TID11A:
    :cvar TID11I:
    :cvar TID11P:
    :cvar TID11PD:
    :cvar TID11PM:
    :cvar TID12A:
    :cvar TID12I:
    :cvar TID12P:
    :cvar TID12PD:
    :cvar TID12PM:
    :cvar TID13A:
    :cvar TID13I:
    :cvar TID13P:
    :cvar TID13PD:
    :cvar TID13PM:
    :cvar TID14A:
    :cvar TID14I:
    :cvar TID14P:
    :cvar TID14PD:
    :cvar TID14PM:
    :cvar TID15A:
    :cvar TID15I:
    :cvar TID15P:
    :cvar TID15PD:
    :cvar TID15PM:
    :cvar TID16A:
    :cvar TID16I:
    :cvar TID16P:
    :cvar TID16PD:
    :cvar TID16PM:
    :cvar TID17A:
    :cvar TID17AD:
    :cvar TID17AM:
    :cvar TID17I:
    :cvar TID17ID:
    :cvar TID17IM:
    :cvar TID17P:
    :cvar TID17PD:
    :cvar TID17PM:
    :cvar TID18A:
    :cvar TID18AD:
    :cvar TID18AM:
    :cvar TID18I:
    :cvar TID18ID:
    :cvar TID18IM:
    :cvar TID18P:
    :cvar TID18PD:
    :cvar TID18PM:
    :cvar TID19A:
    :cvar TID19AD:
    :cvar TID19AM:
    :cvar TID19I:
    :cvar TID19ID:
    :cvar TID19IM:
    :cvar TID19P:
    :cvar TID19PD:
    :cvar TID19PM:
    :cvar TID1A:
    :cvar TID1I:
    :cvar TID1P:
    :cvar TID1PD:
    :cvar TID1PM:
    :cvar TID20A:
    :cvar TID20I:
    :cvar TID20P:
    :cvar TID20PD:
    :cvar TID20PM:
    :cvar TID21A:
    :cvar TID21I:
    :cvar TID21P:
    :cvar TID21PD:
    :cvar TID21PM:
    :cvar TID22A:
    :cvar TID22I:
    :cvar TID22P:
    :cvar TID22PD:
    :cvar TID22PM:
    :cvar TID23A:
    :cvar TID23I:
    :cvar TID23P:
    :cvar TID23PD:
    :cvar TID23PM:
    :cvar TID24A:
    :cvar TID24I:
    :cvar TID24P:
    :cvar TID24PD:
    :cvar TID24PM:
    :cvar TID25A:
    :cvar TID25I:
    :cvar TID25P:
    :cvar TID25PD:
    :cvar TID25PM:
    :cvar TID26A:
    :cvar TID26I:
    :cvar TID26P:
    :cvar TID26PD:
    :cvar TID26PM:
    :cvar TID27A:
    :cvar TID27I:
    :cvar TID27P:
    :cvar TID27PD:
    :cvar TID27PM:
    :cvar TID28A:
    :cvar TID28I:
    :cvar TID28P:
    :cvar TID28PD:
    :cvar TID28PM:
    :cvar TID29A:
    :cvar TID29I:
    :cvar TID29P:
    :cvar TID29PD:
    :cvar TID29PM:
    :cvar TID2A:
    :cvar TID2I:
    :cvar TID2P:
    :cvar TID2PD:
    :cvar TID2PM:
    :cvar TID30A:
    :cvar TID30AD:
    :cvar TID30AM:
    :cvar TID30I:
    :cvar TID30ID:
    :cvar TID30IM:
    :cvar TID30P:
    :cvar TID30PD:
    :cvar TID30PM:
    :cvar TID31A:
    :cvar TID31AD:
    :cvar TID31AM:
    :cvar TID31I:
    :cvar TID31ID:
    :cvar TID31IM:
    :cvar TID31P:
    :cvar TID31PD:
    :cvar TID31PM:
    :cvar TID32A:
    :cvar TID32AD:
    :cvar TID32AM:
    :cvar TID32I:
    :cvar TID32ID:
    :cvar TID32IM:
    :cvar TID32P:
    :cvar TID32PD:
    :cvar TID32PM:
    :cvar TID3A:
    :cvar TID3I:
    :cvar TID3P:
    :cvar TID3PD:
    :cvar TID3PM:
    :cvar TID4A:
    :cvar TID4I:
    :cvar TID4P:
    :cvar TID4PD:
    :cvar TID4PM:
    :cvar TID5A:
    :cvar TID5I:
    :cvar TID5P:
    :cvar TID5PD:
    :cvar TID5PM:
    :cvar TID6A:
    :cvar TID6I:
    :cvar TID6P:
    :cvar TID6PD:
    :cvar TID6PM:
    :cvar TID7A:
    :cvar TID7I:
    :cvar TID7P:
    :cvar TID7PD:
    :cvar TID7PM:
    :cvar TID8A:
    :cvar TID8I:
    :cvar TID8P:
    :cvar TID8PD:
    :cvar TID8PM:
    :cvar TID9A:
    :cvar TID9I:
    :cvar TID9P:
    :cvar TID9PD:
    :cvar TID9PM:
    """
    TID10A = "TID10a"
    TID10I = "TID10i"
    TID10P = "TID10p"
    TID10PD = "TID10pd"
    TID10PM = "TID10pm"
    TID11A = "TID11a"
    TID11I = "TID11i"
    TID11P = "TID11p"
    TID11PD = "TID11pd"
    TID11PM = "TID11pm"
    TID12A = "TID12a"
    TID12I = "TID12i"
    TID12P = "TID12p"
    TID12PD = "TID12pd"
    TID12PM = "TID12pm"
    TID13A = "TID13a"
    TID13I = "TID13i"
    TID13P = "TID13p"
    TID13PD = "TID13pd"
    TID13PM = "TID13pm"
    TID14A = "TID14a"
    TID14I = "TID14i"
    TID14P = "TID14p"
    TID14PD = "TID14pd"
    TID14PM = "TID14pm"
    TID15A = "TID15a"
    TID15I = "TID15i"
    TID15P = "TID15p"
    TID15PD = "TID15pd"
    TID15PM = "TID15pm"
    TID16A = "TID16a"
    TID16I = "TID16i"
    TID16P = "TID16p"
    TID16PD = "TID16pd"
    TID16PM = "TID16pm"
    TID17A = "TID17a"
    TID17AD = "TID17ad"
    TID17AM = "TID17am"
    TID17I = "TID17i"
    TID17ID = "TID17id"
    TID17IM = "TID17im"
    TID17P = "TID17p"
    TID17PD = "TID17pd"
    TID17PM = "TID17pm"
    TID18A = "TID18a"
    TID18AD = "TID18ad"
    TID18AM = "TID18am"
    TID18I = "TID18i"
    TID18ID = "TID18id"
    TID18IM = "TID18im"
    TID18P = "TID18p"
    TID18PD = "TID18pd"
    TID18PM = "TID18pm"
    TID19A = "TID19a"
    TID19AD = "TID19ad"
    TID19AM = "TID19am"
    TID19I = "TID19i"
    TID19ID = "TID19id"
    TID19IM = "TID19im"
    TID19P = "TID19p"
    TID19PD = "TID19pd"
    TID19PM = "TID19pm"
    TID1A = "TID1a"
    TID1I = "TID1i"
    TID1P = "TID1p"
    TID1PD = "TID1pd"
    TID1PM = "TID1pm"
    TID20A = "TID20a"
    TID20I = "TID20i"
    TID20P = "TID20p"
    TID20PD = "TID20pd"
    TID20PM = "TID20pm"
    TID21A = "TID21a"
    TID21I = "TID21i"
    TID21P = "TID21p"
    TID21PD = "TID21pd"
    TID21PM = "TID21pm"
    TID22A = "TID22a"
    TID22I = "TID22i"
    TID22P = "TID22p"
    TID22PD = "TID22pd"
    TID22PM = "TID22pm"
    TID23A = "TID23a"
    TID23I = "TID23i"
    TID23P = "TID23p"
    TID23PD = "TID23pd"
    TID23PM = "TID23pm"
    TID24A = "TID24a"
    TID24I = "TID24i"
    TID24P = "TID24p"
    TID24PD = "TID24pd"
    TID24PM = "TID24pm"
    TID25A = "TID25a"
    TID25I = "TID25i"
    TID25P = "TID25p"
    TID25PD = "TID25pd"
    TID25PM = "TID25pm"
    TID26A = "TID26a"
    TID26I = "TID26i"
    TID26P = "TID26p"
    TID26PD = "TID26pd"
    TID26PM = "TID26pm"
    TID27A = "TID27a"
    TID27I = "TID27i"
    TID27P = "TID27p"
    TID27PD = "TID27pd"
    TID27PM = "TID27pm"
    TID28A = "TID28a"
    TID28I = "TID28i"
    TID28P = "TID28p"
    TID28PD = "TID28pd"
    TID28PM = "TID28pm"
    TID29A = "TID29a"
    TID29I = "TID29i"
    TID29P = "TID29p"
    TID29PD = "TID29pd"
    TID29PM = "TID29pm"
    TID2A = "TID2a"
    TID2I = "TID2i"
    TID2P = "TID2p"
    TID2PD = "TID2pd"
    TID2PM = "TID2pm"
    TID30A = "TID30a"
    TID30AD = "TID30ad"
    TID30AM = "TID30am"
    TID30I = "TID30i"
    TID30ID = "TID30id"
    TID30IM = "TID30im"
    TID30P = "TID30p"
    TID30PD = "TID30pd"
    TID30PM = "TID30pm"
    TID31A = "TID31a"
    TID31AD = "TID31ad"
    TID31AM = "TID31am"
    TID31I = "TID31i"
    TID31ID = "TID31id"
    TID31IM = "TID31im"
    TID31P = "TID31p"
    TID31PD = "TID31pd"
    TID31PM = "TID31pm"
    TID32A = "TID32a"
    TID32AD = "TID32ad"
    TID32AM = "TID32am"
    TID32I = "TID32i"
    TID32ID = "TID32id"
    TID32IM = "TID32im"
    TID32P = "TID32p"
    TID32PD = "TID32pd"
    TID32PM = "TID32pm"
    TID3A = "TID3a"
    TID3I = "TID3i"
    TID3P = "TID3p"
    TID3PD = "TID3pd"
    TID3PM = "TID3pm"
    TID4A = "TID4a"
    TID4I = "TID4i"
    TID4P = "TID4p"
    TID4PD = "TID4pd"
    TID4PM = "TID4pm"
    TID5A = "TID5a"
    TID5I = "TID5i"
    TID5P = "TID5p"
    TID5PD = "TID5pd"
    TID5PM = "TID5pm"
    TID6A = "TID6a"
    TID6I = "TID6i"
    TID6P = "TID6p"
    TID6PD = "TID6pd"
    TID6PM = "TID6pm"
    TID7A = "TID7a"
    TID7I = "TID7i"
    TID7P = "TID7p"
    TID7PD = "TID7pd"
    TID7PM = "TID7pm"
    TID8A = "TID8a"
    TID8I = "TID8i"
    TID8P = "TID8p"
    TID8PD = "TID8pd"
    TID8PM = "TID8pm"
    TID9A = "TID9a"
    TID9I = "TID9i"
    TID9P = "TID9p"
    TID9PD = "TID9pd"
    TID9PM = "TID9pm"


class AskedButUnknown(Enum):
    """
    specDomain: S10614 (C-0-T10609-S10610-S10612-S10614-cpt)
    :cvar ASKU:
    :cvar NAV:
    """
    ASKU = "ASKU"
    NAV = "NAV"


class AssignedNonPersonLivingSubjectRoleType(Enum):
    """
    abstDomain: A19869 (C-0-T12206-A19679-A19869-cpt)
    :cvar BIOTH:
    :cvar ANTIBIOT:
    :cvar DEBR:
    :cvar ASSIST:
    :cvar CCO:
    :cvar SEE:
    :cvar SNIFF:
    """
    BIOTH = "BIOTH"
    ANTIBIOT = "ANTIBIOT"
    DEBR = "DEBR"
    ASSIST = "ASSIST"
    CCO = "CCO"
    SEE = "SEE"
    SNIFF = "SNIFF"


class AssistedLivingFacilityProviderCodes(Enum):
    """
    specDomain: S20820 (C-0-T19465-S20758-S20820-cpt)
    :cvar VALUE_310400000_X:
    :cvar VALUE_3104_A0630_X:
    :cvar VALUE_3104_A0625_X:
    """
    VALUE_310400000_X = "310400000X"
    VALUE_3104_A0630_X = "3104A0630X"
    VALUE_3104_A0625_X = "3104A0625X"


class AudioMediaType(Enum):
    """
    abstDomain: A14835 (C-0-T14824-A14835-cpt)
    :cvar AUDIO_BASIC:
    :cvar AUDIO_K32ADPCM:
    :cvar AUDIO_MPEG:
    """
    AUDIO_BASIC = "audio/basic"
    AUDIO_K32ADPCM = "audio/k32adpcm"
    AUDIO_MPEG = "audio/mpeg"


class AudiologistProviderCodes(Enum):
    """
    specDomain: S20599 (C-0-T19465-S20598-S20599-cpt)
    :cvar VALUE_231_H00000_X:
    :cvar VALUE_231_HA2400_X:
    :cvar VALUE_231_HA2500_X:
    """
    VALUE_231_H00000_X = "231H00000X"
    VALUE_231_HA2400_X = "231HA2400X"
    VALUE_231_HA2500_X = "231HA2500X"


class AuthorizationIssueManagementCode(Enum):
    """
    abstDomain: A19619 (C-0-T13953-A13954-A16695-A19431-A19619-cpt)
    :cvar EMAUTH:
    """
    EMAUTH = "EMAUTH"


class AutomobileInsurancePolicy(Enum):
    """
    specDomain: S19721 (C-0-T13953-A13954-A19855-A19856-S19721-cpt)
    :cvar AUTOPOL:
    :cvar COL:
    :cvar UNINSMOT:
    """
    AUTOPOL = "AUTOPOL"
    COL = "COL"
    UNINSMOT = "UNINSMOT"


class BarDrugForm(Enum):
    """
    specDomain: S14485 (C-0-T19651-A14411-A14412-A14484-S14485-cpt)
    :cvar BARSOAP:
    :cvar MEDBAR:
    :cvar BAR:
    :cvar CHEWBAR:
    """
    BARSOAP = "BARSOAP"
    MEDBAR = "MEDBAR"
    BAR = "BAR"
    CHEWBAR = "CHEWBAR"


class BarSoapDrugForm(Enum):
    """
    specDomain: S14486 (C-0-T19651-A14411-A14412-A14484-S14485-S14486-cpt)
    :cvar BARSOAP:
    :cvar MEDBAR:
    """
    BARSOAP = "BARSOAP"
    MEDBAR = "MEDBAR"


class BehavioralHealthAndOrSocialServiceCounselorHipaa(Enum):
    """
    specDomain: S13132 (C-0-T13129-A13130-A13131-S13132-cpt)
    :cvar VALUE_101_Y00000_N:
    :cvar VALUE_101_YA0400_N:
    :cvar VALUE_101_YM0800_N:
    :cvar VALUE_101_YP1600_N:
    :cvar VALUE_101_YP2500_N:
    :cvar VALUE_101_YS0200_N:
    """
    VALUE_101_Y00000_N = "101Y00000N"
    VALUE_101_YA0400_N = "101YA0400N"
    VALUE_101_YM0800_N = "101YM0800N"
    VALUE_101_YP1600_N = "101YP1600N"
    VALUE_101_YP2500_N = "101YP2500N"
    VALUE_101_YS0200_N = "101YS0200N"


class BehavioralHealthAndOrSocialServiceProviderHipaa(Enum):
    """
    abstDomain: A13131 (C-0-T13129-A13130-A13131-cpt)
    :cvar VALUE_101_Y00000_N:
    :cvar VALUE_101_YA0400_N:
    :cvar VALUE_101_YM0800_N:
    :cvar VALUE_101_YP1600_N:
    :cvar VALUE_101_YP2500_N:
    :cvar VALUE_101_YS0200_N:
    :cvar VALUE_103_GC0700_N:
    :cvar VALUE_103_S00000_N:
    :cvar VALUE_103_SA1800_N:
    :cvar VALUE_103_SA1400_N:
    :cvar VALUE_103_T00000_N:
    :cvar VALUE_103_TA0400_N:
    :cvar VALUE_103_TA0700_N:
    :cvar VALUE_103_TB0200_N:
    :cvar VALUE_103_TC2200_N:
    :cvar VALUE_103_TC0700_N:
    :cvar VALUE_103_TC1900_N:
    :cvar VALUE_103_TE1000_N:
    :cvar VALUE_103_TE1100_N:
    :cvar VALUE_103_TF0000_N:
    :cvar VALUE_103_TF0200_N:
    :cvar VALUE_103_TH0100_N:
    :cvar VALUE_103_TM1700_N:
    :cvar VALUE_103_TM1800_N:
    :cvar VALUE_103_TP2700_N:
    :cvar VALUE_103_TP2701_N:
    :cvar VALUE_103_TR0400_N:
    :cvar VALUE_103_TS0200_N:
    :cvar VALUE_103_TW0100_N:
    :cvar VALUE_104100000_N:
    :cvar VALUE_1041_C0700_N:
    :cvar VALUE_1041_S0200_N:
    :cvar VALUE_106_H00000_N:
    :cvar VALUE_225_CA2500_N:
    """
    VALUE_101_Y00000_N = "101Y00000N"
    VALUE_101_YA0400_N = "101YA0400N"
    VALUE_101_YM0800_N = "101YM0800N"
    VALUE_101_YP1600_N = "101YP1600N"
    VALUE_101_YP2500_N = "101YP2500N"
    VALUE_101_YS0200_N = "101YS0200N"
    VALUE_103_GC0700_N = "103GC0700N"
    VALUE_103_S00000_N = "103S00000N"
    VALUE_103_SA1800_N = "103SA1800N"
    VALUE_103_SA1400_N = "103SA1400N"
    VALUE_103_T00000_N = "103T00000N"
    VALUE_103_TA0400_N = "103TA0400N"
    VALUE_103_TA0700_N = "103TA0700N"
    VALUE_103_TB0200_N = "103TB0200N"
    VALUE_103_TC2200_N = "103TC2200N"
    VALUE_103_TC0700_N = "103TC0700N"
    VALUE_103_TC1900_N = "103TC1900N"
    VALUE_103_TE1000_N = "103TE1000N"
    VALUE_103_TE1100_N = "103TE1100N"
    VALUE_103_TF0000_N = "103TF0000N"
    VALUE_103_TF0200_N = "103TF0200N"
    VALUE_103_TH0100_N = "103TH0100N"
    VALUE_103_TM1700_N = "103TM1700N"
    VALUE_103_TM1800_N = "103TM1800N"
    VALUE_103_TP2700_N = "103TP2700N"
    VALUE_103_TP2701_N = "103TP2701N"
    VALUE_103_TR0400_N = "103TR0400N"
    VALUE_103_TS0200_N = "103TS0200N"
    VALUE_103_TW0100_N = "103TW0100N"
    VALUE_104100000_N = "104100000N"
    VALUE_1041_C0700_N = "1041C0700N"
    VALUE_1041_S0200_N = "1041S0200N"
    VALUE_106_H00000_N = "106H00000N"
    VALUE_225_CA2500_N = "225CA2500N"


class BehavioralHealthandSocialServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20275 (C-0-T19465-S20275-cpt)
    :cvar VALUE_101_Y00000_X:
    :cvar VALUE_101_YA0400_X:
    :cvar VALUE_101_YM0800_X:
    :cvar VALUE_101_YP1600_X:
    :cvar VALUE_101_YP2500_X:
    :cvar VALUE_101_YS0200_X:
    :cvar VALUE_103_G00000_X:
    :cvar VALUE_103_GC0700_X:
    :cvar VALUE_103_T00000_X:
    :cvar VALUE_103_TA0400_X:
    :cvar VALUE_103_TA0700_X:
    :cvar VALUE_103_TB0200_X:
    :cvar VALUE_103_TC2200_X:
    :cvar VALUE_103_TC0700_X:
    :cvar VALUE_103_TC1900_X:
    :cvar VALUE_103_TE1000_X:
    :cvar VALUE_103_TE1100_X:
    :cvar VALUE_103_TF0000_X:
    :cvar VALUE_103_TF0200_X:
    :cvar VALUE_103_TH0100_X:
    :cvar VALUE_103_TM1700_X:
    :cvar VALUE_103_TM1800_X:
    :cvar VALUE_103_TP0814_X:
    :cvar VALUE_103_TP2700_X:
    :cvar VALUE_103_TP2701_X:
    :cvar VALUE_103_TR0400_X:
    :cvar VALUE_103_TS0200_X:
    :cvar VALUE_103_TW0100_X:
    :cvar VALUE_104100000_X:
    :cvar VALUE_1041_C0700_X:
    :cvar VALUE_1041_S0200_X:
    :cvar VALUE_100000000_X:
    :cvar VALUE_106_H00000_X:
    """
    VALUE_101_Y00000_X = "101Y00000X"
    VALUE_101_YA0400_X = "101YA0400X"
    VALUE_101_YM0800_X = "101YM0800X"
    VALUE_101_YP1600_X = "101YP1600X"
    VALUE_101_YP2500_X = "101YP2500X"
    VALUE_101_YS0200_X = "101YS0200X"
    VALUE_103_G00000_X = "103G00000X"
    VALUE_103_GC0700_X = "103GC0700X"
    VALUE_103_T00000_X = "103T00000X"
    VALUE_103_TA0400_X = "103TA0400X"
    VALUE_103_TA0700_X = "103TA0700X"
    VALUE_103_TB0200_X = "103TB0200X"
    VALUE_103_TC2200_X = "103TC2200X"
    VALUE_103_TC0700_X = "103TC0700X"
    VALUE_103_TC1900_X = "103TC1900X"
    VALUE_103_TE1000_X = "103TE1000X"
    VALUE_103_TE1100_X = "103TE1100X"
    VALUE_103_TF0000_X = "103TF0000X"
    VALUE_103_TF0200_X = "103TF0200X"
    VALUE_103_TH0100_X = "103TH0100X"
    VALUE_103_TM1700_X = "103TM1700X"
    VALUE_103_TM1800_X = "103TM1800X"
    VALUE_103_TP0814_X = "103TP0814X"
    VALUE_103_TP2700_X = "103TP2700X"
    VALUE_103_TP2701_X = "103TP2701X"
    VALUE_103_TR0400_X = "103TR0400X"
    VALUE_103_TS0200_X = "103TS0200X"
    VALUE_103_TW0100_X = "103TW0100X"
    VALUE_104100000_X = "104100000X"
    VALUE_1041_C0700_X = "1041C0700X"
    VALUE_1041_S0200_X = "1041S0200X"
    VALUE_100000000_X = "100000000X"
    VALUE_106_H00000_X = "106H00000X"


class BiliaryRoute(Enum):
    """
    abstDomain: A17024 (C-0-T14581-A17021-A17024-cpt)
    :cvar BILINJ:
    :cvar CHOLINJ:
    """
    BILINJ = "BILINJ"
    CHOLINJ = "CHOLINJ"


class BiotherapeuticNonPersonLivingSubjectRoleType(Enum):
    """
    specDomain: S22157 (C-0-T12206-A19679-A19869-S22157-cpt)
    :cvar BIOTH:
    :cvar ANTIBIOT:
    :cvar DEBR:
    """
    BIOTH = "BIOTH"
    ANTIBIOT = "ANTIBIOT"
    DEBR = "DEBR"


class BlisterPackEntityType(Enum):
    """
    specDomain: S16171 (C-0-T16040-A16041-A19867-A16143-S16144-A16152-S16171-cpt)
    :cvar BLSTRPK:
    :cvar CARD:
    """
    BLSTRPK = "BLSTRPK"
    CARD = "CARD"


class BodySurfaceRoute(Enum):
    """
    abstDomain: A17027 (C-0-T14581-A17021-A17027-cpt)
    :cvar ELECTOSMOS:
    :cvar SOAK:
    :cvar TOPICAL:
    :cvar IONTO:
    :cvar DRESS:
    :cvar SWAB:
    """
    ELECTOSMOS = "ELECTOSMOS"
    SOAK = "SOAK"
    TOPICAL = "TOPICAL"
    IONTO = "IONTO"
    DRESS = "DRESS"
    SWAB = "SWAB"


class BottleEntityType(Enum):
    """
    specDomain: S16155 (C-0-T16040-A16041-A19867-A16143-S16144-A16152-A16153-S16155-cpt)
    :cvar BOTP:
    :cvar BOTPLY:
    :cvar BOT:
    :cvar BOTA:
    :cvar BOTD:
    :cvar BOTG:
    """
    BOTP = "BOTP"
    BOTPLY = "BOTPLY"
    BOT = "BOT"
    BOTA = "BOTA"
    BOTD = "BOTD"
    BOTG = "BOTG"


class BuccalMucosaRoute(Enum):
    """
    abstDomain: A17034 (C-0-T14581-A17021-A17034-cpt)
    :cvar BUC:
    """
    BUC = "BUC"


class BuccalTablet(Enum):
    """
    specDomain: S14518 (C-0-T19651-A14411-A14412-A14484-S14506-S14515-S14516-S14518-cpt)
    :cvar BUCTAB:
    :cvar SRBUCTAB:
    """
    BUCTAB = "BUCTAB"
    SRBUCTAB = "SRBUCTAB"


class BuildingNumber(Enum):
    """
    specDomain: S10649 (C-0-T10642-S14822-S10649-cpt)
    :cvar BNS:
    :cvar POB:
    :cvar BNR:
    :cvar BNN:
    """
    BNS = "BNS"
    POB = "POB"
    BNR = "BNR"
    BNN = "BNN"


class BuildingNumberSuffixByBot(Enum):
    """
    specDomain: S17882 (C-0-T10642-S14822-S10649-S17882-cpt)
    :cvar BNS:
    :cvar POB:
    """
    BNS = "BNS"
    POB = "POB"


class CvdiagTherPracticeSetting(Enum):
    """
    specDomain: S10903 (C-0-T12206-A17660-A19450-A10588-S10902-S10903-cpt)
    :cvar CVDX:
    :cvar CATH:
    :cvar ECHO:
    """
    CVDX = "CVDX"
    CATH = "CATH"
    ECHO = "ECHO"


class Cahitan(Enum):
    """
    abstDomain: A18637 (C-0-T18130-A18605-A18636-A18637-cpt)
    :cvar X_YAQ:
    """
    X_YAQ = "x-YAQ"


class Calendar(Enum):
    """
    vocSet: T17422 (C-0-T17422-cpt)
    :cvar GREG:
    """
    GREG = "GREG"


class CalendarCycleOneLetter(Enum):
    """
    abstDomain: A10701 (C-0-T10684-A10701-cpt)
    :cvar D:
    :cvar J:
    :cvar H:
    :cvar N:
    :cvar M:
    :cvar S:
    :cvar W:
    :cvar Y:
    """
    D = "D"
    J = "J"
    H = "H"
    N = "N"
    M = "M"
    S = "S"
    W = "W"
    Y = "Y"


class CalendarType(Enum):
    """
    vocSet: T10682 (C-0-T10682-cpt)
    :cvar GREG:
    """
    GREG = "GREG"


class CaliforniaAthapaskan(Enum):
    """
    abstDomain: A18391 (C-0-T18130-A18352-A18356-A18358-A18386-A18391-cpt)
    :cvar X_KTW:
    :cvar X_HUP:
    """
    X_KTW = "x-KTW"
    X_HUP = "x-HUP"


class CapsuleDrugForm(Enum):
    """
    specDomain: S14507 (C-0-T19651-A14411-A14412-A14484-S14506-S14507-cpt)
    :cvar ENTCAP:
    :cvar ERENTCAP:
    :cvar ERCAP:
    :cvar ERCAP12:
    :cvar ERCAP24:
    :cvar ERECCAP:
    :cvar ORCAP:
    :cvar CAP:
    """
    ENTCAP = "ENTCAP"
    ERENTCAP = "ERENTCAP"
    ERCAP = "ERCAP"
    ERCAP12 = "ERCAP12"
    ERCAP24 = "ERCAP24"
    ERECCAP = "ERECCAP"
    ORCAP = "ORCAP"
    CAP = "CAP"


class CardClinPracticeSetting(Enum):
    """
    specDomain: S10590 (C-0-T12206-A17660-A19450-A10588-S10589-S10590-cpt)
    :cvar CARD:
    :cvar PEDCARD:
    """
    CARD = "CARD"
    PEDCARD = "PEDCARD"


class CardiologySpecialistOrTechnologistHipaa(Enum):
    """
    abstDomain: A13660 (C-0-T13129-A13130-A13644-A13660-cpt)
    :cvar VALUE_246_VC0100_N:
    :cvar VALUE_246_VC2400_N:
    :cvar VALUE_246_VC2901_N:
    :cvar VALUE_246_VC2902_N:
    :cvar VALUE_246_VC2903_N:
    :cvar VALUE_246_VP3600_N:
    :cvar VALUE_246_VS1301_N:
    :cvar VALUE_246_VV0100_N:
    """
    VALUE_246_VC0100_N = "246VC0100N"
    VALUE_246_VC2400_N = "246VC2400N"
    VALUE_246_VC2901_N = "246VC2901N"
    VALUE_246_VC2902_N = "246VC2902N"
    VALUE_246_VC2903_N = "246VC2903N"
    VALUE_246_VP3600_N = "246VP3600N"
    VALUE_246_VS1301_N = "246VS1301N"
    VALUE_246_VV0100_N = "246VV0100N"


class CardiologyTechnicianHipaa(Enum):
    """
    abstDomain: A13700 (C-0-T13129-A13130-A13634-S13635-A13637-A13700-cpt)
    :cvar VALUE_246_WC3000_N:
    :cvar VALUE_246_WE0400_N:
    """
    VALUE_246_WC3000_N = "246WC3000N"
    VALUE_246_WE0400_N = "246WE0400N"


class CaseTransmissionMode(Enum):
    """
    abstDomain: A19795 (C-0-T13953-A19820-A16226-A19712-A19795-cpt)
    :cvar AIRTRNS:
    :cvar ANANTRNS:
    :cvar ANHUMTRNS:
    :cvar BLDTRNS:
    :cvar BDYFLDTRNS:
    :cvar ENVTRNS:
    :cvar FECTRNS:
    :cvar FOMTRNS:
    :cvar FOODTRNS:
    :cvar HUMHUMTRNS:
    :cvar INDTRNS:
    :cvar LACTTRNS:
    :cvar NOSTRNS:
    :cvar PARTRNS:
    :cvar SEXTRNS:
    :cvar DERMTRNS:
    :cvar TRNSFTRNS:
    :cvar PLACTRNS:
    :cvar VECTRNS:
    :cvar WATTRNS:
    """
    AIRTRNS = "AIRTRNS"
    ANANTRNS = "ANANTRNS"
    ANHUMTRNS = "ANHUMTRNS"
    BLDTRNS = "BLDTRNS"
    BDYFLDTRNS = "BDYFLDTRNS"
    ENVTRNS = "ENVTRNS"
    FECTRNS = "FECTRNS"
    FOMTRNS = "FOMTRNS"
    FOODTRNS = "FOODTRNS"
    HUMHUMTRNS = "HUMHUMTRNS"
    INDTRNS = "INDTRNS"
    LACTTRNS = "LACTTRNS"
    NOSTRNS = "NOSTRNS"
    PARTRNS = "PARTRNS"
    SEXTRNS = "SEXTRNS"
    DERMTRNS = "DERMTRNS"
    TRNSFTRNS = "TRNSFTRNS"
    PLACTRNS = "PLACTRNS"
    VECTRNS = "VECTRNS"
    WATTRNS = "WATTRNS"


class Catawba(Enum):
    """
    specDomain: S14972 (C-0-T14914-S14915-S14916-S14972-cpt)
    :cvar VALUE_1076_9:
    :cvar VALUE_1744_2:
    :cvar VALUE_1741_8:
    :cvar VALUE_1742_6:
    :cvar VALUE_1743_4:
    :cvar VALUE_1745_9:
    :cvar VALUE_1746_7:
    :cvar VALUE_1747_5:
    :cvar VALUE_1748_3:
    :cvar VALUE_1749_1:
    :cvar VALUE_1750_9:
    :cvar VALUE_1751_7:
    :cvar VALUE_1752_5:
    :cvar VALUE_1753_3:
    :cvar VALUE_1754_1:
    :cvar VALUE_1755_8:
    :cvar VALUE_1756_6:
    :cvar VALUE_1757_4:
    :cvar VALUE_1758_2:
    :cvar VALUE_1759_0:
    :cvar VALUE_1760_8:
    :cvar VALUE_1761_6:
    :cvar VALUE_1762_4:
    :cvar VALUE_1763_2:
    :cvar VALUE_1764_0:
    :cvar VALUE_1765_7:
    :cvar VALUE_1766_5:
    :cvar VALUE_1767_3:
    :cvar VALUE_1768_1:
    :cvar VALUE_1769_9:
    :cvar VALUE_1770_7:
    :cvar VALUE_1771_5:
    :cvar VALUE_1772_3:
    :cvar VALUE_1773_1:
    :cvar VALUE_1774_9:
    :cvar VALUE_1775_6:
    :cvar VALUE_1776_4:
    :cvar VALUE_1777_2:
    :cvar VALUE_1778_0:
    :cvar VALUE_1780_6:
    :cvar VALUE_1779_8:
    :cvar VALUE_1781_4:
    :cvar VALUE_1782_2:
    :cvar VALUE_1783_0:
    :cvar VALUE_1784_8:
    :cvar VALUE_1785_5:
    :cvar VALUE_1786_3:
    :cvar VALUE_1787_1:
    :cvar VALUE_1788_9:
    :cvar VALUE_1789_7:
    :cvar VALUE_1790_5:
    :cvar VALUE_1791_3:
    :cvar VALUE_1792_1:
    :cvar VALUE_1793_9:
    :cvar VALUE_1795_4:
    :cvar VALUE_1794_7:
    :cvar VALUE_1796_2:
    :cvar VALUE_1797_0:
    :cvar VALUE_1798_8:
    :cvar VALUE_1799_6:
    :cvar VALUE_1800_2:
    :cvar VALUE_1801_0:
    :cvar VALUE_1802_8:
    :cvar VALUE_1803_6:
    :cvar VALUE_1804_4:
    :cvar VALUE_1805_1:
    :cvar VALUE_1806_9:
    :cvar VALUE_1807_7:
    :cvar VALUE_1808_5:
    :cvar VALUE_1809_3:
    """
    VALUE_1076_9 = "1076-9"
    VALUE_1744_2 = "1744-2"
    VALUE_1741_8 = "1741-8"
    VALUE_1742_6 = "1742-6"
    VALUE_1743_4 = "1743-4"
    VALUE_1745_9 = "1745-9"
    VALUE_1746_7 = "1746-7"
    VALUE_1747_5 = "1747-5"
    VALUE_1748_3 = "1748-3"
    VALUE_1749_1 = "1749-1"
    VALUE_1750_9 = "1750-9"
    VALUE_1751_7 = "1751-7"
    VALUE_1752_5 = "1752-5"
    VALUE_1753_3 = "1753-3"
    VALUE_1754_1 = "1754-1"
    VALUE_1755_8 = "1755-8"
    VALUE_1756_6 = "1756-6"
    VALUE_1757_4 = "1757-4"
    VALUE_1758_2 = "1758-2"
    VALUE_1759_0 = "1759-0"
    VALUE_1760_8 = "1760-8"
    VALUE_1761_6 = "1761-6"
    VALUE_1762_4 = "1762-4"
    VALUE_1763_2 = "1763-2"
    VALUE_1764_0 = "1764-0"
    VALUE_1765_7 = "1765-7"
    VALUE_1766_5 = "1766-5"
    VALUE_1767_3 = "1767-3"
    VALUE_1768_1 = "1768-1"
    VALUE_1769_9 = "1769-9"
    VALUE_1770_7 = "1770-7"
    VALUE_1771_5 = "1771-5"
    VALUE_1772_3 = "1772-3"
    VALUE_1773_1 = "1773-1"
    VALUE_1774_9 = "1774-9"
    VALUE_1775_6 = "1775-6"
    VALUE_1776_4 = "1776-4"
    VALUE_1777_2 = "1777-2"
    VALUE_1778_0 = "1778-0"
    VALUE_1780_6 = "1780-6"
    VALUE_1779_8 = "1779-8"
    VALUE_1781_4 = "1781-4"
    VALUE_1782_2 = "1782-2"
    VALUE_1783_0 = "1783-0"
    VALUE_1784_8 = "1784-8"
    VALUE_1785_5 = "1785-5"
    VALUE_1786_3 = "1786-3"
    VALUE_1787_1 = "1787-1"
    VALUE_1788_9 = "1788-9"
    VALUE_1789_7 = "1789-7"
    VALUE_1790_5 = "1790-5"
    VALUE_1791_3 = "1791-3"
    VALUE_1792_1 = "1792-1"
    VALUE_1793_9 = "1793-9"
    VALUE_1795_4 = "1795-4"
    VALUE_1794_7 = "1794-7"
    VALUE_1796_2 = "1796-2"
    VALUE_1797_0 = "1797-0"
    VALUE_1798_8 = "1798-8"
    VALUE_1799_6 = "1799-6"
    VALUE_1800_2 = "1800-2"
    VALUE_1801_0 = "1801-0"
    VALUE_1802_8 = "1802-8"
    VALUE_1803_6 = "1803-6"
    VALUE_1804_4 = "1804-4"
    VALUE_1805_1 = "1805-1"
    VALUE_1806_9 = "1806-9"
    VALUE_1807_7 = "1807-7"
    VALUE_1808_5 = "1808-5"
    VALUE_1809_3 = "1809-3"


class CecostomyRoute(Enum):
    """
    abstDomain: A17036 (C-0-T14581-A17021-A17036-cpt)
    :cvar CECINSTL:
    """
    CECINSTL = "CECINSTL"


class CentralMuskogean(Enum):
    """
    abstDomain: A18342 (C-0-T18130-A18338-A18342-cpt)
    :cvar X_AKZ:
    :cvar X_CKU:
    :cvar X_MIK:
    """
    X_AKZ = "x-AKZ"
    X_CKU = "x-CKU"
    X_MIK = "x-MIK"


class CentralNumic(Enum):
    """
    abstDomain: A18611 (C-0-T18130-A18605-A18606-A18611-cpt)
    :cvar X_COM:
    :cvar X_PAR:
    :cvar X_SHH:
    """
    X_COM = "x-COM"
    X_PAR = "x-PAR"
    X_SHH = "x-SHH"


class CentralSalish(Enum):
    """
    abstDomain: A18524 (C-0-T18130-A18523-A18524-cpt)
    :cvar X_CLM:
    :cvar X_LUT:
    :cvar X_STR:
    """
    X_CLM = "x-CLM"
    X_LUT = "x-LUT"
    X_STR = "x-STR"


class CervicalRoute(Enum):
    """
    abstDomain: A17038 (C-0-T14581-A17021-A17038-cpt)
    :cvar CERVINJ:
    :cvar CERVINS:
    :cvar DENRINSE:
    :cvar CERV:
    :cvar DEN:
    """
    CERVINJ = "CERVINJ"
    CERVINS = "CERVINS"
    DENRINSE = "DENRINSE"
    CERV = "CERV"
    DEN = "DEN"


class Charset(Enum):
    """
    vocSet: T14853 (C-0-T14853-cpt)
    :cvar EBCDIC:
    :cvar ISO_10646_UCS_2:
    :cvar ISO_10646_UCS_4:
    :cvar ISO_8859_1:
    :cvar ISO_8859_2:
    :cvar ISO_8859_5:
    :cvar JIS_2022_JP:
    :cvar US_ASCII:
    :cvar UTF_7:
    :cvar UTF_8:
    """
    EBCDIC = "EBCDIC"
    ISO_10646_UCS_2 = "ISO-10646-UCS-2"
    ISO_10646_UCS_4 = "ISO-10646-UCS-4"
    ISO_8859_1 = "ISO-8859-1"
    ISO_8859_2 = "ISO-8859-2"
    ISO_8859_5 = "ISO-8859-5"
    JIS_2022_JP = "JIS-2022-JP"
    US_ASCII = "US-ASCII"
    UTF_7 = "UTF-7"
    UTF_8 = "UTF-8"


class Chew(Enum):
    """
    abstDomain: A14582 (C-0-T14581-A16931-A14582-cpt)
    :cvar CHEW:
    """
    CHEW = "CHEW"


class Child(Enum):
    """
    specDomain: S16360 (C-0-T12206-A19563-S17926-S16360-cpt)
    :cvar CHLDADOPT:
    :cvar DAUADOPT:
    :cvar SONADOPT:
    :cvar CHLDINLAW:
    :cvar DAUINLAW:
    :cvar SONINLAW:
    :cvar CHLDFOST:
    :cvar DAUFOST:
    :cvar SONFOST:
    :cvar NCHILD:
    :cvar DAU:
    :cvar SON:
    :cvar STPCHLD:
    :cvar STPDAU:
    :cvar STPSON:
    :cvar CHILD:
    """
    CHLDADOPT = "CHLDADOPT"
    DAUADOPT = "DAUADOPT"
    SONADOPT = "SONADOPT"
    CHLDINLAW = "CHLDINLAW"
    DAUINLAW = "DAUINLAW"
    SONINLAW = "SONINLAW"
    CHLDFOST = "CHLDFOST"
    DAUFOST = "DAUFOST"
    SONFOST = "SONFOST"
    NCHILD = "NCHILD"
    DAU = "DAU"
    SON = "SON"
    STPCHLD = "STPCHLD"
    STPDAU = "STPDAU"
    STPSON = "STPSON"
    CHILD = "CHILD"


class ChildInLaw(Enum):
    """
    specDomain: S11563 (C-0-T12206-A19563-S17926-S16360-S11563-cpt)
    :cvar CHLDINLAW:
    :cvar DAUINLAW:
    :cvar SONINLAW:
    """
    CHLDINLAW = "CHLDINLAW"
    DAUINLAW = "DAUINLAW"
    SONINLAW = "SONINLAW"


class Chimakuan(Enum):
    """
    abstDomain: A18238 (C-0-T18130-A18238-cpt)
    :cvar X_QUI:
    """
    X_QUI = "x-QUI"


class ChiropractersHipaa(Enum):
    """
    specDomain: S13175 (C-0-T13129-A13130-A13174-S13175-cpt)
    :cvar VALUE_111_N00000_N:
    :cvar VALUE_111_NI0900_N:
    :cvar VALUE_111_NN0400_N:
    :cvar VALUE_111_NN1001_N:
    :cvar VALUE_111_NX0100_N:
    :cvar VALUE_111_NX0800_N:
    :cvar VALUE_111_NR0200_N:
    :cvar VALUE_111_NS0005_N:
    :cvar VALUE_111_NT0100_N:
    """
    VALUE_111_N00000_N = "111N00000N"
    VALUE_111_NI0900_N = "111NI0900N"
    VALUE_111_NN0400_N = "111NN0400N"
    VALUE_111_NN1001_N = "111NN1001N"
    VALUE_111_NX0100_N = "111NX0100N"
    VALUE_111_NX0800_N = "111NX0800N"
    VALUE_111_NR0200_N = "111NR0200N"
    VALUE_111_NS0005_N = "111NS0005N"
    VALUE_111_NT0100_N = "111NT0100N"


class ChiropracticProvidersProviderCodes(Enum):
    """
    specDomain: S20308 (C-0-T19465-S20308-cpt)
    :cvar VALUE_111_N00000_X:
    :cvar VALUE_111_NI0900_X:
    :cvar VALUE_111_NN0400_X:
    :cvar VALUE_111_NN1001_X:
    :cvar VALUE_111_NX0100_X:
    :cvar VALUE_111_NX0800_X:
    :cvar VALUE_111_NR0200_X:
    :cvar VALUE_111_NS0005_X:
    :cvar VALUE_111_NT0100_X:
    :cvar VALUE_110000000_X:
    """
    VALUE_111_N00000_X = "111N00000X"
    VALUE_111_NI0900_X = "111NI0900X"
    VALUE_111_NN0400_X = "111NN0400X"
    VALUE_111_NN1001_X = "111NN1001X"
    VALUE_111_NX0100_X = "111NX0100X"
    VALUE_111_NX0800_X = "111NX0800X"
    VALUE_111_NR0200_X = "111NR0200X"
    VALUE_111_NS0005_X = "111NS0005X"
    VALUE_111_NT0100_X = "111NT0100X"
    VALUE_110000000_X = "110000000X"


class ChiropractorProviderCodes(Enum):
    """
    specDomain: S20309 (C-0-T19465-S20308-S20309-cpt)
    :cvar VALUE_111_N00000_X:
    :cvar VALUE_111_NI0900_X:
    :cvar VALUE_111_NN0400_X:
    :cvar VALUE_111_NN1001_X:
    :cvar VALUE_111_NX0100_X:
    :cvar VALUE_111_NX0800_X:
    :cvar VALUE_111_NR0200_X:
    :cvar VALUE_111_NS0005_X:
    :cvar VALUE_111_NT0100_X:
    """
    VALUE_111_N00000_X = "111N00000X"
    VALUE_111_NI0900_X = "111NI0900X"
    VALUE_111_NN0400_X = "111NN0400X"
    VALUE_111_NN1001_X = "111NN1001X"
    VALUE_111_NX0100_X = "111NX0100X"
    VALUE_111_NX0800_X = "111NX0800X"
    VALUE_111_NR0200_X = "111NR0200X"
    VALUE_111_NS0005_X = "111NS0005X"
    VALUE_111_NT0100_X = "111NT0100X"


class ChiwereWinnebago(Enum):
    """
    abstDomain: A18593 (C-0-T18130-A18552-A18553-A18562-A18593-cpt)
    :cvar X_IOW:
    :cvar X_WIN:
    """
    X_IOW = "x-IOW"
    X_WIN = "x-WIN"


class ChronicCareFacility(Enum):
    """
    specDomain: S13792 (C-0-T12206-A17660-A19450-A10588-S10602-S13792-cpt)
    :cvar CHR:
    :cvar VALUE_281_PC2000_N:
    """
    CHR = "CHR"
    VALUE_281_PC2000_N = "281PC2000N"


class ChronicDiseaseHospitalProviderCodes(Enum):
    """
    specDomain: S20735 (C-0-T19465-S20733-S20735-cpt)
    :cvar VALUE_281_P00000_X:
    :cvar VALUE_281_PC2000_X:
    """
    VALUE_281_P00000_X = "281P00000X"
    VALUE_281_PC2000_X = "281PC2000X"


class ClaimantCoveredPartyRoleType(Enum):
    """
    abstDomain: A19810 (C-0-T12206-A19809-A19805-A19810-cpt)
    :cvar CRIMEVIC:
    :cvar INJ:
    :cvar INJWKR:
    """
    CRIMEVIC = "CRIMEVIC"
    INJ = "INJ"
    INJWKR = "INJWKR"


class ClinicCenterProviderCodes(Enum):
    """
    specDomain: S20679 (C-0-T19465-S20678-S20679-cpt)
    :cvar VALUE_261_Q00000_X:
    :cvar VALUE_261_QM0855_X:
    :cvar VALUE_261_QA0600_X:
    :cvar VALUE_261_QM0850_X:
    :cvar VALUE_261_QA0005_X:
    :cvar VALUE_261_QA0006_X:
    :cvar VALUE_261_QA1903_X:
    :cvar VALUE_261_QA0900_X:
    :cvar VALUE_261_QA3000_X:
    :cvar VALUE_261_QB0400_X:
    :cvar VALUE_261_QC1500_X:
    :cvar VALUE_261_QC1800_X:
    :cvar VALUE_261_QC0050_X:
    :cvar VALUE_261_QD0000_X:
    :cvar VALUE_261_QD1600_X:
    :cvar VALUE_261_QE0002_X:
    :cvar VALUE_261_QE0700_X:
    :cvar VALUE_261_QE0800_X:
    :cvar VALUE_261_QF0050_X:
    :cvar VALUE_261_QF0400_X:
    :cvar VALUE_261_QG0250_X:
    :cvar VALUE_261_QH0100_X:
    :cvar VALUE_261_QH0700_X:
    :cvar VALUE_261_QI0500_X:
    :cvar VALUE_261_QL0400_X:
    :cvar VALUE_261_QM1200_X:
    :cvar VALUE_261_QR0206_X:
    :cvar VALUE_261_QM2500_X:
    :cvar VALUE_261_QM3000_X:
    :cvar VALUE_261_QM0801_X:
    :cvar VALUE_261_QM2800_X:
    :cvar VALUE_261_QM1000_X:
    :cvar VALUE_261_QM1100_X:
    :cvar VALUE_261_QM1101_X:
    :cvar VALUE_261_QM1102_X:
    :cvar VALUE_261_QR0208_X:
    :cvar VALUE_261_QR0207_X:
    :cvar VALUE_261_QM1300_X:
    :cvar VALUE_261_QX0100_X:
    :cvar VALUE_261_QX0200_X:
    :cvar VALUE_261_QX0203_X:
    :cvar VALUE_261_QS0132_X:
    :cvar VALUE_261_QS0112_X:
    :cvar VALUE_261_QP3300_X:
    :cvar VALUE_261_QP2000_X:
    :cvar VALUE_261_QP1100_X:
    :cvar VALUE_261_QP2300_X:
    :cvar VALUE_261_QP2400_X:
    :cvar VALUE_261_QP0904_X:
    :cvar VALUE_261_QP0905_X:
    :cvar VALUE_261_QR0200_X:
    :cvar VALUE_261_QR0800_X:
    :cvar VALUE_261_QR0400_X:
    :cvar VALUE_261_QR0401_X:
    :cvar VALUE_261_QR0405_X:
    :cvar VALUE_261_QR0404_X:
    :cvar VALUE_261_QR1100_X:
    :cvar VALUE_261_QR1300_X:
    :cvar VALUE_261_QS1200_X:
    :cvar VALUE_261_QS1000_X:
    :cvar VALUE_261_QU0200_X:
    :cvar VALUE_261_QV0200_X:
    """
    VALUE_261_Q00000_X = "261Q00000X"
    VALUE_261_QM0855_X = "261QM0855X"
    VALUE_261_QA0600_X = "261QA0600X"
    VALUE_261_QM0850_X = "261QM0850X"
    VALUE_261_QA0005_X = "261QA0005X"
    VALUE_261_QA0006_X = "261QA0006X"
    VALUE_261_QA1903_X = "261QA1903X"
    VALUE_261_QA0900_X = "261QA0900X"
    VALUE_261_QA3000_X = "261QA3000X"
    VALUE_261_QB0400_X = "261QB0400X"
    VALUE_261_QC1500_X = "261QC1500X"
    VALUE_261_QC1800_X = "261QC1800X"
    VALUE_261_QC0050_X = "261QC0050X"
    VALUE_261_QD0000_X = "261QD0000X"
    VALUE_261_QD1600_X = "261QD1600X"
    VALUE_261_QE0002_X = "261QE0002X"
    VALUE_261_QE0700_X = "261QE0700X"
    VALUE_261_QE0800_X = "261QE0800X"
    VALUE_261_QF0050_X = "261QF0050X"
    VALUE_261_QF0400_X = "261QF0400X"
    VALUE_261_QG0250_X = "261QG0250X"
    VALUE_261_QH0100_X = "261QH0100X"
    VALUE_261_QH0700_X = "261QH0700X"
    VALUE_261_QI0500_X = "261QI0500X"
    VALUE_261_QL0400_X = "261QL0400X"
    VALUE_261_QM1200_X = "261QM1200X"
    VALUE_261_QR0206_X = "261QR0206X"
    VALUE_261_QM2500_X = "261QM2500X"
    VALUE_261_QM3000_X = "261QM3000X"
    VALUE_261_QM0801_X = "261QM0801X"
    VALUE_261_QM2800_X = "261QM2800X"
    VALUE_261_QM1000_X = "261QM1000X"
    VALUE_261_QM1100_X = "261QM1100X"
    VALUE_261_QM1101_X = "261QM1101X"
    VALUE_261_QM1102_X = "261QM1102X"
    VALUE_261_QR0208_X = "261QR0208X"
    VALUE_261_QR0207_X = "261QR0207X"
    VALUE_261_QM1300_X = "261QM1300X"
    VALUE_261_QX0100_X = "261QX0100X"
    VALUE_261_QX0200_X = "261QX0200X"
    VALUE_261_QX0203_X = "261QX0203X"
    VALUE_261_QS0132_X = "261QS0132X"
    VALUE_261_QS0112_X = "261QS0112X"
    VALUE_261_QP3300_X = "261QP3300X"
    VALUE_261_QP2000_X = "261QP2000X"
    VALUE_261_QP1100_X = "261QP1100X"
    VALUE_261_QP2300_X = "261QP2300X"
    VALUE_261_QP2400_X = "261QP2400X"
    VALUE_261_QP0904_X = "261QP0904X"
    VALUE_261_QP0905_X = "261QP0905X"
    VALUE_261_QR0200_X = "261QR0200X"
    VALUE_261_QR0800_X = "261QR0800X"
    VALUE_261_QR0400_X = "261QR0400X"
    VALUE_261_QR0401_X = "261QR0401X"
    VALUE_261_QR0405_X = "261QR0405X"
    VALUE_261_QR0404_X = "261QR0404X"
    VALUE_261_QR1100_X = "261QR1100X"
    VALUE_261_QR1300_X = "261QR1300X"
    VALUE_261_QS1200_X = "261QS1200X"
    VALUE_261_QS1000_X = "261QS1000X"
    VALUE_261_QU0200_X = "261QU0200X"
    VALUE_261_QV0200_X = "261QV0200X"


class ClinicalNurseSpecialistHipaa(Enum):
    """
    specDomain: S13364 (C-0-T13129-A13130-A13363-S13364-cpt)
    :cvar VALUE_364_S00000_N:
    :cvar VALUE_364_SA2100_N:
    :cvar VALUE_364_SA2200_N:
    :cvar VALUE_364_SC2300_N:
    :cvar VALUE_364_SC1501_N:
    :cvar VALUE_364_SC0200_N:
    :cvar VALUE_364_SE0003_N:
    :cvar VALUE_364_SE1400_N:
    :cvar VALUE_364_SF0001_N:
    :cvar VALUE_364_SG0600_N:
    :cvar VALUE_364_SH1100_N:
    :cvar VALUE_364_SH0200_N:
    :cvar VALUE_364_SI0800_N:
    :cvar VALUE_364_SL0600_N:
    :cvar VALUE_364_SM0705_N:
    :cvar VALUE_364_SN0000_N:
    :cvar VALUE_364_SN0004_N:
    :cvar VALUE_364_SN0800_N:
    :cvar VALUE_364_SX0106_N:
    :cvar VALUE_364_SX0200_N:
    :cvar VALUE_364_SX0204_N:
    :cvar VALUE_364_SP0200_N:
    :cvar VALUE_364_SP1700_N:
    :cvar VALUE_364_SP2800_N:
    :cvar VALUE_364_SP0807_N:
    :cvar VALUE_364_SP0808_N:
    :cvar VALUE_364_SP0809_N:
    :cvar VALUE_364_SP0810_N:
    :cvar VALUE_364_SP0811_N:
    :cvar VALUE_364_SP0812_N:
    :cvar VALUE_364_SP0813_N:
    :cvar VALUE_364_SR0400_N:
    :cvar VALUE_364_SR1300_N:
    :cvar VALUE_364_SS0200_N:
    :cvar VALUE_364_ST0500_N:
    :cvar VALUE_364_SW0102_N:
    """
    VALUE_364_S00000_N = "364S00000N"
    VALUE_364_SA2100_N = "364SA2100N"
    VALUE_364_SA2200_N = "364SA2200N"
    VALUE_364_SC2300_N = "364SC2300N"
    VALUE_364_SC1501_N = "364SC1501N"
    VALUE_364_SC0200_N = "364SC0200N"
    VALUE_364_SE0003_N = "364SE0003N"
    VALUE_364_SE1400_N = "364SE1400N"
    VALUE_364_SF0001_N = "364SF0001N"
    VALUE_364_SG0600_N = "364SG0600N"
    VALUE_364_SH1100_N = "364SH1100N"
    VALUE_364_SH0200_N = "364SH0200N"
    VALUE_364_SI0800_N = "364SI0800N"
    VALUE_364_SL0600_N = "364SL0600N"
    VALUE_364_SM0705_N = "364SM0705N"
    VALUE_364_SN0000_N = "364SN0000N"
    VALUE_364_SN0004_N = "364SN0004N"
    VALUE_364_SN0800_N = "364SN0800N"
    VALUE_364_SX0106_N = "364SX0106N"
    VALUE_364_SX0200_N = "364SX0200N"
    VALUE_364_SX0204_N = "364SX0204N"
    VALUE_364_SP0200_N = "364SP0200N"
    VALUE_364_SP1700_N = "364SP1700N"
    VALUE_364_SP2800_N = "364SP2800N"
    VALUE_364_SP0807_N = "364SP0807N"
    VALUE_364_SP0808_N = "364SP0808N"
    VALUE_364_SP0809_N = "364SP0809N"
    VALUE_364_SP0810_N = "364SP0810N"
    VALUE_364_SP0811_N = "364SP0811N"
    VALUE_364_SP0812_N = "364SP0812N"
    VALUE_364_SP0813_N = "364SP0813N"
    VALUE_364_SR0400_N = "364SR0400N"
    VALUE_364_SR1300_N = "364SR1300N"
    VALUE_364_SS0200_N = "364SS0200N"
    VALUE_364_ST0500_N = "364ST0500N"
    VALUE_364_SW0102_N = "364SW0102N"


class ClinicalNurseSpecialistProviderCodes(Enum):
    """
    specDomain: S20465 (C-0-T19465-S20463-S20465-cpt)
    :cvar VALUE_364_S00000_X:
    :cvar VALUE_364_SA2100_X:
    :cvar VALUE_364_SA2200_X:
    :cvar VALUE_364_SC2300_X:
    :cvar VALUE_364_SC1501_X:
    :cvar VALUE_364_SC0200_X:
    :cvar VALUE_364_SE0003_X:
    :cvar VALUE_364_SE1400_X:
    :cvar VALUE_364_SF0001_X:
    :cvar VALUE_364_SG0600_X:
    :cvar VALUE_364_SH1100_X:
    :cvar VALUE_364_SH0200_X:
    :cvar VALUE_364_SI0800_X:
    :cvar VALUE_364_SL0600_X:
    :cvar VALUE_364_SM0705_X:
    :cvar VALUE_364_SN0000_X:
    :cvar VALUE_364_SN0800_X:
    :cvar VALUE_364_SX0106_X:
    :cvar VALUE_364_SX0200_X:
    :cvar VALUE_364_SX0204_X:
    :cvar VALUE_364_SP0200_X:
    :cvar VALUE_364_SP1700_X:
    :cvar VALUE_364_SP2800_X:
    :cvar VALUE_364_SP0808_X:
    :cvar VALUE_364_SP0809_X:
    :cvar VALUE_364_SP0807_X:
    :cvar VALUE_364_SP0810_X:
    :cvar VALUE_364_SP0811_X:
    :cvar VALUE_364_SP0812_X:
    :cvar VALUE_364_SP0813_X:
    :cvar VALUE_364_SR0400_X:
    :cvar VALUE_364_SS0200_X:
    :cvar VALUE_364_ST0500_X:
    :cvar VALUE_364_SW0102_X:
    """
    VALUE_364_S00000_X = "364S00000X"
    VALUE_364_SA2100_X = "364SA2100X"
    VALUE_364_SA2200_X = "364SA2200X"
    VALUE_364_SC2300_X = "364SC2300X"
    VALUE_364_SC1501_X = "364SC1501X"
    VALUE_364_SC0200_X = "364SC0200X"
    VALUE_364_SE0003_X = "364SE0003X"
    VALUE_364_SE1400_X = "364SE1400X"
    VALUE_364_SF0001_X = "364SF0001X"
    VALUE_364_SG0600_X = "364SG0600X"
    VALUE_364_SH1100_X = "364SH1100X"
    VALUE_364_SH0200_X = "364SH0200X"
    VALUE_364_SI0800_X = "364SI0800X"
    VALUE_364_SL0600_X = "364SL0600X"
    VALUE_364_SM0705_X = "364SM0705X"
    VALUE_364_SN0000_X = "364SN0000X"
    VALUE_364_SN0800_X = "364SN0800X"
    VALUE_364_SX0106_X = "364SX0106X"
    VALUE_364_SX0200_X = "364SX0200X"
    VALUE_364_SX0204_X = "364SX0204X"
    VALUE_364_SP0200_X = "364SP0200X"
    VALUE_364_SP1700_X = "364SP1700X"
    VALUE_364_SP2800_X = "364SP2800X"
    VALUE_364_SP0808_X = "364SP0808X"
    VALUE_364_SP0809_X = "364SP0809X"
    VALUE_364_SP0807_X = "364SP0807X"
    VALUE_364_SP0810_X = "364SP0810X"
    VALUE_364_SP0811_X = "364SP0811X"
    VALUE_364_SP0812_X = "364SP0812X"
    VALUE_364_SP0813_X = "364SP0813X"
    VALUE_364_SR0400_X = "364SR0400X"
    VALUE_364_SS0200_X = "364SS0200X"
    VALUE_364_ST0500_X = "364ST0500X"
    VALUE_364_SW0102_X = "364SW0102X"


class ClinicalResearchEventReason(Enum):
    """
    abstDomain: A19755 (C-0-T14878-A19754-A19755-cpt)
    :cvar RET:
    :cvar SCH:
    :cvar TRM:
    :cvar UNS:
    """
    RET = "RET"
    SCH = "SCH"
    TRM = "TRM"
    UNS = "UNS"


class ClinicalResearchObservationReason(Enum):
    """
    abstDomain: A19756 (C-0-T14878-A19754-A19756-cpt)
    :cvar NPT:
    :cvar UPT:
    :cvar PPT:
    """
    NPT = "NPT"
    UPT = "UPT"
    PPT = "PPT"


class CodeIsNotValid(Enum):
    """
    specDomain: S21659 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S21659-cpt)
    :cvar CODE_INVAL:
    :cvar CODE_DEPREC:
    """
    CODE_INVAL = "CODE_INVAL"
    CODE_DEPREC = "CODE_DEPREC"


class CodeSystem(Enum):
    """
    vocSet: T396 (C-0-T396-cpt)
    :cvar ABCCODES:
    :cvar AS4_E:
    :cvar AS4:
    :cvar ACKNOWLEDGEMENT_DETAIL_TYPE:
    :cvar ACKNOWLEDGEMENT_CONDITION:
    :cvar ACKNOWLEDGEMENT_DETAIL_CODE:
    :cvar ACKNOWLEDGEMENT_TYPE:
    :cvar ACT_CLASS:
    :cvar ACT_CODE:
    :cvar ACT_EXPOSURE_LEVEL_CODE:
    :cvar ACT_INVOICE_ELEMENT_MODIFIER:
    :cvar ACT_MOOD:
    :cvar ACT_PRIORITY:
    :cvar ACT_REASON:
    :cvar ACT_RELATIONSHIP_CHECKPOINT:
    :cvar ACT_RELATIONSHIP_JOIN:
    :cvar ACT_RELATIONSHIP_SPLIT:
    :cvar ACT_RELATIONSHIP_SUBSET:
    :cvar ACT_RELATIONSHIP_TYPE:
    :cvar ACT_SITE:
    :cvar ACT_STATUS:
    :cvar ACT_UNCERTAINTY:
    :cvar ADDRESS_PART_TYPE:
    :cvar ADMINISTRATIVE_GENDER:
    :cvar ACR:
    :cvar ATC:
    :cvar AMERICAN_INDIAN_ALASKA_NATIVE_LANGUAGES:
    :cvar CAMNCVS:
    :cvar CSAID:
    :cvar CDCA:
    :cvar CDCM:
    :cvar CDS:
    :cvar CVX:
    :cvar MVX:
    :cvar CD2:
    :cvar CE:
    :cvar CLP:
    :cvar CST:
    :cvar C4:
    :cvar C5:
    :cvar CALENDAR:
    :cvar CALENDAR_CYCLE:
    :cvar CALENDAR_TYPE:
    :cvar CCI:
    :cvar ICD_10_CA:
    :cvar CHARSET:
    :cvar CAS:
    :cvar CODE_SYSTEM:
    :cvar CODING_RATIONALE:
    :cvar COMMUNICATION_FUNCTION_TYPE:
    :cvar COMPRESSION_ALGORITHM:
    :cvar CONCEPT_GENERALITY:
    :cvar CONFIDENTIALITY:
    :cvar CONTAINER_CAP:
    :cvar CONTAINER_SEPARATOR:
    :cvar CONTENT_PROCESSING_MODE:
    :cvar CONTEXT_CONTROL:
    :cvar CURRENCY:
    :cvar DCL:
    :cvar DQL:
    :cvar DCM:
    :cvar DATA_TYPE:
    :cvar DENTITION:
    :cvar DEVICE_ALERT_LEVEL:
    :cvar DOCUMENT_COMPLETION:
    :cvar DOCUMENT_STORAGE:
    :cvar EPSG_GEODETIC_PARAMETER_DATASET:
    :cvar E:
    :cvar EDIT_STATUS:
    :cvar EDUCATION_LEVEL:
    :cvar EMPLOYEE_JOB_CLASS:
    :cvar ENCOUNTER_ACUITY:
    :cvar ENCOUNTER_ACCIDENT:
    :cvar ENCOUNTER_ADMISSION_SOURCE:
    :cvar ENCOUNTER_REFERRAL_SOURCE:
    :cvar ENCOUNTER_SPECIAL_COURTESY:
    :cvar ENTITY_CLASS:
    :cvar ENTITY_CODE:
    :cvar ENTITY_DETERMINER:
    :cvar ENTITY_HANDLING:
    :cvar ENTITY_NAME_PART_QUALIFIER:
    :cvar ENTITY_NAME_PART_TYPE:
    :cvar ENTITY_NAME_USE:
    :cvar ENTITY_RISK:
    :cvar ENTITY_STATUS:
    :cvar ENZC:
    :cvar EQUIPMENT_ALERT_LEVEL:
    :cvar ETHNICITY:
    :cvar E5:
    :cvar E7:
    :cvar E6:
    :cvar EXPOSURE_MODE:
    :cvar FDK:
    :cvar FDDX:
    :cvar FDDC:
    :cvar GTSABBREVIATION:
    :cvar GENDER_STATUS:
    :cvar HPC:
    :cvar HB:
    :cvar CODE_SYSTEM_TYPE:
    :cvar CONCEPT_STATUS:
    :cvar HL7_ITSVERSION_CODE:
    :cvar CONCEPT_PROPERTY:
    :cvar HL7_COMMITTEE_IDIN_RIM:
    :cvar HL7_CONFORMANCE_INCLUSION:
    :cvar HL7_DEFINED_ROSE_PROPERTY:
    :cvar HL7_STANDARD_VERSION_CODE:
    :cvar HL7_UPDATE_MODE:
    :cvar HI:
    :cvar HEALTHCARE_PROVIDER_TAXONOMY_HIPAA:
    :cvar HHC:
    :cvar HTML_LINK_TYPE:
    :cvar ICS:
    :cvar I10:
    :cvar I10_P:
    :cvar I9_C:
    :cvar I9:
    :cvar IC2:
    :cvar IETF1766:
    :cvar IBT:
    :cvar MDC:
    :cvar ISO3166_1:
    :cvar ISO3166_2:
    :cvar ISO3166_3:
    :cvar ISO4217:
    :cvar IUPC:
    :cvar IUPP:
    :cvar INTEGRITY_CHECK_ALGORITHM:
    :cvar ICDO:
    :cvar ICSD:
    :cvar JC8:
    :cvar LANGUAGE_ABILITY_MODE:
    :cvar LANGUAGE_ABILITY_PROFICIENCY:
    :cvar LIVING_ARRANGEMENT:
    :cvar LOCAL_MARKUP_IGNORE:
    :cvar LOCAL_REMOTE_CONTROL_STATE:
    :cvar LN:
    :cvar MDFATTRIBUTE_TYPE:
    :cvar MDFSUBJECT_AREA_PREFIX:
    :cvar UMD:
    :cvar MEDCIN:
    :cvar MIME:
    :cvar MANAGED_PARTICIPATION_STATUS:
    :cvar MAP_RELATIONSHIP:
    :cvar MARITAL_STATUS:
    :cvar MATERIAL_TYPE:
    :cvar MDF_HMD_MET_SOURCE_TYPE:
    :cvar MDF_HMD_ROW_TYPE:
    :cvar MDF_RMIM_ROW_TYPE:
    :cvar MEDIA_TYPE:
    :cvar MEDR:
    :cvar MEDX:
    :cvar MEDC:
    :cvar MDDX:
    :cvar MGPI:
    :cvar MESSAGE_WAITING_PRIORITY:
    :cvar MESSAGE_CONDITION:
    :cvar MODIFY_INDICATOR:
    :cvar MULTUM:
    :cvar NAACCR:
    :cvar NDA:
    :cvar NOC:
    :cvar NUCCPROVIDER_CODES:
    :cvar NUBC_UB92:
    :cvar NDC:
    :cvar NAICS:
    :cvar NULL_FLAVOR:
    :cvar NIC:
    :cvar NMMDS:
    :cvar OBSERVATION_INTERPRETATION:
    :cvar OBSERVATION_METHOD:
    :cvar OBSERVATION_VALUE:
    :cvar OHA:
    :cvar ORDERABLE_DRUG_FORM:
    :cvar ORGANIZATION_NAME_TYPE:
    :cvar POS:
    :cvar PARAMETERIZED_DATA_TYPE:
    :cvar PARTICIPATION_FUNCTION:
    :cvar PARTICIPATION_MODE:
    :cvar PARTICIPATION_SIGNATURE:
    :cvar PARTICIPATION_TYPE:
    :cvar PATIENT_IMPORTANCE:
    :cvar PAYMENT_TERMS:
    :cvar PERIODIC_INTERVAL_OF_TIME_ABBREVIATION:
    :cvar PNDS:
    :cvar PERSON_DISABILITY_TYPE:
    :cvar CONCEPT_CODE_RELATIONSHIP:
    :cvar POSTAL_ADDRESS_USE:
    :cvar PROBABILITY_DISTRIBUTION_TYPE:
    :cvar PROCEDURE_METHOD:
    :cvar PROCESSING_ID:
    :cvar PROCESSING_MODE:
    :cvar QUERY_PARAMETER_VALUE:
    :cvar QUERY_PRIORITY:
    :cvar QUERY_QUANTITY_UNIT:
    :cvar QUERY_REQUEST_LIMIT:
    :cvar QUERY_RESPONSE:
    :cvar QUERY_STATUS_CODE:
    :cvar RACE:
    :cvar RC:
    :cvar RELATIONAL_OPERATOR:
    :cvar RELATIONSHIP_CONJUNCTION:
    :cvar RELIGIOUS_AFFILIATION:
    :cvar RESPONSE_LEVEL:
    :cvar RESPONSE_MODALITY:
    :cvar RESPONSE_MODE:
    :cvar ROLE_CLASS:
    :cvar ROLE_CODE:
    :cvar ROLE_LINK_TYPE:
    :cvar ROLE_STATUS:
    :cvar ROUTE_OF_ADMINISTRATION:
    :cvar SCDHEC_GISSPATIAL_ACCURACY_TIERS:
    :cvar SNM3:
    :cvar SNT:
    :cvar SDM:
    :cvar SEQUENCING:
    :cvar SET_OPERATOR:
    :cvar SPECIAL_ARRANGEMENT:
    :cvar SPECIMEN_TYPE:
    :cvar STYLE_TYPE:
    :cvar SUBSTANCE_ADMIN_SUBSTITUTION:
    :cvar SUBSTITUTION_CONDITION:
    :cvar SNM:
    :cvar TABLE_CELL_HORIZONTAL_ALIGN:
    :cvar TABLE_CELL_SCOPE:
    :cvar TABLE_CELL_VERTICAL_ALIGN:
    :cvar TABLE_FRAME:
    :cvar TABLE_RULES:
    :cvar IETF3066:
    :cvar TARGET_AWARENESS:
    :cvar TELECOMMUNICATION_ADDRESS_USE:
    :cvar RCFB:
    :cvar RCV2:
    :cvar TIMING_EVENT:
    :cvar TRANSMISSION_RELATIONSHIP_TYPE_CODE:
    :cvar TRIBAL_ENTITY_US:
    :cvar UC:
    :cvar UCUM:
    :cvar URLSCHEME:
    :cvar UML:
    :cvar UNITS_OF_MEASURE:
    :cvar UPC:
    :cvar VACCINE_MANUFACTURER:
    :cvar VACCINE_TYPE:
    :cvar VOCABULARY_DOMAIN_QUALIFIER:
    :cvar WC:
    :cvar ART:
    :cvar W4:
    :cvar W1_W2:
    """
    ABCCODES = "ABCcodes"
    AS4_E = "AS4E"
    AS4 = "AS4"
    ACKNOWLEDGEMENT_DETAIL_TYPE = "AcknowledgementDetailType"
    ACKNOWLEDGEMENT_CONDITION = "AcknowledgementCondition"
    ACKNOWLEDGEMENT_DETAIL_CODE = "AcknowledgementDetailCode"
    ACKNOWLEDGEMENT_TYPE = "AcknowledgementType"
    ACT_CLASS = "ActClass"
    ACT_CODE = "ActCode"
    ACT_EXPOSURE_LEVEL_CODE = "ActExposureLevelCode"
    ACT_INVOICE_ELEMENT_MODIFIER = "ActInvoiceElementModifier"
    ACT_MOOD = "ActMood"
    ACT_PRIORITY = "ActPriority"
    ACT_REASON = "ActReason"
    ACT_RELATIONSHIP_CHECKPOINT = "ActRelationshipCheckpoint"
    ACT_RELATIONSHIP_JOIN = "ActRelationshipJoin"
    ACT_RELATIONSHIP_SPLIT = "ActRelationshipSplit"
    ACT_RELATIONSHIP_SUBSET = "ActRelationshipSubset"
    ACT_RELATIONSHIP_TYPE = "ActRelationshipType"
    ACT_SITE = "ActSite"
    ACT_STATUS = "ActStatus"
    ACT_UNCERTAINTY = "ActUncertainty"
    ADDRESS_PART_TYPE = "AddressPartType"
    ADMINISTRATIVE_GENDER = "AdministrativeGender"
    ACR = "ACR"
    ATC = "ATC"
    AMERICAN_INDIAN_ALASKA_NATIVE_LANGUAGES = "AmericanIndianAlaskaNativeLanguages"
    CAMNCVS = "CAMNCVS"
    CSAID = "CSAID"
    CDCA = "CDCA"
    CDCM = "CDCM"
    CDS = "CDS"
    CVX = "CVX"
    MVX = "MVX"
    CD2 = "CD2"
    CE = "CE"
    CLP = "CLP"
    CST = "CST"
    C4 = "C4"
    C5 = "C5"
    CALENDAR = "Calendar"
    CALENDAR_CYCLE = "CalendarCycle"
    CALENDAR_TYPE = "CalendarType"
    CCI = "CCI"
    ICD_10_CA = "ICD-10-CA"
    CHARSET = "Charset"
    CAS = "CAS"
    CODE_SYSTEM = "CodeSystem"
    CODING_RATIONALE = "CodingRationale"
    COMMUNICATION_FUNCTION_TYPE = "CommunicationFunctionType"
    COMPRESSION_ALGORITHM = "CompressionAlgorithm"
    CONCEPT_GENERALITY = "ConceptGenerality"
    CONFIDENTIALITY = "Confidentiality"
    CONTAINER_CAP = "ContainerCap"
    CONTAINER_SEPARATOR = "ContainerSeparator"
    CONTENT_PROCESSING_MODE = "ContentProcessingMode"
    CONTEXT_CONTROL = "ContextControl"
    CURRENCY = "Currency"
    DCL = "DCL"
    DQL = "DQL"
    DCM = "DCM"
    DATA_TYPE = "DataType"
    DENTITION = "Dentition"
    DEVICE_ALERT_LEVEL = "DeviceAlertLevel"
    DOCUMENT_COMPLETION = "DocumentCompletion"
    DOCUMENT_STORAGE = "DocumentStorage"
    EPSG_GEODETIC_PARAMETER_DATASET = "EPSG-GeodeticParameterDataset"
    E = "E"
    EDIT_STATUS = "EditStatus"
    EDUCATION_LEVEL = "EducationLevel"
    EMPLOYEE_JOB_CLASS = "EmployeeJobClass"
    ENCOUNTER_ACUITY = "EncounterAcuity"
    ENCOUNTER_ACCIDENT = "EncounterAccident"
    ENCOUNTER_ADMISSION_SOURCE = "EncounterAdmissionSource"
    ENCOUNTER_REFERRAL_SOURCE = "EncounterReferralSource"
    ENCOUNTER_SPECIAL_COURTESY = "EncounterSpecialCourtesy"
    ENTITY_CLASS = "EntityClass"
    ENTITY_CODE = "EntityCode"
    ENTITY_DETERMINER = "EntityDeterminer"
    ENTITY_HANDLING = "EntityHandling"
    ENTITY_NAME_PART_QUALIFIER = "EntityNamePartQualifier"
    ENTITY_NAME_PART_TYPE = "EntityNamePartType"
    ENTITY_NAME_USE = "EntityNameUse"
    ENTITY_RISK = "EntityRisk"
    ENTITY_STATUS = "EntityStatus"
    ENZC = "ENZC"
    EQUIPMENT_ALERT_LEVEL = "EquipmentAlertLevel"
    ETHNICITY = "Ethnicity"
    E5 = "E5"
    E7 = "E7"
    E6 = "E6"
    EXPOSURE_MODE = "ExposureMode"
    FDK = "FDK"
    FDDX = "FDDX"
    FDDC = "FDDC"
    GTSABBREVIATION = "GTSAbbreviation"
    GENDER_STATUS = "GenderStatus"
    HPC = "HPC"
    HB = "HB"
    CODE_SYSTEM_TYPE = "CodeSystemType"
    CONCEPT_STATUS = "ConceptStatus"
    HL7_ITSVERSION_CODE = "HL7ITSVersionCode"
    CONCEPT_PROPERTY = "ConceptProperty"
    HL7_COMMITTEE_IDIN_RIM = "HL7CommitteeIDInRIM"
    HL7_CONFORMANCE_INCLUSION = "HL7ConformanceInclusion"
    HL7_DEFINED_ROSE_PROPERTY = "HL7DefinedRoseProperty"
    HL7_STANDARD_VERSION_CODE = "HL7StandardVersionCode"
    HL7_UPDATE_MODE = "HL7UpdateMode"
    HI = "HI"
    HEALTHCARE_PROVIDER_TAXONOMY_HIPAA = "HealthcareProviderTaxonomyHIPAA"
    HHC = "HHC"
    HTML_LINK_TYPE = "HtmlLinkType"
    ICS = "ICS"
    I10 = "I10"
    I10_P = "I10P"
    I9_C = "I9C"
    I9 = "I9"
    IC2 = "IC2"
    IETF1766 = "IETF1766"
    IBT = "IBT"
    MDC = "MDC"
    ISO3166_1 = "ISO3166-1"
    ISO3166_2 = "ISO3166-2"
    ISO3166_3 = "ISO3166-3"
    ISO4217 = "ISO4217"
    IUPC = "IUPC"
    IUPP = "IUPP"
    INTEGRITY_CHECK_ALGORITHM = "IntegrityCheckAlgorithm"
    ICDO = "ICDO"
    ICSD = "ICSD"
    JC8 = "JC8"
    LANGUAGE_ABILITY_MODE = "LanguageAbilityMode"
    LANGUAGE_ABILITY_PROFICIENCY = "LanguageAbilityProficiency"
    LIVING_ARRANGEMENT = "LivingArrangement"
    LOCAL_MARKUP_IGNORE = "LocalMarkupIgnore"
    LOCAL_REMOTE_CONTROL_STATE = "LocalRemoteControlState"
    LN = "LN"
    MDFATTRIBUTE_TYPE = "MDFAttributeType"
    MDFSUBJECT_AREA_PREFIX = "MDFSubjectAreaPrefix"
    UMD = "UMD"
    MEDCIN = "MEDCIN"
    MIME = "MIME"
    MANAGED_PARTICIPATION_STATUS = "ManagedParticipationStatus"
    MAP_RELATIONSHIP = "MapRelationship"
    MARITAL_STATUS = "MaritalStatus"
    MATERIAL_TYPE = "MaterialType"
    MDF_HMD_MET_SOURCE_TYPE = "MdfHmdMetSourceType"
    MDF_HMD_ROW_TYPE = "MdfHmdRowType"
    MDF_RMIM_ROW_TYPE = "MdfRmimRowType"
    MEDIA_TYPE = "MediaType"
    MEDR = "MEDR"
    MEDX = "MEDX"
    MEDC = "MEDC"
    MDDX = "MDDX"
    MGPI = "MGPI"
    MESSAGE_WAITING_PRIORITY = "MessageWaitingPriority"
    MESSAGE_CONDITION = "MessageCondition"
    MODIFY_INDICATOR = "ModifyIndicator"
    MULTUM = "MULTUM"
    NAACCR = "NAACCR"
    NDA = "NDA"
    NOC = "NOC"
    NUCCPROVIDER_CODES = "NUCCProviderCodes"
    NUBC_UB92 = "NUBC-UB92"
    NDC = "NDC"
    NAICS = "NAICS"
    NULL_FLAVOR = "NullFlavor"
    NIC = "NIC"
    NMMDS = "NMMDS"
    OBSERVATION_INTERPRETATION = "ObservationInterpretation"
    OBSERVATION_METHOD = "ObservationMethod"
    OBSERVATION_VALUE = "ObservationValue"
    OHA = "OHA"
    ORDERABLE_DRUG_FORM = "OrderableDrugForm"
    ORGANIZATION_NAME_TYPE = "OrganizationNameType"
    POS = "POS"
    PARAMETERIZED_DATA_TYPE = "ParameterizedDataType"
    PARTICIPATION_FUNCTION = "ParticipationFunction"
    PARTICIPATION_MODE = "ParticipationMode"
    PARTICIPATION_SIGNATURE = "ParticipationSignature"
    PARTICIPATION_TYPE = "ParticipationType"
    PATIENT_IMPORTANCE = "PatientImportance"
    PAYMENT_TERMS = "PaymentTerms"
    PERIODIC_INTERVAL_OF_TIME_ABBREVIATION = "PeriodicIntervalOfTimeAbbreviation"
    PNDS = "PNDS"
    PERSON_DISABILITY_TYPE = "PersonDisabilityType"
    CONCEPT_CODE_RELATIONSHIP = "ConceptCodeRelationship"
    POSTAL_ADDRESS_USE = "PostalAddressUse"
    PROBABILITY_DISTRIBUTION_TYPE = "ProbabilityDistributionType"
    PROCEDURE_METHOD = "ProcedureMethod"
    PROCESSING_ID = "ProcessingID"
    PROCESSING_MODE = "ProcessingMode"
    QUERY_PARAMETER_VALUE = "QueryParameterValue"
    QUERY_PRIORITY = "QueryPriority"
    QUERY_QUANTITY_UNIT = "QueryQuantityUnit"
    QUERY_REQUEST_LIMIT = "QueryRequestLimit"
    QUERY_RESPONSE = "QueryResponse"
    QUERY_STATUS_CODE = "QueryStatusCode"
    RACE = "Race"
    RC = "RC"
    RELATIONAL_OPERATOR = "RelationalOperator"
    RELATIONSHIP_CONJUNCTION = "RelationshipConjunction"
    RELIGIOUS_AFFILIATION = "ReligiousAffiliation"
    RESPONSE_LEVEL = "ResponseLevel"
    RESPONSE_MODALITY = "ResponseModality"
    RESPONSE_MODE = "ResponseMode"
    ROLE_CLASS = "RoleClass"
    ROLE_CODE = "RoleCode"
    ROLE_LINK_TYPE = "RoleLinkType"
    ROLE_STATUS = "RoleStatus"
    ROUTE_OF_ADMINISTRATION = "RouteOfAdministration"
    SCDHEC_GISSPATIAL_ACCURACY_TIERS = "SCDHEC-GISSpatialAccuracyTiers"
    SNM3 = "SNM3"
    SNT = "SNT"
    SDM = "SDM"
    SEQUENCING = "Sequencing"
    SET_OPERATOR = "SetOperator"
    SPECIAL_ARRANGEMENT = "SpecialArrangement"
    SPECIMEN_TYPE = "SpecimenType"
    STYLE_TYPE = "StyleType"
    SUBSTANCE_ADMIN_SUBSTITUTION = "SubstanceAdminSubstitution"
    SUBSTITUTION_CONDITION = "SubstitutionCondition"
    SNM = "SNM"
    TABLE_CELL_HORIZONTAL_ALIGN = "TableCellHorizontalAlign"
    TABLE_CELL_SCOPE = "TableCellScope"
    TABLE_CELL_VERTICAL_ALIGN = "TableCellVerticalAlign"
    TABLE_FRAME = "TableFrame"
    TABLE_RULES = "TableRules"
    IETF3066 = "IETF3066"
    TARGET_AWARENESS = "TargetAwareness"
    TELECOMMUNICATION_ADDRESS_USE = "TelecommunicationAddressUse"
    RCFB = "RCFB"
    RCV2 = "RCV2"
    TIMING_EVENT = "TimingEvent"
    TRANSMISSION_RELATIONSHIP_TYPE_CODE = "TransmissionRelationshipTypeCode"
    TRIBAL_ENTITY_US = "TribalEntityUS"
    UC = "UC"
    UCUM = "UCUM"
    URLSCHEME = "URLScheme"
    UML = "UML"
    UNITS_OF_MEASURE = "UnitsOfMeasure"
    UPC = "UPC"
    VACCINE_MANUFACTURER = "VaccineManufacturer"
    VACCINE_TYPE = "VaccineType"
    VOCABULARY_DOMAIN_QUALIFIER = "VocabularyDomainQualifier"
    WC = "WC"
    ART = "ART"
    W4 = "W4"
    W1_W2 = "W1-W2"


class CodeSystemType(Enum):
    """
    vocSet: T19359 (C-0-T19359-cpt)
    :cvar E:
    :cvar EI:
    :cvar I:
    """
    E = "E"
    EI = "EI"
    I = "I"


class CodingRationale(Enum):
    """
    vocSet: T19250 (C-0-T19250-cpt)
    :cvar SH:
    :cvar HL7:
    :cvar SRC:
    """
    SH = "SH"
    HL7 = "HL7"
    SRC = "SRC"


class CombinedPharmacyOrderSuspendReasonCode(Enum):
    """
    abstDomain: A19779 (C-0-T14878-A19692-A19779-cpt)
    :cvar HOSPADM:
    :cvar SALG:
    :cvar SDDI:
    :cvar DRUGHIGH:
    :cvar SDUPTHER:
    :cvar SINTOL:
    :cvar LABINT:
    :cvar PREG:
    :cvar NON_AVAIL:
    :cvar SURG:
    :cvar CLARIF:
    :cvar ALTCHOICE:
    :cvar WASHOUT:
    """
    HOSPADM = "HOSPADM"
    SALG = "SALG"
    SDDI = "SDDI"
    DRUGHIGH = "DRUGHIGH"
    SDUPTHER = "SDUPTHER"
    SINTOL = "SINTOL"
    LABINT = "LABINT"
    PREG = "PREG"
    NON_AVAIL = "NON-AVAIL"
    SURG = "SURG"
    CLARIF = "CLARIF"
    ALTCHOICE = "ALTCHOICE"
    WASHOUT = "WASHOUT"


class CommunicationFunctionType(Enum):
    """
    vocSet: T16031 (C-0-T16031-cpt)
    :cvar RCV:
    :cvar RSP:
    :cvar SND:
    """
    RCV = "RCV"
    RSP = "RSP"
    SND = "SND"


class ComplianceAlert(Enum):
    """
    specDomain: S16687 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S16687-cpt)
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    :cvar COMPLY:
    :cvar PLYDOC:
    :cvar PLYPHRM:
    :cvar ABUSE:
    :cvar FRAUD:
    """
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"
    COMPLY = "COMPLY"
    PLYDOC = "PLYDOC"
    PLYPHRM = "PLYPHRM"
    ABUSE = "ABUSE"
    FRAUD = "FRAUD"


class ComplianceDetectedIssueCode(Enum):
    """
    specDomain: S16687 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16687-cpt)
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    :cvar COMPLY:
    :cvar PLYDOC:
    :cvar PLYPHRM:
    :cvar ABUSE:
    :cvar FRAUD:
    """
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"
    COMPLY = "COMPLY"
    PLYDOC = "PLYDOC"
    PLYPHRM = "PLYPHRM"
    ABUSE = "ABUSE"
    FRAUD = "FRAUD"


class ComplianceDetectedIssueCodeDuplicateTherapyAlertByBot(Enum):
    """
    specDomain: S16688 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16687-S16688-cpt)
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    """
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"


class CompliancePackageEntityType(Enum):
    """
    specDomain: S16170 (C-0-T16040-A16041-A19867-A16143-S16144-S16170-cpt)
    :cvar BLSTRPK:
    :cvar CARD:
    :cvar COMPPKG:
    :cvar DIALPK:
    :cvar DISK:
    :cvar DOSET:
    :cvar STRIP:
    """
    BLSTRPK = "BLSTRPK"
    CARD = "CARD"
    COMPPKG = "COMPPKG"
    DIALPK = "DIALPK"
    DISK = "DISK"
    DOSET = "DOSET"
    STRIP = "STRIP"


class CompressionAlgorithm(Enum):
    """
    vocSet: T10620 (C-0-T10620-cpt)
    :cvar Z:
    :cvar DF:
    :cvar GZ:
    :cvar ZL:
    """
    Z = "Z"
    DF = "DF"
    GZ = "GZ"
    ZL = "ZL"


class ConceptCodeRelationship(Enum):
    """
    vocSet: T19363 (C-0-T19363-cpt)
    :cvar HAS_PART:
    :cvar HAS_SUBTYPE:
    :cvar SMALLER_THAN:
    """
    HAS_PART = "hasPart"
    HAS_SUBTYPE = "hasSubtype"
    SMALLER_THAN = "smallerThan"


class ConceptGenerality(Enum):
    """
    vocSet: T11033 (C-0-T11033-cpt)
    :cvar A:
    :cvar L:
    :cvar S:
    """
    A = "A"
    L = "L"
    S = "S"


class ConceptPropertyId(Enum):
    """
    vocSet: T19361 (C-0-T19361-cpt)
    :cvar OID:
    :cvar VALUE_SET_PROPERTY_ID:
    :cvar APPLIES_TO:
    :cvar HOW_APPLIES:
    :cvar INVERSE_RELATIONSHIP:
    :cvar OPEN_ISSUE:
    """
    OID = "OID"
    VALUE_SET_PROPERTY_ID = "_ValueSetPropertyId"
    APPLIES_TO = "appliesTo"
    HOW_APPLIES = "howApplies"
    INVERSE_RELATIONSHIP = "inverseRelationship"
    OPEN_ISSUE = "openIssue"


class ConceptStatus(Enum):
    """
    vocSet: T19360 (C-0-T19360-cpt)
    :cvar A:
    :cvar D:
    :cvar P:
    :cvar R:
    """
    A = "A"
    D = "D"
    P = "P"
    R = "R"


class ConditionDetectedIssueCode(Enum):
    """
    specDomain: S16665 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16665-cpt)
    :cvar DOSEHINDSA:
    :cvar DOSELINDSA:
    :cvar DOSEHINDW:
    :cvar DOSELINDW:
    :cvar COND:
    :cvar LACT:
    :cvar PREG:
    """
    DOSEHINDSA = "DOSEHINDSA"
    DOSELINDSA = "DOSELINDSA"
    DOSEHINDW = "DOSEHINDW"
    DOSELINDW = "DOSELINDW"
    COND = "COND"
    LACT = "LACT"
    PREG = "PREG"


class Conditional(Enum):
    """
    abstDomain: A17720 (C-0-T17719-A17720-cpt)
    :cvar CONFIRM:
    :cvar NOTIFY:
    """
    CONFIRM = "CONFIRM"
    NOTIFY = "NOTIFY"


class Confidentiality(Enum):
    """
    vocSet: T10228 (C-0-T10228-cpt)
    :cvar B:
    :cvar D:
    :cvar I:
    :cvar L:
    :cvar N:
    :cvar R:
    :cvar V:
    :cvar HIV:
    :cvar PSY:
    :cvar SDV:
    :cvar ETH:
    :cvar C:
    :cvar S:
    :cvar T:
    """
    B = "B"
    D = "D"
    I = "I"
    L = "L"
    N = "N"
    R = "R"
    V = "V"
    HIV = "HIV"
    PSY = "PSY"
    SDV = "SDV"
    ETH = "ETH"
    C = "C"
    S = "S"
    T = "T"


class ConfidentialityByAccessKind(Enum):
    """
    abstDomain: A10229 (C-0-T10228-A10229-cpt)
    :cvar B:
    :cvar D:
    :cvar I:
    :cvar L:
    :cvar N:
    :cvar R:
    :cvar V:
    """
    B = "B"
    D = "D"
    I = "I"
    L = "L"
    N = "N"
    R = "R"
    V = "V"


class ConfidentialityByInfoType(Enum):
    """
    abstDomain: A10240 (C-0-T10228-A10240-cpt)
    :cvar HIV:
    :cvar PSY:
    :cvar SDV:
    :cvar ETH:
    """
    HIV = "HIV"
    PSY = "PSY"
    SDV = "SDV"
    ETH = "ETH"


class ConfidentialityModifiers(Enum):
    """
    abstDomain: A10236 (C-0-T10228-A10236-cpt)
    :cvar C:
    :cvar S:
    :cvar T:
    """
    C = "C"
    S = "S"
    T = "T"


class ConrolActNullificationReasonCode(Enum):
    """
    abstDomain: A19826 (C-0-T14878-A19692-A19826-cpt)
    :cvar ALTD:
    :cvar EIE:
    """
    ALTD = "ALTD"
    EIE = "EIE"


class ConsultedPrescriberManagementCode(Enum):
    """
    specDomain: S16700 (C-0-T13953-A13954-A16695-S16696-S16700-cpt)
    :cvar VALUE_5:
    :cvar VALUE_6:
    """
    VALUE_5 = "5"
    VALUE_6 = "6"


class ContactRoleType(Enum):
    """
    abstDomain: A15920 (C-0-T12206-A15920-cpt)
    :cvar BILL:
    :cvar PAYOR:
    :cvar ORG:
    :cvar ECON:
    :cvar NOK:
    """
    BILL = "BILL"
    PAYOR = "PAYOR"
    ORG = "ORG"
    ECON = "ECON"
    NOK = "NOK"


class ContainerCap(Enum):
    """
    vocSet: T14049 (C-0-T14049-cpt)
    :cvar CHILD:
    :cvar EASY:
    :cvar FILM:
    :cvar FOIL:
    :cvar PUSH:
    :cvar SCR:
    """
    CHILD = "CHILD"
    EASY = "EASY"
    FILM = "FILM"
    FOIL = "FOIL"
    PUSH = "PUSH"
    SCR = "SCR"


class ContainerSeparator(Enum):
    """
    vocSet: T14054 (C-0-T14054-cpt)
    :cvar GEL:
    :cvar NONE_VALUE:
    """
    GEL = "GEL"
    NONE_VALUE = "NONE"


class ContentProcessingMode(Enum):
    """
    vocSet: T19823 (C-0-T19823-cpt)
    :cvar SEQL:
    :cvar UNOR:
    """
    SEQL = "SEQL"
    UNOR = "UNOR"


class ContextControl(Enum):
    """
    vocSet: T16478 (C-0-T16478-cpt)
    :cvar AN:
    :cvar AP:
    :cvar ON:
    :cvar OP:
    """
    AN = "AN"
    AP = "AP"
    ON = "ON"
    OP = "OP"


class ContextControlAdditive(Enum):
    """
    abstDomain: A18934 (C-0-T16478-A18934-cpt)
    :cvar AN:
    :cvar AP:
    """
    AN = "AN"
    AP = "AP"


class ContextControlNonPropagating(Enum):
    """
    abstDomain: A18937 (C-0-T16478-A18937-cpt)
    :cvar AN:
    :cvar ON:
    """
    AN = "AN"
    ON = "ON"


class ContextControlOverriding(Enum):
    """
    abstDomain: A18935 (C-0-T16478-A18935-cpt)
    :cvar ON:
    :cvar OP:
    """
    ON = "ON"
    OP = "OP"


class ContextControlPropagating(Enum):
    """
    abstDomain: A18936 (C-0-T16478-A18936-cpt)
    :cvar AP:
    :cvar OP:
    """
    AP = "AP"
    OP = "OP"


class ContractorProviderCodes(Enum):
    """
    specDomain: S20436 (C-0-T19465-S20434-S20436-cpt)
    :cvar VALUE_171_W00000_X:
    :cvar VALUE_171_WH0202_X:
    :cvar VALUE_171_WV0202_X:
    """
    VALUE_171_W00000_X = "171W00000X"
    VALUE_171_WH0202_X = "171WH0202X"
    VALUE_171_WV0202_X = "171WV0202X"


class Coosan(Enum):
    """
    abstDomain: A18421 (C-0-T18130-A18413-A18421-cpt)
    :cvar X_COS:
    """
    X_COS = "x-COS"


class CounselorProviderCodes(Enum):
    """
    specDomain: S20276 (C-0-T19465-S20275-S20276-cpt)
    :cvar VALUE_101_Y00000_X:
    :cvar VALUE_101_YA0400_X:
    :cvar VALUE_101_YM0800_X:
    :cvar VALUE_101_YP1600_X:
    :cvar VALUE_101_YP2500_X:
    :cvar VALUE_101_YS0200_X:
    """
    VALUE_101_Y00000_X = "101Y00000X"
    VALUE_101_YA0400_X = "101YA0400X"
    VALUE_101_YM0800_X = "101YM0800X"
    VALUE_101_YP1600_X = "101YP1600X"
    VALUE_101_YP2500_X = "101YP2500X"
    VALUE_101_YS0200_X = "101YS0200X"


class CoverageEligibilityReason(Enum):
    """
    abstDomain: A19735 (C-0-T14878-A19871-A19694-A19735-cpt)
    :cvar AGE:
    :cvar CRIME:
    :cvar DIS:
    :cvar EMPLOY:
    :cvar FINAN:
    :cvar HEALTH:
    :cvar VEHIC:
    :cvar MULTI:
    :cvar PNC:
    :cvar STATUTORY:
    :cvar WORK:
    """
    AGE = "AGE"
    CRIME = "CRIME"
    DIS = "DIS"
    EMPLOY = "EMPLOY"
    FINAN = "FINAN"
    HEALTH = "HEALTH"
    VEHIC = "VEHIC"
    MULTI = "MULTI"
    PNC = "PNC"
    STATUTORY = "STATUTORY"
    WORK = "WORK"


class CoverageRoleType(Enum):
    """
    abstDomain: A18877 (C-0-T12206-A19809-A18877-cpt)
    :cvar STUD:
    :cvar FSTUD:
    :cvar PSTUD:
    :cvar FAMDEP:
    :cvar HANDIC:
    :cvar INJ:
    :cvar SELF:
    :cvar SPON:
    """
    STUD = "STUD"
    FSTUD = "FSTUD"
    PSTUD = "PSTUD"
    FAMDEP = "FAMDEP"
    HANDIC = "HANDIC"
    INJ = "INJ"
    SELF = "SELF"
    SPON = "SPON"


class CoverageSponsorRoleType(Enum):
    """
    abstDomain: A19877 (C-0-T12206-A19690-A19877-cpt)
    :cvar FULLINS:
    :cvar SELFINS:
    """
    FULLINS = "FULLINS"
    SELFINS = "SELFINS"


class CreamDrugForm(Enum):
    """
    specDomain: S14466 (C-0-T19651-A14411-A14412-A14463-S14466-cpt)
    :cvar VAGCRM:
    :cvar VAGCRMAPL:
    :cvar CRM:
    :cvar NASCRM:
    :cvar OPCRM:
    :cvar ORCRM:
    :cvar OTCRM:
    :cvar RECCRM:
    :cvar TOPCRM:
    """
    VAGCRM = "VAGCRM"
    VAGCRMAPL = "VAGCRMAPL"
    CRM = "CRM"
    NASCRM = "NASCRM"
    OPCRM = "OPCRM"
    ORCRM = "ORCRM"
    OTCRM = "OTCRM"
    RECCRM = "RECCRM"
    TOPCRM = "TOPCRM"


class CreditCard(Enum):
    """
    abstDomain: A14811 (C-0-T13953-A13954-A14809-A14811-cpt)
    :cvar AE:
    :cvar DN:
    :cvar DV:
    :cvar MC:
    :cvar V:
    """
    AE = "AE"
    DN = "DN"
    DV = "DV"
    MC = "MC"
    V = "V"


class Cree(Enum):
    """
    abstDomain: A18136 (C-0-T18130-A18131-A18132-A18135-A18136-cpt)
    :cvar X_CRP:
    """
    X_CRP = "x-CRP"


class Cupan(Enum):
    """
    abstDomain: A18624 (C-0-T18130-A18605-A18621-A18624-cpt)
    :cvar X_CHL:
    :cvar X_CUP:
    :cvar X_LUI:
    """
    X_CHL = "x-CHL"
    X_CUP = "x-CUP"
    X_LUI = "x-LUI"


class Currency(Enum):
    """
    vocSet: T17388 (C-0-T17388-cpt)
    :cvar ARS:
    :cvar AUD:
    :cvar THB:
    :cvar BRL:
    :cvar CAD:
    :cvar DEM:
    :cvar EUR:
    :cvar FRF:
    :cvar INR:
    :cvar TRL:
    :cvar FIM:
    :cvar MXN:
    :cvar NLG:
    :cvar NZD:
    :cvar PHP:
    :cvar GBP:
    :cvar ZAR:
    :cvar RUR:
    :cvar ILS:
    :cvar ESP:
    :cvar CHF:
    :cvar TWD:
    :cvar USD:
    :cvar CLF:
    :cvar KRW:
    :cvar JPY:
    :cvar CNY:
    """
    ARS = "ARS"
    AUD = "AUD"
    THB = "THB"
    BRL = "BRL"
    CAD = "CAD"
    DEM = "DEM"
    EUR = "EUR"
    FRF = "FRF"
    INR = "INR"
    TRL = "TRL"
    FIM = "FIM"
    MXN = "MXN"
    NLG = "NLG"
    NZD = "NZD"
    PHP = "PHP"
    GBP = "GBP"
    ZAR = "ZAR"
    RUR = "RUR"
    ILS = "ILS"
    ESP = "ESP"
    CHF = "CHF"
    TWD = "TWD"
    USD = "USD"
    CLF = "CLF"
    KRW = "KRW"
    JPY = "JPY"
    CNY = "CNY"


class CustodialCareFacilityProviderCodes(Enum):
    """
    specDomain: S20761 (C-0-T19465-S20758-S20761-cpt)
    :cvar VALUE_311_Z00000_X:
    :cvar VALUE_311_ZA0620_X:
    """
    VALUE_311_Z00000_X = "311Z00000X"
    VALUE_311_ZA0620_X = "311ZA0620X"


class Dakotan(Enum):
    """
    abstDomain: A18563 (C-0-T18130-A18552-A18553-A18562-A18563-cpt)
    :cvar X_ASB:
    :cvar X_DHG:
    :cvar X_LKT:
    :cvar X_NKT:
    """
    X_ASB = "x-ASB"
    X_DHG = "x-DHG"
    X_LKT = "x-LKT"
    X_NKT = "x-NKT"


class DataTypeAddressPart(Enum):
    """
    specDomain: S10792 (C-0-T10774-A10775-S10821-S10822-S10777-S10778-S10779-S10792-cpt)
    :cvar ADXP:
    """
    ADXP = "ADXP"


class DataTypeAnnotated(Enum):
    """
    specDomain: S10845 (C-0-T10774-A10775-S10845-cpt)
    :cvar ANT_CD:
    :cvar ANT_PQ:
    :cvar ANT_ANY:
    """
    ANT_CD = "ANT&lt;CD&gt;"
    ANT_PQ = "ANT&lt;PQ&gt;"
    ANT_ANY = "ANT&lt;ANY&gt;"


class DataTypeAnnotatedConceptDescriptor(Enum):
    """
    specDomain: S10846 (C-0-T10774-A10775-S10845-S10846-cpt)
    :cvar ANT_CD:
    """
    ANT_CD = "ANT&lt;CD&gt;"


class DataTypeAnnotatedPhysicalQuantity(Enum):
    """
    specDomain: S10848 (C-0-T10774-A10775-S10845-S10848-cpt)
    :cvar ANT_PQ:
    """
    ANT_PQ = "ANT&lt;PQ&gt;"


class DataTypeBag(Enum):
    """
    specDomain: S10831 (C-0-T10774-A10775-S10831-cpt)
    :cvar BAG_CD:
    :cvar BAG_PQ:
    :cvar BAG_ANY:
    """
    BAG_CD = "BAG&lt;CD&gt;"
    BAG_PQ = "BAG&lt;PQ&gt;"
    BAG_ANY = "BAG&lt;ANY&gt;"


class DataTypeBagOfConceptDescriptors(Enum):
    """
    specDomain: S10832 (C-0-T10774-A10775-S10831-S10832-cpt)
    :cvar BAG_CD:
    """
    BAG_CD = "BAG&lt;CD&gt;"


class DataTypeBagOfPhysicalQuantities(Enum):
    """
    specDomain: S10833 (C-0-T10774-A10775-S10831-S10833-cpt)
    :cvar BAG_PQ:
    """
    BAG_PQ = "BAG&lt;PQ&gt;"


class DataTypeBinaryData(Enum):
    """
    specDomain: S10777 (C-0-T10774-A10775-S10821-S10822-S10777-cpt)
    :cvar ADXP:
    :cvar ON:
    :cvar PNXP:
    :cvar ST:
    :cvar ED:
    :cvar BIN:
    """
    ADXP = "ADXP"
    ON = "ON"
    PNXP = "PNXP"
    ST = "ST"
    ED = "ED"
    BIN = "BIN"


class DataTypeBoolean(Enum):
    """
    specDomain: S10776 (C-0-T10774-A10775-S10776-cpt)
    :cvar BL:
    """
    BL = "BL"


class DataTypeCharacterString(Enum):
    """
    specDomain: S10779 (C-0-T10774-A10775-S10821-S10822-S10777-S10778-S10779-cpt)
    :cvar ADXP:
    :cvar ON:
    :cvar PNXP:
    :cvar ST:
    """
    ADXP = "ADXP"
    ON = "ON"
    PNXP = "PNXP"
    ST = "ST"


class DataTypeCodedSimpleValue(Enum):
    """
    specDomain: S10782 (C-0-T10774-A10775-S10780-S10782-cpt)
    :cvar CS:
    """
    CS = "CS"


class DataTypeCodedValue(Enum):
    """
    specDomain: S10783 (C-0-T10774-A10775-S10780-S10783-cpt)
    :cvar CV:
    """
    CV = "CV"


class DataTypeCodedWithEquivalents(Enum):
    """
    specDomain: S10784 (C-0-T10774-A10775-S10780-S10784-cpt)
    :cvar CE:
    """
    CE = "CE"


class DataTypeConceptDescriptor(Enum):
    """
    specDomain: S10780 (C-0-T10774-A10775-S10780-cpt)
    :cvar CS:
    :cvar CV:
    :cvar CE:
    :cvar CD:
    """
    CS = "CS"
    CV = "CV"
    CE = "CE"
    CD = "CD"


class DataTypeConceptRole(Enum):
    """
    specDomain: S10781 (C-0-T10774-A10775-S10781-cpt)
    :cvar CR:
    """
    CR = "CR"


class DataTypeEncodedData(Enum):
    """
    specDomain: S10778 (C-0-T10774-A10775-S10821-S10822-S10777-S10778-cpt)
    :cvar ADXP:
    :cvar ON:
    :cvar PNXP:
    :cvar ST:
    :cvar ED:
    """
    ADXP = "ADXP"
    ON = "ON"
    PNXP = "PNXP"
    ST = "ST"
    ED = "ED"


class DataTypeEventRelatedInterval(Enum):
    """
    specDomain: S10844 (C-0-T10774-A10775-S10834-S10841-S10807-S10844-cpt)
    :cvar EIVL_TS:
    """
    EIVL_TS = "EIVL&lt;TS&gt;"


class DataTypeGeneralTimingSpecification(Enum):
    """
    specDomain: S10808 (C-0-T10774-A10775-S10834-S10841-S10807-S10808-cpt)
    :cvar GTS:
    """
    GTS = "GTS"


class DataTypeHistorical(Enum):
    """
    specDomain: S10850 (C-0-T10774-A10775-S10850-cpt)
    :cvar HXIT_AD:
    :cvar HXIT_ANY:
    """
    HXIT_AD = "HXIT&lt;AD&gt;"
    HXIT_ANY = "HXIT&lt;ANY&gt;"


class DataTypeHistoricalAddress(Enum):
    """
    specDomain: S10851 (C-0-T10774-A10775-S10850-S10851-cpt)
    :cvar HXIT_AD:
    """
    HXIT_AD = "HXIT&lt;AD&gt;"


class DataTypeHistoryOfAddress(Enum):
    """
    specDomain: S10813 (C-0-T10774-A10775-S10801-S10810-S10811-S10812-S10813-cpt)
    :cvar HIST_AD:
    """
    HIST_AD = "HIST&lt;AD&gt;"


class DataTypeInstanceIdentifier(Enum):
    """
    specDomain: S10785 (C-0-T10774-A10775-S10785-cpt)
    :cvar II:
    """
    II = "II"


class DataTypeIntegerNumber(Enum):
    """
    specDomain: S10795 (C-0-T10774-A10775-A10794-S10795-cpt)
    :cvar INT_VALUE:
    """
    INT_VALUE = "INT"


class DataTypeInterval(Enum):
    """
    specDomain: S10834 (C-0-T10774-A10775-S10834-cpt)
    :cvar IVL_INT:
    :cvar UVP_IVL_PQ:
    :cvar IVL_PQ:
    :cvar EIVL_TS:
    :cvar GTS:
    :cvar PIVL_TS:
    :cvar SET_TS:
    :cvar IVL_TS:
    :cvar IVL_REAL:
    :cvar IVL_QTY:
    """
    IVL_INT = "IVL&lt;INT&gt;"
    UVP_IVL_PQ = "UVP&lt;IVL&lt;PQ&gt;&gt;"
    IVL_PQ = "IVL&lt;PQ&gt;"
    EIVL_TS = "EIVL&lt;TS&gt;"
    GTS = "GTS"
    PIVL_TS = "PIVL&lt;TS&gt;"
    SET_TS = "SET&lt;TS&gt;"
    IVL_TS = "IVL&lt;TS&gt;"
    IVL_REAL = "IVL&lt;REAL&gt;"
    IVL_QTY = "IVL&lt;QTY&gt;"


class DataTypeIntervalOfIntegerNumbers(Enum):
    """
    specDomain: S10835 (C-0-T10774-A10775-S10834-S10835-cpt)
    :cvar IVL_INT:
    """
    IVL_INT = "IVL&lt;INT&gt;"


class DataTypeIntervalOfPhysicalQuantities(Enum):
    """
    specDomain: S10839 (C-0-T10774-A10775-S10834-S10839-cpt)
    :cvar UVP_IVL_PQ:
    :cvar IVL_PQ:
    """
    UVP_IVL_PQ = "UVP&lt;IVL&lt;PQ&gt;&gt;"
    IVL_PQ = "IVL&lt;PQ&gt;"


class DataTypeIntervalOfPointsInTime(Enum):
    """
    specDomain: S10841 (C-0-T10774-A10775-S10834-S10841-cpt)
    :cvar EIVL_TS:
    :cvar GTS:
    :cvar PIVL_TS:
    :cvar SET_TS:
    :cvar IVL_TS:
    """
    EIVL_TS = "EIVL&lt;TS&gt;"
    GTS = "GTS"
    PIVL_TS = "PIVL&lt;TS&gt;"
    SET_TS = "SET&lt;TS&gt;"
    IVL_TS = "IVL&lt;TS&gt;"


class DataTypeIntervalOfRealNumbers(Enum):
    """
    specDomain: S10837 (C-0-T10774-A10775-S10834-S10837-cpt)
    :cvar IVL_REAL:
    """
    IVL_REAL = "IVL&lt;REAL&gt;"


class DataTypeMonetaryAmount(Enum):
    """
    specDomain: S10798 (C-0-T10774-A10775-A10794-S10798-cpt)
    :cvar MO:
    """
    MO = "MO"


class DataTypeNonParametricProbabilityDistribution(Enum):
    """
    specDomain: S10815 (C-0-T10774-A10775-S10801-S10814-S10815-cpt)
    :cvar NPPD_ANY:
    """
    NPPD_ANY = "NPPD&lt;ANY&gt;"


class DataTypeNonParametricProbabilityDistributionOfConceptDescriptor(Enum):
    """
    specDomain: S10862 (C-0-T10774-A10775-S10801-S10816-S10862-cpt)
    :cvar NPPD_CD:
    """
    NPPD_CD = "NPPD&lt;CD&gt;"


class DataTypeNonParametricProbabilityDistributionOfIntervalOfPhysicalQuantities(Enum):
    """
    specDomain: S10863 (C-0-T10774-A10775-S10801-S10819-S10863-cpt)
    :cvar NPPD_IVL_PQ:
    """
    NPPD_IVL_PQ = "NPPD&lt;IVL&lt;PQ&gt;&gt;"


class DataTypeObjectIdentifier(Enum):
    """
    specDomain: S10786 (C-0-T10774-A10775-S10786-cpt)
    :cvar OID:
    """
    OID = "OID"


class DataTypeOrganizationName(Enum):
    """
    specDomain: S10793 (C-0-T10774-A10775-S10821-S10822-S10777-S10778-S10779-S10793-cpt)
    :cvar ON:
    """
    ON = "ON"


class DataTypeParametricProbabilityDistribution(Enum):
    """
    specDomain: S10864 (C-0-T10774-A10775-A10794-S10864-cpt)
    :cvar PPD_QTY:
    """
    PPD_QTY = "PPD&lt;QTY&gt;"


class DataTypeParametricProbabilityDistributionOfPhysicalQuantities(Enum):
    """
    specDomain: S10866 (C-0-T10774-A10775-A10794-S10797-S10866-cpt)
    :cvar PPD_PQ:
    """
    PPD_PQ = "PPD&lt;PQ&gt;"


class DataTypeParametricProbabilityDistributionOfRealNumbers(Enum):
    """
    specDomain: S10865 (C-0-T10774-A10775-A10794-S10796-S10865-cpt)
    :cvar PPD_REAL:
    """
    PPD_REAL = "PPD&lt;REAL&gt;"


class DataTypePeriodicIntervalOfTime(Enum):
    """
    specDomain: S10843 (C-0-T10774-A10775-S10834-S10841-S10807-S10843-cpt)
    :cvar PIVL_TS:
    """
    PIVL_TS = "PIVL&lt;TS&gt;"


class DataTypePersonNamePart(Enum):
    """
    specDomain: S10790 (C-0-T10774-A10775-S10821-S10822-S10777-S10778-S10779-S10790-cpt)
    :cvar PNXP:
    """
    PNXP = "PNXP"


class DataTypePersonNameType(Enum):
    """
    specDomain: S10789 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-S10827-S10828-S10789-cpt)
    :cvar PN:
    """
    PN = "PN"


class DataTypePhysicalQuantity(Enum):
    """
    specDomain: S10797 (C-0-T10774-A10775-A10794-S10797-cpt)
    :cvar PPD_PQ:
    :cvar PQ:
    """
    PPD_PQ = "PPD&lt;PQ&gt;"
    PQ = "PQ"


class DataTypePointInTime(Enum):
    """
    specDomain: S10799 (C-0-T10774-A10775-A10794-S10799-cpt)
    :cvar TS:
    """
    TS = "TS"


class DataTypePostalAndResidentialAddress(Enum):
    """
    specDomain: S10791 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-S10827-S10829-S10791-cpt)
    :cvar AD:
    """
    AD = "AD"


class DataTypeRatio(Enum):
    """
    specDomain: S10800 (C-0-T10774-A10775-A10794-S10800-cpt)
    :cvar RTO:
    """
    RTO = "RTO"


class DataTypeRealNumber(Enum):
    """
    specDomain: S10796 (C-0-T10774-A10775-A10794-S10796-cpt)
    :cvar PPD_REAL:
    :cvar REAL:
    """
    PPD_REAL = "PPD&lt;REAL&gt;"
    REAL = "REAL"


class DataTypeSequence(Enum):
    """
    specDomain: S10821 (C-0-T10774-A10775-S10821-cpt)
    :cvar ADXP:
    :cvar ON:
    :cvar PNXP:
    :cvar ST:
    :cvar ED:
    :cvar BIN:
    :cvar LIST_BL:
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    :cvar LIST_ED:
    :cvar LIST_BIN:
    :cvar LIST_LIST_BL:
    :cvar LIST_LIST_ANY:
    :cvar LIST_ANY:
    """
    ADXP = "ADXP"
    ON = "ON"
    PNXP = "PNXP"
    ST = "ST"
    ED = "ED"
    BIN = "BIN"
    LIST_BL = "LIST&lt;BL&gt;"
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"
    LIST_ED = "LIST&lt;ED&gt;"
    LIST_BIN = "LIST&lt;BIN&gt;"
    LIST_LIST_BL = "LIST&lt;LIST&lt;BL&gt;&gt;"
    LIST_LIST_ANY = "LIST&lt;LIST&lt;ANY&gt;&gt;"
    LIST_ANY = "LIST&lt;ANY&gt;"


class DataTypeSequenceOfBinaryData(Enum):
    """
    specDomain: S10825 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    :cvar LIST_ED:
    :cvar LIST_BIN:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"
    LIST_ED = "LIST&lt;ED&gt;"
    LIST_BIN = "LIST&lt;BIN&gt;"


class DataTypeSequenceOfBooleans(Enum):
    """
    specDomain: S10822 (C-0-T10774-A10775-S10821-S10822-cpt)
    :cvar ADXP:
    :cvar ON:
    :cvar PNXP:
    :cvar ST:
    :cvar ED:
    :cvar BIN:
    :cvar LIST_BL:
    """
    ADXP = "ADXP"
    ON = "ON"
    PNXP = "PNXP"
    ST = "ST"
    ED = "ED"
    BIN = "BIN"
    LIST_BL = "LIST&lt;BL&gt;"


class DataTypeSequenceOfCharacterStrings(Enum):
    """
    specDomain: S10827 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-S10827-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"


class DataTypeSequenceOfEncodedData(Enum):
    """
    specDomain: S10826 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    :cvar LIST_ED:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"
    LIST_ED = "LIST&lt;ED&gt;"


class DataTypeSequenceOfPersonNameParts(Enum):
    """
    specDomain: S10828 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-S10827-S10828-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"


class DataTypeSequenceOfPostalAddressParts(Enum):
    """
    specDomain: S10829 (C-0-T10774-A10775-S10821-S10823-S10824-S10825-S10826-S10827-S10829-cpt)
    :cvar AD:
    :cvar LIST_ADXP:
    """
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"


class DataTypeSequenceOfSequenceOfBooleans(Enum):
    """
    specDomain: S10824 (C-0-T10774-A10775-S10821-S10823-S10824-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    :cvar LIST_ED:
    :cvar LIST_BIN:
    :cvar LIST_LIST_BL:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"
    LIST_ED = "LIST&lt;ED&gt;"
    LIST_BIN = "LIST&lt;BIN&gt;"
    LIST_LIST_BL = "LIST&lt;LIST&lt;BL&gt;&gt;"


class DataTypeSequenceOfSequencesOfDataValues(Enum):
    """
    specDomain: S10823 (C-0-T10774-A10775-S10821-S10823-cpt)
    :cvar PN:
    :cvar LIST_PNXP:
    :cvar AD:
    :cvar LIST_ADXP:
    :cvar LIST_ST:
    :cvar LIST_ED:
    :cvar LIST_BIN:
    :cvar LIST_LIST_BL:
    :cvar LIST_LIST_ANY:
    """
    PN = "PN"
    LIST_PNXP = "LIST&lt;PNXP&gt;"
    AD = "AD"
    LIST_ADXP = "LIST&lt;ADXP&gt;"
    LIST_ST = "LIST&lt;ST&gt;"
    LIST_ED = "LIST&lt;ED&gt;"
    LIST_BIN = "LIST&lt;BIN&gt;"
    LIST_LIST_BL = "LIST&lt;LIST&lt;BL&gt;&gt;"
    LIST_LIST_ANY = "LIST&lt;LIST&lt;ANY&gt;&gt;"


class DataTypeSet(Enum):
    """
    specDomain: S10801 (C-0-T10774-A10775-S10801-cpt)
    :cvar SET_ST:
    :cvar SET_CS:
    :cvar SET_CV:
    :cvar SET_CE:
    :cvar NPPD_CD:
    :cvar SET_UVP_CD:
    :cvar SET_CD:
    :cvar SET_INT:
    :cvar IVL_INT:
    :cvar NPPD_IVL_PQ:
    :cvar SET_UVP_IVL_PQ:
    :cvar SET_IVL_PQ:
    :cvar SET_PQ:
    :cvar SET_REAL:
    :cvar IVL_REAL:
    :cvar HIST_AD:
    :cvar SET_HXIT_AD:
    :cvar SET_AD:
    :cvar SET_LIST_ST:
    :cvar NPPD_ANY:
    :cvar SET_UVP_ANY:
    :cvar SET_ANY:
    """
    SET_ST = "SET&lt;ST&gt;"
    SET_CS = "SET&lt;CS&gt;"
    SET_CV = "SET&lt;CV&gt;"
    SET_CE = "SET&lt;CE&gt;"
    NPPD_CD = "NPPD&lt;CD&gt;"
    SET_UVP_CD = "SET&lt;UVP&lt;CD&gt;&gt;"
    SET_CD = "SET&lt;CD&gt;"
    SET_INT = "SET&lt;INT&gt;"
    IVL_INT = "IVL&lt;INT&gt;"
    NPPD_IVL_PQ = "NPPD&lt;IVL&lt;PQ&gt;&gt;"
    SET_UVP_IVL_PQ = "SET&lt;UVP&lt;IVL&lt;PQ&gt;&gt;&gt;"
    SET_IVL_PQ = "SET&lt;IVL&lt;PQ&gt;&gt;"
    SET_PQ = "SET&lt;PQ&gt;"
    SET_REAL = "SET&lt;REAL&gt;"
    IVL_REAL = "IVL&lt;REAL&gt;"
    HIST_AD = "HIST&lt;AD&gt;"
    SET_HXIT_AD = "SET&lt;HXIT&lt;AD&gt;&gt;"
    SET_AD = "SET&lt;AD&gt;"
    SET_LIST_ST = "SET&lt;LIST&lt;ST&gt;&gt;"
    NPPD_ANY = "NPPD&lt;ANY&gt;"
    SET_UVP_ANY = "SET&lt;UVP&lt;ANY&gt;&gt;"
    SET_ANY = "SET&lt;ANY&gt;"


class DataTypeSetOfAddresses(Enum):
    """
    specDomain: S10811 (C-0-T10774-A10775-S10801-S10810-S10811-cpt)
    :cvar HIST_AD:
    :cvar SET_HXIT_AD:
    :cvar SET_AD:
    """
    HIST_AD = "HIST&lt;AD&gt;"
    SET_HXIT_AD = "SET&lt;HXIT&lt;AD&gt;&gt;"
    SET_AD = "SET&lt;AD&gt;"


class DataTypeSetOfCharacterStrings(Enum):
    """
    specDomain: S10809 (C-0-T10774-A10775-S10801-S10809-cpt)
    :cvar SET_ST:
    """
    SET_ST = "SET&lt;ST&gt;"


class DataTypeSetOfCodedSimpleValue(Enum):
    """
    specDomain: S10803 (C-0-T10774-A10775-S10801-S10802-S10803-cpt)
    :cvar SET_CS:
    """
    SET_CS = "SET&lt;CS&gt;"


class DataTypeSetOfCodedValue(Enum):
    """
    specDomain: S10804 (C-0-T10774-A10775-S10801-S10802-S10804-cpt)
    :cvar SET_CV:
    """
    SET_CV = "SET&lt;CV&gt;"


class DataTypeSetOfCodedWithEquivalents(Enum):
    """
    specDomain: S10805 (C-0-T10774-A10775-S10801-S10802-S10805-cpt)
    :cvar SET_CE:
    """
    SET_CE = "SET&lt;CE&gt;"


class DataTypeSetOfConceptDescriptors(Enum):
    """
    specDomain: S10802 (C-0-T10774-A10775-S10801-S10802-cpt)
    :cvar SET_CS:
    :cvar SET_CV:
    :cvar SET_CE:
    :cvar NPPD_CD:
    :cvar SET_UVP_CD:
    :cvar SET_CD:
    """
    SET_CS = "SET&lt;CS&gt;"
    SET_CV = "SET&lt;CV&gt;"
    SET_CE = "SET&lt;CE&gt;"
    NPPD_CD = "NPPD&lt;CD&gt;"
    SET_UVP_CD = "SET&lt;UVP&lt;CD&gt;&gt;"
    SET_CD = "SET&lt;CD&gt;"


class DataTypeSetOfHistoricalAddresses(Enum):
    """
    specDomain: S10812 (C-0-T10774-A10775-S10801-S10810-S10811-S10812-cpt)
    :cvar HIST_AD:
    :cvar SET_HXIT_AD:
    """
    HIST_AD = "HIST&lt;AD&gt;"
    SET_HXIT_AD = "SET&lt;HXIT&lt;AD&gt;&gt;"


class DataTypeSetOfIntegerNumbers(Enum):
    """
    specDomain: S10867 (C-0-T10774-A10775-S10801-S10867-cpt)
    :cvar SET_INT:
    :cvar IVL_INT:
    """
    SET_INT = "SET&lt;INT&gt;"
    IVL_INT = "IVL&lt;INT&gt;"


class DataTypeSetOfIntervalsOfPhysicalQuantitiy(Enum):
    """
    specDomain: S10869 (C-0-T10774-A10775-S10801-S10869-cpt)
    :cvar NPPD_IVL_PQ:
    :cvar SET_UVP_IVL_PQ:
    :cvar SET_IVL_PQ:
    """
    NPPD_IVL_PQ = "NPPD&lt;IVL&lt;PQ&gt;&gt;"
    SET_UVP_IVL_PQ = "SET&lt;UVP&lt;IVL&lt;PQ&gt;&gt;&gt;"
    SET_IVL_PQ = "SET&lt;IVL&lt;PQ&gt;&gt;"


class DataTypeSetOfPhysicalQuantities(Enum):
    """
    specDomain: S10818 (C-0-T10774-A10775-S10801-S10818-cpt)
    :cvar SET_PQ:
    """
    SET_PQ = "SET&lt;PQ&gt;"


class DataTypeSetOfPointsInTime(Enum):
    """
    specDomain: S10807 (C-0-T10774-A10775-S10834-S10841-S10807-cpt)
    :cvar EIVL_TS:
    :cvar GTS:
    :cvar PIVL_TS:
    :cvar SET_TS:
    """
    EIVL_TS = "EIVL&lt;TS&gt;"
    GTS = "GTS"
    PIVL_TS = "PIVL&lt;TS&gt;"
    SET_TS = "SET&lt;TS&gt;"


class DataTypeSetOfRealNumbers(Enum):
    """
    specDomain: S10868 (C-0-T10774-A10775-S10801-S10868-cpt)
    :cvar SET_REAL:
    :cvar IVL_REAL:
    """
    SET_REAL = "SET&lt;REAL&gt;"
    IVL_REAL = "IVL&lt;REAL&gt;"


class DataTypeSetOfSequencesOfCharacterStrings(Enum):
    """
    specDomain: S10810 (C-0-T10774-A10775-S10801-S10810-cpt)
    :cvar HIST_AD:
    :cvar SET_HXIT_AD:
    :cvar SET_AD:
    :cvar SET_LIST_ST:
    """
    HIST_AD = "HIST&lt;AD&gt;"
    SET_HXIT_AD = "SET&lt;HXIT&lt;AD&gt;&gt;"
    SET_AD = "SET&lt;AD&gt;"
    SET_LIST_ST = "SET&lt;LIST&lt;ST&gt;&gt;"


class DataTypeSetOfUncertainProbabilisticConceptDescriptor(Enum):
    """
    specDomain: S10816 (C-0-T10774-A10775-S10801-S10816-cpt)
    :cvar NPPD_CD:
    :cvar SET_UVP_CD:
    """
    NPPD_CD = "NPPD&lt;CD&gt;"
    SET_UVP_CD = "SET&lt;UVP&lt;CD&gt;&gt;"


class DataTypeSetOfUncertainProbabilisticIntervalOfPhysicalQuantities(Enum):
    """
    specDomain: S10819 (C-0-T10774-A10775-S10801-S10819-cpt)
    :cvar NPPD_IVL_PQ:
    :cvar SET_UVP_IVL_PQ:
    """
    NPPD_IVL_PQ = "NPPD&lt;IVL&lt;PQ&gt;&gt;"
    SET_UVP_IVL_PQ = "SET&lt;UVP&lt;IVL&lt;PQ&gt;&gt;&gt;"


class DataTypeSetOfUncertainValueProbabilistic(Enum):
    """
    specDomain: S10814 (C-0-T10774-A10775-S10801-S10814-cpt)
    :cvar NPPD_ANY:
    :cvar SET_UVP_ANY:
    """
    NPPD_ANY = "NPPD&lt;ANY&gt;"
    SET_UVP_ANY = "SET&lt;UVP&lt;ANY&gt;&gt;"


class DataTypeTelecommunicationAddress(Enum):
    """
    specDomain: S10787 (C-0-T10774-A10775-S10788-S10787-cpt)
    :cvar TEL:
    """
    TEL = "TEL"


class DataTypeUncertainNarrativeConceptDescriptor(Enum):
    """
    specDomain: S10854 (C-0-T10774-A10775-S10853-S10854-cpt)
    :cvar UVN_CD:
    """
    UVN_CD = "UVN&lt;CD&gt;"


class DataTypeUncertainProbabilisticConceptDescriptor(Enum):
    """
    specDomain: S10857 (C-0-T10774-A10775-S10856-S10857-cpt)
    :cvar UVP_CD:
    """
    UVP_CD = "UVP&lt;CD&gt;"


class DataTypeUncertainProbabilisticIntervalOfPhysicalQuantities(Enum):
    """
    specDomain: S10859 (C-0-T10774-A10775-S10856-S10859-cpt)
    :cvar UVP_IVL_PQ:
    """
    UVP_IVL_PQ = "UVP&lt;IVL&lt;PQ&gt;&gt;"


class DataTypeUncertainValueNarrative(Enum):
    """
    specDomain: S10853 (C-0-T10774-A10775-S10853-cpt)
    :cvar UVN_CD:
    :cvar UVN_ANY:
    """
    UVN_CD = "UVN&lt;CD&gt;"
    UVN_ANY = "UVN&lt;ANY&gt;"


class DataTypeUncertainValueProbabilistic(Enum):
    """
    specDomain: S10856 (C-0-T10774-A10775-S10856-cpt)
    :cvar UVP_CD:
    :cvar UVP_IVL_PQ:
    :cvar UVP_ANY:
    """
    UVP_CD = "UVP&lt;CD&gt;"
    UVP_IVL_PQ = "UVP&lt;IVL&lt;PQ&gt;&gt;"
    UVP_ANY = "UVP&lt;ANY&gt;"


class DataTypeUniversalResourceLocator(Enum):
    """
    specDomain: S10788 (C-0-T10774-A10775-S10788-cpt)
    :cvar TEL:
    :cvar URL:
    """
    TEL = "TEL"
    URL = "URL"


class DecisionObservationMethod(Enum):
    """
    abstDomain: A19378 (C-0-T14079-A19378-cpt)
    :cvar ALGM:
    :cvar BYCL:
    :cvar GINT:
    """
    ALGM = "ALGM"
    BYCL = "BYCL"
    GINT = "GINT"


class DedicatedNonClinicalLocationRoleType(Enum):
    """
    abstDomain: A19452 (C-0-T12206-A17660-A19450-A19452-cpt)
    :cvar MOBL:
    :cvar AMB:
    :cvar DADDR:
    :cvar PHARM:
    """
    MOBL = "MOBL"
    AMB = "AMB"
    DADDR = "DADDR"
    PHARM = "PHARM"


class Delawaran(Enum):
    """
    abstDomain: A18184 (C-0-T18130-A18131-A18132-A18171-A18184-cpt)
    :cvar X_DEL:
    """
    X_DEL = "x-DEL"


class DeliveryAddressLine(Enum):
    """
    specDomain: S17887 (C-0-T10642-S17887-cpt)
    :cvar DAL:
    :cvar DINSTA:
    :cvar DINSTQ:
    :cvar DINST:
    :cvar DMOD:
    :cvar DMODID:
    """
    DAL = "DAL"
    DINSTA = "DINSTA"
    DINSTQ = "DINSTQ"
    DINST = "DINST"
    DMOD = "DMOD"
    DMODID = "DMODID"


class DeltaCalifornia(Enum):
    """
    abstDomain: A18291 (C-0-T18130-A18241-A18274-A18275-A18291-cpt)
    :cvar X_DIH:
    :cvar X_COC:
    """
    X_DIH = "x-DIH"
    X_COC = "x-COC"


class DentalProvidersProviderCodes(Enum):
    """
    specDomain: S20318 (C-0-T19465-S20318-cpt)
    :cvar VALUE_122300000_X:
    :cvar VALUE_1223_D0001_X:
    :cvar VALUE_1223_E0200_X:
    :cvar VALUE_1223_G0001_X:
    :cvar VALUE_1223_P0106_X:
    :cvar VALUE_1223_X0008_X:
    :cvar VALUE_1223_S0112_X:
    :cvar VALUE_1223_X0400_X:
    :cvar VALUE_1223_P0221_X:
    :cvar VALUE_1223_P0300_X:
    :cvar VALUE_1223_P0700_X:
    :cvar VALUE_120000000_X:
    :cvar VALUE_126800000_X:
    :cvar VALUE_124_Q00000_X:
    :cvar VALUE_126900000_X:
    :cvar VALUE_122400000_X:
    """
    VALUE_122300000_X = "122300000X"
    VALUE_1223_D0001_X = "1223D0001X"
    VALUE_1223_E0200_X = "1223E0200X"
    VALUE_1223_G0001_X = "1223G0001X"
    VALUE_1223_P0106_X = "1223P0106X"
    VALUE_1223_X0008_X = "1223X0008X"
    VALUE_1223_S0112_X = "1223S0112X"
    VALUE_1223_X0400_X = "1223X0400X"
    VALUE_1223_P0221_X = "1223P0221X"
    VALUE_1223_P0300_X = "1223P0300X"
    VALUE_1223_P0700_X = "1223P0700X"
    VALUE_120000000_X = "120000000X"
    VALUE_126800000_X = "126800000X"
    VALUE_124_Q00000_X = "124Q00000X"
    VALUE_126900000_X = "126900000X"
    VALUE_122400000_X = "122400000X"


class DentalServiceProviderHipaa(Enum):
    """
    abstDomain: A16460 (C-0-T13129-A13130-A16460-cpt)
    :cvar VALUE_1327_D0700_N:
    :cvar VALUE_122300000_N:
    :cvar VALUE_1223_D0001_Y:
    :cvar VALUE_1223_E0200_Y:
    :cvar VALUE_1223_X0400_Y:
    :cvar VALUE_1223_P0106_Y:
    :cvar VALUE_1223_P0221_Y:
    :cvar VALUE_1223_P0300_Y:
    :cvar VALUE_1223_S0112_Y:
    :cvar VALUE_126800000_N:
    :cvar VALUE_124_Q00000_N:
    :cvar VALUE_126900000_N:
    """
    VALUE_1327_D0700_N = "1327D0700N"
    VALUE_122300000_N = "122300000N"
    VALUE_1223_D0001_Y = "1223D0001Y"
    VALUE_1223_E0200_Y = "1223E0200Y"
    VALUE_1223_X0400_Y = "1223X0400Y"
    VALUE_1223_P0106_Y = "1223P0106Y"
    VALUE_1223_P0221_Y = "1223P0221Y"
    VALUE_1223_P0300_Y = "1223P0300Y"
    VALUE_1223_S0112_Y = "1223S0112Y"
    VALUE_126800000_N = "126800000N"
    VALUE_124_Q00000_N = "124Q00000N"
    VALUE_126900000_N = "126900000N"


class DentistHipaa(Enum):
    """
    specDomain: S13188 (C-0-T13129-A13130-A16460-S13188-cpt)
    :cvar VALUE_1327_D0700_N:
    :cvar VALUE_122300000_N:
    :cvar VALUE_1223_D0001_Y:
    :cvar VALUE_1223_E0200_Y:
    :cvar VALUE_1223_X0400_Y:
    :cvar VALUE_1223_P0106_Y:
    :cvar VALUE_1223_P0221_Y:
    :cvar VALUE_1223_P0300_Y:
    :cvar VALUE_1223_S0112_Y:
    """
    VALUE_1327_D0700_N = "1327D0700N"
    VALUE_122300000_N = "122300000N"
    VALUE_1223_D0001_Y = "1223D0001Y"
    VALUE_1223_E0200_Y = "1223E0200Y"
    VALUE_1223_X0400_Y = "1223X0400Y"
    VALUE_1223_P0106_Y = "1223P0106Y"
    VALUE_1223_P0221_Y = "1223P0221Y"
    VALUE_1223_P0300_Y = "1223P0300Y"
    VALUE_1223_S0112_Y = "1223S0112Y"


class DentistProviderCodes(Enum):
    """
    specDomain: S20322 (C-0-T19465-S20318-S20322-cpt)
    :cvar VALUE_122300000_X:
    :cvar VALUE_1223_D0001_X:
    :cvar VALUE_1223_E0200_X:
    :cvar VALUE_1223_G0001_X:
    :cvar VALUE_1223_P0106_X:
    :cvar VALUE_1223_X0008_X:
    :cvar VALUE_1223_S0112_X:
    :cvar VALUE_1223_X0400_X:
    :cvar VALUE_1223_P0221_X:
    :cvar VALUE_1223_P0300_X:
    :cvar VALUE_1223_P0700_X:
    """
    VALUE_122300000_X = "122300000X"
    VALUE_1223_D0001_X = "1223D0001X"
    VALUE_1223_E0200_X = "1223E0200X"
    VALUE_1223_G0001_X = "1223G0001X"
    VALUE_1223_P0106_X = "1223P0106X"
    VALUE_1223_X0008_X = "1223X0008X"
    VALUE_1223_S0112_X = "1223S0112X"
    VALUE_1223_X0400_X = "1223X0400X"
    VALUE_1223_P0221_X = "1223P0221X"
    VALUE_1223_P0300_X = "1223P0300X"
    VALUE_1223_P0700_X = "1223P0700X"


class DependentCoveredPartyRoleType(Enum):
    """
    abstDomain: A19815 (C-0-T12206-A19809-A19805-A19815-cpt)
    :cvar STUD:
    :cvar FSTUD:
    :cvar PSTUD:
    :cvar COCBEN:
    :cvar DIFFABL:
    :cvar WARD:
    """
    STUD = "STUD"
    FSTUD = "FSTUD"
    PSTUD = "PSTUD"
    COCBEN = "COCBEN"
    DIFFABL = "DIFFABL"
    WARD = "WARD"


class DermatologyProviderCodes(Enum):
    """
    specDomain: S20106 (C-0-T19465-S20096-S20106-cpt)
    :cvar VALUE_207_N00000_X:
    :cvar VALUE_207_NI0002_X:
    :cvar VALUE_207_NS0135_X:
    :cvar VALUE_207_ND0900_X:
    :cvar VALUE_207_ND0101_X:
    :cvar VALUE_207_NP0225_X:
    """
    VALUE_207_N00000_X = "207N00000X"
    VALUE_207_NI0002_X = "207NI0002X"
    VALUE_207_NS0135_X = "207NS0135X"
    VALUE_207_ND0900_X = "207ND0900X"
    VALUE_207_ND0101_X = "207ND0101X"
    VALUE_207_NP0225_X = "207NP0225X"


class DeviceAlertLevel(Enum):
    """
    vocSet: T14066 (C-0-T14066-cpt)
    :cvar C:
    :cvar N:
    :cvar S:
    :cvar W:
    """
    C = "C"
    N = "N"
    S = "S"
    W = "W"


class Dhegiha(Enum):
    """
    abstDomain: A18580 (C-0-T18130-A18552-A18553-A18562-A18580-cpt)
    :cvar X_KAA:
    :cvar X_OMA:
    :cvar X_OSA:
    :cvar X_QUA:
    """
    X_KAA = "x-KAA"
    X_OMA = "x-OMA"
    X_OSA = "x-OSA"
    X_QUA = "x-QUA"


class DiagTherPracticeSetting(Enum):
    """
    specDomain: S10902 (C-0-T12206-A17660-A19450-A10588-S10902-cpt)
    :cvar CVDX:
    :cvar CATH:
    :cvar ECHO:
    :cvar GIDX:
    :cvar VALUE_261_QE0800_N:
    :cvar ENDOS:
    :cvar RADDX:
    :cvar RNEU:
    :cvar VALUE_261_QX0203_N:
    :cvar RADO:
    :cvar DX:
    """
    CVDX = "CVDX"
    CATH = "CATH"
    ECHO = "ECHO"
    GIDX = "GIDX"
    VALUE_261_QE0800_N = "261QE0800N"
    ENDOS = "ENDOS"
    RADDX = "RADDX"
    RNEU = "RNEU"
    VALUE_261_QX0203_N = "261QX0203N"
    RADO = "RADO"
    DX = "DX"


class Diegueno(Enum):
    """
    abstDomain: A18292 (C-0-T18130-A18241-A18274-A18275-A18291-A18292-cpt)
    :cvar X_DIH:
    """
    X_DIH = "x-DIH"


class DietaryandNutritionalServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20334 (C-0-T19465-S20334-cpt)
    :cvar VALUE_133_V00000_X:
    :cvar VALUE_133_VN1006_X:
    :cvar VALUE_133_VN1004_X:
    :cvar VALUE_133_VN1005_X:
    :cvar VALUE_133_N00000_X:
    :cvar VALUE_133_NN1002_X:
    :cvar VALUE_130000000_X:
    :cvar VALUE_132700000_X:
    :cvar VALUE_136_A00000_X:
    """
    VALUE_133_V00000_X = "133V00000X"
    VALUE_133_VN1006_X = "133VN1006X"
    VALUE_133_VN1004_X = "133VN1004X"
    VALUE_133_VN1005_X = "133VN1005X"
    VALUE_133_N00000_X = "133N00000X"
    VALUE_133_NN1002_X = "133NN1002X"
    VALUE_130000000_X = "130000000X"
    VALUE_132700000_X = "132700000X"
    VALUE_136_A00000_X = "136A00000X"


class DietitianRegisteredProviderCodes(Enum):
    """
    specDomain: S20337 (C-0-T19465-S20334-S20337-cpt)
    :cvar VALUE_133_V00000_X:
    :cvar VALUE_133_VN1006_X:
    :cvar VALUE_133_VN1004_X:
    :cvar VALUE_133_VN1005_X:
    """
    VALUE_133_V00000_X = "133V00000X"
    VALUE_133_VN1006_X = "133VN1006X"
    VALUE_133_VN1004_X = "133VN1004X"
    VALUE_133_VN1005_X = "133VN1005X"


class Diffusion(Enum):
    """
    abstDomain: A14584 (C-0-T14581-A16931-A14584-cpt)
    :cvar EXTCORPDIF:
    :cvar HEMODIFF:
    :cvar TRNSDERMD:
    """
    EXTCORPDIF = "EXTCORPDIF"
    HEMODIFF = "HEMODIFF"
    TRNSDERMD = "TRNSDERMD"


class DiseaseProgram(Enum):
    """
    specDomain: S22133 (C-0-T13953-A13954-A19855-A19858-S19718-S22133-cpt)
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    """
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"


class Dissolve(Enum):
    """
    abstDomain: A14586 (C-0-T14581-A16931-A14586-cpt)
    :cvar DISSOLVE:
    :cvar SL:
    """
    DISSOLVE = "DISSOLVE"
    SL = "SL"


class DocumentCompletion(Enum):
    """
    vocSet: T271 (C-0-T271-cpt)
    :cvar AU:
    :cvar DI:
    :cvar DO:
    :cvar IP:
    :cvar IN_VALUE:
    :cvar LA:
    :cvar PA:
    """
    AU = "AU"
    DI = "DI"
    DO = "DO"
    IP = "IP"
    IN_VALUE = "IN"
    LA = "LA"
    PA = "PA"


class DocumentStorage(Enum):
    """
    vocSet: T275 (C-0-T275-cpt)
    :cvar AC:
    :cvar AA:
    :cvar AR:
    :cvar PU:
    """
    AC = "AC"
    AA = "AA"
    AR = "AR"
    PU = "PU"


class DocumentStorageActive(Enum):
    """
    specDomain: S10584 (C-0-T275-S10584-cpt)
    :cvar AC:
    :cvar AA:
    """
    AC = "AC"
    AA = "AA"


class DosageProblem(Enum):
    """
    specDomain: S16680 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S16680-cpt)
    :cvar DOSE:
    :cvar DOSEDUR:
    :cvar DOSEIVL:
    :cvar DOSEH:
    :cvar DOSEL:
    :cvar DOSECOND:
    :cvar MDOSE:
    """
    DOSE = "DOSE"
    DOSEDUR = "DOSEDUR"
    DOSEIVL = "DOSEIVL"
    DOSEH = "DOSEH"
    DOSEL = "DOSEL"
    DOSECOND = "DOSECOND"
    MDOSE = "MDOSE"


class DosageProblemDetectedIssueCode(Enum):
    """
    specDomain: S16680 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-cpt)
    :cvar DOSEDURH:
    :cvar DOSEDURHIND:
    :cvar DOSEDURL:
    :cvar DOSEDURLIND:
    :cvar DOSEDUR:
    :cvar DOSEH:
    :cvar DOSEHINDA:
    :cvar DOSEHINDSA:
    :cvar DOSEHIND:
    :cvar DOSEHINDW:
    :cvar DOSEIVL:
    :cvar DOSEIVLIND:
    :cvar DOSEL:
    :cvar DOSELINDA:
    :cvar DOSELINDSA:
    :cvar DOSELIND:
    :cvar DOSELINDW:
    :cvar DOSE:
    :cvar DOSECOND:
    :cvar MDOSE:
    """
    DOSEDURH = "DOSEDURH"
    DOSEDURHIND = "DOSEDURHIND"
    DOSEDURL = "DOSEDURL"
    DOSEDURLIND = "DOSEDURLIND"
    DOSEDUR = "DOSEDUR"
    DOSEH = "DOSEH"
    DOSEHINDA = "DOSEHINDA"
    DOSEHINDSA = "DOSEHINDSA"
    DOSEHIND = "DOSEHIND"
    DOSEHINDW = "DOSEHINDW"
    DOSEIVL = "DOSEIVL"
    DOSEIVLIND = "DOSEIVLIND"
    DOSEL = "DOSEL"
    DOSELINDA = "DOSELINDA"
    DOSELINDSA = "DOSELINDSA"
    DOSELIND = "DOSELIND"
    DOSELINDW = "DOSELINDW"
    DOSE = "DOSE"
    DOSECOND = "DOSECOND"
    MDOSE = "MDOSE"


class DoseDurationDetectedIssueCode(Enum):
    """
    specDomain: S16684 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16684-cpt)
    :cvar DOSEDURH:
    :cvar DOSEDURHIND:
    :cvar DOSEDURL:
    :cvar DOSEDURLIND:
    :cvar DOSEDUR:
    """
    DOSEDURH = "DOSEDURH"
    DOSEDURHIND = "DOSEDURHIND"
    DOSEDURL = "DOSEDURL"
    DOSEDURLIND = "DOSEDURLIND"
    DOSEDUR = "DOSEDUR"


class DoseDurationHighDetectedIssueCode(Enum):
    """
    specDomain: S16686 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16684-S16686-cpt)
    :cvar DOSEDURH:
    :cvar DOSEDURHIND:
    """
    DOSEDURH = "DOSEDURH"
    DOSEDURHIND = "DOSEDURHIND"


class DoseDurationLowDetectedIssueCode(Enum):
    """
    specDomain: S16685 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16684-S16685-cpt)
    :cvar DOSEDURL:
    :cvar DOSEDURLIND:
    """
    DOSEDURL = "DOSEDURL"
    DOSEDURLIND = "DOSEDURLIND"


class DoseHighDetectedIssueCode(Enum):
    """
    specDomain: S16681 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16681-cpt)
    :cvar DOSEH:
    :cvar DOSEHINDA:
    :cvar DOSEHINDSA:
    :cvar DOSEHIND:
    :cvar DOSEHINDW:
    """
    DOSEH = "DOSEH"
    DOSEHINDA = "DOSEHINDA"
    DOSEHINDSA = "DOSEHINDSA"
    DOSEHIND = "DOSEHIND"
    DOSEHINDW = "DOSEHINDW"


class DoseIntervalDetectedIssueCode(Enum):
    """
    specDomain: S16683 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16683-cpt)
    :cvar DOSEIVL:
    :cvar DOSEIVLIND:
    """
    DOSEIVL = "DOSEIVL"
    DOSEIVLIND = "DOSEIVLIND"


class DoseLowDetectedIssueCode(Enum):
    """
    specDomain: S16682 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S16680-S16682-cpt)
    :cvar DOSEL:
    :cvar DOSELINDA:
    :cvar DOSELINDSA:
    :cvar DOSELIND:
    :cvar DOSELINDW:
    """
    DOSEL = "DOSEL"
    DOSELINDA = "DOSELINDA"
    DOSELINDSA = "DOSELINDSA"
    DOSELIND = "DOSELIND"
    DOSELINDW = "DOSELINDW"


class Douche(Enum):
    """
    abstDomain: A14589 (C-0-T14581-A16931-A14589-cpt)
    :cvar DOUCHE:
    """
    DOUCHE = "DOUCHE"


class DropsDrugForm(Enum):
    """
    specDomain: S14420 (C-0-T19651-A14411-A14412-A14413-S14419-S14420-cpt)
    :cvar DROP:
    :cvar NDROP:
    :cvar OPDROP:
    :cvar ORDROP:
    :cvar OTDROP:
    """
    DROP = "DROP"
    NDROP = "NDROP"
    OPDROP = "OPDROP"
    ORDROP = "ORDROP"
    OTDROP = "OTDROP"


class DuplicateTherapyAlert(Enum):
    """
    specDomain: S16688 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S16687-S16688-cpt)
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    """
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"


class DurableMedicalEquipmentAndOrMedicalSupplySupplierHipaa(Enum):
    """
    specDomain: S13835 (C-0-T13129-A13715-A13833-S13835-cpt)
    :cvar VALUE_332_B00000_N:
    :cvar VALUE_332_BC3200_N:
    :cvar VALUE_332_BD1200_N:
    :cvar VALUE_332_BN1400_N:
    :cvar VALUE_332_BX2000_N:
    :cvar VALUE_332_BP3500_N:
    """
    VALUE_332_B00000_N = "332B00000N"
    VALUE_332_BC3200_N = "332BC3200N"
    VALUE_332_BD1200_N = "332BD1200N"
    VALUE_332_BN1400_N = "332BN1400N"
    VALUE_332_BX2000_N = "332BX2000N"
    VALUE_332_BP3500_N = "332BP3500N"


class DurableMedicalEquipmentandMedicalSuppliesProviderCodes(Enum):
    """
    specDomain: S20774 (C-0-T19465-S20772-S20774-cpt)
    :cvar VALUE_332_B00000_X:
    :cvar VALUE_332_BC3200_X:
    :cvar VALUE_332_BD1200_X:
    :cvar VALUE_332_BN1400_X:
    :cvar VALUE_332_BX2000_X:
    :cvar VALUE_332_BP3500_X:
    """
    VALUE_332_B00000_X = "332B00000X"
    VALUE_332_BC3200_X = "332BC3200X"
    VALUE_332_BD1200_X = "332BD1200X"
    VALUE_332_BN1400_X = "332BN1400X"
    VALUE_332_BX2000_X = "332BX2000X"
    VALUE_332_BP3500_X = "332BP3500X"


class EcgobservationSeriesType(Enum):
    """
    abstDomain: A19322 (C-0-T13953-A19820-A16226-A19321-A19322-cpt)
    :cvar REPRESENTATIVE_BEAT:
    :cvar RHYTHM:
    """
    REPRESENTATIVE_BEAT = "REPRESENTATIVE_BEAT"
    RHYTHM = "RHYTHM"


class ErpracticeSetting(Enum):
    """
    specDomain: S10598 (C-0-T12206-A17660-A19450-A10588-S10596-S10598-cpt)
    :cvar ER:
    :cvar ETU:
    """
    ER = "ER"
    ETU = "ETU"


class EasternAlgonquin(Enum):
    """
    abstDomain: A18171 (C-0-T18130-A18131-A18132-A18171-cpt)
    :cvar X_AAQ:
    :cvar X_MAC:
    :cvar X_ABE:
    :cvar X_DEL:
    :cvar X_MIC:
    """
    X_AAQ = "x-AAQ"
    X_MAC = "x-MAC"
    X_ABE = "x-ABE"
    X_DEL = "x-DEL"
    X_MIC = "x-MIC"


class EasternApachean(Enum):
    """
    abstDomain: A18407 (C-0-T18130-A18352-A18356-A18358-A18399-A18407-cpt)
    :cvar X_APJ:
    :cvar X_APL:
    """
    X_APJ = "x-APJ"
    X_APL = "x-APL"


class EasternMiwok(Enum):
    """
    abstDomain: A18463 (C-0-T18130-A18413-A18458-A18459-A18463-cpt)
    :cvar X_CSM:
    :cvar X_NSQ:
    :cvar X_PMW:
    :cvar X_SKD:
    """
    X_CSM = "x-CSM"
    X_NSQ = "x-NSQ"
    X_PMW = "x-PMW"
    X_SKD = "x-SKD"


class EditStatus(Enum):
    """
    vocSet: T11040 (C-0-T11040-cpt)
    :cvar A:
    :cvar I:
    :cvar O:
    :cvar R:
    :cvar P:
    """
    A = "A"
    I = "I"
    O = "O"
    R = "R"
    P = "P"


class EducationLevel(Enum):
    """
    vocSet: T19175 (C-0-T19175-cpt)
    :cvar ASSOC:
    :cvar BD:
    :cvar POSTG:
    :cvar ELEM:
    :cvar GD:
    :cvar HS:
    :cvar SCOL:
    :cvar PB:
    :cvar SEC:
    """
    ASSOC = "ASSOC"
    BD = "BD"
    POSTG = "POSTG"
    ELEM = "ELEM"
    GD = "GD"
    HS = "HS"
    SCOL = "SCOL"
    PB = "PB"
    SEC = "SEC"


class ElectroOsmosisRoute(Enum):
    """
    abstDomain: A17019 (C-0-T14581-A16931-A17019-cpt)
    :cvar ELECTOSMOS:
    """
    ELECTOSMOS = "ELECTOSMOS"


class EmergencyMedicalServiceProviderHipaa(Enum):
    """
    abstDomain: A13207 (C-0-T13129-A13130-A13207-cpt)
    :cvar VALUE_146_N00000_N:
    :cvar VALUE_146_M00000_N:
    :cvar VALUE_146_L00000_N:
    """
    VALUE_146_N00000_N = "146N00000N"
    VALUE_146_M00000_N = "146M00000N"
    VALUE_146_L00000_N = "146L00000N"


class EmergencyMedicalServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20343 (C-0-T19465-S20343-cpt)
    :cvar VALUE_140000000_X:
    :cvar VALUE_146_N00000_X:
    :cvar VALUE_146_M00000_X:
    :cvar VALUE_146_L00000_X:
    :cvar VALUE_146_D00000_X:
    """
    VALUE_140000000_X = "140000000X"
    VALUE_146_N00000_X = "146N00000X"
    VALUE_146_M00000_X = "146M00000X"
    VALUE_146_L00000_X = "146L00000X"
    VALUE_146_D00000_X = "146D00000X"


class EmergencyMedicineProviderCodes(Enum):
    """
    specDomain: S20112 (C-0-T19465-S20096-S20112-cpt)
    :cvar VALUE_207_P00000_X:
    :cvar VALUE_207_PE0004_X:
    :cvar VALUE_207_PT0002_X:
    :cvar VALUE_207_PP0204_X:
    :cvar VALUE_207_PS0010_X:
    :cvar VALUE_207_PE0005_X:
    """
    VALUE_207_P00000_X = "207P00000X"
    VALUE_207_PE0004_X = "207PE0004X"
    VALUE_207_PT0002_X = "207PT0002X"
    VALUE_207_PP0204_X = "207PP0204X"
    VALUE_207_PS0010_X = "207PS0010X"
    VALUE_207_PE0005_X = "207PE0005X"


class EmergencyPharmacySupplyType(Enum):
    """
    specDomain: S16220 (C-0-T13953-A13954-A16208-S16220-cpt)
    :cvar EM:
    :cvar SO:
    """
    EM = "EM"
    SO = "SO"


class EncounterAdmissionSource(Enum):
    """
    vocSet: T12234 (C-0-T12234-cpt)
    :cvar E:
    :cvar LD:
    :cvar NB:
    """
    E = "E"
    LD = "LD"
    NB = "NB"


class EncounterSpecialCourtesy(Enum):
    """
    vocSet: T12242 (C-0-T12242-cpt)
    :cvar EXT:
    :cvar NRM:
    :cvar PRF:
    :cvar STF:
    :cvar VIP:
    """
    EXT = "EXT"
    NRM = "NRM"
    PRF = "PRF"
    STF = "STF"
    VIP = "VIP"


class EndocervicalRoute(Enum):
    """
    abstDomain: A17045 (C-0-T14581-A17021-A17045-cpt)
    :cvar AMNINJ:
    :cvar BILINJ:
    """
    AMNINJ = "AMNINJ"
    BILINJ = "BILINJ"


class EndocrinologyClinic(Enum):
    """
    specDomain: S10931 (C-0-T12206-A17660-A19450-A10588-S10589-S10931-cpt)
    :cvar ENDO:
    :cvar PEDE:
    """
    ENDO = "ENDO"
    PEDE = "PEDE"


class Enema(Enum):
    """
    abstDomain: A14591 (C-0-T14581-A16931-A14591-cpt)
    :cvar ENEMA:
    :cvar RETENEMA:
    """
    ENEMA = "ENEMA"
    RETENEMA = "RETENEMA"


class EnteralRoute(Enum):
    """
    abstDomain: A17048 (C-0-T14581-A17021-A17048-cpt)
    :cvar ENTINSTL:
    :cvar EFT:
    """
    ENTINSTL = "ENTINSTL"
    EFT = "EFT"


class EntericCoatedCapsule(Enum):
    """
    specDomain: S14509 (C-0-T19651-A14411-A14412-A14484-S14506-S14507-S14508-S14509-cpt)
    :cvar ENTCAP:
    :cvar ERENTCAP:
    """
    ENTCAP = "ENTCAP"
    ERENTCAP = "ERENTCAP"


class EntericCoatedTablet(Enum):
    """
    specDomain: S14524 (C-0-T19651-A14411-A14412-A14484-S14506-S14515-S14516-S14524-cpt)
    :cvar ECTAB:
    :cvar ERECTAB:
    """
    ECTAB = "ECTAB"
    ERECTAB = "ERECTAB"


class EntityClass(Enum):
    """
    vocSet: T10882 (C-0-T10882-cpt)
    :cvar NLIV:
    :cvar ANM:
    :cvar MIC:
    :cvar PLNT:
    :cvar LIV:
    :cvar PSN:
    :cvar CONT:
    :cvar HOLD:
    :cvar DEV:
    :cvar CER:
    :cvar MODDV:
    :cvar MMAT:
    :cvar MAT:
    :cvar CHEM:
    :cvar FOOD:
    :cvar STATE:
    :cvar NAT:
    :cvar ORG:
    :cvar PUB:
    :cvar PLC:
    :cvar CITY:
    :cvar COUNTRY:
    :cvar COUNTY:
    :cvar PROVINCE:
    :cvar ENT:
    :cvar RGRP:
    :cvar HCE:
    """
    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
    ENT = "ENT"
    RGRP = "RGRP"
    HCE = "HCE"


class EntityClassContainer(Enum):
    """
    specDomain: S11622 (C-0-T10882-S13922-S10883-S13934-S11622-cpt)
    :cvar CONT:
    :cvar HOLD:
    """
    CONT = "CONT"
    HOLD = "HOLD"


class EntityClassDevice(Enum):
    """
    specDomain: S11623 (C-0-T10882-S13922-S10883-S13934-S11623-cpt)
    :cvar DEV:
    :cvar CER:
    :cvar MODDV:
    """
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"


class EntityClassLivingSubject(Enum):
    """
    specDomain: S10884 (C-0-T10882-S13922-S10884-cpt)
    :cvar NLIV:
    :cvar ANM:
    :cvar MIC:
    :cvar PLNT:
    :cvar LIV:
    :cvar PSN:
    """
    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"


class EntityClassManufacturedMaterial(Enum):
    """
    specDomain: S13934 (C-0-T10882-S13922-S10883-S13934-cpt)
    :cvar CONT:
    :cvar HOLD:
    :cvar DEV:
    :cvar CER:
    :cvar MODDV:
    :cvar MMAT:
    """
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"


class EntityClassMaterial(Enum):
    """
    specDomain: S10883 (C-0-T10882-S13922-S10883-cpt)
    :cvar CONT:
    :cvar HOLD:
    :cvar DEV:
    :cvar CER:
    :cvar MODDV:
    :cvar MMAT:
    :cvar MAT:
    :cvar CHEM:
    :cvar FOOD:
    """
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"


class EntityClassNonPersonLivingSubject(Enum):
    """
    specDomain: S11621 (C-0-T10882-S13922-S10884-S11621-cpt)
    :cvar NLIV:
    :cvar ANM:
    :cvar MIC:
    :cvar PLNT:
    """
    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"


class EntityClassOrganization(Enum):
    """
    specDomain: S10889 (C-0-T10882-S13922-S10889-cpt)
    :cvar STATE:
    :cvar NAT:
    :cvar ORG:
    :cvar PUB:
    """
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"


class EntityClassPlace(Enum):
    """
    specDomain: S10892 (C-0-T10882-S13922-S10892-cpt)
    :cvar PLC:
    :cvar CITY:
    :cvar COUNTRY:
    :cvar COUNTY:
    :cvar PROVINCE:
    """
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"


class EntityClassRoot(Enum):
    """
    specDomain: S13922 (C-0-T10882-S13922-cpt)
    :cvar NLIV:
    :cvar ANM:
    :cvar MIC:
    :cvar PLNT:
    :cvar LIV:
    :cvar PSN:
    :cvar CONT:
    :cvar HOLD:
    :cvar DEV:
    :cvar CER:
    :cvar MODDV:
    :cvar MMAT:
    :cvar MAT:
    :cvar CHEM:
    :cvar FOOD:
    :cvar STATE:
    :cvar NAT:
    :cvar ORG:
    :cvar PUB:
    :cvar PLC:
    :cvar CITY:
    :cvar COUNTRY:
    :cvar COUNTY:
    :cvar PROVINCE:
    :cvar ENT:
    :cvar RGRP:
    :cvar HCE:
    """
    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
    ENT = "ENT"
    RGRP = "RGRP"
    HCE = "HCE"


class EntityClassState(Enum):
    """
    specDomain: S10890 (C-0-T10882-S13922-S10889-S10890-cpt)
    :cvar STATE:
    :cvar NAT:
    """
    STATE = "STATE"
    NAT = "NAT"


class EntityDeterminer(Enum):
    """
    vocSet: T10878 (C-0-T10878-cpt)
    :cvar KIND:
    :cvar QUANTIFIED_KIND:
    :cvar INSTANCE:
    """
    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
    INSTANCE = "INSTANCE"


class EntityDeterminerDetermined(Enum):
    """
    specDomain: S10879 (C-0-T10878-S10879-cpt)
    :cvar KIND:
    :cvar QUANTIFIED_KIND:
    """
    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"


class EntityHandling(Enum):
    """
    vocSet: T13988 (C-0-T13988-cpt)
    :cvar AMB:
    :cvar C37:
    :cvar CAMB:
    :cvar CFRZ:
    :cvar CREF:
    :cvar DFRZ:
    :cvar MTLF:
    :cvar CATM:
    :cvar PRTL:
    :cvar REF:
    :cvar SBU:
    :cvar UFRZ:
    :cvar PSA:
    :cvar DRY:
    :cvar FRZ:
    :cvar NTR:
    :cvar PSO:
    :cvar UPR:
    """
    AMB = "AMB"
    C37 = "C37"
    CAMB = "CAMB"
    CFRZ = "CFRZ"
    CREF = "CREF"
    DFRZ = "DFRZ"
    MTLF = "MTLF"
    CATM = "CATM"
    PRTL = "PRTL"
    REF = "REF"
    SBU = "SBU"
    UFRZ = "UFRZ"
    PSA = "PSA"
    DRY = "DRY"
    FRZ = "FRZ"
    NTR = "NTR"
    PSO = "PSO"
    UPR = "UPR"


class EntityNamePartQualifier(Enum):
    """
    vocSet: T15888 (C-0-T15888-cpt)
    :cvar LS:
    :cvar AC:
    :cvar NB:
    :cvar PR:
    :cvar VV:
    :cvar AD:
    :cvar BR:
    :cvar SP:
    :cvar CL:
    :cvar IN_VALUE:
    :cvar TITLE:
    """
    LS = "LS"
    AC = "AC"
    NB = "NB"
    PR = "PR"
    VV = "VV"
    AD = "AD"
    BR = "BR"
    SP = "SP"
    CL = "CL"
    IN_VALUE = "IN"
    TITLE = "TITLE"


class EntityNamePartType(Enum):
    """
    vocSet: T15880 (C-0-T15880-cpt)
    :cvar DEL_VALUE:
    :cvar PFX:
    :cvar SFX:
    :cvar FAM:
    :cvar GIV:
    """
    DEL_VALUE = "DEL"
    PFX = "PFX"
    SFX = "SFX"
    FAM = "FAM"
    GIV = "GIV"


class EntityNameSearchUse(Enum):
    """
    specDomain: S21363 (C-0-T15913-A200-S21363-cpt)
    :cvar SRCH:
    :cvar SNDX:
    :cvar PHON:
    """
    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"


class EntityNameUse(Enum):
    """
    vocSet: T15913 (C-0-T15913-cpt)
    :cvar SRCH:
    :cvar SNDX:
    :cvar PHON:
    :cvar L:
    :cvar OR_VALUE:
    :cvar ABC:
    :cvar IDE:
    :cvar SYL:
    :cvar C:
    :cvar P:
    :cvar A:
    :cvar I:
    :cvar R:
    :cvar ASGN:
    """
    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"
    L = "L"
    OR_VALUE = "OR"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    C = "C"
    P = "P"
    A = "A"
    I = "I"
    R = "R"
    ASGN = "ASGN"


class EntityRisk(Enum):
    """
    vocSet: T10405 (C-0-T10405-cpt)
    :cvar INF:
    :cvar BHZ:
    :cvar IFL:
    :cvar EXP:
    :cvar BIO:
    :cvar COR:
    :cvar ESC:
    :cvar AGG:
    :cvar INJ:
    :cvar POI:
    :cvar RAD:
    """
    INF = "INF"
    BHZ = "BHZ"
    IFL = "IFL"
    EXP = "EXP"
    BIO = "BIO"
    COR = "COR"
    ESC = "ESC"
    AGG = "AGG"
    INJ = "INJ"
    POI = "POI"
    RAD = "RAD"


class EntityStatus(Enum):
    """
    vocSet: T16005 (C-0-T16005-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar INACTIVE:
    :cvar NULLIFIED:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    INACTIVE = "inactive"
    NULLIFIED = "nullified"


class EntityStatusNormal(Enum):
    """
    specDomain: S16006 (C-0-T16005-S16006-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar INACTIVE:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    INACTIVE = "inactive"


class EpiduralRoute(Enum):
    """
    abstDomain: A17051 (C-0-T14581-A17021-A17051-cpt)
    :cvar EPI:
    :cvar EPIDURINJ:
    :cvar EPIINJ:
    :cvar EPINJSP:
    """
    EPI = "EPI"
    EPIDURINJ = "EPIDURINJ"
    EPIINJ = "EPIINJ"
    EPINJSP = "EPINJSP"


class EquipmentAlertLevel(Enum):
    """
    vocSet: T10896 (C-0-T10896-cpt)
    :cvar C:
    :cvar N:
    :cvar S:
    :cvar W:
    """
    C = "C"
    N = "N"
    S = "S"
    W = "W"


class Ethnicity(Enum):
    """
    vocSet: T15836 (C-0-T15836-cpt)
    :cvar VALUE_2155_0:
    :cvar VALUE_2163_4:
    :cvar VALUE_2162_6:
    :cvar VALUE_2156_8:
    :cvar VALUE_2157_6:
    :cvar VALUE_2158_4:
    :cvar VALUE_2159_2:
    :cvar VALUE_2160_0:
    :cvar VALUE_2161_8:
    :cvar VALUE_2148_5:
    :cvar VALUE_2151_9:
    :cvar VALUE_2152_7:
    :cvar VALUE_2149_3:
    :cvar VALUE_2153_5:
    :cvar VALUE_2150_1:
    :cvar VALUE_2165_9:
    :cvar VALUE_2166_7:
    :cvar VALUE_2167_5:
    :cvar VALUE_2168_3:
    :cvar VALUE_2169_1:
    :cvar VALUE_2176_6:
    :cvar VALUE_2170_9:
    :cvar VALUE_2171_7:
    :cvar VALUE_2172_5:
    :cvar VALUE_2175_8:
    :cvar VALUE_2173_3:
    :cvar VALUE_2174_1:
    :cvar VALUE_2137_8:
    :cvar VALUE_2138_6:
    :cvar VALUE_2139_4:
    :cvar VALUE_2142_8:
    :cvar VALUE_2145_1:
    :cvar VALUE_2140_2:
    :cvar VALUE_2141_0:
    :cvar VALUE_2143_6:
    :cvar VALUE_2146_9:
    :cvar VALUE_2144_4:
    :cvar VALUE_2135_2:
    :cvar VALUE_2182_4:
    :cvar VALUE_2184_0:
    :cvar VALUE_2178_2:
    :cvar VALUE_2180_8:
    :cvar VALUE_2186_5:
    """
    VALUE_2155_0 = "2155-0"
    VALUE_2163_4 = "2163-4"
    VALUE_2162_6 = "2162-6"
    VALUE_2156_8 = "2156-8"
    VALUE_2157_6 = "2157-6"
    VALUE_2158_4 = "2158-4"
    VALUE_2159_2 = "2159-2"
    VALUE_2160_0 = "2160-0"
    VALUE_2161_8 = "2161-8"
    VALUE_2148_5 = "2148-5"
    VALUE_2151_9 = "2151-9"
    VALUE_2152_7 = "2152-7"
    VALUE_2149_3 = "2149-3"
    VALUE_2153_5 = "2153-5"
    VALUE_2150_1 = "2150-1"
    VALUE_2165_9 = "2165-9"
    VALUE_2166_7 = "2166-7"
    VALUE_2167_5 = "2167-5"
    VALUE_2168_3 = "2168-3"
    VALUE_2169_1 = "2169-1"
    VALUE_2176_6 = "2176-6"
    VALUE_2170_9 = "2170-9"
    VALUE_2171_7 = "2171-7"
    VALUE_2172_5 = "2172-5"
    VALUE_2175_8 = "2175-8"
    VALUE_2173_3 = "2173-3"
    VALUE_2174_1 = "2174-1"
    VALUE_2137_8 = "2137-8"
    VALUE_2138_6 = "2138-6"
    VALUE_2139_4 = "2139-4"
    VALUE_2142_8 = "2142-8"
    VALUE_2145_1 = "2145-1"
    VALUE_2140_2 = "2140-2"
    VALUE_2141_0 = "2141-0"
    VALUE_2143_6 = "2143-6"
    VALUE_2146_9 = "2146-9"
    VALUE_2144_4 = "2144-4"
    VALUE_2135_2 = "2135-2"
    VALUE_2182_4 = "2182-4"
    VALUE_2184_0 = "2184-0"
    VALUE_2178_2 = "2178-2"
    VALUE_2180_8 = "2180-8"
    VALUE_2186_5 = "2186-5"


class EthnicityHispanic(Enum):
    """
    specDomain: S15837 (C-0-T15836-S15837-cpt)
    :cvar VALUE_2155_0:
    :cvar VALUE_2163_4:
    :cvar VALUE_2162_6:
    :cvar VALUE_2156_8:
    :cvar VALUE_2157_6:
    :cvar VALUE_2158_4:
    :cvar VALUE_2159_2:
    :cvar VALUE_2160_0:
    :cvar VALUE_2161_8:
    :cvar VALUE_2148_5:
    :cvar VALUE_2151_9:
    :cvar VALUE_2152_7:
    :cvar VALUE_2149_3:
    :cvar VALUE_2153_5:
    :cvar VALUE_2150_1:
    :cvar VALUE_2165_9:
    :cvar VALUE_2166_7:
    :cvar VALUE_2167_5:
    :cvar VALUE_2168_3:
    :cvar VALUE_2169_1:
    :cvar VALUE_2176_6:
    :cvar VALUE_2170_9:
    :cvar VALUE_2171_7:
    :cvar VALUE_2172_5:
    :cvar VALUE_2175_8:
    :cvar VALUE_2173_3:
    :cvar VALUE_2174_1:
    :cvar VALUE_2137_8:
    :cvar VALUE_2138_6:
    :cvar VALUE_2139_4:
    :cvar VALUE_2142_8:
    :cvar VALUE_2145_1:
    :cvar VALUE_2140_2:
    :cvar VALUE_2141_0:
    :cvar VALUE_2143_6:
    :cvar VALUE_2146_9:
    :cvar VALUE_2144_4:
    :cvar VALUE_2135_2:
    :cvar VALUE_2182_4:
    :cvar VALUE_2184_0:
    :cvar VALUE_2178_2:
    :cvar VALUE_2180_8:
    """
    VALUE_2155_0 = "2155-0"
    VALUE_2163_4 = "2163-4"
    VALUE_2162_6 = "2162-6"
    VALUE_2156_8 = "2156-8"
    VALUE_2157_6 = "2157-6"
    VALUE_2158_4 = "2158-4"
    VALUE_2159_2 = "2159-2"
    VALUE_2160_0 = "2160-0"
    VALUE_2161_8 = "2161-8"
    VALUE_2148_5 = "2148-5"
    VALUE_2151_9 = "2151-9"
    VALUE_2152_7 = "2152-7"
    VALUE_2149_3 = "2149-3"
    VALUE_2153_5 = "2153-5"
    VALUE_2150_1 = "2150-1"
    VALUE_2165_9 = "2165-9"
    VALUE_2166_7 = "2166-7"
    VALUE_2167_5 = "2167-5"
    VALUE_2168_3 = "2168-3"
    VALUE_2169_1 = "2169-1"
    VALUE_2176_6 = "2176-6"
    VALUE_2170_9 = "2170-9"
    VALUE_2171_7 = "2171-7"
    VALUE_2172_5 = "2172-5"
    VALUE_2175_8 = "2175-8"
    VALUE_2173_3 = "2173-3"
    VALUE_2174_1 = "2174-1"
    VALUE_2137_8 = "2137-8"
    VALUE_2138_6 = "2138-6"
    VALUE_2139_4 = "2139-4"
    VALUE_2142_8 = "2142-8"
    VALUE_2145_1 = "2145-1"
    VALUE_2140_2 = "2140-2"
    VALUE_2141_0 = "2141-0"
    VALUE_2143_6 = "2143-6"
    VALUE_2146_9 = "2146-9"
    VALUE_2144_4 = "2144-4"
    VALUE_2135_2 = "2135-2"
    VALUE_2182_4 = "2182-4"
    VALUE_2184_0 = "2184-0"
    VALUE_2178_2 = "2178-2"
    VALUE_2180_8 = "2180-8"


class EthnicityHispanicCentralAmerican(Enum):
    """
    specDomain: S15854 (C-0-T15836-S15837-S15854-cpt)
    :cvar VALUE_2155_0:
    :cvar VALUE_2163_4:
    :cvar VALUE_2162_6:
    :cvar VALUE_2156_8:
    :cvar VALUE_2157_6:
    :cvar VALUE_2158_4:
    :cvar VALUE_2159_2:
    :cvar VALUE_2160_0:
    :cvar VALUE_2161_8:
    """
    VALUE_2155_0 = "2155-0"
    VALUE_2163_4 = "2163-4"
    VALUE_2162_6 = "2162-6"
    VALUE_2156_8 = "2156-8"
    VALUE_2157_6 = "2157-6"
    VALUE_2158_4 = "2158-4"
    VALUE_2159_2 = "2159-2"
    VALUE_2160_0 = "2160-0"
    VALUE_2161_8 = "2161-8"


class EthnicityHispanicMexican(Enum):
    """
    specDomain: S15848 (C-0-T15836-S15837-S15848-cpt)
    :cvar VALUE_2148_5:
    :cvar VALUE_2151_9:
    :cvar VALUE_2152_7:
    :cvar VALUE_2149_3:
    :cvar VALUE_2153_5:
    :cvar VALUE_2150_1:
    """
    VALUE_2148_5 = "2148-5"
    VALUE_2151_9 = "2151-9"
    VALUE_2152_7 = "2152-7"
    VALUE_2149_3 = "2149-3"
    VALUE_2153_5 = "2153-5"
    VALUE_2150_1 = "2150-1"


class EthnicityHispanicSouthAmerican(Enum):
    """
    specDomain: S15863 (C-0-T15836-S15837-S15863-cpt)
    :cvar VALUE_2165_9:
    :cvar VALUE_2166_7:
    :cvar VALUE_2167_5:
    :cvar VALUE_2168_3:
    :cvar VALUE_2169_1:
    :cvar VALUE_2176_6:
    :cvar VALUE_2170_9:
    :cvar VALUE_2171_7:
    :cvar VALUE_2172_5:
    :cvar VALUE_2175_8:
    :cvar VALUE_2173_3:
    :cvar VALUE_2174_1:
    """
    VALUE_2165_9 = "2165-9"
    VALUE_2166_7 = "2166-7"
    VALUE_2167_5 = "2167-5"
    VALUE_2168_3 = "2168-3"
    VALUE_2169_1 = "2169-1"
    VALUE_2176_6 = "2176-6"
    VALUE_2170_9 = "2170-9"
    VALUE_2171_7 = "2171-7"
    VALUE_2172_5 = "2172-5"
    VALUE_2175_8 = "2175-8"
    VALUE_2173_3 = "2173-3"
    VALUE_2174_1 = "2174-1"


class EthnicityHispanicSpaniard(Enum):
    """
    specDomain: S15838 (C-0-T15836-S15837-S15838-cpt)
    :cvar VALUE_2137_8:
    :cvar VALUE_2138_6:
    :cvar VALUE_2139_4:
    :cvar VALUE_2142_8:
    :cvar VALUE_2145_1:
    :cvar VALUE_2140_2:
    :cvar VALUE_2141_0:
    :cvar VALUE_2143_6:
    :cvar VALUE_2146_9:
    :cvar VALUE_2144_4:
    """
    VALUE_2137_8 = "2137-8"
    VALUE_2138_6 = "2138-6"
    VALUE_2139_4 = "2139-4"
    VALUE_2142_8 = "2142-8"
    VALUE_2145_1 = "2145-1"
    VALUE_2140_2 = "2140-2"
    VALUE_2141_0 = "2141-0"
    VALUE_2143_6 = "2143-6"
    VALUE_2146_9 = "2146-9"
    VALUE_2144_4 = "2144-4"


class ExpectedSubset(Enum):
    """
    specDomain: S21368 (C-0-T19613-A19736-S21368-cpt)
    :cvar FUTURE:
    :cvar LAST:
    :cvar NEXT:
    :cvar FUTSUM:
    """
    FUTURE = "FUTURE"
    LAST = "LAST"
    NEXT = "NEXT"
    FUTSUM = "FUTSUM"


class ExposureMode(Enum):
    """
    vocSet: T19940 (C-0-T19940-cpt)
    :cvar AIRBORNE:
    :cvar CONTACT:
    :cvar FOODBORNE:
    :cvar WATERBORNE:
    """
    AIRBORNE = "AIRBORNE"
    CONTACT = "CONTACT"
    FOODBORNE = "FOODBORNE"
    WATERBORNE = "WATERBORNE"


class ExtendedReleaseCapsule(Enum):
    """
    specDomain: S14511 (C-0-T19651-A14411-A14412-A14484-S14506-S14507-S14508-S14511-cpt)
    :cvar ERCAP:
    :cvar ERCAP12:
    :cvar ERCAP24:
    :cvar ERECCAP:
    """
    ERCAP = "ERCAP"
    ERCAP12 = "ERCAP12"
    ERCAP24 = "ERCAP24"
    ERECCAP = "ERECCAP"


class ExtendedReleaseSuspension(Enum):
    """
    specDomain: S14458 (C-0-T19651-A14411-A14412-A14441-S14454-S14457-S14458-cpt)
    :cvar ERSUSP:
    :cvar ERSUSP12:
    :cvar ERSUSP24:
    """
    ERSUSP = "ERSUSP"
    ERSUSP12 = "ERSUSP12"
    ERSUSP24 = "ERSUSP24"


class ExtendedReleaseTablet(Enum):
    """
    specDomain: S14526 (C-0-T19651-A14411-A14412-A14484-S14506-S14515-S14516-S14526-cpt)
    :cvar ERTAB:
    :cvar ERTAB12:
    :cvar ERTAB24:
    :cvar ERECTAB:
    """
    ERTAB = "ERTAB"
    ERTAB12 = "ERTAB12"
    ERTAB24 = "ERTAB24"
    ERECTAB = "ERECTAB"


class Extensibility(Enum):
    """
    abstDomain: A11047 (C-0-T11046-A11047-cpt)
    :cvar CNE:
    :cvar CWE:
    """
    CNE = "CNE"
    CWE = "CWE"


class ExtraAmnioticRoute(Enum):
    """
    abstDomain: A17059 (C-0-T14581-A17021-A17059-cpt)
    :cvar EXTRAMNINJ:
    """
    EXTRAMNINJ = "EXTRAMNINJ"


class ExtracorporealCirculationRoute(Enum):
    """
    abstDomain: A17056 (C-0-T14581-A17021-A17056-cpt)
    :cvar EXTCORPDIF:
    :cvar EXTCORPINJ:
    """
    EXTCORPDIF = "EXTCORPDIF"
    EXTCORPINJ = "EXTCORPINJ"


class EyeAndVisionServiceProviderTechnicianAndOrTechnologistHipaa(Enum):
    """
    abstDomain: A13219 (C-0-T13129-A13130-A13211-A13219-cpt)
    :cvar VALUE_156_FC0800_N:
    :cvar VALUE_156_FC0801_N:
    :cvar VALUE_156_FX1700_N:
    :cvar VALUE_156_FX1100_N:
    :cvar VALUE_156_FX1101_N:
    :cvar VALUE_156_FX1800_N:
    :cvar VALUE_156_FX1201_N:
    :cvar VALUE_156_FX1202_N:
    :cvar VALUE_156_FX1900_N:
    """
    VALUE_156_FC0800_N = "156FC0800N"
    VALUE_156_FC0801_N = "156FC0801N"
    VALUE_156_FX1700_N = "156FX1700N"
    VALUE_156_FX1100_N = "156FX1100N"
    VALUE_156_FX1101_N = "156FX1101N"
    VALUE_156_FX1800_N = "156FX1800N"
    VALUE_156_FX1201_N = "156FX1201N"
    VALUE_156_FX1202_N = "156FX1202N"
    VALUE_156_FX1900_N = "156FX1900N"


class EyeandVisionServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20348 (C-0-T19465-S20348-cpt)
    :cvar VALUE_152_W00000_X:
    :cvar VALUE_152_WC0802_X:
    :cvar VALUE_152_WL0500_X:
    :cvar VALUE_152_WX0102_X:
    :cvar VALUE_152_WP0200_X:
    :cvar VALUE_152_WS0006_X:
    :cvar VALUE_152_WV0400_X:
    :cvar VALUE_156_F00000_X:
    :cvar VALUE_156_FC0800_X:
    :cvar VALUE_156_FC0801_X:
    :cvar VALUE_156_FX1700_X:
    :cvar VALUE_156_FX1100_X:
    :cvar VALUE_156_FX1101_X:
    :cvar VALUE_156_FX1800_X:
    :cvar VALUE_156_FX1201_X:
    :cvar VALUE_156_FX1202_X:
    :cvar VALUE_156_FX1900_X:
    :cvar VALUE_150000000_X:
    """
    VALUE_152_W00000_X = "152W00000X"
    VALUE_152_WC0802_X = "152WC0802X"
    VALUE_152_WL0500_X = "152WL0500X"
    VALUE_152_WX0102_X = "152WX0102X"
    VALUE_152_WP0200_X = "152WP0200X"
    VALUE_152_WS0006_X = "152WS0006X"
    VALUE_152_WV0400_X = "152WV0400X"
    VALUE_156_F00000_X = "156F00000X"
    VALUE_156_FC0800_X = "156FC0800X"
    VALUE_156_FC0801_X = "156FC0801X"
    VALUE_156_FX1700_X = "156FX1700X"
    VALUE_156_FX1100_X = "156FX1100X"
    VALUE_156_FX1101_X = "156FX1101X"
    VALUE_156_FX1800_X = "156FX1800X"
    VALUE_156_FX1201_X = "156FX1201X"
    VALUE_156_FX1202_X = "156FX1202X"
    VALUE_156_FX1900_X = "156FX1900X"
    VALUE_150000000_X = "150000000X"


class FamilyMember(Enum):
    """
    specDomain: S17926 (C-0-T12206-A19563-S17926-cpt)
    :cvar CHLDADOPT:
    :cvar DAUADOPT:
    :cvar SONADOPT:
    :cvar CHLDINLAW:
    :cvar DAUINLAW:
    :cvar SONINLAW:
    :cvar CHLDFOST:
    :cvar DAUFOST:
    :cvar SONFOST:
    :cvar NCHILD:
    :cvar DAU:
    :cvar SON:
    :cvar STPCHLD:
    :cvar STPDAU:
    :cvar STPSON:
    :cvar CHILD:
    :cvar AUNT:
    :cvar MAUNT:
    :cvar PAUNT:
    :cvar COUSN:
    :cvar MCOUSN:
    :cvar PCOUSN:
    :cvar UNCLE:
    :cvar MUNCLE:
    :cvar PUNCLE:
    :cvar GRNDCHILD:
    :cvar GRNDDAU:
    :cvar GRNDSON:
    :cvar GRPRN:
    :cvar GRFTH:
    :cvar GRMTH:
    :cvar MGRFTH:
    :cvar MGRMTH:
    :cvar MGRPRN:
    :cvar PGRFTH:
    :cvar PGRMTH:
    :cvar PGRPRN:
    :cvar GGRPRN:
    :cvar MGGRFTH:
    :cvar MGGRMTH:
    :cvar MGGRPRN:
    :cvar PGGRFTH:
    :cvar PGGRMTH:
    :cvar PGGRPRN:
    :cvar GGRFTH:
    :cvar GGRMTH:
    :cvar NIENEPH:
    :cvar NEPHEW:
    :cvar NIECE:
    :cvar NFTH:
    :cvar NFTHF:
    :cvar NPRN:
    :cvar NMTH:
    :cvar PRNINLAW:
    :cvar FTHINLAW:
    :cvar MTHINLAW:
    :cvar STPPRN:
    :cvar STPFTH:
    :cvar STPMTH:
    :cvar PRN:
    :cvar FTH:
    :cvar MTH:
    :cvar HSIB:
    :cvar HBRO:
    :cvar HSIS:
    :cvar NSIB:
    :cvar NBRO:
    :cvar NSIS:
    :cvar SIBINLAW:
    :cvar BROINLAW:
    :cvar SISINLAW:
    :cvar STPSIB:
    :cvar STPBRO:
    :cvar STPSIS:
    :cvar SIB:
    :cvar BRO:
    :cvar SIS:
    :cvar SPS:
    :cvar HUSB:
    :cvar WIFE:
    :cvar SIGOTHR:
    :cvar FAMMEMB:
    :cvar ROOM:
    :cvar DOMPART:
    """
    CHLDADOPT = "CHLDADOPT"
    DAUADOPT = "DAUADOPT"
    SONADOPT = "SONADOPT"
    CHLDINLAW = "CHLDINLAW"
    DAUINLAW = "DAUINLAW"
    SONINLAW = "SONINLAW"
    CHLDFOST = "CHLDFOST"
    DAUFOST = "DAUFOST"
    SONFOST = "SONFOST"
    NCHILD = "NCHILD"
    DAU = "DAU"
    SON = "SON"
    STPCHLD = "STPCHLD"
    STPDAU = "STPDAU"
    STPSON = "STPSON"
    CHILD = "CHILD"
    AUNT = "AUNT"
    MAUNT = "MAUNT"
    PAUNT = "PAUNT"
    COUSN = "COUSN"
    MCOUSN = "MCOUSN"
    PCOUSN = "PCOUSN"
    UNCLE = "UNCLE"
    MUNCLE = "MUNCLE"
    PUNCLE = "PUNCLE"
    GRNDCHILD = "GRNDCHILD"
    GRNDDAU = "GRNDDAU"
    GRNDSON = "GRNDSON"
    GRPRN = "GRPRN"
    GRFTH = "GRFTH"
    GRMTH = "GRMTH"
    MGRFTH = "MGRFTH"
    MGRMTH = "MGRMTH"
    MGRPRN = "MGRPRN"
    PGRFTH = "PGRFTH"
    PGRMTH = "PGRMTH"
    PGRPRN = "PGRPRN"
    GGRPRN = "GGRPRN"
    MGGRFTH = "MGGRFTH"
    MGGRMTH = "MGGRMTH"
    MGGRPRN = "MGGRPRN"
    PGGRFTH = "PGGRFTH"
    PGGRMTH = "PGGRMTH"
    PGGRPRN = "PGGRPRN"
    GGRFTH = "GGRFTH"
    GGRMTH = "GGRMTH"
    NIENEPH = "NIENEPH"
    NEPHEW = "NEPHEW"
    NIECE = "NIECE"
    NFTH = "NFTH"
    NFTHF = "NFTHF"
    NPRN = "NPRN"
    NMTH = "NMTH"
    PRNINLAW = "PRNINLAW"
    FTHINLAW = "FTHINLAW"
    MTHINLAW = "MTHINLAW"
    STPPRN = "STPPRN"
    STPFTH = "STPFTH"
    STPMTH = "STPMTH"
    PRN = "PRN"
    FTH = "FTH"
    MTH = "MTH"
    HSIB = "HSIB"
    HBRO = "HBRO"
    HSIS = "HSIS"
    NSIB = "NSIB"
    NBRO = "NBRO"
    NSIS = "NSIS"
    SIBINLAW = "SIBINLAW"
    BROINLAW = "BROINLAW"
    SISINLAW = "SISINLAW"
    STPSIB = "STPSIB"
    STPBRO = "STPBRO"
    STPSIS = "STPSIS"
    SIB = "SIB"
    BRO = "BRO"
    SIS = "SIS"
    SPS = "SPS"
    HUSB = "HUSB"
    WIFE = "WIFE"
    SIGOTHR = "SIGOTHR"
    FAMMEMB = "FAMMEMB"
    ROOM = "ROOM"
    DOMPART = "DOMPART"


class FamilyMemberAunt(Enum):
    """
    specDomain: S19748 (C-0-T12206-A19563-S17926-S19748-cpt)
    :cvar AUNT:
    :cvar MAUNT:
    :cvar PAUNT:
    """
    AUNT = "AUNT"
    MAUNT = "MAUNT"
    PAUNT = "PAUNT"


class FamilyMemberCousin(Enum):
    """
    specDomain: S19749 (C-0-T12206-A19563-S17926-S19749-cpt)
    :cvar COUSN:
    :cvar MCOUSN:
    :cvar PCOUSN:
    """
    COUSN = "COUSN"
    MCOUSN = "MCOUSN"
    PCOUSN = "PCOUSN"


class FamilyMemberUncle(Enum):
    """
    specDomain: S19753 (C-0-T12206-A19563-S17926-S19753-cpt)
    :cvar UNCLE:
    :cvar MUNCLE:
    :cvar PUNCLE:
    """
    UNCLE = "UNCLE"
    MUNCLE = "MUNCLE"
    PUNCLE = "PUNCLE"


class FamilyPracticeProviderCodes(Enum):
    """
    specDomain: S20118 (C-0-T19465-S20096-S20118-cpt)
    :cvar VALUE_207_Q00000_X:
    :cvar VALUE_207_QA0401_X:
    :cvar VALUE_207_QA0000_X:
    :cvar VALUE_207_QA0505_X:
    :cvar VALUE_207_QG0300_X:
    :cvar VALUE_207_QS0010_X:
    """
    VALUE_207_Q00000_X = "207Q00000X"
    VALUE_207_QA0401_X = "207QA0401X"
    VALUE_207_QA0000_X = "207QA0000X"
    VALUE_207_QA0505_X = "207QA0505X"
    VALUE_207_QG0300_X = "207QG0300X"
    VALUE_207_QS0010_X = "207QS0010X"


class FirstFillCompletePharmacySupplyType(Enum):
    """
    specDomain: S16210 (C-0-T13953-A13954-A16208-S16209-S16210-cpt)
    :cvar FFC:
    :cvar FFCS:
    """
    FFC = "FFC"
    FFCS = "FFCS"


class FirstFillPartialPharmacySupplyType(Enum):
    """
    specDomain: S17479 (C-0-T13953-A13954-A16208-S16209-S17479-cpt)
    :cvar FFS:
    :cvar FFCS:
    :cvar TFS:
    :cvar FFPS:
    """
    FFS = "FFS"
    FFCS = "FFCS"
    TFS = "TFS"
    FFPS = "FFPS"


class FirstFillPharmacySupplyType(Enum):
    """
    specDomain: S16209 (C-0-T13953-A13954-A16208-S16209-cpt)
    :cvar FFC:
    :cvar FFCS:
    :cvar FFS:
    :cvar TFS:
    :cvar FFPS:
    :cvar FF:
    :cvar FFP:
    :cvar TF:
    """
    FFC = "FFC"
    FFCS = "FFCS"
    FFS = "FFS"
    TFS = "TFS"
    FFPS = "FFPS"
    FF = "FF"
    FFP = "FFP"
    TF = "TF"


class Flush(Enum):
    """
    abstDomain: A14594 (C-0-T14581-A16931-A14594-cpt)
    :cvar IVFLUSH:
    """
    IVFLUSH = "IVFLUSH"


class FoamDrugForm(Enum):
    """
    specDomain: S14546 (C-0-T19651-A14411-A14412-A14545-S14546-cpt)
    :cvar VAGFOAM:
    :cvar VAGFOAMAPL:
    :cvar FOAM:
    :cvar FOAMAPL:
    :cvar RECFORM:
    """
    VAGFOAM = "VAGFOAM"
    VAGFOAMAPL = "VAGFOAMAPL"
    FOAM = "FOAM"
    FOAMAPL = "FOAMAPL"
    RECFORM = "RECFORM"


class FontStyle(Enum):
    """
    abstDomain: A19603 (C-0-T19602-A19603-cpt)
    :cvar BOLD:
    :cvar EMPHASIS:
    :cvar ITALICS:
    :cvar UNDERLINE:
    """
    BOLD = "bold"
    EMPHASIS = "emphasis"
    ITALICS = "italics"
    UNDERLINE = "underline"


class FosterChild(Enum):
    """
    specDomain: S11565 (C-0-T12206-A19563-S17926-S16360-S11565-cpt)
    :cvar CHLDFOST:
    :cvar DAUFOST:
    :cvar SONFOST:
    """
    CHLDFOST = "CHLDFOST"
    DAUFOST = "DAUFOST"
    SONFOST = "SONFOST"


class GiclinicPracticeSetting(Enum):
    """
    specDomain: S10934 (C-0-T12206-A17660-A19450-A10588-S10589-S10934-cpt)
    :cvar GI:
    :cvar PEDGI:
    """
    GI = "GI"
    PEDGI = "PEDGI"


class GidiagTherPracticeSetting(Enum):
    """
    specDomain: S10906 (C-0-T12206-A17660-A19450-A10588-S10902-S10906-cpt)
    :cvar GIDX:
    :cvar VALUE_261_QE0800_N:
    :cvar ENDOS:
    """
    GIDX = "GIDX"
    VALUE_261_QE0800_N = "261QE0800N"
    ENDOS = "ENDOS"


class Gtsabbreviation(Enum):
    """
    vocSet: T10720 (C-0-T10720-cpt)
    :cvar JHCHREAS:
    :cvar JHCHRGFR:
    :cvar JHCHRNEW:
    :cvar JHCHRPEN:
    :cvar JHCHRXME:
    :cvar JHCHRXMS:
    :cvar JHNUS:
    :cvar JHNUSCLM:
    :cvar JHNUSIND:
    :cvar JHNUSIND1:
    :cvar JHNUSIND5:
    :cvar JHNUSLBR:
    :cvar JHNUSMEM:
    :cvar JHNUSMEM5:
    :cvar JHNUSMEM6:
    :cvar JHNUSMLK:
    :cvar JHNUSPRE:
    :cvar JHNUSTKS:
    :cvar JHNUSTKS5:
    :cvar JHNUSVET:
    :cvar JH:
    :cvar AM:
    :cvar BID:
    :cvar JB:
    :cvar JE:
    :cvar PM:
    :cvar QID:
    :cvar TID:
    """
    JHCHREAS = "JHCHREAS"
    JHCHRGFR = "JHCHRGFR"
    JHCHRNEW = "JHCHRNEW"
    JHCHRPEN = "JHCHRPEN"
    JHCHRXME = "JHCHRXME"
    JHCHRXMS = "JHCHRXMS"
    JHNUS = "JHNUS"
    JHNUSCLM = "JHNUSCLM"
    JHNUSIND = "JHNUSIND"
    JHNUSIND1 = "JHNUSIND1"
    JHNUSIND5 = "JHNUSIND5"
    JHNUSLBR = "JHNUSLBR"
    JHNUSMEM = "JHNUSMEM"
    JHNUSMEM5 = "JHNUSMEM5"
    JHNUSMEM6 = "JHNUSMEM6"
    JHNUSMLK = "JHNUSMLK"
    JHNUSPRE = "JHNUSPRE"
    JHNUSTKS = "JHNUSTKS"
    JHNUSTKS5 = "JHNUSTKS5"
    JHNUSVET = "JHNUSVET"
    JH = "JH"
    AM = "AM"
    BID = "BID"
    JB = "JB"
    JE = "JE"
    PM = "PM"
    QID = "QID"
    TID = "TID"


class GtsabbreviationHolidays(Enum):
    """
    specDomain: S10725 (C-0-T10720-S10725-cpt)
    :cvar JHCHREAS:
    :cvar JHCHRGFR:
    :cvar JHCHRNEW:
    :cvar JHCHRPEN:
    :cvar JHCHRXME:
    :cvar JHCHRXMS:
    :cvar JHNUS:
    :cvar JHNUSCLM:
    :cvar JHNUSIND:
    :cvar JHNUSIND1:
    :cvar JHNUSIND5:
    :cvar JHNUSLBR:
    :cvar JHNUSMEM:
    :cvar JHNUSMEM5:
    :cvar JHNUSMEM6:
    :cvar JHNUSMLK:
    :cvar JHNUSPRE:
    :cvar JHNUSTKS:
    :cvar JHNUSTKS5:
    :cvar JHNUSVET:
    :cvar JH:
    """
    JHCHREAS = "JHCHREAS"
    JHCHRGFR = "JHCHRGFR"
    JHCHRNEW = "JHCHRNEW"
    JHCHRPEN = "JHCHRPEN"
    JHCHRXME = "JHCHRXME"
    JHCHRXMS = "JHCHRXMS"
    JHNUS = "JHNUS"
    JHNUSCLM = "JHNUSCLM"
    JHNUSIND = "JHNUSIND"
    JHNUSIND1 = "JHNUSIND1"
    JHNUSIND5 = "JHNUSIND5"
    JHNUSLBR = "JHNUSLBR"
    JHNUSMEM = "JHNUSMEM"
    JHNUSMEM5 = "JHNUSMEM5"
    JHNUSMEM6 = "JHNUSMEM6"
    JHNUSMLK = "JHNUSMLK"
    JHNUSPRE = "JHNUSPRE"
    JHNUSTKS = "JHNUSTKS"
    JHNUSTKS5 = "JHNUSTKS5"
    JHNUSVET = "JHNUSVET"
    JH = "JH"


class GtsabbreviationHolidaysChristianRoman(Enum):
    """
    abstDomain: A10726 (C-0-T10720-S10725-A10726-cpt)
    :cvar JHCHREAS:
    :cvar JHCHRGFR:
    :cvar JHCHRNEW:
    :cvar JHCHRPEN:
    :cvar JHCHRXME:
    :cvar JHCHRXMS:
    """
    JHCHREAS = "JHCHREAS"
    JHCHRGFR = "JHCHRGFR"
    JHCHRNEW = "JHCHRNEW"
    JHCHRPEN = "JHCHRPEN"
    JHCHRXME = "JHCHRXME"
    JHCHRXMS = "JHCHRXMS"


class GtsabbreviationHolidaysUsnational(Enum):
    """
    specDomain: S10733 (C-0-T10720-S10725-S10733-cpt)
    :cvar JHNUS:
    :cvar JHNUSCLM:
    :cvar JHNUSIND:
    :cvar JHNUSIND1:
    :cvar JHNUSIND5:
    :cvar JHNUSLBR:
    :cvar JHNUSMEM:
    :cvar JHNUSMEM5:
    :cvar JHNUSMEM6:
    :cvar JHNUSMLK:
    :cvar JHNUSPRE:
    :cvar JHNUSTKS:
    :cvar JHNUSTKS5:
    :cvar JHNUSVET:
    """
    JHNUS = "JHNUS"
    JHNUSCLM = "JHNUSCLM"
    JHNUSIND = "JHNUSIND"
    JHNUSIND1 = "JHNUSIND1"
    JHNUSIND5 = "JHNUSIND5"
    JHNUSLBR = "JHNUSLBR"
    JHNUSMEM = "JHNUSMEM"
    JHNUSMEM5 = "JHNUSMEM5"
    JHNUSMEM6 = "JHNUSMEM6"
    JHNUSMLK = "JHNUSMLK"
    JHNUSPRE = "JHNUSPRE"
    JHNUSTKS = "JHNUSTKS"
    JHNUSTKS5 = "JHNUSTKS5"
    JHNUSVET = "JHNUSVET"


class GasDrugForm(Enum):
    """
    abstDomain: A14568 (C-0-T19651-A14411-A14412-A14568-cpt)
    :cvar GASINHL:
    """
    GASINHL = "GASINHL"


class GasLiquidMixture(Enum):
    """
    abstDomain: A14545 (C-0-T19651-A14411-A14412-A14545-cpt)
    :cvar AER:
    :cvar BAINHL:
    :cvar INHLSOL:
    :cvar MDINHL:
    :cvar NASSPRY:
    :cvar VAGFOAM:
    :cvar VAGFOAMAPL:
    :cvar FOAM:
    :cvar FOAMAPL:
    :cvar RECFORM:
    :cvar DERMSPRY:
    :cvar RECSPRY:
    :cvar VAGSPRY:
    """
    AER = "AER"
    BAINHL = "BAINHL"
    INHLSOL = "INHLSOL"
    MDINHL = "MDINHL"
    NASSPRY = "NASSPRY"
    VAGFOAM = "VAGFOAM"
    VAGFOAMAPL = "VAGFOAMAPL"
    FOAM = "FOAM"
    FOAMAPL = "FOAMAPL"
    RECFORM = "RECFORM"
    DERMSPRY = "DERMSPRY"
    RECSPRY = "RECSPRY"
    VAGSPRY = "VAGSPRY"


class GasSolidSpray(Enum):
    """
    abstDomain: A14559 (C-0-T19651-A14411-A14412-A14559-cpt)
    :cvar INHL:
    :cvar BAINHLPWD:
    :cvar INHLPWD:
    :cvar MDINHLPWD:
    :cvar NASINHL:
    :cvar ORINHL:
    :cvar PWDSPRY:
    :cvar SPRYADAPT:
    """
    INHL = "INHL"
    BAINHLPWD = "BAINHLPWD"
    INHLPWD = "INHLPWD"
    MDINHLPWD = "MDINHLPWD"
    NASINHL = "NASINHL"
    ORINHL = "ORINHL"
    PWDSPRY = "PWDSPRY"
    SPRYADAPT = "SPRYADAPT"


class GastricRoute(Enum):
    """
    abstDomain: A17061 (C-0-T14581-A17021-A17061-cpt)
    :cvar GBINJ:
    :cvar GT:
    :cvar NGT:
    :cvar OGT:
    """
    GBINJ = "GBINJ"
    GT = "GT"
    NGT = "NGT"
    OGT = "OGT"


class GelDrugForm(Enum):
    """
    specDomain: S14442 (C-0-T19651-A14411-A14412-A14441-S14442-cpt)
    :cvar VAGGEL:
    :cvar VGELAPL:
    :cvar GEL:
    :cvar GELAPL:
    :cvar NASGEL:
    :cvar OPGEL:
    :cvar OTGEL:
    :cvar TOPGEL:
    :cvar URETHGEL:
    """
    VAGGEL = "VAGGEL"
    VGELAPL = "VGELAPL"
    GEL = "GEL"
    GELAPL = "GELAPL"
    NASGEL = "NASGEL"
    OPGEL = "OPGEL"
    OTGEL = "OTGEL"
    TOPGEL = "TOPGEL"
    URETHGEL = "URETHGEL"


class GenderStatus(Enum):
    """
    vocSet: T11523 (C-0-T11523-cpt)
    :cvar I:
    :cvar N:
    """
    I = "I"
    N = "N"


class GeneralAcuteCareHospital(Enum):
    """
    specDomain: S10603 (C-0-T12206-A17660-A19450-A10588-S10602-S10603-cpt)
    :cvar VALUE_282_NW0100_N:
    :cvar VALUE_2865_C1500_N:
    :cvar VALUE_2865_M2000_N:
    :cvar VALUE_2865_X1600_N:
    :cvar GACH:
    :cvar VALUE_282_NC2000_N:
    :cvar VALUE_282_NR1301_N:
    """
    VALUE_282_NW0100_N = "282NW0100N"
    VALUE_2865_C1500_N = "2865C1500N"
    VALUE_2865_M2000_N = "2865M2000N"
    VALUE_2865_X1600_N = "2865X1600N"
    GACH = "GACH"
    VALUE_282_NC2000_N = "282NC2000N"
    VALUE_282_NR1301_N = "282NR1301N"


class GeneralAcuteCareHospitalProviderCodes(Enum):
    """
    specDomain: S20737 (C-0-T19465-S20733-S20737-cpt)
    :cvar VALUE_282_N00000_X:
    :cvar VALUE_282_NC2000_X:
    :cvar VALUE_282_NC0060_X:
    :cvar VALUE_282_NR1301_X:
    :cvar VALUE_282_NW0100_X:
    """
    VALUE_282_N00000_X = "282N00000X"
    VALUE_282_NC2000_X = "282NC2000X"
    VALUE_282_NC0060_X = "282NC0060X"
    VALUE_282_NR1301_X = "282NR1301X"
    VALUE_282_NW0100_X = "282NW0100X"


class GeneralAcuteCareHospitalWomen(Enum):
    """
    specDomain: S13798 (C-0-T12206-A17660-A19450-A10588-S10602-S10603-S13798-cpt)
    :cvar VALUE_282_NW0100_N:
    :cvar VALUE_2865_C1500_N:
    :cvar VALUE_2865_M2000_N:
    :cvar VALUE_2865_X1600_N:
    """
    VALUE_282_NW0100_N = "282NW0100N"
    VALUE_2865_C1500_N = "2865C1500N"
    VALUE_2865_M2000_N = "2865M2000N"
    VALUE_2865_X1600_N = "2865X1600N"


class GenericUpdateReasonCode(Enum):
    """
    abstDomain: A19777 (C-0-T14878-A19692-A19777-cpt)
    :cvar FIXDATA:
    :cvar CHGDATA:
    :cvar NEWDATA:
    """
    FIXDATA = "FIXDATA"
    CHGDATA = "CHGDATA"
    NEWDATA = "NEWDATA"


class GenitourinaryRoute(Enum):
    """
    abstDomain: A17066 (C-0-T14581-A17021-A17066-cpt)
    :cvar GUIRR:
    """
    GUIRR = "GUIRR"


class GingivalRoute(Enum):
    """
    abstDomain: A17068 (C-0-T14581-A17021-A17068-cpt)
    :cvar GINGINJ:
    :cvar GIN:
    """
    GINGINJ = "GINGINJ"
    GIN = "GIN"


class GrandChild(Enum):
    """
    specDomain: S19745 (C-0-T12206-A19563-S17926-S19745-cpt)
    :cvar GRNDCHILD:
    :cvar GRNDDAU:
    :cvar GRNDSON:
    """
    GRNDCHILD = "GRNDCHILD"
    GRNDDAU = "GRNDDAU"
    GRNDSON = "GRNDSON"


class Grandparent(Enum):
    """
    specDomain: S16349 (C-0-T12206-A19563-S17926-S16349-cpt)
    :cvar GRPRN:
    :cvar GRFTH:
    :cvar GRMTH:
    :cvar MGRFTH:
    :cvar MGRMTH:
    :cvar MGRPRN:
    :cvar PGRFTH:
    :cvar PGRMTH:
    :cvar PGRPRN:
    """
    GRPRN = "GRPRN"
    GRFTH = "GRFTH"
    GRMTH = "GRMTH"
    MGRFTH = "MGRFTH"
    MGRMTH = "MGRMTH"
    MGRPRN = "MGRPRN"
    PGRFTH = "PGRFTH"
    PGRMTH = "PGRMTH"
    PGRPRN = "PGRPRN"


class GreatGrandparent(Enum):
    """
    specDomain: S19739 (C-0-T12206-A19563-S17926-S19739-cpt)
    :cvar GGRPRN:
    :cvar MGGRFTH:
    :cvar MGGRMTH:
    :cvar MGGRPRN:
    :cvar PGGRFTH:
    :cvar PGGRMTH:
    :cvar PGGRPRN:
    :cvar GGRFTH:
    :cvar GGRMTH:
    """
    GGRPRN = "GGRPRN"
    MGGRFTH = "MGGRFTH"
    MGGRMTH = "MGGRMTH"
    MGGRPRN = "MGGRPRN"
    PGGRFTH = "PGGRFTH"
    PGGRMTH = "PGGRMTH"
    PGGRPRN = "PGGRPRN"
    GGRFTH = "GGRFTH"
    GGRMTH = "GGRMTH"


class GroupProviderCodes(Enum):
    """
    specDomain: S20800 (C-0-T19465-S20800-cpt)
    :cvar VALUE_190000000_X:
    :cvar VALUE_193200000_X:
    :cvar VALUE_193400000_X:
    """
    VALUE_190000000_X = "190000000X"
    VALUE_193200000_X = "193200000X"
    VALUE_193400000_X = "193400000X"


class Hl7AccommodationCode(Enum):
    """
    abstDomain: A19866 (C-0-T13953-A19820-A16130-A19866-cpt)
    :cvar I:
    :cvar P:
    :cvar SP:
    :cvar S:
    :cvar W:
    """
    I = "I"
    P = "P"
    SP = "SP"
    S = "S"
    W = "W"


class Hl7CommitteeIdinRim(Enum):
    """
    vocSet: T10034 (C-0-T10034-cpt)
    :cvar C02:
    :cvar C06:
    :cvar C09:
    :cvar C00:
    :cvar C04:
    :cvar C03:
    :cvar C12:
    :cvar C10:
    :cvar C20:
    :cvar C01:
    :cvar C21:
    """
    C02 = "C02"
    C06 = "C06"
    C09 = "C09"
    C00 = "C00"
    C04 = "C04"
    C03 = "C03"
    C12 = "C12"
    C10 = "C10"
    C20 = "C20"
    C01 = "C01"
    C21 = "C21"


class Hl7ConformanceInclusion(Enum):
    """
    vocSet: T10010 (C-0-T10010-cpt)
    :cvar NR:
    :cvar X:
    :cvar RE:
    :cvar NP:
    :cvar RQ:
    :cvar M:
    """
    NR = "NR"
    X = "X"
    RE = "RE"
    NP = "NP"
    RQ = "RQ"
    M = "M"


class Hl7DefinedRoseProperty(Enum):
    """
    vocSet: T10083 (C-0-T10083-cpt)
    :cvar APPLICATION_ROLE_I:
    :cvar CARDINALITY:
    :cvar MAY_REPEAT:
    :cvar INSTANCED_DTSYMBO:
    :cvar DTSYMBOL:
    :cvar DEVELOPING_COMMIT:
    :cvar ORGANIZATION:
    :cvar END_STATE:
    :cvar HMD:
    :cvar ZHX_ID:
    :cvar ID:
    :cvar DELETE_FROM_MIM:
    :cvar MIM_ID:
    :cvar MANDATORY_INCLUSI:
    :cvar MSG_ID:
    :cvar MODEL_DATE:
    :cvar MODEL_DESCRIPTION:
    :cvar MODEL_ID:
    :cvar MODEL_NAME:
    :cvar MODEL_VERSION:
    :cvar IS_PRIMITIVE_DT:
    :cvar RCV_RESP:
    :cvar IS_REFERENCE_DT:
    :cvar RESP_COMM_ID:
    :cvar START_STATE:
    :cvar STATE_ATTRIBUTE:
    :cvar STATE_TRANSITION:
    :cvar IS_SUBJECT_CLASS:
    :cvar V23_FIELDS:
    :cvar V23_DATATYPE:
    :cvar VOCAB_DOMAIN:
    :cvar VOCAB_STRENGTH:
    """
    APPLICATION_ROLE_I = "ApplicationRoleI"
    CARDINALITY = "Cardinality"
    MAY_REPEAT = "MayRepeat"
    INSTANCED_DTSYMBO = "InstancedDTsymbo"
    DTSYMBOL = "DTsymbol"
    DEVELOPING_COMMIT = "DevelopingCommit"
    ORGANIZATION = "Organization"
    END_STATE = "EndState"
    HMD = "HMD"
    ZHX_ID = "zhxID"
    ID = "ID"
    DELETE_FROM_MIM = "DeleteFromMIM"
    MIM_ID = "MIM_id"
    MANDATORY_INCLUSI = "MandatoryInclusi"
    MSG_ID = "MsgID"
    MODEL_DATE = "ModelDate"
    MODEL_DESCRIPTION = "ModelDescription"
    MODEL_ID = "ModelID"
    MODEL_NAME = "ModelName"
    MODEL_VERSION = "ModelVersion"
    IS_PRIMITIVE_DT = "IsPrimitiveDT"
    RCV_RESP = "RcvResp"
    IS_REFERENCE_DT = "IsReferenceDT"
    RESP_COMM_ID = "RespComm_id"
    START_STATE = "StartState"
    STATE_ATTRIBUTE = "StateAttribute"
    STATE_TRANSITION = "StateTransition"
    IS_SUBJECT_CLASS = "IsSubjectClass"
    V23_FIELDS = "V23_Fields"
    V23_DATATYPE = "V23_Datatype"
    VOCAB_DOMAIN = "Vocab_domain"
    VOCAB_STRENGTH = "Vocab_strength"


class Hl7ItsversionCode(Enum):
    """
    vocSet: T19449 (C-0-T19449-cpt)
    :cvar XMLV1_PR1:
    """
    XMLV1_PR1 = "XMLV1PR1"


class Hl7StandardVersionCode(Enum):
    """
    vocSet: T19373 (C-0-T19373-cpt)
    :cvar ACT_RELATIONSHIP_EXPECTED_SUBSET:
    :cvar ACT_RELATIONSHIP_PAST_SUBSET:
    :cvar PARTICIPATION_SUBSET:
    :cvar FUTURE:
    :cvar LAST:
    :cvar NEXT:
    :cvar FIRST:
    :cvar FUTSUM:
    :cvar MAX:
    :cvar MIN:
    :cvar RECENT:
    :cvar PAST:
    :cvar PREVSUM:
    :cvar SUM:
    """
    ACT_RELATIONSHIP_EXPECTED_SUBSET = "ActRelationshipExpectedSubset"
    ACT_RELATIONSHIP_PAST_SUBSET = "ActRelationshipPastSubset"
    PARTICIPATION_SUBSET = "_ParticipationSubset"
    FUTURE = "FUTURE"
    LAST = "LAST"
    NEXT = "NEXT"
    FIRST = "FIRST"
    FUTSUM = "FUTSUM"
    MAX = "MAX"
    MIN = "MIN"
    RECENT = "RECENT"
    PAST = "PAST"
    PREVSUM = "PREVSUM"
    SUM = "SUM"


class Hl7UpdateMode(Enum):
    """
    vocSet: T10018 (C-0-T10018-cpt)
    :cvar ESA:
    :cvar ESAC:
    :cvar ESC:
    :cvar ESD:
    :cvar D:
    :cvar I:
    :cvar K:
    :cvar R:
    :cvar V:
    """
    ESA = "ESA"
    ESAC = "ESAC"
    ESC = "ESC"
    ESD = "ESD"
    D = "D"
    I = "I"
    K = "K"
    R = "R"
    V = "V"


class HairRoute(Enum):
    """
    abstDomain: A17071 (C-0-T14581-A17021-A17071-cpt)
    :cvar SHAMPOO:
    :cvar HAIR:
    """
    SHAMPOO = "SHAMPOO"
    HAIR = "HAIR"


class HalfSibling(Enum):
    """
    specDomain: S19776 (C-0-T12206-A19563-S17926-S11567-S19776-cpt)
    :cvar HSIB:
    :cvar HBRO:
    :cvar HSIS:
    """
    HSIB = "HSIB"
    HBRO = "HBRO"
    HSIS = "HSIS"


class HealthInformationSpecialistOrTechnologistHipaa(Enum):
    """
    abstDomain: A13669 (C-0-T13129-A13130-A13644-A13669-cpt)
    :cvar VALUE_246_YC3301_N:
    :cvar VALUE_246_YC3302_N:
    :cvar VALUE_246_YR1600_N:
    """
    VALUE_246_YC3301_N = "246YC3301N"
    VALUE_246_YC3302_N = "246YC3302N"
    VALUE_246_YR1600_N = "246YR1600N"


class HealthInformationTechnicianHipaa(Enum):
    """
    abstDomain: A13703 (C-0-T13129-A13130-A13644-A13703-cpt)
    :cvar VALUE_2470_A2800_N:
    """
    VALUE_2470_A2800_N = "2470A2800N"


class HealthcareProviderAgencyHipaa(Enum):
    """
    abstDomain: A13717 (C-0-T13129-A13715-A13716-A13717-cpt)
    :cvar VALUE_2514_C0400_N:
    :cvar VALUE_2514_H0200_N:
    :cvar VALUE_2514_H0201_N:
    :cvar VALUE_2514_H0300_N:
    :cvar VALUE_2514_N1101_N:
    :cvar VALUE_2514_P0906_N:
    :cvar VALUE_2514_V0001_N:
    """
    VALUE_2514_C0400_N = "2514C0400N"
    VALUE_2514_H0200_N = "2514H0200N"
    VALUE_2514_H0201_N = "2514H0201N"
    VALUE_2514_H0300_N = "2514H0300N"
    VALUE_2514_N1101_N = "2514N1101N"
    VALUE_2514_P0906_N = "2514P0906N"
    VALUE_2514_V0001_N = "2514V0001N"


class HeightSurfaceAreaAlert(Enum):
    """
    abstDomain: A17795 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16665-A17795-cpt)
    :cvar DOSEHINDSA:
    :cvar DOSELINDSA:
    """
    DOSEHINDSA = "DOSEHINDSA"
    DOSELINDSA = "DOSELINDSA"


class HemClinPracticeSetting(Enum):
    """
    specDomain: S10936 (C-0-T12206-A17660-A19450-A10588-S10589-S10936-cpt)
    :cvar HEM:
    :cvar PEDHEM:
    """
    HEM = "HEM"
    PEDHEM = "PEDHEM"


class HomeAddressUse(Enum):
    """
    specDomain: S10628 (C-0-T201-A190-S10628-cpt)
    :cvar H:
    :cvar HP:
    :cvar HV:
    """
    H = "H"
    HP = "HP"
    HV = "HV"


class Homeless(Enum):
    """
    specDomain: S22193 (C-0-T220-S22193-cpt)
    :cvar HL:
    :cvar M:
    :cvar T:
    """
    HL = "HL"
    M = "M"
    T = "T"


class HospitalPracticeSetting(Enum):
    """
    specDomain: S10602 (C-0-T12206-A17660-A19450-A10588-S10602-cpt)
    :cvar CHR:
    :cvar VALUE_281_PC2000_N:
    :cvar VALUE_282_NW0100_N:
    :cvar VALUE_2865_C1500_N:
    :cvar VALUE_2865_M2000_N:
    :cvar VALUE_2865_X1600_N:
    :cvar GACH:
    :cvar VALUE_282_NC2000_N:
    :cvar VALUE_282_NR1301_N:
    :cvar MHSP:
    :cvar RH:
    :cvar VALUE_283_XC2000_N:
    :cvar HOSP:
    :cvar PSYCHF:
    """
    CHR = "CHR"
    VALUE_281_PC2000_N = "281PC2000N"
    VALUE_282_NW0100_N = "282NW0100N"
    VALUE_2865_C1500_N = "2865C1500N"
    VALUE_2865_M2000_N = "2865M2000N"
    VALUE_2865_X1600_N = "2865X1600N"
    GACH = "GACH"
    VALUE_282_NC2000_N = "282NC2000N"
    VALUE_282_NR1301_N = "282NR1301N"
    MHSP = "MHSP"
    RH = "RH"
    VALUE_283_XC2000_N = "283XC2000N"
    HOSP = "HOSP"
    PSYCHF = "PSYCHF"


class HospitalUnitPracticeSetting(Enum):
    """
    specDomain: S10596 (C-0-T12206-A17660-A19450-A10588-S10596-cpt)
    :cvar ER:
    :cvar ETU:
    :cvar PEDICU:
    :cvar PEDNICU:
    :cvar ICU:
    :cvar PEDU:
    :cvar HU:
    :cvar BMTU:
    :cvar CHEST:
    :cvar CCU:
    :cvar EPIL:
    :cvar HD:
    :cvar NCCS:
    :cvar NS:
    :cvar VALUE_273_R00000_N:
    :cvar PHU:
    :cvar VALUE_273_Y00000_N:
    :cvar RHU:
    :cvar SLEEP:
    """
    ER = "ER"
    ETU = "ETU"
    PEDICU = "PEDICU"
    PEDNICU = "PEDNICU"
    ICU = "ICU"
    PEDU = "PEDU"
    HU = "HU"
    BMTU = "BMTU"
    CHEST = "CHEST"
    CCU = "CCU"
    EPIL = "EPIL"
    HD = "HD"
    NCCS = "NCCS"
    NS = "NS"
    VALUE_273_R00000_N = "273R00000N"
    PHU = "PHU"
    VALUE_273_Y00000_N = "273Y00000N"
    RHU = "RHU"
    SLEEP = "SLEEP"


class HospitalUnitsProviderCodes(Enum):
    """
    specDomain: S20728 (C-0-T19465-S20728-cpt)
    :cvar VALUE_270000000_X:
    :cvar VALUE_275_N00000_X:
    :cvar VALUE_273_R00000_X:
    :cvar VALUE_273_Y00000_X:
    :cvar VALUE_276400000_X:
    """
    VALUE_270000000_X = "270000000X"
    VALUE_275_N00000_X = "275N00000X"
    VALUE_273_R00000_X = "273R00000X"
    VALUE_273_Y00000_X = "273Y00000X"
    VALUE_276400000_X = "276400000X"


class HospitalsProviderCodes(Enum):
    """
    specDomain: S20733 (C-0-T19465-S20733-cpt)
    :cvar VALUE_281_P00000_X:
    :cvar VALUE_281_PC2000_X:
    :cvar VALUE_282_N00000_X:
    :cvar VALUE_282_NC2000_X:
    :cvar VALUE_282_NC0060_X:
    :cvar VALUE_282_NR1301_X:
    :cvar VALUE_282_NW0100_X:
    :cvar VALUE_286500000_X:
    :cvar VALUE_2865_C1500_X:
    :cvar VALUE_2865_M2000_X:
    :cvar VALUE_2865_X1600_X:
    :cvar VALUE_283_X00000_X:
    :cvar VALUE_283_XC2000_X:
    :cvar VALUE_280000000_X:
    :cvar VALUE_287300000_X:
    :cvar VALUE_283_Q00000_X:
    :cvar VALUE_284300000_X:
    """
    VALUE_281_P00000_X = "281P00000X"
    VALUE_281_PC2000_X = "281PC2000X"
    VALUE_282_N00000_X = "282N00000X"
    VALUE_282_NC2000_X = "282NC2000X"
    VALUE_282_NC0060_X = "282NC0060X"
    VALUE_282_NR1301_X = "282NR1301X"
    VALUE_282_NW0100_X = "282NW0100X"
    VALUE_286500000_X = "286500000X"
    VALUE_2865_C1500_X = "2865C1500X"
    VALUE_2865_M2000_X = "2865M2000X"
    VALUE_2865_X1600_X = "2865X1600X"
    VALUE_283_X00000_X = "283X00000X"
    VALUE_283_XC2000_X = "283XC2000X"
    VALUE_280000000_X = "280000000X"
    VALUE_287300000_X = "287300000X"
    VALUE_283_Q00000_X = "283Q00000X"
    VALUE_284300000_X = "284300000X"


class HtmlLinkType(Enum):
    """
    vocSet: T11017 (C-0-T11017-cpt)
    :cvar ALTERNATE:
    :cvar APPENDIX:
    :cvar BOOKMARK:
    :cvar CHAPTER:
    :cvar CONTENTS:
    :cvar COPYRIGHT:
    :cvar GLOSSARY:
    :cvar HELP:
    :cvar INDEX:
    :cvar NEXT:
    :cvar PREV:
    :cvar SECTION:
    :cvar START:
    :cvar STYLESHEET:
    :cvar SUBSECTION:
    """
    ALTERNATE = "alternate"
    APPENDIX = "appendix"
    BOOKMARK = "bookmark"
    CHAPTER = "chapter"
    CONTENTS = "contents"
    COPYRIGHT = "copyright"
    GLOSSARY = "glossary"
    HELP = "help"
    INDEX = "index"
    NEXT = "next"
    PREV = "prev"
    SECTION = "section"
    START = "start"
    STYLESHEET = "stylesheet"
    SUBSECTION = "subsection"


class HumanSubstanceAdministrationSite(Enum):
    """
    abstDomain: A19724 (C-0-T16537-A16538-A19724-cpt)
    :cvar BE:
    :cvar OU:
    :cvar BU:
    :cvar LACF:
    :cvar LAC:
    :cvar LA:
    :cvar LD:
    :cvar LE:
    :cvar LEJ:
    :cvar OS:
    :cvar LF:
    :cvar LG:
    :cvar LH:
    :cvar LIJ:
    :cvar LLAQ:
    :cvar LLFA:
    :cvar LMFA:
    :cvar LN:
    :cvar LPC:
    :cvar LSC:
    :cvar LT:
    :cvar LUAQ:
    :cvar LUA:
    :cvar LUFA:
    :cvar LVL:
    :cvar LVG:
    :cvar PA:
    :cvar PERIN:
    :cvar RACF:
    :cvar RAC:
    :cvar RA:
    :cvar RD:
    :cvar RE:
    :cvar REJ:
    :cvar OD:
    :cvar RF:
    :cvar RG:
    :cvar RH:
    :cvar RIJ:
    :cvar RLAQ:
    :cvar RLFA:
    :cvar RMFA:
    :cvar RPC:
    :cvar RSC:
    :cvar RT:
    :cvar RUAQ:
    :cvar RUA:
    :cvar RUFA:
    :cvar RVL:
    :cvar RVG:
    :cvar BN:
    """
    BE = "BE"
    OU = "OU"
    BU = "BU"
    LACF = "LACF"
    LAC = "LAC"
    LA = "LA"
    LD = "LD"
    LE = "LE"
    LEJ = "LEJ"
    OS = "OS"
    LF = "LF"
    LG = "LG"
    LH = "LH"
    LIJ = "LIJ"
    LLAQ = "LLAQ"
    LLFA = "LLFA"
    LMFA = "LMFA"
    LN = "LN"
    LPC = "LPC"
    LSC = "LSC"
    LT = "LT"
    LUAQ = "LUAQ"
    LUA = "LUA"
    LUFA = "LUFA"
    LVL = "LVL"
    LVG = "LVG"
    PA = "PA"
    PERIN = "PERIN"
    RACF = "RACF"
    RAC = "RAC"
    RA = "RA"
    RD = "RD"
    RE = "RE"
    REJ = "REJ"
    OD = "OD"
    RF = "RF"
    RG = "RG"
    RH = "RH"
    RIJ = "RIJ"
    RLAQ = "RLAQ"
    RLFA = "RLFA"
    RMFA = "RMFA"
    RPC = "RPC"
    RSC = "RSC"
    RT = "RT"
    RUAQ = "RUAQ"
    RUA = "RUA"
    RUFA = "RUFA"
    RVL = "RVL"
    RVG = "RVG"
    BN = "BN"


class IcupracticeSetting(Enum):
    """
    specDomain: S10599 (C-0-T12206-A17660-A19450-A10588-S10596-S10599-cpt)
    :cvar PEDICU:
    :cvar PEDNICU:
    :cvar ICU:
    """
    PEDICU = "PEDICU"
    PEDNICU = "PEDNICU"
    ICU = "ICU"


class IdclinPracticeSetting(Enum):
    """
    specDomain: S10939 (C-0-T12206-A17660-A19450-A10588-S10589-S10939-cpt)
    :cvar INFD:
    :cvar PEDID:
    """
    INFD = "INFD"
    PEDID = "PEDID"


class ImageMediaType(Enum):
    """
    abstDomain: A14839 (C-0-T14824-A14839-cpt)
    :cvar IMAGE_G3FAX:
    :cvar IMAGE_GIF:
    :cvar IMAGE_JPEG:
    :cvar IMAGE_PNG:
    :cvar IMAGE_TIFF:
    """
    IMAGE_G3FAX = "image/g3fax"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_TIFF = "image/tiff"


class Implantation(Enum):
    """
    abstDomain: A14598 (C-0-T14581-A16931-A14598-cpt)
    :cvar IDIMPLNT:
    :cvar IVITIMPLNT:
    :cvar SQIMPLNT:
    """
    IDIMPLNT = "IDIMPLNT"
    IVITIMPLNT = "IVITIMPLNT"
    SQIMPLNT = "SQIMPLNT"


class InactiveEditStatus(Enum):
    """
    specDomain: S11044 (C-0-T11040-S11044-cpt)
    :cvar I:
    """
    I = "I"


class IncidentalServiceDeliveryLocationRoleType(Enum):
    """
    abstDomain: A19451 (C-0-T12206-A17660-A19451-cpt)
    :cvar COMM:
    :cvar PTRES:
    :cvar ACC:
    :cvar SCHOOL:
    :cvar WORK:
    """
    COMM = "COMM"
    PTRES = "PTRES"
    ACC = "ACC"
    SCHOOL = "SCHOOL"
    WORK = "WORK"


class InclusionNotMandatory(Enum):
    """
    abstDomain: A10012 (C-0-T10010-A10012-cpt)
    :cvar NR:
    :cvar X:
    :cvar RE:
    :cvar NP:
    :cvar RQ:
    """
    NR = "NR"
    X = "X"
    RE = "RE"
    NP = "NP"
    RQ = "RQ"


class InclusionNotRequired(Enum):
    """
    specDomain: S10015 (C-0-T10010-A10012-S10015-cpt)
    :cvar NR:
    :cvar X:
    :cvar RE:
    """
    NR = "NR"
    X = "X"
    RE = "RE"


class IndividualInsuredCoveredPartyRoleType(Enum):
    """
    abstDomain: A19813 (C-0-T12206-A19809-A19805-A19813-cpt)
    :cvar STUD:
    :cvar FSTUD:
    :cvar PSTUD:
    :cvar COCBEN:
    :cvar RETIREE:
    """
    STUD = "STUD"
    FSTUD = "FSTUD"
    PSTUD = "PSTUD"
    COCBEN = "COCBEN"
    RETIREE = "RETIREE"


class IndividualPackageEntityType(Enum):
    """
    abstDomain: A16176 (C-0-T16040-A16041-A19867-A16143-S16144-A16152-A16176-cpt)
    :cvar AMP:
    :cvar MINIM:
    :cvar NEBAMP:
    :cvar OVUL:
    """
    AMP = "AMP"
    MINIM = "MINIM"
    NEBAMP = "NEBAMP"
    OVUL = "OVUL"


class Infusion(Enum):
    """
    abstDomain: A14602 (C-0-T14581-A16931-A14602-cpt)
    :cvar IV:
    :cvar IVC:
    :cvar IVCC:
    :cvar IVCI:
    :cvar PCA:
    :cvar EPI:
    :cvar IA:
    :cvar IC:
    :cvar ICOR:
    :cvar IOSSC:
    :cvar IT:
    :cvar IVASCINFUS:
    :cvar SQINFUS:
    """
    IV = "IV"
    IVC = "IVC"
    IVCC = "IVCC"
    IVCI = "IVCI"
    PCA = "PCA"
    EPI = "EPI"
    IA = "IA"
    IC = "IC"
    ICOR = "ICOR"
    IOSSC = "IOSSC"
    IT = "IT"
    IVASCINFUS = "IVASCINFUS"
    SQINFUS = "SQINFUS"


class InhalantDrugForm(Enum):
    """
    specDomain: S14560 (C-0-T19651-A14411-A14412-A14559-S14560-cpt)
    :cvar INHL:
    :cvar BAINHLPWD:
    :cvar INHLPWD:
    :cvar MDINHLPWD:
    :cvar NASINHL:
    :cvar ORINHL:
    """
    INHL = "INHL"
    BAINHLPWD = "BAINHLPWD"
    INHLPWD = "INHLPWD"
    MDINHLPWD = "MDINHLPWD"
    NASINHL = "NASINHL"
    ORINHL = "ORINHL"


class Inhalation(Enum):
    """
    abstDomain: A14615 (C-0-T14581-A16931-A14615-cpt)
    :cvar NASINHL:
    :cvar NASINHLC:
    :cvar NP:
    :cvar NEB:
    :cvar NASNEB:
    :cvar ORNEB:
    :cvar ORINHL:
    :cvar ORIFINHL:
    :cvar REBREATH:
    :cvar IPPB:
    :cvar TRACH:
    :cvar VENT:
    :cvar VENTMASK:
    """
    NASINHL = "NASINHL"
    NASINHLC = "NASINHLC"
    NP = "NP"
    NEB = "NEB"
    NASNEB = "NASNEB"
    ORNEB = "ORNEB"
    ORINHL = "ORINHL"
    ORIFINHL = "ORIFINHL"
    REBREATH = "REBREATH"
    IPPB = "IPPB"
    TRACH = "TRACH"
    VENT = "VENT"
    VENTMASK = "VENTMASK"


class InhalerMedicalDevice(Enum):
    """
    specDomain: S16196 (C-0-T16040-A16041-A19867-A16188-A16189-S16196-cpt)
    :cvar INH:
    :cvar DSKUNH:
    :cvar DSKS:
    :cvar TRBINH:
    """
    INH = "INH"
    DSKUNH = "DSKUNH"
    DSKS = "DSKS"
    TRBINH = "TRBINH"


class Injection(Enum):
    """
    abstDomain: A14628 (C-0-T14581-A16931-A14628-cpt)
    :cvar IAINJ:
    :cvar IAINJP:
    :cvar IAINJSP:
    :cvar ICARDINJ:
    :cvar ICARINJP:
    :cvar ICARDINJRP:
    :cvar ICARDINJSP:
    :cvar ICORONINJ:
    :cvar ICORONINJP:
    :cvar IM:
    :cvar IMD:
    :cvar IMZ:
    :cvar IVINJ:
    :cvar IVINJBOL:
    :cvar IVPUSH:
    :cvar IVRPUSH:
    :cvar IVSPUSH:
    :cvar AMNINJ:
    :cvar BILINJ:
    :cvar CERVINJ:
    :cvar ENDOSININJ:
    :cvar EPIDURINJ:
    :cvar EPIINJ:
    :cvar EPINJSP:
    :cvar EXTRAMNINJ:
    :cvar EXTCORPINJ:
    :cvar CHOLINJ:
    :cvar GBINJ:
    :cvar GINGINJ:
    :cvar HEMOPORT:
    :cvar IPUMPINJ:
    :cvar INTERMENINJ:
    :cvar INTERSTITINJ:
    :cvar IABDINJ:
    :cvar IARTINJ:
    :cvar IBURSINJ:
    :cvar ICARTINJ:
    :cvar ICAUDINJ:
    :cvar ICAVINJ:
    :cvar ICAVITINJ:
    :cvar ICEREBINJ:
    :cvar IUINJC:
    :cvar ICISTERNINJ:
    :cvar ICORPCAVINJ:
    :cvar IDINJ:
    :cvar IDISCINJ:
    :cvar IDUCTINJ:
    :cvar IDURINJ:
    :cvar IEPIDINJ:
    :cvar IEPITHINJ:
    :cvar ILESINJ:
    :cvar ILUMINJ:
    :cvar ILYMPJINJ:
    :cvar IMEDULINJ:
    :cvar IOINJ:
    :cvar IOSSINJ:
    :cvar IOVARINJ:
    :cvar IPCARDINJ:
    :cvar IPERINJ:
    :cvar IPLRINJ:
    :cvar IPROSTINJ:
    :cvar IPINJ:
    :cvar ISINJ:
    :cvar ISTERINJ:
    :cvar ISYNINJ:
    :cvar ITENDINJ:
    :cvar ITESTINJ:
    :cvar ITINJ:
    :cvar ITHORINJ:
    :cvar ITUBINJ:
    :cvar ITUMINJ:
    :cvar ITYMPINJ:
    :cvar IURETINJ:
    :cvar IUINJ:
    :cvar IVASCINJ:
    :cvar IVENTINJ:
    :cvar IVESINJ:
    :cvar IVITINJ:
    :cvar PNSINJ:
    :cvar PARENTINJ:
    :cvar PAINJ:
    :cvar PDURINJ:
    :cvar PNINJ:
    :cvar PDONTINJ:
    :cvar PDPINJ:
    :cvar RBINJ:
    :cvar SOFTISINJ:
    :cvar SUBARACHINJ:
    :cvar SCINJ:
    :cvar SQ:
    :cvar SLESINJ:
    :cvar SUBMUCINJ:
    :cvar TRPLACINJ:
    :cvar TRTRACHINJ:
    :cvar URETINJ:
    :cvar URETHINJ:
    :cvar BLADINJ:
    """
    IAINJ = "IAINJ"
    IAINJP = "IAINJP"
    IAINJSP = "IAINJSP"
    ICARDINJ = "ICARDINJ"
    ICARINJP = "ICARINJP"
    ICARDINJRP = "ICARDINJRP"
    ICARDINJSP = "ICARDINJSP"
    ICORONINJ = "ICORONINJ"
    ICORONINJP = "ICORONINJP"
    IM = "IM"
    IMD = "IMD"
    IMZ = "IMZ"
    IVINJ = "IVINJ"
    IVINJBOL = "IVINJBOL"
    IVPUSH = "IVPUSH"
    IVRPUSH = "IVRPUSH"
    IVSPUSH = "IVSPUSH"
    AMNINJ = "AMNINJ"
    BILINJ = "BILINJ"
    CERVINJ = "CERVINJ"
    ENDOSININJ = "ENDOSININJ"
    EPIDURINJ = "EPIDURINJ"
    EPIINJ = "EPIINJ"
    EPINJSP = "EPINJSP"
    EXTRAMNINJ = "EXTRAMNINJ"
    EXTCORPINJ = "EXTCORPINJ"
    CHOLINJ = "CHOLINJ"
    GBINJ = "GBINJ"
    GINGINJ = "GINGINJ"
    HEMOPORT = "HEMOPORT"
    IPUMPINJ = "IPUMPINJ"
    INTERMENINJ = "INTERMENINJ"
    INTERSTITINJ = "INTERSTITINJ"
    IABDINJ = "IABDINJ"
    IARTINJ = "IARTINJ"
    IBURSINJ = "IBURSINJ"
    ICARTINJ = "ICARTINJ"
    ICAUDINJ = "ICAUDINJ"
    ICAVINJ = "ICAVINJ"
    ICAVITINJ = "ICAVITINJ"
    ICEREBINJ = "ICEREBINJ"
    IUINJC = "IUINJC"
    ICISTERNINJ = "ICISTERNINJ"
    ICORPCAVINJ = "ICORPCAVINJ"
    IDINJ = "IDINJ"
    IDISCINJ = "IDISCINJ"
    IDUCTINJ = "IDUCTINJ"
    IDURINJ = "IDURINJ"
    IEPIDINJ = "IEPIDINJ"
    IEPITHINJ = "IEPITHINJ"
    ILESINJ = "ILESINJ"
    ILUMINJ = "ILUMINJ"
    ILYMPJINJ = "ILYMPJINJ"
    IMEDULINJ = "IMEDULINJ"
    IOINJ = "IOINJ"
    IOSSINJ = "IOSSINJ"
    IOVARINJ = "IOVARINJ"
    IPCARDINJ = "IPCARDINJ"
    IPERINJ = "IPERINJ"
    IPLRINJ = "IPLRINJ"
    IPROSTINJ = "IPROSTINJ"
    IPINJ = "IPINJ"
    ISINJ = "ISINJ"
    ISTERINJ = "ISTERINJ"
    ISYNINJ = "ISYNINJ"
    ITENDINJ = "ITENDINJ"
    ITESTINJ = "ITESTINJ"
    ITINJ = "ITINJ"
    ITHORINJ = "ITHORINJ"
    ITUBINJ = "ITUBINJ"
    ITUMINJ = "ITUMINJ"
    ITYMPINJ = "ITYMPINJ"
    IURETINJ = "IURETINJ"
    IUINJ = "IUINJ"
    IVASCINJ = "IVASCINJ"
    IVENTINJ = "IVENTINJ"
    IVESINJ = "IVESINJ"
    IVITINJ = "IVITINJ"
    PNSINJ = "PNSINJ"
    PARENTINJ = "PARENTINJ"
    PAINJ = "PAINJ"
    PDURINJ = "PDURINJ"
    PNINJ = "PNINJ"
    PDONTINJ = "PDONTINJ"
    PDPINJ = "PDPINJ"
    RBINJ = "RBINJ"
    SOFTISINJ = "SOFTISINJ"
    SUBARACHINJ = "SUBARACHINJ"
    SCINJ = "SCINJ"
    SQ = "SQ"
    SLESINJ = "SLESINJ"
    SUBMUCINJ = "SUBMUCINJ"
    TRPLACINJ = "TRPLACINJ"
    TRTRACHINJ = "TRTRACHINJ"
    URETINJ = "URETINJ"
    URETHINJ = "URETHINJ"
    BLADINJ = "BLADINJ"


class InjectionMedicalDevice(Enum):
    """
    abstDomain: A16191 (C-0-T16040-A16041-A19867-A16188-A16189-A16191-cpt)
    :cvar AINJ:
    :cvar PEN:
    :cvar SYR:
    """
    AINJ = "AINJ"
    PEN = "PEN"
    SYR = "SYR"


class Insertion(Enum):
    """
    abstDomain: A14687 (C-0-T14581-A16931-A14687-cpt)
    :cvar CERVINS:
    :cvar IOSURGINS:
    :cvar IU:
    :cvar LPINS:
    :cvar PR:
    :cvar SQSURGINS:
    :cvar URETHINS:
    :cvar VAGINSI:
    """
    CERVINS = "CERVINS"
    IOSURGINS = "IOSURGINS"
    IU = "IU"
    LPINS = "LPINS"
    PR = "PR"
    SQSURGINS = "SQSURGINS"
    URETHINS = "URETHINS"
    VAGINSI = "VAGINSI"


class Instillation(Enum):
    """
    abstDomain: A14696 (C-0-T14581-A16931-A14696-cpt)
    :cvar RECINSTL:
    :cvar RECTINSTL:
    :cvar CECINSTL:
    :cvar CTINSTL:
    :cvar CAPDINSTL:
    :cvar ETINSTL:
    :cvar ENTINSTL:
    :cvar EFT:
    :cvar GJT:
    :cvar GT:
    :cvar IBRONCHINSTIL:
    :cvar IDUODINSTIL:
    :cvar IESOPHINSTIL:
    :cvar IGASTINSTIL:
    :cvar IILEALINJ:
    :cvar IOINSTL:
    :cvar ISININSTIL:
    :cvar ITRACHINSTIL:
    :cvar IUINSTL:
    :cvar JJTINSTL:
    :cvar LARYNGINSTIL:
    :cvar NASALINSTIL:
    :cvar NASOGASINSTIL:
    :cvar NGT:
    :cvar NTT:
    :cvar OGT:
    :cvar OJJ:
    :cvar OT:
    :cvar PNSINSTL:
    :cvar PDPINSTL:
    :cvar SININSTIL:
    :cvar SOFTISINSTIL:
    :cvar TRACHINSTL:
    :cvar TRTYMPINSTIL:
    :cvar BLADINSTL:
    :cvar URETHINSTL:
    """
    RECINSTL = "RECINSTL"
    RECTINSTL = "RECTINSTL"
    CECINSTL = "CECINSTL"
    CTINSTL = "CTINSTL"
    CAPDINSTL = "CAPDINSTL"
    ETINSTL = "ETINSTL"
    ENTINSTL = "ENTINSTL"
    EFT = "EFT"
    GJT = "GJT"
    GT = "GT"
    IBRONCHINSTIL = "IBRONCHINSTIL"
    IDUODINSTIL = "IDUODINSTIL"
    IESOPHINSTIL = "IESOPHINSTIL"
    IGASTINSTIL = "IGASTINSTIL"
    IILEALINJ = "IILEALINJ"
    IOINSTL = "IOINSTL"
    ISININSTIL = "ISININSTIL"
    ITRACHINSTIL = "ITRACHINSTIL"
    IUINSTL = "IUINSTL"
    JJTINSTL = "JJTINSTL"
    LARYNGINSTIL = "LARYNGINSTIL"
    NASALINSTIL = "NASALINSTIL"
    NASOGASINSTIL = "NASOGASINSTIL"
    NGT = "NGT"
    NTT = "NTT"
    OGT = "OGT"
    OJJ = "OJJ"
    OT = "OT"
    PNSINSTL = "PNSINSTL"
    PDPINSTL = "PDPINSTL"
    SININSTIL = "SININSTIL"
    SOFTISINSTIL = "SOFTISINSTIL"
    TRACHINSTL = "TRACHINSTL"
    TRTYMPINSTIL = "TRTYMPINSTIL"
    BLADINSTL = "BLADINSTL"
    URETHINSTL = "URETHINSTL"


class Institution(Enum):
    """
    specDomain: S10189 (C-0-T220-S10189-cpt)
    :cvar I:
    :cvar X:
    :cvar G:
    :cvar N:
    :cvar CS:
    """
    I = "I"
    X = "X"
    G = "G"
    N = "N"
    CS = "CS"


class IntegrityCheckAlgorithm(Enum):
    """
    vocSet: T17385 (C-0-T17385-cpt)
    :cvar SHA_1:
    :cvar SHA_256:
    """
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class InteractionDetectedIssueCode(Enum):
    """
    abstDomain: A16659 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-A16659-cpt)
    :cvar TPROD:
    :cvar DRG:
    :cvar NHP:
    :cvar NONRX:
    :cvar FOOD:
    """
    TPROD = "TPROD"
    DRG = "DRG"
    NHP = "NHP"
    NONRX = "NONRX"
    FOOD = "FOOD"


class InterameningealRoute(Enum):
    """
    abstDomain: A17074 (C-0-T14581-A17021-A17074-cpt)
    :cvar INTERMENINJ:
    """
    INTERMENINJ = "INTERMENINJ"


class InteriorSalish(Enum):
    """
    abstDomain: A18540 (C-0-T18130-A18523-A18540-cpt)
    :cvar X_CRD:
    :cvar X_COL:
    :cvar X_FLA:
    :cvar X_OKA:
    """
    X_CRD = "x-CRD"
    X_COL = "x-COL"
    X_FLA = "x-FLA"
    X_OKA = "x-OKA"


class InternalMedicineProviderCodes(Enum):
    """
    specDomain: S20126 (C-0-T19465-S20096-S20126-cpt)
    :cvar VALUE_207_R00000_X:
    :cvar VALUE_207_RA0401_X:
    :cvar VALUE_207_RA0000_X:
    :cvar VALUE_207_RA0201_X:
    :cvar VALUE_207_RC0000_X:
    :cvar VALUE_207_RI0001_X:
    :cvar VALUE_207_RC0001_X:
    :cvar VALUE_207_RC0200_X:
    :cvar VALUE_207_RE0101_X:
    :cvar VALUE_207_RG0100_X:
    :cvar VALUE_207_RG0300_X:
    :cvar VALUE_207_RH0000_X:
    :cvar VALUE_207_RH0003_X:
    :cvar VALUE_207_RI0008_X:
    :cvar VALUE_207_RI0200_X:
    :cvar VALUE_207_RI0011_X:
    :cvar VALUE_207_RM1200_X:
    :cvar VALUE_207_RX0202_X:
    :cvar VALUE_207_RN0300_X:
    :cvar VALUE_207_RP1001_X:
    :cvar VALUE_207_RR0500_X:
    :cvar VALUE_207_RS0010_X:
    """
    VALUE_207_R00000_X = "207R00000X"
    VALUE_207_RA0401_X = "207RA0401X"
    VALUE_207_RA0000_X = "207RA0000X"
    VALUE_207_RA0201_X = "207RA0201X"
    VALUE_207_RC0000_X = "207RC0000X"
    VALUE_207_RI0001_X = "207RI0001X"
    VALUE_207_RC0001_X = "207RC0001X"
    VALUE_207_RC0200_X = "207RC0200X"
    VALUE_207_RE0101_X = "207RE0101X"
    VALUE_207_RG0100_X = "207RG0100X"
    VALUE_207_RG0300_X = "207RG0300X"
    VALUE_207_RH0000_X = "207RH0000X"
    VALUE_207_RH0003_X = "207RH0003X"
    VALUE_207_RI0008_X = "207RI0008X"
    VALUE_207_RI0200_X = "207RI0200X"
    VALUE_207_RI0011_X = "207RI0011X"
    VALUE_207_RM1200_X = "207RM1200X"
    VALUE_207_RX0202_X = "207RX0202X"
    VALUE_207_RN0300_X = "207RN0300X"
    VALUE_207_RP1001_X = "207RP1001X"
    VALUE_207_RR0500_X = "207RR0500X"
    VALUE_207_RS0010_X = "207RS0010X"


class InterstitialRoute(Enum):
    """
    abstDomain: A17076 (C-0-T14581-A17021-A17076-cpt)
    :cvar INTERSTITINJ:
    """
    INTERSTITINJ = "INTERSTITINJ"


class IntraabdominalRoute(Enum):
    """
    abstDomain: A17078 (C-0-T14581-A17021-A17078-cpt)
    :cvar IABDINJ:
    """
    IABDINJ = "IABDINJ"


class IntraarterialInjection(Enum):
    """
    specDomain: S14639 (C-0-T14581-A17021-A17080-S14639-cpt)
    :cvar IAINJ:
    :cvar IAINJP:
    :cvar IAINJSP:
    """
    IAINJ = "IAINJ"
    IAINJP = "IAINJP"
    IAINJSP = "IAINJSP"


class IntraarterialRoute(Enum):
    """
    abstDomain: A17080 (C-0-T14581-A17021-A17080-cpt)
    :cvar IAINJ:
    :cvar IAINJP:
    :cvar IAINJSP:
    :cvar IA:
    """
    IAINJ = "IAINJ"
    IAINJP = "IAINJP"
    IAINJSP = "IAINJSP"
    IA = "IA"


class IntraarticularRoute(Enum):
    """
    abstDomain: A17085 (C-0-T14581-A17021-A17085-cpt)
    :cvar IARTINJ:
    """
    IARTINJ = "IARTINJ"


class IntrabronchialRoute(Enum):
    """
    abstDomain: A17087 (C-0-T14581-A17021-A17087-cpt)
    :cvar IBRONCHINSTIL:
    """
    IBRONCHINSTIL = "IBRONCHINSTIL"


class IntrabursalRoute(Enum):
    """
    abstDomain: A17089 (C-0-T14581-A17021-A17089-cpt)
    :cvar IBURSINJ:
    """
    IBURSINJ = "IBURSINJ"


class IntracardiacInjection(Enum):
    """
    specDomain: S14644 (C-0-T14581-A17021-A17091-S14644-cpt)
    :cvar ICARDINJ:
    :cvar ICARINJP:
    :cvar ICARDINJRP:
    :cvar ICARDINJSP:
    """
    ICARDINJ = "ICARDINJ"
    ICARINJP = "ICARINJP"
    ICARDINJRP = "ICARDINJRP"
    ICARDINJSP = "ICARDINJSP"


class IntracardiacRoute(Enum):
    """
    abstDomain: A17091 (C-0-T14581-A17021-A17091-cpt)
    :cvar ICARDINJ:
    :cvar ICARINJP:
    :cvar ICARDINJRP:
    :cvar ICARDINJSP:
    :cvar IC:
    """
    ICARDINJ = "ICARDINJ"
    ICARINJP = "ICARINJP"
    ICARDINJRP = "ICARDINJRP"
    ICARDINJSP = "ICARDINJSP"
    IC = "IC"


class IntracartilaginousRoute(Enum):
    """
    abstDomain: A17097 (C-0-T14581-A17021-A17097-cpt)
    :cvar ICARTINJ:
    """
    ICARTINJ = "ICARTINJ"


class IntracaudalRoute(Enum):
    """
    abstDomain: A17099 (C-0-T14581-A17021-A17099-cpt)
    :cvar ICAUDINJ:
    """
    ICAUDINJ = "ICAUDINJ"


class IntracavernosalRoute(Enum):
    """
    abstDomain: A17101 (C-0-T14581-A17021-A17101-cpt)
    :cvar ICAVINJ:
    """
    ICAVINJ = "ICAVINJ"


class IntracavitaryRoute(Enum):
    """
    abstDomain: A17103 (C-0-T14581-A17021-A17103-cpt)
    :cvar ICAVITINJ:
    """
    ICAVITINJ = "ICAVITINJ"


class IntracerebralRoute(Enum):
    """
    abstDomain: A17105 (C-0-T14581-A17021-A17105-cpt)
    :cvar ICEREBINJ:
    """
    ICEREBINJ = "ICEREBINJ"


class IntracervicalRoute(Enum):
    """
    abstDomain: A17107 (C-0-T14581-A17021-A17107-cpt)
    :cvar IUINJC:
    """
    IUINJC = "IUINJC"


class IntracisternalRoute(Enum):
    """
    abstDomain: A17109 (C-0-T14581-A17021-A17109-cpt)
    :cvar ICISTERNINJ:
    """
    ICISTERNINJ = "ICISTERNINJ"


class IntracornealRoute(Enum):
    """
    abstDomain: A17111 (C-0-T14581-A17021-A17111-cpt)
    :cvar ICORNTA:
    """
    ICORNTA = "ICORNTA"


class IntracoronalRoute(Enum):
    """
    abstDomain: A17113 (C-0-T14581-A17021-A17113-cpt)
    :cvar ICORONTA:
    """
    ICORONTA = "ICORONTA"


class IntracoronaryInjection(Enum):
    """
    specDomain: S14650 (C-0-T14581-A17021-A17115-S14650-cpt)
    :cvar ICORONINJ:
    :cvar ICORONINJP:
    """
    ICORONINJ = "ICORONINJ"
    ICORONINJP = "ICORONINJP"


class IntracoronaryRoute(Enum):
    """
    abstDomain: A17115 (C-0-T14581-A17021-A17115-cpt)
    :cvar ICORONINJ:
    :cvar ICORONINJP:
    :cvar ICOR:
    """
    ICORONINJ = "ICORONINJ"
    ICORONINJP = "ICORONINJP"
    ICOR = "ICOR"


class IntracorpusCavernosumRoute(Enum):
    """
    abstDomain: A17119 (C-0-T14581-A17021-A17119-cpt)
    :cvar ICORPCAVINJ:
    """
    ICORPCAVINJ = "ICORPCAVINJ"


class IntradermalRoute(Enum):
    """
    abstDomain: A17123 (C-0-T14581-A17021-A17123-cpt)
    :cvar IDIMPLNT:
    :cvar IDINJ:
    """
    IDIMPLNT = "IDIMPLNT"
    IDINJ = "IDINJ"


class IntradiscalRoute(Enum):
    """
    abstDomain: A17126 (C-0-T14581-A17021-A17126-cpt)
    :cvar IDISCINJ:
    """
    IDISCINJ = "IDISCINJ"


class IntraductalRoute(Enum):
    """
    abstDomain: A17128 (C-0-T14581-A17021-A17128-cpt)
    :cvar IDUCTINJ:
    """
    IDUCTINJ = "IDUCTINJ"


class IntraduodenalRoute(Enum):
    """
    abstDomain: A17130 (C-0-T14581-A17021-A17130-cpt)
    :cvar IDUODINSTIL:
    :cvar IDOUDMAB:
    """
    IDUODINSTIL = "IDUODINSTIL"
    IDOUDMAB = "IDOUDMAB"


class IntraduralRoute(Enum):
    """
    abstDomain: A17133 (C-0-T14581-A17021-A17133-cpt)
    :cvar IDURINJ:
    """
    IDURINJ = "IDURINJ"


class IntraepidermalRoute(Enum):
    """
    abstDomain: A17135 (C-0-T14581-A17021-A17135-cpt)
    :cvar IEPIDINJ:
    """
    IEPIDINJ = "IEPIDINJ"


class IntraepithelialRoute(Enum):
    """
    abstDomain: A17137 (C-0-T14581-A17021-A17137-cpt)
    :cvar IEPITHINJ:
    """
    IEPITHINJ = "IEPITHINJ"


class IntraesophagealRoute(Enum):
    """
    abstDomain: A17139 (C-0-T14581-A17021-A17139-cpt)
    :cvar IESOPHINSTIL:
    :cvar IESOPHTA:
    """
    IESOPHINSTIL = "IESOPHINSTIL"
    IESOPHTA = "IESOPHTA"


class IntragastricRoute(Enum):
    """
    abstDomain: A17142 (C-0-T14581-A17021-A17142-cpt)
    :cvar IGASTINSTIL:
    :cvar IGASTIRR:
    :cvar IGASTLAV:
    """
    IGASTINSTIL = "IGASTINSTIL"
    IGASTIRR = "IGASTIRR"
    IGASTLAV = "IGASTLAV"


class IntrailealRoute(Enum):
    """
    abstDomain: A17146 (C-0-T14581-A17021-A17146-cpt)
    :cvar IILEALINJ:
    :cvar IILEALTA:
    """
    IILEALINJ = "IILEALINJ"
    IILEALTA = "IILEALTA"


class IntralesionalRoute(Enum):
    """
    abstDomain: A17149 (C-0-T14581-A17021-A17149-cpt)
    :cvar ILESINJ:
    :cvar ILESIRR:
    :cvar ILTOP:
    """
    ILESINJ = "ILESINJ"
    ILESIRR = "ILESIRR"
    ILTOP = "ILTOP"


class IntraluminalRoute(Enum):
    """
    abstDomain: A17153 (C-0-T14581-A17021-A17153-cpt)
    :cvar ILUMINJ:
    :cvar ILUMTA:
    """
    ILUMINJ = "ILUMINJ"
    ILUMTA = "ILUMTA"


class IntralymphaticRoute(Enum):
    """
    abstDomain: A17156 (C-0-T14581-A17021-A17156-cpt)
    :cvar ILYMPJINJ:
    """
    ILYMPJINJ = "ILYMPJINJ"


class IntramedullaryRoute(Enum):
    """
    abstDomain: A17158 (C-0-T14581-A17021-A17158-cpt)
    :cvar IMEDULINJ:
    """
    IMEDULINJ = "IMEDULINJ"


class IntramuscularInjection(Enum):
    """
    specDomain: S14657 (C-0-T14581-A17021-A17160-S14657-cpt)
    :cvar IM:
    :cvar IMD:
    :cvar IMZ:
    """
    IM = "IM"
    IMD = "IMD"
    IMZ = "IMZ"


class IntraocularRoute(Enum):
    """
    abstDomain: A17164 (C-0-T14581-A17021-A17164-cpt)
    :cvar IOINJ:
    :cvar IOSURGINS:
    :cvar IOINSTL:
    :cvar IOIRR:
    :cvar IOTOP:
    """
    IOINJ = "IOINJ"
    IOSURGINS = "IOSURGINS"
    IOINSTL = "IOINSTL"
    IOIRR = "IOIRR"
    IOTOP = "IOTOP"


class IntraosseousRoute(Enum):
    """
    abstDomain: A17170 (C-0-T14581-A17021-A17170-cpt)
    :cvar IOSSC:
    :cvar IOSSINJ:
    """
    IOSSC = "IOSSC"
    IOSSINJ = "IOSSINJ"


class IntraovarianRoute(Enum):
    """
    abstDomain: A17173 (C-0-T14581-A17021-A17173-cpt)
    :cvar IOVARINJ:
    """
    IOVARINJ = "IOVARINJ"


class IntrapericardialRoute(Enum):
    """
    abstDomain: A17175 (C-0-T14581-A17021-A17175-cpt)
    :cvar IPCARDINJ:
    """
    IPCARDINJ = "IPCARDINJ"


class IntraperitonealRoute(Enum):
    """
    abstDomain: A17177 (C-0-T14581-A17021-A17177-cpt)
    :cvar IPERINJ:
    :cvar PDPINJ:
    :cvar CAPDINSTL:
    :cvar PDPINSTL:
    """
    IPERINJ = "IPERINJ"
    PDPINJ = "PDPINJ"
    CAPDINSTL = "CAPDINSTL"
    PDPINSTL = "PDPINSTL"


class IntrapleuralRoute(Enum):
    """
    abstDomain: A17182 (C-0-T14581-A17021-A17182-cpt)
    :cvar IPLRINJ:
    :cvar CTINSTL:
    """
    IPLRINJ = "IPLRINJ"
    CTINSTL = "CTINSTL"


class IntraprostaticRoute(Enum):
    """
    abstDomain: A17185 (C-0-T14581-A17021-A17185-cpt)
    :cvar IPROSTINJ:
    """
    IPROSTINJ = "IPROSTINJ"


class IntrapulmonaryRoute(Enum):
    """
    abstDomain: A17187 (C-0-T14581-A17021-A17187-cpt)
    :cvar EXTCORPINJ:
    :cvar IPINJ:
    """
    EXTCORPINJ = "EXTCORPINJ"
    IPINJ = "IPINJ"


class IntrasinalRoute(Enum):
    """
    abstDomain: A17190 (C-0-T14581-A17021-A17190-cpt)
    :cvar ISININSTIL:
    """
    ISININSTIL = "ISININSTIL"


class IntraspinalRoute(Enum):
    """
    abstDomain: A17192 (C-0-T14581-A17021-A17192-cpt)
    :cvar ISINJ:
    """
    ISINJ = "ISINJ"


class IntrasternalRoute(Enum):
    """
    abstDomain: A17194 (C-0-T14581-A17021-A17194-cpt)
    :cvar ISTERINJ:
    """
    ISTERINJ = "ISTERINJ"


class IntrasynovialRoute(Enum):
    """
    abstDomain: A17196 (C-0-T14581-A17021-A17196-cpt)
    :cvar ISYNINJ:
    """
    ISYNINJ = "ISYNINJ"


class IntratendinousRoute(Enum):
    """
    abstDomain: A17121 (C-0-T14581-A17021-A17121-cpt)
    :cvar ITENDINJ:
    """
    ITENDINJ = "ITENDINJ"


class IntratesticularRoute(Enum):
    """
    abstDomain: A17198 (C-0-T14581-A17021-A17198-cpt)
    :cvar ITESTINJ:
    """
    ITESTINJ = "ITESTINJ"


class IntrathecalRoute(Enum):
    """
    abstDomain: A17200 (C-0-T14581-A17021-A17200-cpt)
    :cvar IT:
    :cvar ITINJ:
    """
    IT = "IT"
    ITINJ = "ITINJ"


class IntrathoracicRoute(Enum):
    """
    abstDomain: A17203 (C-0-T14581-A17021-A17203-cpt)
    :cvar ITHORINJ:
    """
    ITHORINJ = "ITHORINJ"


class IntratrachealRoute(Enum):
    """
    abstDomain: A17205 (C-0-T14581-A17021-A17205-cpt)
    :cvar ITRACHINSTIL:
    :cvar ITRACHMAB:
    """
    ITRACHINSTIL = "ITRACHINSTIL"
    ITRACHMAB = "ITRACHMAB"


class IntratubularRoute(Enum):
    """
    abstDomain: A17208 (C-0-T14581-A17021-A17208-cpt)
    :cvar ITUBINJ:
    """
    ITUBINJ = "ITUBINJ"


class IntratumorRoute(Enum):
    """
    abstDomain: A17210 (C-0-T14581-A17021-A17210-cpt)
    :cvar ITUMINJ:
    """
    ITUMINJ = "ITUMINJ"


class IntratympanicRoute(Enum):
    """
    abstDomain: A17212 (C-0-T14581-A17021-A17212-cpt)
    :cvar ITYMPINJ:
    """
    ITYMPINJ = "ITYMPINJ"


class IntrauterineRoute(Enum):
    """
    abstDomain: A17214 (C-0-T14581-A17021-A17214-cpt)
    :cvar IURETINJ:
    :cvar IUINJ:
    :cvar IU:
    :cvar IUINSTL:
    """
    IURETINJ = "IURETINJ"
    IUINJ = "IUINJ"
    IU = "IU"
    IUINSTL = "IUINSTL"


class IntravascularRoute(Enum):
    """
    abstDomain: A17219 (C-0-T14581-A17021-A17219-cpt)
    :cvar HEMODIFF:
    :cvar IVASCINFUS:
    :cvar HEMOPORT:
    :cvar IVASCINJ:
    """
    HEMODIFF = "HEMODIFF"
    IVASCINFUS = "IVASCINFUS"
    HEMOPORT = "HEMOPORT"
    IVASCINJ = "IVASCINJ"


class IntravenousInfusion(Enum):
    """
    specDomain: S14609 (C-0-T14581-A16931-A14602-S14609-cpt)
    :cvar IV:
    :cvar IVC:
    :cvar IVCC:
    :cvar IVCI:
    :cvar PCA:
    """
    IV = "IV"
    IVC = "IVC"
    IVCC = "IVCC"
    IVCI = "IVCI"
    PCA = "PCA"


class IntravenousInjection(Enum):
    """
    specDomain: S14670 (C-0-T14581-A17021-A17224-S14670-cpt)
    :cvar IVINJ:
    :cvar IVINJBOL:
    :cvar IVPUSH:
    :cvar IVRPUSH:
    :cvar IVSPUSH:
    """
    IVINJ = "IVINJ"
    IVINJBOL = "IVINJBOL"
    IVPUSH = "IVPUSH"
    IVRPUSH = "IVRPUSH"
    IVSPUSH = "IVSPUSH"


class IntravenousRoute(Enum):
    """
    abstDomain: A17224 (C-0-T14581-A17021-A17224-cpt)
    :cvar IVINJ:
    :cvar IVINJBOL:
    :cvar IVPUSH:
    :cvar IVRPUSH:
    :cvar IVSPUSH:
    :cvar IVFLUSH:
    """
    IVINJ = "IVINJ"
    IVINJBOL = "IVINJBOL"
    IVPUSH = "IVPUSH"
    IVRPUSH = "IVRPUSH"
    IVSPUSH = "IVSPUSH"
    IVFLUSH = "IVFLUSH"


class IntraventricularRoute(Enum):
    """
    abstDomain: A17235 (C-0-T14581-A17021-A17235-cpt)
    :cvar IVENTINJ:
    """
    IVENTINJ = "IVENTINJ"


class IntravesicleRoute(Enum):
    """
    abstDomain: A17237 (C-0-T14581-A17021-A17237-cpt)
    :cvar IVESINJ:
    """
    IVESINJ = "IVESINJ"


class IntravitrealRoute(Enum):
    """
    abstDomain: A17239 (C-0-T14581-A17021-A17239-cpt)
    :cvar IVITINJ:
    """
    IVITINJ = "IVITINJ"


class InuitInupiaq(Enum):
    """
    abstDomain: A18210 (C-0-T18130-A18191-A18192-A18210-cpt)
    :cvar X_ESI:
    :cvar X_ESK:
    """
    X_ESI = "x-ESI"
    X_ESK = "x-ESK"


class InvoiceElementAdjudicated(Enum):
    """
    abstDomain: A17530 (C-0-T13953-A13954-A17522-A17530-cpt)
    :cvar ADNPPPELAT:
    :cvar ADNPPPELCT:
    :cvar ADNPPPMNAT:
    :cvar ADNPPPMNCT:
    :cvar ADNPSPELAT:
    :cvar ADNPSPELCT:
    :cvar ADNPSPMNAT:
    :cvar ADNPSPMNCT:
    :cvar ADNFPPELAT:
    :cvar ADNFPPELCT:
    :cvar ADNFPPMNAT:
    :cvar ADNFPPMNCT:
    :cvar ADNFSPELAT:
    :cvar ADNFSPELCT:
    :cvar ADNFSPMNAT:
    :cvar ADNFSPMNCT:
    :cvar ADPPPPELAT:
    :cvar ADPPPPELCT:
    :cvar ADPPPPMNAT:
    :cvar ADPPPPMNCT:
    :cvar ADPPSPELAT:
    :cvar ADPPSPELCT:
    :cvar ADPPSPMNAT:
    :cvar ADPPSPMNCT:
    :cvar ADRFPPELAT:
    :cvar ADRFPPELCT:
    :cvar ADRFPPMNAT:
    :cvar ADRFPPMNCT:
    :cvar ADRFSPELAT:
    :cvar ADRFSPELCT:
    :cvar ADRFSPMNAT:
    :cvar ADRFSPMNCT:
    """
    ADNPPPELAT = "ADNPPPELAT"
    ADNPPPELCT = "ADNPPPELCT"
    ADNPPPMNAT = "ADNPPPMNAT"
    ADNPPPMNCT = "ADNPPPMNCT"
    ADNPSPELAT = "ADNPSPELAT"
    ADNPSPELCT = "ADNPSPELCT"
    ADNPSPMNAT = "ADNPSPMNAT"
    ADNPSPMNCT = "ADNPSPMNCT"
    ADNFPPELAT = "ADNFPPELAT"
    ADNFPPELCT = "ADNFPPELCT"
    ADNFPPMNAT = "ADNFPPMNAT"
    ADNFPPMNCT = "ADNFPPMNCT"
    ADNFSPELAT = "ADNFSPELAT"
    ADNFSPELCT = "ADNFSPELCT"
    ADNFSPMNAT = "ADNFSPMNAT"
    ADNFSPMNCT = "ADNFSPMNCT"
    ADPPPPELAT = "ADPPPPELAT"
    ADPPPPELCT = "ADPPPPELCT"
    ADPPPPMNAT = "ADPPPPMNAT"
    ADPPPPMNCT = "ADPPPPMNCT"
    ADPPSPELAT = "ADPPSPELAT"
    ADPPSPELCT = "ADPPSPELCT"
    ADPPSPMNAT = "ADPPSPMNAT"
    ADPPSPMNCT = "ADPPSPMNCT"
    ADRFPPELAT = "ADRFPPELAT"
    ADRFPPELCT = "ADRFPPELCT"
    ADRFPPMNAT = "ADRFPPMNAT"
    ADRFPPMNCT = "ADRFPPMNCT"
    ADRFSPELAT = "ADRFSPELAT"
    ADRFSPELCT = "ADRFSPELCT"
    ADRFSPMNAT = "ADRFSPMNAT"
    ADRFSPMNCT = "ADRFSPMNCT"


class InvoiceElementPaid(Enum):
    """
    abstDomain: A17563 (C-0-T13953-A13954-A17522-A17563-cpt)
    :cvar PDNPPPELAT:
    :cvar PDNPPPELCT:
    :cvar PDNPPPMNAT:
    :cvar PDNPPPMNCT:
    :cvar PDNPSPELAT:
    :cvar PDNPSPELCT:
    :cvar PDNPSPMNAT:
    :cvar PDNPSPMNCT:
    :cvar PDNFPPELAT:
    :cvar PDNFPPELCT:
    :cvar PDNFPPMNAT:
    :cvar PDNFPPMNCT:
    :cvar PDNFSPELAT:
    :cvar PDNFSPELCT:
    :cvar PDNFSPMNAT:
    :cvar PDNFSPMNCT:
    :cvar PDPPPPELAT:
    :cvar PDPPPPELCT:
    :cvar PDPPPPMNAT:
    :cvar PDPPPPMNCT:
    :cvar PDPPSPELAT:
    :cvar PDPPSPELCT:
    :cvar PDPPSPMNAT:
    :cvar PDPPSPMNCT:
    """
    PDNPPPELAT = "PDNPPPELAT"
    PDNPPPELCT = "PDNPPPELCT"
    PDNPPPMNAT = "PDNPPPMNAT"
    PDNPPPMNCT = "PDNPPPMNCT"
    PDNPSPELAT = "PDNPSPELAT"
    PDNPSPELCT = "PDNPSPELCT"
    PDNPSPMNAT = "PDNPSPMNAT"
    PDNPSPMNCT = "PDNPSPMNCT"
    PDNFPPELAT = "PDNFPPELAT"
    PDNFPPELCT = "PDNFPPELCT"
    PDNFPPMNAT = "PDNFPPMNAT"
    PDNFPPMNCT = "PDNFPPMNCT"
    PDNFSPELAT = "PDNFSPELAT"
    PDNFSPELCT = "PDNFSPELCT"
    PDNFSPMNAT = "PDNFSPMNAT"
    PDNFSPMNCT = "PDNFSPMNCT"
    PDPPPPELAT = "PDPPPPELAT"
    PDPPPPELCT = "PDPPPPELCT"
    PDPPPPMNAT = "PDPPPPMNAT"
    PDPPPPMNCT = "PDPPPPMNCT"
    PDPPSPELAT = "PDPPSPELAT"
    PDPPSPELCT = "PDPPSPELCT"
    PDPPSPMNAT = "PDPPSPMNAT"
    PDPPSPMNCT = "PDPPSPMNCT"


class InvoiceElementSubmitted(Enum):
    """
    abstDomain: A17523 (C-0-T13953-A13954-A17522-A17523-cpt)
    :cvar SBBLELAT:
    :cvar SBBLELCT:
    :cvar SBNFELCT:
    :cvar SBNFELAT:
    :cvar SBPDELAT:
    :cvar SBPDELCT:
    """
    SBBLELAT = "SBBLELAT"
    SBBLELCT = "SBBLELCT"
    SBNFELCT = "SBNFELCT"
    SBNFELAT = "SBNFELAT"
    SBPDELAT = "SBPDELAT"
    SBPDELCT = "SBPDELCT"


class IontophoresisRoute(Enum):
    """
    abstDomain: A16990 (C-0-T14581-A16931-A16990-cpt)
    :cvar IONTO:
    """
    IONTO = "IONTO"


class Iroquoian(Enum):
    """
    abstDomain: A18306 (C-0-T18130-A18306-cpt)
    :cvar X_CAY:
    :cvar X_MOH:
    :cvar X_ONE:
    :cvar X_ONO:
    :cvar X_SEE:
    :cvar X_TUS:
    :cvar X_CER:
    """
    X_CAY = "x-CAY"
    X_MOH = "x-MOH"
    X_ONE = "x-ONE"
    X_ONO = "x-ONO"
    X_SEE = "x-SEE"
    X_TUS = "x-TUS"
    X_CER = "x-CER"


class Irrigation(Enum):
    """
    abstDomain: A14721 (C-0-T14581-A16931-A14721-cpt)
    :cvar BLADIRR:
    :cvar BLADIRRC:
    :cvar BLADIRRT:
    :cvar GUIRR:
    :cvar IGASTIRR:
    :cvar ILESIRR:
    :cvar IOIRR:
    :cvar RECIRR:
    """
    BLADIRR = "BLADIRR"
    BLADIRRC = "BLADIRRC"
    BLADIRRT = "BLADIRRT"
    GUIRR = "GUIRR"
    IGASTIRR = "IGASTIRR"
    ILESIRR = "ILESIRR"
    IOIRR = "IOIRR"
    RECIRR = "RECIRR"


class IrrigationSolution(Enum):
    """
    specDomain: S14427 (C-0-T19651-A14411-A14412-A14413-S14419-S14427-cpt)
    :cvar IRSOL:
    :cvar DOUCHE:
    :cvar ENEMA:
    :cvar OPIRSOL:
    """
    IRSOL = "IRSOL"
    DOUCHE = "DOUCHE"
    ENEMA = "ENEMA"
    OPIRSOL = "OPIRSOL"


class IssueFilterCode(Enum):
    """
    abstDomain: A19819 (C-0-T19726-A19819-cpt)
    :cvar ISSFA:
    :cvar ISSFI:
    :cvar ISSFU:
    """
    ISSFA = "ISSFA"
    ISSFI = "ISSFI"
    ISSFU = "ISSFU"


class JejunumRoute(Enum):
    """
    abstDomain: A17241 (C-0-T14581-A17021-A17241-cpt)
    :cvar GJT:
    :cvar JJTINSTL:
    :cvar OJJ:
    """
    GJT = "GJT"
    JJTINSTL = "JJTINSTL"
    OJJ = "OJJ"


class Kalapuyan(Enum):
    """
    abstDomain: A18425 (C-0-T18130-A18413-A18424-A18425-cpt)
    :cvar X_KAL:
    """
    X_KAL = "x-KAL"


class Keresan(Enum):
    """
    abstDomain: A18319 (C-0-T18130-A18319-cpt)
    :cvar X_KJQ:
    :cvar X_KEE:
    """
    X_KJQ = "x-KJQ"
    X_KEE = "x-KEE"


class KiowaTanoan(Enum):
    """
    abstDomain: A18327 (C-0-T18130-A18327-cpt)
    :cvar X_TAO:
    :cvar X_TIX:
    :cvar X_TOW:
    :cvar X_KIO:
    :cvar X_TEW:
    """
    X_TAO = "x-TAO"
    X_TIX = "x-TIX"
    X_TOW = "x-TOW"
    X_KIO = "x-KIO"
    X_TEW = "x-TEW"


class KitEntityType(Enum):
    """
    specDomain: S16145 (C-0-T16040-A16041-A19867-A16143-S16144-S16145-cpt)
    :cvar KIT:
    :cvar SYSTM:
    """
    KIT = "KIT"
    SYSTM = "SYSTM"


class KoyukonIngalik(Enum):
    """
    abstDomain: A18366 (C-0-T18130-A18352-A18356-A18358-A18365-A18366-cpt)
    :cvar X_ING:
    :cvar X_HOI:
    :cvar X_KOY:
    """
    X_ING = "x-ING"
    X_HOI = "x-HOI"
    X_KOY = "x-KOY"


class KutchinHan(Enum):
    """
    abstDomain: A18379 (C-0-T18130-A18352-A18356-A18358-A18365-A18379-cpt)
    :cvar X_HAA:
    :cvar X_KUC:
    """
    X_HAA = "x-HAA"
    X_KUC = "x-KUC"


class LoincobservationActContextAgeType(Enum):
    """
    abstDomain: A19758 (C-0-T13953-A19820-A16226-A19757-A19758-cpt)
    :cvar VALUE_30972_4:
    :cvar VALUE_29553_5:
    :cvar VALUE_30525_0:
    :cvar VALUE_21611_9:
    :cvar VALUE_21612_7:
    """
    VALUE_30972_4 = "30972-4"
    VALUE_29553_5 = "29553-5"
    VALUE_30525_0 = "30525-0"
    VALUE_21611_9 = "21611-9"
    VALUE_21612_7 = "21612-7"


class LaboratoriesProviderCodes(Enum):
    """
    specDomain: S20749 (C-0-T19465-S20749-cpt)
    :cvar VALUE_290000000_X:
    :cvar VALUE_291_U00000_X:
    :cvar VALUE_292200000_X:
    :cvar VALUE_293_D00000_X:
    """
    VALUE_290000000_X = "290000000X"
    VALUE_291_U00000_X = "291U00000X"
    VALUE_292200000_X = "292200000X"
    VALUE_293_D00000_X = "293D00000X"


class LaboratoryHipaa(Enum):
    """
    abstDomain: A13808 (C-0-T13129-A13715-A13808-cpt)
    :cvar VALUE_291_U00000_N:
    :cvar VALUE_292200000_N:
    :cvar VALUE_293_D00000_N:
    """
    VALUE_291_U00000_N = "291U00000N"
    VALUE_292200000_N = "292200000N"
    VALUE_293_D00000_N = "293D00000N"


class LacrimalPunctaRoute(Enum):
    """
    abstDomain: A17245 (C-0-T14581-A17021-A17245-cpt)
    :cvar LPINS:
    """
    LPINS = "LPINS"


class LanguageAbilityMode(Enum):
    """
    vocSet: T12249 (C-0-T12249-cpt)
    :cvar ESGN:
    :cvar ESP:
    :cvar EWR:
    :cvar RSGN:
    :cvar RSP:
    :cvar RWR:
    """
    ESGN = "ESGN"
    ESP = "ESP"
    EWR = "EWR"
    RSGN = "RSGN"
    RSP = "RSP"
    RWR = "RWR"


class LanguageAbilityProficiency(Enum):
    """
    vocSet: T12199 (C-0-T12199-cpt)
    :cvar E:
    :cvar F:
    :cvar G:
    :cvar P:
    """
    E = "E"
    F = "F"
    G = "G"
    P = "P"


class LaryngealRoute(Enum):
    """
    abstDomain: A17247 (C-0-T14581-A17021-A17247-cpt)
    :cvar LARYNGINSTIL:
    :cvar LARYNGTA:
    """
    LARYNGINSTIL = "LARYNGINSTIL"
    LARYNGTA = "LARYNGTA"


class LavageRoute(Enum):
    """
    abstDomain: A16995 (C-0-T14581-A16931-A16995-cpt)
    :cvar IGASTLAV:
    """
    IGASTLAV = "IGASTLAV"


class LengthOutOfRange(Enum):
    """
    specDomain: S21656 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S21656-cpt)
    :cvar LEN_RANGE:
    :cvar LEN_LONG:
    :cvar LEN_SHORT:
    """
    LEN_RANGE = "LEN_RANGE"
    LEN_LONG = "LEN_LONG"
    LEN_SHORT = "LEN_SHORT"


class LifeInsurancePolicy(Enum):
    """
    specDomain: S22148 (C-0-T13953-A13954-A19855-A19856-S22148-cpt)
    :cvar LIFE:
    :cvar ANNU:
    :cvar TLIFE:
    :cvar ULIFE:
    """
    LIFE = "LIFE"
    ANNU = "ANNU"
    TLIFE = "TLIFE"
    ULIFE = "ULIFE"


class LineAccessMedicalDevice(Enum):
    """
    specDomain: S16201 (C-0-T16040-A16041-A19867-A16188-A16200-S16201-cpt)
    :cvar LINE:
    :cvar IALINE:
    :cvar IVLINE:
    """
    LINE = "LINE"
    IALINE = "IALINE"
    IVLINE = "IVLINE"


class LingualRoute(Enum):
    """
    abstDomain: A17250 (C-0-T14581-A17021-A17250-cpt)
    :cvar TRNSLING:
    """
    TRNSLING = "TRNSLING"


class LiquidCleanser(Enum):
    """
    specDomain: S14414 (C-0-T19651-A14411-A14412-A14413-S14414-cpt)
    :cvar LIQCLN:
    :cvar LIQSOAP:
    :cvar SHMP:
    """
    LIQCLN = "LIQCLN"
    LIQSOAP = "LIQSOAP"
    SHMP = "SHMP"


class LivingArrangement(Enum):
    """
    vocSet: T220 (C-0-T220-cpt)
    :cvar HL:
    :cvar M:
    :cvar T:
    :cvar I:
    :cvar X:
    :cvar G:
    :cvar N:
    :cvar CS:
    :cvar PR:
    :cvar H:
    :cvar R:
    :cvar SL:
    """
    HL = "HL"
    M = "M"
    T = "T"
    I = "I"
    X = "X"
    G = "G"
    N = "N"
    CS = "CS"
    PR = "PR"
    H = "H"
    R = "R"
    SL = "SL"


class LivingSubjectProductionClass(Enum):
    """
    abstDomain: A16368 (C-0-T12206-A16368-cpt)
    :cvar BF:
    :cvar BR:
    :cvar BL:
    :cvar CO:
    :cvar DA:
    :cvar DR:
    :cvar DU:
    :cvar FI:
    :cvar LY:
    :cvar MT:
    :cvar MU:
    :cvar PL:
    :cvar RC:
    :cvar SH:
    :cvar VL:
    :cvar WL:
    :cvar WO:
    """
    BF = "BF"
    BR = "BR"
    BL = "BL"
    CO = "CO"
    DA = "DA"
    DR = "DR"
    DU = "DU"
    FI = "FI"
    LY = "LY"
    MT = "MT"
    MU = "MU"
    PL = "PL"
    RC = "RC"
    SH = "SH"
    VL = "VL"
    WL = "WL"
    WO = "WO"


class Loan(Enum):
    """
    specDomain: S17961 (C-0-T13953-A13954-A17958-S17961-cpt)
    :cvar LOAN:
    :cvar RENT:
    """
    LOAN = "LOAN"
    RENT = "RENT"


class LocalMarkupIgnore(Enum):
    """
    vocSet: T10975 (C-0-T10975-cpt)
    :cvar ALL:
    :cvar MARKUP:
    """
    ALL = "all"
    MARKUP = "markup"


class LocalRemoteControlState(Enum):
    """
    vocSet: T10893 (C-0-T10893-cpt)
    :cvar L:
    :cvar R:
    """
    L = "L"
    R = "R"


class LotionDrugForm(Enum):
    """
    specDomain: S14464 (C-0-T19651-A14411-A14412-A14463-S14464-cpt)
    :cvar LTN:
    :cvar TOPLTN:
    """
    LTN = "LTN"
    TOPLTN = "TOPLTN"


class MdfattributeType(Enum):
    """
    vocSet: T10045 (C-0-T10045-cpt)
    :cvar ADDR:
    :cvar CD:
    :cvar COM:
    :cvar DTTM:
    :cvar DESC:
    :cvar EXPR:
    :cvar FRC:
    :cvar TIME:
    :cvar ID:
    :cvar IND:
    :cvar NM:
    :cvar NBR:
    :cvar PHON:
    :cvar QTY:
    :cvar TXT:
    :cvar TMR:
    :cvar VALUE:
    """
    ADDR = "ADDR"
    CD = "CD"
    COM = "COM"
    DTTM = "DTTM"
    DESC = "DESC"
    EXPR = "EXPR"
    FRC = "FRC"
    TIME = "TIME"
    ID = "ID"
    IND = "IND"
    NM = "NM"
    NBR = "NBR"
    PHON = "PHON"
    QTY = "QTY"
    TXT = "TXT"
    TMR = "TMR"
    VALUE = "VALUE"


class MdfsubjectAreaPrefix(Enum):
    """
    vocSet: T10029 (C-0-T10029-cpt)
    :cvar COI:
    :cvar DIM:
    :cvar RIM:
    :cvar STW:
    """
    COI = "COI"
    DIM = "DIM"
    RIM = "RIM"
    STW = "STW"


class Maiduan(Enum):
    """
    abstDomain: A18435 (C-0-T18130-A18413-A18435-cpt)
    :cvar X_NSZ:
    :cvar X_NMU:
    :cvar X_MAI:
    """
    X_NSZ = "x-NSZ"
    X_NMU = "x-NMU"
    X_MAI = "x-MAI"


class ManagedCareOrganizationHipaa(Enum):
    """
    abstDomain: A13812 (C-0-T13129-A13715-A13812-cpt)
    :cvar VALUE_302_F00000_N:
    :cvar VALUE_302_R00000_N:
    :cvar VALUE_305_S00000_N:
    :cvar VALUE_305_R00000_N:
    """
    VALUE_302_F00000_N = "302F00000N"
    VALUE_302_R00000_N = "302R00000N"
    VALUE_305_S00000_N = "305S00000N"
    VALUE_305_R00000_N = "305R00000N"


class ManagedCareOrganizationsProviderCodes(Enum):
    """
    specDomain: S20753 (C-0-T19465-S20753-cpt)
    :cvar VALUE_300000000_X:
    :cvar VALUE_302_F00000_X:
    :cvar VALUE_302_R00000_X:
    :cvar VALUE_305_S00000_X:
    :cvar VALUE_305_R00000_X:
    """
    VALUE_300000000_X = "300000000X"
    VALUE_302_F00000_X = "302F00000X"
    VALUE_302_R00000_X = "302R00000X"
    VALUE_305_S00000_X = "305S00000X"
    VALUE_305_R00000_X = "305R00000X"


class ManagedCarePolicy(Enum):
    """
    specDomain: S22147 (C-0-T13953-A13954-A19855-A19856-A19857-S22147-cpt)
    :cvar MCPOL:
    :cvar HMO:
    :cvar POS:
    :cvar PPO:
    """
    MCPOL = "MCPOL"
    HMO = "HMO"
    POS = "POS"
    PPO = "PPO"


class ManagedParticipationStatus(Enum):
    """
    vocSet: T15992 (C-0-T15992-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar COMPLETED:
    :cvar PENDING:
    :cvar NULLIFIED:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    PENDING = "pending"
    NULLIFIED = "nullified"


class ManagedParticipationStatusNormal(Enum):
    """
    specDomain: S15993 (C-0-T15992-S15993-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar COMPLETED:
    :cvar PENDING:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    PENDING = "pending"


class MapRelationship(Enum):
    """
    vocSet: T11052 (C-0-T11052-cpt)
    :cvar BT:
    :cvar E:
    :cvar NT:
    """
    BT = "BT"
    E = "E"
    NT = "NT"


class MaterialDangerInfectious(Enum):
    """
    specDomain: S10407 (C-0-T10405-S10407-cpt)
    :cvar INF:
    :cvar BHZ:
    """
    INF = "INF"
    BHZ = "BHZ"


class MaterialDangerInflammable(Enum):
    """
    specDomain: S10412 (C-0-T10405-S10412-cpt)
    :cvar IFL:
    :cvar EXP:
    """
    IFL = "IFL"
    EXP = "EXP"


class MaterialEntityAdditive(Enum):
    """
    abstDomain: A16042 (C-0-T16040-A16041-A19867-A16042-cpt)
    :cvar F10:
    :cvar C32:
    :cvar C38:
    :cvar HCL6:
    :cvar ACDA:
    :cvar ACDB:
    :cvar ACET:
    :cvar AMIES:
    :cvar HEPA:
    :cvar BACTM:
    :cvar BOR:
    :cvar BOUIN:
    :cvar BF10:
    :cvar WEST:
    :cvar BSKM:
    :cvar CTAD:
    :cvar CARS:
    :cvar CARY:
    :cvar CHLTM:
    :cvar ENT:
    :cvar JKM:
    :cvar KARN:
    :cvar LIA:
    :cvar HEPL:
    :cvar M4:
    :cvar M4_RT:
    :cvar M5:
    :cvar MMDTM:
    :cvar MICHTM:
    :cvar HNO3:
    :cvar NONE_VALUE:
    :cvar PAGE:
    :cvar PHENOL:
    :cvar PVA:
    :cvar KOX:
    :cvar EDTK15:
    :cvar EDTK75:
    :cvar RLM:
    :cvar SST:
    :cvar SILICA:
    :cvar NAF:
    :cvar FL100:
    :cvar FL10:
    :cvar SPS:
    :cvar HEPN:
    :cvar EDTN:
    :cvar STUTM:
    :cvar THROM:
    :cvar FDP:
    :cvar THYMOL:
    :cvar THYO:
    :cvar TOLU:
    :cvar URETM:
    :cvar VIRTM:
    """
    F10 = "F10"
    C32 = "C32"
    C38 = "C38"
    HCL6 = "HCL6"
    ACDA = "ACDA"
    ACDB = "ACDB"
    ACET = "ACET"
    AMIES = "AMIES"
    HEPA = "HEPA"
    BACTM = "BACTM"
    BOR = "BOR"
    BOUIN = "BOUIN"
    BF10 = "BF10"
    WEST = "WEST"
    BSKM = "BSKM"
    CTAD = "CTAD"
    CARS = "CARS"
    CARY = "CARY"
    CHLTM = "CHLTM"
    ENT = "ENT"
    JKM = "JKM"
    KARN = "KARN"
    LIA = "LIA"
    HEPL = "HEPL"
    M4 = "M4"
    M4_RT = "M4RT"
    M5 = "M5"
    MMDTM = "MMDTM"
    MICHTM = "MICHTM"
    HNO3 = "HNO3"
    NONE_VALUE = "NONE"
    PAGE = "PAGE"
    PHENOL = "PHENOL"
    PVA = "PVA"
    KOX = "KOX"
    EDTK15 = "EDTK15"
    EDTK75 = "EDTK75"
    RLM = "RLM"
    SST = "SST"
    SILICA = "SILICA"
    NAF = "NAF"
    FL100 = "FL100"
    FL10 = "FL10"
    SPS = "SPS"
    HEPN = "HEPN"
    EDTN = "EDTN"
    STUTM = "STUTM"
    THROM = "THROM"
    FDP = "FDP"
    THYMOL = "THYMOL"
    THYO = "THYO"
    TOLU = "TOLU"
    URETM = "URETM"
    VIRTM = "VIRTM"


class MdfHmdMetSourceType(Enum):
    """
    vocSet: T10076 (C-0-T10076-cpt)
    :cvar C:
    :cvar D:
    :cvar N:
    :cvar U:
    :cvar R:
    :cvar I:
    """
    C = "C"
    D = "D"
    N = "N"
    U = "U"
    R = "R"
    I = "I"


class MdfHmdRowType(Enum):
    """
    vocSet: T10069 (C-0-T10069-cpt)
    :cvar ASSOC:
    :cvar ATTR:
    :cvar ITEM:
    :cvar HMD:
    :cvar CLASS_VALUE:
    :cvar STC:
    """
    ASSOC = "assoc"
    ATTR = "attr"
    ITEM = "item"
    HMD = "hmd"
    CLASS_VALUE = "class"
    STC = "stc"


class MdfRmimRowType(Enum):
    """
    vocSet: T10063 (C-0-T10063-cpt)
    :cvar ASSOC:
    :cvar ATTR:
    :cvar CLASS_VALUE:
    :cvar RMIM:
    :cvar STC:
    """
    ASSOC = "assoc"
    ATTR = "attr"
    CLASS_VALUE = "class"
    RMIM = "rmim"
    STC = "stc"


class MedOncClinPracticeSetting(Enum):
    """
    specDomain: S10947 (C-0-T12206-A17660-A19450-A10588-S10589-S10947-cpt)
    :cvar ONCL:
    :cvar PEDHO:
    """
    ONCL = "ONCL"
    PEDHO = "PEDHO"


class MediaType(Enum):
    """
    vocSet: T14824 (C-0-T14824-cpt)
    :cvar APPLICATION_DICOM:
    :cvar APPLICATION_MSWORD:
    :cvar APPLICATION_PDF:
    :cvar AUDIO_BASIC:
    :cvar AUDIO_K32ADPCM:
    :cvar AUDIO_MPEG:
    :cvar IMAGE_G3FAX:
    :cvar IMAGE_GIF:
    :cvar IMAGE_JPEG:
    :cvar IMAGE_PNG:
    :cvar IMAGE_TIFF:
    :cvar MODEL_VRML:
    :cvar MULTIPART_X_HL7_CDA_LEVEL_ONE:
    :cvar TEXT_X_HL7_FT:
    :cvar TEXT_HTML:
    :cvar TEXT_PLAIN:
    :cvar TEXT_RTF:
    :cvar TEXT_SGML:
    :cvar TEXT_XML:
    :cvar VIDEO_MPEG:
    :cvar VIDEO_X_AVI:
    """
    APPLICATION_DICOM = "application/dicom"
    APPLICATION_MSWORD = "application/msword"
    APPLICATION_PDF = "application/pdf"
    AUDIO_BASIC = "audio/basic"
    AUDIO_K32ADPCM = "audio/k32adpcm"
    AUDIO_MPEG = "audio/mpeg"
    IMAGE_G3FAX = "image/g3fax"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_TIFF = "image/tiff"
    MODEL_VRML = "model/vrml"
    MULTIPART_X_HL7_CDA_LEVEL_ONE = "multipart/x-hl7-cda-level-one"
    TEXT_X_HL7_FT = "text/x-hl7-ft"
    TEXT_HTML = "text/html"
    TEXT_PLAIN = "text/plain"
    TEXT_RTF = "text/rtf"
    TEXT_SGML = "text/sgml"
    TEXT_XML = "text/xml"
    VIDEO_MPEG = "video/mpeg"
    VIDEO_X_AVI = "video/x-avi"


class MedicalGeneticsProviderCodes(Enum):
    """
    specDomain: S20149 (C-0-T19465-S20096-S20149-cpt)
    :cvar VALUE_207_S00000_X:
    :cvar VALUE_207_SG0202_X:
    :cvar VALUE_207_SC0300_X:
    :cvar VALUE_207_SG0201_X:
    :cvar VALUE_207_SG0203_X:
    :cvar VALUE_207_SM0001_X:
    :cvar VALUE_207_SG0205_X:
    """
    VALUE_207_S00000_X = "207S00000X"
    VALUE_207_SG0202_X = "207SG0202X"
    VALUE_207_SC0300_X = "207SC0300X"
    VALUE_207_SG0201_X = "207SG0201X"
    VALUE_207_SG0203_X = "207SG0203X"
    VALUE_207_SM0001_X = "207SM0001X"
    VALUE_207_SG0205_X = "207SG0205X"


class MedicationCap(Enum):
    """
    abstDomain: A16184 (C-0-T14049-A16184-cpt)
    :cvar CHILD:
    :cvar EASY:
    """
    CHILD = "CHILD"
    EASY = "EASY"


class MedicationGeneralizationRoleType(Enum):
    """
    abstDomain: A19720 (C-0-T12206-A19720-cpt)
    :cvar GD:
    :cvar GDF:
    :cvar GDS:
    :cvar GDSF:
    :cvar MGDSF:
    """
    GD = "GD"
    GDF = "GDF"
    GDS = "GDS"
    GDSF = "GDSF"
    MGDSF = "MGDSF"


class MedicationObservationType(Enum):
    """
    abstDomain: A19751 (C-0-T13953-A19820-A16226-A19751-cpt)
    :cvar SPLCOATING:
    :cvar SPLCOLOR:
    :cvar SPLIMAGE:
    :cvar SPLIMPRINT:
    :cvar REP_HALF_LIFE:
    :cvar SPLSCORING:
    :cvar SPLSHAPE:
    :cvar SPLSIZE:
    :cvar SPLSYMBOL:
    """
    SPLCOATING = "SPLCOATING"
    SPLCOLOR = "SPLCOLOR"
    SPLIMAGE = "SPLIMAGE"
    SPLIMPRINT = "SPLIMPRINT"
    REP_HALF_LIFE = "REP_HALF_LIFE"
    SPLSCORING = "SPLSCORING"
    SPLSHAPE = "SPLSHAPE"
    SPLSIZE = "SPLSIZE"
    SPLSYMBOL = "SPLSYMBOL"


class MedicationOrderReleaseReasonCode(Enum):
    """
    abstDomain: A19782 (C-0-T14878-A19692-A19782-cpt)
    :cvar HOLDINAP:
    :cvar HOLDDONE:
    """
    HOLDINAP = "HOLDINAP"
    HOLDDONE = "HOLDDONE"


class MemberRoleType(Enum):
    """
    abstDomain: A15925 (C-0-T12206-A15925-cpt)
    :cvar TRB:
    """
    TRB = "TRB"


class MessageCondition(Enum):
    """
    vocSet: T357 (C-0-T357-cpt)
    :cvar VALUE_207:
    :cvar VALUE_206:
    :cvar VALUE_102:
    :cvar VALUE_205:
    :cvar VALUE_0:
    :cvar VALUE_101:
    :cvar VALUE_100:
    :cvar VALUE_103:
    :cvar VALUE_204:
    :cvar VALUE_202:
    :cvar VALUE_203:
    :cvar VALUE_201:
    :cvar VALUE_200:
    """
    VALUE_207 = "207"
    VALUE_206 = "206"
    VALUE_102 = "102"
    VALUE_205 = "205"
    VALUE_0 = "0"
    VALUE_101 = "101"
    VALUE_100 = "100"
    VALUE_103 = "103"
    VALUE_204 = "204"
    VALUE_202 = "202"
    VALUE_203 = "203"
    VALUE_201 = "201"
    VALUE_200 = "200"


class MessageWaitingPriority(Enum):
    """
    vocSet: T19581 (C-0-T19581-cpt)
    :cvar H:
    :cvar L:
    :cvar M:
    """
    H = "H"
    L = "L"
    M = "M"


class MilitaryHospital(Enum):
    """
    specDomain: S13799 (C-0-T12206-A17660-A19450-A10588-S10602-S13799-cpt)
    :cvar MHSP:
    """
    MHSP = "MHSP"


class MilitaryHospitalProviderCodes(Enum):
    """
    specDomain: S20741 (C-0-T19465-S20733-S20741-cpt)
    :cvar VALUE_286500000_X:
    :cvar VALUE_2865_C1500_X:
    :cvar VALUE_2865_M2000_X:
    :cvar VALUE_2865_X1600_X:
    """
    VALUE_286500000_X = "286500000X"
    VALUE_2865_C1500_X = "2865C1500X"
    VALUE_2865_M2000_X = "2865M2000X"
    VALUE_2865_X1600_X = "2865X1600X"


class MilitaryRoleType(Enum):
    """
    specDomain: S21968 (C-0-T12206-A19809-A19805-A19814-S21968-cpt)
    :cvar MIL:
    :cvar ACTMIL:
    :cvar RETMIL:
    :cvar VET:
    """
    MIL = "MIL"
    ACTMIL = "ACTMIL"
    RETMIL = "RETMIL"
    VET = "VET"


class MissouriRiver(Enum):
    """
    abstDomain: A18554 (C-0-T18130-A18552-A18553-A18554-cpt)
    :cvar X_CRO:
    :cvar X_HID:
    """
    X_CRO = "x-CRO"
    X_HID = "x-HID"


class MobileUnit(Enum):
    """
    specDomain: S18100 (C-0-T12206-A17660-A19450-A19452-S18100-cpt)
    :cvar MOBL:
    :cvar AMB:
    """
    MOBL = "MOBL"
    AMB = "AMB"


class MobilityImpaired(Enum):
    """
    specDomain: S10186 (C-0-T295-S10186-cpt)
    :cvar VALUE_5:
    :cvar CB:
    :cvar CR:
    :cvar G:
    :cvar WK:
    :cvar WC:
    """
    VALUE_5 = "5"
    CB = "CB"
    CR = "CR"
    G = "G"
    WK = "WK"
    WC = "WC"


class ModelMediaType(Enum):
    """
    abstDomain: A14848 (C-0-T14824-A14848-cpt)
    :cvar MODEL_VRML:
    """
    MODEL_VRML = "model/vrml"


class ModifyIndicator(Enum):
    """
    vocSet: T395 (C-0-T395-cpt)
    :cvar M:
    :cvar N:
    """
    M = "M"
    N = "N"


class MucosalAbsorptionRoute(Enum):
    """
    abstDomain: A16997 (C-0-T14581-A16931-A16997-cpt)
    :cvar IDOUDMAB:
    :cvar ITRACHMAB:
    :cvar SMUCMAB:
    """
    IDOUDMAB = "IDOUDMAB"
    ITRACHMAB = "ITRACHMAB"
    SMUCMAB = "SMUCMAB"


class MucousMembraneRoute(Enum):
    """
    abstDomain: A17252 (C-0-T14581-A17021-A17252-cpt)
    :cvar MUC:
    """
    MUC = "MUC"


class MultiUseContainerEntityType(Enum):
    """
    abstDomain: A16153 (C-0-T16040-A16041-A19867-A16143-S16144-A16152-A16153-cpt)
    :cvar BOTP:
    :cvar BOTPLY:
    :cvar BOT:
    :cvar BOTA:
    :cvar BOTD:
    :cvar BOTG:
    :cvar BOX:
    :cvar CAN:
    :cvar CNSTR:
    :cvar CART:
    :cvar JAR:
    :cvar JUG:
    :cvar TIN:
    :cvar TUB:
    :cvar TUBE:
    :cvar VIAL:
    """
    BOTP = "BOTP"
    BOTPLY = "BOTPLY"
    BOT = "BOT"
    BOTA = "BOTA"
    BOTD = "BOTD"
    BOTG = "BOTG"
    BOX = "BOX"
    CAN = "CAN"
    CNSTR = "CNSTR"
    CART = "CART"
    JAR = "JAR"
    JUG = "JUG"
    TIN = "TIN"
    TUB = "TUB"
    TUBE = "TUBE"
    VIAL = "VIAL"


class MultipartMediaType(Enum):
    """
    abstDomain: A14850 (C-0-T14824-A14850-cpt)
    :cvar MULTIPART_X_HL7_CDA_LEVEL_ONE:
    """
    MULTIPART_X_HL7_CDA_LEVEL_ONE = "multipart/x-hl7-cda-level-one"


class Muskogean(Enum):
    """
    abstDomain: A18338 (C-0-T18130-A18338-cpt)
    :cvar X_AKZ:
    :cvar X_CKU:
    :cvar X_MIK:
    :cvar X_CIC:
    :cvar X_CCT:
    :cvar X_CRK:
    """
    X_AKZ = "x-AKZ"
    X_CKU = "x-CKU"
    X_MIK = "x-MIK"
    X_CIC = "x-CIC"
    X_CCT = "x-CCT"
    X_CRK = "x-CRK"


class NailRoute(Enum):
    """
    abstDomain: A17254 (C-0-T14581-A17021-A17254-cpt)
    :cvar NAIL:
    """
    NAIL = "NAIL"


class NameLegalUse(Enum):
    """
    specDomain: S10176 (C-0-T15913-S10176-cpt)
    :cvar L:
    :cvar OR_VALUE:
    """
    L = "L"
    OR_VALUE = "OR"


class NameRepresentationUse(Enum):
    """
    abstDomain: A17860 (C-0-T10637-A17860-cpt)
    :cvar ABC:
    :cvar IDE:
    :cvar SYL:
    """
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"


class NasalInhalation(Enum):
    """
    specDomain: S14617 (C-0-T14581-A17021-A17256-S14617-cpt)
    :cvar NASINHL:
    :cvar NASINHLC:
    :cvar NP:
    """
    NASINHL = "NASINHL"
    NASINHLC = "NASINHLC"
    NP = "NP"


class NasalRoute(Enum):
    """
    abstDomain: A17256 (C-0-T14581-A17021-A17256-cpt)
    :cvar NASINHL:
    :cvar NASINHLC:
    :cvar NP:
    :cvar NASALINSTIL:
    :cvar NASOGASINSTIL:
    :cvar NASAL:
    """
    NASINHL = "NASINHL"
    NASINHLC = "NASINHLC"
    NP = "NP"
    NASALINSTIL = "NASALINSTIL"
    NASOGASINSTIL = "NASOGASINSTIL"
    NASAL = "NASAL"


class NativeEntityAlaska(Enum):
    """
    abstDomain: A11969 (C-0-T11631-A11969-cpt)
    :cvar VALUE_339:
    :cvar VALUE_341:
    :cvar VALUE_342:
    :cvar VALUE_345:
    :cvar VALUE_347:
    :cvar VALUE_348:
    :cvar VALUE_352:
    :cvar VALUE_354:
    :cvar VALUE_355:
    :cvar VALUE_356:
    :cvar VALUE_359:
    :cvar VALUE_361:
    :cvar VALUE_364:
    :cvar VALUE_549:
    :cvar VALUE_369:
    :cvar VALUE_371:
    :cvar VALUE_372:
    :cvar VALUE_375:
    :cvar VALUE_376:
    :cvar VALUE_377:
    :cvar VALUE_378:
    :cvar VALUE_382:
    :cvar VALUE_383:
    :cvar VALUE_386:
    :cvar VALUE_388:
    :cvar VALUE_392:
    :cvar VALUE_395:
    :cvar VALUE_396:
    :cvar VALUE_398:
    :cvar VALUE_400:
    :cvar VALUE_401:
    :cvar VALUE_406:
    :cvar VALUE_411:
    :cvar VALUE_413:
    :cvar VALUE_414:
    :cvar VALUE_415:
    :cvar VALUE_417:
    :cvar VALUE_418:
    :cvar VALUE_419:
    :cvar VALUE_420:
    :cvar VALUE_422:
    :cvar VALUE_423:
    :cvar VALUE_424:
    :cvar VALUE_425:
    :cvar VALUE_427:
    :cvar VALUE_434:
    :cvar VALUE_435:
    :cvar VALUE_437:
    :cvar VALUE_438:
    :cvar VALUE_441:
    :cvar VALUE_443:
    :cvar VALUE_445:
    :cvar VALUE_450:
    :cvar VALUE_456:
    :cvar VALUE_455:
    :cvar VALUE_457:
    :cvar VALUE_459:
    :cvar VALUE_460:
    :cvar VALUE_463:
    :cvar VALUE_465:
    :cvar VALUE_466:
    :cvar VALUE_468:
    :cvar VALUE_340:
    :cvar VALUE_343:
    :cvar VALUE_346:
    :cvar VALUE_349:
    :cvar VALUE_357:
    :cvar VALUE_360:
    :cvar VALUE_362:
    :cvar VALUE_365:
    :cvar VALUE_366:
    :cvar VALUE_367:
    :cvar VALUE_368:
    :cvar VALUE_373:
    :cvar VALUE_374:
    :cvar VALUE_379:
    :cvar VALUE_380:
    :cvar VALUE_381:
    :cvar VALUE_385:
    :cvar VALUE_389:
    :cvar VALUE_390:
    :cvar VALUE_393:
    :cvar VALUE_394:
    :cvar VALUE_397:
    :cvar VALUE_399:
    :cvar VALUE_402:
    :cvar VALUE_403:
    :cvar VALUE_404:
    :cvar VALUE_405:
    :cvar VALUE_407:
    :cvar VALUE_408:
    :cvar VALUE_409:
    :cvar VALUE_412:
    :cvar VALUE_416:
    :cvar VALUE_430:
    :cvar VALUE_431:
    :cvar VALUE_433:
    :cvar VALUE_436:
    :cvar VALUE_439:
    :cvar VALUE_440:
    :cvar VALUE_442:
    :cvar VALUE_444:
    :cvar VALUE_446:
    :cvar VALUE_448:
    :cvar VALUE_449:
    :cvar VALUE_452:
    :cvar VALUE_453:
    :cvar VALUE_454:
    :cvar VALUE_461:
    :cvar VALUE_462:
    :cvar VALUE_464:
    :cvar VALUE_467:
    :cvar VALUE_469:
    :cvar VALUE_470:
    :cvar VALUE_471:
    :cvar VALUE_472:
    :cvar VALUE_473:
    :cvar VALUE_479:
    :cvar VALUE_481:
    :cvar VALUE_483:
    :cvar VALUE_488:
    :cvar VALUE_491:
    :cvar VALUE_496:
    :cvar VALUE_497:
    :cvar VALUE_500:
    :cvar VALUE_502:
    :cvar VALUE_504:
    :cvar VALUE_506:
    :cvar VALUE_507:
    :cvar VALUE_508:
    :cvar VALUE_509:
    :cvar VALUE_510:
    :cvar VALUE_517:
    :cvar VALUE_519:
    :cvar VALUE_522:
    :cvar VALUE_524:
    :cvar VALUE_525:
    :cvar VALUE_528:
    :cvar VALUE_529:
    :cvar VALUE_530:
    :cvar VALUE_532:
    :cvar VALUE_539:
    :cvar VALUE_542:
    :cvar VALUE_543:
    :cvar VALUE_544:
    :cvar VALUE_545:
    :cvar VALUE_547:
    :cvar VALUE_548:
    :cvar VALUE_552:
    :cvar VALUE_553:
    :cvar VALUE_555:
    :cvar VALUE_558:
    :cvar VALUE_559:
    :cvar VALUE_561:
    :cvar VALUE_563:
    :cvar VALUE_564:
    :cvar VALUE_474:
    :cvar VALUE_475:
    :cvar VALUE_476:
    :cvar VALUE_477:
    :cvar VALUE_478:
    :cvar VALUE_480:
    :cvar VALUE_482:
    :cvar VALUE_484:
    :cvar VALUE_485:
    :cvar VALUE_486:
    :cvar VALUE_487:
    :cvar VALUE_489:
    :cvar VALUE_490:
    :cvar VALUE_410:
    :cvar VALUE_426:
    :cvar VALUE_432:
    :cvar VALUE_451:
    :cvar VALUE_523:
    :cvar VALUE_494:
    :cvar VALUE_495:
    :cvar VALUE_498:
    :cvar VALUE_499:
    :cvar VALUE_501:
    :cvar VALUE_503:
    :cvar VALUE_505:
    :cvar VALUE_511:
    :cvar VALUE_512:
    :cvar VALUE_513:
    :cvar VALUE_514:
    :cvar VALUE_515:
    :cvar VALUE_518:
    :cvar VALUE_520:
    :cvar VALUE_526:
    :cvar VALUE_527:
    :cvar VALUE_531:
    :cvar VALUE_533:
    :cvar VALUE_534:
    :cvar VALUE_537:
    :cvar VALUE_538:
    :cvar VALUE_541:
    :cvar VALUE_546:
    :cvar VALUE_550:
    :cvar VALUE_551:
    :cvar VALUE_554:
    :cvar VALUE_556:
    :cvar VALUE_557:
    :cvar VALUE_338:
    :cvar VALUE_344:
    :cvar VALUE_350:
    :cvar VALUE_353:
    :cvar VALUE_358:
    :cvar VALUE_363:
    :cvar VALUE_370:
    :cvar VALUE_384:
    :cvar VALUE_387:
    :cvar VALUE_391:
    :cvar VALUE_421:
    :cvar VALUE_428:
    :cvar VALUE_429:
    :cvar VALUE_447:
    :cvar VALUE_458:
    :cvar VALUE_492:
    :cvar VALUE_493:
    :cvar VALUE_516:
    :cvar VALUE_521:
    :cvar VALUE_535:
    :cvar VALUE_536:
    :cvar VALUE_540:
    :cvar VALUE_560:
    :cvar VALUE_562:
    :cvar VALUE_565:
    :cvar VALUE_566:
    :cvar VALUE_351:
    """
    VALUE_339 = "339"
    VALUE_341 = "341"
    VALUE_342 = "342"
    VALUE_345 = "345"
    VALUE_347 = "347"
    VALUE_348 = "348"
    VALUE_352 = "352"
    VALUE_354 = "354"
    VALUE_355 = "355"
    VALUE_356 = "356"
    VALUE_359 = "359"
    VALUE_361 = "361"
    VALUE_364 = "364"
    VALUE_549 = "549"
    VALUE_369 = "369"
    VALUE_371 = "371"
    VALUE_372 = "372"
    VALUE_375 = "375"
    VALUE_376 = "376"
    VALUE_377 = "377"
    VALUE_378 = "378"
    VALUE_382 = "382"
    VALUE_383 = "383"
    VALUE_386 = "386"
    VALUE_388 = "388"
    VALUE_392 = "392"
    VALUE_395 = "395"
    VALUE_396 = "396"
    VALUE_398 = "398"
    VALUE_400 = "400"
    VALUE_401 = "401"
    VALUE_406 = "406"
    VALUE_411 = "411"
    VALUE_413 = "413"
    VALUE_414 = "414"
    VALUE_415 = "415"
    VALUE_417 = "417"
    VALUE_418 = "418"
    VALUE_419 = "419"
    VALUE_420 = "420"
    VALUE_422 = "422"
    VALUE_423 = "423"
    VALUE_424 = "424"
    VALUE_425 = "425"
    VALUE_427 = "427"
    VALUE_434 = "434"
    VALUE_435 = "435"
    VALUE_437 = "437"
    VALUE_438 = "438"
    VALUE_441 = "441"
    VALUE_443 = "443"
    VALUE_445 = "445"
    VALUE_450 = "450"
    VALUE_456 = "456"
    VALUE_455 = "455"
    VALUE_457 = "457"
    VALUE_459 = "459"
    VALUE_460 = "460"
    VALUE_463 = "463"
    VALUE_465 = "465"
    VALUE_466 = "466"
    VALUE_468 = "468"
    VALUE_340 = "340"
    VALUE_343 = "343"
    VALUE_346 = "346"
    VALUE_349 = "349"
    VALUE_357 = "357"
    VALUE_360 = "360"
    VALUE_362 = "362"
    VALUE_365 = "365"
    VALUE_366 = "366"
    VALUE_367 = "367"
    VALUE_368 = "368"
    VALUE_373 = "373"
    VALUE_374 = "374"
    VALUE_379 = "379"
    VALUE_380 = "380"
    VALUE_381 = "381"
    VALUE_385 = "385"
    VALUE_389 = "389"
    VALUE_390 = "390"
    VALUE_393 = "393"
    VALUE_394 = "394"
    VALUE_397 = "397"
    VALUE_399 = "399"
    VALUE_402 = "402"
    VALUE_403 = "403"
    VALUE_404 = "404"
    VALUE_405 = "405"
    VALUE_407 = "407"
    VALUE_408 = "408"
    VALUE_409 = "409"
    VALUE_412 = "412"
    VALUE_416 = "416"
    VALUE_430 = "430"
    VALUE_431 = "431"
    VALUE_433 = "433"
    VALUE_436 = "436"
    VALUE_439 = "439"
    VALUE_440 = "440"
    VALUE_442 = "442"
    VALUE_444 = "444"
    VALUE_446 = "446"
    VALUE_448 = "448"
    VALUE_449 = "449"
    VALUE_452 = "452"
    VALUE_453 = "453"
    VALUE_454 = "454"
    VALUE_461 = "461"
    VALUE_462 = "462"
    VALUE_464 = "464"
    VALUE_467 = "467"
    VALUE_469 = "469"
    VALUE_470 = "470"
    VALUE_471 = "471"
    VALUE_472 = "472"
    VALUE_473 = "473"
    VALUE_479 = "479"
    VALUE_481 = "481"
    VALUE_483 = "483"
    VALUE_488 = "488"
    VALUE_491 = "491"
    VALUE_496 = "496"
    VALUE_497 = "497"
    VALUE_500 = "500"
    VALUE_502 = "502"
    VALUE_504 = "504"
    VALUE_506 = "506"
    VALUE_507 = "507"
    VALUE_508 = "508"
    VALUE_509 = "509"
    VALUE_510 = "510"
    VALUE_517 = "517"
    VALUE_519 = "519"
    VALUE_522 = "522"
    VALUE_524 = "524"
    VALUE_525 = "525"
    VALUE_528 = "528"
    VALUE_529 = "529"
    VALUE_530 = "530"
    VALUE_532 = "532"
    VALUE_539 = "539"
    VALUE_542 = "542"
    VALUE_543 = "543"
    VALUE_544 = "544"
    VALUE_545 = "545"
    VALUE_547 = "547"
    VALUE_548 = "548"
    VALUE_552 = "552"
    VALUE_553 = "553"
    VALUE_555 = "555"
    VALUE_558 = "558"
    VALUE_559 = "559"
    VALUE_561 = "561"
    VALUE_563 = "563"
    VALUE_564 = "564"
    VALUE_474 = "474"
    VALUE_475 = "475"
    VALUE_476 = "476"
    VALUE_477 = "477"
    VALUE_478 = "478"
    VALUE_480 = "480"
    VALUE_482 = "482"
    VALUE_484 = "484"
    VALUE_485 = "485"
    VALUE_486 = "486"
    VALUE_487 = "487"
    VALUE_489 = "489"
    VALUE_490 = "490"
    VALUE_410 = "410"
    VALUE_426 = "426"
    VALUE_432 = "432"
    VALUE_451 = "451"
    VALUE_523 = "523"
    VALUE_494 = "494"
    VALUE_495 = "495"
    VALUE_498 = "498"
    VALUE_499 = "499"
    VALUE_501 = "501"
    VALUE_503 = "503"
    VALUE_505 = "505"
    VALUE_511 = "511"
    VALUE_512 = "512"
    VALUE_513 = "513"
    VALUE_514 = "514"
    VALUE_515 = "515"
    VALUE_518 = "518"
    VALUE_520 = "520"
    VALUE_526 = "526"
    VALUE_527 = "527"
    VALUE_531 = "531"
    VALUE_533 = "533"
    VALUE_534 = "534"
    VALUE_537 = "537"
    VALUE_538 = "538"
    VALUE_541 = "541"
    VALUE_546 = "546"
    VALUE_550 = "550"
    VALUE_551 = "551"
    VALUE_554 = "554"
    VALUE_556 = "556"
    VALUE_557 = "557"
    VALUE_338 = "338"
    VALUE_344 = "344"
    VALUE_350 = "350"
    VALUE_353 = "353"
    VALUE_358 = "358"
    VALUE_363 = "363"
    VALUE_370 = "370"
    VALUE_384 = "384"
    VALUE_387 = "387"
    VALUE_391 = "391"
    VALUE_421 = "421"
    VALUE_428 = "428"
    VALUE_429 = "429"
    VALUE_447 = "447"
    VALUE_458 = "458"
    VALUE_492 = "492"
    VALUE_493 = "493"
    VALUE_516 = "516"
    VALUE_521 = "521"
    VALUE_535 = "535"
    VALUE_536 = "536"
    VALUE_540 = "540"
    VALUE_560 = "560"
    VALUE_562 = "562"
    VALUE_565 = "565"
    VALUE_566 = "566"
    VALUE_351 = "351"


class NativeEntityContiguous(Enum):
    """
    abstDomain: A12548 (C-0-T11631-A12548-cpt)
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    :cvar VALUE_10:
    :cvar VALUE_11:
    :cvar VALUE_12:
    :cvar VALUE_33:
    :cvar VALUE_13:
    :cvar VALUE_14:
    :cvar VALUE_15:
    :cvar VALUE_16:
    :cvar VALUE_17:
    :cvar VALUE_18:
    :cvar VALUE_19:
    :cvar VALUE_20:
    :cvar VALUE_21:
    :cvar VALUE_160:
    :cvar VALUE_22:
    :cvar VALUE_23:
    :cvar VALUE_24:
    :cvar VALUE_25:
    :cvar VALUE_26:
    :cvar VALUE_27:
    :cvar VALUE_29:
    :cvar VALUE_28:
    :cvar VALUE_30:
    :cvar VALUE_31:
    :cvar VALUE_32:
    :cvar VALUE_35:
    :cvar VALUE_36:
    :cvar VALUE_37:
    :cvar VALUE_38:
    :cvar VALUE_39:
    :cvar VALUE_40:
    :cvar VALUE_42:
    :cvar VALUE_41:
    :cvar VALUE_43:
    :cvar VALUE_44:
    :cvar VALUE_45:
    :cvar VALUE_46:
    :cvar VALUE_47:
    :cvar VALUE_48:
    :cvar VALUE_49:
    :cvar VALUE_50:
    :cvar VALUE_51:
    :cvar VALUE_52:
    :cvar VALUE_53:
    :cvar VALUE_54:
    :cvar VALUE_55:
    :cvar VALUE_64:
    :cvar VALUE_56:
    :cvar VALUE_57:
    :cvar VALUE_58:
    :cvar VALUE_59:
    :cvar VALUE_60:
    :cvar VALUE_61:
    :cvar VALUE_62:
    :cvar VALUE_63:
    :cvar VALUE_65:
    :cvar VALUE_66:
    :cvar VALUE_67:
    :cvar VALUE_68:
    :cvar VALUE_69:
    :cvar VALUE_71:
    :cvar VALUE_70:
    :cvar VALUE_72:
    :cvar VALUE_73:
    :cvar VALUE_74:
    :cvar VALUE_75:
    :cvar VALUE_76:
    :cvar VALUE_77:
    :cvar VALUE_78:
    :cvar VALUE_79:
    :cvar VALUE_80:
    :cvar VALUE_81:
    :cvar VALUE_82:
    :cvar VALUE_83:
    :cvar VALUE_84:
    :cvar VALUE_85:
    :cvar VALUE_86:
    :cvar VALUE_87:
    :cvar VALUE_88:
    :cvar VALUE_89:
    :cvar VALUE_90:
    :cvar VALUE_91:
    :cvar VALUE_92:
    :cvar VALUE_93:
    :cvar VALUE_94:
    :cvar VALUE_95:
    :cvar VALUE_96:
    :cvar VALUE_97:
    :cvar VALUE_98:
    :cvar VALUE_99:
    :cvar VALUE_100:
    :cvar VALUE_101:
    :cvar VALUE_102:
    :cvar VALUE_103:
    :cvar VALUE_104:
    :cvar VALUE_105:
    :cvar VALUE_106:
    :cvar VALUE_107:
    :cvar VALUE_108:
    :cvar VALUE_109:
    :cvar VALUE_110:
    :cvar VALUE_111:
    :cvar VALUE_112:
    :cvar VALUE_113:
    :cvar VALUE_114:
    :cvar VALUE_115:
    :cvar VALUE_116:
    :cvar VALUE_117:
    :cvar VALUE_118:
    :cvar VALUE_119:
    :cvar VALUE_120:
    :cvar VALUE_121:
    :cvar VALUE_122:
    :cvar VALUE_123:
    :cvar VALUE_124:
    :cvar VALUE_127:
    :cvar VALUE_125:
    :cvar VALUE_126:
    :cvar VALUE_128:
    :cvar VALUE_129:
    :cvar VALUE_130:
    :cvar VALUE_131:
    :cvar VALUE_132:
    :cvar VALUE_133:
    :cvar VALUE_135:
    :cvar VALUE_134:
    :cvar VALUE_136:
    :cvar VALUE_137:
    :cvar VALUE_138:
    :cvar VALUE_140:
    :cvar VALUE_141:
    :cvar VALUE_142:
    :cvar VALUE_143:
    :cvar VALUE_139:
    :cvar VALUE_144:
    :cvar VALUE_145:
    :cvar VALUE_146:
    :cvar VALUE_147:
    :cvar VALUE_148:
    :cvar VALUE_149:
    :cvar VALUE_150:
    :cvar VALUE_151:
    :cvar VALUE_152:
    :cvar VALUE_153:
    :cvar VALUE_154:
    :cvar VALUE_155:
    :cvar VALUE_156:
    :cvar VALUE_157:
    :cvar VALUE_158:
    :cvar VALUE_159:
    :cvar VALUE_161:
    :cvar VALUE_162:
    :cvar VALUE_163:
    :cvar VALUE_164:
    :cvar VALUE_165:
    :cvar VALUE_166:
    :cvar VALUE_167:
    :cvar VALUE_168:
    :cvar VALUE_169:
    :cvar VALUE_170:
    :cvar VALUE_171:
    :cvar VALUE_172:
    :cvar VALUE_173:
    :cvar VALUE_174:
    :cvar VALUE_175:
    :cvar VALUE_176:
    :cvar VALUE_177:
    :cvar VALUE_178:
    :cvar VALUE_179:
    :cvar VALUE_180:
    :cvar VALUE_181:
    :cvar VALUE_182:
    :cvar VALUE_184:
    :cvar VALUE_183:
    :cvar VALUE_185:
    :cvar VALUE_186:
    :cvar VALUE_188:
    :cvar VALUE_187:
    :cvar VALUE_189:
    :cvar VALUE_190:
    :cvar VALUE_191:
    :cvar VALUE_192:
    :cvar VALUE_193:
    :cvar VALUE_194:
    :cvar VALUE_195:
    :cvar VALUE_196:
    :cvar VALUE_197:
    :cvar VALUE_198:
    :cvar VALUE_199:
    :cvar VALUE_200:
    :cvar VALUE_201:
    :cvar VALUE_202:
    :cvar VALUE_203:
    :cvar VALUE_204:
    :cvar VALUE_205:
    :cvar VALUE_206:
    :cvar VALUE_207:
    :cvar VALUE_208:
    :cvar VALUE_209:
    :cvar VALUE_210:
    :cvar VALUE_212:
    :cvar VALUE_211:
    :cvar VALUE_213:
    :cvar VALUE_214:
    :cvar VALUE_215:
    :cvar VALUE_216:
    :cvar VALUE_217:
    :cvar VALUE_219:
    :cvar VALUE_218:
    :cvar VALUE_220:
    :cvar VALUE_221:
    :cvar VALUE_222:
    :cvar VALUE_223:
    :cvar VALUE_224:
    :cvar VALUE_225:
    :cvar VALUE_226:
    :cvar VALUE_227:
    :cvar VALUE_228:
    :cvar VALUE_229:
    :cvar VALUE_230:
    :cvar VALUE_231:
    :cvar VALUE_232:
    :cvar VALUE_233:
    :cvar VALUE_234:
    :cvar VALUE_235:
    :cvar VALUE_236:
    :cvar VALUE_237:
    :cvar VALUE_238:
    :cvar VALUE_239:
    :cvar VALUE_240:
    :cvar VALUE_241:
    :cvar VALUE_242:
    :cvar VALUE_243:
    :cvar VALUE_244:
    :cvar VALUE_245:
    :cvar VALUE_247:
    :cvar VALUE_248:
    :cvar VALUE_246:
    :cvar VALUE_249:
    :cvar VALUE_250:
    :cvar VALUE_251:
    :cvar VALUE_252:
    :cvar VALUE_253:
    :cvar VALUE_254:
    :cvar VALUE_255:
    :cvar VALUE_257:
    :cvar VALUE_256:
    :cvar VALUE_258:
    :cvar VALUE_259:
    :cvar VALUE_260:
    :cvar VALUE_261:
    :cvar VALUE_262:
    :cvar VALUE_263:
    :cvar VALUE_264:
    :cvar VALUE_265:
    :cvar VALUE_266:
    :cvar VALUE_267:
    :cvar VALUE_268:
    :cvar VALUE_269:
    :cvar VALUE_270:
    :cvar VALUE_271:
    :cvar VALUE_272:
    :cvar VALUE_273:
    :cvar VALUE_274:
    :cvar VALUE_275:
    :cvar VALUE_276:
    :cvar VALUE_277:
    :cvar VALUE_278:
    :cvar VALUE_279:
    :cvar VALUE_280:
    :cvar VALUE_281:
    :cvar VALUE_282:
    :cvar VALUE_283:
    :cvar VALUE_284:
    :cvar VALUE_285:
    :cvar VALUE_286:
    :cvar VALUE_287:
    :cvar VALUE_288:
    :cvar VALUE_289:
    :cvar VALUE_291:
    :cvar VALUE_290:
    :cvar VALUE_292:
    :cvar VALUE_293:
    :cvar VALUE_294:
    :cvar VALUE_295:
    :cvar VALUE_296:
    :cvar VALUE_297:
    :cvar VALUE_298:
    :cvar VALUE_299:
    :cvar VALUE_300:
    :cvar VALUE_301:
    :cvar VALUE_302:
    :cvar VALUE_303:
    :cvar VALUE_304:
    :cvar VALUE_305:
    :cvar VALUE_306:
    :cvar VALUE_308:
    :cvar VALUE_307:
    :cvar VALUE_309:
    :cvar VALUE_310:
    :cvar VALUE_311:
    :cvar VALUE_312:
    :cvar VALUE_313:
    :cvar VALUE_314:
    :cvar VALUE_315:
    :cvar VALUE_316:
    :cvar VALUE_317:
    :cvar VALUE_318:
    :cvar VALUE_319:
    :cvar VALUE_320:
    :cvar VALUE_321:
    :cvar VALUE_34:
    :cvar VALUE_322:
    :cvar VALUE_323:
    :cvar VALUE_324:
    :cvar VALUE_325:
    :cvar VALUE_326:
    :cvar VALUE_327:
    :cvar VALUE_328:
    :cvar VALUE_329:
    :cvar VALUE_330:
    :cvar VALUE_331:
    :cvar VALUE_332:
    :cvar VALUE_333:
    :cvar VALUE_334:
    :cvar VALUE_335:
    :cvar VALUE_336:
    :cvar VALUE_337:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_33 = "33"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_160 = "160"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_29 = "29"
    VALUE_28 = "28"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_42 = "42"
    VALUE_41 = "41"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_64 = "64"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_71 = "71"
    VALUE_70 = "70"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_81 = "81"
    VALUE_82 = "82"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_88 = "88"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"
    VALUE_100 = "100"
    VALUE_101 = "101"
    VALUE_102 = "102"
    VALUE_103 = "103"
    VALUE_104 = "104"
    VALUE_105 = "105"
    VALUE_106 = "106"
    VALUE_107 = "107"
    VALUE_108 = "108"
    VALUE_109 = "109"
    VALUE_110 = "110"
    VALUE_111 = "111"
    VALUE_112 = "112"
    VALUE_113 = "113"
    VALUE_114 = "114"
    VALUE_115 = "115"
    VALUE_116 = "116"
    VALUE_117 = "117"
    VALUE_118 = "118"
    VALUE_119 = "119"
    VALUE_120 = "120"
    VALUE_121 = "121"
    VALUE_122 = "122"
    VALUE_123 = "123"
    VALUE_124 = "124"
    VALUE_127 = "127"
    VALUE_125 = "125"
    VALUE_126 = "126"
    VALUE_128 = "128"
    VALUE_129 = "129"
    VALUE_130 = "130"
    VALUE_131 = "131"
    VALUE_132 = "132"
    VALUE_133 = "133"
    VALUE_135 = "135"
    VALUE_134 = "134"
    VALUE_136 = "136"
    VALUE_137 = "137"
    VALUE_138 = "138"
    VALUE_140 = "140"
    VALUE_141 = "141"
    VALUE_142 = "142"
    VALUE_143 = "143"
    VALUE_139 = "139"
    VALUE_144 = "144"
    VALUE_145 = "145"
    VALUE_146 = "146"
    VALUE_147 = "147"
    VALUE_148 = "148"
    VALUE_149 = "149"
    VALUE_150 = "150"
    VALUE_151 = "151"
    VALUE_152 = "152"
    VALUE_153 = "153"
    VALUE_154 = "154"
    VALUE_155 = "155"
    VALUE_156 = "156"
    VALUE_157 = "157"
    VALUE_158 = "158"
    VALUE_159 = "159"
    VALUE_161 = "161"
    VALUE_162 = "162"
    VALUE_163 = "163"
    VALUE_164 = "164"
    VALUE_165 = "165"
    VALUE_166 = "166"
    VALUE_167 = "167"
    VALUE_168 = "168"
    VALUE_169 = "169"
    VALUE_170 = "170"
    VALUE_171 = "171"
    VALUE_172 = "172"
    VALUE_173 = "173"
    VALUE_174 = "174"
    VALUE_175 = "175"
    VALUE_176 = "176"
    VALUE_177 = "177"
    VALUE_178 = "178"
    VALUE_179 = "179"
    VALUE_180 = "180"
    VALUE_181 = "181"
    VALUE_182 = "182"
    VALUE_184 = "184"
    VALUE_183 = "183"
    VALUE_185 = "185"
    VALUE_186 = "186"
    VALUE_188 = "188"
    VALUE_187 = "187"
    VALUE_189 = "189"
    VALUE_190 = "190"
    VALUE_191 = "191"
    VALUE_192 = "192"
    VALUE_193 = "193"
    VALUE_194 = "194"
    VALUE_195 = "195"
    VALUE_196 = "196"
    VALUE_197 = "197"
    VALUE_198 = "198"
    VALUE_199 = "199"
    VALUE_200 = "200"
    VALUE_201 = "201"
    VALUE_202 = "202"
    VALUE_203 = "203"
    VALUE_204 = "204"
    VALUE_205 = "205"
    VALUE_206 = "206"
    VALUE_207 = "207"
    VALUE_208 = "208"
    VALUE_209 = "209"
    VALUE_210 = "210"
    VALUE_212 = "212"
    VALUE_211 = "211"
    VALUE_213 = "213"
    VALUE_214 = "214"
    VALUE_215 = "215"
    VALUE_216 = "216"
    VALUE_217 = "217"
    VALUE_219 = "219"
    VALUE_218 = "218"
    VALUE_220 = "220"
    VALUE_221 = "221"
    VALUE_222 = "222"
    VALUE_223 = "223"
    VALUE_224 = "224"
    VALUE_225 = "225"
    VALUE_226 = "226"
    VALUE_227 = "227"
    VALUE_228 = "228"
    VALUE_229 = "229"
    VALUE_230 = "230"
    VALUE_231 = "231"
    VALUE_232 = "232"
    VALUE_233 = "233"
    VALUE_234 = "234"
    VALUE_235 = "235"
    VALUE_236 = "236"
    VALUE_237 = "237"
    VALUE_238 = "238"
    VALUE_239 = "239"
    VALUE_240 = "240"
    VALUE_241 = "241"
    VALUE_242 = "242"
    VALUE_243 = "243"
    VALUE_244 = "244"
    VALUE_245 = "245"
    VALUE_247 = "247"
    VALUE_248 = "248"
    VALUE_246 = "246"
    VALUE_249 = "249"
    VALUE_250 = "250"
    VALUE_251 = "251"
    VALUE_252 = "252"
    VALUE_253 = "253"
    VALUE_254 = "254"
    VALUE_255 = "255"
    VALUE_257 = "257"
    VALUE_256 = "256"
    VALUE_258 = "258"
    VALUE_259 = "259"
    VALUE_260 = "260"
    VALUE_261 = "261"
    VALUE_262 = "262"
    VALUE_263 = "263"
    VALUE_264 = "264"
    VALUE_265 = "265"
    VALUE_266 = "266"
    VALUE_267 = "267"
    VALUE_268 = "268"
    VALUE_269 = "269"
    VALUE_270 = "270"
    VALUE_271 = "271"
    VALUE_272 = "272"
    VALUE_273 = "273"
    VALUE_274 = "274"
    VALUE_275 = "275"
    VALUE_276 = "276"
    VALUE_277 = "277"
    VALUE_278 = "278"
    VALUE_279 = "279"
    VALUE_280 = "280"
    VALUE_281 = "281"
    VALUE_282 = "282"
    VALUE_283 = "283"
    VALUE_284 = "284"
    VALUE_285 = "285"
    VALUE_286 = "286"
    VALUE_287 = "287"
    VALUE_288 = "288"
    VALUE_289 = "289"
    VALUE_291 = "291"
    VALUE_290 = "290"
    VALUE_292 = "292"
    VALUE_293 = "293"
    VALUE_294 = "294"
    VALUE_295 = "295"
    VALUE_296 = "296"
    VALUE_297 = "297"
    VALUE_298 = "298"
    VALUE_299 = "299"
    VALUE_300 = "300"
    VALUE_301 = "301"
    VALUE_302 = "302"
    VALUE_303 = "303"
    VALUE_304 = "304"
    VALUE_305 = "305"
    VALUE_306 = "306"
    VALUE_308 = "308"
    VALUE_307 = "307"
    VALUE_309 = "309"
    VALUE_310 = "310"
    VALUE_311 = "311"
    VALUE_312 = "312"
    VALUE_313 = "313"
    VALUE_314 = "314"
    VALUE_315 = "315"
    VALUE_316 = "316"
    VALUE_317 = "317"
    VALUE_318 = "318"
    VALUE_319 = "319"
    VALUE_320 = "320"
    VALUE_321 = "321"
    VALUE_34 = "34"
    VALUE_322 = "322"
    VALUE_323 = "323"
    VALUE_324 = "324"
    VALUE_325 = "325"
    VALUE_326 = "326"
    VALUE_327 = "327"
    VALUE_328 = "328"
    VALUE_329 = "329"
    VALUE_330 = "330"
    VALUE_331 = "331"
    VALUE_332 = "332"
    VALUE_333 = "333"
    VALUE_334 = "334"
    VALUE_335 = "335"
    VALUE_336 = "336"
    VALUE_337 = "337"


class NaturalChild(Enum):
    """
    specDomain: S17930 (C-0-T12206-A19563-S17926-S16360-S17930-cpt)
    :cvar NCHILD:
    :cvar DAU:
    :cvar SON:
    """
    NCHILD = "NCHILD"
    DAU = "DAU"
    SON = "SON"


class NaturalFather(Enum):
    """
    specDomain: S19765 (C-0-T12206-A19563-S17926-S16346-S19764-S19765-cpt)
    :cvar NFTH:
    :cvar NFTHF:
    """
    NFTH = "NFTH"
    NFTHF = "NFTHF"


class NaturalParent(Enum):
    """
    specDomain: S19764 (C-0-T12206-A19563-S17926-S16346-S19764-cpt)
    :cvar NFTH:
    :cvar NFTHF:
    :cvar NPRN:
    :cvar NMTH:
    """
    NFTH = "NFTH"
    NFTHF = "NFTHF"
    NPRN = "NPRN"
    NMTH = "NMTH"


class NaturalSibling(Enum):
    """
    specDomain: S19773 (C-0-T12206-A19563-S17926-S11567-S19773-cpt)
    :cvar NSIB:
    :cvar NBRO:
    :cvar NSIS:
    """
    NSIB = "NSIB"
    NBRO = "NBRO"
    NSIS = "NSIS"


class Nebulization(Enum):
    """
    abstDomain: A14728 (C-0-T14581-A16931-A14728-cpt)
    :cvar ETNEB:
    """
    ETNEB = "ETNEB"


class NebulizationInhalation(Enum):
    """
    specDomain: S14619 (C-0-T14581-A16931-A14615-S14619-cpt)
    :cvar NEB:
    :cvar NASNEB:
    :cvar ORNEB:
    """
    NEB = "NEB"
    NASNEB = "NASNEB"
    ORNEB = "ORNEB"


class NephClinPracticeSetting(Enum):
    """
    specDomain: S10943 (C-0-T12206-A17660-A19450-A10588-S10589-S10943-cpt)
    :cvar NEPH:
    :cvar PEDNEPH:
    """
    NEPH = "NEPH"
    PEDNEPH = "PEDNEPH"


class NeuropsychologistHipaa(Enum):
    """
    abstDomain: A13147 (C-0-T13129-A13130-A13131-A13147-cpt)
    :cvar VALUE_103_GC0700_N:
    """
    VALUE_103_GC0700_N = "103GC0700N"


class NeuropsychologistProviderCodes(Enum):
    """
    specDomain: S20283 (C-0-T19465-S20275-S20283-cpt)
    :cvar VALUE_103_G00000_X:
    :cvar VALUE_103_GC0700_X:
    """
    VALUE_103_G00000_X = "103G00000X"
    VALUE_103_GC0700_X = "103GC0700X"


class NieceNephew(Enum):
    """
    specDomain: S19750 (C-0-T12206-A19563-S17926-S19750-cpt)
    :cvar NIENEPH:
    :cvar NEPHEW:
    :cvar NIECE:
    """
    NIENEPH = "NIENEPH"
    NEPHEW = "NEPHEW"
    NIECE = "NIECE"


class NoInformation(Enum):
    """
    specDomain: S10610 (C-0-T10609-S10610-cpt)
    :cvar OTH:
    :cvar NINF:
    :cvar PINF:
    :cvar ASKU:
    :cvar NAV:
    :cvar UNK:
    :cvar QS:
    :cvar NASK:
    :cvar TRC:
    :cvar NI:
    :cvar MSK:
    :cvar NA:
    :cvar UNC:
    """
    OTH = "OTH"
    NINF = "NINF"
    PINF = "PINF"
    ASKU = "ASKU"
    NAV = "NAV"
    UNK = "UNK"
    QS = "QS"
    NASK = "NASK"
    TRC = "TRC"
    NI = "NI"
    MSK = "MSK"
    NA = "NA"
    UNC = "UNC"


class NonDrugAgentEntity(Enum):
    """
    abstDomain: A19699 (C-0-T16040-A16041-A19698-A19699-cpt)
    :cvar NDA16:
    :cvar NDA17:
    :cvar NDA01:
    :cvar NDA02:
    :cvar NDA08:
    :cvar NDA03:
    :cvar NDA12:
    :cvar NDA10:
    :cvar NDA04:
    :cvar NDA13:
    :cvar NDA09:
    :cvar NDA05:
    :cvar NDA14:
    :cvar NDA06:
    :cvar NDA15:
    :cvar NDA11:
    :cvar NDA07:
    """
    NDA16 = "NDA16"
    NDA17 = "NDA17"
    NDA01 = "NDA01"
    NDA02 = "NDA02"
    NDA08 = "NDA08"
    NDA03 = "NDA03"
    NDA12 = "NDA12"
    NDA10 = "NDA10"
    NDA04 = "NDA04"
    NDA13 = "NDA13"
    NDA09 = "NDA09"
    NDA05 = "NDA05"
    NDA14 = "NDA14"
    NDA06 = "NDA06"
    NDA15 = "NDA15"
    NDA11 = "NDA11"
    NDA07 = "NDA07"


class NonRigidContainerEntityType(Enum):
    """
    abstDomain: A16147 (C-0-T16040-A16041-A19867-A16143-S16144-A16147-cpt)
    :cvar BAG:
    :cvar PACKT:
    :cvar PCH:
    :cvar SACH:
    """
    BAG = "BAG"
    PACKT = "PACKT"
    PCH = "PCH"
    SACH = "SACH"


class Nootkan(Enum):
    """
    abstDomain: A18641 (C-0-T18130-A18640-A18641-cpt)
    :cvar X_MYH:
    """
    X_MYH = "x-MYH"


class NorthernCaddoan(Enum):
    """
    abstDomain: A18224 (C-0-T18130-A18223-A18224-cpt)
    :cvar X_ARI:
    :cvar X_PAW:
    :cvar X_WIC:
    """
    X_ARI = "x-ARI"
    X_PAW = "x-PAW"
    X_WIC = "x-WIC"


class NorthernIroquoian(Enum):
    """
    abstDomain: A18307 (C-0-T18130-A18306-A18307-cpt)
    :cvar X_CAY:
    :cvar X_MOH:
    :cvar X_ONE:
    :cvar X_ONO:
    :cvar X_SEE:
    :cvar X_TUS:
    """
    X_CAY = "x-CAY"
    X_MOH = "x-MOH"
    X_ONE = "x-ONE"
    X_ONO = "x-ONO"
    X_SEE = "x-SEE"
    X_TUS = "x-TUS"


class NuclearMedicineProviderCodes(Enum):
    """
    specDomain: S20159 (C-0-T19465-S20096-S20159-cpt)
    :cvar VALUE_207_U00000_X:
    :cvar VALUE_207_UN0903_X:
    :cvar VALUE_207_UN0901_X:
    :cvar VALUE_207_UN0902_X:
    """
    VALUE_207_U00000_X = "207U00000X"
    VALUE_207_UN0903_X = "207UN0903X"
    VALUE_207_UN0901_X = "207UN0901X"
    VALUE_207_UN0902_X = "207UN0902X"


class NullFlavor(Enum):
    """
    vocSet: T10609 (C-0-T10609-cpt)
    :cvar OTH:
    :cvar NINF:
    :cvar PINF:
    :cvar ASKU:
    :cvar NAV:
    :cvar UNK:
    :cvar QS:
    :cvar NASK:
    :cvar TRC:
    :cvar NI:
    :cvar MSK:
    :cvar NA:
    :cvar UNC:
    """
    OTH = "OTH"
    NINF = "NINF"
    PINF = "PINF"
    ASKU = "ASKU"
    NAV = "NAV"
    UNK = "UNK"
    QS = "QS"
    NASK = "NASK"
    TRC = "TRC"
    NI = "NI"
    MSK = "MSK"
    NA = "NA"
    UNC = "UNC"


class NursePractitionerHipaa(Enum):
    """
    specDomain: S13402 (C-0-T13129-A13130-A13363-S13402-cpt)
    :cvar VALUE_363_L00000_N:
    :cvar VALUE_363_LA2100_N:
    :cvar VALUE_363_LA2200_N:
    :cvar VALUE_363_LC1500_N:
    :cvar VALUE_363_LC0200_N:
    :cvar VALUE_363_LF0000_N:
    :cvar VALUE_363_LG0600_N:
    :cvar VALUE_363_LN0000_N:
    :cvar VALUE_363_LN0005_N:
    :cvar VALUE_363_LX0001_N:
    :cvar VALUE_363_LX0106_N:
    :cvar VALUE_363_LP0200_N:
    :cvar VALUE_363_LP0223_N:
    :cvar VALUE_363_LP0222_N:
    :cvar VALUE_363_LP1700_N:
    :cvar VALUE_363_LP2300_N:
    :cvar VALUE_363_LP0808_N:
    :cvar VALUE_363_LS0200_N:
    :cvar VALUE_363_LW0102_N:
    """
    VALUE_363_L00000_N = "363L00000N"
    VALUE_363_LA2100_N = "363LA2100N"
    VALUE_363_LA2200_N = "363LA2200N"
    VALUE_363_LC1500_N = "363LC1500N"
    VALUE_363_LC0200_N = "363LC0200N"
    VALUE_363_LF0000_N = "363LF0000N"
    VALUE_363_LG0600_N = "363LG0600N"
    VALUE_363_LN0000_N = "363LN0000N"
    VALUE_363_LN0005_N = "363LN0005N"
    VALUE_363_LX0001_N = "363LX0001N"
    VALUE_363_LX0106_N = "363LX0106N"
    VALUE_363_LP0200_N = "363LP0200N"
    VALUE_363_LP0223_N = "363LP0223N"
    VALUE_363_LP0222_N = "363LP0222N"
    VALUE_363_LP1700_N = "363LP1700N"
    VALUE_363_LP2300_N = "363LP2300N"
    VALUE_363_LP0808_N = "363LP0808N"
    VALUE_363_LS0200_N = "363LS0200N"
    VALUE_363_LW0102_N = "363LW0102N"


class NursePractitionerProviderCodes(Enum):
    """
    specDomain: S20501 (C-0-T19465-S20463-S20501-cpt)
    :cvar VALUE_363_A00000_X:
    :cvar VALUE_363_AM0700_X:
    :cvar VALUE_363_AS0400_X:
    :cvar VALUE_363_L00000_X:
    :cvar VALUE_363_LA2100_X:
    :cvar VALUE_363_LA2200_X:
    :cvar VALUE_363_LC1500_X:
    :cvar VALUE_363_LC0200_X:
    :cvar VALUE_363_LF0000_X:
    :cvar VALUE_363_LG0600_X:
    :cvar VALUE_363_LN0000_X:
    :cvar VALUE_363_LN0005_X:
    :cvar VALUE_363_LX0001_X:
    :cvar VALUE_363_LX0106_X:
    :cvar VALUE_363_LP0200_X:
    :cvar VALUE_363_LP0222_X:
    :cvar VALUE_363_LP1700_X:
    :cvar VALUE_363_LP2300_X:
    :cvar VALUE_363_LP0808_X:
    :cvar VALUE_363_LS0200_X:
    :cvar VALUE_363_LW0102_X:
    """
    VALUE_363_A00000_X = "363A00000X"
    VALUE_363_AM0700_X = "363AM0700X"
    VALUE_363_AS0400_X = "363AS0400X"
    VALUE_363_L00000_X = "363L00000X"
    VALUE_363_LA2100_X = "363LA2100X"
    VALUE_363_LA2200_X = "363LA2200X"
    VALUE_363_LC1500_X = "363LC1500X"
    VALUE_363_LC0200_X = "363LC0200X"
    VALUE_363_LF0000_X = "363LF0000X"
    VALUE_363_LG0600_X = "363LG0600X"
    VALUE_363_LN0000_X = "363LN0000X"
    VALUE_363_LN0005_X = "363LN0005X"
    VALUE_363_LX0001_X = "363LX0001X"
    VALUE_363_LX0106_X = "363LX0106X"
    VALUE_363_LP0200_X = "363LP0200X"
    VALUE_363_LP0222_X = "363LP0222X"
    VALUE_363_LP1700_X = "363LP1700X"
    VALUE_363_LP2300_X = "363LP2300X"
    VALUE_363_LP0808_X = "363LP0808X"
    VALUE_363_LS0200_X = "363LS0200X"
    VALUE_363_LW0102_X = "363LW0102X"


class NursingOrCustodialCarePracticeSetting(Enum):
    """
    specDomain: S10605 (C-0-T12206-A17660-A19450-A10588-S10605-cpt)
    :cvar NCCF:
    :cvar VALUE_314000000_N:
    :cvar SNF:
    """
    NCCF = "NCCF"
    VALUE_314000000_N = "314000000N"
    SNF = "SNF"


class NursingServiceProviderHipaa(Enum):
    """
    abstDomain: A13229 (C-0-T13129-A13130-A13229-cpt)
    :cvar VALUE_163_W00000_N:
    :cvar VALUE_163_WA0400_N:
    :cvar VALUE_163_WA2000_N:
    :cvar VALUE_163_WC3500_N:
    :cvar VALUE_163_WC0400_N:
    :cvar VALUE_163_WC1400_N:
    :cvar VALUE_163_WC1500_N:
    :cvar VALUE_163_WC2100_N:
    :cvar VALUE_163_WC1600_N:
    :cvar VALUE_163_WC0200_N:
    :cvar VALUE_163_WD0400_N:
    :cvar VALUE_163_WD1100_N:
    :cvar VALUE_163_WE0003_N:
    :cvar VALUE_163_WE0900_N:
    :cvar VALUE_163_WF0300_N:
    :cvar VALUE_163_WG0100_N:
    :cvar VALUE_163_WG0000_N:
    :cvar VALUE_163_WG0600_N:
    :cvar VALUE_163_WH0500_N:
    :cvar VALUE_163_WH0200_N:
    :cvar VALUE_163_WH1000_N:
    :cvar VALUE_163_WI0600_N:
    :cvar VALUE_163_WI0500_N:
    :cvar VALUE_163_WL0100_N:
    :cvar VALUE_163_WM1400_N:
    :cvar VALUE_163_WM0102_N:
    :cvar VALUE_163_WM0705_N:
    :cvar VALUE_163_WN0002_N:
    :cvar VALUE_163_WN0003_N:
    :cvar VALUE_163_WN0300_N:
    :cvar VALUE_163_WN0800_N:
    :cvar VALUE_163_WN1003_N:
    :cvar VALUE_163_WX0002_N:
    :cvar VALUE_163_WX0003_N:
    :cvar VALUE_163_WX0106_N:
    :cvar VALUE_163_WX0200_N:
    :cvar VALUE_163_WX1000_N:
    :cvar VALUE_163_WX1100_N:
    :cvar VALUE_163_WX0800_N:
    :cvar VALUE_163_WX1500_N:
    :cvar VALUE_163_WX0601_N:
    :cvar VALUE_163_WP0000_N:
    :cvar VALUE_163_WP0218_N:
    :cvar VALUE_163_WP0200_N:
    :cvar VALUE_163_WP1700_N:
    :cvar VALUE_163_WP2200_N:
    :cvar VALUE_163_WP2201_N:
    :cvar VALUE_163_WP0808_N:
    :cvar VALUE_163_WP0809_N:
    :cvar VALUE_163_WP0807_N:
    :cvar VALUE_163_WR0400_N:
    :cvar VALUE_163_WR1000_N:
    :cvar VALUE_163_WS0200_N:
    :cvar VALUE_163_WS0121_N:
    :cvar VALUE_163_WU0100_N:
    :cvar VALUE_163_WW0101_N:
    :cvar VALUE_163_WW0000_N:
    :cvar VALUE_164_W00000_N:
    :cvar VALUE_164_X00000_N:
    """
    VALUE_163_W00000_N = "163W00000N"
    VALUE_163_WA0400_N = "163WA0400N"
    VALUE_163_WA2000_N = "163WA2000N"
    VALUE_163_WC3500_N = "163WC3500N"
    VALUE_163_WC0400_N = "163WC0400N"
    VALUE_163_WC1400_N = "163WC1400N"
    VALUE_163_WC1500_N = "163WC1500N"
    VALUE_163_WC2100_N = "163WC2100N"
    VALUE_163_WC1600_N = "163WC1600N"
    VALUE_163_WC0200_N = "163WC0200N"
    VALUE_163_WD0400_N = "163WD0400N"
    VALUE_163_WD1100_N = "163WD1100N"
    VALUE_163_WE0003_N = "163WE0003N"
    VALUE_163_WE0900_N = "163WE0900N"
    VALUE_163_WF0300_N = "163WF0300N"
    VALUE_163_WG0100_N = "163WG0100N"
    VALUE_163_WG0000_N = "163WG0000N"
    VALUE_163_WG0600_N = "163WG0600N"
    VALUE_163_WH0500_N = "163WH0500N"
    VALUE_163_WH0200_N = "163WH0200N"
    VALUE_163_WH1000_N = "163WH1000N"
    VALUE_163_WI0600_N = "163WI0600N"
    VALUE_163_WI0500_N = "163WI0500N"
    VALUE_163_WL0100_N = "163WL0100N"
    VALUE_163_WM1400_N = "163WM1400N"
    VALUE_163_WM0102_N = "163WM0102N"
    VALUE_163_WM0705_N = "163WM0705N"
    VALUE_163_WN0002_N = "163WN0002N"
    VALUE_163_WN0003_N = "163WN0003N"
    VALUE_163_WN0300_N = "163WN0300N"
    VALUE_163_WN0800_N = "163WN0800N"
    VALUE_163_WN1003_N = "163WN1003N"
    VALUE_163_WX0002_N = "163WX0002N"
    VALUE_163_WX0003_N = "163WX0003N"
    VALUE_163_WX0106_N = "163WX0106N"
    VALUE_163_WX0200_N = "163WX0200N"
    VALUE_163_WX1000_N = "163WX1000N"
    VALUE_163_WX1100_N = "163WX1100N"
    VALUE_163_WX0800_N = "163WX0800N"
    VALUE_163_WX1500_N = "163WX1500N"
    VALUE_163_WX0601_N = "163WX0601N"
    VALUE_163_WP0000_N = "163WP0000N"
    VALUE_163_WP0218_N = "163WP0218N"
    VALUE_163_WP0200_N = "163WP0200N"
    VALUE_163_WP1700_N = "163WP1700N"
    VALUE_163_WP2200_N = "163WP2200N"
    VALUE_163_WP2201_N = "163WP2201N"
    VALUE_163_WP0808_N = "163WP0808N"
    VALUE_163_WP0809_N = "163WP0809N"
    VALUE_163_WP0807_N = "163WP0807N"
    VALUE_163_WR0400_N = "163WR0400N"
    VALUE_163_WR1000_N = "163WR1000N"
    VALUE_163_WS0200_N = "163WS0200N"
    VALUE_163_WS0121_N = "163WS0121N"
    VALUE_163_WU0100_N = "163WU0100N"
    VALUE_163_WW0101_N = "163WW0101N"
    VALUE_163_WW0000_N = "163WW0000N"
    VALUE_164_W00000_N = "164W00000N"
    VALUE_164_X00000_N = "164X00000N"


class NursingServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20366 (C-0-T19465-S20366-cpt)
    :cvar VALUE_163_W00000_X:
    :cvar VALUE_163_WA0400_X:
    :cvar VALUE_163_WA2000_X:
    :cvar VALUE_163_WP2201_X:
    :cvar VALUE_163_WC3500_X:
    :cvar VALUE_163_WC0400_X:
    :cvar VALUE_163_WC1400_X:
    :cvar VALUE_163_WC1500_X:
    :cvar VALUE_163_WC2100_X:
    :cvar VALUE_163_WC1600_X:
    :cvar VALUE_163_WC0200_X:
    :cvar VALUE_163_WD0400_X:
    :cvar VALUE_163_WD1100_X:
    :cvar VALUE_163_WE0003_X:
    :cvar VALUE_163_WE0900_X:
    :cvar VALUE_163_WF0300_X:
    :cvar VALUE_163_WG0100_X:
    :cvar VALUE_163_WG0000_X:
    :cvar VALUE_163_WG0600_X:
    :cvar VALUE_163_WH0500_X:
    :cvar VALUE_163_WH0200_X:
    :cvar VALUE_163_WH1000_X:
    :cvar VALUE_163_WI0600_X:
    :cvar VALUE_163_WI0500_X:
    :cvar VALUE_163_WL0100_X:
    :cvar VALUE_163_WM0102_X:
    :cvar VALUE_163_WM0705_X:
    :cvar VALUE_163_WN0002_X:
    :cvar VALUE_163_WN0003_X:
    :cvar VALUE_163_WN0300_X:
    :cvar VALUE_163_WN0800_X:
    :cvar VALUE_163_WM1400_X:
    :cvar VALUE_163_WN1003_X:
    :cvar VALUE_163_WX0002_X:
    :cvar VALUE_163_WX0003_X:
    :cvar VALUE_163_WX0106_X:
    :cvar VALUE_163_WX0200_X:
    :cvar VALUE_163_WX1100_X:
    :cvar VALUE_163_WX0800_X:
    :cvar VALUE_163_WX1500_X:
    :cvar VALUE_163_WX0601_X:
    :cvar VALUE_163_WP0000_X:
    :cvar VALUE_163_WP0218_X:
    :cvar VALUE_163_WP0200_X:
    :cvar VALUE_163_WP1700_X:
    :cvar VALUE_163_WS0121_X:
    :cvar VALUE_163_WP0808_X:
    :cvar VALUE_163_WP0809_X:
    :cvar VALUE_163_WP0807_X:
    :cvar VALUE_163_WR0400_X:
    :cvar VALUE_163_WR1000_X:
    :cvar VALUE_163_WS0200_X:
    :cvar VALUE_163_WU0100_X:
    :cvar VALUE_163_WW0101_X:
    :cvar VALUE_163_WW0000_X:
    :cvar VALUE_160000000_X:
    :cvar VALUE_164_W00000_X:
    :cvar VALUE_167_G00000_X:
    :cvar VALUE_164_X00000_X:
    """
    VALUE_163_W00000_X = "163W00000X"
    VALUE_163_WA0400_X = "163WA0400X"
    VALUE_163_WA2000_X = "163WA2000X"
    VALUE_163_WP2201_X = "163WP2201X"
    VALUE_163_WC3500_X = "163WC3500X"
    VALUE_163_WC0400_X = "163WC0400X"
    VALUE_163_WC1400_X = "163WC1400X"
    VALUE_163_WC1500_X = "163WC1500X"
    VALUE_163_WC2100_X = "163WC2100X"
    VALUE_163_WC1600_X = "163WC1600X"
    VALUE_163_WC0200_X = "163WC0200X"
    VALUE_163_WD0400_X = "163WD0400X"
    VALUE_163_WD1100_X = "163WD1100X"
    VALUE_163_WE0003_X = "163WE0003X"
    VALUE_163_WE0900_X = "163WE0900X"
    VALUE_163_WF0300_X = "163WF0300X"
    VALUE_163_WG0100_X = "163WG0100X"
    VALUE_163_WG0000_X = "163WG0000X"
    VALUE_163_WG0600_X = "163WG0600X"
    VALUE_163_WH0500_X = "163WH0500X"
    VALUE_163_WH0200_X = "163WH0200X"
    VALUE_163_WH1000_X = "163WH1000X"
    VALUE_163_WI0600_X = "163WI0600X"
    VALUE_163_WI0500_X = "163WI0500X"
    VALUE_163_WL0100_X = "163WL0100X"
    VALUE_163_WM0102_X = "163WM0102X"
    VALUE_163_WM0705_X = "163WM0705X"
    VALUE_163_WN0002_X = "163WN0002X"
    VALUE_163_WN0003_X = "163WN0003X"
    VALUE_163_WN0300_X = "163WN0300X"
    VALUE_163_WN0800_X = "163WN0800X"
    VALUE_163_WM1400_X = "163WM1400X"
    VALUE_163_WN1003_X = "163WN1003X"
    VALUE_163_WX0002_X = "163WX0002X"
    VALUE_163_WX0003_X = "163WX0003X"
    VALUE_163_WX0106_X = "163WX0106X"
    VALUE_163_WX0200_X = "163WX0200X"
    VALUE_163_WX1100_X = "163WX1100X"
    VALUE_163_WX0800_X = "163WX0800X"
    VALUE_163_WX1500_X = "163WX1500X"
    VALUE_163_WX0601_X = "163WX0601X"
    VALUE_163_WP0000_X = "163WP0000X"
    VALUE_163_WP0218_X = "163WP0218X"
    VALUE_163_WP0200_X = "163WP0200X"
    VALUE_163_WP1700_X = "163WP1700X"
    VALUE_163_WS0121_X = "163WS0121X"
    VALUE_163_WP0808_X = "163WP0808X"
    VALUE_163_WP0809_X = "163WP0809X"
    VALUE_163_WP0807_X = "163WP0807X"
    VALUE_163_WR0400_X = "163WR0400X"
    VALUE_163_WR1000_X = "163WR1000X"
    VALUE_163_WS0200_X = "163WS0200X"
    VALUE_163_WU0100_X = "163WU0100X"
    VALUE_163_WW0101_X = "163WW0101X"
    VALUE_163_WW0000_X = "163WW0000X"
    VALUE_160000000_X = "160000000X"
    VALUE_164_W00000_X = "164W00000X"
    VALUE_167_G00000_X = "167G00000X"
    VALUE_164_X00000_X = "164X00000X"


class NursingServiceRelatedProviderHipaa(Enum):
    """
    specDomain: S13134 (C-0-T13129-A13130-S13134-cpt)
    :cvar VALUE_3747_P1801_N:
    :cvar VALUE_374700000_N:
    """
    VALUE_3747_P1801_N = "3747P1801N"
    VALUE_374700000_N = "374700000N"


class NursingServiceRelatedProviderTechnicianHipaa(Enum):
    """
    abstDomain: A13134 (C-0-T13129-A13130-S13134-A13134-cpt)
    :cvar VALUE_3747_P1801_N:
    """
    VALUE_3747_P1801_N = "3747P1801N"


class NursingServiceRelatedProvidersProviderCodes(Enum):
    """
    specDomain: S20425 (C-0-T19465-S20425-cpt)
    :cvar VALUE_374700000_X:
    :cvar VALUE_3747_A0650_X:
    :cvar VALUE_3747_P1801_X:
    :cvar VALUE_370000000_X:
    :cvar VALUE_372600000_X:
    :cvar VALUE_372500000_X:
    :cvar VALUE_374_T00000_X:
    :cvar VALUE_373_H00000_X:
    :cvar VALUE_374_U00000_X:
    :cvar VALUE_376_J00000_X:
    :cvar VALUE_376_K00000_X:
    :cvar VALUE_376_G00000_X:
    """
    VALUE_374700000_X = "374700000X"
    VALUE_3747_A0650_X = "3747A0650X"
    VALUE_3747_P1801_X = "3747P1801X"
    VALUE_370000000_X = "370000000X"
    VALUE_372600000_X = "372600000X"
    VALUE_372500000_X = "372500000X"
    VALUE_374_T00000_X = "374T00000X"
    VALUE_373_H00000_X = "373H00000X"
    VALUE_374_U00000_X = "374U00000X"
    VALUE_376_J00000_X = "376J00000X"
    VALUE_376_K00000_X = "376K00000X"
    VALUE_376_G00000_X = "376G00000X"


class NursingandCustodialCareFacilitiesProviderCodes(Enum):
    """
    specDomain: S20758 (C-0-T19465-S20758-cpt)
    :cvar VALUE_310400000_X:
    :cvar VALUE_3104_A0630_X:
    :cvar VALUE_3104_A0625_X:
    :cvar VALUE_311_Z00000_X:
    :cvar VALUE_311_ZA0620_X:
    :cvar VALUE_314000000_X:
    :cvar VALUE_3140_N1450_X:
    :cvar VALUE_310000000_X:
    :cvar VALUE_311500000_X:
    :cvar VALUE_317400000_X:
    :cvar VALUE_315_D00000_X:
    :cvar VALUE_315_P00000_X:
    :cvar VALUE_310500000_X:
    :cvar VALUE_313_M00000_X:
    """
    VALUE_310400000_X = "310400000X"
    VALUE_3104_A0630_X = "3104A0630X"
    VALUE_3104_A0625_X = "3104A0625X"
    VALUE_311_Z00000_X = "311Z00000X"
    VALUE_311_ZA0620_X = "311ZA0620X"
    VALUE_314000000_X = "314000000X"
    VALUE_3140_N1450_X = "3140N1450X"
    VALUE_310000000_X = "310000000X"
    VALUE_311500000_X = "311500000X"
    VALUE_317400000_X = "317400000X"
    VALUE_315_D00000_X = "315D00000X"
    VALUE_315_P00000_X = "315P00000X"
    VALUE_310500000_X = "310500000X"
    VALUE_313_M00000_X = "313M00000X"


class NutritionistHipaa(Enum):
    """
    specDomain: S13205 (C-0-T13129-A13130-A13197-S13205-cpt)
    :cvar VALUE_133_N00000_N:
    :cvar VALUE_133_NN1002_N:
    """
    VALUE_133_N00000_N = "133N00000N"
    VALUE_133_NN1002_N = "133NN1002N"


class NutritionistProviderCodes(Enum):
    """
    specDomain: S20341 (C-0-T19465-S20334-S20341-cpt)
    :cvar VALUE_133_N00000_X:
    :cvar VALUE_133_NN1002_X:
    """
    VALUE_133_N00000_X = "133N00000X"
    VALUE_133_NN1002_X = "133NN1002X"


class ObservationAlert(Enum):
    """
    specDomain: S16664 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S16664-cpt)
    :cvar OBSA:
    :cvar AGE:
    :cvar COND:
    :cvar GEND:
    :cvar GEN:
    :cvar LAB:
    :cvar REACT:
    :cvar RREACT:
    :cvar CREACT:
    """
    OBSA = "OBSA"
    AGE = "AGE"
    COND = "COND"
    GEND = "GEND"
    GEN = "GEN"
    LAB = "LAB"
    REACT = "REACT"
    RREACT = "RREACT"
    CREACT = "CREACT"


class ObservationAllergyType(Enum):
    """
    specDomain: S21499 (C-0-T13953-A19820-A16226-S21498-S21499-cpt)
    :cvar ALG:
    :cvar DALG:
    :cvar EALG:
    :cvar FALG:
    """
    ALG = "ALG"
    DALG = "DALG"
    EALG = "EALG"
    FALG = "FALG"


class ObservationAssetValue(Enum):
    """
    specDomain: S22316 (C-0-T16614-A19918-A19924-S22316-cpt)
    :cvar ASSET:
    :cvar ANNUITY:
    :cvar PROP:
    :cvar RETACCT:
    :cvar TRUST:
    """
    ASSET = "ASSET"
    ANNUITY = "ANNUITY"
    PROP = "PROP"
    RETACCT = "RETACCT"
    TRUST = "TRUST"


class ObservationDetectedIssueCode(Enum):
    """
    specDomain: S16664 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-cpt)
    :cvar AGE:
    :cvar DOSEHINDA:
    :cvar DOSELINDA:
    :cvar DOSEHINDSA:
    :cvar DOSELINDSA:
    :cvar DOSEHINDW:
    :cvar DOSELINDW:
    :cvar COND:
    :cvar LACT:
    :cvar PREG:
    :cvar REACT:
    :cvar ALGY:
    :cvar INT_VALUE:
    :cvar RREACT:
    :cvar RALG:
    :cvar RINT:
    :cvar RAR:
    :cvar OBSA:
    :cvar GEND:
    :cvar GEN:
    :cvar LAB:
    :cvar CREACT:
    """
    AGE = "AGE"
    DOSEHINDA = "DOSEHINDA"
    DOSELINDA = "DOSELINDA"
    DOSEHINDSA = "DOSEHINDSA"
    DOSELINDSA = "DOSELINDSA"
    DOSEHINDW = "DOSEHINDW"
    DOSELINDW = "DOSELINDW"
    COND = "COND"
    LACT = "LACT"
    PREG = "PREG"
    REACT = "REACT"
    ALGY = "ALGY"
    INT_VALUE = "INT"
    RREACT = "RREACT"
    RALG = "RALG"
    RINT = "RINT"
    RAR = "RAR"
    OBSA = "OBSA"
    GEND = "GEND"
    GEN = "GEN"
    LAB = "LAB"
    CREACT = "CREACT"


class ObservationDiagnosisTypes(Enum):
    """
    specDomain: S20927 (C-0-T13953-A19820-A16226-S20927-cpt)
    :cvar DX:
    :cvar ADMDX:
    :cvar DISDX:
    :cvar INTDX:
    :cvar NOI:
    """
    DX = "DX"
    ADMDX = "ADMDX"
    DISDX = "DISDX"
    INTDX = "INTDX"
    NOI = "NOI"


class ObservationDrugIntoleranceType(Enum):
    """
    specDomain: S21501 (C-0-T13953-A19820-A16226-S21498-S21501-cpt)
    :cvar DINT:
    :cvar DALG:
    :cvar DNAINT:
    """
    DINT = "DINT"
    DALG = "DALG"
    DNAINT = "DNAINT"


class ObservationEligibilityIndicatorValue(Enum):
    """
    specDomain: S22295 (C-0-T16614-A19918-S22295-cpt)
    :cvar ELSTAT:
    :cvar ADOPT:
    :cvar BTHCERT:
    :cvar CCOC:
    :cvar DRLIC:
    :cvar FOSTER:
    :cvar MRGCERT:
    :cvar MIL:
    :cvar PASSPORT:
    :cvar MEMBER:
    :cvar STUDENRL:
    """
    ELSTAT = "ELSTAT"
    ADOPT = "ADOPT"
    BTHCERT = "BTHCERT"
    CCOC = "CCOC"
    DRLIC = "DRLIC"
    FOSTER = "FOSTER"
    MRGCERT = "MRGCERT"
    MIL = "MIL"
    PASSPORT = "PASSPORT"
    MEMBER = "MEMBER"
    STUDENRL = "STUDENRL"


class ObservationEnvironmentalIntoleranceType(Enum):
    """
    specDomain: S21503 (C-0-T13953-A19820-A16226-S21498-S21503-cpt)
    :cvar EINT:
    :cvar EALG:
    :cvar ENAINT:
    """
    EINT = "EINT"
    EALG = "EALG"
    ENAINT = "ENAINT"


class ObservationFoodIntoleranceType(Enum):
    """
    specDomain: S21502 (C-0-T13953-A19820-A16226-S21498-S21502-cpt)
    :cvar FINT:
    :cvar FALG:
    :cvar FNAINT:
    """
    FINT = "FINT"
    FALG = "FALG"
    FNAINT = "FNAINT"


class ObservationHealthStatusValue(Enum):
    """
    specDomain: S22290 (C-0-T16614-A19918-S22290-cpt)
    :cvar HLSTAT:
    :cvar IVDRG:
    :cvar DISABLE:
    :cvar DRUG:
    :cvar PGNT:
    """
    HLSTAT = "HLSTAT"
    IVDRG = "IVDRG"
    DISABLE = "DISABLE"
    DRUG = "DRUG"
    PGNT = "PGNT"


class ObservationIncomeValue(Enum):
    """
    specDomain: S22307 (C-0-T16614-A19918-A19924-S22307-cpt)
    :cvar INCOME:
    :cvar CHILD:
    :cvar DISABL:
    :cvar SUPPLE:
    :cvar INVEST:
    :cvar PAY:
    :cvar RETIRE:
    :cvar SPOUSAL:
    :cvar TAX:
    """
    INCOME = "INCOME"
    CHILD = "CHILD"
    DISABL = "DISABL"
    SUPPLE = "SUPPLE"
    INVEST = "INVEST"
    PAY = "PAY"
    RETIRE = "RETIRE"
    SPOUSAL = "SPOUSAL"
    TAX = "TAX"


class ObservationInterpretationChange(Enum):
    """
    abstDomain: A10214 (C-0-T78-A10214-cpt)
    :cvar B:
    :cvar D:
    :cvar U:
    :cvar W:
    """
    B = "B"
    D = "D"
    U = "U"
    W = "W"


class ObservationInterpretationExceptions(Enum):
    """
    abstDomain: A10225 (C-0-T78-A10225-cpt)
    :cvar VALUE:
    :cvar VALUE_1:
    """
    VALUE = "&gt;"
    VALUE_1 = "&lt;"


class ObservationInterpretationNormality(Enum):
    """
    abstDomain: A10206 (C-0-T78-A10206-cpt)
    :cvar AA:
    :cvar HH:
    :cvar LL:
    :cvar H:
    :cvar L:
    :cvar A:
    :cvar N:
    """
    AA = "AA"
    HH = "HH"
    LL = "LL"
    H = "H"
    L = "L"
    A = "A"
    N = "N"


class ObservationInterpretationNormalityAbnormal(Enum):
    """
    specDomain: S10208 (C-0-T78-A10206-S10208-cpt)
    :cvar AA:
    :cvar HH:
    :cvar LL:
    :cvar H:
    :cvar L:
    :cvar A:
    """
    AA = "AA"
    HH = "HH"
    LL = "LL"
    H = "H"
    L = "L"
    A = "A"


class ObservationInterpretationNormalityAlert(Enum):
    """
    specDomain: S10211 (C-0-T78-A10206-S10208-S10211-cpt)
    :cvar AA:
    :cvar HH:
    :cvar LL:
    """
    AA = "AA"
    HH = "HH"
    LL = "LL"


class ObservationInterpretationNormalityHigh(Enum):
    """
    specDomain: S10210 (C-0-T78-A10206-S10208-S10210-cpt)
    :cvar H:
    :cvar HH:
    """
    H = "H"
    HH = "HH"


class ObservationInterpretationNormalityLow(Enum):
    """
    specDomain: S10209 (C-0-T78-A10206-S10208-S10209-cpt)
    :cvar L:
    :cvar LL:
    """
    L = "L"
    LL = "LL"


class ObservationInterpretationOustsideThreshold(Enum):
    """
    specDomain: S21634 (C-0-T78-A19759-S21634-cpt)
    :cvar EX:
    :cvar HX:
    :cvar LX:
    """
    EX = "EX"
    HX = "HX"
    LX = "LX"


class ObservationInterpretationSusceptibility(Enum):
    """
    abstDomain: A10219 (C-0-T78-A10219-cpt)
    :cvar I:
    :cvar MS:
    :cvar R:
    :cvar S:
    :cvar VS:
    """
    I = "I"
    MS = "MS"
    R = "R"
    S = "S"
    VS = "VS"


class ObservationIntoleranceType(Enum):
    """
    specDomain: S21498 (C-0-T13953-A19820-A16226-S21498-cpt)
    :cvar ALG:
    :cvar DALG:
    :cvar EALG:
    :cvar FALG:
    :cvar DINT:
    :cvar DNAINT:
    :cvar EINT:
    :cvar ENAINT:
    :cvar FINT:
    :cvar FNAINT:
    :cvar NAINT:
    :cvar OINT:
    """
    ALG = "ALG"
    DALG = "DALG"
    EALG = "EALG"
    FALG = "FALG"
    DINT = "DINT"
    DNAINT = "DNAINT"
    EINT = "EINT"
    ENAINT = "ENAINT"
    FINT = "FINT"
    FNAINT = "FNAINT"
    NAINT = "NAINT"
    OINT = "OINT"


class ObservationLivingDependencyValue(Enum):
    """
    specDomain: S22286 (C-0-T16614-A19918-S22286-cpt)
    :cvar LIVDEP:
    :cvar RELDEP:
    :cvar SPSDEP:
    :cvar URELDEP:
    """
    LIVDEP = "LIVDEP"
    RELDEP = "RELDEP"
    SPSDEP = "SPSDEP"
    URELDEP = "URELDEP"


class ObservationLivingExpenseValue(Enum):
    """
    specDomain: S22321 (C-0-T16614-A19918-A19924-S22321-cpt)
    :cvar LIVEXP:
    :cvar CLOTH:
    :cvar FOOD:
    :cvar HEALTH:
    :cvar HOUSE:
    :cvar LEGAL:
    :cvar MORTG:
    :cvar RENT:
    :cvar SUNDRY:
    :cvar TRANS:
    :cvar UTIL:
    """
    LIVEXP = "LIVEXP"
    CLOTH = "CLOTH"
    FOOD = "FOOD"
    HEALTH = "HEALTH"
    HOUSE = "HOUSE"
    LEGAL = "LEGAL"
    MORTG = "MORTG"
    RENT = "RENT"
    SUNDRY = "SUNDRY"
    TRANS = "TRANS"
    UTIL = "UTIL"


class ObservationLivingSituationValue(Enum):
    """
    specDomain: S22277 (C-0-T16614-A19918-S22277-cpt)
    :cvar LIVSIT:
    :cvar ALONE:
    :cvar DEPCHD:
    :cvar DEPSPS:
    :cvar DEPYGCHD:
    :cvar FAM:
    :cvar RELAT:
    :cvar SPS:
    :cvar UNREL:
    """
    LIVSIT = "LIVSIT"
    ALONE = "ALONE"
    DEPCHD = "DEPCHD"
    DEPSPS = "DEPSPS"
    DEPYGCHD = "DEPYGCHD"
    FAM = "FAM"
    RELAT = "RELAT"
    SPS = "SPS"
    UNREL = "UNREL"


class ObservationNonAllergyIntoleranceType(Enum):
    """
    specDomain: S21500 (C-0-T13953-A19820-A16226-S21498-S21500-cpt)
    :cvar NAINT:
    :cvar DNAINT:
    :cvar ENAINT:
    :cvar FNAINT:
    """
    NAINT = "NAINT"
    DNAINT = "DNAINT"
    ENAINT = "ENAINT"
    FNAINT = "FNAINT"


class ObservationSocioEconomicStatusValue(Enum):
    """
    specDomain: S22269 (C-0-T16614-A19918-S22269-cpt)
    :cvar SOECSTAT:
    :cvar ABUSE:
    :cvar HMLESS:
    :cvar ILGIM:
    :cvar INCAR:
    :cvar PROB:
    :cvar REFUG:
    :cvar UNEMPL:
    """
    SOECSTAT = "SOECSTAT"
    ABUSE = "ABUSE"
    HMLESS = "HMLESS"
    ILGIM = "ILGIM"
    INCAR = "INCAR"
    PROB = "PROB"
    REFUG = "REFUG"
    UNEMPL = "UNEMPL"


class ObsoleteEditStatus(Enum):
    """
    specDomain: S11045 (C-0-T11040-S11045-cpt)
    :cvar O:
    """
    O = "O"


class ObstetricsGynecologyProviderCodes(Enum):
    """
    specDomain: S20163 (C-0-T19465-S20096-S20163-cpt)
    :cvar VALUE_207_V00000_X:
    :cvar VALUE_207_VC0200_X:
    :cvar VALUE_207_VX0201_X:
    :cvar VALUE_207_VG0400_X:
    :cvar VALUE_207_VM0101_X:
    :cvar VALUE_207_VX0000_X:
    :cvar VALUE_207_VE0102_X:
    """
    VALUE_207_V00000_X = "207V00000X"
    VALUE_207_VC0200_X = "207VC0200X"
    VALUE_207_VX0201_X = "207VX0201X"
    VALUE_207_VG0400_X = "207VG0400X"
    VALUE_207_VM0101_X = "207VM0101X"
    VALUE_207_VX0000_X = "207VX0000X"
    VALUE_207_VE0102_X = "207VE0102X"


class OccupationalTherapistHipaa(Enum):
    """
    specDomain: S13598 (C-0-T13129-A13130-A13592-S13598-cpt)
    :cvar VALUE_225_X00000_N:
    :cvar VALUE_225_XC0400_N:
    :cvar VALUE_225_XE1200_N:
    :cvar VALUE_225_XH1200_N:
    :cvar VALUE_225_XH1300_N:
    :cvar VALUE_225_XN1300_N:
    :cvar VALUE_225_XP0200_N:
    :cvar VALUE_225_XR0403_N:
    """
    VALUE_225_X00000_N = "225X00000N"
    VALUE_225_XC0400_N = "225XC0400N"
    VALUE_225_XE1200_N = "225XE1200N"
    VALUE_225_XH1200_N = "225XH1200N"
    VALUE_225_XH1300_N = "225XH1300N"
    VALUE_225_XN1300_N = "225XN1300N"
    VALUE_225_XP0200_N = "225XP0200N"
    VALUE_225_XR0403_N = "225XR0403N"


class OccupationalTherapistProviderCodes(Enum):
    """
    specDomain: S20538 (C-0-T19465-S20532-S20538-cpt)
    :cvar VALUE_225_X00000_X:
    :cvar VALUE_225_XE1200_X:
    :cvar VALUE_225_XH1200_X:
    :cvar VALUE_225_XH1300_X:
    :cvar VALUE_225_XN1300_X:
    :cvar VALUE_225_XP0200_X:
    :cvar VALUE_225_XR0403_X:
    """
    VALUE_225_X00000_X = "225X00000X"
    VALUE_225_XE1200_X = "225XE1200X"
    VALUE_225_XH1200_X = "225XH1200X"
    VALUE_225_XH1300_X = "225XH1300X"
    VALUE_225_XN1300_X = "225XN1300X"
    VALUE_225_XP0200_X = "225XP0200X"
    VALUE_225_XR0403_X = "225XR0403X"


class OilDrugForm(Enum):
    """
    specDomain: S14417 (C-0-T19651-A14411-A14412-A14413-S14417-cpt)
    :cvar OIL:
    :cvar TOPOIL:
    """
    OIL = "OIL"
    TOPOIL = "TOPOIL"


class OintmentDrugForm(Enum):
    """
    specDomain: S14475 (C-0-T19651-A14411-A14412-A14463-S14475-cpt)
    :cvar VAGOINT:
    :cvar VAGOINTAPL:
    :cvar OINT:
    :cvar NASOINT:
    :cvar OINTAPL:
    :cvar OPOINT:
    :cvar OTOINT:
    :cvar RECOINT:
    :cvar TOPOINT:
    """
    VAGOINT = "VAGOINT"
    VAGOINTAPL = "VAGOINTAPL"
    OINT = "OINT"
    NASOINT = "NASOINT"
    OINTAPL = "OINTAPL"
    OPOINT = "OPOINT"
    OTOINT = "OTOINT"
    RECOINT = "RECOINT"
    TOPOINT = "TOPOINT"


class Ojibwayan(Enum):
    """
    abstDomain: A18156 (C-0-T18130-A18131-A18132-A18156-cpt)
    :cvar X_POT:
    :cvar X_OJB:
    """
    X_POT = "x-POT"
    X_OJB = "x-OJB"


class OphthalmicRoute(Enum):
    """
    abstDomain: A17264 (C-0-T14581-A17021-A17264-cpt)
    :cvar OPTHALTA:
    """
    OPTHALTA = "OPTHALTA"


class OptometristHipaa(Enum):
    """
    specDomain: S13212 (C-0-T13129-A13130-A13211-S13212-cpt)
    :cvar VALUE_152_W00000_N:
    :cvar VALUE_152_WC0800_N:
    :cvar VALUE_152_WL0500_N:
    :cvar VALUE_152_WX0102_N:
    :cvar VALUE_152_WP0200_N:
    :cvar VALUE_152_WS0006_N:
    :cvar VALUE_152_WV0400_N:
    """
    VALUE_152_W00000_N = "152W00000N"
    VALUE_152_WC0800_N = "152WC0800N"
    VALUE_152_WL0500_N = "152WL0500N"
    VALUE_152_WX0102_N = "152WX0102N"
    VALUE_152_WP0200_N = "152WP0200N"
    VALUE_152_WS0006_N = "152WS0006N"
    VALUE_152_WV0400_N = "152WV0400N"


class OptometristProviderCodes(Enum):
    """
    specDomain: S20349 (C-0-T19465-S20348-S20349-cpt)
    :cvar VALUE_152_W00000_X:
    :cvar VALUE_152_WC0802_X:
    :cvar VALUE_152_WL0500_X:
    :cvar VALUE_152_WX0102_X:
    :cvar VALUE_152_WP0200_X:
    :cvar VALUE_152_WS0006_X:
    :cvar VALUE_152_WV0400_X:
    """
    VALUE_152_W00000_X = "152W00000X"
    VALUE_152_WC0802_X = "152WC0802X"
    VALUE_152_WL0500_X = "152WL0500X"
    VALUE_152_WX0102_X = "152WX0102X"
    VALUE_152_WP0200_X = "152WP0200X"
    VALUE_152_WS0006_X = "152WS0006X"
    VALUE_152_WV0400_X = "152WV0400X"


class OralCapsule(Enum):
    """
    specDomain: S14508 (C-0-T19651-A14411-A14412-A14484-S14506-S14507-S14508-cpt)
    :cvar ENTCAP:
    :cvar ERENTCAP:
    :cvar ERCAP:
    :cvar ERCAP12:
    :cvar ERCAP24:
    :cvar ERECCAP:
    :cvar ORCAP:
    """
    ENTCAP = "ENTCAP"
    ERENTCAP = "ERENTCAP"
    ERCAP = "ERCAP"
    ERCAP12 = "ERCAP12"
    ERCAP24 = "ERCAP24"
    ERECCAP = "ERECCAP"
    ORCAP = "ORCAP"


class OralInhalation(Enum):
    """
    specDomain: S14622 (C-0-T14581-A17021-A17319-S14622-cpt)
    :cvar ORINHL:
    :cvar ORIFINHL:
    :cvar REBREATH:
    """
    ORINHL = "ORINHL"
    ORIFINHL = "ORIFINHL"
    REBREATH = "REBREATH"


class OralRoute(Enum):
    """
    abstDomain: A17266 (C-0-T14581-A17021-A17266-cpt)
    :cvar ORINHL:
    :cvar ORIFINHL:
    :cvar REBREATH:
    :cvar CHEW:
    :cvar DISSOLVE:
    :cvar ORRINSE:
    :cvar PO:
    :cvar ORALTA:
    """
    ORINHL = "ORINHL"
    ORIFINHL = "ORIFINHL"
    REBREATH = "REBREATH"
    CHEW = "CHEW"
    DISSOLVE = "DISSOLVE"
    ORRINSE = "ORRINSE"
    PO = "PO"
    ORALTA = "ORALTA"


class OralSolution(Enum):
    """
    specDomain: S14431 (C-0-T19651-A14411-A14412-A14413-S14419-S14431-cpt)
    :cvar ORALSOL:
    :cvar ELIXIR:
    :cvar RINSE:
    :cvar ORDROP:
    :cvar SYRUP:
    """
    ORALSOL = "ORALSOL"
    ELIXIR = "ELIXIR"
    RINSE = "RINSE"
    ORDROP = "ORDROP"
    SYRUP = "SYRUP"


class OralSuspension(Enum):
    """
    specDomain: S14457 (C-0-T19651-A14411-A14412-A14441-S14454-S14457-cpt)
    :cvar ERSUSP:
    :cvar ERSUSP12:
    :cvar ERSUSP24:
    :cvar ORSUSP:
    """
    ERSUSP = "ERSUSP"
    ERSUSP12 = "ERSUSP12"
    ERSUSP24 = "ERSUSP24"
    ORSUSP = "ORSUSP"


class OralTablet(Enum):
    """
    specDomain: S14516 (C-0-T19651-A14411-A14412-A14484-S14506-S14515-S14516-cpt)
    :cvar BUCTAB:
    :cvar SRBUCTAB:
    :cvar ECTAB:
    :cvar ERECTAB:
    :cvar ERTAB:
    :cvar ERTAB12:
    :cvar ERTAB24:
    :cvar ORTAB:
    :cvar CAPLET:
    :cvar CHEWTAB:
    :cvar CPTAB:
    :cvar DRTAB:
    :cvar DISINTAB:
    :cvar ORTROCHE:
    :cvar SLTAB:
    """
    BUCTAB = "BUCTAB"
    SRBUCTAB = "SRBUCTAB"
    ECTAB = "ECTAB"
    ERECTAB = "ERECTAB"
    ERTAB = "ERTAB"
    ERTAB12 = "ERTAB12"
    ERTAB24 = "ERTAB24"
    ORTAB = "ORTAB"
    CAPLET = "CAPLET"
    CHEWTAB = "CHEWTAB"
    CPTAB = "CPTAB"
    DRTAB = "DRTAB"
    DISINTAB = "DISINTAB"
    ORTROCHE = "ORTROCHE"
    SLTAB = "SLTAB"


class OrderedListStyle(Enum):
    """
    abstDomain: A19606 (C-0-T19602-A19605-A19606-cpt)
    :cvar ARABIC:
    :cvar BIG_ALPHA:
    :cvar BIG_ROMAN:
    :cvar LITTLE_ALPHA:
    :cvar LITTLE_ROMAN:
    """
    ARABIC = "Arabic"
    BIG_ALPHA = "BigAlpha"
    BIG_ROMAN = "BigRoman"
    LITTLE_ALPHA = "LittleAlpha"
    LITTLE_ROMAN = "LittleRoman"


class OregonAthapaskan(Enum):
    """
    abstDomain: A18387 (C-0-T18130-A18352-A18356-A18358-A18386-A18387-cpt)
    :cvar X_TOL:
    :cvar X_TUU:
    """
    X_TOL = "x-TOL"
    X_TUU = "x-TUU"


class OrganizationNamePartQualifier(Enum):
    """
    abstDomain: A15889 (C-0-T15888-A15889-cpt)
    :cvar LS:
    """
    LS = "LS"


class OrganizationNameType(Enum):
    """
    vocSet: T204 (C-0-T204-cpt)
    :cvar A:
    :cvar L:
    :cvar ST:
    """
    A = "A"
    L = "L"
    ST = "ST"


class OrganizationNameUse(Enum):
    """
    abstDomain: A15914 (C-0-T15913-A15914-cpt)
    :cvar SRCH:
    :cvar SNDX:
    :cvar PHON:
    :cvar ABC:
    :cvar IDE:
    :cvar SYL:
    :cvar L:
    :cvar OR_VALUE:
    :cvar C:
    """
    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    L = "L"
    OR_VALUE = "OR"
    C = "C"


class OrganizationNameUseLegalByBot(Enum):
    """
    specDomain: S10176 (C-0-T15913-A15914-S10176-cpt)
    :cvar L:
    :cvar OR_VALUE:
    """
    L = "L"
    OR_VALUE = "OR"


class OromucosalRoute(Enum):
    """
    abstDomain: A17276 (C-0-T14581-A17021-A17276-cpt)
    :cvar GARGLE:
    :cvar SUCK:
    :cvar SWISHSPIT:
    :cvar SWISHSWAL:
    :cvar ORMUC:
    """
    GARGLE = "GARGLE"
    SUCK = "SUCK"
    SWISHSPIT = "SWISHSPIT"
    SWISHSWAL = "SWISHSWAL"
    ORMUC = "ORMUC"


class OropharyngealRoute(Enum):
    """
    abstDomain: A17282 (C-0-T14581-A17021-A17282-cpt)
    :cvar OROPHARTA:
    """
    OROPHARTA = "OROPHARTA"


class OrthoClinPracticeSetting(Enum):
    """
    specDomain: S10949 (C-0-T12206-A17660-A19450-A10588-S10589-S10949-cpt)
    :cvar ORTHO:
    :cvar HAND:
    """
    ORTHO = "ORTHO"
    HAND = "HAND"


class OrthopaedicSurgeryProviderCodes(Enum):
    """
    specDomain: S20172 (C-0-T19465-S20096-S20172-cpt)
    :cvar VALUE_207_X00000_X:
    :cvar VALUE_207_XS0114_X:
    :cvar VALUE_207_XX0004_X:
    :cvar VALUE_207_XS0106_X:
    :cvar VALUE_207_XS0117_X:
    :cvar VALUE_207_XX0801_X:
    :cvar VALUE_207_XX0005_X:
    """
    VALUE_207_X00000_X = "207X00000X"
    VALUE_207_XS0114_X = "207XS0114X"
    VALUE_207_XX0004_X = "207XX0004X"
    VALUE_207_XS0106_X = "207XS0106X"
    VALUE_207_XS0117_X = "207XS0117X"
    VALUE_207_XX0801_X = "207XX0801X"
    VALUE_207_XX0005_X = "207XX0005X"


class Other(Enum):
    """
    specDomain: S10616 (C-0-T10609-S10610-S10616-cpt)
    :cvar OTH:
    :cvar NINF:
    :cvar PINF:
    """
    OTH = "OTH"
    NINF = "NINF"
    PINF = "PINF"


class OtherActionTakenManagementCode(Enum):
    """
    specDomain: S16703 (C-0-T13953-A13954-A16695-S16703-cpt)
    :cvar VALUE_8:
    :cvar VALUE_11:
    :cvar VALUE_9:
    :cvar VALUE_10:
    :cvar VALUE_13:
    :cvar VALUE_12:
    """
    VALUE_8 = "8"
    VALUE_11 = "11"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_13 = "13"
    VALUE_12 = "12"


class OtherIndicationValue(Enum):
    """
    abstDomain: A19731 (C-0-T16614-A19729-A19731-cpt)
    :cvar DIAGNOSIS_VALUE:
    :cvar INDICATION_VALUE:
    :cvar SYMPTOM_VALUE:
    """
    DIAGNOSIS_VALUE = "_DiagnosisValue"
    INDICATION_VALUE = "_IndicationValue"
    SYMPTOM_VALUE = "_SymptomValue"


class OtherPhysicianOsteopathHipaa(Enum):
    """
    abstDomain: A13579 (C-0-T13129-A13130-A13578-A13579-cpt)
    :cvar VALUE_353_BL0002_N:
    :cvar VALUE_353_BS0900_N:
    """
    VALUE_353_BL0002_N = "353BL0002N"
    VALUE_353_BS0900_N = "353BS0900N"


class OtherServiceProviderContractorHipaa(Enum):
    """
    abstDomain: A13139 (C-0-T13129-A13130-A13136-A13139-cpt)
    :cvar VALUE_171_WH0202_N:
    """
    VALUE_171_WH0202_N = "171WH0202N"


class OtherServiceProviderHipaa(Enum):
    """
    abstDomain: A13136 (C-0-T13129-A13130-A13136-cpt)
    :cvar VALUE_171_WH0202_N:
    :cvar VALUE_1744_G0900_N:
    :cvar VALUE_1744_P3200_N:
    :cvar VALUE_1744_R1103_N:
    :cvar VALUE_1744_R1102_N:
    :cvar VALUE_174_MM1900_N:
    :cvar VALUE_171100000_N:
    :cvar VALUE_172_A00000_N:
    :cvar VALUE_176_P00000_N:
    :cvar VALUE_175_L00000_N:
    :cvar VALUE_173000000_N:
    :cvar VALUE_175_M00000_N:
    :cvar VALUE_175_F00000_N:
    """
    VALUE_171_WH0202_N = "171WH0202N"
    VALUE_1744_G0900_N = "1744G0900N"
    VALUE_1744_P3200_N = "1744P3200N"
    VALUE_1744_R1103_N = "1744R1103N"
    VALUE_1744_R1102_N = "1744R1102N"
    VALUE_174_MM1900_N = "174MM1900N"
    VALUE_171100000_N = "171100000N"
    VALUE_172_A00000_N = "172A00000N"
    VALUE_176_P00000_N = "176P00000N"
    VALUE_175_L00000_N = "175L00000N"
    VALUE_173000000_N = "173000000N"
    VALUE_175_M00000_N = "175M00000N"
    VALUE_175_F00000_N = "175F00000N"


class OtherServiceProviderSpecialistHipaa(Enum):
    """
    abstDomain: A13347 (C-0-T13129-A13130-A13136-A13347-cpt)
    :cvar VALUE_1744_G0900_N:
    :cvar VALUE_1744_P3200_N:
    :cvar VALUE_1744_R1103_N:
    :cvar VALUE_1744_R1102_N:
    """
    VALUE_1744_G0900_N = "1744G0900N"
    VALUE_1744_P3200_N = "1744P3200N"
    VALUE_1744_R1103_N = "1744R1103N"
    VALUE_1744_R1102_N = "1744R1102N"


class OtherServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20434 (C-0-T19465-S20434-cpt)
    :cvar VALUE_171_W00000_X:
    :cvar VALUE_171_WH0202_X:
    :cvar VALUE_171_WV0202_X:
    :cvar VALUE_174_M00000_X:
    :cvar VALUE_174_MM1900_X:
    :cvar VALUE_174400000_X:
    :cvar VALUE_1744_G0900_X:
    :cvar VALUE_1744_P3200_X:
    :cvar VALUE_1744_R1103_X:
    :cvar VALUE_1744_R1102_X:
    :cvar VALUE_170000000_X:
    :cvar VALUE_171100000_X:
    :cvar VALUE_172_A00000_X:
    :cvar VALUE_176_P00000_X:
    :cvar VALUE_175_L00000_X:
    :cvar VALUE_173000000_X:
    :cvar VALUE_177_F00000_X:
    :cvar VALUE_176_B00000_X:
    :cvar VALUE_175_M00000_X:
    :cvar VALUE_175_F00000_X:
    :cvar VALUE_170100000_X:
    """
    VALUE_171_W00000_X = "171W00000X"
    VALUE_171_WH0202_X = "171WH0202X"
    VALUE_171_WV0202_X = "171WV0202X"
    VALUE_174_M00000_X = "174M00000X"
    VALUE_174_MM1900_X = "174MM1900X"
    VALUE_174400000_X = "174400000X"
    VALUE_1744_G0900_X = "1744G0900X"
    VALUE_1744_P3200_X = "1744P3200X"
    VALUE_1744_R1103_X = "1744R1103X"
    VALUE_1744_R1102_X = "1744R1102X"
    VALUE_170000000_X = "170000000X"
    VALUE_171100000_X = "171100000X"
    VALUE_172_A00000_X = "172A00000X"
    VALUE_176_P00000_X = "176P00000X"
    VALUE_175_L00000_X = "175L00000X"
    VALUE_173000000_X = "173000000X"
    VALUE_177_F00000_X = "177F00000X"
    VALUE_176_B00000_X = "176B00000X"
    VALUE_175_M00000_X = "175M00000X"
    VALUE_175_F00000_X = "175F00000X"
    VALUE_170100000_X = "170100000X"


class OtherTechnologistOrTechnicianHipaa(Enum):
    """
    abstDomain: A13673 (C-0-T13129-A13130-A13644-A13673-cpt)
    :cvar VALUE_246_ZA2600_N:
    :cvar VALUE_246_ZB0500_N:
    :cvar VALUE_246_ZB0301_N:
    :cvar VALUE_246_ZB0302_N:
    :cvar VALUE_246_ZB0600_N:
    :cvar VALUE_246_ZE0500_N:
    :cvar VALUE_246_ZE0600_N:
    :cvar VALUE_246_ZF0200_N:
    :cvar VALUE_246_ZG1000_N:
    :cvar VALUE_246_ZG0701_N:
    :cvar VALUE_246_ZI1000_N:
    :cvar VALUE_246_ZN0300_N:
    :cvar VALUE_246_ZS0400_N:
    :cvar VALUE_246_ZV0500_N:
    """
    VALUE_246_ZA2600_N = "246ZA2600N"
    VALUE_246_ZB0500_N = "246ZB0500N"
    VALUE_246_ZB0301_N = "246ZB0301N"
    VALUE_246_ZB0302_N = "246ZB0302N"
    VALUE_246_ZB0600_N = "246ZB0600N"
    VALUE_246_ZE0500_N = "246ZE0500N"
    VALUE_246_ZE0600_N = "246ZE0600N"
    VALUE_246_ZF0200_N = "246ZF0200N"
    VALUE_246_ZG1000_N = "246ZG1000N"
    VALUE_246_ZG0701_N = "246ZG0701N"
    VALUE_246_ZI1000_N = "246ZI1000N"
    VALUE_246_ZN0300_N = "246ZN0300N"
    VALUE_246_ZS0400_N = "246ZS0400N"
    VALUE_246_ZV0500_N = "246ZV0500N"


class OtherTechnologistOrTechnicianProviderHipaa(Enum):
    """
    abstDomain: A13705 (C-0-T13129-A13130-A13644-A13705-cpt)
    :cvar VALUE_2472_B0301_N:
    :cvar VALUE_2472_D0500_N:
    :cvar VALUE_2472_E0500_N:
    :cvar VALUE_2472_R0900_N:
    :cvar VALUE_2472_V0600_N:
    """
    VALUE_2472_B0301_N = "2472B0301N"
    VALUE_2472_D0500_N = "2472D0500N"
    VALUE_2472_E0500_N = "2472E0500N"
    VALUE_2472_R0900_N = "2472R0900N"
    VALUE_2472_V0600_N = "2472V0600N"


class OticRoute(Enum):
    """
    abstDomain: A17284 (C-0-T14581-A17021-A17284-cpt)
    :cvar OT:
    """
    OT = "OT"


class OtolaryngologyProviderCodes(Enum):
    """
    specDomain: S20179 (C-0-T19465-S20096-S20179-cpt)
    :cvar VALUE_207_Y00000_X:
    :cvar VALUE_207_YS0123_X:
    :cvar VALUE_207_YX0602_X:
    :cvar VALUE_207_YX0905_X:
    :cvar VALUE_207_YX0901_X:
    :cvar VALUE_207_YP0228_X:
    :cvar VALUE_207_YX0007_X:
    """
    VALUE_207_Y00000_X = "207Y00000X"
    VALUE_207_YS0123_X = "207YS0123X"
    VALUE_207_YX0602_X = "207YX0602X"
    VALUE_207_YX0905_X = "207YX0905X"
    VALUE_207_YX0901_X = "207YX0901X"
    VALUE_207_YP0228_X = "207YP0228X"
    VALUE_207_YX0007_X = "207YX0007X"


class OutpatientFacilityPracticeSetting(Enum):
    """
    specDomain: S10589 (C-0-T12206-A17660-A19450-A10588-S10589-cpt)
    :cvar CARD:
    :cvar PEDCARD:
    :cvar ENDO:
    :cvar PEDE:
    :cvar GI:
    :cvar PEDGI:
    :cvar HEM:
    :cvar PEDHEM:
    :cvar INFD:
    :cvar PEDID:
    :cvar ONCL:
    :cvar PEDHO:
    :cvar NEPH:
    :cvar PEDNEPH:
    :cvar ORTHO:
    :cvar HAND:
    :cvar PEDC:
    :cvar PEDRHEUM:
    :cvar RHEUM:
    :cvar SU:
    :cvar PLS:
    :cvar URO:
    :cvar OF:
    :cvar ALL:
    :cvar AMPUT:
    :cvar BMTC:
    :cvar BREAST:
    :cvar CANC:
    :cvar CAPC:
    :cvar COAG:
    :cvar CRS:
    :cvar DERM:
    :cvar FMC:
    :cvar GIM:
    :cvar GYN:
    :cvar HTN:
    :cvar IEC:
    :cvar INV:
    :cvar LYMPH:
    :cvar MGEN:
    :cvar NEUR:
    :cvar OB:
    :cvar OPH:
    :cvar VALUE_261_QS0112_N:
    :cvar OMS:
    :cvar ENT:
    :cvar VALUE_261_QP3300_N:
    :cvar PAINCL:
    :cvar VALUE_261_QP1100_N:
    :cvar POD:
    :cvar PREV:
    :cvar VALUE_261_QP2300_N:
    :cvar PC:
    :cvar PROCTO:
    :cvar PROS:
    :cvar PROFF:
    :cvar PSY:
    :cvar PSI:
    :cvar SPMED:
    :cvar TR:
    :cvar TRAVEL:
    :cvar WND:
    """
    CARD = "CARD"
    PEDCARD = "PEDCARD"
    ENDO = "ENDO"
    PEDE = "PEDE"
    GI = "GI"
    PEDGI = "PEDGI"
    HEM = "HEM"
    PEDHEM = "PEDHEM"
    INFD = "INFD"
    PEDID = "PEDID"
    ONCL = "ONCL"
    PEDHO = "PEDHO"
    NEPH = "NEPH"
    PEDNEPH = "PEDNEPH"
    ORTHO = "ORTHO"
    HAND = "HAND"
    PEDC = "PEDC"
    PEDRHEUM = "PEDRHEUM"
    RHEUM = "RHEUM"
    SU = "SU"
    PLS = "PLS"
    URO = "URO"
    OF = "OF"
    ALL = "ALL"
    AMPUT = "AMPUT"
    BMTC = "BMTC"
    BREAST = "BREAST"
    CANC = "CANC"
    CAPC = "CAPC"
    COAG = "COAG"
    CRS = "CRS"
    DERM = "DERM"
    FMC = "FMC"
    GIM = "GIM"
    GYN = "GYN"
    HTN = "HTN"
    IEC = "IEC"
    INV = "INV"
    LYMPH = "LYMPH"
    MGEN = "MGEN"
    NEUR = "NEUR"
    OB = "OB"
    OPH = "OPH"
    VALUE_261_QS0112_N = "261QS0112N"
    OMS = "OMS"
    ENT = "ENT"
    VALUE_261_QP3300_N = "261QP3300N"
    PAINCL = "PAINCL"
    VALUE_261_QP1100_N = "261QP1100N"
    POD = "POD"
    PREV = "PREV"
    VALUE_261_QP2300_N = "261QP2300N"
    PC = "PC"
    PROCTO = "PROCTO"
    PROS = "PROS"
    PROFF = "PROFF"
    PSY = "PSY"
    PSI = "PSI"
    SPMED = "SPMED"
    TR = "TR"
    TRAVEL = "TRAVEL"
    WND = "WND"


class PadDrugForm(Enum):
    """
    specDomain: S14497 (C-0-T19651-A14411-A14412-A14484-S14497-cpt)
    :cvar PAD:
    :cvar MEDPAD:
    """
    PAD = "PAD"
    MEDPAD = "MEDPAD"


class Pai(Enum):
    """
    abstDomain: A18276 (C-0-T18130-A18241-A18274-A18275-A18276-cpt)
    :cvar X_YUF:
    """
    X_YUF = "x-YUF"


class PainMedicineProviderCodes(Enum):
    """
    specDomain: S20186 (C-0-T19465-S20096-S20186-cpt)
    :cvar VALUE_208_V00000_X:
    :cvar VALUE_208_VP0014_X:
    :cvar VALUE_208_VP0000_X:
    """
    VALUE_208_V00000_X = "208V00000X"
    VALUE_208_VP0014_X = "208VP0014X"
    VALUE_208_VP0000_X = "208VP0000X"


class Palaihnihan(Enum):
    """
    abstDomain: A18248 (C-0-T18130-A18241-A18248-cpt)
    :cvar X_ACH:
    :cvar X_ATW:
    """
    X_ACH = "x-ACH"
    X_ATW = "x-ATW"


class ParameterizedDataType(Enum):
    """
    vocSet: T10759 (C-0-T10759-cpt)
    :cvar BAG_T:
    :cvar LIST_T:
    :cvar EIVL_T:
    :cvar IVL_T:
    :cvar PIVL_T:
    :cvar SET_T:
    :cvar ANT_T:
    :cvar HXIT_T:
    :cvar NPPD_T:
    :cvar PPD_T:
    :cvar UVN_T:
    :cvar UVP_T:
    :cvar T:
    """
    BAG_T = "BAG&lt;T&gt;"
    LIST_T = "LIST&lt;T&gt;"
    EIVL_T = "EIVL&lt;T&gt;"
    IVL_T = "IVL&lt;T&gt;"
    PIVL_T = "PIVL&lt;T&gt;"
    SET_T = "SET&lt;T&gt;"
    ANT_T = "ANT&lt;T&gt;"
    HXIT_T = "HXIT&lt;T&gt;"
    NPPD_T = "NPPD&lt;T&gt;"
    PPD_T = "PPD&lt;T&gt;"
    UVN_T = "UVN&lt;T&gt;"
    UVP_T = "UVP&lt;T&gt;"
    T = "T"


class ParameterizedDataTypeAnnotated(Enum):
    """
    specDomain: S10767 (C-0-T10759-S10760-S10767-cpt)
    :cvar ANT_T:
    """
    ANT_T = "ANT&lt;T&gt;"


class ParameterizedDataTypeBag(Enum):
    """
    specDomain: S10763 (C-0-T10759-S10763-cpt)
    :cvar BAG_T:
    """
    BAG_T = "BAG&lt;T&gt;"


class ParameterizedDataTypeEventRelatedInterval(Enum):
    """
    specDomain: S10766 (C-0-T10759-S10761-S10766-cpt)
    :cvar EIVL_T:
    """
    EIVL_T = "EIVL&lt;T&gt;"


class ParameterizedDataTypeHistorical(Enum):
    """
    specDomain: S10768 (C-0-T10759-S10760-S10768-cpt)
    :cvar HXIT_T:
    """
    HXIT_T = "HXIT&lt;T&gt;"


class ParameterizedDataTypeInterval(Enum):
    """
    specDomain: S10764 (C-0-T10759-S10761-S10764-cpt)
    :cvar IVL_T:
    """
    IVL_T = "IVL&lt;T&gt;"


class ParameterizedDataTypeNonParametricProbabilityDistribution(Enum):
    """
    specDomain: S10771 (C-0-T10759-S10760-S10771-cpt)
    :cvar NPPD_T:
    """
    NPPD_T = "NPPD&lt;T&gt;"


class ParameterizedDataTypeParametricProbabilityDistribution(Enum):
    """
    specDomain: S10772 (C-0-T10759-S10760-S10772-cpt)
    :cvar PPD_T:
    """
    PPD_T = "PPD&lt;T&gt;"


class ParameterizedDataTypePeriodicInterval(Enum):
    """
    specDomain: S10765 (C-0-T10759-S10761-S10765-cpt)
    :cvar PIVL_T:
    """
    PIVL_T = "PIVL&lt;T&gt;"


class ParameterizedDataTypeSequence(Enum):
    """
    specDomain: S10762 (C-0-T10759-S10762-cpt)
    :cvar LIST_T:
    """
    LIST_T = "LIST&lt;T&gt;"


class ParameterizedDataTypeSet(Enum):
    """
    specDomain: S10761 (C-0-T10759-S10761-cpt)
    :cvar EIVL_T:
    :cvar IVL_T:
    :cvar PIVL_T:
    :cvar SET_T:
    """
    EIVL_T = "EIVL&lt;T&gt;"
    IVL_T = "IVL&lt;T&gt;"
    PIVL_T = "PIVL&lt;T&gt;"
    SET_T = "SET&lt;T&gt;"


class ParameterizedDataTypeType(Enum):
    """
    specDomain: S10760 (C-0-T10759-S10760-cpt)
    :cvar ANT_T:
    :cvar HXIT_T:
    :cvar NPPD_T:
    :cvar PPD_T:
    :cvar UVN_T:
    :cvar UVP_T:
    :cvar T:
    """
    ANT_T = "ANT&lt;T&gt;"
    HXIT_T = "HXIT&lt;T&gt;"
    NPPD_T = "NPPD&lt;T&gt;"
    PPD_T = "PPD&lt;T&gt;"
    UVN_T = "UVN&lt;T&gt;"
    UVP_T = "UVP&lt;T&gt;"
    T = "T"


class ParameterizedDataTypeUncertainValueNarrative(Enum):
    """
    specDomain: S10769 (C-0-T10759-S10760-S10769-cpt)
    :cvar UVN_T:
    """
    UVN_T = "UVN&lt;T&gt;"


class ParameterizedDataTypeUncertainValueProbabilistic(Enum):
    """
    specDomain: S10770 (C-0-T10759-S10760-S10770-cpt)
    :cvar UVP_T:
    """
    UVP_T = "UVP&lt;T&gt;"


class ParanasalSinusesRoute(Enum):
    """
    abstDomain: A17286 (C-0-T14581-A17021-A17286-cpt)
    :cvar PNSINJ:
    :cvar PNSINSTL:
    """
    PNSINJ = "PNSINJ"
    PNSINSTL = "PNSINSTL"


class Parent(Enum):
    """
    specDomain: S16346 (C-0-T12206-A19563-S17926-S16346-cpt)
    :cvar NFTH:
    :cvar NFTHF:
    :cvar NPRN:
    :cvar NMTH:
    :cvar PRNINLAW:
    :cvar FTHINLAW:
    :cvar MTHINLAW:
    :cvar STPPRN:
    :cvar STPFTH:
    :cvar STPMTH:
    :cvar PRN:
    :cvar FTH:
    :cvar MTH:
    """
    NFTH = "NFTH"
    NFTHF = "NFTHF"
    NPRN = "NPRN"
    NMTH = "NMTH"
    PRNINLAW = "PRNINLAW"
    FTHINLAW = "FTHINLAW"
    MTHINLAW = "MTHINLAW"
    STPPRN = "STPPRN"
    STPFTH = "STPFTH"
    STPMTH = "STPMTH"
    PRN = "PRN"
    FTH = "FTH"
    MTH = "MTH"


class ParentInLaw(Enum):
    """
    specDomain: S19770 (C-0-T12206-A19563-S17926-S16346-S19770-cpt)
    :cvar PRNINLAW:
    :cvar FTHINLAW:
    :cvar MTHINLAW:
    """
    PRNINLAW = "PRNINLAW"
    FTHINLAW = "FTHINLAW"
    MTHINLAW = "MTHINLAW"


class ParenteralRoute(Enum):
    """
    abstDomain: A17289 (C-0-T14581-A17021-A17289-cpt)
    :cvar PARENTINJ:
    """
    PARENTINJ = "PARENTINJ"


class PartialCompletionScale(Enum):
    """
    abstDomain: A18120 (C-0-T16614-A18120-cpt)
    :cvar G:
    :cvar LE:
    :cvar ME:
    :cvar MI:
    :cvar N:
    :cvar S:
    """
    G = "G"
    LE = "LE"
    ME = "ME"
    MI = "MI"
    N = "N"
    S = "S"


class ParticipationAncillary(Enum):
    """
    abstDomain: A10247 (C-0-T10901-S21573-A10247-cpt)
    :cvar ADM:
    :cvar ATND:
    :cvar CALLBCK:
    :cvar CON:
    :cvar DIS:
    :cvar ESC:
    :cvar REF:
    """
    ADM = "ADM"
    ATND = "ATND"
    CALLBCK = "CALLBCK"
    CON = "CON"
    DIS = "DIS"
    ESC = "ESC"
    REF = "REF"


class ParticipationExposureparticipation(Enum):
    """
    specDomain: S21978 (C-0-T10901-S21573-S10286-S21978-cpt)
    :cvar EXPART:
    :cvar EXSRC:
    :cvar EXPTRGT:
    """
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"


class ParticipationIndirectTarget(Enum):
    """
    specDomain: S19032 (C-0-T10901-S21573-S19032-cpt)
    :cvar IND:
    :cvar BEN:
    :cvar CAGNT:
    :cvar COV:
    :cvar GUAR:
    :cvar HLD:
    :cvar RCV:
    :cvar RCT:
    """
    IND = "IND"
    BEN = "BEN"
    CAGNT = "CAGNT"
    COV = "COV"
    GUAR = "GUAR"
    HLD = "HLD"
    RCV = "RCV"
    RCT = "RCT"


class ParticipationInformationGenerator(Enum):
    """
    abstDomain: A10251 (C-0-T10901-S21573-A10251-cpt)
    :cvar TRANS:
    :cvar ENT:
    :cvar AUT:
    :cvar INF:
    :cvar WIT:
    """
    TRANS = "TRANS"
    ENT = "ENT"
    AUT = "AUT"
    INF = "INF"
    WIT = "WIT"


class ParticipationInformationRecipient(Enum):
    """
    specDomain: S10263 (C-0-T10901-S21573-S10263-cpt)
    :cvar IRCP:
    :cvar REFB:
    :cvar REFT:
    :cvar PRCP:
    :cvar TRC:
    :cvar NOT_VALUE:
    """
    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT_VALUE = "NOT"


class ParticipationInformationTranscriber(Enum):
    """
    specDomain: S21463 (C-0-T10901-S21573-A10251-S21463-cpt)
    :cvar TRANS:
    :cvar ENT:
    """
    TRANS = "TRANS"
    ENT = "ENT"


class ParticipationMode(Enum):
    """
    vocSet: T16543 (C-0-T16543-cpt)
    :cvar ELECTRONIC:
    :cvar VERBAL:
    :cvar DICTATE:
    :cvar FACE:
    :cvar PHONE:
    :cvar VIDEOCONF:
    :cvar WRITTEN:
    :cvar EMAILWRIT:
    :cvar HANDWRIT:
    :cvar FAXWRIT:
    :cvar TYPEWRIT:
    :cvar PHYSICAL:
    :cvar REMOTE:
    """
    ELECTRONIC = "ELECTRONIC"
    VERBAL = "VERBAL"
    DICTATE = "DICTATE"
    FACE = "FACE"
    PHONE = "PHONE"
    VIDEOCONF = "VIDEOCONF"
    WRITTEN = "WRITTEN"
    EMAILWRIT = "EMAILWRIT"
    HANDWRIT = "HANDWRIT"
    FAXWRIT = "FAXWRIT"
    TYPEWRIT = "TYPEWRIT"
    PHYSICAL = "PHYSICAL"
    REMOTE = "REMOTE"


class ParticipationModeElectronicData(Enum):
    """
    specDomain: S16554 (C-0-T16543-S16554-cpt)
    :cvar ELECTRONIC:
    """
    ELECTRONIC = "ELECTRONIC"


class ParticipationModeVerbal(Enum):
    """
    specDomain: S16544 (C-0-T16543-S16544-cpt)
    :cvar VERBAL:
    :cvar DICTATE:
    :cvar FACE:
    :cvar PHONE:
    :cvar VIDEOCONF:
    """
    VERBAL = "VERBAL"
    DICTATE = "DICTATE"
    FACE = "FACE"
    PHONE = "PHONE"
    VIDEOCONF = "VIDEOCONF"


class ParticipationModeWritten(Enum):
    """
    specDomain: S16549 (C-0-T16543-S16549-cpt)
    :cvar WRITTEN:
    :cvar EMAILWRIT:
    :cvar HANDWRIT:
    :cvar FAXWRIT:
    :cvar TYPEWRIT:
    """
    WRITTEN = "WRITTEN"
    EMAILWRIT = "EMAILWRIT"
    HANDWRIT = "HANDWRIT"
    FAXWRIT = "FAXWRIT"
    TYPEWRIT = "TYPEWRIT"


class ParticipationParticipation(Enum):
    """
    specDomain: S21573 (C-0-T10901-S21573-cpt)
    :cvar ADM:
    :cvar ATND:
    :cvar CALLBCK:
    :cvar CON:
    :cvar DIS:
    :cvar ESC:
    :cvar REF:
    :cvar IND:
    :cvar BEN:
    :cvar CAGNT:
    :cvar COV:
    :cvar GUAR:
    :cvar HLD:
    :cvar RCV:
    :cvar RCT:
    :cvar TRANS:
    :cvar ENT:
    :cvar AUT:
    :cvar INF:
    :cvar WIT:
    :cvar IRCP:
    :cvar REFB:
    :cvar REFT:
    :cvar PRCP:
    :cvar TRC:
    :cvar NOT_VALUE:
    :cvar PRF:
    :cvar DIST:
    :cvar PPRF:
    :cvar SPRF:
    :cvar EXPART:
    :cvar EXSRC:
    :cvar EXPTRGT:
    :cvar DEV:
    :cvar NRD:
    :cvar RDV:
    :cvar SBJ:
    :cvar SPC:
    :cvar DIR:
    :cvar EXPAGNT:
    :cvar BBY:
    :cvar CSM:
    :cvar DON:
    :cvar PRD:
    :cvar LOC:
    :cvar DST:
    :cvar ELOC:
    :cvar ORG:
    :cvar RML:
    :cvar VIA:
    :cvar VRF:
    :cvar AUTHEN:
    :cvar LA:
    :cvar PART:
    :cvar CST:
    :cvar RESP:
    """
    ADM = "ADM"
    ATND = "ATND"
    CALLBCK = "CALLBCK"
    CON = "CON"
    DIS = "DIS"
    ESC = "ESC"
    REF = "REF"
    IND = "IND"
    BEN = "BEN"
    CAGNT = "CAGNT"
    COV = "COV"
    GUAR = "GUAR"
    HLD = "HLD"
    RCV = "RCV"
    RCT = "RCT"
    TRANS = "TRANS"
    ENT = "ENT"
    AUT = "AUT"
    INF = "INF"
    WIT = "WIT"
    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT_VALUE = "NOT"
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"
    SBJ = "SBJ"
    SPC = "SPC"
    DIR = "DIR"
    EXPAGNT = "EXPAGNT"
    BBY = "BBY"
    CSM = "CSM"
    DON = "DON"
    PRD = "PRD"
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"
    PART = "PART"
    CST = "CST"
    RESP = "RESP"


class ParticipationPhysicalPerformer(Enum):
    """
    specDomain: S10248 (C-0-T10901-S21573-S10248-cpt)
    :cvar PRF:
    :cvar DIST:
    :cvar PPRF:
    :cvar SPRF:
    """
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"


class ParticipationSignature(Enum):
    """
    vocSet: T10282 (C-0-T10282-cpt)
    :cvar I:
    :cvar X:
    :cvar S:
    """
    I = "I"
    X = "X"
    S = "S"


class ParticipationSubset(Enum):
    """
    abstDomain: A19736 (C-0-T19613-A19736-cpt)
    :cvar FUTURE:
    :cvar LAST:
    :cvar NEXT:
    :cvar FUTSUM:
    :cvar PAST:
    :cvar FIRST:
    :cvar RECENT:
    :cvar PREVSUM:
    :cvar SUM:
    """
    FUTURE = "FUTURE"
    LAST = "LAST"
    NEXT = "NEXT"
    FUTSUM = "FUTSUM"
    PAST = "PAST"
    FIRST = "FIRST"
    RECENT = "RECENT"
    PREVSUM = "PREVSUM"
    SUM = "SUM"


class ParticipationTargetDevice(Enum):
    """
    specDomain: S10298 (C-0-T10901-S21573-S10286-S10298-cpt)
    :cvar DEV:
    :cvar NRD:
    :cvar RDV:
    """
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"


class ParticipationTargetDirect(Enum):
    """
    specDomain: S10286 (C-0-T10901-S21573-S10286-cpt)
    :cvar EXPART:
    :cvar EXSRC:
    :cvar EXPTRGT:
    :cvar DEV:
    :cvar NRD:
    :cvar RDV:
    :cvar SBJ:
    :cvar SPC:
    :cvar DIR:
    :cvar EXPAGNT:
    :cvar BBY:
    :cvar CSM:
    :cvar DON:
    :cvar PRD:
    """
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"
    SBJ = "SBJ"
    SPC = "SPC"
    DIR = "DIR"
    EXPAGNT = "EXPAGNT"
    BBY = "BBY"
    CSM = "CSM"
    DON = "DON"
    PRD = "PRD"


class ParticipationTargetLocation(Enum):
    """
    specDomain: S10302 (C-0-T10901-S21573-S10302-cpt)
    :cvar LOC:
    :cvar DST:
    :cvar ELOC:
    :cvar ORG:
    :cvar RML:
    :cvar VIA:
    """
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"


class ParticipationTargetSubject(Enum):
    """
    specDomain: S10287 (C-0-T10901-S21573-S10286-S10287-cpt)
    :cvar SBJ:
    :cvar SPC:
    """
    SBJ = "SBJ"
    SPC = "SPC"


class ParticipationType(Enum):
    """
    vocSet: T10901 (C-0-T10901-cpt)
    :cvar ADM:
    :cvar ATND:
    :cvar CALLBCK:
    :cvar CON:
    :cvar DIS:
    :cvar ESC:
    :cvar REF:
    :cvar IND:
    :cvar BEN:
    :cvar CAGNT:
    :cvar COV:
    :cvar GUAR:
    :cvar HLD:
    :cvar RCV:
    :cvar RCT:
    :cvar TRANS:
    :cvar ENT:
    :cvar AUT:
    :cvar INF:
    :cvar WIT:
    :cvar IRCP:
    :cvar REFB:
    :cvar REFT:
    :cvar PRCP:
    :cvar TRC:
    :cvar NOT_VALUE:
    :cvar PRF:
    :cvar DIST:
    :cvar PPRF:
    :cvar SPRF:
    :cvar EXPART:
    :cvar EXSRC:
    :cvar EXPTRGT:
    :cvar DEV:
    :cvar NRD:
    :cvar RDV:
    :cvar SBJ:
    :cvar SPC:
    :cvar DIR:
    :cvar EXPAGNT:
    :cvar BBY:
    :cvar CSM:
    :cvar DON:
    :cvar PRD:
    :cvar LOC:
    :cvar DST:
    :cvar ELOC:
    :cvar ORG:
    :cvar RML:
    :cvar VIA:
    :cvar VRF:
    :cvar AUTHEN:
    :cvar LA:
    :cvar PART:
    :cvar CST:
    :cvar RESP:
    """
    ADM = "ADM"
    ATND = "ATND"
    CALLBCK = "CALLBCK"
    CON = "CON"
    DIS = "DIS"
    ESC = "ESC"
    REF = "REF"
    IND = "IND"
    BEN = "BEN"
    CAGNT = "CAGNT"
    COV = "COV"
    GUAR = "GUAR"
    HLD = "HLD"
    RCV = "RCV"
    RCT = "RCT"
    TRANS = "TRANS"
    ENT = "ENT"
    AUT = "AUT"
    INF = "INF"
    WIT = "WIT"
    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT_VALUE = "NOT"
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"
    SBJ = "SBJ"
    SPC = "SPC"
    DIR = "DIR"
    EXPAGNT = "EXPAGNT"
    BBY = "BBY"
    CSM = "CSM"
    DON = "DON"
    PRD = "PRD"
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"
    PART = "PART"
    CST = "CST"
    RESP = "RESP"


class ParticipationVerifier(Enum):
    """
    specDomain: S10259 (C-0-T10901-S21573-S10259-cpt)
    :cvar VRF:
    :cvar AUTHEN:
    :cvar LA:
    """
    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"


class PastSubset(Enum):
    """
    specDomain: S21367 (C-0-T19613-S21367-cpt)
    :cvar PAST:
    :cvar FIRST:
    :cvar RECENT:
    :cvar PREVSUM:
    """
    PAST = "PAST"
    FIRST = "FIRST"
    RECENT = "RECENT"
    PREVSUM = "PREVSUM"


class PasteDrugForm(Enum):
    """
    specDomain: S14451 (C-0-T19651-A14411-A14412-A14441-S14451-cpt)
    :cvar PASTE:
    :cvar PUD:
    :cvar TPASTE:
    """
    PASTE = "PASTE"
    PUD = "PUD"
    TPASTE = "TPASTE"


class PatchDrugForm(Enum):
    """
    specDomain: S14499 (C-0-T19651-A14411-A14412-A14484-S14499-cpt)
    :cvar TPATCH:
    :cvar TPATH16:
    :cvar TPATH24:
    :cvar TPATH72:
    :cvar TPATH2_WK:
    :cvar TPATHWK:
    :cvar PATCH:
    """
    TPATCH = "TPATCH"
    TPATH16 = "TPATH16"
    TPATH24 = "TPATH24"
    TPATH72 = "TPATH72"
    TPATH2_WK = "TPATH2WK"
    TPATHWK = "TPATHWK"
    PATCH = "PATCH"


class PathologyProviderCodes(Enum):
    """
    specDomain: S20189 (C-0-T19465-S20096-S20189-cpt)
    :cvar VALUE_207_Z00000_X:
    :cvar VALUE_207_ZP0101_X:
    :cvar VALUE_207_ZP0102_X:
    :cvar VALUE_207_ZB0001_X:
    :cvar VALUE_207_ZP0104_X:
    :cvar VALUE_207_ZP0105_X:
    :cvar VALUE_207_ZC0500_X:
    :cvar VALUE_207_ZD0900_X:
    :cvar VALUE_207_ZF0201_X:
    :cvar VALUE_207_ZH0000_X:
    :cvar VALUE_207_ZI0100_X:
    :cvar VALUE_207_ZM0300_X:
    :cvar VALUE_207_ZP0007_X:
    :cvar VALUE_207_ZN0500_X:
    :cvar VALUE_207_ZP0213_X:
    """
    VALUE_207_Z00000_X = "207Z00000X"
    VALUE_207_ZP0101_X = "207ZP0101X"
    VALUE_207_ZP0102_X = "207ZP0102X"
    VALUE_207_ZB0001_X = "207ZB0001X"
    VALUE_207_ZP0104_X = "207ZP0104X"
    VALUE_207_ZP0105_X = "207ZP0105X"
    VALUE_207_ZC0500_X = "207ZC0500X"
    VALUE_207_ZD0900_X = "207ZD0900X"
    VALUE_207_ZF0201_X = "207ZF0201X"
    VALUE_207_ZH0000_X = "207ZH0000X"
    VALUE_207_ZI0100_X = "207ZI0100X"
    VALUE_207_ZM0300_X = "207ZM0300X"
    VALUE_207_ZP0007_X = "207ZP0007X"
    VALUE_207_ZN0500_X = "207ZN0500X"
    VALUE_207_ZP0213_X = "207ZP0213X"


class PathologySpecialistOrTechnologistHipaa(Enum):
    """
    abstDomain: A13688 (C-0-T13129-A13130-A13644-A13688-cpt)
    :cvar VALUE_246_QB0000_N:
    :cvar VALUE_246_QC1000_N:
    :cvar VALUE_246_QC2700_N:
    :cvar VALUE_246_QH0401_N:
    :cvar VALUE_246_QH0000_N:
    :cvar VALUE_246_QH0600_N:
    :cvar VALUE_246_QI0000_N:
    :cvar VALUE_246_QL0900_N:
    :cvar VALUE_246_QL0901_N:
    :cvar VALUE_246_QM0706_N:
    :cvar VALUE_246_QM0900_N:
    """
    VALUE_246_QB0000_N = "246QB0000N"
    VALUE_246_QC1000_N = "246QC1000N"
    VALUE_246_QC2700_N = "246QC2700N"
    VALUE_246_QH0401_N = "246QH0401N"
    VALUE_246_QH0000_N = "246QH0000N"
    VALUE_246_QH0600_N = "246QH0600N"
    VALUE_246_QI0000_N = "246QI0000N"
    VALUE_246_QL0900_N = "246QL0900N"
    VALUE_246_QL0901_N = "246QL0901N"
    VALUE_246_QM0706_N = "246QM0706N"
    VALUE_246_QM0900_N = "246QM0900N"


class PathologyTechnicianHipaa(Enum):
    """
    abstDomain: A13711 (C-0-T13129-A13130-A13644-A13711-cpt)
    :cvar VALUE_246_RH0600_N:
    :cvar VALUE_246_RM2200_N:
    :cvar VALUE_246_RP1900_N:
    """
    VALUE_246_RH0600_N = "246RH0600N"
    VALUE_246_RM2200_N = "246RM2200N"
    VALUE_246_RP1900_N = "246RP1900N"


class PatientImportance(Enum):
    """
    vocSet: T19265 (C-0-T19265-cpt)
    :cvar BM:
    :cvar FD:
    :cvar FOR_VALUE:
    :cvar GOVT:
    :cvar DFM:
    :cvar SFM:
    :cvar STF:
    :cvar DR:
    :cvar VIP:
    """
    BM = "BM"
    FD = "FD"
    FOR_VALUE = "FOR"
    GOVT = "GOVT"
    DFM = "DFM"
    SFM = "SFM"
    STF = "STF"
    DR = "DR"
    VIP = "VIP"


class PatientProfileQueryReasonCode(Enum):
    """
    abstDomain: A19784 (C-0-T14878-A19692-A19784-cpt)
    :cvar ADMREV:
    :cvar PATCAR:
    :cvar PATREQ:
    :cvar PRCREV:
    :cvar REGUL:
    :cvar RSRCH:
    :cvar LEGAL:
    :cvar VALIDATION:
    """
    ADMREV = "ADMREV"
    PATCAR = "PATCAR"
    PATREQ = "PATREQ"
    PRCREV = "PRCREV"
    REGUL = "REGUL"
    RSRCH = "RSRCH"
    LEGAL = "LEGAL"
    VALIDATION = "VALIDATION"


class PaymentTerms(Enum):
    """
    vocSet: T14908 (C-0-T14908-cpt)
    :cvar COD:
    :cvar N30:
    :cvar N60:
    :cvar N90:
    """
    COD = "COD"
    N30 = "N30"
    N60 = "N60"
    N90 = "N90"


class PayorParticipationFunction(Enum):
    """
    abstDomain: A19906 (C-0-T10267-A19903-A19906-cpt)
    :cvar CLMADJ:
    :cvar ENROLL:
    :cvar FFSMGT:
    :cvar MCMGT:
    :cvar PROVMGT:
    :cvar UMGT:
    """
    CLMADJ = "CLMADJ"
    ENROLL = "ENROLL"
    FFSMGT = "FFSMGT"
    MCMGT = "MCMGT"
    PROVMGT = "PROVMGT"
    UMGT = "UMGT"


class PayorRoleType(Enum):
    """
    abstDomain: A19853 (C-0-T12206-A19690-A19853-cpt)
    :cvar ENROLBKR:
    :cvar TPA:
    :cvar UMO:
    """
    ENROLBKR = "ENROLBKR"
    TPA = "TPA"
    UMO = "UMO"


class PediatricsProviderCodes(Enum):
    """
    specDomain: S20204 (C-0-T19465-S20096-S20204-cpt)
    :cvar VALUE_208000000_X:
    :cvar VALUE_2080_A0000_X:
    :cvar VALUE_2080_I0007_X:
    :cvar VALUE_2080_P0006_X:
    :cvar VALUE_2080_T0002_X:
    :cvar VALUE_2080_N0001_X:
    :cvar VALUE_2080_P0008_X:
    :cvar VALUE_2080_P0201_X:
    :cvar VALUE_2080_P0202_X:
    :cvar VALUE_2080_P0203_X:
    :cvar VALUE_2080_P0204_X:
    :cvar VALUE_2080_P0205_X:
    :cvar VALUE_2080_P0206_X:
    :cvar VALUE_2080_P0207_X:
    :cvar VALUE_2080_P0208_X:
    :cvar VALUE_2080_P0210_X:
    :cvar VALUE_2080_P0214_X:
    :cvar VALUE_2080_P0216_X:
    :cvar VALUE_2080_S0010_X:
    """
    VALUE_208000000_X = "208000000X"
    VALUE_2080_A0000_X = "2080A0000X"
    VALUE_2080_I0007_X = "2080I0007X"
    VALUE_2080_P0006_X = "2080P0006X"
    VALUE_2080_T0002_X = "2080T0002X"
    VALUE_2080_N0001_X = "2080N0001X"
    VALUE_2080_P0008_X = "2080P0008X"
    VALUE_2080_P0201_X = "2080P0201X"
    VALUE_2080_P0202_X = "2080P0202X"
    VALUE_2080_P0203_X = "2080P0203X"
    VALUE_2080_P0204_X = "2080P0204X"
    VALUE_2080_P0205_X = "2080P0205X"
    VALUE_2080_P0206_X = "2080P0206X"
    VALUE_2080_P0207_X = "2080P0207X"
    VALUE_2080_P0208_X = "2080P0208X"
    VALUE_2080_P0210_X = "2080P0210X"
    VALUE_2080_P0214_X = "2080P0214X"
    VALUE_2080_P0216_X = "2080P0216X"
    VALUE_2080_S0010_X = "2080S0010X"


class PedsClinPracticeSetting(Enum):
    """
    specDomain: S10953 (C-0-T12206-A17660-A19450-A10588-S10589-S10953-cpt)
    :cvar PEDC:
    :cvar PEDCARD:
    :cvar PEDE:
    :cvar PEDGI:
    :cvar PEDHEM:
    :cvar PEDID:
    :cvar PEDNEPH:
    :cvar PEDHO:
    :cvar PEDRHEUM:
    """
    PEDC = "PEDC"
    PEDCARD = "PEDCARD"
    PEDE = "PEDE"
    PEDGI = "PEDGI"
    PEDHEM = "PEDHEM"
    PEDID = "PEDID"
    PEDNEPH = "PEDNEPH"
    PEDHO = "PEDHO"
    PEDRHEUM = "PEDRHEUM"


class PedsIcupracticeSetting(Enum):
    """
    specDomain: S10916 (C-0-T12206-A17660-A19450-A10588-S10596-S10920-S10916-cpt)
    :cvar PEDICU:
    :cvar PEDNICU:
    """
    PEDICU = "PEDICU"
    PEDNICU = "PEDNICU"


class PedsPracticeSetting(Enum):
    """
    specDomain: S10920 (C-0-T12206-A17660-A19450-A10588-S10596-S10920-cpt)
    :cvar PEDICU:
    :cvar PEDNICU:
    :cvar PEDU:
    """
    PEDICU = "PEDICU"
    PEDNICU = "PEDNICU"
    PEDU = "PEDU"


class PerianalRoute(Enum):
    """
    abstDomain: A17291 (C-0-T14581-A17021-A17291-cpt)
    :cvar PERIANAL:
    """
    PERIANAL = "PERIANAL"


class PeriarticularRoute(Enum):
    """
    abstDomain: A17293 (C-0-T14581-A17021-A17293-cpt)
    :cvar PAINJ:
    """
    PAINJ = "PAINJ"


class PeriduralRoute(Enum):
    """
    abstDomain: A17298 (C-0-T14581-A17021-A17298-cpt)
    :cvar PDURINJ:
    """
    PDURINJ = "PDURINJ"


class PerinealRoute(Enum):
    """
    abstDomain: A17300 (C-0-T14581-A17021-A17300-cpt)
    :cvar PERINEAL:
    """
    PERINEAL = "PERINEAL"


class PerineuralRoute(Enum):
    """
    abstDomain: A17302 (C-0-T14581-A17021-A17302-cpt)
    :cvar PNINJ:
    """
    PNINJ = "PNINJ"


class PeriodontalRoute(Enum):
    """
    abstDomain: A17295 (C-0-T14581-A17021-A17295-cpt)
    :cvar PDONTINJ:
    :cvar PDONTTA:
    """
    PDONTINJ = "PDONTINJ"
    PDONTTA = "PDONTTA"


class PermanentDentition(Enum):
    """
    abstDomain: A19342 (C-0-T16537-A16538-A19346-A19342-cpt)
    :cvar TID1:
    :cvar TID10:
    :cvar TID11:
    :cvar TID12:
    :cvar TID13:
    :cvar TID14:
    :cvar TID15:
    :cvar TID16:
    :cvar TID17:
    :cvar TID17D:
    :cvar TID17M:
    :cvar TID18:
    :cvar TID18D:
    :cvar TID18M:
    :cvar TID19:
    :cvar TID19D:
    :cvar TID19M:
    :cvar TID2:
    :cvar TID20:
    :cvar TID21:
    :cvar TID22:
    :cvar TID23:
    :cvar TID24:
    :cvar TID25:
    :cvar TID26:
    :cvar TID27:
    :cvar TID28:
    :cvar TID29:
    :cvar TID3:
    :cvar TID30:
    :cvar TID30D:
    :cvar TID30M:
    :cvar TID31:
    :cvar TID31D:
    :cvar TID31M:
    :cvar TID32:
    :cvar TID32D:
    :cvar TID32M:
    :cvar TID4:
    :cvar TID5:
    :cvar TID6:
    :cvar TID7:
    :cvar TID8:
    :cvar TID9:
    """
    TID1 = "TID1"
    TID10 = "TID10"
    TID11 = "TID11"
    TID12 = "TID12"
    TID13 = "TID13"
    TID14 = "TID14"
    TID15 = "TID15"
    TID16 = "TID16"
    TID17 = "TID17"
    TID17D = "TID17d"
    TID17M = "TID17m"
    TID18 = "TID18"
    TID18D = "TID18d"
    TID18M = "TID18m"
    TID19 = "TID19"
    TID19D = "TID19d"
    TID19M = "TID19m"
    TID2 = "TID2"
    TID20 = "TID20"
    TID21 = "TID21"
    TID22 = "TID22"
    TID23 = "TID23"
    TID24 = "TID24"
    TID25 = "TID25"
    TID26 = "TID26"
    TID27 = "TID27"
    TID28 = "TID28"
    TID29 = "TID29"
    TID3 = "TID3"
    TID30 = "TID30"
    TID30D = "TID30d"
    TID30M = "TID30m"
    TID31 = "TID31"
    TID31D = "TID31d"
    TID31M = "TID31m"
    TID32 = "TID32"
    TID32D = "TID32d"
    TID32M = "TID32m"
    TID4 = "TID4"
    TID5 = "TID5"
    TID6 = "TID6"
    TID7 = "TID7"
    TID8 = "TID8"
    TID9 = "TID9"


class PersonDisabilityType(Enum):
    """
    vocSet: T295 (C-0-T295-cpt)
    :cvar VALUE_5:
    :cvar CB:
    :cvar CR:
    :cvar G:
    :cvar WK:
    :cvar WC:
    :cvar VALUE_4:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_1:
    """
    VALUE_5 = "5"
    CB = "CB"
    CR = "CR"
    G = "G"
    WK = "WK"
    WC = "WC"
    VALUE_4 = "4"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_1 = "1"


class PersonNamePartAffixTypes(Enum):
    """
    abstDomain: A10666 (C-0-T15888-A10659-A10666-cpt)
    :cvar AC:
    :cvar NB:
    :cvar PR:
    :cvar VV:
    """
    AC = "AC"
    NB = "NB"
    PR = "PR"
    VV = "VV"


class PersonNamePartChangeQualifier(Enum):
    """
    abstDomain: A10660 (C-0-T15888-A10659-A10660-cpt)
    :cvar AD:
    :cvar BR:
    :cvar SP:
    """
    AD = "AD"
    BR = "BR"
    SP = "SP"


class PersonNamePartMiscQualifier(Enum):
    """
    abstDomain: A10671 (C-0-T15888-A10659-A10671-cpt)
    :cvar CL:
    """
    CL = "CL"


class PersonNamePartQualifier(Enum):
    """
    abstDomain: A10659 (C-0-T15888-A10659-cpt)
    :cvar AC:
    :cvar NB:
    :cvar PR:
    :cvar VV:
    :cvar AD:
    :cvar BR:
    :cvar SP:
    :cvar CL:
    :cvar IN_VALUE:
    :cvar TITLE:
    """
    AC = "AC"
    NB = "NB"
    PR = "PR"
    VV = "VV"
    AD = "AD"
    BR = "BR"
    SP = "SP"
    CL = "CL"
    IN_VALUE = "IN"
    TITLE = "TITLE"


class PersonNameUse(Enum):
    """
    abstDomain: A200 (C-0-T15913-A200-cpt)
    :cvar SRCH:
    :cvar SNDX:
    :cvar PHON:
    :cvar ABC:
    :cvar IDE:
    :cvar SYL:
    :cvar L:
    :cvar OR_VALUE:
    :cvar P:
    :cvar A:
    :cvar I:
    :cvar C:
    :cvar R:
    :cvar ASGN:
    """
    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    L = "L"
    OR_VALUE = "OR"
    P = "P"
    A = "A"
    I = "I"
    C = "C"
    R = "R"
    ASGN = "ASGN"


class PersonNameUseLegalByBot(Enum):
    """
    specDomain: S10176 (C-0-T15913-A200-S10176-cpt)
    :cvar L:
    :cvar OR_VALUE:
    """
    L = "L"
    OR_VALUE = "OR"


class PersonNameUsePseudonym(Enum):
    """
    specDomain: S21321 (C-0-T15913-A200-S21321-cpt)
    :cvar P:
    :cvar A:
    """
    P = "P"
    A = "A"


class PersonalRelationshipRoleType(Enum):
    """
    abstDomain: A19563 (C-0-T12206-A19563-cpt)
    :cvar CHLDADOPT:
    :cvar DAUADOPT:
    :cvar SONADOPT:
    :cvar CHLDINLAW:
    :cvar DAUINLAW:
    :cvar SONINLAW:
    :cvar CHLDFOST:
    :cvar DAUFOST:
    :cvar SONFOST:
    :cvar NCHILD:
    :cvar DAU:
    :cvar SON:
    :cvar STPCHLD:
    :cvar STPDAU:
    :cvar STPSON:
    :cvar CHILD:
    :cvar AUNT:
    :cvar MAUNT:
    :cvar PAUNT:
    :cvar COUSN:
    :cvar MCOUSN:
    :cvar PCOUSN:
    :cvar UNCLE:
    :cvar MUNCLE:
    :cvar PUNCLE:
    :cvar GRNDCHILD:
    :cvar GRNDDAU:
    :cvar GRNDSON:
    :cvar GRPRN:
    :cvar GRFTH:
    :cvar GRMTH:
    :cvar MGRFTH:
    :cvar MGRMTH:
    :cvar MGRPRN:
    :cvar PGRFTH:
    :cvar PGRMTH:
    :cvar PGRPRN:
    :cvar GGRPRN:
    :cvar MGGRFTH:
    :cvar MGGRMTH:
    :cvar MGGRPRN:
    :cvar PGGRFTH:
    :cvar PGGRMTH:
    :cvar PGGRPRN:
    :cvar GGRFTH:
    :cvar GGRMTH:
    :cvar NIENEPH:
    :cvar NEPHEW:
    :cvar NIECE:
    :cvar NFTH:
    :cvar NFTHF:
    :cvar NPRN:
    :cvar NMTH:
    :cvar PRNINLAW:
    :cvar FTHINLAW:
    :cvar MTHINLAW:
    :cvar STPPRN:
    :cvar STPFTH:
    :cvar STPMTH:
    :cvar PRN:
    :cvar FTH:
    :cvar MTH:
    :cvar HSIB:
    :cvar HBRO:
    :cvar HSIS:
    :cvar NSIB:
    :cvar NBRO:
    :cvar NSIS:
    :cvar SIBINLAW:
    :cvar BROINLAW:
    :cvar SISINLAW:
    :cvar STPSIB:
    :cvar STPBRO:
    :cvar STPSIS:
    :cvar SIB:
    :cvar BRO:
    :cvar SIS:
    :cvar SPS:
    :cvar HUSB:
    :cvar WIFE:
    :cvar SIGOTHR:
    :cvar FAMMEMB:
    :cvar ROOM:
    :cvar DOMPART:
    :cvar NBOR:
    :cvar FRND:
    """
    CHLDADOPT = "CHLDADOPT"
    DAUADOPT = "DAUADOPT"
    SONADOPT = "SONADOPT"
    CHLDINLAW = "CHLDINLAW"
    DAUINLAW = "DAUINLAW"
    SONINLAW = "SONINLAW"
    CHLDFOST = "CHLDFOST"
    DAUFOST = "DAUFOST"
    SONFOST = "SONFOST"
    NCHILD = "NCHILD"
    DAU = "DAU"
    SON = "SON"
    STPCHLD = "STPCHLD"
    STPDAU = "STPDAU"
    STPSON = "STPSON"
    CHILD = "CHILD"
    AUNT = "AUNT"
    MAUNT = "MAUNT"
    PAUNT = "PAUNT"
    COUSN = "COUSN"
    MCOUSN = "MCOUSN"
    PCOUSN = "PCOUSN"
    UNCLE = "UNCLE"
    MUNCLE = "MUNCLE"
    PUNCLE = "PUNCLE"
    GRNDCHILD = "GRNDCHILD"
    GRNDDAU = "GRNDDAU"
    GRNDSON = "GRNDSON"
    GRPRN = "GRPRN"
    GRFTH = "GRFTH"
    GRMTH = "GRMTH"
    MGRFTH = "MGRFTH"
    MGRMTH = "MGRMTH"
    MGRPRN = "MGRPRN"
    PGRFTH = "PGRFTH"
    PGRMTH = "PGRMTH"
    PGRPRN = "PGRPRN"
    GGRPRN = "GGRPRN"
    MGGRFTH = "MGGRFTH"
    MGGRMTH = "MGGRMTH"
    MGGRPRN = "MGGRPRN"
    PGGRFTH = "PGGRFTH"
    PGGRMTH = "PGGRMTH"
    PGGRPRN = "PGGRPRN"
    GGRFTH = "GGRFTH"
    GGRMTH = "GGRMTH"
    NIENEPH = "NIENEPH"
    NEPHEW = "NEPHEW"
    NIECE = "NIECE"
    NFTH = "NFTH"
    NFTHF = "NFTHF"
    NPRN = "NPRN"
    NMTH = "NMTH"
    PRNINLAW = "PRNINLAW"
    FTHINLAW = "FTHINLAW"
    MTHINLAW = "MTHINLAW"
    STPPRN = "STPPRN"
    STPFTH = "STPFTH"
    STPMTH = "STPMTH"
    PRN = "PRN"
    FTH = "FTH"
    MTH = "MTH"
    HSIB = "HSIB"
    HBRO = "HBRO"
    HSIS = "HSIS"
    NSIB = "NSIB"
    NBRO = "NBRO"
    NSIS = "NSIS"
    SIBINLAW = "SIBINLAW"
    BROINLAW = "BROINLAW"
    SISINLAW = "SISINLAW"
    STPSIB = "STPSIB"
    STPBRO = "STPBRO"
    STPSIS = "STPSIS"
    SIB = "SIB"
    BRO = "BRO"
    SIS = "SIS"
    SPS = "SPS"
    HUSB = "HUSB"
    WIFE = "WIFE"
    SIGOTHR = "SIGOTHR"
    FAMMEMB = "FAMMEMB"
    ROOM = "ROOM"
    DOMPART = "DOMPART"
    NBOR = "NBOR"
    FRND = "FRND"


class PharmacistHipaa(Enum):
    """
    specDomain: S13355 (C-0-T13129-A13130-A13354-S13355-cpt)
    :cvar VALUE_183500000_N:
    :cvar VALUE_1835_G0000_N:
    :cvar VALUE_1835_N0905_N:
    :cvar VALUE_1835_N1003_N:
    :cvar VALUE_1835_P1200_N:
    :cvar VALUE_1835_P1300_N:
    """
    VALUE_183500000_N = "183500000N"
    VALUE_1835_G0000_N = "1835G0000N"
    VALUE_1835_N0905_N = "1835N0905N"
    VALUE_1835_N1003_N = "1835N1003N"
    VALUE_1835_P1200_N = "1835P1200N"
    VALUE_1835_P1300_N = "1835P1300N"


class PharmacistProviderCodes(Enum):
    """
    specDomain: S20456 (C-0-T19465-S20455-S20456-cpt)
    :cvar VALUE_183500000_X:
    :cvar VALUE_1835_G0000_X:
    :cvar VALUE_1835_N0905_X:
    :cvar VALUE_1835_N1003_X:
    :cvar VALUE_1835_P1200_X:
    :cvar VALUE_1835_P1300_X:
    """
    VALUE_183500000_X = "183500000X"
    VALUE_1835_G0000_X = "1835G0000X"
    VALUE_1835_N0905_X = "1835N0905X"
    VALUE_1835_N1003_X = "1835N1003X"
    VALUE_1835_P1200_X = "1835P1200X"
    VALUE_1835_P1300_X = "1835P1300X"


class PharmacyServiceProviderTechnicianHipaa(Enum):
    """
    abstDomain: A13361 (C-0-T13129-A13130-A13354-A13361-cpt)
    :cvar VALUE_1847_P3400_N:
    """
    VALUE_1847_P3400_N = "1847P3400N"


class PharmacyServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20455 (C-0-T19465-S20455-cpt)
    :cvar VALUE_183500000_X:
    :cvar VALUE_1835_G0000_X:
    :cvar VALUE_1835_N0905_X:
    :cvar VALUE_1835_N1003_X:
    :cvar VALUE_1835_P1200_X:
    :cvar VALUE_1835_P1300_X:
    :cvar VALUE_180000000_X:
    :cvar VALUE_183700000_X:
    """
    VALUE_183500000_X = "183500000X"
    VALUE_1835_G0000_X = "1835G0000X"
    VALUE_1835_N0905_X = "1835N0905X"
    VALUE_1835_N1003_X = "1835N1003X"
    VALUE_1835_P1200_X = "1835P1200X"
    VALUE_1835_P1300_X = "1835P1300X"
    VALUE_180000000_X = "180000000X"
    VALUE_183700000_X = "183700000X"


class PharmacySupplyEventStockReasonCode(Enum):
    """
    abstDomain: A19785 (C-0-T14878-A19785-cpt)
    :cvar FLRSTCK:
    :cvar LTC:
    :cvar OFFICE:
    :cvar PHARM:
    :cvar PROG:
    """
    FLRSTCK = "FLRSTCK"
    LTC = "LTC"
    OFFICE = "OFFICE"
    PHARM = "PHARM"
    PROG = "PROG"


class PharmacySupplyRequestRenewalRefusalReasonCode(Enum):
    """
    abstDomain: A19786 (C-0-T14878-A19786-cpt)
    :cvar FAMPHYS:
    :cvar ONHOLD:
    :cvar MODIFY:
    :cvar ALREADYRX:
    :cvar NEEDAPMT:
    :cvar NOTPAT:
    :cvar NOTAVAIL:
    :cvar DISCONT:
    :cvar TOOEARLY:
    """
    FAMPHYS = "FAMPHYS"
    ONHOLD = "ONHOLD"
    MODIFY = "MODIFY"
    ALREADYRX = "ALREADYRX"
    NEEDAPMT = "NEEDAPMT"
    NOTPAT = "NOTPAT"
    NOTAVAIL = "NOTAVAIL"
    DISCONT = "DISCONT"
    TOOEARLY = "TOOEARLY"


class PhysicalMedicineandRehabilitationProviderCodes(Enum):
    """
    specDomain: S20223 (C-0-T19465-S20096-S20223-cpt)
    :cvar VALUE_208100000_X:
    :cvar VALUE_2081_P2900_X:
    :cvar VALUE_2081_P0010_X:
    :cvar VALUE_2081_P0004_X:
    :cvar VALUE_2081_S0010_X:
    """
    VALUE_208100000_X = "208100000X"
    VALUE_2081_P2900_X = "2081P2900X"
    VALUE_2081_P0010_X = "2081P0010X"
    VALUE_2081_P0004_X = "2081P0004X"
    VALUE_2081_S0010_X = "2081S0010X"


class PhysicalTherapistHipaa(Enum):
    """
    specDomain: S13609 (C-0-T13129-A13130-A13592-S13609-cpt)
    :cvar VALUE_225100000_N:
    :cvar VALUE_2251_C2600_N:
    :cvar VALUE_2251_C0400_N:
    :cvar VALUE_2251_E1300_N:
    :cvar VALUE_2251_E1200_N:
    :cvar VALUE_2251_G0304_N:
    :cvar VALUE_2251_H1200_N:
    :cvar VALUE_2251_H1300_N:
    :cvar VALUE_2251_N0400_N:
    :cvar VALUE_2251_X0800_N:
    :cvar VALUE_2251_P0200_N:
    :cvar VALUE_2251_S0007_N:
    """
    VALUE_225100000_N = "225100000N"
    VALUE_2251_C2600_N = "2251C2600N"
    VALUE_2251_C0400_N = "2251C0400N"
    VALUE_2251_E1300_N = "2251E1300N"
    VALUE_2251_E1200_N = "2251E1200N"
    VALUE_2251_G0304_N = "2251G0304N"
    VALUE_2251_H1200_N = "2251H1200N"
    VALUE_2251_H1300_N = "2251H1300N"
    VALUE_2251_N0400_N = "2251N0400N"
    VALUE_2251_X0800_N = "2251X0800N"
    VALUE_2251_P0200_N = "2251P0200N"
    VALUE_2251_S0007_N = "2251S0007N"


class PhysicalTherapistProviderCodes(Enum):
    """
    specDomain: S20548 (C-0-T19465-S20532-S20548-cpt)
    :cvar VALUE_225100000_X:
    :cvar VALUE_2251_C2600_X:
    :cvar VALUE_2251_E1300_X:
    :cvar VALUE_2251_E1200_X:
    :cvar VALUE_2251_G0304_X:
    :cvar VALUE_2251_H1200_X:
    :cvar VALUE_2251_H1300_X:
    :cvar VALUE_2251_N0400_X:
    :cvar VALUE_2251_X0800_X:
    :cvar VALUE_2251_P0200_X:
    :cvar VALUE_2251_S0007_X:
    """
    VALUE_225100000_X = "225100000X"
    VALUE_2251_C2600_X = "2251C2600X"
    VALUE_2251_E1300_X = "2251E1300X"
    VALUE_2251_E1200_X = "2251E1200X"
    VALUE_2251_G0304_X = "2251G0304X"
    VALUE_2251_H1200_X = "2251H1200X"
    VALUE_2251_H1300_X = "2251H1300X"
    VALUE_2251_N0400_X = "2251N0400X"
    VALUE_2251_X0800_X = "2251X0800X"
    VALUE_2251_P0200_X = "2251P0200X"
    VALUE_2251_S0007_X = "2251S0007X"


class PhysicianAndOrOsteopathHipaa(Enum):
    """
    specDomain: S13426 (C-0-T13129-A13130-A13425-S13426-cpt)
    :cvar VALUE_203_B00000_N:
    :cvar VALUE_203_BA0401_N:
    :cvar VALUE_203_BA0000_Y:
    :cvar VALUE_203_BA0001_N:
    :cvar VALUE_203_BA0002_Y:
    :cvar VALUE_203_BA0003_Y:
    :cvar VALUE_203_BA0501_N:
    :cvar VALUE_203_BA0502_N:
    :cvar VALUE_203_BA0100_Y:
    :cvar VALUE_203_BA0101_Y:
    :cvar VALUE_203_BA0503_N:
    :cvar VALUE_203_BA0504_N:
    :cvar VALUE_203_BA0200_N:
    :cvar VALUE_203_BA0201_Y:
    :cvar VALUE_203_BA0202_N:
    :cvar VALUE_203_BA0300_Y:
    :cvar VALUE_203_BB0000_N:
    :cvar VALUE_203_BB0001_Y:
    :cvar VALUE_203_BB0100_Y:
    :cvar VALUE_203_BC0000_Y:
    :cvar VALUE_203_BC0001_Y:
    :cvar VALUE_203_BC0100_Y:
    :cvar VALUE_203_BC2500_Y:
    :cvar VALUE_203_BC0200_Y:
    :cvar VALUE_203_BC0201_Y:
    :cvar VALUE_203_BC0202_Y:
    :cvar VALUE_203_BC0203_Y:
    :cvar VALUE_203_BC0300_Y:
    :cvar VALUE_203_BC0500_Y:
    :cvar VALUE_203_BD0100_Y:
    :cvar VALUE_203_BD0101_Y:
    :cvar VALUE_203_BD0900_Y:
    :cvar VALUE_203_BD0901_N:
    :cvar VALUE_203_BD0300_N:
    :cvar VALUE_203_BE0004_Y:
    :cvar VALUE_203_BE0100_Y:
    :cvar VALUE_203_BE0101_Y:
    :cvar VALUE_203_BE0102_Y:
    :cvar VALUE_203_BF0100_Y:
    :cvar VALUE_203_BF0201_Y:
    :cvar VALUE_203_BF0202_N:
    :cvar VALUE_203_BG0100_Y:
    :cvar VALUE_203_BG0000_Y:
    :cvar VALUE_203_BG0201_Y:
    :cvar VALUE_203_BG0202_Y:
    :cvar VALUE_203_BG0204_Y:
    :cvar VALUE_203_BG0203_Y:
    :cvar VALUE_203_BG0200_Y:
    :cvar VALUE_203_BG0300_N:
    :cvar VALUE_203_BG0301_Y:
    :cvar VALUE_203_BG0302_Y:
    :cvar VALUE_203_BG0303_Y:
    :cvar VALUE_203_BG0400_N:
    :cvar VALUE_203_BH0000_Y:
    :cvar VALUE_203_BH0003_Y:
    :cvar VALUE_203_BH0001_Y:
    :cvar VALUE_203_BH0002_Y:
    :cvar VALUE_203_BI0001_N:
    :cvar VALUE_203_BI0002_N:
    :cvar VALUE_203_BI0005_N:
    :cvar VALUE_203_BI0006_N:
    :cvar VALUE_203_BI0007_N:
    :cvar VALUE_203_BI0003_Y:
    :cvar VALUE_203_BI0004_Y:
    :cvar VALUE_203_BI0100_Y:
    :cvar VALUE_203_BI0200_Y:
    :cvar VALUE_203_BI0400_N:
    :cvar VALUE_203_BI0300_Y:
    :cvar VALUE_203_BL0000_Y:
    :cvar VALUE_203_BM0101_Y:
    :cvar VALUE_203_BM0200_Y:
    :cvar VALUE_203_BM0300_Y:
    :cvar VALUE_203_BN0001_Y:
    :cvar VALUE_203_BN0100_Y:
    :cvar VALUE_203_BN0200_N:
    :cvar VALUE_203_BN0300_Y:
    :cvar VALUE_203_BN0400_Y:
    :cvar VALUE_203_BN0402_Y:
    :cvar VALUE_203_BN0500_Y:
    :cvar VALUE_203_BN0600_Y:
    :cvar VALUE_203_BN0700_Y:
    :cvar VALUE_203_BN0901_Y:
    :cvar VALUE_203_BN0902_Y:
    :cvar VALUE_203_BN0900_Y:
    :cvar VALUE_203_BN0903_Y:
    :cvar VALUE_203_BN0904_Y:
    :cvar VALUE_203_BX0000_N:
    :cvar VALUE_203_BX0001_Y:
    :cvar VALUE_203_BX0100_Y:
    :cvar VALUE_203_BX0104_Y:
    :cvar VALUE_203_BX0105_Y:
    :cvar VALUE_203_BX0200_Y:
    :cvar VALUE_203_BX0201_Y:
    :cvar VALUE_203_BX0202_Y:
    :cvar VALUE_203_BX0300_Y:
    :cvar VALUE_203_BX0800_N:
    :cvar VALUE_203_BX2100_Y:
    :cvar VALUE_203_BX0500_Y:
    :cvar VALUE_203_BX0900_N:
    :cvar VALUE_203_BX0901_N:
    :cvar VALUE_203_BX0600_Y:
    :cvar VALUE_203_BX0601_N:
    :cvar VALUE_203_BP0001_Y:
    :cvar VALUE_203_BP2900_N:
    :cvar VALUE_203_BP0100_Y:
    :cvar VALUE_203_BP0101_Y:
    :cvar VALUE_203_BP0102_Y:
    :cvar VALUE_203_BP0103_Y:
    :cvar VALUE_203_BP0104_Y:
    :cvar VALUE_203_BP0105_Y:
    :cvar VALUE_203_BP0107_N:
    :cvar VALUE_203_BP0201_Y:
    :cvar VALUE_203_BP0202_Y:
    :cvar VALUE_203_BP0203_Y:
    :cvar VALUE_203_BP0204_Y:
    :cvar VALUE_203_BP0205_Y:
    :cvar VALUE_203_BP0206_Y:
    :cvar VALUE_203_BP0207_Y:
    :cvar VALUE_203_BP0208_Y:
    :cvar VALUE_203_BP0209_Y:
    :cvar VALUE_203_BP0220_N:
    :cvar VALUE_203_BP0210_Y:
    :cvar VALUE_203_BP0211_Y:
    :cvar VALUE_203_BP0212_Y:
    :cvar VALUE_203_BP0213_Y:
    :cvar VALUE_203_BP0214_Y:
    :cvar VALUE_203_BP0215_N:
    :cvar VALUE_203_BP0216_Y:
    :cvar VALUE_203_BP0200_Y:
    :cvar VALUE_203_BP2600_N:
    :cvar VALUE_203_BP1200_N:
    :cvar VALUE_203_BP0400_Y:
    :cvar VALUE_203_BP0500_Y:
    :cvar VALUE_203_BP0600_Y:
    :cvar VALUE_203_BP0800_Y:
    :cvar VALUE_203_BP0801_Y:
    :cvar VALUE_203_BP0802_Y:
    :cvar VALUE_203_BP0803_Y:
    :cvar VALUE_203_BP0804_Y:
    :cvar VALUE_203_BP0805_Y:
    :cvar VALUE_203_BP0806_N:
    :cvar VALUE_203_BP1300_N:
    :cvar VALUE_203_BP0901_N:
    :cvar VALUE_203_BP0903_Y:
    :cvar VALUE_203_BP1001_Y:
    :cvar VALUE_203_BP1003_Y:
    :cvar VALUE_203_BR0001_Y:
    :cvar VALUE_203_BR0002_Y:
    :cvar VALUE_203_BR0205_N:
    :cvar VALUE_203_BR0200_Y:
    :cvar VALUE_203_BR0201_Y:
    :cvar VALUE_203_BR0202_Y:
    :cvar VALUE_203_BR0203_N:
    :cvar VALUE_203_BR0204_N:
    :cvar VALUE_203_BR0300_N:
    :cvar VALUE_203_BR0402_Y:
    :cvar VALUE_203_BR0500_Y:
    :cvar VALUE_203_BR0600_N:
    :cvar VALUE_203_BR0700_Y:
    :cvar VALUE_203_BR0701_Y:
    :cvar VALUE_203_BS0000_Y:
    :cvar VALUE_203_BS0001_Y:
    :cvar VALUE_203_BS0002_Y:
    :cvar VALUE_203_BS0003_Y:
    :cvar VALUE_203_BS0004_Y:
    :cvar VALUE_203_BS0104_N:
    :cvar VALUE_203_BS0133_N:
    :cvar VALUE_203_BS0101_Y:
    :cvar VALUE_203_BS0123_Y:
    :cvar VALUE_203_BS0100_Y:
    :cvar VALUE_203_BS0129_Y:
    :cvar VALUE_203_BS0105_Y:
    :cvar VALUE_203_BS0106_Y:
    :cvar VALUE_203_BS0107_Y:
    :cvar VALUE_203_BS0108_N:
    :cvar VALUE_203_BS0110_Y:
    :cvar VALUE_203_BS0111_Y:
    :cvar VALUE_203_BS0113_Y:
    :cvar VALUE_203_BS0114_N:
    :cvar VALUE_203_BS0115_N:
    :cvar VALUE_203_BS0116_N:
    :cvar VALUE_203_BS0117_N:
    :cvar VALUE_203_BS0119_N:
    :cvar VALUE_203_BS0130_Y:
    :cvar VALUE_203_BS0120_Y:
    :cvar VALUE_203_BS0121_Y:
    :cvar VALUE_203_BS0122_Y:
    :cvar VALUE_203_BS0125_Y:
    :cvar VALUE_203_BS0126_Y:
    :cvar VALUE_203_BS0127_N:
    :cvar VALUE_203_BS0128_Y:
    :cvar VALUE_203_BS0102_Y:
    :cvar VALUE_203_BT0100_N:
    :cvar VALUE_203_BT0000_Y:
    :cvar VALUE_203_BT0002_Y:
    :cvar VALUE_203_BT0001_Y:
    :cvar VALUE_203_BU0001_Y:
    :cvar VALUE_203_BU0300_Y:
    :cvar VALUE_203_BU0100_Y:
    """
    VALUE_203_B00000_N = "203B00000N"
    VALUE_203_BA0401_N = "203BA0401N"
    VALUE_203_BA0000_Y = "203BA0000Y"
    VALUE_203_BA0001_N = "203BA0001N"
    VALUE_203_BA0002_Y = "203BA0002Y"
    VALUE_203_BA0003_Y = "203BA0003Y"
    VALUE_203_BA0501_N = "203BA0501N"
    VALUE_203_BA0502_N = "203BA0502N"
    VALUE_203_BA0100_Y = "203BA0100Y"
    VALUE_203_BA0101_Y = "203BA0101Y"
    VALUE_203_BA0503_N = "203BA0503N"
    VALUE_203_BA0504_N = "203BA0504N"
    VALUE_203_BA0200_N = "203BA0200N"
    VALUE_203_BA0201_Y = "203BA0201Y"
    VALUE_203_BA0202_N = "203BA0202N"
    VALUE_203_BA0300_Y = "203BA0300Y"
    VALUE_203_BB0000_N = "203BB0000N"
    VALUE_203_BB0001_Y = "203BB0001Y"
    VALUE_203_BB0100_Y = "203BB0100Y"
    VALUE_203_BC0000_Y = "203BC0000Y"
    VALUE_203_BC0001_Y = "203BC0001Y"
    VALUE_203_BC0100_Y = "203BC0100Y"
    VALUE_203_BC2500_Y = "203BC2500Y"
    VALUE_203_BC0200_Y = "203BC0200Y"
    VALUE_203_BC0201_Y = "203BC0201Y"
    VALUE_203_BC0202_Y = "203BC0202Y"
    VALUE_203_BC0203_Y = "203BC0203Y"
    VALUE_203_BC0300_Y = "203BC0300Y"
    VALUE_203_BC0500_Y = "203BC0500Y"
    VALUE_203_BD0100_Y = "203BD0100Y"
    VALUE_203_BD0101_Y = "203BD0101Y"
    VALUE_203_BD0900_Y = "203BD0900Y"
    VALUE_203_BD0901_N = "203BD0901N"
    VALUE_203_BD0300_N = "203BD0300N"
    VALUE_203_BE0004_Y = "203BE0004Y"
    VALUE_203_BE0100_Y = "203BE0100Y"
    VALUE_203_BE0101_Y = "203BE0101Y"
    VALUE_203_BE0102_Y = "203BE0102Y"
    VALUE_203_BF0100_Y = "203BF0100Y"
    VALUE_203_BF0201_Y = "203BF0201Y"
    VALUE_203_BF0202_N = "203BF0202N"
    VALUE_203_BG0100_Y = "203BG0100Y"
    VALUE_203_BG0000_Y = "203BG0000Y"
    VALUE_203_BG0201_Y = "203BG0201Y"
    VALUE_203_BG0202_Y = "203BG0202Y"
    VALUE_203_BG0204_Y = "203BG0204Y"
    VALUE_203_BG0203_Y = "203BG0203Y"
    VALUE_203_BG0200_Y = "203BG0200Y"
    VALUE_203_BG0300_N = "203BG0300N"
    VALUE_203_BG0301_Y = "203BG0301Y"
    VALUE_203_BG0302_Y = "203BG0302Y"
    VALUE_203_BG0303_Y = "203BG0303Y"
    VALUE_203_BG0400_N = "203BG0400N"
    VALUE_203_BH0000_Y = "203BH0000Y"
    VALUE_203_BH0003_Y = "203BH0003Y"
    VALUE_203_BH0001_Y = "203BH0001Y"
    VALUE_203_BH0002_Y = "203BH0002Y"
    VALUE_203_BI0001_N = "203BI0001N"
    VALUE_203_BI0002_N = "203BI0002N"
    VALUE_203_BI0005_N = "203BI0005N"
    VALUE_203_BI0006_N = "203BI0006N"
    VALUE_203_BI0007_N = "203BI0007N"
    VALUE_203_BI0003_Y = "203BI0003Y"
    VALUE_203_BI0004_Y = "203BI0004Y"
    VALUE_203_BI0100_Y = "203BI0100Y"
    VALUE_203_BI0200_Y = "203BI0200Y"
    VALUE_203_BI0400_N = "203BI0400N"
    VALUE_203_BI0300_Y = "203BI0300Y"
    VALUE_203_BL0000_Y = "203BL0000Y"
    VALUE_203_BM0101_Y = "203BM0101Y"
    VALUE_203_BM0200_Y = "203BM0200Y"
    VALUE_203_BM0300_Y = "203BM0300Y"
    VALUE_203_BN0001_Y = "203BN0001Y"
    VALUE_203_BN0100_Y = "203BN0100Y"
    VALUE_203_BN0200_N = "203BN0200N"
    VALUE_203_BN0300_Y = "203BN0300Y"
    VALUE_203_BN0400_Y = "203BN0400Y"
    VALUE_203_BN0402_Y = "203BN0402Y"
    VALUE_203_BN0500_Y = "203BN0500Y"
    VALUE_203_BN0600_Y = "203BN0600Y"
    VALUE_203_BN0700_Y = "203BN0700Y"
    VALUE_203_BN0901_Y = "203BN0901Y"
    VALUE_203_BN0902_Y = "203BN0902Y"
    VALUE_203_BN0900_Y = "203BN0900Y"
    VALUE_203_BN0903_Y = "203BN0903Y"
    VALUE_203_BN0904_Y = "203BN0904Y"
    VALUE_203_BX0000_N = "203BX0000N"
    VALUE_203_BX0001_Y = "203BX0001Y"
    VALUE_203_BX0100_Y = "203BX0100Y"
    VALUE_203_BX0104_Y = "203BX0104Y"
    VALUE_203_BX0105_Y = "203BX0105Y"
    VALUE_203_BX0200_Y = "203BX0200Y"
    VALUE_203_BX0201_Y = "203BX0201Y"
    VALUE_203_BX0202_Y = "203BX0202Y"
    VALUE_203_BX0300_Y = "203BX0300Y"
    VALUE_203_BX0800_N = "203BX0800N"
    VALUE_203_BX2100_Y = "203BX2100Y"
    VALUE_203_BX0500_Y = "203BX0500Y"
    VALUE_203_BX0900_N = "203BX0900N"
    VALUE_203_BX0901_N = "203BX0901N"
    VALUE_203_BX0600_Y = "203BX0600Y"
    VALUE_203_BX0601_N = "203BX0601N"
    VALUE_203_BP0001_Y = "203BP0001Y"
    VALUE_203_BP2900_N = "203BP2900N"
    VALUE_203_BP0100_Y = "203BP0100Y"
    VALUE_203_BP0101_Y = "203BP0101Y"
    VALUE_203_BP0102_Y = "203BP0102Y"
    VALUE_203_BP0103_Y = "203BP0103Y"
    VALUE_203_BP0104_Y = "203BP0104Y"
    VALUE_203_BP0105_Y = "203BP0105Y"
    VALUE_203_BP0107_N = "203BP0107N"
    VALUE_203_BP0201_Y = "203BP0201Y"
    VALUE_203_BP0202_Y = "203BP0202Y"
    VALUE_203_BP0203_Y = "203BP0203Y"
    VALUE_203_BP0204_Y = "203BP0204Y"
    VALUE_203_BP0205_Y = "203BP0205Y"
    VALUE_203_BP0206_Y = "203BP0206Y"
    VALUE_203_BP0207_Y = "203BP0207Y"
    VALUE_203_BP0208_Y = "203BP0208Y"
    VALUE_203_BP0209_Y = "203BP0209Y"
    VALUE_203_BP0220_N = "203BP0220N"
    VALUE_203_BP0210_Y = "203BP0210Y"
    VALUE_203_BP0211_Y = "203BP0211Y"
    VALUE_203_BP0212_Y = "203BP0212Y"
    VALUE_203_BP0213_Y = "203BP0213Y"
    VALUE_203_BP0214_Y = "203BP0214Y"
    VALUE_203_BP0215_N = "203BP0215N"
    VALUE_203_BP0216_Y = "203BP0216Y"
    VALUE_203_BP0200_Y = "203BP0200Y"
    VALUE_203_BP2600_N = "203BP2600N"
    VALUE_203_BP1200_N = "203BP1200N"
    VALUE_203_BP0400_Y = "203BP0400Y"
    VALUE_203_BP0500_Y = "203BP0500Y"
    VALUE_203_BP0600_Y = "203BP0600Y"
    VALUE_203_BP0800_Y = "203BP0800Y"
    VALUE_203_BP0801_Y = "203BP0801Y"
    VALUE_203_BP0802_Y = "203BP0802Y"
    VALUE_203_BP0803_Y = "203BP0803Y"
    VALUE_203_BP0804_Y = "203BP0804Y"
    VALUE_203_BP0805_Y = "203BP0805Y"
    VALUE_203_BP0806_N = "203BP0806N"
    VALUE_203_BP1300_N = "203BP1300N"
    VALUE_203_BP0901_N = "203BP0901N"
    VALUE_203_BP0903_Y = "203BP0903Y"
    VALUE_203_BP1001_Y = "203BP1001Y"
    VALUE_203_BP1003_Y = "203BP1003Y"
    VALUE_203_BR0001_Y = "203BR0001Y"
    VALUE_203_BR0002_Y = "203BR0002Y"
    VALUE_203_BR0205_N = "203BR0205N"
    VALUE_203_BR0200_Y = "203BR0200Y"
    VALUE_203_BR0201_Y = "203BR0201Y"
    VALUE_203_BR0202_Y = "203BR0202Y"
    VALUE_203_BR0203_N = "203BR0203N"
    VALUE_203_BR0204_N = "203BR0204N"
    VALUE_203_BR0300_N = "203BR0300N"
    VALUE_203_BR0402_Y = "203BR0402Y"
    VALUE_203_BR0500_Y = "203BR0500Y"
    VALUE_203_BR0600_N = "203BR0600N"
    VALUE_203_BR0700_Y = "203BR0700Y"
    VALUE_203_BR0701_Y = "203BR0701Y"
    VALUE_203_BS0000_Y = "203BS0000Y"
    VALUE_203_BS0001_Y = "203BS0001Y"
    VALUE_203_BS0002_Y = "203BS0002Y"
    VALUE_203_BS0003_Y = "203BS0003Y"
    VALUE_203_BS0004_Y = "203BS0004Y"
    VALUE_203_BS0104_N = "203BS0104N"
    VALUE_203_BS0133_N = "203BS0133N"
    VALUE_203_BS0101_Y = "203BS0101Y"
    VALUE_203_BS0123_Y = "203BS0123Y"
    VALUE_203_BS0100_Y = "203BS0100Y"
    VALUE_203_BS0129_Y = "203BS0129Y"
    VALUE_203_BS0105_Y = "203BS0105Y"
    VALUE_203_BS0106_Y = "203BS0106Y"
    VALUE_203_BS0107_Y = "203BS0107Y"
    VALUE_203_BS0108_N = "203BS0108N"
    VALUE_203_BS0110_Y = "203BS0110Y"
    VALUE_203_BS0111_Y = "203BS0111Y"
    VALUE_203_BS0113_Y = "203BS0113Y"
    VALUE_203_BS0114_N = "203BS0114N"
    VALUE_203_BS0115_N = "203BS0115N"
    VALUE_203_BS0116_N = "203BS0116N"
    VALUE_203_BS0117_N = "203BS0117N"
    VALUE_203_BS0119_N = "203BS0119N"
    VALUE_203_BS0130_Y = "203BS0130Y"
    VALUE_203_BS0120_Y = "203BS0120Y"
    VALUE_203_BS0121_Y = "203BS0121Y"
    VALUE_203_BS0122_Y = "203BS0122Y"
    VALUE_203_BS0125_Y = "203BS0125Y"
    VALUE_203_BS0126_Y = "203BS0126Y"
    VALUE_203_BS0127_N = "203BS0127N"
    VALUE_203_BS0128_Y = "203BS0128Y"
    VALUE_203_BS0102_Y = "203BS0102Y"
    VALUE_203_BT0100_N = "203BT0100N"
    VALUE_203_BT0000_Y = "203BT0000Y"
    VALUE_203_BT0002_Y = "203BT0002Y"
    VALUE_203_BT0001_Y = "203BT0001Y"
    VALUE_203_BU0001_Y = "203BU0001Y"
    VALUE_203_BU0300_Y = "203BU0300Y"
    VALUE_203_BU0100_Y = "203BU0100Y"


class PhysicianAssistantHipaa(Enum):
    """
    specDomain: S13422 (C-0-T13129-A13130-A13363-S13422-cpt)
    :cvar VALUE_363_A00000_N:
    :cvar VALUE_363_AM0700_N:
    :cvar VALUE_363_AS0400_N:
    """
    VALUE_363_A00000_N = "363A00000N"
    VALUE_363_AM0700_N = "363AM0700N"
    VALUE_363_AS0400_N = "363AS0400N"


class PhysicianAssistantProviderCodes(Enum):
    """
    specDomain: S20519 (C-0-T19465-S20463-S20501-S20519-cpt)
    :cvar VALUE_363_A00000_X:
    :cvar VALUE_363_AM0700_X:
    :cvar VALUE_363_AS0400_X:
    """
    VALUE_363_A00000_X = "363A00000X"
    VALUE_363_AM0700_X = "363AM0700X"
    VALUE_363_AS0400_X = "363AS0400X"


class PhysicianAssistantsAndOrAdvancedPracticeNursingProviderHipaa(Enum):
    """
    abstDomain: A13363 (C-0-T13129-A13130-A13363-cpt)
    :cvar VALUE_364_S00000_N:
    :cvar VALUE_364_SA2100_N:
    :cvar VALUE_364_SA2200_N:
    :cvar VALUE_364_SC2300_N:
    :cvar VALUE_364_SC1501_N:
    :cvar VALUE_364_SC0200_N:
    :cvar VALUE_364_SE0003_N:
    :cvar VALUE_364_SE1400_N:
    :cvar VALUE_364_SF0001_N:
    :cvar VALUE_364_SG0600_N:
    :cvar VALUE_364_SH1100_N:
    :cvar VALUE_364_SH0200_N:
    :cvar VALUE_364_SI0800_N:
    :cvar VALUE_364_SL0600_N:
    :cvar VALUE_364_SM0705_N:
    :cvar VALUE_364_SN0000_N:
    :cvar VALUE_364_SN0004_N:
    :cvar VALUE_364_SN0800_N:
    :cvar VALUE_364_SX0106_N:
    :cvar VALUE_364_SX0200_N:
    :cvar VALUE_364_SX0204_N:
    :cvar VALUE_364_SP0200_N:
    :cvar VALUE_364_SP1700_N:
    :cvar VALUE_364_SP2800_N:
    :cvar VALUE_364_SP0807_N:
    :cvar VALUE_364_SP0808_N:
    :cvar VALUE_364_SP0809_N:
    :cvar VALUE_364_SP0810_N:
    :cvar VALUE_364_SP0811_N:
    :cvar VALUE_364_SP0812_N:
    :cvar VALUE_364_SP0813_N:
    :cvar VALUE_364_SR0400_N:
    :cvar VALUE_364_SR1300_N:
    :cvar VALUE_364_SS0200_N:
    :cvar VALUE_364_ST0500_N:
    :cvar VALUE_364_SW0102_N:
    :cvar VALUE_363_L00000_N:
    :cvar VALUE_363_LA2100_N:
    :cvar VALUE_363_LA2200_N:
    :cvar VALUE_363_LC1500_N:
    :cvar VALUE_363_LC0200_N:
    :cvar VALUE_363_LF0000_N:
    :cvar VALUE_363_LG0600_N:
    :cvar VALUE_363_LN0000_N:
    :cvar VALUE_363_LN0005_N:
    :cvar VALUE_363_LX0001_N:
    :cvar VALUE_363_LX0106_N:
    :cvar VALUE_363_LP0200_N:
    :cvar VALUE_363_LP0223_N:
    :cvar VALUE_363_LP0222_N:
    :cvar VALUE_363_LP1700_N:
    :cvar VALUE_363_LP2300_N:
    :cvar VALUE_363_LP0808_N:
    :cvar VALUE_363_LS0200_N:
    :cvar VALUE_363_LW0102_N:
    :cvar VALUE_363_A00000_N:
    :cvar VALUE_363_AM0700_N:
    :cvar VALUE_363_AS0400_N:
    :cvar VALUE_366_B00000_N:
    :cvar VALUE_367500000_N:
    """
    VALUE_364_S00000_N = "364S00000N"
    VALUE_364_SA2100_N = "364SA2100N"
    VALUE_364_SA2200_N = "364SA2200N"
    VALUE_364_SC2300_N = "364SC2300N"
    VALUE_364_SC1501_N = "364SC1501N"
    VALUE_364_SC0200_N = "364SC0200N"
    VALUE_364_SE0003_N = "364SE0003N"
    VALUE_364_SE1400_N = "364SE1400N"
    VALUE_364_SF0001_N = "364SF0001N"
    VALUE_364_SG0600_N = "364SG0600N"
    VALUE_364_SH1100_N = "364SH1100N"
    VALUE_364_SH0200_N = "364SH0200N"
    VALUE_364_SI0800_N = "364SI0800N"
    VALUE_364_SL0600_N = "364SL0600N"
    VALUE_364_SM0705_N = "364SM0705N"
    VALUE_364_SN0000_N = "364SN0000N"
    VALUE_364_SN0004_N = "364SN0004N"
    VALUE_364_SN0800_N = "364SN0800N"
    VALUE_364_SX0106_N = "364SX0106N"
    VALUE_364_SX0200_N = "364SX0200N"
    VALUE_364_SX0204_N = "364SX0204N"
    VALUE_364_SP0200_N = "364SP0200N"
    VALUE_364_SP1700_N = "364SP1700N"
    VALUE_364_SP2800_N = "364SP2800N"
    VALUE_364_SP0807_N = "364SP0807N"
    VALUE_364_SP0808_N = "364SP0808N"
    VALUE_364_SP0809_N = "364SP0809N"
    VALUE_364_SP0810_N = "364SP0810N"
    VALUE_364_SP0811_N = "364SP0811N"
    VALUE_364_SP0812_N = "364SP0812N"
    VALUE_364_SP0813_N = "364SP0813N"
    VALUE_364_SR0400_N = "364SR0400N"
    VALUE_364_SR1300_N = "364SR1300N"
    VALUE_364_SS0200_N = "364SS0200N"
    VALUE_364_ST0500_N = "364ST0500N"
    VALUE_364_SW0102_N = "364SW0102N"
    VALUE_363_L00000_N = "363L00000N"
    VALUE_363_LA2100_N = "363LA2100N"
    VALUE_363_LA2200_N = "363LA2200N"
    VALUE_363_LC1500_N = "363LC1500N"
    VALUE_363_LC0200_N = "363LC0200N"
    VALUE_363_LF0000_N = "363LF0000N"
    VALUE_363_LG0600_N = "363LG0600N"
    VALUE_363_LN0000_N = "363LN0000N"
    VALUE_363_LN0005_N = "363LN0005N"
    VALUE_363_LX0001_N = "363LX0001N"
    VALUE_363_LX0106_N = "363LX0106N"
    VALUE_363_LP0200_N = "363LP0200N"
    VALUE_363_LP0223_N = "363LP0223N"
    VALUE_363_LP0222_N = "363LP0222N"
    VALUE_363_LP1700_N = "363LP1700N"
    VALUE_363_LP2300_N = "363LP2300N"
    VALUE_363_LP0808_N = "363LP0808N"
    VALUE_363_LS0200_N = "363LS0200N"
    VALUE_363_LW0102_N = "363LW0102N"
    VALUE_363_A00000_N = "363A00000N"
    VALUE_363_AM0700_N = "363AM0700N"
    VALUE_363_AS0400_N = "363AS0400N"
    VALUE_366_B00000_N = "366B00000N"
    VALUE_367500000_N = "367500000N"


class PhysicianAssistantsandAdvancedPracticeNursingProvidersProviderCodes(Enum):
    """
    specDomain: S20463 (C-0-T19465-S20463-cpt)
    :cvar VALUE_364_S00000_X:
    :cvar VALUE_364_SA2100_X:
    :cvar VALUE_364_SA2200_X:
    :cvar VALUE_364_SC2300_X:
    :cvar VALUE_364_SC1501_X:
    :cvar VALUE_364_SC0200_X:
    :cvar VALUE_364_SE0003_X:
    :cvar VALUE_364_SE1400_X:
    :cvar VALUE_364_SF0001_X:
    :cvar VALUE_364_SG0600_X:
    :cvar VALUE_364_SH1100_X:
    :cvar VALUE_364_SH0200_X:
    :cvar VALUE_364_SI0800_X:
    :cvar VALUE_364_SL0600_X:
    :cvar VALUE_364_SM0705_X:
    :cvar VALUE_364_SN0000_X:
    :cvar VALUE_364_SN0800_X:
    :cvar VALUE_364_SX0106_X:
    :cvar VALUE_364_SX0200_X:
    :cvar VALUE_364_SX0204_X:
    :cvar VALUE_364_SP0200_X:
    :cvar VALUE_364_SP1700_X:
    :cvar VALUE_364_SP2800_X:
    :cvar VALUE_364_SP0808_X:
    :cvar VALUE_364_SP0809_X:
    :cvar VALUE_364_SP0807_X:
    :cvar VALUE_364_SP0810_X:
    :cvar VALUE_364_SP0811_X:
    :cvar VALUE_364_SP0812_X:
    :cvar VALUE_364_SP0813_X:
    :cvar VALUE_364_SR0400_X:
    :cvar VALUE_364_SS0200_X:
    :cvar VALUE_364_ST0500_X:
    :cvar VALUE_364_SW0102_X:
    :cvar VALUE_363_A00000_X:
    :cvar VALUE_363_AM0700_X:
    :cvar VALUE_363_AS0400_X:
    :cvar VALUE_363_L00000_X:
    :cvar VALUE_363_LA2100_X:
    :cvar VALUE_363_LA2200_X:
    :cvar VALUE_363_LC1500_X:
    :cvar VALUE_363_LC0200_X:
    :cvar VALUE_363_LF0000_X:
    :cvar VALUE_363_LG0600_X:
    :cvar VALUE_363_LN0000_X:
    :cvar VALUE_363_LN0005_X:
    :cvar VALUE_363_LX0001_X:
    :cvar VALUE_363_LX0106_X:
    :cvar VALUE_363_LP0200_X:
    :cvar VALUE_363_LP0222_X:
    :cvar VALUE_363_LP1700_X:
    :cvar VALUE_363_LP2300_X:
    :cvar VALUE_363_LP0808_X:
    :cvar VALUE_363_LS0200_X:
    :cvar VALUE_363_LW0102_X:
    :cvar VALUE_360000000_X:
    :cvar VALUE_367_H00000_X:
    :cvar VALUE_367_A00000_X:
    :cvar VALUE_367500000_X:
    """
    VALUE_364_S00000_X = "364S00000X"
    VALUE_364_SA2100_X = "364SA2100X"
    VALUE_364_SA2200_X = "364SA2200X"
    VALUE_364_SC2300_X = "364SC2300X"
    VALUE_364_SC1501_X = "364SC1501X"
    VALUE_364_SC0200_X = "364SC0200X"
    VALUE_364_SE0003_X = "364SE0003X"
    VALUE_364_SE1400_X = "364SE1400X"
    VALUE_364_SF0001_X = "364SF0001X"
    VALUE_364_SG0600_X = "364SG0600X"
    VALUE_364_SH1100_X = "364SH1100X"
    VALUE_364_SH0200_X = "364SH0200X"
    VALUE_364_SI0800_X = "364SI0800X"
    VALUE_364_SL0600_X = "364SL0600X"
    VALUE_364_SM0705_X = "364SM0705X"
    VALUE_364_SN0000_X = "364SN0000X"
    VALUE_364_SN0800_X = "364SN0800X"
    VALUE_364_SX0106_X = "364SX0106X"
    VALUE_364_SX0200_X = "364SX0200X"
    VALUE_364_SX0204_X = "364SX0204X"
    VALUE_364_SP0200_X = "364SP0200X"
    VALUE_364_SP1700_X = "364SP1700X"
    VALUE_364_SP2800_X = "364SP2800X"
    VALUE_364_SP0808_X = "364SP0808X"
    VALUE_364_SP0809_X = "364SP0809X"
    VALUE_364_SP0807_X = "364SP0807X"
    VALUE_364_SP0810_X = "364SP0810X"
    VALUE_364_SP0811_X = "364SP0811X"
    VALUE_364_SP0812_X = "364SP0812X"
    VALUE_364_SP0813_X = "364SP0813X"
    VALUE_364_SR0400_X = "364SR0400X"
    VALUE_364_SS0200_X = "364SS0200X"
    VALUE_364_ST0500_X = "364ST0500X"
    VALUE_364_SW0102_X = "364SW0102X"
    VALUE_363_A00000_X = "363A00000X"
    VALUE_363_AM0700_X = "363AM0700X"
    VALUE_363_AS0400_X = "363AS0400X"
    VALUE_363_L00000_X = "363L00000X"
    VALUE_363_LA2100_X = "363LA2100X"
    VALUE_363_LA2200_X = "363LA2200X"
    VALUE_363_LC1500_X = "363LC1500X"
    VALUE_363_LC0200_X = "363LC0200X"
    VALUE_363_LF0000_X = "363LF0000X"
    VALUE_363_LG0600_X = "363LG0600X"
    VALUE_363_LN0000_X = "363LN0000X"
    VALUE_363_LN0005_X = "363LN0005X"
    VALUE_363_LX0001_X = "363LX0001X"
    VALUE_363_LX0106_X = "363LX0106X"
    VALUE_363_LP0200_X = "363LP0200X"
    VALUE_363_LP0222_X = "363LP0222X"
    VALUE_363_LP1700_X = "363LP1700X"
    VALUE_363_LP2300_X = "363LP2300X"
    VALUE_363_LP0808_X = "363LP0808X"
    VALUE_363_LS0200_X = "363LS0200X"
    VALUE_363_LW0102_X = "363LW0102X"
    VALUE_360000000_X = "360000000X"
    VALUE_367_H00000_X = "367H00000X"
    VALUE_367_A00000_X = "367A00000X"
    VALUE_367500000_X = "367500000X"


class Pidgin(Enum):
    """
    abstDomain: A18518 (C-0-T18130-A18518-cpt)
    :cvar X_CHH:
    """
    X_CHH = "x-CHH"


class PillDrugForm(Enum):
    """
    specDomain: S14506 (C-0-T19651-A14411-A14412-A14484-S14506-cpt)
    :cvar ENTCAP:
    :cvar ERENTCAP:
    :cvar ERCAP:
    :cvar ERCAP12:
    :cvar ERCAP24:
    :cvar ERECCAP:
    :cvar ORCAP:
    :cvar CAP:
    :cvar BUCTAB:
    :cvar SRBUCTAB:
    :cvar ECTAB:
    :cvar ERECTAB:
    :cvar ERTAB:
    :cvar ERTAB12:
    :cvar ERTAB24:
    :cvar ORTAB:
    :cvar CAPLET:
    :cvar CHEWTAB:
    :cvar CPTAB:
    :cvar DRTAB:
    :cvar DISINTAB:
    :cvar ORTROCHE:
    :cvar SLTAB:
    :cvar TAB:
    :cvar VAGTAB:
    :cvar PILL:
    """
    ENTCAP = "ENTCAP"
    ERENTCAP = "ERENTCAP"
    ERCAP = "ERCAP"
    ERCAP12 = "ERCAP12"
    ERCAP24 = "ERCAP24"
    ERECCAP = "ERECCAP"
    ORCAP = "ORCAP"
    CAP = "CAP"
    BUCTAB = "BUCTAB"
    SRBUCTAB = "SRBUCTAB"
    ECTAB = "ECTAB"
    ERECTAB = "ERECTAB"
    ERTAB = "ERTAB"
    ERTAB12 = "ERTAB12"
    ERTAB24 = "ERTAB24"
    ORTAB = "ORTAB"
    CAPLET = "CAPLET"
    CHEWTAB = "CHEWTAB"
    CPTAB = "CPTAB"
    DRTAB = "DRTAB"
    DISINTAB = "DISINTAB"
    ORTROCHE = "ORTROCHE"
    SLTAB = "SLTAB"
    TAB = "TAB"
    VAGTAB = "VAGTAB"
    PILL = "PILL"


class PlasticBottleEntityType(Enum):
    """
    specDomain: S16159 (C-0-T16040-A16041-A19867-A16143-S16144-A16152-A16153-S16155-S16159-cpt)
    :cvar BOTP:
    :cvar BOTPLY:
    """
    BOTP = "BOTP"
    BOTPLY = "BOTPLY"


class PlasticSurgeryProviderCodes(Enum):
    """
    specDomain: S20228 (C-0-T19465-S20096-S20228-cpt)
    :cvar VALUE_208200000_X:
    :cvar VALUE_2082_S0099_X:
    :cvar VALUE_2082_S0105_X:
    """
    VALUE_208200000_X = "208200000X"
    VALUE_2082_S0099_X = "2082S0099X"
    VALUE_2082_S0105_X = "2082S0105X"


class PlateauPenutian(Enum):
    """
    abstDomain: A18498 (C-0-T18130-A18413-A18498-cpt)
    :cvar X_WAR:
    :cvar X_UMA:
    :cvar X_WAA:
    :cvar X_YAK:
    :cvar X_KLA:
    :cvar X_NEZ:
    """
    X_WAR = "x-WAR"
    X_UMA = "x-UMA"
    X_WAA = "x-WAA"
    X_YAK = "x-YAK"
    X_KLA = "x-KLA"
    X_NEZ = "x-NEZ"


class PodiatricMedicineAndOrSurgeryServiceProviderHipaa(Enum):
    """
    abstDomain: A13582 (C-0-T13129-A13130-A13582-cpt)
    :cvar VALUE_213_E00000_N:
    :cvar VALUE_213_EG0000_N:
    :cvar VALUE_213_EP0504_N:
    :cvar VALUE_213_EP1101_N:
    :cvar VALUE_213_ER0200_N:
    :cvar VALUE_213_ES0000_N:
    :cvar VALUE_213_ES0131_N:
    :cvar VALUE_213_ES0103_N:
    :cvar VALUE_211_D00000_N:
    """
    VALUE_213_E00000_N = "213E00000N"
    VALUE_213_EG0000_N = "213EG0000N"
    VALUE_213_EP0504_N = "213EP0504N"
    VALUE_213_EP1101_N = "213EP1101N"
    VALUE_213_ER0200_N = "213ER0200N"
    VALUE_213_ES0000_N = "213ES0000N"
    VALUE_213_ES0131_N = "213ES0131N"
    VALUE_213_ES0103_N = "213ES0103N"
    VALUE_211_D00000_N = "211D00000N"


class PodiatricMedicineandSurgeryProvidersProviderCodes(Enum):
    """
    specDomain: S20522 (C-0-T19465-S20522-cpt)
    :cvar VALUE_213_E00000_X:
    :cvar VALUE_213_EG0000_X:
    :cvar VALUE_213_EP1101_X:
    :cvar VALUE_213_EP0504_X:
    :cvar VALUE_213_ER0200_X:
    :cvar VALUE_213_ES0000_X:
    :cvar VALUE_213_ES0131_X:
    :cvar VALUE_213_ES0103_X:
    :cvar VALUE_210000000_X:
    :cvar VALUE_211_D00000_X:
    """
    VALUE_213_E00000_X = "213E00000X"
    VALUE_213_EG0000_X = "213EG0000X"
    VALUE_213_EP1101_X = "213EP1101X"
    VALUE_213_EP0504_X = "213EP0504X"
    VALUE_213_ER0200_X = "213ER0200X"
    VALUE_213_ES0000_X = "213ES0000X"
    VALUE_213_ES0131_X = "213ES0131X"
    VALUE_213_ES0103_X = "213ES0103X"
    VALUE_210000000_X = "210000000X"
    VALUE_211_D00000_X = "211D00000X"


class PodiatristHipaa(Enum):
    """
    specDomain: S13584 (C-0-T13129-A13130-A13582-S13584-cpt)
    :cvar VALUE_213_E00000_N:
    :cvar VALUE_213_EG0000_N:
    :cvar VALUE_213_EP0504_N:
    :cvar VALUE_213_EP1101_N:
    :cvar VALUE_213_ER0200_N:
    :cvar VALUE_213_ES0000_N:
    :cvar VALUE_213_ES0131_N:
    :cvar VALUE_213_ES0103_N:
    """
    VALUE_213_E00000_N = "213E00000N"
    VALUE_213_EG0000_N = "213EG0000N"
    VALUE_213_EP0504_N = "213EP0504N"
    VALUE_213_EP1101_N = "213EP1101N"
    VALUE_213_ER0200_N = "213ER0200N"
    VALUE_213_ES0000_N = "213ES0000N"
    VALUE_213_ES0131_N = "213ES0131N"
    VALUE_213_ES0103_N = "213ES0103N"


class PodiatristProviderCodes(Enum):
    """
    specDomain: S20524 (C-0-T19465-S20522-S20524-cpt)
    :cvar VALUE_213_E00000_X:
    :cvar VALUE_213_EG0000_X:
    :cvar VALUE_213_EP1101_X:
    :cvar VALUE_213_EP0504_X:
    :cvar VALUE_213_ER0200_X:
    :cvar VALUE_213_ES0000_X:
    :cvar VALUE_213_ES0131_X:
    :cvar VALUE_213_ES0103_X:
    """
    VALUE_213_E00000_X = "213E00000X"
    VALUE_213_EG0000_X = "213EG0000X"
    VALUE_213_EP1101_X = "213EP1101X"
    VALUE_213_EP0504_X = "213EP0504X"
    VALUE_213_ER0200_X = "213ER0200X"
    VALUE_213_ES0000_X = "213ES0000X"
    VALUE_213_ES0131_X = "213ES0131X"
    VALUE_213_ES0103_X = "213ES0103X"


class Pomoan(Enum):
    """
    abstDomain: A18253 (C-0-T18130-A18241-A18253-cpt)
    :cvar X_POO:
    :cvar X_KJU:
    :cvar X_PEF:
    :cvar X_PEO:
    :cvar X_PEQ:
    """
    X_POO = "x-POO"
    X_KJU = "x-KJU"
    X_PEF = "x-PEF"
    X_PEO = "x-PEO"
    X_PEQ = "x-PEQ"


class Position(Enum):
    """
    specDomain: S21646 (C-0-T11527-S13856-A19822-S11529-S21646-cpt)
    :cvar POS:
    :cvar POSACC:
    :cvar POSCOORD:
    """
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"


class PostalAddressUse(Enum):
    """
    vocSet: T10637 (C-0-T10637-cpt)
    :cvar H:
    :cvar HP:
    :cvar HV:
    :cvar WP:
    :cvar DIR:
    :cvar PUB:
    :cvar BAD:
    :cvar TMP:
    :cvar ABC:
    :cvar IDE:
    :cvar SYL:
    :cvar PHYS:
    :cvar PST:
    """
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    PHYS = "PHYS"
    PST = "PST"


class PowderDrugForm(Enum):
    """
    specDomain: S14534 (C-0-T19651-A14411-A14412-A14484-S14534-cpt)
    :cvar TOPPWD:
    :cvar RECPWD:
    :cvar VAGPWD:
    :cvar POWD:
    """
    TOPPWD = "TOPPWD"
    RECPWD = "RECPWD"
    VAGPWD = "VAGPWD"
    POWD = "POWD"


class PowerOfAttorney(Enum):
    """
    specDomain: S22034 (C-0-T12206-A19690-S22030-S22034-cpt)
    :cvar POWATT:
    :cvar DPOWATT:
    :cvar HPOWATT:
    :cvar SPOWATT:
    """
    POWATT = "POWATT"
    DPOWATT = "DPOWATT"
    HPOWATT = "HPOWATT"
    SPOWATT = "SPOWATT"


class PrescriptionDispenseFilterCode(Enum):
    """
    abstDomain: A19727 (C-0-T19726-A19727-cpt)
    :cvar C:
    :cvar R:
    :cvar N:
    """
    C = "C"
    R = "R"
    N = "N"


class PreventiveMedicineProviderCodes(Enum):
    """
    specDomain: S20231 (C-0-T19465-S20096-S20231-cpt)
    :cvar VALUE_208300000_X:
    :cvar VALUE_2083_A0100_X:
    :cvar VALUE_2083_T0002_X:
    :cvar VALUE_2083_X0100_X:
    :cvar VALUE_2083_P0500_X:
    :cvar VALUE_2083_P0901_X:
    :cvar VALUE_2083_S0010_X:
    :cvar VALUE_2083_P0011_X:
    """
    VALUE_208300000_X = "208300000X"
    VALUE_2083_A0100_X = "2083A0100X"
    VALUE_2083_T0002_X = "2083T0002X"
    VALUE_2083_X0100_X = "2083X0100X"
    VALUE_2083_P0500_X = "2083P0500X"
    VALUE_2083_P0901_X = "2083P0901X"
    VALUE_2083_S0010_X = "2083S0010X"
    VALUE_2083_P0011_X = "2083P0011X"


class PrimaryDentition(Enum):
    """
    abstDomain: A19344 (C-0-T16537-A16538-A19346-A19344-cpt)
    :cvar TIDA:
    :cvar TIDB:
    :cvar TIDC:
    :cvar TIDD:
    :cvar TIDE:
    :cvar TIDF:
    :cvar TIDG:
    :cvar TIDH:
    :cvar TIDI:
    :cvar TIDJ:
    :cvar TIDK:
    :cvar TIDL:
    :cvar TIDM:
    :cvar TIDN:
    :cvar TIDO:
    :cvar TIDP:
    :cvar TIDQ:
    :cvar TIDR:
    :cvar TIDS:
    :cvar TIDT:
    """
    TIDA = "TIDA"
    TIDB = "TIDB"
    TIDC = "TIDC"
    TIDD = "TIDD"
    TIDE = "TIDE"
    TIDF = "TIDF"
    TIDG = "TIDG"
    TIDH = "TIDH"
    TIDI = "TIDI"
    TIDJ = "TIDJ"
    TIDK = "TIDK"
    TIDL = "TIDL"
    TIDM = "TIDM"
    TIDN = "TIDN"
    TIDO = "TIDO"
    TIDP = "TIDP"
    TIDQ = "TIDQ"
    TIDR = "TIDR"
    TIDS = "TIDS"
    TIDT = "TIDT"


class PrivateResidence(Enum):
    """
    specDomain: S22190 (C-0-T220-S22190-cpt)
    :cvar PR:
    :cvar H:
    :cvar R:
    :cvar SL:
    """
    PR = "PR"
    H = "H"
    R = "R"
    SL = "SL"


class ProbabilityDistributionType(Enum):
    """
    vocSet: T10747 (C-0-T10747-cpt)
    :cvar G:
    :cvar F:
    :cvar T:
    :cvar B:
    :cvar X2:
    :cvar E:
    :cvar LN:
    :cvar N:
    :cvar U:
    """
    G = "G"
    F = "F"
    T = "T"
    B = "B"
    X2 = "X2"
    E = "E"
    LN = "LN"
    N = "N"
    U = "U"


class ProcessingId(Enum):
    """
    vocSet: T103 (C-0-T103-cpt)
    :cvar D:
    :cvar P:
    :cvar T:
    """
    D = "D"
    P = "P"
    T = "T"


class ProcessingMode(Enum):
    """
    vocSet: T207 (C-0-T207-cpt)
    :cvar A:
    :cvar T:
    :cvar I:
    :cvar R:
    """
    A = "A"
    T = "T"
    I = "I"
    R = "R"


class ProgramEligibleCoveredPartyRoleType(Enum):
    """
    abstDomain: A19811 (C-0-T12206-A19809-A19805-A19811-cpt)
    :cvar MIL:
    :cvar ACTMIL:
    :cvar RETMIL:
    :cvar VET:
    :cvar CRIMEVIC:
    :cvar DIFFABL:
    :cvar INJWKR:
    :cvar INDIG:
    :cvar WARD:
    """
    MIL = "MIL"
    ACTMIL = "ACTMIL"
    RETMIL = "RETMIL"
    VET = "VET"
    CRIMEVIC = "CRIMEVIC"
    DIFFABL = "DIFFABL"
    INJWKR = "INJWKR"
    INDIG = "INDIG"
    WARD = "WARD"


class Prosthodontics(Enum):
    """
    abstDomain: A13195 (C-0-T13129-A13130-A16460-S13188-A13195-cpt)
    :cvar VALUE_1327_D0700_N:
    """
    VALUE_1327_D0700_N = "1327D0700N"


class ProviderCodes(Enum):
    """
    vocSet: T19465 (C-0-T19465-cpt)
    :cvar VALUE_250000000_X:
    :cvar VALUE_251_B00000_X:
    :cvar VALUE_251_C00000_X:
    :cvar VALUE_251_E00000_X:
    :cvar VALUE_251_F00000_X:
    :cvar VALUE_251_G00000_X:
    :cvar VALUE_251_J00000_X:
    :cvar VALUE_251_K00000_X:
    :cvar VALUE_251_V00000_X:
    :cvar VALUE_207_K00000_X:
    :cvar VALUE_207_KA0200_X:
    :cvar VALUE_207_KI0005_X:
    :cvar VALUE_207_L00000_X:
    :cvar VALUE_207_LA0401_X:
    :cvar VALUE_207_LC0200_X:
    :cvar VALUE_207_LP2900_X:
    :cvar VALUE_207_N00000_X:
    :cvar VALUE_207_NI0002_X:
    :cvar VALUE_207_NS0135_X:
    :cvar VALUE_207_ND0900_X:
    :cvar VALUE_207_ND0101_X:
    :cvar VALUE_207_NP0225_X:
    :cvar VALUE_207_P00000_X:
    :cvar VALUE_207_PE0004_X:
    :cvar VALUE_207_PT0002_X:
    :cvar VALUE_207_PP0204_X:
    :cvar VALUE_207_PS0010_X:
    :cvar VALUE_207_PE0005_X:
    :cvar VALUE_207_Q00000_X:
    :cvar VALUE_207_QA0401_X:
    :cvar VALUE_207_QA0000_X:
    :cvar VALUE_207_QA0505_X:
    :cvar VALUE_207_QG0300_X:
    :cvar VALUE_207_QS0010_X:
    :cvar VALUE_207_R00000_X:
    :cvar VALUE_207_RA0401_X:
    :cvar VALUE_207_RA0000_X:
    :cvar VALUE_207_RA0201_X:
    :cvar VALUE_207_RC0000_X:
    :cvar VALUE_207_RI0001_X:
    :cvar VALUE_207_RC0001_X:
    :cvar VALUE_207_RC0200_X:
    :cvar VALUE_207_RE0101_X:
    :cvar VALUE_207_RG0100_X:
    :cvar VALUE_207_RG0300_X:
    :cvar VALUE_207_RH0000_X:
    :cvar VALUE_207_RH0003_X:
    :cvar VALUE_207_RI0008_X:
    :cvar VALUE_207_RI0200_X:
    :cvar VALUE_207_RI0011_X:
    :cvar VALUE_207_RM1200_X:
    :cvar VALUE_207_RX0202_X:
    :cvar VALUE_207_RN0300_X:
    :cvar VALUE_207_RP1001_X:
    :cvar VALUE_207_RR0500_X:
    :cvar VALUE_207_RS0010_X:
    :cvar VALUE_207_S00000_X:
    :cvar VALUE_207_SG0202_X:
    :cvar VALUE_207_SC0300_X:
    :cvar VALUE_207_SG0201_X:
    :cvar VALUE_207_SG0203_X:
    :cvar VALUE_207_SM0001_X:
    :cvar VALUE_207_SG0205_X:
    :cvar VALUE_207_U00000_X:
    :cvar VALUE_207_UN0903_X:
    :cvar VALUE_207_UN0901_X:
    :cvar VALUE_207_UN0902_X:
    :cvar VALUE_207_V00000_X:
    :cvar VALUE_207_VC0200_X:
    :cvar VALUE_207_VX0201_X:
    :cvar VALUE_207_VG0400_X:
    :cvar VALUE_207_VM0101_X:
    :cvar VALUE_207_VX0000_X:
    :cvar VALUE_207_VE0102_X:
    :cvar VALUE_207_X00000_X:
    :cvar VALUE_207_XS0114_X:
    :cvar VALUE_207_XX0004_X:
    :cvar VALUE_207_XS0106_X:
    :cvar VALUE_207_XS0117_X:
    :cvar VALUE_207_XX0801_X:
    :cvar VALUE_207_XX0005_X:
    :cvar VALUE_207_Y00000_X:
    :cvar VALUE_207_YS0123_X:
    :cvar VALUE_207_YX0602_X:
    :cvar VALUE_207_YX0905_X:
    :cvar VALUE_207_YX0901_X:
    :cvar VALUE_207_YP0228_X:
    :cvar VALUE_207_YX0007_X:
    :cvar VALUE_208_V00000_X:
    :cvar VALUE_208_VP0014_X:
    :cvar VALUE_208_VP0000_X:
    :cvar VALUE_207_Z00000_X:
    :cvar VALUE_207_ZP0101_X:
    :cvar VALUE_207_ZP0102_X:
    :cvar VALUE_207_ZB0001_X:
    :cvar VALUE_207_ZP0104_X:
    :cvar VALUE_207_ZP0105_X:
    :cvar VALUE_207_ZC0500_X:
    :cvar VALUE_207_ZD0900_X:
    :cvar VALUE_207_ZF0201_X:
    :cvar VALUE_207_ZH0000_X:
    :cvar VALUE_207_ZI0100_X:
    :cvar VALUE_207_ZM0300_X:
    :cvar VALUE_207_ZP0007_X:
    :cvar VALUE_207_ZN0500_X:
    :cvar VALUE_207_ZP0213_X:
    :cvar VALUE_208000000_X:
    :cvar VALUE_2080_A0000_X:
    :cvar VALUE_2080_I0007_X:
    :cvar VALUE_2080_P0006_X:
    :cvar VALUE_2080_T0002_X:
    :cvar VALUE_2080_N0001_X:
    :cvar VALUE_2080_P0008_X:
    :cvar VALUE_2080_P0201_X:
    :cvar VALUE_2080_P0202_X:
    :cvar VALUE_2080_P0203_X:
    :cvar VALUE_2080_P0204_X:
    :cvar VALUE_2080_P0205_X:
    :cvar VALUE_2080_P0206_X:
    :cvar VALUE_2080_P0207_X:
    :cvar VALUE_2080_P0208_X:
    :cvar VALUE_2080_P0210_X:
    :cvar VALUE_2080_P0214_X:
    :cvar VALUE_2080_P0216_X:
    :cvar VALUE_2080_S0010_X:
    :cvar VALUE_208100000_X:
    :cvar VALUE_2081_P2900_X:
    :cvar VALUE_2081_P0010_X:
    :cvar VALUE_2081_P0004_X:
    :cvar VALUE_2081_S0010_X:
    :cvar VALUE_208200000_X:
    :cvar VALUE_2082_S0099_X:
    :cvar VALUE_2082_S0105_X:
    :cvar VALUE_208300000_X:
    :cvar VALUE_2083_A0100_X:
    :cvar VALUE_2083_T0002_X:
    :cvar VALUE_2083_X0100_X:
    :cvar VALUE_2083_P0500_X:
    :cvar VALUE_2083_P0901_X:
    :cvar VALUE_2083_S0010_X:
    :cvar VALUE_2083_P0011_X:
    :cvar VALUE_208400000_X:
    :cvar VALUE_2084_A0401_X:
    :cvar VALUE_2084_P0802_X:
    :cvar VALUE_2084_P0804_X:
    :cvar VALUE_2084_N0600_X:
    :cvar VALUE_2084_F0202_X:
    :cvar VALUE_2084_P0805_X:
    :cvar VALUE_2084_P0005_X:
    :cvar VALUE_2084_N0400_X:
    :cvar VALUE_2084_N0402_X:
    :cvar VALUE_2084_P2900_X:
    :cvar VALUE_2084_P0800_X:
    :cvar VALUE_2084_S0010_X:
    :cvar VALUE_2084_V0102_X:
    :cvar VALUE_208500000_X:
    :cvar VALUE_2085_B0100_X:
    :cvar VALUE_2085_R0202_X:
    :cvar VALUE_2085_U0001_X:
    :cvar VALUE_2085_N0700_X:
    :cvar VALUE_2085_N0904_X:
    :cvar VALUE_2085_P0229_X:
    :cvar VALUE_2085_R0001_X:
    :cvar VALUE_2085_R0205_X:
    :cvar VALUE_2085_R0203_X:
    :cvar VALUE_2085_R0204_X:
    :cvar VALUE_208600000_X:
    :cvar VALUE_2086_S0120_X:
    :cvar VALUE_2086_S0122_X:
    :cvar VALUE_2086_S0105_X:
    :cvar VALUE_2086_S0102_X:
    :cvar VALUE_2086_X0206_X:
    :cvar VALUE_208_G00000_X:
    :cvar VALUE_204_F00000_X:
    :cvar VALUE_2086_S0127_X:
    :cvar VALUE_2086_S0129_X:
    :cvar VALUE_200000000_X:
    :cvar VALUE_208_U00000_X:
    :cvar VALUE_208_C00000_X:
    :cvar VALUE_208_D00000_X:
    :cvar VALUE_208_M00000_X:
    :cvar VALUE_209800000_X:
    :cvar VALUE_207_T00000_X:
    :cvar VALUE_204_D00000_X:
    :cvar VALUE_204_C00000_X:
    :cvar VALUE_207_W00000_X:
    :cvar VALUE_204_E00000_X:
    :cvar VALUE_208800000_X:
    :cvar VALUE_261_Q00000_X:
    :cvar VALUE_261_QM0855_X:
    :cvar VALUE_261_QA0600_X:
    :cvar VALUE_261_QM0850_X:
    :cvar VALUE_261_QA0005_X:
    :cvar VALUE_261_QA0006_X:
    :cvar VALUE_261_QA1903_X:
    :cvar VALUE_261_QA0900_X:
    :cvar VALUE_261_QA3000_X:
    :cvar VALUE_261_QB0400_X:
    :cvar VALUE_261_QC1500_X:
    :cvar VALUE_261_QC1800_X:
    :cvar VALUE_261_QC0050_X:
    :cvar VALUE_261_QD0000_X:
    :cvar VALUE_261_QD1600_X:
    :cvar VALUE_261_QE0002_X:
    :cvar VALUE_261_QE0700_X:
    :cvar VALUE_261_QE0800_X:
    :cvar VALUE_261_QF0050_X:
    :cvar VALUE_261_QF0400_X:
    :cvar VALUE_261_QG0250_X:
    :cvar VALUE_261_QH0100_X:
    :cvar VALUE_261_QH0700_X:
    :cvar VALUE_261_QI0500_X:
    :cvar VALUE_261_QL0400_X:
    :cvar VALUE_261_QM1200_X:
    :cvar VALUE_261_QR0206_X:
    :cvar VALUE_261_QM2500_X:
    :cvar VALUE_261_QM3000_X:
    :cvar VALUE_261_QM0801_X:
    :cvar VALUE_261_QM2800_X:
    :cvar VALUE_261_QM1000_X:
    :cvar VALUE_261_QM1100_X:
    :cvar VALUE_261_QM1101_X:
    :cvar VALUE_261_QM1102_X:
    :cvar VALUE_261_QR0208_X:
    :cvar VALUE_261_QR0207_X:
    :cvar VALUE_261_QM1300_X:
    :cvar VALUE_261_QX0100_X:
    :cvar VALUE_261_QX0200_X:
    :cvar VALUE_261_QX0203_X:
    :cvar VALUE_261_QS0132_X:
    :cvar VALUE_261_QS0112_X:
    :cvar VALUE_261_QP3300_X:
    :cvar VALUE_261_QP2000_X:
    :cvar VALUE_261_QP1100_X:
    :cvar VALUE_261_QP2300_X:
    :cvar VALUE_261_QP2400_X:
    :cvar VALUE_261_QP0904_X:
    :cvar VALUE_261_QP0905_X:
    :cvar VALUE_261_QR0200_X:
    :cvar VALUE_261_QR0800_X:
    :cvar VALUE_261_QR0400_X:
    :cvar VALUE_261_QR0401_X:
    :cvar VALUE_261_QR0405_X:
    :cvar VALUE_261_QR0404_X:
    :cvar VALUE_261_QR1100_X:
    :cvar VALUE_261_QR1300_X:
    :cvar VALUE_261_QS1200_X:
    :cvar VALUE_261_QS1000_X:
    :cvar VALUE_261_QU0200_X:
    :cvar VALUE_261_QV0200_X:
    :cvar VALUE_260000000_X:
    :cvar VALUE_101_Y00000_X:
    :cvar VALUE_101_YA0400_X:
    :cvar VALUE_101_YM0800_X:
    :cvar VALUE_101_YP1600_X:
    :cvar VALUE_101_YP2500_X:
    :cvar VALUE_101_YS0200_X:
    :cvar VALUE_103_G00000_X:
    :cvar VALUE_103_GC0700_X:
    :cvar VALUE_103_T00000_X:
    :cvar VALUE_103_TA0400_X:
    :cvar VALUE_103_TA0700_X:
    :cvar VALUE_103_TB0200_X:
    :cvar VALUE_103_TC2200_X:
    :cvar VALUE_103_TC0700_X:
    :cvar VALUE_103_TC1900_X:
    :cvar VALUE_103_TE1000_X:
    :cvar VALUE_103_TE1100_X:
    :cvar VALUE_103_TF0000_X:
    :cvar VALUE_103_TF0200_X:
    :cvar VALUE_103_TH0100_X:
    :cvar VALUE_103_TM1700_X:
    :cvar VALUE_103_TM1800_X:
    :cvar VALUE_103_TP0814_X:
    :cvar VALUE_103_TP2700_X:
    :cvar VALUE_103_TP2701_X:
    :cvar VALUE_103_TR0400_X:
    :cvar VALUE_103_TS0200_X:
    :cvar VALUE_103_TW0100_X:
    :cvar VALUE_104100000_X:
    :cvar VALUE_1041_C0700_X:
    :cvar VALUE_1041_S0200_X:
    :cvar VALUE_100000000_X:
    :cvar VALUE_106_H00000_X:
    :cvar VALUE_111_N00000_X:
    :cvar VALUE_111_NI0900_X:
    :cvar VALUE_111_NN0400_X:
    :cvar VALUE_111_NN1001_X:
    :cvar VALUE_111_NX0100_X:
    :cvar VALUE_111_NX0800_X:
    :cvar VALUE_111_NR0200_X:
    :cvar VALUE_111_NS0005_X:
    :cvar VALUE_111_NT0100_X:
    :cvar VALUE_110000000_X:
    :cvar VALUE_122300000_X:
    :cvar VALUE_1223_D0001_X:
    :cvar VALUE_1223_E0200_X:
    :cvar VALUE_1223_G0001_X:
    :cvar VALUE_1223_P0106_X:
    :cvar VALUE_1223_X0008_X:
    :cvar VALUE_1223_S0112_X:
    :cvar VALUE_1223_X0400_X:
    :cvar VALUE_1223_P0221_X:
    :cvar VALUE_1223_P0300_X:
    :cvar VALUE_1223_P0700_X:
    :cvar VALUE_120000000_X:
    :cvar VALUE_126800000_X:
    :cvar VALUE_124_Q00000_X:
    :cvar VALUE_126900000_X:
    :cvar VALUE_122400000_X:
    :cvar VALUE_133_V00000_X:
    :cvar VALUE_133_VN1006_X:
    :cvar VALUE_133_VN1004_X:
    :cvar VALUE_133_VN1005_X:
    :cvar VALUE_133_N00000_X:
    :cvar VALUE_133_NN1002_X:
    :cvar VALUE_130000000_X:
    :cvar VALUE_132700000_X:
    :cvar VALUE_136_A00000_X:
    :cvar VALUE_140000000_X:
    :cvar VALUE_146_N00000_X:
    :cvar VALUE_146_M00000_X:
    :cvar VALUE_146_L00000_X:
    :cvar VALUE_146_D00000_X:
    :cvar VALUE_152_W00000_X:
    :cvar VALUE_152_WC0802_X:
    :cvar VALUE_152_WL0500_X:
    :cvar VALUE_152_WX0102_X:
    :cvar VALUE_152_WP0200_X:
    :cvar VALUE_152_WS0006_X:
    :cvar VALUE_152_WV0400_X:
    :cvar VALUE_156_F00000_X:
    :cvar VALUE_156_FC0800_X:
    :cvar VALUE_156_FC0801_X:
    :cvar VALUE_156_FX1700_X:
    :cvar VALUE_156_FX1100_X:
    :cvar VALUE_156_FX1101_X:
    :cvar VALUE_156_FX1800_X:
    :cvar VALUE_156_FX1201_X:
    :cvar VALUE_156_FX1202_X:
    :cvar VALUE_156_FX1900_X:
    :cvar VALUE_150000000_X:
    :cvar VALUE_190000000_X:
    :cvar VALUE_193200000_X:
    :cvar VALUE_193400000_X:
    :cvar VALUE_270000000_X:
    :cvar VALUE_275_N00000_X:
    :cvar VALUE_273_R00000_X:
    :cvar VALUE_273_Y00000_X:
    :cvar VALUE_276400000_X:
    :cvar VALUE_281_P00000_X:
    :cvar VALUE_281_PC2000_X:
    :cvar VALUE_282_N00000_X:
    :cvar VALUE_282_NC2000_X:
    :cvar VALUE_282_NC0060_X:
    :cvar VALUE_282_NR1301_X:
    :cvar VALUE_282_NW0100_X:
    :cvar VALUE_286500000_X:
    :cvar VALUE_2865_C1500_X:
    :cvar VALUE_2865_M2000_X:
    :cvar VALUE_2865_X1600_X:
    :cvar VALUE_283_X00000_X:
    :cvar VALUE_283_XC2000_X:
    :cvar VALUE_280000000_X:
    :cvar VALUE_287300000_X:
    :cvar VALUE_283_Q00000_X:
    :cvar VALUE_284300000_X:
    :cvar VALUE_290000000_X:
    :cvar VALUE_291_U00000_X:
    :cvar VALUE_292200000_X:
    :cvar VALUE_293_D00000_X:
    :cvar VALUE_300000000_X:
    :cvar VALUE_302_F00000_X:
    :cvar VALUE_302_R00000_X:
    :cvar VALUE_305_S00000_X:
    :cvar VALUE_305_R00000_X:
    :cvar VALUE_163_W00000_X:
    :cvar VALUE_163_WA0400_X:
    :cvar VALUE_163_WA2000_X:
    :cvar VALUE_163_WP2201_X:
    :cvar VALUE_163_WC3500_X:
    :cvar VALUE_163_WC0400_X:
    :cvar VALUE_163_WC1400_X:
    :cvar VALUE_163_WC1500_X:
    :cvar VALUE_163_WC2100_X:
    :cvar VALUE_163_WC1600_X:
    :cvar VALUE_163_WC0200_X:
    :cvar VALUE_163_WD0400_X:
    :cvar VALUE_163_WD1100_X:
    :cvar VALUE_163_WE0003_X:
    :cvar VALUE_163_WE0900_X:
    :cvar VALUE_163_WF0300_X:
    :cvar VALUE_163_WG0100_X:
    :cvar VALUE_163_WG0000_X:
    :cvar VALUE_163_WG0600_X:
    :cvar VALUE_163_WH0500_X:
    :cvar VALUE_163_WH0200_X:
    :cvar VALUE_163_WH1000_X:
    :cvar VALUE_163_WI0600_X:
    :cvar VALUE_163_WI0500_X:
    :cvar VALUE_163_WL0100_X:
    :cvar VALUE_163_WM0102_X:
    :cvar VALUE_163_WM0705_X:
    :cvar VALUE_163_WN0002_X:
    :cvar VALUE_163_WN0003_X:
    :cvar VALUE_163_WN0300_X:
    :cvar VALUE_163_WN0800_X:
    :cvar VALUE_163_WM1400_X:
    :cvar VALUE_163_WN1003_X:
    :cvar VALUE_163_WX0002_X:
    :cvar VALUE_163_WX0003_X:
    :cvar VALUE_163_WX0106_X:
    :cvar VALUE_163_WX0200_X:
    :cvar VALUE_163_WX1100_X:
    :cvar VALUE_163_WX0800_X:
    :cvar VALUE_163_WX1500_X:
    :cvar VALUE_163_WX0601_X:
    :cvar VALUE_163_WP0000_X:
    :cvar VALUE_163_WP0218_X:
    :cvar VALUE_163_WP0200_X:
    :cvar VALUE_163_WP1700_X:
    :cvar VALUE_163_WS0121_X:
    :cvar VALUE_163_WP0808_X:
    :cvar VALUE_163_WP0809_X:
    :cvar VALUE_163_WP0807_X:
    :cvar VALUE_163_WR0400_X:
    :cvar VALUE_163_WR1000_X:
    :cvar VALUE_163_WS0200_X:
    :cvar VALUE_163_WU0100_X:
    :cvar VALUE_163_WW0101_X:
    :cvar VALUE_163_WW0000_X:
    :cvar VALUE_160000000_X:
    :cvar VALUE_164_W00000_X:
    :cvar VALUE_167_G00000_X:
    :cvar VALUE_164_X00000_X:
    :cvar VALUE_374700000_X:
    :cvar VALUE_3747_A0650_X:
    :cvar VALUE_3747_P1801_X:
    :cvar VALUE_370000000_X:
    :cvar VALUE_372600000_X:
    :cvar VALUE_372500000_X:
    :cvar VALUE_374_T00000_X:
    :cvar VALUE_373_H00000_X:
    :cvar VALUE_374_U00000_X:
    :cvar VALUE_376_J00000_X:
    :cvar VALUE_376_K00000_X:
    :cvar VALUE_376_G00000_X:
    :cvar VALUE_310400000_X:
    :cvar VALUE_3104_A0630_X:
    :cvar VALUE_3104_A0625_X:
    :cvar VALUE_311_Z00000_X:
    :cvar VALUE_311_ZA0620_X:
    :cvar VALUE_314000000_X:
    :cvar VALUE_3140_N1450_X:
    :cvar VALUE_310000000_X:
    :cvar VALUE_311500000_X:
    :cvar VALUE_317400000_X:
    :cvar VALUE_315_D00000_X:
    :cvar VALUE_315_P00000_X:
    :cvar VALUE_310500000_X:
    :cvar VALUE_313_M00000_X:
    :cvar VALUE_171_W00000_X:
    :cvar VALUE_171_WH0202_X:
    :cvar VALUE_171_WV0202_X:
    :cvar VALUE_174_M00000_X:
    :cvar VALUE_174_MM1900_X:
    :cvar VALUE_174400000_X:
    :cvar VALUE_1744_G0900_X:
    :cvar VALUE_1744_P3200_X:
    :cvar VALUE_1744_R1103_X:
    :cvar VALUE_1744_R1102_X:
    :cvar VALUE_170000000_X:
    :cvar VALUE_171100000_X:
    :cvar VALUE_172_A00000_X:
    :cvar VALUE_176_P00000_X:
    :cvar VALUE_175_L00000_X:
    :cvar VALUE_173000000_X:
    :cvar VALUE_177_F00000_X:
    :cvar VALUE_176_B00000_X:
    :cvar VALUE_175_M00000_X:
    :cvar VALUE_175_F00000_X:
    :cvar VALUE_170100000_X:
    :cvar VALUE_183500000_X:
    :cvar VALUE_1835_G0000_X:
    :cvar VALUE_1835_N0905_X:
    :cvar VALUE_1835_N1003_X:
    :cvar VALUE_1835_P1200_X:
    :cvar VALUE_1835_P1300_X:
    :cvar VALUE_180000000_X:
    :cvar VALUE_183700000_X:
    :cvar VALUE_364_S00000_X:
    :cvar VALUE_364_SA2100_X:
    :cvar VALUE_364_SA2200_X:
    :cvar VALUE_364_SC2300_X:
    :cvar VALUE_364_SC1501_X:
    :cvar VALUE_364_SC0200_X:
    :cvar VALUE_364_SE0003_X:
    :cvar VALUE_364_SE1400_X:
    :cvar VALUE_364_SF0001_X:
    :cvar VALUE_364_SG0600_X:
    :cvar VALUE_364_SH1100_X:
    :cvar VALUE_364_SH0200_X:
    :cvar VALUE_364_SI0800_X:
    :cvar VALUE_364_SL0600_X:
    :cvar VALUE_364_SM0705_X:
    :cvar VALUE_364_SN0000_X:
    :cvar VALUE_364_SN0800_X:
    :cvar VALUE_364_SX0106_X:
    :cvar VALUE_364_SX0200_X:
    :cvar VALUE_364_SX0204_X:
    :cvar VALUE_364_SP0200_X:
    :cvar VALUE_364_SP1700_X:
    :cvar VALUE_364_SP2800_X:
    :cvar VALUE_364_SP0808_X:
    :cvar VALUE_364_SP0809_X:
    :cvar VALUE_364_SP0807_X:
    :cvar VALUE_364_SP0810_X:
    :cvar VALUE_364_SP0811_X:
    :cvar VALUE_364_SP0812_X:
    :cvar VALUE_364_SP0813_X:
    :cvar VALUE_364_SR0400_X:
    :cvar VALUE_364_SS0200_X:
    :cvar VALUE_364_ST0500_X:
    :cvar VALUE_364_SW0102_X:
    :cvar VALUE_363_A00000_X:
    :cvar VALUE_363_AM0700_X:
    :cvar VALUE_363_AS0400_X:
    :cvar VALUE_363_L00000_X:
    :cvar VALUE_363_LA2100_X:
    :cvar VALUE_363_LA2200_X:
    :cvar VALUE_363_LC1500_X:
    :cvar VALUE_363_LC0200_X:
    :cvar VALUE_363_LF0000_X:
    :cvar VALUE_363_LG0600_X:
    :cvar VALUE_363_LN0000_X:
    :cvar VALUE_363_LN0005_X:
    :cvar VALUE_363_LX0001_X:
    :cvar VALUE_363_LX0106_X:
    :cvar VALUE_363_LP0200_X:
    :cvar VALUE_363_LP0222_X:
    :cvar VALUE_363_LP1700_X:
    :cvar VALUE_363_LP2300_X:
    :cvar VALUE_363_LP0808_X:
    :cvar VALUE_363_LS0200_X:
    :cvar VALUE_363_LW0102_X:
    :cvar VALUE_360000000_X:
    :cvar VALUE_367_H00000_X:
    :cvar VALUE_367_A00000_X:
    :cvar VALUE_367500000_X:
    :cvar VALUE_213_E00000_X:
    :cvar VALUE_213_EG0000_X:
    :cvar VALUE_213_EP1101_X:
    :cvar VALUE_213_EP0504_X:
    :cvar VALUE_213_ER0200_X:
    :cvar VALUE_213_ES0000_X:
    :cvar VALUE_213_ES0131_X:
    :cvar VALUE_213_ES0103_X:
    :cvar VALUE_210000000_X:
    :cvar VALUE_211_D00000_X:
    :cvar VALUE_324500000_X:
    :cvar VALUE_3245_S0500_X:
    :cvar VALUE_320000000_X:
    :cvar VALUE_320800000_X:
    :cvar VALUE_320900000_X:
    :cvar VALUE_323_P00000_X:
    :cvar VALUE_322_D00000_X:
    :cvar VALUE_320600000_X:
    :cvar VALUE_320700000_X:
    :cvar VALUE_225_X00000_X:
    :cvar VALUE_225_XE1200_X:
    :cvar VALUE_225_XH1200_X:
    :cvar VALUE_225_XH1300_X:
    :cvar VALUE_225_XN1300_X:
    :cvar VALUE_225_XP0200_X:
    :cvar VALUE_225_XR0403_X:
    :cvar VALUE_225100000_X:
    :cvar VALUE_2251_C2600_X:
    :cvar VALUE_2251_E1300_X:
    :cvar VALUE_2251_E1200_X:
    :cvar VALUE_2251_G0304_X:
    :cvar VALUE_2251_H1200_X:
    :cvar VALUE_2251_H1300_X:
    :cvar VALUE_2251_N0400_X:
    :cvar VALUE_2251_X0800_X:
    :cvar VALUE_2251_P0200_X:
    :cvar VALUE_2251_S0007_X:
    :cvar VALUE_225_C00000_X:
    :cvar VALUE_225_CA2400_X:
    :cvar VALUE_225_CA2500_X:
    :cvar VALUE_227800000_X:
    :cvar VALUE_2278_C0205_X:
    :cvar VALUE_2278_E0002_X:
    :cvar VALUE_2278_G1100_X:
    :cvar VALUE_2278_G0305_X:
    :cvar VALUE_2278_H0200_X:
    :cvar VALUE_2278_P3900_X:
    :cvar VALUE_2278_P3800_X:
    :cvar VALUE_2278_E1000_X:
    :cvar VALUE_2278_P4000_X:
    :cvar VALUE_2278_P1004_X:
    :cvar VALUE_2278_P1006_X:
    :cvar VALUE_2278_P1005_X:
    :cvar VALUE_2278_S1500_X:
    :cvar VALUE_227900000_X:
    :cvar VALUE_2279_C0205_X:
    :cvar VALUE_2279_E0002_X:
    :cvar VALUE_2279_G1100_X:
    :cvar VALUE_2279_G0305_X:
    :cvar VALUE_2279_H0200_X:
    :cvar VALUE_2279_P3900_X:
    :cvar VALUE_2279_P3800_X:
    :cvar VALUE_2279_E1000_X:
    :cvar VALUE_2279_P4000_X:
    :cvar VALUE_2279_P1004_X:
    :cvar VALUE_2279_P1006_X:
    :cvar VALUE_2279_P1005_X:
    :cvar VALUE_2279_S1500_X:
    :cvar VALUE_225500000_X:
    :cvar VALUE_2255_A2300_X:
    :cvar VALUE_2255_R0406_X:
    :cvar VALUE_220000000_X:
    :cvar VALUE_221700000_X:
    :cvar VALUE_225600000_X:
    :cvar VALUE_226300000_X:
    :cvar VALUE_225700000_X:
    :cvar VALUE_225_A00000_X:
    :cvar VALUE_224_Z00000_X:
    :cvar VALUE_225000000_X:
    :cvar VALUE_222_Z00000_X:
    :cvar VALUE_225200000_X:
    :cvar VALUE_224_P00000_X:
    :cvar VALUE_225_B00000_X:
    :cvar VALUE_225800000_X:
    :cvar VALUE_225400000_X:
    :cvar VALUE_385_H00000_X:
    :cvar VALUE_385_HR2050_X:
    :cvar VALUE_385_HR2055_X:
    :cvar VALUE_385_HR2060_X:
    :cvar VALUE_385_HR2065_X:
    :cvar VALUE_380000000_X:
    :cvar VALUE_231_H00000_X:
    :cvar VALUE_231_HA2400_X:
    :cvar VALUE_231_HA2500_X:
    :cvar VALUE_235500000_X:
    :cvar VALUE_2355_A2700_X:
    :cvar VALUE_2355_S0801_X:
    :cvar VALUE_230000000_X:
    :cvar VALUE_237600000_X:
    :cvar VALUE_237700000_X:
    :cvar VALUE_235_Z00000_X:
    :cvar VALUE_332_B00000_X:
    :cvar VALUE_332_BC3200_X:
    :cvar VALUE_332_BD1200_X:
    :cvar VALUE_332_BN1400_X:
    :cvar VALUE_332_BX2000_X:
    :cvar VALUE_332_BP3500_X:
    :cvar VALUE_330000000_X:
    :cvar VALUE_331_L00000_X:
    :cvar VALUE_332_G00000_X:
    :cvar VALUE_332_H00000_X:
    :cvar VALUE_332_S00000_X:
    :cvar VALUE_332_U00000_X:
    :cvar VALUE_335_U00000_X:
    :cvar VALUE_333600000_X:
    :cvar VALUE_335_V00000_X:
    :cvar VALUE_335_E00000_X:
    :cvar VALUE_247100000_X:
    :cvar VALUE_2471_B0102_X:
    :cvar VALUE_2471_C1106_X:
    :cvar VALUE_2471_C1101_X:
    :cvar VALUE_2471_C3401_X:
    :cvar VALUE_2471_M1202_X:
    :cvar VALUE_2471_M2300_X:
    :cvar VALUE_2471_N0900_X:
    :cvar VALUE_2471_Q0001_X:
    :cvar VALUE_2471_R0002_X:
    :cvar VALUE_2471_C3402_X:
    :cvar VALUE_2471_S1302_X:
    :cvar VALUE_2471_V0105_X:
    :cvar VALUE_2471_V0106_X:
    :cvar VALUE_246_X00000_X:
    :cvar VALUE_246_XC2901_X:
    :cvar VALUE_246_XS1301_X:
    :cvar VALUE_246_XC2903_X:
    :cvar VALUE_246_Y00000_X:
    :cvar VALUE_246_YC3301_X:
    :cvar VALUE_246_YC3302_X:
    :cvar VALUE_246_YR1600_X:
    :cvar VALUE_246_Z00000_X:
    :cvar VALUE_246_ZA2600_X:
    :cvar VALUE_246_ZB0500_X:
    :cvar VALUE_246_ZB0301_X:
    :cvar VALUE_246_ZB0302_X:
    :cvar VALUE_246_ZB0600_X:
    :cvar VALUE_246_ZE0500_X:
    :cvar VALUE_246_ZE0600_X:
    :cvar VALUE_246_ZG1000_X:
    :cvar VALUE_246_ZG0701_X:
    :cvar VALUE_246_ZI1000_X:
    :cvar VALUE_246_ZN0300_X:
    :cvar VALUE_246_ZS0400_X:
    :cvar VALUE_246_Q00000_X:
    :cvar VALUE_246_QB0000_X:
    :cvar VALUE_246_QC1000_X:
    :cvar VALUE_246_QC2700_X:
    :cvar VALUE_246_QH0401_X:
    :cvar VALUE_246_QH0000_X:
    :cvar VALUE_246_QH0600_X:
    :cvar VALUE_246_QI0000_X:
    :cvar VALUE_246_QL0900_X:
    :cvar VALUE_246_QL0901_X:
    :cvar VALUE_246_QM0706_X:
    :cvar VALUE_246_QM0900_X:
    :cvar VALUE_247000000_X:
    :cvar VALUE_2470_A2800_X:
    :cvar VALUE_247200000_X:
    :cvar VALUE_2472_B0301_X:
    :cvar VALUE_2472_D0500_X:
    :cvar VALUE_2472_E0500_X:
    :cvar VALUE_2472_R0900_X:
    :cvar VALUE_2472_V0600_X:
    :cvar VALUE_246_R00000_X:
    :cvar VALUE_246_RH0600_X:
    :cvar VALUE_246_RM2200_X:
    :cvar VALUE_246_RP1900_X:
    :cvar VALUE_240000000_X:
    :cvar VALUE_246_W00000_X:
    :cvar VALUE_341600000_X:
    :cvar VALUE_3416_A0800_X:
    :cvar VALUE_3416_L0300_X:
    :cvar VALUE_3416_S0300_X:
    :cvar VALUE_340000000_X:
    :cvar VALUE_347_B00000_X:
    :cvar VALUE_343900000_X:
    :cvar VALUE_347_C00000_X:
    :cvar VALUE_343800000_X:
    :cvar VALUE_344600000_X:
    :cvar VALUE_347_D00000_X:
    :cvar VALUE_347_E00000_X:
    """
    VALUE_250000000_X = "250000000X"
    VALUE_251_B00000_X = "251B00000X"
    VALUE_251_C00000_X = "251C00000X"
    VALUE_251_E00000_X = "251E00000X"
    VALUE_251_F00000_X = "251F00000X"
    VALUE_251_G00000_X = "251G00000X"
    VALUE_251_J00000_X = "251J00000X"
    VALUE_251_K00000_X = "251K00000X"
    VALUE_251_V00000_X = "251V00000X"
    VALUE_207_K00000_X = "207K00000X"
    VALUE_207_KA0200_X = "207KA0200X"
    VALUE_207_KI0005_X = "207KI0005X"
    VALUE_207_L00000_X = "207L00000X"
    VALUE_207_LA0401_X = "207LA0401X"
    VALUE_207_LC0200_X = "207LC0200X"
    VALUE_207_LP2900_X = "207LP2900X"
    VALUE_207_N00000_X = "207N00000X"
    VALUE_207_NI0002_X = "207NI0002X"
    VALUE_207_NS0135_X = "207NS0135X"
    VALUE_207_ND0900_X = "207ND0900X"
    VALUE_207_ND0101_X = "207ND0101X"
    VALUE_207_NP0225_X = "207NP0225X"
    VALUE_207_P00000_X = "207P00000X"
    VALUE_207_PE0004_X = "207PE0004X"
    VALUE_207_PT0002_X = "207PT0002X"
    VALUE_207_PP0204_X = "207PP0204X"
    VALUE_207_PS0010_X = "207PS0010X"
    VALUE_207_PE0005_X = "207PE0005X"
    VALUE_207_Q00000_X = "207Q00000X"
    VALUE_207_QA0401_X = "207QA0401X"
    VALUE_207_QA0000_X = "207QA0000X"
    VALUE_207_QA0505_X = "207QA0505X"
    VALUE_207_QG0300_X = "207QG0300X"
    VALUE_207_QS0010_X = "207QS0010X"
    VALUE_207_R00000_X = "207R00000X"
    VALUE_207_RA0401_X = "207RA0401X"
    VALUE_207_RA0000_X = "207RA0000X"
    VALUE_207_RA0201_X = "207RA0201X"
    VALUE_207_RC0000_X = "207RC0000X"
    VALUE_207_RI0001_X = "207RI0001X"
    VALUE_207_RC0001_X = "207RC0001X"
    VALUE_207_RC0200_X = "207RC0200X"
    VALUE_207_RE0101_X = "207RE0101X"
    VALUE_207_RG0100_X = "207RG0100X"
    VALUE_207_RG0300_X = "207RG0300X"
    VALUE_207_RH0000_X = "207RH0000X"
    VALUE_207_RH0003_X = "207RH0003X"
    VALUE_207_RI0008_X = "207RI0008X"
    VALUE_207_RI0200_X = "207RI0200X"
    VALUE_207_RI0011_X = "207RI0011X"
    VALUE_207_RM1200_X = "207RM1200X"
    VALUE_207_RX0202_X = "207RX0202X"
    VALUE_207_RN0300_X = "207RN0300X"
    VALUE_207_RP1001_X = "207RP1001X"
    VALUE_207_RR0500_X = "207RR0500X"
    VALUE_207_RS0010_X = "207RS0010X"
    VALUE_207_S00000_X = "207S00000X"
    VALUE_207_SG0202_X = "207SG0202X"
    VALUE_207_SC0300_X = "207SC0300X"
    VALUE_207_SG0201_X = "207SG0201X"
    VALUE_207_SG0203_X = "207SG0203X"
    VALUE_207_SM0001_X = "207SM0001X"
    VALUE_207_SG0205_X = "207SG0205X"
    VALUE_207_U00000_X = "207U00000X"
    VALUE_207_UN0903_X = "207UN0903X"
    VALUE_207_UN0901_X = "207UN0901X"
    VALUE_207_UN0902_X = "207UN0902X"
    VALUE_207_V00000_X = "207V00000X"
    VALUE_207_VC0200_X = "207VC0200X"
    VALUE_207_VX0201_X = "207VX0201X"
    VALUE_207_VG0400_X = "207VG0400X"
    VALUE_207_VM0101_X = "207VM0101X"
    VALUE_207_VX0000_X = "207VX0000X"
    VALUE_207_VE0102_X = "207VE0102X"
    VALUE_207_X00000_X = "207X00000X"
    VALUE_207_XS0114_X = "207XS0114X"
    VALUE_207_XX0004_X = "207XX0004X"
    VALUE_207_XS0106_X = "207XS0106X"
    VALUE_207_XS0117_X = "207XS0117X"
    VALUE_207_XX0801_X = "207XX0801X"
    VALUE_207_XX0005_X = "207XX0005X"
    VALUE_207_Y00000_X = "207Y00000X"
    VALUE_207_YS0123_X = "207YS0123X"
    VALUE_207_YX0602_X = "207YX0602X"
    VALUE_207_YX0905_X = "207YX0905X"
    VALUE_207_YX0901_X = "207YX0901X"
    VALUE_207_YP0228_X = "207YP0228X"
    VALUE_207_YX0007_X = "207YX0007X"
    VALUE_208_V00000_X = "208V00000X"
    VALUE_208_VP0014_X = "208VP0014X"
    VALUE_208_VP0000_X = "208VP0000X"
    VALUE_207_Z00000_X = "207Z00000X"
    VALUE_207_ZP0101_X = "207ZP0101X"
    VALUE_207_ZP0102_X = "207ZP0102X"
    VALUE_207_ZB0001_X = "207ZB0001X"
    VALUE_207_ZP0104_X = "207ZP0104X"
    VALUE_207_ZP0105_X = "207ZP0105X"
    VALUE_207_ZC0500_X = "207ZC0500X"
    VALUE_207_ZD0900_X = "207ZD0900X"
    VALUE_207_ZF0201_X = "207ZF0201X"
    VALUE_207_ZH0000_X = "207ZH0000X"
    VALUE_207_ZI0100_X = "207ZI0100X"
    VALUE_207_ZM0300_X = "207ZM0300X"
    VALUE_207_ZP0007_X = "207ZP0007X"
    VALUE_207_ZN0500_X = "207ZN0500X"
    VALUE_207_ZP0213_X = "207ZP0213X"
    VALUE_208000000_X = "208000000X"
    VALUE_2080_A0000_X = "2080A0000X"
    VALUE_2080_I0007_X = "2080I0007X"
    VALUE_2080_P0006_X = "2080P0006X"
    VALUE_2080_T0002_X = "2080T0002X"
    VALUE_2080_N0001_X = "2080N0001X"
    VALUE_2080_P0008_X = "2080P0008X"
    VALUE_2080_P0201_X = "2080P0201X"
    VALUE_2080_P0202_X = "2080P0202X"
    VALUE_2080_P0203_X = "2080P0203X"
    VALUE_2080_P0204_X = "2080P0204X"
    VALUE_2080_P0205_X = "2080P0205X"
    VALUE_2080_P0206_X = "2080P0206X"
    VALUE_2080_P0207_X = "2080P0207X"
    VALUE_2080_P0208_X = "2080P0208X"
    VALUE_2080_P0210_X = "2080P0210X"
    VALUE_2080_P0214_X = "2080P0214X"
    VALUE_2080_P0216_X = "2080P0216X"
    VALUE_2080_S0010_X = "2080S0010X"
    VALUE_208100000_X = "208100000X"
    VALUE_2081_P2900_X = "2081P2900X"
    VALUE_2081_P0010_X = "2081P0010X"
    VALUE_2081_P0004_X = "2081P0004X"
    VALUE_2081_S0010_X = "2081S0010X"
    VALUE_208200000_X = "208200000X"
    VALUE_2082_S0099_X = "2082S0099X"
    VALUE_2082_S0105_X = "2082S0105X"
    VALUE_208300000_X = "208300000X"
    VALUE_2083_A0100_X = "2083A0100X"
    VALUE_2083_T0002_X = "2083T0002X"
    VALUE_2083_X0100_X = "2083X0100X"
    VALUE_2083_P0500_X = "2083P0500X"
    VALUE_2083_P0901_X = "2083P0901X"
    VALUE_2083_S0010_X = "2083S0010X"
    VALUE_2083_P0011_X = "2083P0011X"
    VALUE_208400000_X = "208400000X"
    VALUE_2084_A0401_X = "2084A0401X"
    VALUE_2084_P0802_X = "2084P0802X"
    VALUE_2084_P0804_X = "2084P0804X"
    VALUE_2084_N0600_X = "2084N0600X"
    VALUE_2084_F0202_X = "2084F0202X"
    VALUE_2084_P0805_X = "2084P0805X"
    VALUE_2084_P0005_X = "2084P0005X"
    VALUE_2084_N0400_X = "2084N0400X"
    VALUE_2084_N0402_X = "2084N0402X"
    VALUE_2084_P2900_X = "2084P2900X"
    VALUE_2084_P0800_X = "2084P0800X"
    VALUE_2084_S0010_X = "2084S0010X"
    VALUE_2084_V0102_X = "2084V0102X"
    VALUE_208500000_X = "208500000X"
    VALUE_2085_B0100_X = "2085B0100X"
    VALUE_2085_R0202_X = "2085R0202X"
    VALUE_2085_U0001_X = "2085U0001X"
    VALUE_2085_N0700_X = "2085N0700X"
    VALUE_2085_N0904_X = "2085N0904X"
    VALUE_2085_P0229_X = "2085P0229X"
    VALUE_2085_R0001_X = "2085R0001X"
    VALUE_2085_R0205_X = "2085R0205X"
    VALUE_2085_R0203_X = "2085R0203X"
    VALUE_2085_R0204_X = "2085R0204X"
    VALUE_208600000_X = "208600000X"
    VALUE_2086_S0120_X = "2086S0120X"
    VALUE_2086_S0122_X = "2086S0122X"
    VALUE_2086_S0105_X = "2086S0105X"
    VALUE_2086_S0102_X = "2086S0102X"
    VALUE_2086_X0206_X = "2086X0206X"
    VALUE_208_G00000_X = "208G00000X"
    VALUE_204_F00000_X = "204F00000X"
    VALUE_2086_S0127_X = "2086S0127X"
    VALUE_2086_S0129_X = "2086S0129X"
    VALUE_200000000_X = "200000000X"
    VALUE_208_U00000_X = "208U00000X"
    VALUE_208_C00000_X = "208C00000X"
    VALUE_208_D00000_X = "208D00000X"
    VALUE_208_M00000_X = "208M00000X"
    VALUE_209800000_X = "209800000X"
    VALUE_207_T00000_X = "207T00000X"
    VALUE_204_D00000_X = "204D00000X"
    VALUE_204_C00000_X = "204C00000X"
    VALUE_207_W00000_X = "207W00000X"
    VALUE_204_E00000_X = "204E00000X"
    VALUE_208800000_X = "208800000X"
    VALUE_261_Q00000_X = "261Q00000X"
    VALUE_261_QM0855_X = "261QM0855X"
    VALUE_261_QA0600_X = "261QA0600X"
    VALUE_261_QM0850_X = "261QM0850X"
    VALUE_261_QA0005_X = "261QA0005X"
    VALUE_261_QA0006_X = "261QA0006X"
    VALUE_261_QA1903_X = "261QA1903X"
    VALUE_261_QA0900_X = "261QA0900X"
    VALUE_261_QA3000_X = "261QA3000X"
    VALUE_261_QB0400_X = "261QB0400X"
    VALUE_261_QC1500_X = "261QC1500X"
    VALUE_261_QC1800_X = "261QC1800X"
    VALUE_261_QC0050_X = "261QC0050X"
    VALUE_261_QD0000_X = "261QD0000X"
    VALUE_261_QD1600_X = "261QD1600X"
    VALUE_261_QE0002_X = "261QE0002X"
    VALUE_261_QE0700_X = "261QE0700X"
    VALUE_261_QE0800_X = "261QE0800X"
    VALUE_261_QF0050_X = "261QF0050X"
    VALUE_261_QF0400_X = "261QF0400X"
    VALUE_261_QG0250_X = "261QG0250X"
    VALUE_261_QH0100_X = "261QH0100X"
    VALUE_261_QH0700_X = "261QH0700X"
    VALUE_261_QI0500_X = "261QI0500X"
    VALUE_261_QL0400_X = "261QL0400X"
    VALUE_261_QM1200_X = "261QM1200X"
    VALUE_261_QR0206_X = "261QR0206X"
    VALUE_261_QM2500_X = "261QM2500X"
    VALUE_261_QM3000_X = "261QM3000X"
    VALUE_261_QM0801_X = "261QM0801X"
    VALUE_261_QM2800_X = "261QM2800X"
    VALUE_261_QM1000_X = "261QM1000X"
    VALUE_261_QM1100_X = "261QM1100X"
    VALUE_261_QM1101_X = "261QM1101X"
    VALUE_261_QM1102_X = "261QM1102X"
    VALUE_261_QR0208_X = "261QR0208X"
    VALUE_261_QR0207_X = "261QR0207X"
    VALUE_261_QM1300_X = "261QM1300X"
    VALUE_261_QX0100_X = "261QX0100X"
    VALUE_261_QX0200_X = "261QX0200X"
    VALUE_261_QX0203_X = "261QX0203X"
    VALUE_261_QS0132_X = "261QS0132X"
    VALUE_261_QS0112_X = "261QS0112X"
    VALUE_261_QP3300_X = "261QP3300X"
    VALUE_261_QP2000_X = "261QP2000X"
    VALUE_261_QP1100_X = "261QP1100X"
    VALUE_261_QP2300_X = "261QP2300X"
    VALUE_261_QP2400_X = "261QP2400X"
    VALUE_261_QP0904_X = "261QP0904X"
    VALUE_261_QP0905_X = "261QP0905X"
    VALUE_261_QR0200_X = "261QR0200X"
    VALUE_261_QR0800_X = "261QR0800X"
    VALUE_261_QR0400_X = "261QR0400X"
    VALUE_261_QR0401_X = "261QR0401X"
    VALUE_261_QR0405_X = "261QR0405X"
    VALUE_261_QR0404_X = "261QR0404X"
    VALUE_261_QR1100_X = "261QR1100X"
    VALUE_261_QR1300_X = "261QR1300X"
    VALUE_261_QS1200_X = "261QS1200X"
    VALUE_261_QS1000_X = "261QS1000X"
    VALUE_261_QU0200_X = "261QU0200X"
    VALUE_261_QV0200_X = "261QV0200X"
    VALUE_260000000_X = "260000000X"
    VALUE_101_Y00000_X = "101Y00000X"
    VALUE_101_YA0400_X = "101YA0400X"
    VALUE_101_YM0800_X = "101YM0800X"
    VALUE_101_YP1600_X = "101YP1600X"
    VALUE_101_YP2500_X = "101YP2500X"
    VALUE_101_YS0200_X = "101YS0200X"
    VALUE_103_G00000_X = "103G00000X"
    VALUE_103_GC0700_X = "103GC0700X"
    VALUE_103_T00000_X = "103T00000X"
    VALUE_103_TA0400_X = "103TA0400X"
    VALUE_103_TA0700_X = "103TA0700X"
    VALUE_103_TB0200_X = "103TB0200X"
    VALUE_103_TC2200_X = "103TC2200X"
    VALUE_103_TC0700_X = "103TC0700X"
    VALUE_103_TC1900_X = "103TC1900X"
    VALUE_103_TE1000_X = "103TE1000X"
    VALUE_103_TE1100_X = "103TE1100X"
    VALUE_103_TF0000_X = "103TF0000X"
    VALUE_103_TF0200_X = "103TF0200X"
    VALUE_103_TH0100_X = "103TH0100X"
    VALUE_103_TM1700_X = "103TM1700X"
    VALUE_103_TM1800_X = "103TM1800X"
    VALUE_103_TP0814_X = "103TP0814X"
    VALUE_103_TP2700_X = "103TP2700X"
    VALUE_103_TP2701_X = "103TP2701X"
    VALUE_103_TR0400_X = "103TR0400X"
    VALUE_103_TS0200_X = "103TS0200X"
    VALUE_103_TW0100_X = "103TW0100X"
    VALUE_104100000_X = "104100000X"
    VALUE_1041_C0700_X = "1041C0700X"
    VALUE_1041_S0200_X = "1041S0200X"
    VALUE_100000000_X = "100000000X"
    VALUE_106_H00000_X = "106H00000X"
    VALUE_111_N00000_X = "111N00000X"
    VALUE_111_NI0900_X = "111NI0900X"
    VALUE_111_NN0400_X = "111NN0400X"
    VALUE_111_NN1001_X = "111NN1001X"
    VALUE_111_NX0100_X = "111NX0100X"
    VALUE_111_NX0800_X = "111NX0800X"
    VALUE_111_NR0200_X = "111NR0200X"
    VALUE_111_NS0005_X = "111NS0005X"
    VALUE_111_NT0100_X = "111NT0100X"
    VALUE_110000000_X = "110000000X"
    VALUE_122300000_X = "122300000X"
    VALUE_1223_D0001_X = "1223D0001X"
    VALUE_1223_E0200_X = "1223E0200X"
    VALUE_1223_G0001_X = "1223G0001X"
    VALUE_1223_P0106_X = "1223P0106X"
    VALUE_1223_X0008_X = "1223X0008X"
    VALUE_1223_S0112_X = "1223S0112X"
    VALUE_1223_X0400_X = "1223X0400X"
    VALUE_1223_P0221_X = "1223P0221X"
    VALUE_1223_P0300_X = "1223P0300X"
    VALUE_1223_P0700_X = "1223P0700X"
    VALUE_120000000_X = "120000000X"
    VALUE_126800000_X = "126800000X"
    VALUE_124_Q00000_X = "124Q00000X"
    VALUE_126900000_X = "126900000X"
    VALUE_122400000_X = "122400000X"
    VALUE_133_V00000_X = "133V00000X"
    VALUE_133_VN1006_X = "133VN1006X"
    VALUE_133_VN1004_X = "133VN1004X"
    VALUE_133_VN1005_X = "133VN1005X"
    VALUE_133_N00000_X = "133N00000X"
    VALUE_133_NN1002_X = "133NN1002X"
    VALUE_130000000_X = "130000000X"
    VALUE_132700000_X = "132700000X"
    VALUE_136_A00000_X = "136A00000X"
    VALUE_140000000_X = "140000000X"
    VALUE_146_N00000_X = "146N00000X"
    VALUE_146_M00000_X = "146M00000X"
    VALUE_146_L00000_X = "146L00000X"
    VALUE_146_D00000_X = "146D00000X"
    VALUE_152_W00000_X = "152W00000X"
    VALUE_152_WC0802_X = "152WC0802X"
    VALUE_152_WL0500_X = "152WL0500X"
    VALUE_152_WX0102_X = "152WX0102X"
    VALUE_152_WP0200_X = "152WP0200X"
    VALUE_152_WS0006_X = "152WS0006X"
    VALUE_152_WV0400_X = "152WV0400X"
    VALUE_156_F00000_X = "156F00000X"
    VALUE_156_FC0800_X = "156FC0800X"
    VALUE_156_FC0801_X = "156FC0801X"
    VALUE_156_FX1700_X = "156FX1700X"
    VALUE_156_FX1100_X = "156FX1100X"
    VALUE_156_FX1101_X = "156FX1101X"
    VALUE_156_FX1800_X = "156FX1800X"
    VALUE_156_FX1201_X = "156FX1201X"
    VALUE_156_FX1202_X = "156FX1202X"
    VALUE_156_FX1900_X = "156FX1900X"
    VALUE_150000000_X = "150000000X"
    VALUE_190000000_X = "190000000X"
    VALUE_193200000_X = "193200000X"
    VALUE_193400000_X = "193400000X"
    VALUE_270000000_X = "270000000X"
    VALUE_275_N00000_X = "275N00000X"
    VALUE_273_R00000_X = "273R00000X"
    VALUE_273_Y00000_X = "273Y00000X"
    VALUE_276400000_X = "276400000X"
    VALUE_281_P00000_X = "281P00000X"
    VALUE_281_PC2000_X = "281PC2000X"
    VALUE_282_N00000_X = "282N00000X"
    VALUE_282_NC2000_X = "282NC2000X"
    VALUE_282_NC0060_X = "282NC0060X"
    VALUE_282_NR1301_X = "282NR1301X"
    VALUE_282_NW0100_X = "282NW0100X"
    VALUE_286500000_X = "286500000X"
    VALUE_2865_C1500_X = "2865C1500X"
    VALUE_2865_M2000_X = "2865M2000X"
    VALUE_2865_X1600_X = "2865X1600X"
    VALUE_283_X00000_X = "283X00000X"
    VALUE_283_XC2000_X = "283XC2000X"
    VALUE_280000000_X = "280000000X"
    VALUE_287300000_X = "287300000X"
    VALUE_283_Q00000_X = "283Q00000X"
    VALUE_284300000_X = "284300000X"
    VALUE_290000000_X = "290000000X"
    VALUE_291_U00000_X = "291U00000X"
    VALUE_292200000_X = "292200000X"
    VALUE_293_D00000_X = "293D00000X"
    VALUE_300000000_X = "300000000X"
    VALUE_302_F00000_X = "302F00000X"
    VALUE_302_R00000_X = "302R00000X"
    VALUE_305_S00000_X = "305S00000X"
    VALUE_305_R00000_X = "305R00000X"
    VALUE_163_W00000_X = "163W00000X"
    VALUE_163_WA0400_X = "163WA0400X"
    VALUE_163_WA2000_X = "163WA2000X"
    VALUE_163_WP2201_X = "163WP2201X"
    VALUE_163_WC3500_X = "163WC3500X"
    VALUE_163_WC0400_X = "163WC0400X"
    VALUE_163_WC1400_X = "163WC1400X"
    VALUE_163_WC1500_X = "163WC1500X"
    VALUE_163_WC2100_X = "163WC2100X"
    VALUE_163_WC1600_X = "163WC1600X"
    VALUE_163_WC0200_X = "163WC0200X"
    VALUE_163_WD0400_X = "163WD0400X"
    VALUE_163_WD1100_X = "163WD1100X"
    VALUE_163_WE0003_X = "163WE0003X"
    VALUE_163_WE0900_X = "163WE0900X"
    VALUE_163_WF0300_X = "163WF0300X"
    VALUE_163_WG0100_X = "163WG0100X"
    VALUE_163_WG0000_X = "163WG0000X"
    VALUE_163_WG0600_X = "163WG0600X"
    VALUE_163_WH0500_X = "163WH0500X"
    VALUE_163_WH0200_X = "163WH0200X"
    VALUE_163_WH1000_X = "163WH1000X"
    VALUE_163_WI0600_X = "163WI0600X"
    VALUE_163_WI0500_X = "163WI0500X"
    VALUE_163_WL0100_X = "163WL0100X"
    VALUE_163_WM0102_X = "163WM0102X"
    VALUE_163_WM0705_X = "163WM0705X"
    VALUE_163_WN0002_X = "163WN0002X"
    VALUE_163_WN0003_X = "163WN0003X"
    VALUE_163_WN0300_X = "163WN0300X"
    VALUE_163_WN0800_X = "163WN0800X"
    VALUE_163_WM1400_X = "163WM1400X"
    VALUE_163_WN1003_X = "163WN1003X"
    VALUE_163_WX0002_X = "163WX0002X"
    VALUE_163_WX0003_X = "163WX0003X"
    VALUE_163_WX0106_X = "163WX0106X"
    VALUE_163_WX0200_X = "163WX0200X"
    VALUE_163_WX1100_X = "163WX1100X"
    VALUE_163_WX0800_X = "163WX0800X"
    VALUE_163_WX1500_X = "163WX1500X"
    VALUE_163_WX0601_X = "163WX0601X"
    VALUE_163_WP0000_X = "163WP0000X"
    VALUE_163_WP0218_X = "163WP0218X"
    VALUE_163_WP0200_X = "163WP0200X"
    VALUE_163_WP1700_X = "163WP1700X"
    VALUE_163_WS0121_X = "163WS0121X"
    VALUE_163_WP0808_X = "163WP0808X"
    VALUE_163_WP0809_X = "163WP0809X"
    VALUE_163_WP0807_X = "163WP0807X"
    VALUE_163_WR0400_X = "163WR0400X"
    VALUE_163_WR1000_X = "163WR1000X"
    VALUE_163_WS0200_X = "163WS0200X"
    VALUE_163_WU0100_X = "163WU0100X"
    VALUE_163_WW0101_X = "163WW0101X"
    VALUE_163_WW0000_X = "163WW0000X"
    VALUE_160000000_X = "160000000X"
    VALUE_164_W00000_X = "164W00000X"
    VALUE_167_G00000_X = "167G00000X"
    VALUE_164_X00000_X = "164X00000X"
    VALUE_374700000_X = "374700000X"
    VALUE_3747_A0650_X = "3747A0650X"
    VALUE_3747_P1801_X = "3747P1801X"
    VALUE_370000000_X = "370000000X"
    VALUE_372600000_X = "372600000X"
    VALUE_372500000_X = "372500000X"
    VALUE_374_T00000_X = "374T00000X"
    VALUE_373_H00000_X = "373H00000X"
    VALUE_374_U00000_X = "374U00000X"
    VALUE_376_J00000_X = "376J00000X"
    VALUE_376_K00000_X = "376K00000X"
    VALUE_376_G00000_X = "376G00000X"
    VALUE_310400000_X = "310400000X"
    VALUE_3104_A0630_X = "3104A0630X"
    VALUE_3104_A0625_X = "3104A0625X"
    VALUE_311_Z00000_X = "311Z00000X"
    VALUE_311_ZA0620_X = "311ZA0620X"
    VALUE_314000000_X = "314000000X"
    VALUE_3140_N1450_X = "3140N1450X"
    VALUE_310000000_X = "310000000X"
    VALUE_311500000_X = "311500000X"
    VALUE_317400000_X = "317400000X"
    VALUE_315_D00000_X = "315D00000X"
    VALUE_315_P00000_X = "315P00000X"
    VALUE_310500000_X = "310500000X"
    VALUE_313_M00000_X = "313M00000X"
    VALUE_171_W00000_X = "171W00000X"
    VALUE_171_WH0202_X = "171WH0202X"
    VALUE_171_WV0202_X = "171WV0202X"
    VALUE_174_M00000_X = "174M00000X"
    VALUE_174_MM1900_X = "174MM1900X"
    VALUE_174400000_X = "174400000X"
    VALUE_1744_G0900_X = "1744G0900X"
    VALUE_1744_P3200_X = "1744P3200X"
    VALUE_1744_R1103_X = "1744R1103X"
    VALUE_1744_R1102_X = "1744R1102X"
    VALUE_170000000_X = "170000000X"
    VALUE_171100000_X = "171100000X"
    VALUE_172_A00000_X = "172A00000X"
    VALUE_176_P00000_X = "176P00000X"
    VALUE_175_L00000_X = "175L00000X"
    VALUE_173000000_X = "173000000X"
    VALUE_177_F00000_X = "177F00000X"
    VALUE_176_B00000_X = "176B00000X"
    VALUE_175_M00000_X = "175M00000X"
    VALUE_175_F00000_X = "175F00000X"
    VALUE_170100000_X = "170100000X"
    VALUE_183500000_X = "183500000X"
    VALUE_1835_G0000_X = "1835G0000X"
    VALUE_1835_N0905_X = "1835N0905X"
    VALUE_1835_N1003_X = "1835N1003X"
    VALUE_1835_P1200_X = "1835P1200X"
    VALUE_1835_P1300_X = "1835P1300X"
    VALUE_180000000_X = "180000000X"
    VALUE_183700000_X = "183700000X"
    VALUE_364_S00000_X = "364S00000X"
    VALUE_364_SA2100_X = "364SA2100X"
    VALUE_364_SA2200_X = "364SA2200X"
    VALUE_364_SC2300_X = "364SC2300X"
    VALUE_364_SC1501_X = "364SC1501X"
    VALUE_364_SC0200_X = "364SC0200X"
    VALUE_364_SE0003_X = "364SE0003X"
    VALUE_364_SE1400_X = "364SE1400X"
    VALUE_364_SF0001_X = "364SF0001X"
    VALUE_364_SG0600_X = "364SG0600X"
    VALUE_364_SH1100_X = "364SH1100X"
    VALUE_364_SH0200_X = "364SH0200X"
    VALUE_364_SI0800_X = "364SI0800X"
    VALUE_364_SL0600_X = "364SL0600X"
    VALUE_364_SM0705_X = "364SM0705X"
    VALUE_364_SN0000_X = "364SN0000X"
    VALUE_364_SN0800_X = "364SN0800X"
    VALUE_364_SX0106_X = "364SX0106X"
    VALUE_364_SX0200_X = "364SX0200X"
    VALUE_364_SX0204_X = "364SX0204X"
    VALUE_364_SP0200_X = "364SP0200X"
    VALUE_364_SP1700_X = "364SP1700X"
    VALUE_364_SP2800_X = "364SP2800X"
    VALUE_364_SP0808_X = "364SP0808X"
    VALUE_364_SP0809_X = "364SP0809X"
    VALUE_364_SP0807_X = "364SP0807X"
    VALUE_364_SP0810_X = "364SP0810X"
    VALUE_364_SP0811_X = "364SP0811X"
    VALUE_364_SP0812_X = "364SP0812X"
    VALUE_364_SP0813_X = "364SP0813X"
    VALUE_364_SR0400_X = "364SR0400X"
    VALUE_364_SS0200_X = "364SS0200X"
    VALUE_364_ST0500_X = "364ST0500X"
    VALUE_364_SW0102_X = "364SW0102X"
    VALUE_363_A00000_X = "363A00000X"
    VALUE_363_AM0700_X = "363AM0700X"
    VALUE_363_AS0400_X = "363AS0400X"
    VALUE_363_L00000_X = "363L00000X"
    VALUE_363_LA2100_X = "363LA2100X"
    VALUE_363_LA2200_X = "363LA2200X"
    VALUE_363_LC1500_X = "363LC1500X"
    VALUE_363_LC0200_X = "363LC0200X"
    VALUE_363_LF0000_X = "363LF0000X"
    VALUE_363_LG0600_X = "363LG0600X"
    VALUE_363_LN0000_X = "363LN0000X"
    VALUE_363_LN0005_X = "363LN0005X"
    VALUE_363_LX0001_X = "363LX0001X"
    VALUE_363_LX0106_X = "363LX0106X"
    VALUE_363_LP0200_X = "363LP0200X"
    VALUE_363_LP0222_X = "363LP0222X"
    VALUE_363_LP1700_X = "363LP1700X"
    VALUE_363_LP2300_X = "363LP2300X"
    VALUE_363_LP0808_X = "363LP0808X"
    VALUE_363_LS0200_X = "363LS0200X"
    VALUE_363_LW0102_X = "363LW0102X"
    VALUE_360000000_X = "360000000X"
    VALUE_367_H00000_X = "367H00000X"
    VALUE_367_A00000_X = "367A00000X"
    VALUE_367500000_X = "367500000X"
    VALUE_213_E00000_X = "213E00000X"
    VALUE_213_EG0000_X = "213EG0000X"
    VALUE_213_EP1101_X = "213EP1101X"
    VALUE_213_EP0504_X = "213EP0504X"
    VALUE_213_ER0200_X = "213ER0200X"
    VALUE_213_ES0000_X = "213ES0000X"
    VALUE_213_ES0131_X = "213ES0131X"
    VALUE_213_ES0103_X = "213ES0103X"
    VALUE_210000000_X = "210000000X"
    VALUE_211_D00000_X = "211D00000X"
    VALUE_324500000_X = "324500000X"
    VALUE_3245_S0500_X = "3245S0500X"
    VALUE_320000000_X = "320000000X"
    VALUE_320800000_X = "320800000X"
    VALUE_320900000_X = "320900000X"
    VALUE_323_P00000_X = "323P00000X"
    VALUE_322_D00000_X = "322D00000X"
    VALUE_320600000_X = "320600000X"
    VALUE_320700000_X = "320700000X"
    VALUE_225_X00000_X = "225X00000X"
    VALUE_225_XE1200_X = "225XE1200X"
    VALUE_225_XH1200_X = "225XH1200X"
    VALUE_225_XH1300_X = "225XH1300X"
    VALUE_225_XN1300_X = "225XN1300X"
    VALUE_225_XP0200_X = "225XP0200X"
    VALUE_225_XR0403_X = "225XR0403X"
    VALUE_225100000_X = "225100000X"
    VALUE_2251_C2600_X = "2251C2600X"
    VALUE_2251_E1300_X = "2251E1300X"
    VALUE_2251_E1200_X = "2251E1200X"
    VALUE_2251_G0304_X = "2251G0304X"
    VALUE_2251_H1200_X = "2251H1200X"
    VALUE_2251_H1300_X = "2251H1300X"
    VALUE_2251_N0400_X = "2251N0400X"
    VALUE_2251_X0800_X = "2251X0800X"
    VALUE_2251_P0200_X = "2251P0200X"
    VALUE_2251_S0007_X = "2251S0007X"
    VALUE_225_C00000_X = "225C00000X"
    VALUE_225_CA2400_X = "225CA2400X"
    VALUE_225_CA2500_X = "225CA2500X"
    VALUE_227800000_X = "227800000X"
    VALUE_2278_C0205_X = "2278C0205X"
    VALUE_2278_E0002_X = "2278E0002X"
    VALUE_2278_G1100_X = "2278G1100X"
    VALUE_2278_G0305_X = "2278G0305X"
    VALUE_2278_H0200_X = "2278H0200X"
    VALUE_2278_P3900_X = "2278P3900X"
    VALUE_2278_P3800_X = "2278P3800X"
    VALUE_2278_E1000_X = "2278E1000X"
    VALUE_2278_P4000_X = "2278P4000X"
    VALUE_2278_P1004_X = "2278P1004X"
    VALUE_2278_P1006_X = "2278P1006X"
    VALUE_2278_P1005_X = "2278P1005X"
    VALUE_2278_S1500_X = "2278S1500X"
    VALUE_227900000_X = "227900000X"
    VALUE_2279_C0205_X = "2279C0205X"
    VALUE_2279_E0002_X = "2279E0002X"
    VALUE_2279_G1100_X = "2279G1100X"
    VALUE_2279_G0305_X = "2279G0305X"
    VALUE_2279_H0200_X = "2279H0200X"
    VALUE_2279_P3900_X = "2279P3900X"
    VALUE_2279_P3800_X = "2279P3800X"
    VALUE_2279_E1000_X = "2279E1000X"
    VALUE_2279_P4000_X = "2279P4000X"
    VALUE_2279_P1004_X = "2279P1004X"
    VALUE_2279_P1006_X = "2279P1006X"
    VALUE_2279_P1005_X = "2279P1005X"
    VALUE_2279_S1500_X = "2279S1500X"
    VALUE_225500000_X = "225500000X"
    VALUE_2255_A2300_X = "2255A2300X"
    VALUE_2255_R0406_X = "2255R0406X"
    VALUE_220000000_X = "220000000X"
    VALUE_221700000_X = "221700000X"
    VALUE_225600000_X = "225600000X"
    VALUE_226300000_X = "226300000X"
    VALUE_225700000_X = "225700000X"
    VALUE_225_A00000_X = "225A00000X"
    VALUE_224_Z00000_X = "224Z00000X"
    VALUE_225000000_X = "225000000X"
    VALUE_222_Z00000_X = "222Z00000X"
    VALUE_225200000_X = "225200000X"
    VALUE_224_P00000_X = "224P00000X"
    VALUE_225_B00000_X = "225B00000X"
    VALUE_225800000_X = "225800000X"
    VALUE_225400000_X = "225400000X"
    VALUE_385_H00000_X = "385H00000X"
    VALUE_385_HR2050_X = "385HR2050X"
    VALUE_385_HR2055_X = "385HR2055X"
    VALUE_385_HR2060_X = "385HR2060X"
    VALUE_385_HR2065_X = "385HR2065X"
    VALUE_380000000_X = "380000000X"
    VALUE_231_H00000_X = "231H00000X"
    VALUE_231_HA2400_X = "231HA2400X"
    VALUE_231_HA2500_X = "231HA2500X"
    VALUE_235500000_X = "235500000X"
    VALUE_2355_A2700_X = "2355A2700X"
    VALUE_2355_S0801_X = "2355S0801X"
    VALUE_230000000_X = "230000000X"
    VALUE_237600000_X = "237600000X"
    VALUE_237700000_X = "237700000X"
    VALUE_235_Z00000_X = "235Z00000X"
    VALUE_332_B00000_X = "332B00000X"
    VALUE_332_BC3200_X = "332BC3200X"
    VALUE_332_BD1200_X = "332BD1200X"
    VALUE_332_BN1400_X = "332BN1400X"
    VALUE_332_BX2000_X = "332BX2000X"
    VALUE_332_BP3500_X = "332BP3500X"
    VALUE_330000000_X = "330000000X"
    VALUE_331_L00000_X = "331L00000X"
    VALUE_332_G00000_X = "332G00000X"
    VALUE_332_H00000_X = "332H00000X"
    VALUE_332_S00000_X = "332S00000X"
    VALUE_332_U00000_X = "332U00000X"
    VALUE_335_U00000_X = "335U00000X"
    VALUE_333600000_X = "333600000X"
    VALUE_335_V00000_X = "335V00000X"
    VALUE_335_E00000_X = "335E00000X"
    VALUE_247100000_X = "247100000X"
    VALUE_2471_B0102_X = "2471B0102X"
    VALUE_2471_C1106_X = "2471C1106X"
    VALUE_2471_C1101_X = "2471C1101X"
    VALUE_2471_C3401_X = "2471C3401X"
    VALUE_2471_M1202_X = "2471M1202X"
    VALUE_2471_M2300_X = "2471M2300X"
    VALUE_2471_N0900_X = "2471N0900X"
    VALUE_2471_Q0001_X = "2471Q0001X"
    VALUE_2471_R0002_X = "2471R0002X"
    VALUE_2471_C3402_X = "2471C3402X"
    VALUE_2471_S1302_X = "2471S1302X"
    VALUE_2471_V0105_X = "2471V0105X"
    VALUE_2471_V0106_X = "2471V0106X"
    VALUE_246_X00000_X = "246X00000X"
    VALUE_246_XC2901_X = "246XC2901X"
    VALUE_246_XS1301_X = "246XS1301X"
    VALUE_246_XC2903_X = "246XC2903X"
    VALUE_246_Y00000_X = "246Y00000X"
    VALUE_246_YC3301_X = "246YC3301X"
    VALUE_246_YC3302_X = "246YC3302X"
    VALUE_246_YR1600_X = "246YR1600X"
    VALUE_246_Z00000_X = "246Z00000X"
    VALUE_246_ZA2600_X = "246ZA2600X"
    VALUE_246_ZB0500_X = "246ZB0500X"
    VALUE_246_ZB0301_X = "246ZB0301X"
    VALUE_246_ZB0302_X = "246ZB0302X"
    VALUE_246_ZB0600_X = "246ZB0600X"
    VALUE_246_ZE0500_X = "246ZE0500X"
    VALUE_246_ZE0600_X = "246ZE0600X"
    VALUE_246_ZG1000_X = "246ZG1000X"
    VALUE_246_ZG0701_X = "246ZG0701X"
    VALUE_246_ZI1000_X = "246ZI1000X"
    VALUE_246_ZN0300_X = "246ZN0300X"
    VALUE_246_ZS0400_X = "246ZS0400X"
    VALUE_246_Q00000_X = "246Q00000X"
    VALUE_246_QB0000_X = "246QB0000X"
    VALUE_246_QC1000_X = "246QC1000X"
    VALUE_246_QC2700_X = "246QC2700X"
    VALUE_246_QH0401_X = "246QH0401X"
    VALUE_246_QH0000_X = "246QH0000X"
    VALUE_246_QH0600_X = "246QH0600X"
    VALUE_246_QI0000_X = "246QI0000X"
    VALUE_246_QL0900_X = "246QL0900X"
    VALUE_246_QL0901_X = "246QL0901X"
    VALUE_246_QM0706_X = "246QM0706X"
    VALUE_246_QM0900_X = "246QM0900X"
    VALUE_247000000_X = "247000000X"
    VALUE_2470_A2800_X = "2470A2800X"
    VALUE_247200000_X = "247200000X"
    VALUE_2472_B0301_X = "2472B0301X"
    VALUE_2472_D0500_X = "2472D0500X"
    VALUE_2472_E0500_X = "2472E0500X"
    VALUE_2472_R0900_X = "2472R0900X"
    VALUE_2472_V0600_X = "2472V0600X"
    VALUE_246_R00000_X = "246R00000X"
    VALUE_246_RH0600_X = "246RH0600X"
    VALUE_246_RM2200_X = "246RM2200X"
    VALUE_246_RP1900_X = "246RP1900X"
    VALUE_240000000_X = "240000000X"
    VALUE_246_W00000_X = "246W00000X"
    VALUE_341600000_X = "341600000X"
    VALUE_3416_A0800_X = "3416A0800X"
    VALUE_3416_L0300_X = "3416L0300X"
    VALUE_3416_S0300_X = "3416S0300X"
    VALUE_340000000_X = "340000000X"
    VALUE_347_B00000_X = "347B00000X"
    VALUE_343900000_X = "343900000X"
    VALUE_347_C00000_X = "347C00000X"
    VALUE_343800000_X = "343800000X"
    VALUE_344600000_X = "344600000X"
    VALUE_347_D00000_X = "347D00000X"
    VALUE_347_E00000_X = "347E00000X"


class PsychiatryandNeurologyProviderCodes(Enum):
    """
    specDomain: S20239 (C-0-T19465-S20096-S20239-cpt)
    :cvar VALUE_208400000_X:
    :cvar VALUE_2084_A0401_X:
    :cvar VALUE_2084_P0802_X:
    :cvar VALUE_2084_P0804_X:
    :cvar VALUE_2084_N0600_X:
    :cvar VALUE_2084_F0202_X:
    :cvar VALUE_2084_P0805_X:
    :cvar VALUE_2084_P0005_X:
    :cvar VALUE_2084_N0400_X:
    :cvar VALUE_2084_N0402_X:
    :cvar VALUE_2084_P2900_X:
    :cvar VALUE_2084_P0800_X:
    :cvar VALUE_2084_S0010_X:
    :cvar VALUE_2084_V0102_X:
    """
    VALUE_208400000_X = "208400000X"
    VALUE_2084_A0401_X = "2084A0401X"
    VALUE_2084_P0802_X = "2084P0802X"
    VALUE_2084_P0804_X = "2084P0804X"
    VALUE_2084_N0600_X = "2084N0600X"
    VALUE_2084_F0202_X = "2084F0202X"
    VALUE_2084_P0805_X = "2084P0805X"
    VALUE_2084_P0005_X = "2084P0005X"
    VALUE_2084_N0400_X = "2084N0400X"
    VALUE_2084_N0402_X = "2084N0402X"
    VALUE_2084_P2900_X = "2084P2900X"
    VALUE_2084_P0800_X = "2084P0800X"
    VALUE_2084_S0010_X = "2084S0010X"
    VALUE_2084_V0102_X = "2084V0102X"


class PsychoanalystHipaa(Enum):
    """
    specDomain: S13149 (C-0-T13129-A13130-A13131-S13149-cpt)
    :cvar VALUE_103_S00000_N:
    :cvar VALUE_103_SA1800_N:
    :cvar VALUE_103_SA1400_N:
    """
    VALUE_103_S00000_N = "103S00000N"
    VALUE_103_SA1800_N = "103SA1800N"
    VALUE_103_SA1400_N = "103SA1400N"


class PsychologistHipaa(Enum):
    """
    specDomain: S13152 (C-0-T13129-A13130-A13131-S13152-cpt)
    :cvar VALUE_103_T00000_N:
    :cvar VALUE_103_TA0400_N:
    :cvar VALUE_103_TA0700_N:
    :cvar VALUE_103_TB0200_N:
    :cvar VALUE_103_TC2200_N:
    :cvar VALUE_103_TC0700_N:
    :cvar VALUE_103_TC1900_N:
    :cvar VALUE_103_TE1000_N:
    :cvar VALUE_103_TE1100_N:
    :cvar VALUE_103_TF0000_N:
    :cvar VALUE_103_TF0200_N:
    :cvar VALUE_103_TH0100_N:
    :cvar VALUE_103_TM1700_N:
    :cvar VALUE_103_TM1800_N:
    :cvar VALUE_103_TP2700_N:
    :cvar VALUE_103_TP2701_N:
    :cvar VALUE_103_TR0400_N:
    :cvar VALUE_103_TS0200_N:
    :cvar VALUE_103_TW0100_N:
    """
    VALUE_103_T00000_N = "103T00000N"
    VALUE_103_TA0400_N = "103TA0400N"
    VALUE_103_TA0700_N = "103TA0700N"
    VALUE_103_TB0200_N = "103TB0200N"
    VALUE_103_TC2200_N = "103TC2200N"
    VALUE_103_TC0700_N = "103TC0700N"
    VALUE_103_TC1900_N = "103TC1900N"
    VALUE_103_TE1000_N = "103TE1000N"
    VALUE_103_TE1100_N = "103TE1100N"
    VALUE_103_TF0000_N = "103TF0000N"
    VALUE_103_TF0200_N = "103TF0200N"
    VALUE_103_TH0100_N = "103TH0100N"
    VALUE_103_TM1700_N = "103TM1700N"
    VALUE_103_TM1800_N = "103TM1800N"
    VALUE_103_TP2700_N = "103TP2700N"
    VALUE_103_TP2701_N = "103TP2701N"
    VALUE_103_TR0400_N = "103TR0400N"
    VALUE_103_TS0200_N = "103TS0200N"
    VALUE_103_TW0100_N = "103TW0100N"


class PsychologistProviderCodes(Enum):
    """
    specDomain: S20285 (C-0-T19465-S20275-S20285-cpt)
    :cvar VALUE_103_T00000_X:
    :cvar VALUE_103_TA0400_X:
    :cvar VALUE_103_TA0700_X:
    :cvar VALUE_103_TB0200_X:
    :cvar VALUE_103_TC2200_X:
    :cvar VALUE_103_TC0700_X:
    :cvar VALUE_103_TC1900_X:
    :cvar VALUE_103_TE1000_X:
    :cvar VALUE_103_TE1100_X:
    :cvar VALUE_103_TF0000_X:
    :cvar VALUE_103_TF0200_X:
    :cvar VALUE_103_TH0100_X:
    :cvar VALUE_103_TM1700_X:
    :cvar VALUE_103_TM1800_X:
    :cvar VALUE_103_TP0814_X:
    :cvar VALUE_103_TP2700_X:
    :cvar VALUE_103_TP2701_X:
    :cvar VALUE_103_TR0400_X:
    :cvar VALUE_103_TS0200_X:
    :cvar VALUE_103_TW0100_X:
    """
    VALUE_103_T00000_X = "103T00000X"
    VALUE_103_TA0400_X = "103TA0400X"
    VALUE_103_TA0700_X = "103TA0700X"
    VALUE_103_TB0200_X = "103TB0200X"
    VALUE_103_TC2200_X = "103TC2200X"
    VALUE_103_TC0700_X = "103TC0700X"
    VALUE_103_TC1900_X = "103TC1900X"
    VALUE_103_TE1000_X = "103TE1000X"
    VALUE_103_TE1100_X = "103TE1100X"
    VALUE_103_TF0000_X = "103TF0000X"
    VALUE_103_TF0200_X = "103TF0200X"
    VALUE_103_TH0100_X = "103TH0100X"
    VALUE_103_TM1700_X = "103TM1700X"
    VALUE_103_TM1800_X = "103TM1800X"
    VALUE_103_TP0814_X = "103TP0814X"
    VALUE_103_TP2700_X = "103TP2700X"
    VALUE_103_TP2701_X = "103TP2701X"
    VALUE_103_TR0400_X = "103TR0400X"
    VALUE_103_TS0200_X = "103TS0200X"
    VALUE_103_TW0100_X = "103TW0100X"


class PublicHealthcareProgram(Enum):
    """
    specDomain: S19718 (C-0-T13953-A13954-A19855-A19858-S19718-cpt)
    :cvar DISEASEPRG:
    :cvar HIVAIDS:
    :cvar CANPRG:
    :cvar ENDRENAL:
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    :cvar PUBLICPOL:
    :cvar DENTPRG:
    :cvar MANDPOL:
    :cvar MENTPRG:
    :cvar SAFNET:
    :cvar SUBPRG:
    """
    DISEASEPRG = "DISEASEPRG"
    HIVAIDS = "HIVAIDS"
    CANPRG = "CANPRG"
    ENDRENAL = "ENDRENAL"
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"
    PUBLICPOL = "PUBLICPOL"
    DENTPRG = "DENTPRG"
    MANDPOL = "MANDPOL"
    MENTPRG = "MENTPRG"
    SAFNET = "SAFNET"
    SUBPRG = "SUBPRG"


class PulmonaryRoute(Enum):
    """
    abstDomain: A17304 (C-0-T14581-A17021-A17304-cpt)
    :cvar IPPB:
    :cvar VENT:
    :cvar VENTMASK:
    :cvar ETINSTL:
    :cvar NTT:
    :cvar ETNEB:
    """
    IPPB = "IPPB"
    VENT = "VENT"
    VENTMASK = "VENTMASK"
    ETINSTL = "ETINSTL"
    NTT = "NTT"
    ETNEB = "ETNEB"


class QualitySpecimenRoleType(Enum):
    """
    specDomain: S16521 (C-0-T12206-A16515-S16521-cpt)
    :cvar Q:
    :cvar B:
    :cvar E:
    :cvar F:
    :cvar O:
    :cvar V:
    """
    Q = "Q"
    B = "B"
    E = "E"
    F = "F"
    O = "O"
    V = "V"


class QueryParameterValue(Enum):
    """
    vocSet: T19726 (C-0-T19726-cpt)
    :cvar ISSFA:
    :cvar ISSFI:
    :cvar ISSFU:
    :cvar C:
    :cvar R:
    :cvar N:
    """
    ISSFA = "ISSFA"
    ISSFI = "ISSFI"
    ISSFU = "ISSFU"
    C = "C"
    R = "R"
    N = "N"


class QueryPriority(Enum):
    """
    vocSet: T91 (C-0-T91-cpt)
    :cvar D:
    :cvar I:
    """
    D = "D"
    I = "I"


class QueryQuantityUnit(Enum):
    """
    vocSet: T126 (C-0-T126-cpt)
    :cvar CH:
    :cvar LI:
    :cvar PG:
    :cvar RD:
    """
    CH = "CH"
    LI = "LI"
    PG = "PG"
    RD = "RD"


class QueryRequestLimit(Enum):
    """
    vocSet: T19911 (C-0-T19911-cpt)
    :cvar RD:
    """
    RD = "RD"


class QueryResponse(Enum):
    """
    vocSet: T208 (C-0-T208-cpt)
    :cvar AE:
    :cvar OK:
    :cvar NF:
    :cvar QE:
    """
    AE = "AE"
    OK = "OK"
    NF = "NF"
    QE = "QE"


class QueryStatusCode(Enum):
    """
    vocSet: T18899 (C-0-T18899-cpt)
    :cvar ABORTED:
    :cvar DELIVERED_RESPONSE:
    :cvar EXECUTING:
    :cvar NEW:
    :cvar WAIT_CONTINUED_QUERY_RESPONSE:
    """
    ABORTED = "aborted"
    DELIVERED_RESPONSE = "deliveredResponse"
    EXECUTING = "executing"
    NEW = "new"
    WAIT_CONTINUED_QUERY_RESPONSE = "waitContinuedQueryResponse"


class RoioverlayShape(Enum):
    """
    abstDomain: A16117 (C-0-T13953-A13954-A16117-cpt)
    :cvar CIRCLE:
    :cvar ELLIPSE:
    :cvar POINT:
    :cvar POLY:
    """
    CIRCLE = "CIRCLE"
    ELLIPSE = "ELLIPSE"
    POINT = "POINT"
    POLY = "POLY"


class Race(Enum):
    """
    vocSet: T14914 (C-0-T14914-cpt)
    :cvar VALUE_2028_9:
    :cvar VALUE_2029_7:
    :cvar VALUE_2030_5:
    :cvar VALUE_2031_3:
    :cvar VALUE_2032_1:
    :cvar VALUE_2033_9:
    :cvar VALUE_2034_7:
    :cvar VALUE_2036_2:
    :cvar VALUE_2037_0:
    :cvar VALUE_2038_8:
    :cvar VALUE_2048_7:
    :cvar VALUE_2039_6:
    :cvar VALUE_2040_4:
    :cvar VALUE_2041_2:
    :cvar VALUE_2052_9:
    :cvar VALUE_2042_0:
    :cvar VALUE_2049_5:
    :cvar VALUE_2050_3:
    :cvar VALUE_2043_8:
    :cvar VALUE_2044_6:
    :cvar VALUE_2051_1:
    :cvar VALUE_2045_3:
    :cvar VALUE_2035_4:
    :cvar VALUE_2046_1:
    :cvar VALUE_2047_9:
    :cvar VALUE_2060_2:
    :cvar VALUE_2061_0:
    :cvar VALUE_2062_8:
    :cvar VALUE_2063_6:
    :cvar VALUE_2064_4:
    :cvar VALUE_2065_1:
    :cvar VALUE_2066_9:
    :cvar VALUE_2054_5:
    :cvar VALUE_2058_6:
    :cvar VALUE_2067_7:
    :cvar VALUE_2068_5:
    :cvar VALUE_2056_0:
    :cvar VALUE_2070_1:
    :cvar VALUE_2069_3:
    :cvar VALUE_2071_9:
    :cvar VALUE_2072_7:
    :cvar VALUE_2073_5:
    :cvar VALUE_2074_3:
    :cvar VALUE_2075_0:
    :cvar VALUE_2100_6:
    :cvar VALUE_2101_4:
    :cvar VALUE_2104_8:
    :cvar VALUE_2102_2:
    :cvar VALUE_2103_0:
    :cvar VALUE_2085_9:
    :cvar VALUE_2092_5:
    :cvar VALUE_2088_3:
    :cvar VALUE_2097_4:
    :cvar VALUE_2087_5:
    :cvar VALUE_2086_7:
    :cvar VALUE_2096_6:
    :cvar VALUE_2093_3:
    :cvar VALUE_2089_1:
    :cvar VALUE_2090_9:
    :cvar VALUE_2091_7:
    :cvar VALUE_2094_1:
    :cvar VALUE_2095_8:
    :cvar VALUE_2098_2:
    :cvar VALUE_2078_4:
    :cvar VALUE_2079_2:
    :cvar VALUE_2080_0:
    :cvar VALUE_2081_8:
    :cvar VALUE_2083_4:
    :cvar VALUE_2082_6:
    :cvar VALUE_2076_8:
    :cvar VALUE_2500_7:
    :cvar VALUE_1739_2:
    :cvar VALUE_1740_0:
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    :cvar VALUE_1811_9:
    :cvar VALUE_1737_6:
    :cvar VALUE_1968_7:
    :cvar VALUE_1969_5:
    :cvar VALUE_1970_3:
    :cvar VALUE_1972_9:
    :cvar VALUE_1973_7:
    :cvar VALUE_1974_5:
    :cvar VALUE_1975_2:
    :cvar VALUE_1976_0:
    :cvar VALUE_1977_8:
    :cvar VALUE_1978_6:
    :cvar VALUE_1979_4:
    :cvar VALUE_1980_2:
    :cvar VALUE_1981_0:
    :cvar VALUE_1982_8:
    :cvar VALUE_1984_4:
    :cvar VALUE_1985_1:
    :cvar VALUE_1986_9:
    :cvar VALUE_1987_7:
    :cvar VALUE_1988_5:
    :cvar VALUE_1992_7:
    :cvar VALUE_1994_3:
    :cvar VALUE_1993_5:
    :cvar VALUE_1995_0:
    :cvar VALUE_1996_8:
    :cvar VALUE_1997_6:
    :cvar VALUE_1998_4:
    :cvar VALUE_1999_2:
    :cvar VALUE_2000_8:
    :cvar VALUE_2006_5:
    :cvar VALUE_2007_3:
    :cvar VALUE_2008_1:
    :cvar VALUE_2009_9:
    :cvar VALUE_2010_7:
    :cvar VALUE_2011_5:
    :cvar VALUE_2012_3:
    :cvar VALUE_2013_1:
    :cvar VALUE_2015_6:
    :cvar VALUE_2014_9:
    :cvar VALUE_2016_4:
    :cvar VALUE_2017_2:
    :cvar VALUE_2018_0:
    :cvar VALUE_2019_8:
    :cvar VALUE_2020_6:
    :cvar VALUE_2023_0:
    :cvar VALUE_2024_8:
    :cvar VALUE_2021_4:
    :cvar VALUE_2022_2:
    :cvar VALUE_2025_5:
    :cvar VALUE_2026_3:
    :cvar VALUE_1966_1:
    :cvar VALUE_1990_1:
    :cvar VALUE_2002_4:
    :cvar VALUE_2004_0:
    :cvar VALUE_1844_0:
    :cvar VALUE_1845_7:
    :cvar VALUE_1846_5:
    :cvar VALUE_1847_3:
    :cvar VALUE_1849_9:
    :cvar VALUE_1848_1:
    :cvar VALUE_1850_7:
    :cvar VALUE_1851_5:
    :cvar VALUE_1852_3:
    :cvar VALUE_1853_1:
    :cvar VALUE_1854_9:
    :cvar VALUE_1855_6:
    :cvar VALUE_1856_4:
    :cvar VALUE_1857_2:
    :cvar VALUE_1858_0:
    :cvar VALUE_1859_8:
    :cvar VALUE_1860_6:
    :cvar VALUE_1861_4:
    :cvar VALUE_1862_2:
    :cvar VALUE_1863_0:
    :cvar VALUE_1864_8:
    :cvar VALUE_1865_5:
    :cvar VALUE_1866_3:
    :cvar VALUE_1867_1:
    :cvar VALUE_1868_9:
    :cvar VALUE_1869_7:
    :cvar VALUE_1889_5:
    :cvar VALUE_1870_5:
    :cvar VALUE_1871_3:
    :cvar VALUE_1872_1:
    :cvar VALUE_1873_9:
    :cvar VALUE_1874_7:
    :cvar VALUE_1875_4:
    :cvar VALUE_1876_2:
    :cvar VALUE_1877_0:
    :cvar VALUE_1878_8:
    :cvar VALUE_1879_6:
    :cvar VALUE_1880_4:
    :cvar VALUE_1881_2:
    :cvar VALUE_1882_0:
    :cvar VALUE_1883_8:
    :cvar VALUE_1884_6:
    :cvar VALUE_1885_3:
    :cvar VALUE_1886_1:
    :cvar VALUE_1887_9:
    :cvar VALUE_1888_7:
    :cvar VALUE_1891_1:
    :cvar VALUE_1892_9:
    :cvar VALUE_1893_7:
    :cvar VALUE_1894_5:
    :cvar VALUE_1896_0:
    :cvar VALUE_1897_8:
    :cvar VALUE_1898_6:
    :cvar VALUE_1899_4:
    :cvar VALUE_1900_0:
    :cvar VALUE_1901_8:
    :cvar VALUE_1902_6:
    :cvar VALUE_1903_4:
    :cvar VALUE_1904_2:
    :cvar VALUE_1905_9:
    :cvar VALUE_1906_7:
    :cvar VALUE_1907_5:
    :cvar VALUE_1908_3:
    :cvar VALUE_1909_1:
    :cvar VALUE_1910_9:
    :cvar VALUE_1911_7:
    :cvar VALUE_1912_5:
    :cvar VALUE_1913_3:
    :cvar VALUE_1914_1:
    :cvar VALUE_1915_8:
    :cvar VALUE_1916_6:
    :cvar VALUE_1917_4:
    :cvar VALUE_1962_0:
    :cvar VALUE_1918_2:
    :cvar VALUE_1919_0:
    :cvar VALUE_1920_8:
    :cvar VALUE_1921_6:
    :cvar VALUE_1922_4:
    :cvar VALUE_1923_2:
    :cvar VALUE_1924_0:
    :cvar VALUE_1925_7:
    :cvar VALUE_1926_5:
    :cvar VALUE_1927_3:
    :cvar VALUE_1928_1:
    :cvar VALUE_1929_9:
    :cvar VALUE_1930_7:
    :cvar VALUE_1931_5:
    :cvar VALUE_1932_3:
    :cvar VALUE_1933_1:
    :cvar VALUE_1934_9:
    :cvar VALUE_1935_6:
    :cvar VALUE_1937_2:
    :cvar VALUE_1938_0:
    :cvar VALUE_1936_4:
    :cvar VALUE_1940_6:
    :cvar VALUE_1939_8:
    :cvar VALUE_1941_4:
    :cvar VALUE_1942_2:
    :cvar VALUE_1943_0:
    :cvar VALUE_1944_8:
    :cvar VALUE_1945_5:
    :cvar VALUE_1946_3:
    :cvar VALUE_1947_1:
    :cvar VALUE_1948_9:
    :cvar VALUE_1949_7:
    :cvar VALUE_1950_5:
    :cvar VALUE_1952_1:
    :cvar VALUE_1953_9:
    :cvar VALUE_1954_7:
    :cvar VALUE_1963_8:
    :cvar VALUE_1951_3:
    :cvar VALUE_1955_4:
    :cvar VALUE_1956_2:
    :cvar VALUE_1957_0:
    :cvar VALUE_1958_8:
    :cvar VALUE_1959_6:
    :cvar VALUE_1960_4:
    :cvar VALUE_1961_2:
    :cvar VALUE_1964_6:
    :cvar VALUE_1840_8:
    :cvar VALUE_1842_4:
    :cvar VALUE_1735_0:
    :cvar VALUE_1076_9:
    :cvar VALUE_1744_2:
    :cvar VALUE_1741_8:
    :cvar VALUE_1742_6:
    :cvar VALUE_1743_4:
    :cvar VALUE_1745_9:
    :cvar VALUE_1746_7:
    :cvar VALUE_1747_5:
    :cvar VALUE_1748_3:
    :cvar VALUE_1749_1:
    :cvar VALUE_1750_9:
    :cvar VALUE_1751_7:
    :cvar VALUE_1752_5:
    :cvar VALUE_1753_3:
    :cvar VALUE_1754_1:
    :cvar VALUE_1755_8:
    :cvar VALUE_1756_6:
    :cvar VALUE_1757_4:
    :cvar VALUE_1758_2:
    :cvar VALUE_1759_0:
    :cvar VALUE_1760_8:
    :cvar VALUE_1761_6:
    :cvar VALUE_1762_4:
    :cvar VALUE_1763_2:
    :cvar VALUE_1764_0:
    :cvar VALUE_1765_7:
    :cvar VALUE_1766_5:
    :cvar VALUE_1767_3:
    :cvar VALUE_1768_1:
    :cvar VALUE_1769_9:
    :cvar VALUE_1770_7:
    :cvar VALUE_1771_5:
    :cvar VALUE_1772_3:
    :cvar VALUE_1773_1:
    :cvar VALUE_1774_9:
    :cvar VALUE_1775_6:
    :cvar VALUE_1776_4:
    :cvar VALUE_1777_2:
    :cvar VALUE_1778_0:
    :cvar VALUE_1780_6:
    :cvar VALUE_1779_8:
    :cvar VALUE_1781_4:
    :cvar VALUE_1782_2:
    :cvar VALUE_1783_0:
    :cvar VALUE_1784_8:
    :cvar VALUE_1785_5:
    :cvar VALUE_1786_3:
    :cvar VALUE_1787_1:
    :cvar VALUE_1788_9:
    :cvar VALUE_1789_7:
    :cvar VALUE_1790_5:
    :cvar VALUE_1791_3:
    :cvar VALUE_1792_1:
    :cvar VALUE_1793_9:
    :cvar VALUE_1795_4:
    :cvar VALUE_1794_7:
    :cvar VALUE_1796_2:
    :cvar VALUE_1797_0:
    :cvar VALUE_1798_8:
    :cvar VALUE_1799_6:
    :cvar VALUE_1800_2:
    :cvar VALUE_1801_0:
    :cvar VALUE_1802_8:
    :cvar VALUE_1803_6:
    :cvar VALUE_1804_4:
    :cvar VALUE_1805_1:
    :cvar VALUE_1806_9:
    :cvar VALUE_1807_7:
    :cvar VALUE_1808_5:
    :cvar VALUE_1809_3:
    :cvar VALUE_1010_8:
    :cvar VALUE_1011_6:
    :cvar VALUE_1012_4:
    :cvar VALUE_1013_2:
    :cvar VALUE_1014_0:
    :cvar VALUE_1015_7:
    :cvar VALUE_1016_5:
    :cvar VALUE_1017_3:
    :cvar VALUE_1018_1:
    :cvar VALUE_1019_9:
    :cvar VALUE_1021_5:
    :cvar VALUE_1022_3:
    :cvar VALUE_1023_1:
    :cvar VALUE_1024_9:
    :cvar VALUE_1030_6:
    :cvar VALUE_1031_4:
    :cvar VALUE_1041_3:
    :cvar VALUE_1042_1:
    :cvar VALUE_1044_7:
    :cvar VALUE_1045_4:
    :cvar VALUE_1046_2:
    :cvar VALUE_1047_0:
    :cvar VALUE_1048_8:
    :cvar VALUE_1049_6:
    :cvar VALUE_1050_4:
    :cvar VALUE_1051_2:
    :cvar VALUE_1053_8:
    :cvar VALUE_1054_6:
    :cvar VALUE_1055_3:
    :cvar VALUE_1056_1:
    :cvar VALUE_1057_9:
    :cvar VALUE_1058_7:
    :cvar VALUE_1059_5:
    :cvar VALUE_1060_3:
    :cvar VALUE_1061_1:
    :cvar VALUE_1062_9:
    :cvar VALUE_1063_7:
    :cvar VALUE_1064_5:
    :cvar VALUE_1065_2:
    :cvar VALUE_1066_0:
    :cvar VALUE_1082_7:
    :cvar VALUE_1083_5:
    :cvar VALUE_1084_3:
    :cvar VALUE_1088_4:
    :cvar VALUE_1089_2:
    :cvar VALUE_1090_0:
    :cvar VALUE_1091_8:
    :cvar VALUE_1092_6:
    :cvar VALUE_1093_4:
    :cvar VALUE_1094_2:
    :cvar VALUE_1095_9:
    :cvar VALUE_1096_7:
    :cvar VALUE_1097_5:
    :cvar VALUE_1098_3:
    :cvar VALUE_1102_3:
    :cvar VALUE_1103_1:
    :cvar VALUE_1104_9:
    :cvar VALUE_1108_0:
    :cvar VALUE_1109_8:
    :cvar VALUE_1110_6:
    :cvar VALUE_1114_8:
    :cvar VALUE_1115_5:
    :cvar VALUE_1116_3:
    :cvar VALUE_1117_1:
    :cvar VALUE_1118_9:
    :cvar VALUE_1119_7:
    :cvar VALUE_1120_5:
    :cvar VALUE_1121_3:
    :cvar VALUE_1123_9:
    :cvar VALUE_1124_7:
    :cvar VALUE_1125_4:
    :cvar VALUE_1126_2:
    :cvar VALUE_1127_0:
    :cvar VALUE_1128_8:
    :cvar VALUE_1129_6:
    :cvar VALUE_1130_4:
    :cvar VALUE_1131_2:
    :cvar VALUE_1132_0:
    :cvar VALUE_1134_6:
    :cvar VALUE_1133_8:
    :cvar VALUE_1135_3:
    :cvar VALUE_1136_1:
    :cvar VALUE_1137_9:
    :cvar VALUE_1138_7:
    :cvar VALUE_1139_5:
    :cvar VALUE_1140_3:
    :cvar VALUE_1141_1:
    :cvar VALUE_1142_9:
    :cvar VALUE_1143_7:
    :cvar VALUE_1145_2:
    :cvar VALUE_1146_0:
    :cvar VALUE_1144_5:
    :cvar VALUE_1147_8:
    :cvar VALUE_1148_6:
    :cvar VALUE_1150_2:
    :cvar VALUE_1151_0:
    :cvar VALUE_1155_1:
    :cvar VALUE_1156_9:
    :cvar VALUE_1157_7:
    :cvar VALUE_1158_5:
    :cvar VALUE_1159_3:
    :cvar VALUE_1160_1:
    :cvar VALUE_1162_7:
    :cvar VALUE_1163_5:
    :cvar VALUE_1175_9:
    :cvar VALUE_1176_7:
    :cvar VALUE_1186_6:
    :cvar VALUE_1187_4:
    :cvar VALUE_1193_2:
    :cvar VALUE_1194_0:
    :cvar VALUE_1195_7:
    :cvar VALUE_1196_5:
    :cvar VALUE_1197_3:
    :cvar VALUE_1198_1:
    :cvar VALUE_1199_9:
    :cvar VALUE_1200_5:
    :cvar VALUE_1201_3:
    :cvar VALUE_1202_1:
    :cvar VALUE_1203_9:
    :cvar VALUE_1204_7:
    :cvar VALUE_1205_4:
    :cvar VALUE_1211_2:
    :cvar VALUE_1212_0:
    :cvar VALUE_1214_6:
    :cvar VALUE_1215_3:
    :cvar VALUE_1216_1:
    :cvar VALUE_1217_9:
    :cvar VALUE_1218_7:
    :cvar VALUE_1219_5:
    :cvar VALUE_1220_3:
    :cvar VALUE_1222_9:
    :cvar VALUE_1223_7:
    :cvar VALUE_1224_5:
    :cvar VALUE_1225_2:
    :cvar VALUE_1226_0:
    :cvar VALUE_1227_8:
    :cvar VALUE_1228_6:
    :cvar VALUE_1229_4:
    :cvar VALUE_1230_2:
    :cvar VALUE_1231_0:
    :cvar VALUE_1233_6:
    :cvar VALUE_1234_4:
    :cvar VALUE_1235_1:
    :cvar VALUE_1236_9:
    :cvar VALUE_1237_7:
    :cvar VALUE_1238_5:
    :cvar VALUE_1239_3:
    :cvar VALUE_1240_1:
    :cvar VALUE_1241_9:
    :cvar VALUE_1242_7:
    :cvar VALUE_1243_5:
    :cvar VALUE_1244_3:
    :cvar VALUE_1245_0:
    :cvar VALUE_1246_8:
    :cvar VALUE_1247_6:
    :cvar VALUE_1248_4:
    :cvar VALUE_1264_1:
    :cvar VALUE_1265_8:
    :cvar VALUE_1271_6:
    :cvar VALUE_1272_4:
    :cvar VALUE_1273_2:
    :cvar VALUE_1281_5:
    :cvar VALUE_1282_3:
    :cvar VALUE_1283_1:
    :cvar VALUE_1285_6:
    :cvar VALUE_1286_4:
    :cvar VALUE_1287_2:
    :cvar VALUE_1288_0:
    :cvar VALUE_1289_8:
    :cvar VALUE_1290_6:
    :cvar VALUE_1291_4:
    :cvar VALUE_1292_2:
    :cvar VALUE_1293_0:
    :cvar VALUE_1294_8:
    :cvar VALUE_1295_5:
    :cvar VALUE_1305_2:
    :cvar VALUE_1306_0:
    :cvar VALUE_1307_8:
    :cvar VALUE_1309_4:
    :cvar VALUE_1310_2:
    :cvar VALUE_1312_8:
    :cvar VALUE_1313_6:
    :cvar VALUE_1314_4:
    :cvar VALUE_1315_1:
    :cvar VALUE_1325_0:
    :cvar VALUE_1326_8:
    :cvar VALUE_1327_6:
    :cvar VALUE_1328_4:
    :cvar VALUE_1329_2:
    :cvar VALUE_1331_8:
    :cvar VALUE_1332_6:
    :cvar VALUE_1333_4:
    :cvar VALUE_1334_2:
    :cvar VALUE_1335_9:
    :cvar VALUE_1336_7:
    :cvar VALUE_1338_3:
    :cvar VALUE_1337_5:
    :cvar VALUE_1344_1:
    :cvar VALUE_1345_8:
    :cvar VALUE_1346_6:
    :cvar VALUE_1358_1:
    :cvar VALUE_1359_9:
    :cvar VALUE_1360_7:
    :cvar VALUE_1361_5:
    :cvar VALUE_1365_6:
    :cvar VALUE_1366_4:
    :cvar VALUE_1382_1:
    :cvar VALUE_1383_9:
    :cvar VALUE_1384_7:
    :cvar VALUE_1385_4:
    :cvar VALUE_1391_2:
    :cvar VALUE_1392_0:
    :cvar VALUE_1393_8:
    :cvar VALUE_1394_6:
    :cvar VALUE_1395_3:
    :cvar VALUE_1396_1:
    :cvar VALUE_1397_9:
    :cvar VALUE_1398_7:
    :cvar VALUE_1399_5:
    :cvar VALUE_1400_1:
    :cvar VALUE_1401_9:
    :cvar VALUE_1411_8:
    :cvar VALUE_1412_6:
    :cvar VALUE_1413_4:
    :cvar VALUE_1414_2:
    :cvar VALUE_1416_7:
    :cvar VALUE_1417_5:
    :cvar VALUE_1418_3:
    :cvar VALUE_1419_1:
    :cvar VALUE_1420_9:
    :cvar VALUE_1421_7:
    :cvar VALUE_1422_5:
    :cvar VALUE_1423_3:
    :cvar VALUE_1424_1:
    :cvar VALUE_1425_8:
    :cvar VALUE_1426_6:
    :cvar VALUE_1427_4:
    :cvar VALUE_1428_2:
    :cvar VALUE_1429_0:
    :cvar VALUE_1430_8:
    :cvar VALUE_1431_6:
    :cvar VALUE_1432_4:
    :cvar VALUE_1433_2:
    :cvar VALUE_1434_0:
    :cvar VALUE_1435_7:
    :cvar VALUE_1436_5:
    :cvar VALUE_1437_3:
    :cvar VALUE_1441_5:
    :cvar VALUE_1442_3:
    :cvar VALUE_1443_1:
    :cvar VALUE_1445_6:
    :cvar VALUE_1446_4:
    :cvar VALUE_1450_6:
    :cvar VALUE_1451_4:
    :cvar VALUE_1453_0:
    :cvar VALUE_1454_8:
    :cvar VALUE_1456_3:
    :cvar VALUE_1457_1:
    :cvar VALUE_1458_9:
    :cvar VALUE_1464_7:
    :cvar VALUE_1465_4:
    :cvar VALUE_1466_2:
    :cvar VALUE_1467_0:
    :cvar VALUE_1468_8:
    :cvar VALUE_1469_6:
    :cvar VALUE_1470_4:
    :cvar VALUE_1471_2:
    :cvar VALUE_1472_0:
    :cvar VALUE_1474_6:
    :cvar VALUE_1475_3:
    :cvar VALUE_1476_1:
    :cvar VALUE_1478_7:
    :cvar VALUE_1479_5:
    :cvar VALUE_1480_3:
    :cvar VALUE_1481_1:
    :cvar VALUE_1482_9:
    :cvar VALUE_1483_7:
    :cvar VALUE_1484_5:
    :cvar VALUE_1485_2:
    :cvar VALUE_1489_4:
    :cvar VALUE_1490_2:
    :cvar VALUE_1491_0:
    :cvar VALUE_1492_8:
    :cvar VALUE_1493_6:
    :cvar VALUE_1494_4:
    :cvar VALUE_1495_1:
    :cvar VALUE_1496_9:
    :cvar VALUE_1497_7:
    :cvar VALUE_1498_5:
    :cvar VALUE_1499_3:
    :cvar VALUE_1500_8:
    :cvar VALUE_1501_6:
    :cvar VALUE_1502_4:
    :cvar VALUE_1503_2:
    :cvar VALUE_1506_5:
    :cvar VALUE_1505_7:
    :cvar VALUE_1504_0:
    :cvar VALUE_1507_3:
    :cvar VALUE_1508_1:
    :cvar VALUE_1509_9:
    :cvar VALUE_1510_7:
    :cvar VALUE_1511_5:
    :cvar VALUE_1512_3:
    :cvar VALUE_1513_1:
    :cvar VALUE_1514_9:
    :cvar VALUE_1515_6:
    :cvar VALUE_1516_4:
    :cvar VALUE_1518_0:
    :cvar VALUE_1519_8:
    :cvar VALUE_1520_6:
    :cvar VALUE_1521_4:
    :cvar VALUE_1522_2:
    :cvar VALUE_1523_0:
    :cvar VALUE_1524_8:
    :cvar VALUE_1525_5:
    :cvar VALUE_1526_3:
    :cvar VALUE_1527_1:
    :cvar VALUE_1528_9:
    :cvar VALUE_1529_7:
    :cvar VALUE_1530_5:
    :cvar VALUE_1531_3:
    :cvar VALUE_1532_1:
    :cvar VALUE_1533_9:
    :cvar VALUE_1534_7:
    :cvar VALUE_1535_4:
    :cvar VALUE_1536_2:
    :cvar VALUE_1537_0:
    :cvar VALUE_1538_8:
    :cvar VALUE_1539_6:
    :cvar VALUE_1551_1:
    :cvar VALUE_1552_9:
    :cvar VALUE_1553_7:
    :cvar VALUE_1554_5:
    :cvar VALUE_1566_9:
    :cvar VALUE_1567_7:
    :cvar VALUE_1568_5:
    :cvar VALUE_1569_3:
    :cvar VALUE_1570_1:
    :cvar VALUE_1571_9:
    :cvar VALUE_1573_5:
    :cvar VALUE_1574_3:
    :cvar VALUE_1578_4:
    :cvar VALUE_1579_2:
    :cvar VALUE_1580_0:
    :cvar VALUE_1586_7:
    :cvar VALUE_1587_5:
    :cvar VALUE_1588_3:
    :cvar VALUE_1589_1:
    :cvar VALUE_1590_9:
    :cvar VALUE_1591_7:
    :cvar VALUE_1592_5:
    :cvar VALUE_1593_3:
    :cvar VALUE_1594_1:
    :cvar VALUE_1595_8:
    :cvar VALUE_1596_6:
    :cvar VALUE_1597_4:
    :cvar VALUE_1598_2:
    :cvar VALUE_1599_0:
    :cvar VALUE_1600_6:
    :cvar VALUE_1602_2:
    :cvar VALUE_1603_0:
    :cvar VALUE_1604_8:
    :cvar VALUE_1605_5:
    :cvar VALUE_1609_7:
    :cvar VALUE_1610_5:
    :cvar VALUE_1611_3:
    :cvar VALUE_1612_1:
    :cvar VALUE_1613_9:
    :cvar VALUE_1614_7:
    :cvar VALUE_1615_4:
    :cvar VALUE_1616_2:
    :cvar VALUE_1617_0:
    :cvar VALUE_1618_8:
    :cvar VALUE_1619_6:
    :cvar VALUE_1620_4:
    :cvar VALUE_1621_2:
    :cvar VALUE_1622_0:
    :cvar VALUE_1623_8:
    :cvar VALUE_1624_6:
    :cvar VALUE_1625_3:
    :cvar VALUE_1626_1:
    :cvar VALUE_1627_9:
    :cvar VALUE_1628_7:
    :cvar VALUE_1629_5:
    :cvar VALUE_1631_1:
    :cvar VALUE_1630_3:
    :cvar VALUE_1632_9:
    :cvar VALUE_1633_7:
    :cvar VALUE_1634_5:
    :cvar VALUE_1635_2:
    :cvar VALUE_1636_0:
    :cvar VALUE_1637_8:
    :cvar VALUE_1638_6:
    :cvar VALUE_1639_4:
    :cvar VALUE_1640_2:
    :cvar VALUE_1641_0:
    :cvar VALUE_1653_5:
    :cvar VALUE_1654_3:
    :cvar VALUE_1655_0:
    :cvar VALUE_1656_8:
    :cvar VALUE_1657_6:
    :cvar VALUE_1667_5:
    :cvar VALUE_1668_3:
    :cvar VALUE_1670_9:
    :cvar VALUE_1671_7:
    :cvar VALUE_1672_5:
    :cvar VALUE_1673_3:
    :cvar VALUE_1679_0:
    :cvar VALUE_1680_8:
    :cvar VALUE_1681_6:
    :cvar VALUE_1687_3:
    :cvar VALUE_1688_1:
    :cvar VALUE_1689_9:
    :cvar VALUE_1690_7:
    :cvar VALUE_1696_4:
    :cvar VALUE_1697_2:
    :cvar VALUE_1698_0:
    :cvar VALUE_1724_4:
    :cvar VALUE_1725_1:
    :cvar VALUE_1726_9:
    :cvar VALUE_1727_7:
    :cvar VALUE_1728_5:
    :cvar VALUE_1729_3:
    :cvar VALUE_1730_1:
    :cvar VALUE_1731_9:
    :cvar VALUE_1732_7:
    :cvar VALUE_1733_5:
    :cvar VALUE_1068_6:
    :cvar VALUE_1069_4:
    :cvar VALUE_1070_2:
    :cvar VALUE_1071_0:
    :cvar VALUE_1072_8:
    :cvar VALUE_1073_6:
    :cvar VALUE_1704_6:
    :cvar VALUE_1705_3:
    :cvar VALUE_1711_1:
    :cvar VALUE_1712_9:
    :cvar VALUE_1713_7:
    :cvar VALUE_1717_8:
    :cvar VALUE_1718_6:
    :cvar VALUE_1719_4:
    :cvar VALUE_1720_2:
    :cvar VALUE_1004_1:
    :cvar VALUE_1006_6:
    :cvar VALUE_1008_2:
    :cvar VALUE_1026_4:
    :cvar VALUE_1028_0:
    :cvar VALUE_1033_0:
    :cvar VALUE_1035_5:
    :cvar VALUE_1037_1:
    :cvar VALUE_1039_7:
    :cvar VALUE_1078_5:
    :cvar VALUE_1080_1:
    :cvar VALUE_1086_8:
    :cvar VALUE_1100_7:
    :cvar VALUE_1106_4:
    :cvar VALUE_1112_2:
    :cvar VALUE_1153_6:
    :cvar VALUE_1165_0:
    :cvar VALUE_1167_6:
    :cvar VALUE_1169_2:
    :cvar VALUE_1171_8:
    :cvar VALUE_1173_4:
    :cvar VALUE_1180_9:
    :cvar VALUE_1178_3:
    :cvar VALUE_1182_5:
    :cvar VALUE_1184_1:
    :cvar VALUE_1189_0:
    :cvar VALUE_1191_6:
    :cvar VALUE_1207_0:
    :cvar VALUE_1209_6:
    :cvar VALUE_1250_0:
    :cvar VALUE_1252_6:
    :cvar VALUE_1254_2:
    :cvar VALUE_1258_3:
    :cvar VALUE_1256_7:
    :cvar VALUE_1260_9:
    :cvar VALUE_1262_5:
    :cvar VALUE_1267_4:
    :cvar VALUE_1269_0:
    :cvar VALUE_1275_7:
    :cvar VALUE_1277_3:
    :cvar VALUE_1279_9:
    :cvar VALUE_1297_1:
    :cvar VALUE_1299_7:
    :cvar VALUE_1301_1:
    :cvar VALUE_1303_7:
    :cvar VALUE_1317_7:
    :cvar VALUE_1319_3:
    :cvar VALUE_1321_9:
    :cvar VALUE_1323_5:
    :cvar VALUE_1340_9:
    :cvar VALUE_1342_5:
    :cvar VALUE_1348_2:
    :cvar VALUE_1350_8:
    :cvar VALUE_1352_4:
    :cvar VALUE_1354_0:
    :cvar VALUE_1356_5:
    :cvar VALUE_1363_1:
    :cvar VALUE_1368_0:
    :cvar VALUE_1370_6:
    :cvar VALUE_1372_2:
    :cvar VALUE_1374_8:
    :cvar VALUE_1376_3:
    :cvar VALUE_1378_9:
    :cvar VALUE_1380_5:
    :cvar VALUE_1387_0:
    :cvar VALUE_1389_6:
    :cvar VALUE_1403_5:
    :cvar VALUE_1405_0:
    :cvar VALUE_1407_6:
    :cvar VALUE_1409_2:
    :cvar VALUE_1439_9:
    :cvar VALUE_1448_0:
    :cvar VALUE_1460_5:
    :cvar VALUE_1462_1:
    :cvar VALUE_1487_8:
    :cvar VALUE_1541_2:
    :cvar VALUE_1543_8:
    :cvar VALUE_1545_3:
    :cvar VALUE_1547_9:
    :cvar VALUE_1549_5:
    :cvar VALUE_1556_0:
    :cvar VALUE_1558_6:
    :cvar VALUE_1560_2:
    :cvar VALUE_1562_8:
    :cvar VALUE_1564_4:
    :cvar VALUE_1576_8:
    :cvar VALUE_1582_6:
    :cvar VALUE_1584_2:
    :cvar VALUE_1607_1:
    :cvar VALUE_1643_6:
    :cvar VALUE_1074_4:
    :cvar VALUE_1645_1:
    :cvar VALUE_1647_7:
    :cvar VALUE_1649_3:
    :cvar VALUE_1651_9:
    :cvar VALUE_1659_2:
    :cvar VALUE_1661_8:
    :cvar VALUE_1663_4:
    :cvar VALUE_1665_9:
    :cvar VALUE_1675_8:
    :cvar VALUE_1677_4:
    :cvar VALUE_1683_2:
    :cvar VALUE_1685_7:
    :cvar VALUE_1692_3:
    :cvar VALUE_1694_9:
    :cvar VALUE_1700_4:
    :cvar VALUE_1702_0:
    :cvar VALUE_1707_9:
    :cvar VALUE_1709_5:
    :cvar VALUE_1715_2:
    :cvar VALUE_1722_8:
    :cvar VALUE_1002_5:
    :cvar VALUE_2129_5:
    :cvar VALUE_2108_9:
    :cvar VALUE_2109_7:
    :cvar VALUE_2110_5:
    :cvar VALUE_2111_3:
    :cvar VALUE_2112_1:
    :cvar VALUE_2113_9:
    :cvar VALUE_2114_7:
    :cvar VALUE_2115_4:
    :cvar VALUE_2116_2:
    :cvar VALUE_2118_8:
    :cvar VALUE_2126_1:
    :cvar VALUE_2119_6:
    :cvar VALUE_2120_4:
    :cvar VALUE_2121_2:
    :cvar VALUE_2122_0:
    :cvar VALUE_2127_9:
    :cvar VALUE_2123_8:
    :cvar VALUE_2124_6:
    :cvar VALUE_2125_3:
    :cvar VALUE_2106_3:
    :cvar VALUE_2131_1:
    """
    VALUE_2028_9 = "2028-9"
    VALUE_2029_7 = "2029-7"
    VALUE_2030_5 = "2030-5"
    VALUE_2031_3 = "2031-3"
    VALUE_2032_1 = "2032-1"
    VALUE_2033_9 = "2033-9"
    VALUE_2034_7 = "2034-7"
    VALUE_2036_2 = "2036-2"
    VALUE_2037_0 = "2037-0"
    VALUE_2038_8 = "2038-8"
    VALUE_2048_7 = "2048-7"
    VALUE_2039_6 = "2039-6"
    VALUE_2040_4 = "2040-4"
    VALUE_2041_2 = "2041-2"
    VALUE_2052_9 = "2052-9"
    VALUE_2042_0 = "2042-0"
    VALUE_2049_5 = "2049-5"
    VALUE_2050_3 = "2050-3"
    VALUE_2043_8 = "2043-8"
    VALUE_2044_6 = "2044-6"
    VALUE_2051_1 = "2051-1"
    VALUE_2045_3 = "2045-3"
    VALUE_2035_4 = "2035-4"
    VALUE_2046_1 = "2046-1"
    VALUE_2047_9 = "2047-9"
    VALUE_2060_2 = "2060-2"
    VALUE_2061_0 = "2061-0"
    VALUE_2062_8 = "2062-8"
    VALUE_2063_6 = "2063-6"
    VALUE_2064_4 = "2064-4"
    VALUE_2065_1 = "2065-1"
    VALUE_2066_9 = "2066-9"
    VALUE_2054_5 = "2054-5"
    VALUE_2058_6 = "2058-6"
    VALUE_2067_7 = "2067-7"
    VALUE_2068_5 = "2068-5"
    VALUE_2056_0 = "2056-0"
    VALUE_2070_1 = "2070-1"
    VALUE_2069_3 = "2069-3"
    VALUE_2071_9 = "2071-9"
    VALUE_2072_7 = "2072-7"
    VALUE_2073_5 = "2073-5"
    VALUE_2074_3 = "2074-3"
    VALUE_2075_0 = "2075-0"
    VALUE_2100_6 = "2100-6"
    VALUE_2101_4 = "2101-4"
    VALUE_2104_8 = "2104-8"
    VALUE_2102_2 = "2102-2"
    VALUE_2103_0 = "2103-0"
    VALUE_2085_9 = "2085-9"
    VALUE_2092_5 = "2092-5"
    VALUE_2088_3 = "2088-3"
    VALUE_2097_4 = "2097-4"
    VALUE_2087_5 = "2087-5"
    VALUE_2086_7 = "2086-7"
    VALUE_2096_6 = "2096-6"
    VALUE_2093_3 = "2093-3"
    VALUE_2089_1 = "2089-1"
    VALUE_2090_9 = "2090-9"
    VALUE_2091_7 = "2091-7"
    VALUE_2094_1 = "2094-1"
    VALUE_2095_8 = "2095-8"
    VALUE_2098_2 = "2098-2"
    VALUE_2078_4 = "2078-4"
    VALUE_2079_2 = "2079-2"
    VALUE_2080_0 = "2080-0"
    VALUE_2081_8 = "2081-8"
    VALUE_2083_4 = "2083-4"
    VALUE_2082_6 = "2082-6"
    VALUE_2076_8 = "2076-8"
    VALUE_2500_7 = "2500-7"
    VALUE_1739_2 = "1739-2"
    VALUE_1740_0 = "1740-0"
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"
    VALUE_1811_9 = "1811-9"
    VALUE_1737_6 = "1737-6"
    VALUE_1968_7 = "1968-7"
    VALUE_1969_5 = "1969-5"
    VALUE_1970_3 = "1970-3"
    VALUE_1972_9 = "1972-9"
    VALUE_1973_7 = "1973-7"
    VALUE_1974_5 = "1974-5"
    VALUE_1975_2 = "1975-2"
    VALUE_1976_0 = "1976-0"
    VALUE_1977_8 = "1977-8"
    VALUE_1978_6 = "1978-6"
    VALUE_1979_4 = "1979-4"
    VALUE_1980_2 = "1980-2"
    VALUE_1981_0 = "1981-0"
    VALUE_1982_8 = "1982-8"
    VALUE_1984_4 = "1984-4"
    VALUE_1985_1 = "1985-1"
    VALUE_1986_9 = "1986-9"
    VALUE_1987_7 = "1987-7"
    VALUE_1988_5 = "1988-5"
    VALUE_1992_7 = "1992-7"
    VALUE_1994_3 = "1994-3"
    VALUE_1993_5 = "1993-5"
    VALUE_1995_0 = "1995-0"
    VALUE_1996_8 = "1996-8"
    VALUE_1997_6 = "1997-6"
    VALUE_1998_4 = "1998-4"
    VALUE_1999_2 = "1999-2"
    VALUE_2000_8 = "2000-8"
    VALUE_2006_5 = "2006-5"
    VALUE_2007_3 = "2007-3"
    VALUE_2008_1 = "2008-1"
    VALUE_2009_9 = "2009-9"
    VALUE_2010_7 = "2010-7"
    VALUE_2011_5 = "2011-5"
    VALUE_2012_3 = "2012-3"
    VALUE_2013_1 = "2013-1"
    VALUE_2015_6 = "2015-6"
    VALUE_2014_9 = "2014-9"
    VALUE_2016_4 = "2016-4"
    VALUE_2017_2 = "2017-2"
    VALUE_2018_0 = "2018-0"
    VALUE_2019_8 = "2019-8"
    VALUE_2020_6 = "2020-6"
    VALUE_2023_0 = "2023-0"
    VALUE_2024_8 = "2024-8"
    VALUE_2021_4 = "2021-4"
    VALUE_2022_2 = "2022-2"
    VALUE_2025_5 = "2025-5"
    VALUE_2026_3 = "2026-3"
    VALUE_1966_1 = "1966-1"
    VALUE_1990_1 = "1990-1"
    VALUE_2002_4 = "2002-4"
    VALUE_2004_0 = "2004-0"
    VALUE_1844_0 = "1844-0"
    VALUE_1845_7 = "1845-7"
    VALUE_1846_5 = "1846-5"
    VALUE_1847_3 = "1847-3"
    VALUE_1849_9 = "1849-9"
    VALUE_1848_1 = "1848-1"
    VALUE_1850_7 = "1850-7"
    VALUE_1851_5 = "1851-5"
    VALUE_1852_3 = "1852-3"
    VALUE_1853_1 = "1853-1"
    VALUE_1854_9 = "1854-9"
    VALUE_1855_6 = "1855-6"
    VALUE_1856_4 = "1856-4"
    VALUE_1857_2 = "1857-2"
    VALUE_1858_0 = "1858-0"
    VALUE_1859_8 = "1859-8"
    VALUE_1860_6 = "1860-6"
    VALUE_1861_4 = "1861-4"
    VALUE_1862_2 = "1862-2"
    VALUE_1863_0 = "1863-0"
    VALUE_1864_8 = "1864-8"
    VALUE_1865_5 = "1865-5"
    VALUE_1866_3 = "1866-3"
    VALUE_1867_1 = "1867-1"
    VALUE_1868_9 = "1868-9"
    VALUE_1869_7 = "1869-7"
    VALUE_1889_5 = "1889-5"
    VALUE_1870_5 = "1870-5"
    VALUE_1871_3 = "1871-3"
    VALUE_1872_1 = "1872-1"
    VALUE_1873_9 = "1873-9"
    VALUE_1874_7 = "1874-7"
    VALUE_1875_4 = "1875-4"
    VALUE_1876_2 = "1876-2"
    VALUE_1877_0 = "1877-0"
    VALUE_1878_8 = "1878-8"
    VALUE_1879_6 = "1879-6"
    VALUE_1880_4 = "1880-4"
    VALUE_1881_2 = "1881-2"
    VALUE_1882_0 = "1882-0"
    VALUE_1883_8 = "1883-8"
    VALUE_1884_6 = "1884-6"
    VALUE_1885_3 = "1885-3"
    VALUE_1886_1 = "1886-1"
    VALUE_1887_9 = "1887-9"
    VALUE_1888_7 = "1888-7"
    VALUE_1891_1 = "1891-1"
    VALUE_1892_9 = "1892-9"
    VALUE_1893_7 = "1893-7"
    VALUE_1894_5 = "1894-5"
    VALUE_1896_0 = "1896-0"
    VALUE_1897_8 = "1897-8"
    VALUE_1898_6 = "1898-6"
    VALUE_1899_4 = "1899-4"
    VALUE_1900_0 = "1900-0"
    VALUE_1901_8 = "1901-8"
    VALUE_1902_6 = "1902-6"
    VALUE_1903_4 = "1903-4"
    VALUE_1904_2 = "1904-2"
    VALUE_1905_9 = "1905-9"
    VALUE_1906_7 = "1906-7"
    VALUE_1907_5 = "1907-5"
    VALUE_1908_3 = "1908-3"
    VALUE_1909_1 = "1909-1"
    VALUE_1910_9 = "1910-9"
    VALUE_1911_7 = "1911-7"
    VALUE_1912_5 = "1912-5"
    VALUE_1913_3 = "1913-3"
    VALUE_1914_1 = "1914-1"
    VALUE_1915_8 = "1915-8"
    VALUE_1916_6 = "1916-6"
    VALUE_1917_4 = "1917-4"
    VALUE_1962_0 = "1962-0"
    VALUE_1918_2 = "1918-2"
    VALUE_1919_0 = "1919-0"
    VALUE_1920_8 = "1920-8"
    VALUE_1921_6 = "1921-6"
    VALUE_1922_4 = "1922-4"
    VALUE_1923_2 = "1923-2"
    VALUE_1924_0 = "1924-0"
    VALUE_1925_7 = "1925-7"
    VALUE_1926_5 = "1926-5"
    VALUE_1927_3 = "1927-3"
    VALUE_1928_1 = "1928-1"
    VALUE_1929_9 = "1929-9"
    VALUE_1930_7 = "1930-7"
    VALUE_1931_5 = "1931-5"
    VALUE_1932_3 = "1932-3"
    VALUE_1933_1 = "1933-1"
    VALUE_1934_9 = "1934-9"
    VALUE_1935_6 = "1935-6"
    VALUE_1937_2 = "1937-2"
    VALUE_1938_0 = "1938-0"
    VALUE_1936_4 = "1936-4"
    VALUE_1940_6 = "1940-6"
    VALUE_1939_8 = "1939-8"
    VALUE_1941_4 = "1941-4"
    VALUE_1942_2 = "1942-2"
    VALUE_1943_0 = "1943-0"
    VALUE_1944_8 = "1944-8"
    VALUE_1945_5 = "1945-5"
    VALUE_1946_3 = "1946-3"
    VALUE_1947_1 = "1947-1"
    VALUE_1948_9 = "1948-9"
    VALUE_1949_7 = "1949-7"
    VALUE_1950_5 = "1950-5"
    VALUE_1952_1 = "1952-1"
    VALUE_1953_9 = "1953-9"
    VALUE_1954_7 = "1954-7"
    VALUE_1963_8 = "1963-8"
    VALUE_1951_3 = "1951-3"
    VALUE_1955_4 = "1955-4"
    VALUE_1956_2 = "1956-2"
    VALUE_1957_0 = "1957-0"
    VALUE_1958_8 = "1958-8"
    VALUE_1959_6 = "1959-6"
    VALUE_1960_4 = "1960-4"
    VALUE_1961_2 = "1961-2"
    VALUE_1964_6 = "1964-6"
    VALUE_1840_8 = "1840-8"
    VALUE_1842_4 = "1842-4"
    VALUE_1735_0 = "1735-0"
    VALUE_1076_9 = "1076-9"
    VALUE_1744_2 = "1744-2"
    VALUE_1741_8 = "1741-8"
    VALUE_1742_6 = "1742-6"
    VALUE_1743_4 = "1743-4"
    VALUE_1745_9 = "1745-9"
    VALUE_1746_7 = "1746-7"
    VALUE_1747_5 = "1747-5"
    VALUE_1748_3 = "1748-3"
    VALUE_1749_1 = "1749-1"
    VALUE_1750_9 = "1750-9"
    VALUE_1751_7 = "1751-7"
    VALUE_1752_5 = "1752-5"
    VALUE_1753_3 = "1753-3"
    VALUE_1754_1 = "1754-1"
    VALUE_1755_8 = "1755-8"
    VALUE_1756_6 = "1756-6"
    VALUE_1757_4 = "1757-4"
    VALUE_1758_2 = "1758-2"
    VALUE_1759_0 = "1759-0"
    VALUE_1760_8 = "1760-8"
    VALUE_1761_6 = "1761-6"
    VALUE_1762_4 = "1762-4"
    VALUE_1763_2 = "1763-2"
    VALUE_1764_0 = "1764-0"
    VALUE_1765_7 = "1765-7"
    VALUE_1766_5 = "1766-5"
    VALUE_1767_3 = "1767-3"
    VALUE_1768_1 = "1768-1"
    VALUE_1769_9 = "1769-9"
    VALUE_1770_7 = "1770-7"
    VALUE_1771_5 = "1771-5"
    VALUE_1772_3 = "1772-3"
    VALUE_1773_1 = "1773-1"
    VALUE_1774_9 = "1774-9"
    VALUE_1775_6 = "1775-6"
    VALUE_1776_4 = "1776-4"
    VALUE_1777_2 = "1777-2"
    VALUE_1778_0 = "1778-0"
    VALUE_1780_6 = "1780-6"
    VALUE_1779_8 = "1779-8"
    VALUE_1781_4 = "1781-4"
    VALUE_1782_2 = "1782-2"
    VALUE_1783_0 = "1783-0"
    VALUE_1784_8 = "1784-8"
    VALUE_1785_5 = "1785-5"
    VALUE_1786_3 = "1786-3"
    VALUE_1787_1 = "1787-1"
    VALUE_1788_9 = "1788-9"
    VALUE_1789_7 = "1789-7"
    VALUE_1790_5 = "1790-5"
    VALUE_1791_3 = "1791-3"
    VALUE_1792_1 = "1792-1"
    VALUE_1793_9 = "1793-9"
    VALUE_1795_4 = "1795-4"
    VALUE_1794_7 = "1794-7"
    VALUE_1796_2 = "1796-2"
    VALUE_1797_0 = "1797-0"
    VALUE_1798_8 = "1798-8"
    VALUE_1799_6 = "1799-6"
    VALUE_1800_2 = "1800-2"
    VALUE_1801_0 = "1801-0"
    VALUE_1802_8 = "1802-8"
    VALUE_1803_6 = "1803-6"
    VALUE_1804_4 = "1804-4"
    VALUE_1805_1 = "1805-1"
    VALUE_1806_9 = "1806-9"
    VALUE_1807_7 = "1807-7"
    VALUE_1808_5 = "1808-5"
    VALUE_1809_3 = "1809-3"
    VALUE_1010_8 = "1010-8"
    VALUE_1011_6 = "1011-6"
    VALUE_1012_4 = "1012-4"
    VALUE_1013_2 = "1013-2"
    VALUE_1014_0 = "1014-0"
    VALUE_1015_7 = "1015-7"
    VALUE_1016_5 = "1016-5"
    VALUE_1017_3 = "1017-3"
    VALUE_1018_1 = "1018-1"
    VALUE_1019_9 = "1019-9"
    VALUE_1021_5 = "1021-5"
    VALUE_1022_3 = "1022-3"
    VALUE_1023_1 = "1023-1"
    VALUE_1024_9 = "1024-9"
    VALUE_1030_6 = "1030-6"
    VALUE_1031_4 = "1031-4"
    VALUE_1041_3 = "1041-3"
    VALUE_1042_1 = "1042-1"
    VALUE_1044_7 = "1044-7"
    VALUE_1045_4 = "1045-4"
    VALUE_1046_2 = "1046-2"
    VALUE_1047_0 = "1047-0"
    VALUE_1048_8 = "1048-8"
    VALUE_1049_6 = "1049-6"
    VALUE_1050_4 = "1050-4"
    VALUE_1051_2 = "1051-2"
    VALUE_1053_8 = "1053-8"
    VALUE_1054_6 = "1054-6"
    VALUE_1055_3 = "1055-3"
    VALUE_1056_1 = "1056-1"
    VALUE_1057_9 = "1057-9"
    VALUE_1058_7 = "1058-7"
    VALUE_1059_5 = "1059-5"
    VALUE_1060_3 = "1060-3"
    VALUE_1061_1 = "1061-1"
    VALUE_1062_9 = "1062-9"
    VALUE_1063_7 = "1063-7"
    VALUE_1064_5 = "1064-5"
    VALUE_1065_2 = "1065-2"
    VALUE_1066_0 = "1066-0"
    VALUE_1082_7 = "1082-7"
    VALUE_1083_5 = "1083-5"
    VALUE_1084_3 = "1084-3"
    VALUE_1088_4 = "1088-4"
    VALUE_1089_2 = "1089-2"
    VALUE_1090_0 = "1090-0"
    VALUE_1091_8 = "1091-8"
    VALUE_1092_6 = "1092-6"
    VALUE_1093_4 = "1093-4"
    VALUE_1094_2 = "1094-2"
    VALUE_1095_9 = "1095-9"
    VALUE_1096_7 = "1096-7"
    VALUE_1097_5 = "1097-5"
    VALUE_1098_3 = "1098-3"
    VALUE_1102_3 = "1102-3"
    VALUE_1103_1 = "1103-1"
    VALUE_1104_9 = "1104-9"
    VALUE_1108_0 = "1108-0"
    VALUE_1109_8 = "1109-8"
    VALUE_1110_6 = "1110-6"
    VALUE_1114_8 = "1114-8"
    VALUE_1115_5 = "1115-5"
    VALUE_1116_3 = "1116-3"
    VALUE_1117_1 = "1117-1"
    VALUE_1118_9 = "1118-9"
    VALUE_1119_7 = "1119-7"
    VALUE_1120_5 = "1120-5"
    VALUE_1121_3 = "1121-3"
    VALUE_1123_9 = "1123-9"
    VALUE_1124_7 = "1124-7"
    VALUE_1125_4 = "1125-4"
    VALUE_1126_2 = "1126-2"
    VALUE_1127_0 = "1127-0"
    VALUE_1128_8 = "1128-8"
    VALUE_1129_6 = "1129-6"
    VALUE_1130_4 = "1130-4"
    VALUE_1131_2 = "1131-2"
    VALUE_1132_0 = "1132-0"
    VALUE_1134_6 = "1134-6"
    VALUE_1133_8 = "1133-8"
    VALUE_1135_3 = "1135-3"
    VALUE_1136_1 = "1136-1"
    VALUE_1137_9 = "1137-9"
    VALUE_1138_7 = "1138-7"
    VALUE_1139_5 = "1139-5"
    VALUE_1140_3 = "1140-3"
    VALUE_1141_1 = "1141-1"
    VALUE_1142_9 = "1142-9"
    VALUE_1143_7 = "1143-7"
    VALUE_1145_2 = "1145-2"
    VALUE_1146_0 = "1146-0"
    VALUE_1144_5 = "1144-5"
    VALUE_1147_8 = "1147-8"
    VALUE_1148_6 = "1148-6"
    VALUE_1150_2 = "1150-2"
    VALUE_1151_0 = "1151-0"
    VALUE_1155_1 = "1155-1"
    VALUE_1156_9 = "1156-9"
    VALUE_1157_7 = "1157-7"
    VALUE_1158_5 = "1158-5"
    VALUE_1159_3 = "1159-3"
    VALUE_1160_1 = "1160-1"
    VALUE_1162_7 = "1162-7"
    VALUE_1163_5 = "1163-5"
    VALUE_1175_9 = "1175-9"
    VALUE_1176_7 = "1176-7"
    VALUE_1186_6 = "1186-6"
    VALUE_1187_4 = "1187-4"
    VALUE_1193_2 = "1193-2"
    VALUE_1194_0 = "1194-0"
    VALUE_1195_7 = "1195-7"
    VALUE_1196_5 = "1196-5"
    VALUE_1197_3 = "1197-3"
    VALUE_1198_1 = "1198-1"
    VALUE_1199_9 = "1199-9"
    VALUE_1200_5 = "1200-5"
    VALUE_1201_3 = "1201-3"
    VALUE_1202_1 = "1202-1"
    VALUE_1203_9 = "1203-9"
    VALUE_1204_7 = "1204-7"
    VALUE_1205_4 = "1205-4"
    VALUE_1211_2 = "1211-2"
    VALUE_1212_0 = "1212-0"
    VALUE_1214_6 = "1214-6"
    VALUE_1215_3 = "1215-3"
    VALUE_1216_1 = "1216-1"
    VALUE_1217_9 = "1217-9"
    VALUE_1218_7 = "1218-7"
    VALUE_1219_5 = "1219-5"
    VALUE_1220_3 = "1220-3"
    VALUE_1222_9 = "1222-9"
    VALUE_1223_7 = "1223-7"
    VALUE_1224_5 = "1224-5"
    VALUE_1225_2 = "1225-2"
    VALUE_1226_0 = "1226-0"
    VALUE_1227_8 = "1227-8"
    VALUE_1228_6 = "1228-6"
    VALUE_1229_4 = "1229-4"
    VALUE_1230_2 = "1230-2"
    VALUE_1231_0 = "1231-0"
    VALUE_1233_6 = "1233-6"
    VALUE_1234_4 = "1234-4"
    VALUE_1235_1 = "1235-1"
    VALUE_1236_9 = "1236-9"
    VALUE_1237_7 = "1237-7"
    VALUE_1238_5 = "1238-5"
    VALUE_1239_3 = "1239-3"
    VALUE_1240_1 = "1240-1"
    VALUE_1241_9 = "1241-9"
    VALUE_1242_7 = "1242-7"
    VALUE_1243_5 = "1243-5"
    VALUE_1244_3 = "1244-3"
    VALUE_1245_0 = "1245-0"
    VALUE_1246_8 = "1246-8"
    VALUE_1247_6 = "1247-6"
    VALUE_1248_4 = "1248-4"
    VALUE_1264_1 = "1264-1"
    VALUE_1265_8 = "1265-8"
    VALUE_1271_6 = "1271-6"
    VALUE_1272_4 = "1272-4"
    VALUE_1273_2 = "1273-2"
    VALUE_1281_5 = "1281-5"
    VALUE_1282_3 = "1282-3"
    VALUE_1283_1 = "1283-1"
    VALUE_1285_6 = "1285-6"
    VALUE_1286_4 = "1286-4"
    VALUE_1287_2 = "1287-2"
    VALUE_1288_0 = "1288-0"
    VALUE_1289_8 = "1289-8"
    VALUE_1290_6 = "1290-6"
    VALUE_1291_4 = "1291-4"
    VALUE_1292_2 = "1292-2"
    VALUE_1293_0 = "1293-0"
    VALUE_1294_8 = "1294-8"
    VALUE_1295_5 = "1295-5"
    VALUE_1305_2 = "1305-2"
    VALUE_1306_0 = "1306-0"
    VALUE_1307_8 = "1307-8"
    VALUE_1309_4 = "1309-4"
    VALUE_1310_2 = "1310-2"
    VALUE_1312_8 = "1312-8"
    VALUE_1313_6 = "1313-6"
    VALUE_1314_4 = "1314-4"
    VALUE_1315_1 = "1315-1"
    VALUE_1325_0 = "1325-0"
    VALUE_1326_8 = "1326-8"
    VALUE_1327_6 = "1327-6"
    VALUE_1328_4 = "1328-4"
    VALUE_1329_2 = "1329-2"
    VALUE_1331_8 = "1331-8"
    VALUE_1332_6 = "1332-6"
    VALUE_1333_4 = "1333-4"
    VALUE_1334_2 = "1334-2"
    VALUE_1335_9 = "1335-9"
    VALUE_1336_7 = "1336-7"
    VALUE_1338_3 = "1338-3"
    VALUE_1337_5 = "1337-5"
    VALUE_1344_1 = "1344-1"
    VALUE_1345_8 = "1345-8"
    VALUE_1346_6 = "1346-6"
    VALUE_1358_1 = "1358-1"
    VALUE_1359_9 = "1359-9"
    VALUE_1360_7 = "1360-7"
    VALUE_1361_5 = "1361-5"
    VALUE_1365_6 = "1365-6"
    VALUE_1366_4 = "1366-4"
    VALUE_1382_1 = "1382-1"
    VALUE_1383_9 = "1383-9"
    VALUE_1384_7 = "1384-7"
    VALUE_1385_4 = "1385-4"
    VALUE_1391_2 = "1391-2"
    VALUE_1392_0 = "1392-0"
    VALUE_1393_8 = "1393-8"
    VALUE_1394_6 = "1394-6"
    VALUE_1395_3 = "1395-3"
    VALUE_1396_1 = "1396-1"
    VALUE_1397_9 = "1397-9"
    VALUE_1398_7 = "1398-7"
    VALUE_1399_5 = "1399-5"
    VALUE_1400_1 = "1400-1"
    VALUE_1401_9 = "1401-9"
    VALUE_1411_8 = "1411-8"
    VALUE_1412_6 = "1412-6"
    VALUE_1413_4 = "1413-4"
    VALUE_1414_2 = "1414-2"
    VALUE_1416_7 = "1416-7"
    VALUE_1417_5 = "1417-5"
    VALUE_1418_3 = "1418-3"
    VALUE_1419_1 = "1419-1"
    VALUE_1420_9 = "1420-9"
    VALUE_1421_7 = "1421-7"
    VALUE_1422_5 = "1422-5"
    VALUE_1423_3 = "1423-3"
    VALUE_1424_1 = "1424-1"
    VALUE_1425_8 = "1425-8"
    VALUE_1426_6 = "1426-6"
    VALUE_1427_4 = "1427-4"
    VALUE_1428_2 = "1428-2"
    VALUE_1429_0 = "1429-0"
    VALUE_1430_8 = "1430-8"
    VALUE_1431_6 = "1431-6"
    VALUE_1432_4 = "1432-4"
    VALUE_1433_2 = "1433-2"
    VALUE_1434_0 = "1434-0"
    VALUE_1435_7 = "1435-7"
    VALUE_1436_5 = "1436-5"
    VALUE_1437_3 = "1437-3"
    VALUE_1441_5 = "1441-5"
    VALUE_1442_3 = "1442-3"
    VALUE_1443_1 = "1443-1"
    VALUE_1445_6 = "1445-6"
    VALUE_1446_4 = "1446-4"
    VALUE_1450_6 = "1450-6"
    VALUE_1451_4 = "1451-4"
    VALUE_1453_0 = "1453-0"
    VALUE_1454_8 = "1454-8"
    VALUE_1456_3 = "1456-3"
    VALUE_1457_1 = "1457-1"
    VALUE_1458_9 = "1458-9"
    VALUE_1464_7 = "1464-7"
    VALUE_1465_4 = "1465-4"
    VALUE_1466_2 = "1466-2"
    VALUE_1467_0 = "1467-0"
    VALUE_1468_8 = "1468-8"
    VALUE_1469_6 = "1469-6"
    VALUE_1470_4 = "1470-4"
    VALUE_1471_2 = "1471-2"
    VALUE_1472_0 = "1472-0"
    VALUE_1474_6 = "1474-6"
    VALUE_1475_3 = "1475-3"
    VALUE_1476_1 = "1476-1"
    VALUE_1478_7 = "1478-7"
    VALUE_1479_5 = "1479-5"
    VALUE_1480_3 = "1480-3"
    VALUE_1481_1 = "1481-1"
    VALUE_1482_9 = "1482-9"
    VALUE_1483_7 = "1483-7"
    VALUE_1484_5 = "1484-5"
    VALUE_1485_2 = "1485-2"
    VALUE_1489_4 = "1489-4"
    VALUE_1490_2 = "1490-2"
    VALUE_1491_0 = "1491-0"
    VALUE_1492_8 = "1492-8"
    VALUE_1493_6 = "1493-6"
    VALUE_1494_4 = "1494-4"
    VALUE_1495_1 = "1495-1"
    VALUE_1496_9 = "1496-9"
    VALUE_1497_7 = "1497-7"
    VALUE_1498_5 = "1498-5"
    VALUE_1499_3 = "1499-3"
    VALUE_1500_8 = "1500-8"
    VALUE_1501_6 = "1501-6"
    VALUE_1502_4 = "1502-4"
    VALUE_1503_2 = "1503-2"
    VALUE_1506_5 = "1506-5"
    VALUE_1505_7 = "1505-7"
    VALUE_1504_0 = "1504-0"
    VALUE_1507_3 = "1507-3"
    VALUE_1508_1 = "1508-1"
    VALUE_1509_9 = "1509-9"
    VALUE_1510_7 = "1510-7"
    VALUE_1511_5 = "1511-5"
    VALUE_1512_3 = "1512-3"
    VALUE_1513_1 = "1513-1"
    VALUE_1514_9 = "1514-9"
    VALUE_1515_6 = "1515-6"
    VALUE_1516_4 = "1516-4"
    VALUE_1518_0 = "1518-0"
    VALUE_1519_8 = "1519-8"
    VALUE_1520_6 = "1520-6"
    VALUE_1521_4 = "1521-4"
    VALUE_1522_2 = "1522-2"
    VALUE_1523_0 = "1523-0"
    VALUE_1524_8 = "1524-8"
    VALUE_1525_5 = "1525-5"
    VALUE_1526_3 = "1526-3"
    VALUE_1527_1 = "1527-1"
    VALUE_1528_9 = "1528-9"
    VALUE_1529_7 = "1529-7"
    VALUE_1530_5 = "1530-5"
    VALUE_1531_3 = "1531-3"
    VALUE_1532_1 = "1532-1"
    VALUE_1533_9 = "1533-9"
    VALUE_1534_7 = "1534-7"
    VALUE_1535_4 = "1535-4"
    VALUE_1536_2 = "1536-2"
    VALUE_1537_0 = "1537-0"
    VALUE_1538_8 = "1538-8"
    VALUE_1539_6 = "1539-6"
    VALUE_1551_1 = "1551-1"
    VALUE_1552_9 = "1552-9"
    VALUE_1553_7 = "1553-7"
    VALUE_1554_5 = "1554-5"
    VALUE_1566_9 = "1566-9"
    VALUE_1567_7 = "1567-7"
    VALUE_1568_5 = "1568-5"
    VALUE_1569_3 = "1569-3"
    VALUE_1570_1 = "1570-1"
    VALUE_1571_9 = "1571-9"
    VALUE_1573_5 = "1573-5"
    VALUE_1574_3 = "1574-3"
    VALUE_1578_4 = "1578-4"
    VALUE_1579_2 = "1579-2"
    VALUE_1580_0 = "1580-0"
    VALUE_1586_7 = "1586-7"
    VALUE_1587_5 = "1587-5"
    VALUE_1588_3 = "1588-3"
    VALUE_1589_1 = "1589-1"
    VALUE_1590_9 = "1590-9"
    VALUE_1591_7 = "1591-7"
    VALUE_1592_5 = "1592-5"
    VALUE_1593_3 = "1593-3"
    VALUE_1594_1 = "1594-1"
    VALUE_1595_8 = "1595-8"
    VALUE_1596_6 = "1596-6"
    VALUE_1597_4 = "1597-4"
    VALUE_1598_2 = "1598-2"
    VALUE_1599_0 = "1599-0"
    VALUE_1600_6 = "1600-6"
    VALUE_1602_2 = "1602-2"
    VALUE_1603_0 = "1603-0"
    VALUE_1604_8 = "1604-8"
    VALUE_1605_5 = "1605-5"
    VALUE_1609_7 = "1609-7"
    VALUE_1610_5 = "1610-5"
    VALUE_1611_3 = "1611-3"
    VALUE_1612_1 = "1612-1"
    VALUE_1613_9 = "1613-9"
    VALUE_1614_7 = "1614-7"
    VALUE_1615_4 = "1615-4"
    VALUE_1616_2 = "1616-2"
    VALUE_1617_0 = "1617-0"
    VALUE_1618_8 = "1618-8"
    VALUE_1619_6 = "1619-6"
    VALUE_1620_4 = "1620-4"
    VALUE_1621_2 = "1621-2"
    VALUE_1622_0 = "1622-0"
    VALUE_1623_8 = "1623-8"
    VALUE_1624_6 = "1624-6"
    VALUE_1625_3 = "1625-3"
    VALUE_1626_1 = "1626-1"
    VALUE_1627_9 = "1627-9"
    VALUE_1628_7 = "1628-7"
    VALUE_1629_5 = "1629-5"
    VALUE_1631_1 = "1631-1"
    VALUE_1630_3 = "1630-3"
    VALUE_1632_9 = "1632-9"
    VALUE_1633_7 = "1633-7"
    VALUE_1634_5 = "1634-5"
    VALUE_1635_2 = "1635-2"
    VALUE_1636_0 = "1636-0"
    VALUE_1637_8 = "1637-8"
    VALUE_1638_6 = "1638-6"
    VALUE_1639_4 = "1639-4"
    VALUE_1640_2 = "1640-2"
    VALUE_1641_0 = "1641-0"
    VALUE_1653_5 = "1653-5"
    VALUE_1654_3 = "1654-3"
    VALUE_1655_0 = "1655-0"
    VALUE_1656_8 = "1656-8"
    VALUE_1657_6 = "1657-6"
    VALUE_1667_5 = "1667-5"
    VALUE_1668_3 = "1668-3"
    VALUE_1670_9 = "1670-9"
    VALUE_1671_7 = "1671-7"
    VALUE_1672_5 = "1672-5"
    VALUE_1673_3 = "1673-3"
    VALUE_1679_0 = "1679-0"
    VALUE_1680_8 = "1680-8"
    VALUE_1681_6 = "1681-6"
    VALUE_1687_3 = "1687-3"
    VALUE_1688_1 = "1688-1"
    VALUE_1689_9 = "1689-9"
    VALUE_1690_7 = "1690-7"
    VALUE_1696_4 = "1696-4"
    VALUE_1697_2 = "1697-2"
    VALUE_1698_0 = "1698-0"
    VALUE_1724_4 = "1724-4"
    VALUE_1725_1 = "1725-1"
    VALUE_1726_9 = "1726-9"
    VALUE_1727_7 = "1727-7"
    VALUE_1728_5 = "1728-5"
    VALUE_1729_3 = "1729-3"
    VALUE_1730_1 = "1730-1"
    VALUE_1731_9 = "1731-9"
    VALUE_1732_7 = "1732-7"
    VALUE_1733_5 = "1733-5"
    VALUE_1068_6 = "1068-6"
    VALUE_1069_4 = "1069-4"
    VALUE_1070_2 = "1070-2"
    VALUE_1071_0 = "1071-0"
    VALUE_1072_8 = "1072-8"
    VALUE_1073_6 = "1073-6"
    VALUE_1704_6 = "1704-6"
    VALUE_1705_3 = "1705-3"
    VALUE_1711_1 = "1711-1"
    VALUE_1712_9 = "1712-9"
    VALUE_1713_7 = "1713-7"
    VALUE_1717_8 = "1717-8"
    VALUE_1718_6 = "1718-6"
    VALUE_1719_4 = "1719-4"
    VALUE_1720_2 = "1720-2"
    VALUE_1004_1 = "1004-1"
    VALUE_1006_6 = "1006-6"
    VALUE_1008_2 = "1008-2"
    VALUE_1026_4 = "1026-4"
    VALUE_1028_0 = "1028-0"
    VALUE_1033_0 = "1033-0"
    VALUE_1035_5 = "1035-5"
    VALUE_1037_1 = "1037-1"
    VALUE_1039_7 = "1039-7"
    VALUE_1078_5 = "1078-5"
    VALUE_1080_1 = "1080-1"
    VALUE_1086_8 = "1086-8"
    VALUE_1100_7 = "1100-7"
    VALUE_1106_4 = "1106-4"
    VALUE_1112_2 = "1112-2"
    VALUE_1153_6 = "1153-6"
    VALUE_1165_0 = "1165-0"
    VALUE_1167_6 = "1167-6"
    VALUE_1169_2 = "1169-2"
    VALUE_1171_8 = "1171-8"
    VALUE_1173_4 = "1173-4"
    VALUE_1180_9 = "1180-9"
    VALUE_1178_3 = "1178-3"
    VALUE_1182_5 = "1182-5"
    VALUE_1184_1 = "1184-1"
    VALUE_1189_0 = "1189-0"
    VALUE_1191_6 = "1191-6"
    VALUE_1207_0 = "1207-0"
    VALUE_1209_6 = "1209-6"
    VALUE_1250_0 = "1250-0"
    VALUE_1252_6 = "1252-6"
    VALUE_1254_2 = "1254-2"
    VALUE_1258_3 = "1258-3"
    VALUE_1256_7 = "1256-7"
    VALUE_1260_9 = "1260-9"
    VALUE_1262_5 = "1262-5"
    VALUE_1267_4 = "1267-4"
    VALUE_1269_0 = "1269-0"
    VALUE_1275_7 = "1275-7"
    VALUE_1277_3 = "1277-3"
    VALUE_1279_9 = "1279-9"
    VALUE_1297_1 = "1297-1"
    VALUE_1299_7 = "1299-7"
    VALUE_1301_1 = "1301-1"
    VALUE_1303_7 = "1303-7"
    VALUE_1317_7 = "1317-7"
    VALUE_1319_3 = "1319-3"
    VALUE_1321_9 = "1321-9"
    VALUE_1323_5 = "1323-5"
    VALUE_1340_9 = "1340-9"
    VALUE_1342_5 = "1342-5"
    VALUE_1348_2 = "1348-2"
    VALUE_1350_8 = "1350-8"
    VALUE_1352_4 = "1352-4"
    VALUE_1354_0 = "1354-0"
    VALUE_1356_5 = "1356-5"
    VALUE_1363_1 = "1363-1"
    VALUE_1368_0 = "1368-0"
    VALUE_1370_6 = "1370-6"
    VALUE_1372_2 = "1372-2"
    VALUE_1374_8 = "1374-8"
    VALUE_1376_3 = "1376-3"
    VALUE_1378_9 = "1378-9"
    VALUE_1380_5 = "1380-5"
    VALUE_1387_0 = "1387-0"
    VALUE_1389_6 = "1389-6"
    VALUE_1403_5 = "1403-5"
    VALUE_1405_0 = "1405-0"
    VALUE_1407_6 = "1407-6"
    VALUE_1409_2 = "1409-2"
    VALUE_1439_9 = "1439-9"
    VALUE_1448_0 = "1448-0"
    VALUE_1460_5 = "1460-5"
    VALUE_1462_1 = "1462-1"
    VALUE_1487_8 = "1487-8"
    VALUE_1541_2 = "1541-2"
    VALUE_1543_8 = "1543-8"
    VALUE_1545_3 = "1545-3"
    VALUE_1547_9 = "1547-9"
    VALUE_1549_5 = "1549-5"
    VALUE_1556_0 = "1556-0"
    VALUE_1558_6 = "1558-6"
    VALUE_1560_2 = "1560-2"
    VALUE_1562_8 = "1562-8"
    VALUE_1564_4 = "1564-4"
    VALUE_1576_8 = "1576-8"
    VALUE_1582_6 = "1582-6"
    VALUE_1584_2 = "1584-2"
    VALUE_1607_1 = "1607-1"
    VALUE_1643_6 = "1643-6"
    VALUE_1074_4 = "1074-4"
    VALUE_1645_1 = "1645-1"
    VALUE_1647_7 = "1647-7"
    VALUE_1649_3 = "1649-3"
    VALUE_1651_9 = "1651-9"
    VALUE_1659_2 = "1659-2"
    VALUE_1661_8 = "1661-8"
    VALUE_1663_4 = "1663-4"
    VALUE_1665_9 = "1665-9"
    VALUE_1675_8 = "1675-8"
    VALUE_1677_4 = "1677-4"
    VALUE_1683_2 = "1683-2"
    VALUE_1685_7 = "1685-7"
    VALUE_1692_3 = "1692-3"
    VALUE_1694_9 = "1694-9"
    VALUE_1700_4 = "1700-4"
    VALUE_1702_0 = "1702-0"
    VALUE_1707_9 = "1707-9"
    VALUE_1709_5 = "1709-5"
    VALUE_1715_2 = "1715-2"
    VALUE_1722_8 = "1722-8"
    VALUE_1002_5 = "1002-5"
    VALUE_2129_5 = "2129-5"
    VALUE_2108_9 = "2108-9"
    VALUE_2109_7 = "2109-7"
    VALUE_2110_5 = "2110-5"
    VALUE_2111_3 = "2111-3"
    VALUE_2112_1 = "2112-1"
    VALUE_2113_9 = "2113-9"
    VALUE_2114_7 = "2114-7"
    VALUE_2115_4 = "2115-4"
    VALUE_2116_2 = "2116-2"
    VALUE_2118_8 = "2118-8"
    VALUE_2126_1 = "2126-1"
    VALUE_2119_6 = "2119-6"
    VALUE_2120_4 = "2120-4"
    VALUE_2121_2 = "2121-2"
    VALUE_2122_0 = "2122-0"
    VALUE_2127_9 = "2127-9"
    VALUE_2123_8 = "2123-8"
    VALUE_2124_6 = "2124-6"
    VALUE_2125_3 = "2125-3"
    VALUE_2106_3 = "2106-3"
    VALUE_2131_1 = "2131-1"


class RaceAfricanAmericanAfrican(Enum):
    """
    specDomain: S15771 (C-0-T14914-S15768-S15771-cpt)
    :cvar VALUE_2060_2:
    :cvar VALUE_2061_0:
    :cvar VALUE_2062_8:
    :cvar VALUE_2063_6:
    :cvar VALUE_2064_4:
    :cvar VALUE_2065_1:
    :cvar VALUE_2066_9:
    """
    VALUE_2060_2 = "2060-2"
    VALUE_2061_0 = "2061-0"
    VALUE_2062_8 = "2062-8"
    VALUE_2063_6 = "2063-6"
    VALUE_2064_4 = "2064-4"
    VALUE_2065_1 = "2065-1"
    VALUE_2066_9 = "2066-9"


class RaceAlaskanIndian(Enum):
    """
    specDomain: S15471 (C-0-T14914-S14915-S15470-S15471-cpt)
    :cvar VALUE_1739_2:
    :cvar VALUE_1740_0:
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    :cvar VALUE_1811_9:
    :cvar VALUE_1737_6:
    """
    VALUE_1739_2 = "1739-2"
    VALUE_1740_0 = "1740-0"
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"
    VALUE_1811_9 = "1811-9"
    VALUE_1737_6 = "1737-6"


class RaceAlaskanIndianAthabascan(Enum):
    """
    specDomain: S15472 (C-0-T14914-S14915-S15470-S15471-S15472-cpt)
    :cvar VALUE_1739_2:
    :cvar VALUE_1740_0:
    """
    VALUE_1739_2 = "1739-2"
    VALUE_1740_0 = "1740-0"


class RaceAlaskanNative(Enum):
    """
    specDomain: S15470 (C-0-T14914-S14915-S15470-cpt)
    :cvar VALUE_1739_2:
    :cvar VALUE_1740_0:
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    :cvar VALUE_1811_9:
    :cvar VALUE_1737_6:
    :cvar VALUE_1968_7:
    :cvar VALUE_1969_5:
    :cvar VALUE_1970_3:
    :cvar VALUE_1972_9:
    :cvar VALUE_1973_7:
    :cvar VALUE_1974_5:
    :cvar VALUE_1975_2:
    :cvar VALUE_1976_0:
    :cvar VALUE_1977_8:
    :cvar VALUE_1978_6:
    :cvar VALUE_1979_4:
    :cvar VALUE_1980_2:
    :cvar VALUE_1981_0:
    :cvar VALUE_1982_8:
    :cvar VALUE_1984_4:
    :cvar VALUE_1985_1:
    :cvar VALUE_1986_9:
    :cvar VALUE_1987_7:
    :cvar VALUE_1988_5:
    :cvar VALUE_1992_7:
    :cvar VALUE_1994_3:
    :cvar VALUE_1993_5:
    :cvar VALUE_1995_0:
    :cvar VALUE_1996_8:
    :cvar VALUE_1997_6:
    :cvar VALUE_1998_4:
    :cvar VALUE_1999_2:
    :cvar VALUE_2000_8:
    :cvar VALUE_2006_5:
    :cvar VALUE_2007_3:
    :cvar VALUE_2008_1:
    :cvar VALUE_2009_9:
    :cvar VALUE_2010_7:
    :cvar VALUE_2011_5:
    :cvar VALUE_2012_3:
    :cvar VALUE_2013_1:
    :cvar VALUE_2015_6:
    :cvar VALUE_2014_9:
    :cvar VALUE_2016_4:
    :cvar VALUE_2017_2:
    :cvar VALUE_2018_0:
    :cvar VALUE_2019_8:
    :cvar VALUE_2020_6:
    :cvar VALUE_2023_0:
    :cvar VALUE_2024_8:
    :cvar VALUE_2021_4:
    :cvar VALUE_2022_2:
    :cvar VALUE_2025_5:
    :cvar VALUE_2026_3:
    :cvar VALUE_1966_1:
    :cvar VALUE_1990_1:
    :cvar VALUE_2002_4:
    :cvar VALUE_2004_0:
    :cvar VALUE_1844_0:
    :cvar VALUE_1845_7:
    :cvar VALUE_1846_5:
    :cvar VALUE_1847_3:
    :cvar VALUE_1849_9:
    :cvar VALUE_1848_1:
    :cvar VALUE_1850_7:
    :cvar VALUE_1851_5:
    :cvar VALUE_1852_3:
    :cvar VALUE_1853_1:
    :cvar VALUE_1854_9:
    :cvar VALUE_1855_6:
    :cvar VALUE_1856_4:
    :cvar VALUE_1857_2:
    :cvar VALUE_1858_0:
    :cvar VALUE_1859_8:
    :cvar VALUE_1860_6:
    :cvar VALUE_1861_4:
    :cvar VALUE_1862_2:
    :cvar VALUE_1863_0:
    :cvar VALUE_1864_8:
    :cvar VALUE_1865_5:
    :cvar VALUE_1866_3:
    :cvar VALUE_1867_1:
    :cvar VALUE_1868_9:
    :cvar VALUE_1869_7:
    :cvar VALUE_1889_5:
    :cvar VALUE_1870_5:
    :cvar VALUE_1871_3:
    :cvar VALUE_1872_1:
    :cvar VALUE_1873_9:
    :cvar VALUE_1874_7:
    :cvar VALUE_1875_4:
    :cvar VALUE_1876_2:
    :cvar VALUE_1877_0:
    :cvar VALUE_1878_8:
    :cvar VALUE_1879_6:
    :cvar VALUE_1880_4:
    :cvar VALUE_1881_2:
    :cvar VALUE_1882_0:
    :cvar VALUE_1883_8:
    :cvar VALUE_1884_6:
    :cvar VALUE_1885_3:
    :cvar VALUE_1886_1:
    :cvar VALUE_1887_9:
    :cvar VALUE_1888_7:
    :cvar VALUE_1891_1:
    :cvar VALUE_1892_9:
    :cvar VALUE_1893_7:
    :cvar VALUE_1894_5:
    :cvar VALUE_1896_0:
    :cvar VALUE_1897_8:
    :cvar VALUE_1898_6:
    :cvar VALUE_1899_4:
    :cvar VALUE_1900_0:
    :cvar VALUE_1901_8:
    :cvar VALUE_1902_6:
    :cvar VALUE_1903_4:
    :cvar VALUE_1904_2:
    :cvar VALUE_1905_9:
    :cvar VALUE_1906_7:
    :cvar VALUE_1907_5:
    :cvar VALUE_1908_3:
    :cvar VALUE_1909_1:
    :cvar VALUE_1910_9:
    :cvar VALUE_1911_7:
    :cvar VALUE_1912_5:
    :cvar VALUE_1913_3:
    :cvar VALUE_1914_1:
    :cvar VALUE_1915_8:
    :cvar VALUE_1916_6:
    :cvar VALUE_1917_4:
    :cvar VALUE_1962_0:
    :cvar VALUE_1918_2:
    :cvar VALUE_1919_0:
    :cvar VALUE_1920_8:
    :cvar VALUE_1921_6:
    :cvar VALUE_1922_4:
    :cvar VALUE_1923_2:
    :cvar VALUE_1924_0:
    :cvar VALUE_1925_7:
    :cvar VALUE_1926_5:
    :cvar VALUE_1927_3:
    :cvar VALUE_1928_1:
    :cvar VALUE_1929_9:
    :cvar VALUE_1930_7:
    :cvar VALUE_1931_5:
    :cvar VALUE_1932_3:
    :cvar VALUE_1933_1:
    :cvar VALUE_1934_9:
    :cvar VALUE_1935_6:
    :cvar VALUE_1937_2:
    :cvar VALUE_1938_0:
    :cvar VALUE_1936_4:
    :cvar VALUE_1940_6:
    :cvar VALUE_1939_8:
    :cvar VALUE_1941_4:
    :cvar VALUE_1942_2:
    :cvar VALUE_1943_0:
    :cvar VALUE_1944_8:
    :cvar VALUE_1945_5:
    :cvar VALUE_1946_3:
    :cvar VALUE_1947_1:
    :cvar VALUE_1948_9:
    :cvar VALUE_1949_7:
    :cvar VALUE_1950_5:
    :cvar VALUE_1952_1:
    :cvar VALUE_1953_9:
    :cvar VALUE_1954_7:
    :cvar VALUE_1963_8:
    :cvar VALUE_1951_3:
    :cvar VALUE_1955_4:
    :cvar VALUE_1956_2:
    :cvar VALUE_1957_0:
    :cvar VALUE_1958_8:
    :cvar VALUE_1959_6:
    :cvar VALUE_1960_4:
    :cvar VALUE_1961_2:
    :cvar VALUE_1964_6:
    :cvar VALUE_1840_8:
    :cvar VALUE_1842_4:
    :cvar VALUE_1735_0:
    """
    VALUE_1739_2 = "1739-2"
    VALUE_1740_0 = "1740-0"
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"
    VALUE_1811_9 = "1811-9"
    VALUE_1737_6 = "1737-6"
    VALUE_1968_7 = "1968-7"
    VALUE_1969_5 = "1969-5"
    VALUE_1970_3 = "1970-3"
    VALUE_1972_9 = "1972-9"
    VALUE_1973_7 = "1973-7"
    VALUE_1974_5 = "1974-5"
    VALUE_1975_2 = "1975-2"
    VALUE_1976_0 = "1976-0"
    VALUE_1977_8 = "1977-8"
    VALUE_1978_6 = "1978-6"
    VALUE_1979_4 = "1979-4"
    VALUE_1980_2 = "1980-2"
    VALUE_1981_0 = "1981-0"
    VALUE_1982_8 = "1982-8"
    VALUE_1984_4 = "1984-4"
    VALUE_1985_1 = "1985-1"
    VALUE_1986_9 = "1986-9"
    VALUE_1987_7 = "1987-7"
    VALUE_1988_5 = "1988-5"
    VALUE_1992_7 = "1992-7"
    VALUE_1994_3 = "1994-3"
    VALUE_1993_5 = "1993-5"
    VALUE_1995_0 = "1995-0"
    VALUE_1996_8 = "1996-8"
    VALUE_1997_6 = "1997-6"
    VALUE_1998_4 = "1998-4"
    VALUE_1999_2 = "1999-2"
    VALUE_2000_8 = "2000-8"
    VALUE_2006_5 = "2006-5"
    VALUE_2007_3 = "2007-3"
    VALUE_2008_1 = "2008-1"
    VALUE_2009_9 = "2009-9"
    VALUE_2010_7 = "2010-7"
    VALUE_2011_5 = "2011-5"
    VALUE_2012_3 = "2012-3"
    VALUE_2013_1 = "2013-1"
    VALUE_2015_6 = "2015-6"
    VALUE_2014_9 = "2014-9"
    VALUE_2016_4 = "2016-4"
    VALUE_2017_2 = "2017-2"
    VALUE_2018_0 = "2018-0"
    VALUE_2019_8 = "2019-8"
    VALUE_2020_6 = "2020-6"
    VALUE_2023_0 = "2023-0"
    VALUE_2024_8 = "2024-8"
    VALUE_2021_4 = "2021-4"
    VALUE_2022_2 = "2022-2"
    VALUE_2025_5 = "2025-5"
    VALUE_2026_3 = "2026-3"
    VALUE_1966_1 = "1966-1"
    VALUE_1990_1 = "1990-1"
    VALUE_2002_4 = "2002-4"
    VALUE_2004_0 = "2004-0"
    VALUE_1844_0 = "1844-0"
    VALUE_1845_7 = "1845-7"
    VALUE_1846_5 = "1846-5"
    VALUE_1847_3 = "1847-3"
    VALUE_1849_9 = "1849-9"
    VALUE_1848_1 = "1848-1"
    VALUE_1850_7 = "1850-7"
    VALUE_1851_5 = "1851-5"
    VALUE_1852_3 = "1852-3"
    VALUE_1853_1 = "1853-1"
    VALUE_1854_9 = "1854-9"
    VALUE_1855_6 = "1855-6"
    VALUE_1856_4 = "1856-4"
    VALUE_1857_2 = "1857-2"
    VALUE_1858_0 = "1858-0"
    VALUE_1859_8 = "1859-8"
    VALUE_1860_6 = "1860-6"
    VALUE_1861_4 = "1861-4"
    VALUE_1862_2 = "1862-2"
    VALUE_1863_0 = "1863-0"
    VALUE_1864_8 = "1864-8"
    VALUE_1865_5 = "1865-5"
    VALUE_1866_3 = "1866-3"
    VALUE_1867_1 = "1867-1"
    VALUE_1868_9 = "1868-9"
    VALUE_1869_7 = "1869-7"
    VALUE_1889_5 = "1889-5"
    VALUE_1870_5 = "1870-5"
    VALUE_1871_3 = "1871-3"
    VALUE_1872_1 = "1872-1"
    VALUE_1873_9 = "1873-9"
    VALUE_1874_7 = "1874-7"
    VALUE_1875_4 = "1875-4"
    VALUE_1876_2 = "1876-2"
    VALUE_1877_0 = "1877-0"
    VALUE_1878_8 = "1878-8"
    VALUE_1879_6 = "1879-6"
    VALUE_1880_4 = "1880-4"
    VALUE_1881_2 = "1881-2"
    VALUE_1882_0 = "1882-0"
    VALUE_1883_8 = "1883-8"
    VALUE_1884_6 = "1884-6"
    VALUE_1885_3 = "1885-3"
    VALUE_1886_1 = "1886-1"
    VALUE_1887_9 = "1887-9"
    VALUE_1888_7 = "1888-7"
    VALUE_1891_1 = "1891-1"
    VALUE_1892_9 = "1892-9"
    VALUE_1893_7 = "1893-7"
    VALUE_1894_5 = "1894-5"
    VALUE_1896_0 = "1896-0"
    VALUE_1897_8 = "1897-8"
    VALUE_1898_6 = "1898-6"
    VALUE_1899_4 = "1899-4"
    VALUE_1900_0 = "1900-0"
    VALUE_1901_8 = "1901-8"
    VALUE_1902_6 = "1902-6"
    VALUE_1903_4 = "1903-4"
    VALUE_1904_2 = "1904-2"
    VALUE_1905_9 = "1905-9"
    VALUE_1906_7 = "1906-7"
    VALUE_1907_5 = "1907-5"
    VALUE_1908_3 = "1908-3"
    VALUE_1909_1 = "1909-1"
    VALUE_1910_9 = "1910-9"
    VALUE_1911_7 = "1911-7"
    VALUE_1912_5 = "1912-5"
    VALUE_1913_3 = "1913-3"
    VALUE_1914_1 = "1914-1"
    VALUE_1915_8 = "1915-8"
    VALUE_1916_6 = "1916-6"
    VALUE_1917_4 = "1917-4"
    VALUE_1962_0 = "1962-0"
    VALUE_1918_2 = "1918-2"
    VALUE_1919_0 = "1919-0"
    VALUE_1920_8 = "1920-8"
    VALUE_1921_6 = "1921-6"
    VALUE_1922_4 = "1922-4"
    VALUE_1923_2 = "1923-2"
    VALUE_1924_0 = "1924-0"
    VALUE_1925_7 = "1925-7"
    VALUE_1926_5 = "1926-5"
    VALUE_1927_3 = "1927-3"
    VALUE_1928_1 = "1928-1"
    VALUE_1929_9 = "1929-9"
    VALUE_1930_7 = "1930-7"
    VALUE_1931_5 = "1931-5"
    VALUE_1932_3 = "1932-3"
    VALUE_1933_1 = "1933-1"
    VALUE_1934_9 = "1934-9"
    VALUE_1935_6 = "1935-6"
    VALUE_1937_2 = "1937-2"
    VALUE_1938_0 = "1938-0"
    VALUE_1936_4 = "1936-4"
    VALUE_1940_6 = "1940-6"
    VALUE_1939_8 = "1939-8"
    VALUE_1941_4 = "1941-4"
    VALUE_1942_2 = "1942-2"
    VALUE_1943_0 = "1943-0"
    VALUE_1944_8 = "1944-8"
    VALUE_1945_5 = "1945-5"
    VALUE_1946_3 = "1946-3"
    VALUE_1947_1 = "1947-1"
    VALUE_1948_9 = "1948-9"
    VALUE_1949_7 = "1949-7"
    VALUE_1950_5 = "1950-5"
    VALUE_1952_1 = "1952-1"
    VALUE_1953_9 = "1953-9"
    VALUE_1954_7 = "1954-7"
    VALUE_1963_8 = "1963-8"
    VALUE_1951_3 = "1951-3"
    VALUE_1955_4 = "1955-4"
    VALUE_1956_2 = "1956-2"
    VALUE_1957_0 = "1957-0"
    VALUE_1958_8 = "1958-8"
    VALUE_1959_6 = "1959-6"
    VALUE_1960_4 = "1960-4"
    VALUE_1961_2 = "1961-2"
    VALUE_1964_6 = "1964-6"
    VALUE_1840_8 = "1840-8"
    VALUE_1842_4 = "1842-4"
    VALUE_1735_0 = "1735-0"


class RaceAlaskanNativeAleut(Enum):
    """
    specDomain: S15690 (C-0-T14914-S14915-S15470-S15690-cpt)
    :cvar VALUE_1968_7:
    :cvar VALUE_1969_5:
    :cvar VALUE_1970_3:
    :cvar VALUE_1972_9:
    :cvar VALUE_1973_7:
    :cvar VALUE_1974_5:
    :cvar VALUE_1975_2:
    :cvar VALUE_1976_0:
    :cvar VALUE_1977_8:
    :cvar VALUE_1978_6:
    :cvar VALUE_1979_4:
    :cvar VALUE_1980_2:
    :cvar VALUE_1981_0:
    :cvar VALUE_1982_8:
    :cvar VALUE_1984_4:
    :cvar VALUE_1985_1:
    :cvar VALUE_1986_9:
    :cvar VALUE_1987_7:
    :cvar VALUE_1988_5:
    :cvar VALUE_1992_7:
    :cvar VALUE_1994_3:
    :cvar VALUE_1993_5:
    :cvar VALUE_1995_0:
    :cvar VALUE_1996_8:
    :cvar VALUE_1997_6:
    :cvar VALUE_1998_4:
    :cvar VALUE_1999_2:
    :cvar VALUE_2000_8:
    :cvar VALUE_2006_5:
    :cvar VALUE_2007_3:
    :cvar VALUE_2008_1:
    :cvar VALUE_2009_9:
    :cvar VALUE_2010_7:
    :cvar VALUE_2011_5:
    :cvar VALUE_2012_3:
    :cvar VALUE_2013_1:
    :cvar VALUE_2015_6:
    :cvar VALUE_2014_9:
    :cvar VALUE_2016_4:
    :cvar VALUE_2017_2:
    :cvar VALUE_2018_0:
    :cvar VALUE_2019_8:
    :cvar VALUE_2020_6:
    :cvar VALUE_2023_0:
    :cvar VALUE_2024_8:
    :cvar VALUE_2021_4:
    :cvar VALUE_2022_2:
    :cvar VALUE_2025_5:
    :cvar VALUE_2026_3:
    :cvar VALUE_1966_1:
    :cvar VALUE_1990_1:
    :cvar VALUE_2002_4:
    :cvar VALUE_2004_0:
    """
    VALUE_1968_7 = "1968-7"
    VALUE_1969_5 = "1969-5"
    VALUE_1970_3 = "1970-3"
    VALUE_1972_9 = "1972-9"
    VALUE_1973_7 = "1973-7"
    VALUE_1974_5 = "1974-5"
    VALUE_1975_2 = "1975-2"
    VALUE_1976_0 = "1976-0"
    VALUE_1977_8 = "1977-8"
    VALUE_1978_6 = "1978-6"
    VALUE_1979_4 = "1979-4"
    VALUE_1980_2 = "1980-2"
    VALUE_1981_0 = "1981-0"
    VALUE_1982_8 = "1982-8"
    VALUE_1984_4 = "1984-4"
    VALUE_1985_1 = "1985-1"
    VALUE_1986_9 = "1986-9"
    VALUE_1987_7 = "1987-7"
    VALUE_1988_5 = "1988-5"
    VALUE_1992_7 = "1992-7"
    VALUE_1994_3 = "1994-3"
    VALUE_1993_5 = "1993-5"
    VALUE_1995_0 = "1995-0"
    VALUE_1996_8 = "1996-8"
    VALUE_1997_6 = "1997-6"
    VALUE_1998_4 = "1998-4"
    VALUE_1999_2 = "1999-2"
    VALUE_2000_8 = "2000-8"
    VALUE_2006_5 = "2006-5"
    VALUE_2007_3 = "2007-3"
    VALUE_2008_1 = "2008-1"
    VALUE_2009_9 = "2009-9"
    VALUE_2010_7 = "2010-7"
    VALUE_2011_5 = "2011-5"
    VALUE_2012_3 = "2012-3"
    VALUE_2013_1 = "2013-1"
    VALUE_2015_6 = "2015-6"
    VALUE_2014_9 = "2014-9"
    VALUE_2016_4 = "2016-4"
    VALUE_2017_2 = "2017-2"
    VALUE_2018_0 = "2018-0"
    VALUE_2019_8 = "2019-8"
    VALUE_2020_6 = "2020-6"
    VALUE_2023_0 = "2023-0"
    VALUE_2024_8 = "2024-8"
    VALUE_2021_4 = "2021-4"
    VALUE_2022_2 = "2022-2"
    VALUE_2025_5 = "2025-5"
    VALUE_2026_3 = "2026-3"
    VALUE_1966_1 = "1966-1"
    VALUE_1990_1 = "1990-1"
    VALUE_2002_4 = "2002-4"
    VALUE_2004_0 = "2004-0"


class RaceAlaskanNativeAleutAlutiiq(Enum):
    """
    specDomain: S15691 (C-0-T14914-S14915-S15470-S15690-S15691-cpt)
    :cvar VALUE_1968_7:
    :cvar VALUE_1969_5:
    :cvar VALUE_1970_3:
    """
    VALUE_1968_7 = "1968-7"
    VALUE_1969_5 = "1969-5"
    VALUE_1970_3 = "1970-3"


class RaceAlaskanNativeAleutBristolBay(Enum):
    """
    specDomain: S16466 (C-0-T14914-S14915-S15470-S15690-S16466-cpt)
    :cvar VALUE_1972_9:
    :cvar VALUE_1973_7:
    :cvar VALUE_1974_5:
    :cvar VALUE_1975_2:
    :cvar VALUE_1976_0:
    :cvar VALUE_1977_8:
    :cvar VALUE_1978_6:
    :cvar VALUE_1979_4:
    :cvar VALUE_1980_2:
    :cvar VALUE_1981_0:
    :cvar VALUE_1982_8:
    """
    VALUE_1972_9 = "1972-9"
    VALUE_1973_7 = "1973-7"
    VALUE_1974_5 = "1974-5"
    VALUE_1975_2 = "1975-2"
    VALUE_1976_0 = "1976-0"
    VALUE_1977_8 = "1977-8"
    VALUE_1978_6 = "1978-6"
    VALUE_1979_4 = "1979-4"
    VALUE_1980_2 = "1980-2"
    VALUE_1981_0 = "1981-0"
    VALUE_1982_8 = "1982-8"


class RaceAlaskanNativeAleutChugach(Enum):
    """
    specDomain: S15705 (C-0-T14914-S14915-S15470-S15690-S15705-cpt)
    :cvar VALUE_1984_4:
    :cvar VALUE_1985_1:
    :cvar VALUE_1986_9:
    :cvar VALUE_1987_7:
    :cvar VALUE_1988_5:
    """
    VALUE_1984_4 = "1984-4"
    VALUE_1985_1 = "1985-1"
    VALUE_1986_9 = "1986-9"
    VALUE_1987_7 = "1987-7"
    VALUE_1988_5 = "1988-5"


class RaceAlaskanNativeAleutKoniag(Enum):
    """
    specDomain: S15711 (C-0-T14914-S14915-S15470-S15690-S15711-cpt)
    :cvar VALUE_1992_7:
    :cvar VALUE_1994_3:
    :cvar VALUE_1993_5:
    :cvar VALUE_1995_0:
    :cvar VALUE_1996_8:
    :cvar VALUE_1997_6:
    :cvar VALUE_1998_4:
    :cvar VALUE_1999_2:
    :cvar VALUE_2000_8:
    """
    VALUE_1992_7 = "1992-7"
    VALUE_1994_3 = "1994-3"
    VALUE_1993_5 = "1993-5"
    VALUE_1995_0 = "1995-0"
    VALUE_1996_8 = "1996-8"
    VALUE_1997_6 = "1997-6"
    VALUE_1998_4 = "1998-4"
    VALUE_1999_2 = "1999-2"
    VALUE_2000_8 = "2000-8"


class RaceAlaskanNativeAleutUnangan(Enum):
    """
    specDomain: S15722 (C-0-T14914-S14915-S15470-S15690-S15722-cpt)
    :cvar VALUE_2006_5:
    :cvar VALUE_2007_3:
    :cvar VALUE_2008_1:
    :cvar VALUE_2009_9:
    :cvar VALUE_2010_7:
    :cvar VALUE_2011_5:
    :cvar VALUE_2012_3:
    :cvar VALUE_2013_1:
    :cvar VALUE_2015_6:
    :cvar VALUE_2014_9:
    :cvar VALUE_2016_4:
    :cvar VALUE_2017_2:
    :cvar VALUE_2018_0:
    :cvar VALUE_2019_8:
    :cvar VALUE_2020_6:
    :cvar VALUE_2023_0:
    :cvar VALUE_2024_8:
    :cvar VALUE_2021_4:
    :cvar VALUE_2022_2:
    :cvar VALUE_2025_5:
    :cvar VALUE_2026_3:
    """
    VALUE_2006_5 = "2006-5"
    VALUE_2007_3 = "2007-3"
    VALUE_2008_1 = "2008-1"
    VALUE_2009_9 = "2009-9"
    VALUE_2010_7 = "2010-7"
    VALUE_2011_5 = "2011-5"
    VALUE_2012_3 = "2012-3"
    VALUE_2013_1 = "2013-1"
    VALUE_2015_6 = "2015-6"
    VALUE_2014_9 = "2014-9"
    VALUE_2016_4 = "2016-4"
    VALUE_2017_2 = "2017-2"
    VALUE_2018_0 = "2018-0"
    VALUE_2019_8 = "2019-8"
    VALUE_2020_6 = "2020-6"
    VALUE_2023_0 = "2023-0"
    VALUE_2024_8 = "2024-8"
    VALUE_2021_4 = "2021-4"
    VALUE_2022_2 = "2022-2"
    VALUE_2025_5 = "2025-5"
    VALUE_2026_3 = "2026-3"


class RaceAlaskanNativeEskimo(Enum):
    """
    specDomain: S15569 (C-0-T14914-S14915-S15470-S15569-cpt)
    :cvar VALUE_1844_0:
    :cvar VALUE_1845_7:
    :cvar VALUE_1846_5:
    :cvar VALUE_1847_3:
    :cvar VALUE_1849_9:
    :cvar VALUE_1848_1:
    :cvar VALUE_1850_7:
    :cvar VALUE_1851_5:
    :cvar VALUE_1852_3:
    :cvar VALUE_1853_1:
    :cvar VALUE_1854_9:
    :cvar VALUE_1855_6:
    :cvar VALUE_1856_4:
    :cvar VALUE_1857_2:
    :cvar VALUE_1858_0:
    :cvar VALUE_1859_8:
    :cvar VALUE_1860_6:
    :cvar VALUE_1861_4:
    :cvar VALUE_1862_2:
    :cvar VALUE_1863_0:
    :cvar VALUE_1864_8:
    :cvar VALUE_1865_5:
    :cvar VALUE_1866_3:
    :cvar VALUE_1867_1:
    :cvar VALUE_1868_9:
    :cvar VALUE_1869_7:
    :cvar VALUE_1889_5:
    :cvar VALUE_1870_5:
    :cvar VALUE_1871_3:
    :cvar VALUE_1872_1:
    :cvar VALUE_1873_9:
    :cvar VALUE_1874_7:
    :cvar VALUE_1875_4:
    :cvar VALUE_1876_2:
    :cvar VALUE_1877_0:
    :cvar VALUE_1878_8:
    :cvar VALUE_1879_6:
    :cvar VALUE_1880_4:
    :cvar VALUE_1881_2:
    :cvar VALUE_1882_0:
    :cvar VALUE_1883_8:
    :cvar VALUE_1884_6:
    :cvar VALUE_1885_3:
    :cvar VALUE_1886_1:
    :cvar VALUE_1887_9:
    :cvar VALUE_1888_7:
    :cvar VALUE_1891_1:
    :cvar VALUE_1892_9:
    :cvar VALUE_1893_7:
    :cvar VALUE_1894_5:
    :cvar VALUE_1896_0:
    :cvar VALUE_1897_8:
    :cvar VALUE_1898_6:
    :cvar VALUE_1899_4:
    :cvar VALUE_1900_0:
    :cvar VALUE_1901_8:
    :cvar VALUE_1902_6:
    :cvar VALUE_1903_4:
    :cvar VALUE_1904_2:
    :cvar VALUE_1905_9:
    :cvar VALUE_1906_7:
    :cvar VALUE_1907_5:
    :cvar VALUE_1908_3:
    :cvar VALUE_1909_1:
    :cvar VALUE_1910_9:
    :cvar VALUE_1911_7:
    :cvar VALUE_1912_5:
    :cvar VALUE_1913_3:
    :cvar VALUE_1914_1:
    :cvar VALUE_1915_8:
    :cvar VALUE_1916_6:
    :cvar VALUE_1917_4:
    :cvar VALUE_1962_0:
    :cvar VALUE_1918_2:
    :cvar VALUE_1919_0:
    :cvar VALUE_1920_8:
    :cvar VALUE_1921_6:
    :cvar VALUE_1922_4:
    :cvar VALUE_1923_2:
    :cvar VALUE_1924_0:
    :cvar VALUE_1925_7:
    :cvar VALUE_1926_5:
    :cvar VALUE_1927_3:
    :cvar VALUE_1928_1:
    :cvar VALUE_1929_9:
    :cvar VALUE_1930_7:
    :cvar VALUE_1931_5:
    :cvar VALUE_1932_3:
    :cvar VALUE_1933_1:
    :cvar VALUE_1934_9:
    :cvar VALUE_1935_6:
    :cvar VALUE_1937_2:
    :cvar VALUE_1938_0:
    :cvar VALUE_1936_4:
    :cvar VALUE_1940_6:
    :cvar VALUE_1939_8:
    :cvar VALUE_1941_4:
    :cvar VALUE_1942_2:
    :cvar VALUE_1943_0:
    :cvar VALUE_1944_8:
    :cvar VALUE_1945_5:
    :cvar VALUE_1946_3:
    :cvar VALUE_1947_1:
    :cvar VALUE_1948_9:
    :cvar VALUE_1949_7:
    :cvar VALUE_1950_5:
    :cvar VALUE_1952_1:
    :cvar VALUE_1953_9:
    :cvar VALUE_1954_7:
    :cvar VALUE_1963_8:
    :cvar VALUE_1951_3:
    :cvar VALUE_1955_4:
    :cvar VALUE_1956_2:
    :cvar VALUE_1957_0:
    :cvar VALUE_1958_8:
    :cvar VALUE_1959_6:
    :cvar VALUE_1960_4:
    :cvar VALUE_1961_2:
    :cvar VALUE_1964_6:
    :cvar VALUE_1840_8:
    :cvar VALUE_1842_4:
    """
    VALUE_1844_0 = "1844-0"
    VALUE_1845_7 = "1845-7"
    VALUE_1846_5 = "1846-5"
    VALUE_1847_3 = "1847-3"
    VALUE_1849_9 = "1849-9"
    VALUE_1848_1 = "1848-1"
    VALUE_1850_7 = "1850-7"
    VALUE_1851_5 = "1851-5"
    VALUE_1852_3 = "1852-3"
    VALUE_1853_1 = "1853-1"
    VALUE_1854_9 = "1854-9"
    VALUE_1855_6 = "1855-6"
    VALUE_1856_4 = "1856-4"
    VALUE_1857_2 = "1857-2"
    VALUE_1858_0 = "1858-0"
    VALUE_1859_8 = "1859-8"
    VALUE_1860_6 = "1860-6"
    VALUE_1861_4 = "1861-4"
    VALUE_1862_2 = "1862-2"
    VALUE_1863_0 = "1863-0"
    VALUE_1864_8 = "1864-8"
    VALUE_1865_5 = "1865-5"
    VALUE_1866_3 = "1866-3"
    VALUE_1867_1 = "1867-1"
    VALUE_1868_9 = "1868-9"
    VALUE_1869_7 = "1869-7"
    VALUE_1889_5 = "1889-5"
    VALUE_1870_5 = "1870-5"
    VALUE_1871_3 = "1871-3"
    VALUE_1872_1 = "1872-1"
    VALUE_1873_9 = "1873-9"
    VALUE_1874_7 = "1874-7"
    VALUE_1875_4 = "1875-4"
    VALUE_1876_2 = "1876-2"
    VALUE_1877_0 = "1877-0"
    VALUE_1878_8 = "1878-8"
    VALUE_1879_6 = "1879-6"
    VALUE_1880_4 = "1880-4"
    VALUE_1881_2 = "1881-2"
    VALUE_1882_0 = "1882-0"
    VALUE_1883_8 = "1883-8"
    VALUE_1884_6 = "1884-6"
    VALUE_1885_3 = "1885-3"
    VALUE_1886_1 = "1886-1"
    VALUE_1887_9 = "1887-9"
    VALUE_1888_7 = "1888-7"
    VALUE_1891_1 = "1891-1"
    VALUE_1892_9 = "1892-9"
    VALUE_1893_7 = "1893-7"
    VALUE_1894_5 = "1894-5"
    VALUE_1896_0 = "1896-0"
    VALUE_1897_8 = "1897-8"
    VALUE_1898_6 = "1898-6"
    VALUE_1899_4 = "1899-4"
    VALUE_1900_0 = "1900-0"
    VALUE_1901_8 = "1901-8"
    VALUE_1902_6 = "1902-6"
    VALUE_1903_4 = "1903-4"
    VALUE_1904_2 = "1904-2"
    VALUE_1905_9 = "1905-9"
    VALUE_1906_7 = "1906-7"
    VALUE_1907_5 = "1907-5"
    VALUE_1908_3 = "1908-3"
    VALUE_1909_1 = "1909-1"
    VALUE_1910_9 = "1910-9"
    VALUE_1911_7 = "1911-7"
    VALUE_1912_5 = "1912-5"
    VALUE_1913_3 = "1913-3"
    VALUE_1914_1 = "1914-1"
    VALUE_1915_8 = "1915-8"
    VALUE_1916_6 = "1916-6"
    VALUE_1917_4 = "1917-4"
    VALUE_1962_0 = "1962-0"
    VALUE_1918_2 = "1918-2"
    VALUE_1919_0 = "1919-0"
    VALUE_1920_8 = "1920-8"
    VALUE_1921_6 = "1921-6"
    VALUE_1922_4 = "1922-4"
    VALUE_1923_2 = "1923-2"
    VALUE_1924_0 = "1924-0"
    VALUE_1925_7 = "1925-7"
    VALUE_1926_5 = "1926-5"
    VALUE_1927_3 = "1927-3"
    VALUE_1928_1 = "1928-1"
    VALUE_1929_9 = "1929-9"
    VALUE_1930_7 = "1930-7"
    VALUE_1931_5 = "1931-5"
    VALUE_1932_3 = "1932-3"
    VALUE_1933_1 = "1933-1"
    VALUE_1934_9 = "1934-9"
    VALUE_1935_6 = "1935-6"
    VALUE_1937_2 = "1937-2"
    VALUE_1938_0 = "1938-0"
    VALUE_1936_4 = "1936-4"
    VALUE_1940_6 = "1940-6"
    VALUE_1939_8 = "1939-8"
    VALUE_1941_4 = "1941-4"
    VALUE_1942_2 = "1942-2"
    VALUE_1943_0 = "1943-0"
    VALUE_1944_8 = "1944-8"
    VALUE_1945_5 = "1945-5"
    VALUE_1946_3 = "1946-3"
    VALUE_1947_1 = "1947-1"
    VALUE_1948_9 = "1948-9"
    VALUE_1949_7 = "1949-7"
    VALUE_1950_5 = "1950-5"
    VALUE_1952_1 = "1952-1"
    VALUE_1953_9 = "1953-9"
    VALUE_1954_7 = "1954-7"
    VALUE_1963_8 = "1963-8"
    VALUE_1951_3 = "1951-3"
    VALUE_1955_4 = "1955-4"
    VALUE_1956_2 = "1956-2"
    VALUE_1957_0 = "1957-0"
    VALUE_1958_8 = "1958-8"
    VALUE_1959_6 = "1959-6"
    VALUE_1960_4 = "1960-4"
    VALUE_1961_2 = "1961-2"
    VALUE_1964_6 = "1964-6"
    VALUE_1840_8 = "1840-8"
    VALUE_1842_4 = "1842-4"


class RaceAlaskanNativeInupiatEskimo(Enum):
    """
    specDomain: S15571 (C-0-T14914-S14915-S15470-S15569-S15571-cpt)
    :cvar VALUE_1844_0:
    :cvar VALUE_1845_7:
    :cvar VALUE_1846_5:
    :cvar VALUE_1847_3:
    :cvar VALUE_1849_9:
    :cvar VALUE_1848_1:
    :cvar VALUE_1850_7:
    :cvar VALUE_1851_5:
    :cvar VALUE_1852_3:
    :cvar VALUE_1853_1:
    :cvar VALUE_1854_9:
    :cvar VALUE_1855_6:
    :cvar VALUE_1856_4:
    :cvar VALUE_1857_2:
    :cvar VALUE_1858_0:
    :cvar VALUE_1859_8:
    :cvar VALUE_1860_6:
    :cvar VALUE_1861_4:
    :cvar VALUE_1862_2:
    :cvar VALUE_1863_0:
    :cvar VALUE_1864_8:
    :cvar VALUE_1865_5:
    :cvar VALUE_1866_3:
    :cvar VALUE_1867_1:
    :cvar VALUE_1868_9:
    :cvar VALUE_1869_7:
    :cvar VALUE_1889_5:
    :cvar VALUE_1870_5:
    :cvar VALUE_1871_3:
    :cvar VALUE_1872_1:
    :cvar VALUE_1873_9:
    :cvar VALUE_1874_7:
    :cvar VALUE_1875_4:
    :cvar VALUE_1876_2:
    :cvar VALUE_1877_0:
    :cvar VALUE_1878_8:
    :cvar VALUE_1879_6:
    :cvar VALUE_1880_4:
    :cvar VALUE_1881_2:
    :cvar VALUE_1882_0:
    :cvar VALUE_1883_8:
    :cvar VALUE_1884_6:
    :cvar VALUE_1885_3:
    :cvar VALUE_1886_1:
    :cvar VALUE_1887_9:
    :cvar VALUE_1888_7:
    """
    VALUE_1844_0 = "1844-0"
    VALUE_1845_7 = "1845-7"
    VALUE_1846_5 = "1846-5"
    VALUE_1847_3 = "1847-3"
    VALUE_1849_9 = "1849-9"
    VALUE_1848_1 = "1848-1"
    VALUE_1850_7 = "1850-7"
    VALUE_1851_5 = "1851-5"
    VALUE_1852_3 = "1852-3"
    VALUE_1853_1 = "1853-1"
    VALUE_1854_9 = "1854-9"
    VALUE_1855_6 = "1855-6"
    VALUE_1856_4 = "1856-4"
    VALUE_1857_2 = "1857-2"
    VALUE_1858_0 = "1858-0"
    VALUE_1859_8 = "1859-8"
    VALUE_1860_6 = "1860-6"
    VALUE_1861_4 = "1861-4"
    VALUE_1862_2 = "1862-2"
    VALUE_1863_0 = "1863-0"
    VALUE_1864_8 = "1864-8"
    VALUE_1865_5 = "1865-5"
    VALUE_1866_3 = "1866-3"
    VALUE_1867_1 = "1867-1"
    VALUE_1868_9 = "1868-9"
    VALUE_1869_7 = "1869-7"
    VALUE_1889_5 = "1889-5"
    VALUE_1870_5 = "1870-5"
    VALUE_1871_3 = "1871-3"
    VALUE_1872_1 = "1872-1"
    VALUE_1873_9 = "1873-9"
    VALUE_1874_7 = "1874-7"
    VALUE_1875_4 = "1875-4"
    VALUE_1876_2 = "1876-2"
    VALUE_1877_0 = "1877-0"
    VALUE_1878_8 = "1878-8"
    VALUE_1879_6 = "1879-6"
    VALUE_1880_4 = "1880-4"
    VALUE_1881_2 = "1881-2"
    VALUE_1882_0 = "1882-0"
    VALUE_1883_8 = "1883-8"
    VALUE_1884_6 = "1884-6"
    VALUE_1885_3 = "1885-3"
    VALUE_1886_1 = "1886-1"
    VALUE_1887_9 = "1887-9"
    VALUE_1888_7 = "1888-7"


class RaceAlaskanNativeSiberianEskimo(Enum):
    """
    specDomain: S15617 (C-0-T14914-S14915-S15470-S15569-S15617-cpt)
    :cvar VALUE_1891_1:
    :cvar VALUE_1892_9:
    :cvar VALUE_1893_7:
    :cvar VALUE_1894_5:
    """
    VALUE_1891_1 = "1891-1"
    VALUE_1892_9 = "1892-9"
    VALUE_1893_7 = "1893-7"
    VALUE_1894_5 = "1894-5"


class RaceAlaskanNativeYupikEskimo(Enum):
    """
    specDomain: S15621 (C-0-T14914-S14915-S15470-S15569-S15621-cpt)
    :cvar VALUE_1896_0:
    :cvar VALUE_1897_8:
    :cvar VALUE_1898_6:
    :cvar VALUE_1899_4:
    :cvar VALUE_1900_0:
    :cvar VALUE_1901_8:
    :cvar VALUE_1902_6:
    :cvar VALUE_1903_4:
    :cvar VALUE_1904_2:
    :cvar VALUE_1905_9:
    :cvar VALUE_1906_7:
    :cvar VALUE_1907_5:
    :cvar VALUE_1908_3:
    :cvar VALUE_1909_1:
    :cvar VALUE_1910_9:
    :cvar VALUE_1911_7:
    :cvar VALUE_1912_5:
    :cvar VALUE_1913_3:
    :cvar VALUE_1914_1:
    :cvar VALUE_1915_8:
    :cvar VALUE_1916_6:
    :cvar VALUE_1917_4:
    :cvar VALUE_1962_0:
    :cvar VALUE_1918_2:
    :cvar VALUE_1919_0:
    :cvar VALUE_1920_8:
    :cvar VALUE_1921_6:
    :cvar VALUE_1922_4:
    :cvar VALUE_1923_2:
    :cvar VALUE_1924_0:
    :cvar VALUE_1925_7:
    :cvar VALUE_1926_5:
    :cvar VALUE_1927_3:
    :cvar VALUE_1928_1:
    :cvar VALUE_1929_9:
    :cvar VALUE_1930_7:
    :cvar VALUE_1931_5:
    :cvar VALUE_1932_3:
    :cvar VALUE_1933_1:
    :cvar VALUE_1934_9:
    :cvar VALUE_1935_6:
    :cvar VALUE_1937_2:
    :cvar VALUE_1938_0:
    :cvar VALUE_1936_4:
    :cvar VALUE_1940_6:
    :cvar VALUE_1939_8:
    :cvar VALUE_1941_4:
    :cvar VALUE_1942_2:
    :cvar VALUE_1943_0:
    :cvar VALUE_1944_8:
    :cvar VALUE_1945_5:
    :cvar VALUE_1946_3:
    :cvar VALUE_1947_1:
    :cvar VALUE_1948_9:
    :cvar VALUE_1949_7:
    :cvar VALUE_1950_5:
    :cvar VALUE_1952_1:
    :cvar VALUE_1953_9:
    :cvar VALUE_1954_7:
    :cvar VALUE_1963_8:
    :cvar VALUE_1951_3:
    :cvar VALUE_1955_4:
    :cvar VALUE_1956_2:
    :cvar VALUE_1957_0:
    :cvar VALUE_1958_8:
    :cvar VALUE_1959_6:
    :cvar VALUE_1960_4:
    :cvar VALUE_1961_2:
    :cvar VALUE_1964_6:
    """
    VALUE_1896_0 = "1896-0"
    VALUE_1897_8 = "1897-8"
    VALUE_1898_6 = "1898-6"
    VALUE_1899_4 = "1899-4"
    VALUE_1900_0 = "1900-0"
    VALUE_1901_8 = "1901-8"
    VALUE_1902_6 = "1902-6"
    VALUE_1903_4 = "1903-4"
    VALUE_1904_2 = "1904-2"
    VALUE_1905_9 = "1905-9"
    VALUE_1906_7 = "1906-7"
    VALUE_1907_5 = "1907-5"
    VALUE_1908_3 = "1908-3"
    VALUE_1909_1 = "1909-1"
    VALUE_1910_9 = "1910-9"
    VALUE_1911_7 = "1911-7"
    VALUE_1912_5 = "1912-5"
    VALUE_1913_3 = "1913-3"
    VALUE_1914_1 = "1914-1"
    VALUE_1915_8 = "1915-8"
    VALUE_1916_6 = "1916-6"
    VALUE_1917_4 = "1917-4"
    VALUE_1962_0 = "1962-0"
    VALUE_1918_2 = "1918-2"
    VALUE_1919_0 = "1919-0"
    VALUE_1920_8 = "1920-8"
    VALUE_1921_6 = "1921-6"
    VALUE_1922_4 = "1922-4"
    VALUE_1923_2 = "1923-2"
    VALUE_1924_0 = "1924-0"
    VALUE_1925_7 = "1925-7"
    VALUE_1926_5 = "1926-5"
    VALUE_1927_3 = "1927-3"
    VALUE_1928_1 = "1928-1"
    VALUE_1929_9 = "1929-9"
    VALUE_1930_7 = "1930-7"
    VALUE_1931_5 = "1931-5"
    VALUE_1932_3 = "1932-3"
    VALUE_1933_1 = "1933-1"
    VALUE_1934_9 = "1934-9"
    VALUE_1935_6 = "1935-6"
    VALUE_1937_2 = "1937-2"
    VALUE_1938_0 = "1938-0"
    VALUE_1936_4 = "1936-4"
    VALUE_1940_6 = "1940-6"
    VALUE_1939_8 = "1939-8"
    VALUE_1941_4 = "1941-4"
    VALUE_1942_2 = "1942-2"
    VALUE_1943_0 = "1943-0"
    VALUE_1944_8 = "1944-8"
    VALUE_1945_5 = "1945-5"
    VALUE_1946_3 = "1946-3"
    VALUE_1947_1 = "1947-1"
    VALUE_1948_9 = "1948-9"
    VALUE_1949_7 = "1949-7"
    VALUE_1950_5 = "1950-5"
    VALUE_1952_1 = "1952-1"
    VALUE_1953_9 = "1953-9"
    VALUE_1954_7 = "1954-7"
    VALUE_1963_8 = "1963-8"
    VALUE_1951_3 = "1951-3"
    VALUE_1955_4 = "1955-4"
    VALUE_1956_2 = "1956-2"
    VALUE_1957_0 = "1957-0"
    VALUE_1958_8 = "1958-8"
    VALUE_1959_6 = "1959-6"
    VALUE_1960_4 = "1960-4"
    VALUE_1961_2 = "1961-2"
    VALUE_1964_6 = "1964-6"


class RaceAmericanIndian(Enum):
    """
    specDomain: S14916 (C-0-T14914-S14915-S14916-cpt)
    :cvar VALUE_1076_9:
    :cvar VALUE_1744_2:
    :cvar VALUE_1741_8:
    :cvar VALUE_1742_6:
    :cvar VALUE_1743_4:
    :cvar VALUE_1745_9:
    :cvar VALUE_1746_7:
    :cvar VALUE_1747_5:
    :cvar VALUE_1748_3:
    :cvar VALUE_1749_1:
    :cvar VALUE_1750_9:
    :cvar VALUE_1751_7:
    :cvar VALUE_1752_5:
    :cvar VALUE_1753_3:
    :cvar VALUE_1754_1:
    :cvar VALUE_1755_8:
    :cvar VALUE_1756_6:
    :cvar VALUE_1757_4:
    :cvar VALUE_1758_2:
    :cvar VALUE_1759_0:
    :cvar VALUE_1760_8:
    :cvar VALUE_1761_6:
    :cvar VALUE_1762_4:
    :cvar VALUE_1763_2:
    :cvar VALUE_1764_0:
    :cvar VALUE_1765_7:
    :cvar VALUE_1766_5:
    :cvar VALUE_1767_3:
    :cvar VALUE_1768_1:
    :cvar VALUE_1769_9:
    :cvar VALUE_1770_7:
    :cvar VALUE_1771_5:
    :cvar VALUE_1772_3:
    :cvar VALUE_1773_1:
    :cvar VALUE_1774_9:
    :cvar VALUE_1775_6:
    :cvar VALUE_1776_4:
    :cvar VALUE_1777_2:
    :cvar VALUE_1778_0:
    :cvar VALUE_1780_6:
    :cvar VALUE_1779_8:
    :cvar VALUE_1781_4:
    :cvar VALUE_1782_2:
    :cvar VALUE_1783_0:
    :cvar VALUE_1784_8:
    :cvar VALUE_1785_5:
    :cvar VALUE_1786_3:
    :cvar VALUE_1787_1:
    :cvar VALUE_1788_9:
    :cvar VALUE_1789_7:
    :cvar VALUE_1790_5:
    :cvar VALUE_1791_3:
    :cvar VALUE_1792_1:
    :cvar VALUE_1793_9:
    :cvar VALUE_1795_4:
    :cvar VALUE_1794_7:
    :cvar VALUE_1796_2:
    :cvar VALUE_1797_0:
    :cvar VALUE_1798_8:
    :cvar VALUE_1799_6:
    :cvar VALUE_1800_2:
    :cvar VALUE_1801_0:
    :cvar VALUE_1802_8:
    :cvar VALUE_1803_6:
    :cvar VALUE_1804_4:
    :cvar VALUE_1805_1:
    :cvar VALUE_1806_9:
    :cvar VALUE_1807_7:
    :cvar VALUE_1808_5:
    :cvar VALUE_1809_3:
    :cvar VALUE_1010_8:
    :cvar VALUE_1011_6:
    :cvar VALUE_1012_4:
    :cvar VALUE_1013_2:
    :cvar VALUE_1014_0:
    :cvar VALUE_1015_7:
    :cvar VALUE_1016_5:
    :cvar VALUE_1017_3:
    :cvar VALUE_1018_1:
    :cvar VALUE_1019_9:
    :cvar VALUE_1021_5:
    :cvar VALUE_1022_3:
    :cvar VALUE_1023_1:
    :cvar VALUE_1024_9:
    :cvar VALUE_1030_6:
    :cvar VALUE_1031_4:
    :cvar VALUE_1041_3:
    :cvar VALUE_1042_1:
    :cvar VALUE_1044_7:
    :cvar VALUE_1045_4:
    :cvar VALUE_1046_2:
    :cvar VALUE_1047_0:
    :cvar VALUE_1048_8:
    :cvar VALUE_1049_6:
    :cvar VALUE_1050_4:
    :cvar VALUE_1051_2:
    :cvar VALUE_1053_8:
    :cvar VALUE_1054_6:
    :cvar VALUE_1055_3:
    :cvar VALUE_1056_1:
    :cvar VALUE_1057_9:
    :cvar VALUE_1058_7:
    :cvar VALUE_1059_5:
    :cvar VALUE_1060_3:
    :cvar VALUE_1061_1:
    :cvar VALUE_1062_9:
    :cvar VALUE_1063_7:
    :cvar VALUE_1064_5:
    :cvar VALUE_1065_2:
    :cvar VALUE_1066_0:
    :cvar VALUE_1082_7:
    :cvar VALUE_1083_5:
    :cvar VALUE_1084_3:
    :cvar VALUE_1088_4:
    :cvar VALUE_1089_2:
    :cvar VALUE_1090_0:
    :cvar VALUE_1091_8:
    :cvar VALUE_1092_6:
    :cvar VALUE_1093_4:
    :cvar VALUE_1094_2:
    :cvar VALUE_1095_9:
    :cvar VALUE_1096_7:
    :cvar VALUE_1097_5:
    :cvar VALUE_1098_3:
    :cvar VALUE_1102_3:
    :cvar VALUE_1103_1:
    :cvar VALUE_1104_9:
    :cvar VALUE_1108_0:
    :cvar VALUE_1109_8:
    :cvar VALUE_1110_6:
    :cvar VALUE_1114_8:
    :cvar VALUE_1115_5:
    :cvar VALUE_1116_3:
    :cvar VALUE_1117_1:
    :cvar VALUE_1118_9:
    :cvar VALUE_1119_7:
    :cvar VALUE_1120_5:
    :cvar VALUE_1121_3:
    :cvar VALUE_1123_9:
    :cvar VALUE_1124_7:
    :cvar VALUE_1125_4:
    :cvar VALUE_1126_2:
    :cvar VALUE_1127_0:
    :cvar VALUE_1128_8:
    :cvar VALUE_1129_6:
    :cvar VALUE_1130_4:
    :cvar VALUE_1131_2:
    :cvar VALUE_1132_0:
    :cvar VALUE_1134_6:
    :cvar VALUE_1133_8:
    :cvar VALUE_1135_3:
    :cvar VALUE_1136_1:
    :cvar VALUE_1137_9:
    :cvar VALUE_1138_7:
    :cvar VALUE_1139_5:
    :cvar VALUE_1140_3:
    :cvar VALUE_1141_1:
    :cvar VALUE_1142_9:
    :cvar VALUE_1143_7:
    :cvar VALUE_1145_2:
    :cvar VALUE_1146_0:
    :cvar VALUE_1144_5:
    :cvar VALUE_1147_8:
    :cvar VALUE_1148_6:
    :cvar VALUE_1150_2:
    :cvar VALUE_1151_0:
    :cvar VALUE_1155_1:
    :cvar VALUE_1156_9:
    :cvar VALUE_1157_7:
    :cvar VALUE_1158_5:
    :cvar VALUE_1159_3:
    :cvar VALUE_1160_1:
    :cvar VALUE_1162_7:
    :cvar VALUE_1163_5:
    :cvar VALUE_1175_9:
    :cvar VALUE_1176_7:
    :cvar VALUE_1186_6:
    :cvar VALUE_1187_4:
    :cvar VALUE_1193_2:
    :cvar VALUE_1194_0:
    :cvar VALUE_1195_7:
    :cvar VALUE_1196_5:
    :cvar VALUE_1197_3:
    :cvar VALUE_1198_1:
    :cvar VALUE_1199_9:
    :cvar VALUE_1200_5:
    :cvar VALUE_1201_3:
    :cvar VALUE_1202_1:
    :cvar VALUE_1203_9:
    :cvar VALUE_1204_7:
    :cvar VALUE_1205_4:
    :cvar VALUE_1211_2:
    :cvar VALUE_1212_0:
    :cvar VALUE_1214_6:
    :cvar VALUE_1215_3:
    :cvar VALUE_1216_1:
    :cvar VALUE_1217_9:
    :cvar VALUE_1218_7:
    :cvar VALUE_1219_5:
    :cvar VALUE_1220_3:
    :cvar VALUE_1222_9:
    :cvar VALUE_1223_7:
    :cvar VALUE_1224_5:
    :cvar VALUE_1225_2:
    :cvar VALUE_1226_0:
    :cvar VALUE_1227_8:
    :cvar VALUE_1228_6:
    :cvar VALUE_1229_4:
    :cvar VALUE_1230_2:
    :cvar VALUE_1231_0:
    :cvar VALUE_1233_6:
    :cvar VALUE_1234_4:
    :cvar VALUE_1235_1:
    :cvar VALUE_1236_9:
    :cvar VALUE_1237_7:
    :cvar VALUE_1238_5:
    :cvar VALUE_1239_3:
    :cvar VALUE_1240_1:
    :cvar VALUE_1241_9:
    :cvar VALUE_1242_7:
    :cvar VALUE_1243_5:
    :cvar VALUE_1244_3:
    :cvar VALUE_1245_0:
    :cvar VALUE_1246_8:
    :cvar VALUE_1247_6:
    :cvar VALUE_1248_4:
    :cvar VALUE_1264_1:
    :cvar VALUE_1265_8:
    :cvar VALUE_1271_6:
    :cvar VALUE_1272_4:
    :cvar VALUE_1273_2:
    :cvar VALUE_1281_5:
    :cvar VALUE_1282_3:
    :cvar VALUE_1283_1:
    :cvar VALUE_1285_6:
    :cvar VALUE_1286_4:
    :cvar VALUE_1287_2:
    :cvar VALUE_1288_0:
    :cvar VALUE_1289_8:
    :cvar VALUE_1290_6:
    :cvar VALUE_1291_4:
    :cvar VALUE_1292_2:
    :cvar VALUE_1293_0:
    :cvar VALUE_1294_8:
    :cvar VALUE_1295_5:
    :cvar VALUE_1305_2:
    :cvar VALUE_1306_0:
    :cvar VALUE_1307_8:
    :cvar VALUE_1309_4:
    :cvar VALUE_1310_2:
    :cvar VALUE_1312_8:
    :cvar VALUE_1313_6:
    :cvar VALUE_1314_4:
    :cvar VALUE_1315_1:
    :cvar VALUE_1325_0:
    :cvar VALUE_1326_8:
    :cvar VALUE_1327_6:
    :cvar VALUE_1328_4:
    :cvar VALUE_1329_2:
    :cvar VALUE_1331_8:
    :cvar VALUE_1332_6:
    :cvar VALUE_1333_4:
    :cvar VALUE_1334_2:
    :cvar VALUE_1335_9:
    :cvar VALUE_1336_7:
    :cvar VALUE_1338_3:
    :cvar VALUE_1337_5:
    :cvar VALUE_1344_1:
    :cvar VALUE_1345_8:
    :cvar VALUE_1346_6:
    :cvar VALUE_1358_1:
    :cvar VALUE_1359_9:
    :cvar VALUE_1360_7:
    :cvar VALUE_1361_5:
    :cvar VALUE_1365_6:
    :cvar VALUE_1366_4:
    :cvar VALUE_1382_1:
    :cvar VALUE_1383_9:
    :cvar VALUE_1384_7:
    :cvar VALUE_1385_4:
    :cvar VALUE_1391_2:
    :cvar VALUE_1392_0:
    :cvar VALUE_1393_8:
    :cvar VALUE_1394_6:
    :cvar VALUE_1395_3:
    :cvar VALUE_1396_1:
    :cvar VALUE_1397_9:
    :cvar VALUE_1398_7:
    :cvar VALUE_1399_5:
    :cvar VALUE_1400_1:
    :cvar VALUE_1401_9:
    :cvar VALUE_1411_8:
    :cvar VALUE_1412_6:
    :cvar VALUE_1413_4:
    :cvar VALUE_1414_2:
    :cvar VALUE_1416_7:
    :cvar VALUE_1417_5:
    :cvar VALUE_1418_3:
    :cvar VALUE_1419_1:
    :cvar VALUE_1420_9:
    :cvar VALUE_1421_7:
    :cvar VALUE_1422_5:
    :cvar VALUE_1423_3:
    :cvar VALUE_1424_1:
    :cvar VALUE_1425_8:
    :cvar VALUE_1426_6:
    :cvar VALUE_1427_4:
    :cvar VALUE_1428_2:
    :cvar VALUE_1429_0:
    :cvar VALUE_1430_8:
    :cvar VALUE_1431_6:
    :cvar VALUE_1432_4:
    :cvar VALUE_1433_2:
    :cvar VALUE_1434_0:
    :cvar VALUE_1435_7:
    :cvar VALUE_1436_5:
    :cvar VALUE_1437_3:
    :cvar VALUE_1441_5:
    :cvar VALUE_1442_3:
    :cvar VALUE_1443_1:
    :cvar VALUE_1445_6:
    :cvar VALUE_1446_4:
    :cvar VALUE_1450_6:
    :cvar VALUE_1451_4:
    :cvar VALUE_1453_0:
    :cvar VALUE_1454_8:
    :cvar VALUE_1456_3:
    :cvar VALUE_1457_1:
    :cvar VALUE_1458_9:
    :cvar VALUE_1464_7:
    :cvar VALUE_1465_4:
    :cvar VALUE_1466_2:
    :cvar VALUE_1467_0:
    :cvar VALUE_1468_8:
    :cvar VALUE_1469_6:
    :cvar VALUE_1470_4:
    :cvar VALUE_1471_2:
    :cvar VALUE_1472_0:
    :cvar VALUE_1474_6:
    :cvar VALUE_1475_3:
    :cvar VALUE_1476_1:
    :cvar VALUE_1478_7:
    :cvar VALUE_1479_5:
    :cvar VALUE_1480_3:
    :cvar VALUE_1481_1:
    :cvar VALUE_1482_9:
    :cvar VALUE_1483_7:
    :cvar VALUE_1484_5:
    :cvar VALUE_1485_2:
    :cvar VALUE_1489_4:
    :cvar VALUE_1490_2:
    :cvar VALUE_1491_0:
    :cvar VALUE_1492_8:
    :cvar VALUE_1493_6:
    :cvar VALUE_1494_4:
    :cvar VALUE_1495_1:
    :cvar VALUE_1496_9:
    :cvar VALUE_1497_7:
    :cvar VALUE_1498_5:
    :cvar VALUE_1499_3:
    :cvar VALUE_1500_8:
    :cvar VALUE_1501_6:
    :cvar VALUE_1502_4:
    :cvar VALUE_1503_2:
    :cvar VALUE_1506_5:
    :cvar VALUE_1505_7:
    :cvar VALUE_1504_0:
    :cvar VALUE_1507_3:
    :cvar VALUE_1508_1:
    :cvar VALUE_1509_9:
    :cvar VALUE_1510_7:
    :cvar VALUE_1511_5:
    :cvar VALUE_1512_3:
    :cvar VALUE_1513_1:
    :cvar VALUE_1514_9:
    :cvar VALUE_1515_6:
    :cvar VALUE_1516_4:
    :cvar VALUE_1518_0:
    :cvar VALUE_1519_8:
    :cvar VALUE_1520_6:
    :cvar VALUE_1521_4:
    :cvar VALUE_1522_2:
    :cvar VALUE_1523_0:
    :cvar VALUE_1524_8:
    :cvar VALUE_1525_5:
    :cvar VALUE_1526_3:
    :cvar VALUE_1527_1:
    :cvar VALUE_1528_9:
    :cvar VALUE_1529_7:
    :cvar VALUE_1530_5:
    :cvar VALUE_1531_3:
    :cvar VALUE_1532_1:
    :cvar VALUE_1533_9:
    :cvar VALUE_1534_7:
    :cvar VALUE_1535_4:
    :cvar VALUE_1536_2:
    :cvar VALUE_1537_0:
    :cvar VALUE_1538_8:
    :cvar VALUE_1539_6:
    :cvar VALUE_1551_1:
    :cvar VALUE_1552_9:
    :cvar VALUE_1553_7:
    :cvar VALUE_1554_5:
    :cvar VALUE_1566_9:
    :cvar VALUE_1567_7:
    :cvar VALUE_1568_5:
    :cvar VALUE_1569_3:
    :cvar VALUE_1570_1:
    :cvar VALUE_1571_9:
    :cvar VALUE_1573_5:
    :cvar VALUE_1574_3:
    :cvar VALUE_1578_4:
    :cvar VALUE_1579_2:
    :cvar VALUE_1580_0:
    :cvar VALUE_1586_7:
    :cvar VALUE_1587_5:
    :cvar VALUE_1588_3:
    :cvar VALUE_1589_1:
    :cvar VALUE_1590_9:
    :cvar VALUE_1591_7:
    :cvar VALUE_1592_5:
    :cvar VALUE_1593_3:
    :cvar VALUE_1594_1:
    :cvar VALUE_1595_8:
    :cvar VALUE_1596_6:
    :cvar VALUE_1597_4:
    :cvar VALUE_1598_2:
    :cvar VALUE_1599_0:
    :cvar VALUE_1600_6:
    :cvar VALUE_1602_2:
    :cvar VALUE_1603_0:
    :cvar VALUE_1604_8:
    :cvar VALUE_1605_5:
    :cvar VALUE_1609_7:
    :cvar VALUE_1610_5:
    :cvar VALUE_1611_3:
    :cvar VALUE_1612_1:
    :cvar VALUE_1613_9:
    :cvar VALUE_1614_7:
    :cvar VALUE_1615_4:
    :cvar VALUE_1616_2:
    :cvar VALUE_1617_0:
    :cvar VALUE_1618_8:
    :cvar VALUE_1619_6:
    :cvar VALUE_1620_4:
    :cvar VALUE_1621_2:
    :cvar VALUE_1622_0:
    :cvar VALUE_1623_8:
    :cvar VALUE_1624_6:
    :cvar VALUE_1625_3:
    :cvar VALUE_1626_1:
    :cvar VALUE_1627_9:
    :cvar VALUE_1628_7:
    :cvar VALUE_1629_5:
    :cvar VALUE_1631_1:
    :cvar VALUE_1630_3:
    :cvar VALUE_1632_9:
    :cvar VALUE_1633_7:
    :cvar VALUE_1634_5:
    :cvar VALUE_1635_2:
    :cvar VALUE_1636_0:
    :cvar VALUE_1637_8:
    :cvar VALUE_1638_6:
    :cvar VALUE_1639_4:
    :cvar VALUE_1640_2:
    :cvar VALUE_1641_0:
    :cvar VALUE_1653_5:
    :cvar VALUE_1654_3:
    :cvar VALUE_1655_0:
    :cvar VALUE_1656_8:
    :cvar VALUE_1657_6:
    :cvar VALUE_1667_5:
    :cvar VALUE_1668_3:
    :cvar VALUE_1670_9:
    :cvar VALUE_1671_7:
    :cvar VALUE_1672_5:
    :cvar VALUE_1673_3:
    :cvar VALUE_1679_0:
    :cvar VALUE_1680_8:
    :cvar VALUE_1681_6:
    :cvar VALUE_1687_3:
    :cvar VALUE_1688_1:
    :cvar VALUE_1689_9:
    :cvar VALUE_1690_7:
    :cvar VALUE_1696_4:
    :cvar VALUE_1697_2:
    :cvar VALUE_1698_0:
    :cvar VALUE_1724_4:
    :cvar VALUE_1725_1:
    :cvar VALUE_1726_9:
    :cvar VALUE_1727_7:
    :cvar VALUE_1728_5:
    :cvar VALUE_1729_3:
    :cvar VALUE_1730_1:
    :cvar VALUE_1731_9:
    :cvar VALUE_1732_7:
    :cvar VALUE_1733_5:
    :cvar VALUE_1068_6:
    :cvar VALUE_1069_4:
    :cvar VALUE_1070_2:
    :cvar VALUE_1071_0:
    :cvar VALUE_1072_8:
    :cvar VALUE_1073_6:
    :cvar VALUE_1704_6:
    :cvar VALUE_1705_3:
    :cvar VALUE_1711_1:
    :cvar VALUE_1712_9:
    :cvar VALUE_1713_7:
    :cvar VALUE_1717_8:
    :cvar VALUE_1718_6:
    :cvar VALUE_1719_4:
    :cvar VALUE_1720_2:
    :cvar VALUE_1004_1:
    :cvar VALUE_1006_6:
    :cvar VALUE_1008_2:
    :cvar VALUE_1026_4:
    :cvar VALUE_1028_0:
    :cvar VALUE_1033_0:
    :cvar VALUE_1035_5:
    :cvar VALUE_1037_1:
    :cvar VALUE_1039_7:
    :cvar VALUE_1078_5:
    :cvar VALUE_1080_1:
    :cvar VALUE_1086_8:
    :cvar VALUE_1100_7:
    :cvar VALUE_1106_4:
    :cvar VALUE_1112_2:
    :cvar VALUE_1153_6:
    :cvar VALUE_1165_0:
    :cvar VALUE_1167_6:
    :cvar VALUE_1169_2:
    :cvar VALUE_1171_8:
    :cvar VALUE_1173_4:
    :cvar VALUE_1180_9:
    :cvar VALUE_1178_3:
    :cvar VALUE_1182_5:
    :cvar VALUE_1184_1:
    :cvar VALUE_1189_0:
    :cvar VALUE_1191_6:
    :cvar VALUE_1207_0:
    :cvar VALUE_1209_6:
    :cvar VALUE_1250_0:
    :cvar VALUE_1252_6:
    :cvar VALUE_1254_2:
    :cvar VALUE_1258_3:
    :cvar VALUE_1256_7:
    :cvar VALUE_1260_9:
    :cvar VALUE_1262_5:
    :cvar VALUE_1267_4:
    :cvar VALUE_1269_0:
    :cvar VALUE_1275_7:
    :cvar VALUE_1277_3:
    :cvar VALUE_1279_9:
    :cvar VALUE_1297_1:
    :cvar VALUE_1299_7:
    :cvar VALUE_1301_1:
    :cvar VALUE_1303_7:
    :cvar VALUE_1317_7:
    :cvar VALUE_1319_3:
    :cvar VALUE_1321_9:
    :cvar VALUE_1323_5:
    :cvar VALUE_1340_9:
    :cvar VALUE_1342_5:
    :cvar VALUE_1348_2:
    :cvar VALUE_1350_8:
    :cvar VALUE_1352_4:
    :cvar VALUE_1354_0:
    :cvar VALUE_1356_5:
    :cvar VALUE_1363_1:
    :cvar VALUE_1368_0:
    :cvar VALUE_1370_6:
    :cvar VALUE_1372_2:
    :cvar VALUE_1374_8:
    :cvar VALUE_1376_3:
    :cvar VALUE_1378_9:
    :cvar VALUE_1380_5:
    :cvar VALUE_1387_0:
    :cvar VALUE_1389_6:
    :cvar VALUE_1403_5:
    :cvar VALUE_1405_0:
    :cvar VALUE_1407_6:
    :cvar VALUE_1409_2:
    :cvar VALUE_1439_9:
    :cvar VALUE_1448_0:
    :cvar VALUE_1460_5:
    :cvar VALUE_1462_1:
    :cvar VALUE_1487_8:
    :cvar VALUE_1541_2:
    :cvar VALUE_1543_8:
    :cvar VALUE_1545_3:
    :cvar VALUE_1547_9:
    :cvar VALUE_1549_5:
    :cvar VALUE_1556_0:
    :cvar VALUE_1558_6:
    :cvar VALUE_1560_2:
    :cvar VALUE_1562_8:
    :cvar VALUE_1564_4:
    :cvar VALUE_1576_8:
    :cvar VALUE_1582_6:
    :cvar VALUE_1584_2:
    :cvar VALUE_1607_1:
    :cvar VALUE_1643_6:
    :cvar VALUE_1074_4:
    :cvar VALUE_1645_1:
    :cvar VALUE_1647_7:
    :cvar VALUE_1649_3:
    :cvar VALUE_1651_9:
    :cvar VALUE_1659_2:
    :cvar VALUE_1661_8:
    :cvar VALUE_1663_4:
    :cvar VALUE_1665_9:
    :cvar VALUE_1675_8:
    :cvar VALUE_1677_4:
    :cvar VALUE_1683_2:
    :cvar VALUE_1685_7:
    :cvar VALUE_1692_3:
    :cvar VALUE_1694_9:
    :cvar VALUE_1700_4:
    :cvar VALUE_1702_0:
    :cvar VALUE_1707_9:
    :cvar VALUE_1709_5:
    :cvar VALUE_1715_2:
    :cvar VALUE_1722_8:
    """
    VALUE_1076_9 = "1076-9"
    VALUE_1744_2 = "1744-2"
    VALUE_1741_8 = "1741-8"
    VALUE_1742_6 = "1742-6"
    VALUE_1743_4 = "1743-4"
    VALUE_1745_9 = "1745-9"
    VALUE_1746_7 = "1746-7"
    VALUE_1747_5 = "1747-5"
    VALUE_1748_3 = "1748-3"
    VALUE_1749_1 = "1749-1"
    VALUE_1750_9 = "1750-9"
    VALUE_1751_7 = "1751-7"
    VALUE_1752_5 = "1752-5"
    VALUE_1753_3 = "1753-3"
    VALUE_1754_1 = "1754-1"
    VALUE_1755_8 = "1755-8"
    VALUE_1756_6 = "1756-6"
    VALUE_1757_4 = "1757-4"
    VALUE_1758_2 = "1758-2"
    VALUE_1759_0 = "1759-0"
    VALUE_1760_8 = "1760-8"
    VALUE_1761_6 = "1761-6"
    VALUE_1762_4 = "1762-4"
    VALUE_1763_2 = "1763-2"
    VALUE_1764_0 = "1764-0"
    VALUE_1765_7 = "1765-7"
    VALUE_1766_5 = "1766-5"
    VALUE_1767_3 = "1767-3"
    VALUE_1768_1 = "1768-1"
    VALUE_1769_9 = "1769-9"
    VALUE_1770_7 = "1770-7"
    VALUE_1771_5 = "1771-5"
    VALUE_1772_3 = "1772-3"
    VALUE_1773_1 = "1773-1"
    VALUE_1774_9 = "1774-9"
    VALUE_1775_6 = "1775-6"
    VALUE_1776_4 = "1776-4"
    VALUE_1777_2 = "1777-2"
    VALUE_1778_0 = "1778-0"
    VALUE_1780_6 = "1780-6"
    VALUE_1779_8 = "1779-8"
    VALUE_1781_4 = "1781-4"
    VALUE_1782_2 = "1782-2"
    VALUE_1783_0 = "1783-0"
    VALUE_1784_8 = "1784-8"
    VALUE_1785_5 = "1785-5"
    VALUE_1786_3 = "1786-3"
    VALUE_1787_1 = "1787-1"
    VALUE_1788_9 = "1788-9"
    VALUE_1789_7 = "1789-7"
    VALUE_1790_5 = "1790-5"
    VALUE_1791_3 = "1791-3"
    VALUE_1792_1 = "1792-1"
    VALUE_1793_9 = "1793-9"
    VALUE_1795_4 = "1795-4"
    VALUE_1794_7 = "1794-7"
    VALUE_1796_2 = "1796-2"
    VALUE_1797_0 = "1797-0"
    VALUE_1798_8 = "1798-8"
    VALUE_1799_6 = "1799-6"
    VALUE_1800_2 = "1800-2"
    VALUE_1801_0 = "1801-0"
    VALUE_1802_8 = "1802-8"
    VALUE_1803_6 = "1803-6"
    VALUE_1804_4 = "1804-4"
    VALUE_1805_1 = "1805-1"
    VALUE_1806_9 = "1806-9"
    VALUE_1807_7 = "1807-7"
    VALUE_1808_5 = "1808-5"
    VALUE_1809_3 = "1809-3"
    VALUE_1010_8 = "1010-8"
    VALUE_1011_6 = "1011-6"
    VALUE_1012_4 = "1012-4"
    VALUE_1013_2 = "1013-2"
    VALUE_1014_0 = "1014-0"
    VALUE_1015_7 = "1015-7"
    VALUE_1016_5 = "1016-5"
    VALUE_1017_3 = "1017-3"
    VALUE_1018_1 = "1018-1"
    VALUE_1019_9 = "1019-9"
    VALUE_1021_5 = "1021-5"
    VALUE_1022_3 = "1022-3"
    VALUE_1023_1 = "1023-1"
    VALUE_1024_9 = "1024-9"
    VALUE_1030_6 = "1030-6"
    VALUE_1031_4 = "1031-4"
    VALUE_1041_3 = "1041-3"
    VALUE_1042_1 = "1042-1"
    VALUE_1044_7 = "1044-7"
    VALUE_1045_4 = "1045-4"
    VALUE_1046_2 = "1046-2"
    VALUE_1047_0 = "1047-0"
    VALUE_1048_8 = "1048-8"
    VALUE_1049_6 = "1049-6"
    VALUE_1050_4 = "1050-4"
    VALUE_1051_2 = "1051-2"
    VALUE_1053_8 = "1053-8"
    VALUE_1054_6 = "1054-6"
    VALUE_1055_3 = "1055-3"
    VALUE_1056_1 = "1056-1"
    VALUE_1057_9 = "1057-9"
    VALUE_1058_7 = "1058-7"
    VALUE_1059_5 = "1059-5"
    VALUE_1060_3 = "1060-3"
    VALUE_1061_1 = "1061-1"
    VALUE_1062_9 = "1062-9"
    VALUE_1063_7 = "1063-7"
    VALUE_1064_5 = "1064-5"
    VALUE_1065_2 = "1065-2"
    VALUE_1066_0 = "1066-0"
    VALUE_1082_7 = "1082-7"
    VALUE_1083_5 = "1083-5"
    VALUE_1084_3 = "1084-3"
    VALUE_1088_4 = "1088-4"
    VALUE_1089_2 = "1089-2"
    VALUE_1090_0 = "1090-0"
    VALUE_1091_8 = "1091-8"
    VALUE_1092_6 = "1092-6"
    VALUE_1093_4 = "1093-4"
    VALUE_1094_2 = "1094-2"
    VALUE_1095_9 = "1095-9"
    VALUE_1096_7 = "1096-7"
    VALUE_1097_5 = "1097-5"
    VALUE_1098_3 = "1098-3"
    VALUE_1102_3 = "1102-3"
    VALUE_1103_1 = "1103-1"
    VALUE_1104_9 = "1104-9"
    VALUE_1108_0 = "1108-0"
    VALUE_1109_8 = "1109-8"
    VALUE_1110_6 = "1110-6"
    VALUE_1114_8 = "1114-8"
    VALUE_1115_5 = "1115-5"
    VALUE_1116_3 = "1116-3"
    VALUE_1117_1 = "1117-1"
    VALUE_1118_9 = "1118-9"
    VALUE_1119_7 = "1119-7"
    VALUE_1120_5 = "1120-5"
    VALUE_1121_3 = "1121-3"
    VALUE_1123_9 = "1123-9"
    VALUE_1124_7 = "1124-7"
    VALUE_1125_4 = "1125-4"
    VALUE_1126_2 = "1126-2"
    VALUE_1127_0 = "1127-0"
    VALUE_1128_8 = "1128-8"
    VALUE_1129_6 = "1129-6"
    VALUE_1130_4 = "1130-4"
    VALUE_1131_2 = "1131-2"
    VALUE_1132_0 = "1132-0"
    VALUE_1134_6 = "1134-6"
    VALUE_1133_8 = "1133-8"
    VALUE_1135_3 = "1135-3"
    VALUE_1136_1 = "1136-1"
    VALUE_1137_9 = "1137-9"
    VALUE_1138_7 = "1138-7"
    VALUE_1139_5 = "1139-5"
    VALUE_1140_3 = "1140-3"
    VALUE_1141_1 = "1141-1"
    VALUE_1142_9 = "1142-9"
    VALUE_1143_7 = "1143-7"
    VALUE_1145_2 = "1145-2"
    VALUE_1146_0 = "1146-0"
    VALUE_1144_5 = "1144-5"
    VALUE_1147_8 = "1147-8"
    VALUE_1148_6 = "1148-6"
    VALUE_1150_2 = "1150-2"
    VALUE_1151_0 = "1151-0"
    VALUE_1155_1 = "1155-1"
    VALUE_1156_9 = "1156-9"
    VALUE_1157_7 = "1157-7"
    VALUE_1158_5 = "1158-5"
    VALUE_1159_3 = "1159-3"
    VALUE_1160_1 = "1160-1"
    VALUE_1162_7 = "1162-7"
    VALUE_1163_5 = "1163-5"
    VALUE_1175_9 = "1175-9"
    VALUE_1176_7 = "1176-7"
    VALUE_1186_6 = "1186-6"
    VALUE_1187_4 = "1187-4"
    VALUE_1193_2 = "1193-2"
    VALUE_1194_0 = "1194-0"
    VALUE_1195_7 = "1195-7"
    VALUE_1196_5 = "1196-5"
    VALUE_1197_3 = "1197-3"
    VALUE_1198_1 = "1198-1"
    VALUE_1199_9 = "1199-9"
    VALUE_1200_5 = "1200-5"
    VALUE_1201_3 = "1201-3"
    VALUE_1202_1 = "1202-1"
    VALUE_1203_9 = "1203-9"
    VALUE_1204_7 = "1204-7"
    VALUE_1205_4 = "1205-4"
    VALUE_1211_2 = "1211-2"
    VALUE_1212_0 = "1212-0"
    VALUE_1214_6 = "1214-6"
    VALUE_1215_3 = "1215-3"
    VALUE_1216_1 = "1216-1"
    VALUE_1217_9 = "1217-9"
    VALUE_1218_7 = "1218-7"
    VALUE_1219_5 = "1219-5"
    VALUE_1220_3 = "1220-3"
    VALUE_1222_9 = "1222-9"
    VALUE_1223_7 = "1223-7"
    VALUE_1224_5 = "1224-5"
    VALUE_1225_2 = "1225-2"
    VALUE_1226_0 = "1226-0"
    VALUE_1227_8 = "1227-8"
    VALUE_1228_6 = "1228-6"
    VALUE_1229_4 = "1229-4"
    VALUE_1230_2 = "1230-2"
    VALUE_1231_0 = "1231-0"
    VALUE_1233_6 = "1233-6"
    VALUE_1234_4 = "1234-4"
    VALUE_1235_1 = "1235-1"
    VALUE_1236_9 = "1236-9"
    VALUE_1237_7 = "1237-7"
    VALUE_1238_5 = "1238-5"
    VALUE_1239_3 = "1239-3"
    VALUE_1240_1 = "1240-1"
    VALUE_1241_9 = "1241-9"
    VALUE_1242_7 = "1242-7"
    VALUE_1243_5 = "1243-5"
    VALUE_1244_3 = "1244-3"
    VALUE_1245_0 = "1245-0"
    VALUE_1246_8 = "1246-8"
    VALUE_1247_6 = "1247-6"
    VALUE_1248_4 = "1248-4"
    VALUE_1264_1 = "1264-1"
    VALUE_1265_8 = "1265-8"
    VALUE_1271_6 = "1271-6"
    VALUE_1272_4 = "1272-4"
    VALUE_1273_2 = "1273-2"
    VALUE_1281_5 = "1281-5"
    VALUE_1282_3 = "1282-3"
    VALUE_1283_1 = "1283-1"
    VALUE_1285_6 = "1285-6"
    VALUE_1286_4 = "1286-4"
    VALUE_1287_2 = "1287-2"
    VALUE_1288_0 = "1288-0"
    VALUE_1289_8 = "1289-8"
    VALUE_1290_6 = "1290-6"
    VALUE_1291_4 = "1291-4"
    VALUE_1292_2 = "1292-2"
    VALUE_1293_0 = "1293-0"
    VALUE_1294_8 = "1294-8"
    VALUE_1295_5 = "1295-5"
    VALUE_1305_2 = "1305-2"
    VALUE_1306_0 = "1306-0"
    VALUE_1307_8 = "1307-8"
    VALUE_1309_4 = "1309-4"
    VALUE_1310_2 = "1310-2"
    VALUE_1312_8 = "1312-8"
    VALUE_1313_6 = "1313-6"
    VALUE_1314_4 = "1314-4"
    VALUE_1315_1 = "1315-1"
    VALUE_1325_0 = "1325-0"
    VALUE_1326_8 = "1326-8"
    VALUE_1327_6 = "1327-6"
    VALUE_1328_4 = "1328-4"
    VALUE_1329_2 = "1329-2"
    VALUE_1331_8 = "1331-8"
    VALUE_1332_6 = "1332-6"
    VALUE_1333_4 = "1333-4"
    VALUE_1334_2 = "1334-2"
    VALUE_1335_9 = "1335-9"
    VALUE_1336_7 = "1336-7"
    VALUE_1338_3 = "1338-3"
    VALUE_1337_5 = "1337-5"
    VALUE_1344_1 = "1344-1"
    VALUE_1345_8 = "1345-8"
    VALUE_1346_6 = "1346-6"
    VALUE_1358_1 = "1358-1"
    VALUE_1359_9 = "1359-9"
    VALUE_1360_7 = "1360-7"
    VALUE_1361_5 = "1361-5"
    VALUE_1365_6 = "1365-6"
    VALUE_1366_4 = "1366-4"
    VALUE_1382_1 = "1382-1"
    VALUE_1383_9 = "1383-9"
    VALUE_1384_7 = "1384-7"
    VALUE_1385_4 = "1385-4"
    VALUE_1391_2 = "1391-2"
    VALUE_1392_0 = "1392-0"
    VALUE_1393_8 = "1393-8"
    VALUE_1394_6 = "1394-6"
    VALUE_1395_3 = "1395-3"
    VALUE_1396_1 = "1396-1"
    VALUE_1397_9 = "1397-9"
    VALUE_1398_7 = "1398-7"
    VALUE_1399_5 = "1399-5"
    VALUE_1400_1 = "1400-1"
    VALUE_1401_9 = "1401-9"
    VALUE_1411_8 = "1411-8"
    VALUE_1412_6 = "1412-6"
    VALUE_1413_4 = "1413-4"
    VALUE_1414_2 = "1414-2"
    VALUE_1416_7 = "1416-7"
    VALUE_1417_5 = "1417-5"
    VALUE_1418_3 = "1418-3"
    VALUE_1419_1 = "1419-1"
    VALUE_1420_9 = "1420-9"
    VALUE_1421_7 = "1421-7"
    VALUE_1422_5 = "1422-5"
    VALUE_1423_3 = "1423-3"
    VALUE_1424_1 = "1424-1"
    VALUE_1425_8 = "1425-8"
    VALUE_1426_6 = "1426-6"
    VALUE_1427_4 = "1427-4"
    VALUE_1428_2 = "1428-2"
    VALUE_1429_0 = "1429-0"
    VALUE_1430_8 = "1430-8"
    VALUE_1431_6 = "1431-6"
    VALUE_1432_4 = "1432-4"
    VALUE_1433_2 = "1433-2"
    VALUE_1434_0 = "1434-0"
    VALUE_1435_7 = "1435-7"
    VALUE_1436_5 = "1436-5"
    VALUE_1437_3 = "1437-3"
    VALUE_1441_5 = "1441-5"
    VALUE_1442_3 = "1442-3"
    VALUE_1443_1 = "1443-1"
    VALUE_1445_6 = "1445-6"
    VALUE_1446_4 = "1446-4"
    VALUE_1450_6 = "1450-6"
    VALUE_1451_4 = "1451-4"
    VALUE_1453_0 = "1453-0"
    VALUE_1454_8 = "1454-8"
    VALUE_1456_3 = "1456-3"
    VALUE_1457_1 = "1457-1"
    VALUE_1458_9 = "1458-9"
    VALUE_1464_7 = "1464-7"
    VALUE_1465_4 = "1465-4"
    VALUE_1466_2 = "1466-2"
    VALUE_1467_0 = "1467-0"
    VALUE_1468_8 = "1468-8"
    VALUE_1469_6 = "1469-6"
    VALUE_1470_4 = "1470-4"
    VALUE_1471_2 = "1471-2"
    VALUE_1472_0 = "1472-0"
    VALUE_1474_6 = "1474-6"
    VALUE_1475_3 = "1475-3"
    VALUE_1476_1 = "1476-1"
    VALUE_1478_7 = "1478-7"
    VALUE_1479_5 = "1479-5"
    VALUE_1480_3 = "1480-3"
    VALUE_1481_1 = "1481-1"
    VALUE_1482_9 = "1482-9"
    VALUE_1483_7 = "1483-7"
    VALUE_1484_5 = "1484-5"
    VALUE_1485_2 = "1485-2"
    VALUE_1489_4 = "1489-4"
    VALUE_1490_2 = "1490-2"
    VALUE_1491_0 = "1491-0"
    VALUE_1492_8 = "1492-8"
    VALUE_1493_6 = "1493-6"
    VALUE_1494_4 = "1494-4"
    VALUE_1495_1 = "1495-1"
    VALUE_1496_9 = "1496-9"
    VALUE_1497_7 = "1497-7"
    VALUE_1498_5 = "1498-5"
    VALUE_1499_3 = "1499-3"
    VALUE_1500_8 = "1500-8"
    VALUE_1501_6 = "1501-6"
    VALUE_1502_4 = "1502-4"
    VALUE_1503_2 = "1503-2"
    VALUE_1506_5 = "1506-5"
    VALUE_1505_7 = "1505-7"
    VALUE_1504_0 = "1504-0"
    VALUE_1507_3 = "1507-3"
    VALUE_1508_1 = "1508-1"
    VALUE_1509_9 = "1509-9"
    VALUE_1510_7 = "1510-7"
    VALUE_1511_5 = "1511-5"
    VALUE_1512_3 = "1512-3"
    VALUE_1513_1 = "1513-1"
    VALUE_1514_9 = "1514-9"
    VALUE_1515_6 = "1515-6"
    VALUE_1516_4 = "1516-4"
    VALUE_1518_0 = "1518-0"
    VALUE_1519_8 = "1519-8"
    VALUE_1520_6 = "1520-6"
    VALUE_1521_4 = "1521-4"
    VALUE_1522_2 = "1522-2"
    VALUE_1523_0 = "1523-0"
    VALUE_1524_8 = "1524-8"
    VALUE_1525_5 = "1525-5"
    VALUE_1526_3 = "1526-3"
    VALUE_1527_1 = "1527-1"
    VALUE_1528_9 = "1528-9"
    VALUE_1529_7 = "1529-7"
    VALUE_1530_5 = "1530-5"
    VALUE_1531_3 = "1531-3"
    VALUE_1532_1 = "1532-1"
    VALUE_1533_9 = "1533-9"
    VALUE_1534_7 = "1534-7"
    VALUE_1535_4 = "1535-4"
    VALUE_1536_2 = "1536-2"
    VALUE_1537_0 = "1537-0"
    VALUE_1538_8 = "1538-8"
    VALUE_1539_6 = "1539-6"
    VALUE_1551_1 = "1551-1"
    VALUE_1552_9 = "1552-9"
    VALUE_1553_7 = "1553-7"
    VALUE_1554_5 = "1554-5"
    VALUE_1566_9 = "1566-9"
    VALUE_1567_7 = "1567-7"
    VALUE_1568_5 = "1568-5"
    VALUE_1569_3 = "1569-3"
    VALUE_1570_1 = "1570-1"
    VALUE_1571_9 = "1571-9"
    VALUE_1573_5 = "1573-5"
    VALUE_1574_3 = "1574-3"
    VALUE_1578_4 = "1578-4"
    VALUE_1579_2 = "1579-2"
    VALUE_1580_0 = "1580-0"
    VALUE_1586_7 = "1586-7"
    VALUE_1587_5 = "1587-5"
    VALUE_1588_3 = "1588-3"
    VALUE_1589_1 = "1589-1"
    VALUE_1590_9 = "1590-9"
    VALUE_1591_7 = "1591-7"
    VALUE_1592_5 = "1592-5"
    VALUE_1593_3 = "1593-3"
    VALUE_1594_1 = "1594-1"
    VALUE_1595_8 = "1595-8"
    VALUE_1596_6 = "1596-6"
    VALUE_1597_4 = "1597-4"
    VALUE_1598_2 = "1598-2"
    VALUE_1599_0 = "1599-0"
    VALUE_1600_6 = "1600-6"
    VALUE_1602_2 = "1602-2"
    VALUE_1603_0 = "1603-0"
    VALUE_1604_8 = "1604-8"
    VALUE_1605_5 = "1605-5"
    VALUE_1609_7 = "1609-7"
    VALUE_1610_5 = "1610-5"
    VALUE_1611_3 = "1611-3"
    VALUE_1612_1 = "1612-1"
    VALUE_1613_9 = "1613-9"
    VALUE_1614_7 = "1614-7"
    VALUE_1615_4 = "1615-4"
    VALUE_1616_2 = "1616-2"
    VALUE_1617_0 = "1617-0"
    VALUE_1618_8 = "1618-8"
    VALUE_1619_6 = "1619-6"
    VALUE_1620_4 = "1620-4"
    VALUE_1621_2 = "1621-2"
    VALUE_1622_0 = "1622-0"
    VALUE_1623_8 = "1623-8"
    VALUE_1624_6 = "1624-6"
    VALUE_1625_3 = "1625-3"
    VALUE_1626_1 = "1626-1"
    VALUE_1627_9 = "1627-9"
    VALUE_1628_7 = "1628-7"
    VALUE_1629_5 = "1629-5"
    VALUE_1631_1 = "1631-1"
    VALUE_1630_3 = "1630-3"
    VALUE_1632_9 = "1632-9"
    VALUE_1633_7 = "1633-7"
    VALUE_1634_5 = "1634-5"
    VALUE_1635_2 = "1635-2"
    VALUE_1636_0 = "1636-0"
    VALUE_1637_8 = "1637-8"
    VALUE_1638_6 = "1638-6"
    VALUE_1639_4 = "1639-4"
    VALUE_1640_2 = "1640-2"
    VALUE_1641_0 = "1641-0"
    VALUE_1653_5 = "1653-5"
    VALUE_1654_3 = "1654-3"
    VALUE_1655_0 = "1655-0"
    VALUE_1656_8 = "1656-8"
    VALUE_1657_6 = "1657-6"
    VALUE_1667_5 = "1667-5"
    VALUE_1668_3 = "1668-3"
    VALUE_1670_9 = "1670-9"
    VALUE_1671_7 = "1671-7"
    VALUE_1672_5 = "1672-5"
    VALUE_1673_3 = "1673-3"
    VALUE_1679_0 = "1679-0"
    VALUE_1680_8 = "1680-8"
    VALUE_1681_6 = "1681-6"
    VALUE_1687_3 = "1687-3"
    VALUE_1688_1 = "1688-1"
    VALUE_1689_9 = "1689-9"
    VALUE_1690_7 = "1690-7"
    VALUE_1696_4 = "1696-4"
    VALUE_1697_2 = "1697-2"
    VALUE_1698_0 = "1698-0"
    VALUE_1724_4 = "1724-4"
    VALUE_1725_1 = "1725-1"
    VALUE_1726_9 = "1726-9"
    VALUE_1727_7 = "1727-7"
    VALUE_1728_5 = "1728-5"
    VALUE_1729_3 = "1729-3"
    VALUE_1730_1 = "1730-1"
    VALUE_1731_9 = "1731-9"
    VALUE_1732_7 = "1732-7"
    VALUE_1733_5 = "1733-5"
    VALUE_1068_6 = "1068-6"
    VALUE_1069_4 = "1069-4"
    VALUE_1070_2 = "1070-2"
    VALUE_1071_0 = "1071-0"
    VALUE_1072_8 = "1072-8"
    VALUE_1073_6 = "1073-6"
    VALUE_1704_6 = "1704-6"
    VALUE_1705_3 = "1705-3"
    VALUE_1711_1 = "1711-1"
    VALUE_1712_9 = "1712-9"
    VALUE_1713_7 = "1713-7"
    VALUE_1717_8 = "1717-8"
    VALUE_1718_6 = "1718-6"
    VALUE_1719_4 = "1719-4"
    VALUE_1720_2 = "1720-2"
    VALUE_1004_1 = "1004-1"
    VALUE_1006_6 = "1006-6"
    VALUE_1008_2 = "1008-2"
    VALUE_1026_4 = "1026-4"
    VALUE_1028_0 = "1028-0"
    VALUE_1033_0 = "1033-0"
    VALUE_1035_5 = "1035-5"
    VALUE_1037_1 = "1037-1"
    VALUE_1039_7 = "1039-7"
    VALUE_1078_5 = "1078-5"
    VALUE_1080_1 = "1080-1"
    VALUE_1086_8 = "1086-8"
    VALUE_1100_7 = "1100-7"
    VALUE_1106_4 = "1106-4"
    VALUE_1112_2 = "1112-2"
    VALUE_1153_6 = "1153-6"
    VALUE_1165_0 = "1165-0"
    VALUE_1167_6 = "1167-6"
    VALUE_1169_2 = "1169-2"
    VALUE_1171_8 = "1171-8"
    VALUE_1173_4 = "1173-4"
    VALUE_1180_9 = "1180-9"
    VALUE_1178_3 = "1178-3"
    VALUE_1182_5 = "1182-5"
    VALUE_1184_1 = "1184-1"
    VALUE_1189_0 = "1189-0"
    VALUE_1191_6 = "1191-6"
    VALUE_1207_0 = "1207-0"
    VALUE_1209_6 = "1209-6"
    VALUE_1250_0 = "1250-0"
    VALUE_1252_6 = "1252-6"
    VALUE_1254_2 = "1254-2"
    VALUE_1258_3 = "1258-3"
    VALUE_1256_7 = "1256-7"
    VALUE_1260_9 = "1260-9"
    VALUE_1262_5 = "1262-5"
    VALUE_1267_4 = "1267-4"
    VALUE_1269_0 = "1269-0"
    VALUE_1275_7 = "1275-7"
    VALUE_1277_3 = "1277-3"
    VALUE_1279_9 = "1279-9"
    VALUE_1297_1 = "1297-1"
    VALUE_1299_7 = "1299-7"
    VALUE_1301_1 = "1301-1"
    VALUE_1303_7 = "1303-7"
    VALUE_1317_7 = "1317-7"
    VALUE_1319_3 = "1319-3"
    VALUE_1321_9 = "1321-9"
    VALUE_1323_5 = "1323-5"
    VALUE_1340_9 = "1340-9"
    VALUE_1342_5 = "1342-5"
    VALUE_1348_2 = "1348-2"
    VALUE_1350_8 = "1350-8"
    VALUE_1352_4 = "1352-4"
    VALUE_1354_0 = "1354-0"
    VALUE_1356_5 = "1356-5"
    VALUE_1363_1 = "1363-1"
    VALUE_1368_0 = "1368-0"
    VALUE_1370_6 = "1370-6"
    VALUE_1372_2 = "1372-2"
    VALUE_1374_8 = "1374-8"
    VALUE_1376_3 = "1376-3"
    VALUE_1378_9 = "1378-9"
    VALUE_1380_5 = "1380-5"
    VALUE_1387_0 = "1387-0"
    VALUE_1389_6 = "1389-6"
    VALUE_1403_5 = "1403-5"
    VALUE_1405_0 = "1405-0"
    VALUE_1407_6 = "1407-6"
    VALUE_1409_2 = "1409-2"
    VALUE_1439_9 = "1439-9"
    VALUE_1448_0 = "1448-0"
    VALUE_1460_5 = "1460-5"
    VALUE_1462_1 = "1462-1"
    VALUE_1487_8 = "1487-8"
    VALUE_1541_2 = "1541-2"
    VALUE_1543_8 = "1543-8"
    VALUE_1545_3 = "1545-3"
    VALUE_1547_9 = "1547-9"
    VALUE_1549_5 = "1549-5"
    VALUE_1556_0 = "1556-0"
    VALUE_1558_6 = "1558-6"
    VALUE_1560_2 = "1560-2"
    VALUE_1562_8 = "1562-8"
    VALUE_1564_4 = "1564-4"
    VALUE_1576_8 = "1576-8"
    VALUE_1582_6 = "1582-6"
    VALUE_1584_2 = "1584-2"
    VALUE_1607_1 = "1607-1"
    VALUE_1643_6 = "1643-6"
    VALUE_1074_4 = "1074-4"
    VALUE_1645_1 = "1645-1"
    VALUE_1647_7 = "1647-7"
    VALUE_1649_3 = "1649-3"
    VALUE_1651_9 = "1651-9"
    VALUE_1659_2 = "1659-2"
    VALUE_1661_8 = "1661-8"
    VALUE_1663_4 = "1663-4"
    VALUE_1665_9 = "1665-9"
    VALUE_1675_8 = "1675-8"
    VALUE_1677_4 = "1677-4"
    VALUE_1683_2 = "1683-2"
    VALUE_1685_7 = "1685-7"
    VALUE_1692_3 = "1692-3"
    VALUE_1694_9 = "1694-9"
    VALUE_1700_4 = "1700-4"
    VALUE_1702_0 = "1702-0"
    VALUE_1707_9 = "1707-9"
    VALUE_1709_5 = "1709-5"
    VALUE_1715_2 = "1715-2"
    VALUE_1722_8 = "1722-8"


class RaceAmericanIndianApache(Enum):
    """
    specDomain: S14919 (C-0-T14914-S14915-S14916-S14919-cpt)
    :cvar VALUE_1010_8:
    :cvar VALUE_1011_6:
    :cvar VALUE_1012_4:
    :cvar VALUE_1013_2:
    :cvar VALUE_1014_0:
    :cvar VALUE_1015_7:
    :cvar VALUE_1016_5:
    :cvar VALUE_1017_3:
    :cvar VALUE_1018_1:
    :cvar VALUE_1019_9:
    """
    VALUE_1010_8 = "1010-8"
    VALUE_1011_6 = "1011-6"
    VALUE_1012_4 = "1012-4"
    VALUE_1013_2 = "1013-2"
    VALUE_1014_0 = "1014-0"
    VALUE_1015_7 = "1015-7"
    VALUE_1016_5 = "1016-5"
    VALUE_1017_3 = "1017-3"
    VALUE_1018_1 = "1018-1"
    VALUE_1019_9 = "1019-9"


class RaceAmericanIndianArapaho(Enum):
    """
    specDomain: S14929 (C-0-T14914-S14915-S14916-S14929-cpt)
    :cvar VALUE_1021_5:
    :cvar VALUE_1022_3:
    :cvar VALUE_1023_1:
    :cvar VALUE_1024_9:
    """
    VALUE_1021_5 = "1021-5"
    VALUE_1022_3 = "1022-3"
    VALUE_1023_1 = "1023-1"
    VALUE_1024_9 = "1024-9"


class RaceAmericanIndianAssiniboineSioux(Enum):
    """
    specDomain: S14935 (C-0-T14914-S14915-S14916-S14935-cpt)
    :cvar VALUE_1030_6:
    :cvar VALUE_1031_4:
    """
    VALUE_1030_6 = "1030-6"
    VALUE_1031_4 = "1031-4"


class RaceAmericanIndianCaddo(Enum):
    """
    specDomain: S14941 (C-0-T14914-S14915-S14916-S14941-cpt)
    :cvar VALUE_1041_3:
    :cvar VALUE_1042_1:
    """
    VALUE_1041_3 = "1041-3"
    VALUE_1042_1 = "1042-1"


class RaceAmericanIndianCahuilla(Enum):
    """
    specDomain: S14943 (C-0-T14914-S14915-S14916-S14943-cpt)
    :cvar VALUE_1044_7:
    :cvar VALUE_1045_4:
    :cvar VALUE_1046_2:
    :cvar VALUE_1047_0:
    :cvar VALUE_1048_8:
    :cvar VALUE_1049_6:
    :cvar VALUE_1050_4:
    :cvar VALUE_1051_2:
    """
    VALUE_1044_7 = "1044-7"
    VALUE_1045_4 = "1045-4"
    VALUE_1046_2 = "1046-2"
    VALUE_1047_0 = "1047-0"
    VALUE_1048_8 = "1048-8"
    VALUE_1049_6 = "1049-6"
    VALUE_1050_4 = "1050-4"
    VALUE_1051_2 = "1051-2"


class RaceAmericanIndianCalifornia(Enum):
    """
    specDomain: S14951 (C-0-T14914-S14915-S14916-S14951-cpt)
    :cvar VALUE_1053_8:
    :cvar VALUE_1054_6:
    :cvar VALUE_1055_3:
    :cvar VALUE_1056_1:
    :cvar VALUE_1057_9:
    :cvar VALUE_1058_7:
    :cvar VALUE_1059_5:
    :cvar VALUE_1060_3:
    :cvar VALUE_1061_1:
    :cvar VALUE_1062_9:
    :cvar VALUE_1063_7:
    :cvar VALUE_1064_5:
    :cvar VALUE_1065_2:
    :cvar VALUE_1066_0:
    """
    VALUE_1053_8 = "1053-8"
    VALUE_1054_6 = "1054-6"
    VALUE_1055_3 = "1055-3"
    VALUE_1056_1 = "1056-1"
    VALUE_1057_9 = "1057-9"
    VALUE_1058_7 = "1058-7"
    VALUE_1059_5 = "1059-5"
    VALUE_1060_3 = "1060-3"
    VALUE_1061_1 = "1061-1"
    VALUE_1062_9 = "1062-9"
    VALUE_1063_7 = "1063-7"
    VALUE_1064_5 = "1064-5"
    VALUE_1065_2 = "1065-2"
    VALUE_1066_0 = "1066-0"


class RaceAmericanIndianChemakuan(Enum):
    """
    specDomain: S14975 (C-0-T14914-S14915-S14916-S14975-cpt)
    :cvar VALUE_1082_7:
    :cvar VALUE_1083_5:
    :cvar VALUE_1084_3:
    """
    VALUE_1082_7 = "1082-7"
    VALUE_1083_5 = "1083-5"
    VALUE_1084_3 = "1084-3"


class RaceAmericanIndianCherokee(Enum):
    """
    specDomain: S14979 (C-0-T14914-S14915-S14916-S14979-cpt)
    :cvar VALUE_1088_4:
    :cvar VALUE_1089_2:
    :cvar VALUE_1090_0:
    :cvar VALUE_1091_8:
    :cvar VALUE_1092_6:
    :cvar VALUE_1093_4:
    :cvar VALUE_1094_2:
    :cvar VALUE_1095_9:
    :cvar VALUE_1096_7:
    :cvar VALUE_1097_5:
    :cvar VALUE_1098_3:
    """
    VALUE_1088_4 = "1088-4"
    VALUE_1089_2 = "1089-2"
    VALUE_1090_0 = "1090-0"
    VALUE_1091_8 = "1091-8"
    VALUE_1092_6 = "1092-6"
    VALUE_1093_4 = "1093-4"
    VALUE_1094_2 = "1094-2"
    VALUE_1095_9 = "1095-9"
    VALUE_1096_7 = "1096-7"
    VALUE_1097_5 = "1097-5"
    VALUE_1098_3 = "1098-3"


class RaceAmericanIndianCheyenne(Enum):
    """
    specDomain: S14991 (C-0-T14914-S14915-S14916-S14991-cpt)
    :cvar VALUE_1102_3:
    :cvar VALUE_1103_1:
    :cvar VALUE_1104_9:
    """
    VALUE_1102_3 = "1102-3"
    VALUE_1103_1 = "1103-1"
    VALUE_1104_9 = "1104-9"


class RaceAmericanIndianChickahominy(Enum):
    """
    specDomain: S14995 (C-0-T14914-S14915-S14916-S14995-cpt)
    :cvar VALUE_1108_0:
    :cvar VALUE_1109_8:
    :cvar VALUE_1110_6:
    """
    VALUE_1108_0 = "1108-0"
    VALUE_1109_8 = "1109-8"
    VALUE_1110_6 = "1110-6"


class RaceAmericanIndianChinook(Enum):
    """
    specDomain: S14999 (C-0-T14914-S14915-S14916-S14999-cpt)
    :cvar VALUE_1114_8:
    :cvar VALUE_1115_5:
    :cvar VALUE_1116_3:
    :cvar VALUE_1117_1:
    :cvar VALUE_1118_9:
    :cvar VALUE_1119_7:
    :cvar VALUE_1120_5:
    :cvar VALUE_1121_3:
    """
    VALUE_1114_8 = "1114-8"
    VALUE_1115_5 = "1115-5"
    VALUE_1116_3 = "1116-3"
    VALUE_1117_1 = "1117-1"
    VALUE_1118_9 = "1118-9"
    VALUE_1119_7 = "1119-7"
    VALUE_1120_5 = "1120-5"
    VALUE_1121_3 = "1121-3"


class RaceAmericanIndianChippewa(Enum):
    """
    specDomain: S15007 (C-0-T14914-S14915-S14916-S15007-cpt)
    :cvar VALUE_1123_9:
    :cvar VALUE_1124_7:
    :cvar VALUE_1125_4:
    :cvar VALUE_1126_2:
    :cvar VALUE_1127_0:
    :cvar VALUE_1128_8:
    :cvar VALUE_1129_6:
    :cvar VALUE_1130_4:
    :cvar VALUE_1131_2:
    :cvar VALUE_1132_0:
    :cvar VALUE_1134_6:
    :cvar VALUE_1133_8:
    :cvar VALUE_1135_3:
    :cvar VALUE_1136_1:
    :cvar VALUE_1137_9:
    :cvar VALUE_1138_7:
    :cvar VALUE_1139_5:
    :cvar VALUE_1140_3:
    :cvar VALUE_1141_1:
    :cvar VALUE_1142_9:
    :cvar VALUE_1143_7:
    :cvar VALUE_1145_2:
    :cvar VALUE_1146_0:
    :cvar VALUE_1144_5:
    :cvar VALUE_1147_8:
    :cvar VALUE_1148_6:
    """
    VALUE_1123_9 = "1123-9"
    VALUE_1124_7 = "1124-7"
    VALUE_1125_4 = "1125-4"
    VALUE_1126_2 = "1126-2"
    VALUE_1127_0 = "1127-0"
    VALUE_1128_8 = "1128-8"
    VALUE_1129_6 = "1129-6"
    VALUE_1130_4 = "1130-4"
    VALUE_1131_2 = "1131-2"
    VALUE_1132_0 = "1132-0"
    VALUE_1134_6 = "1134-6"
    VALUE_1133_8 = "1133-8"
    VALUE_1135_3 = "1135-3"
    VALUE_1136_1 = "1136-1"
    VALUE_1137_9 = "1137-9"
    VALUE_1138_7 = "1138-7"
    VALUE_1139_5 = "1139-5"
    VALUE_1140_3 = "1140-3"
    VALUE_1141_1 = "1141-1"
    VALUE_1142_9 = "1142-9"
    VALUE_1143_7 = "1143-7"
    VALUE_1145_2 = "1145-2"
    VALUE_1146_0 = "1146-0"
    VALUE_1144_5 = "1144-5"
    VALUE_1147_8 = "1147-8"
    VALUE_1148_6 = "1148-6"


class RaceAmericanIndianChippewaCree(Enum):
    """
    specDomain: S15033 (C-0-T14914-S14915-S14916-S15033-cpt)
    :cvar VALUE_1150_2:
    :cvar VALUE_1151_0:
    """
    VALUE_1150_2 = "1150-2"
    VALUE_1151_0 = "1151-0"


class RaceAmericanIndianChoctaw(Enum):
    """
    specDomain: S15036 (C-0-T14914-S14915-S14916-S15036-cpt)
    :cvar VALUE_1155_1:
    :cvar VALUE_1156_9:
    :cvar VALUE_1157_7:
    :cvar VALUE_1158_5:
    :cvar VALUE_1159_3:
    :cvar VALUE_1160_1:
    """
    VALUE_1155_1 = "1155-1"
    VALUE_1156_9 = "1156-9"
    VALUE_1157_7 = "1157-7"
    VALUE_1158_5 = "1158-5"
    VALUE_1159_3 = "1159-3"
    VALUE_1160_1 = "1160-1"


class RaceAmericanIndianChumash(Enum):
    """
    specDomain: S15042 (C-0-T14914-S14915-S14916-S15042-cpt)
    :cvar VALUE_1162_7:
    :cvar VALUE_1163_5:
    """
    VALUE_1162_7 = "1162-7"
    VALUE_1163_5 = "1163-5"


class RaceAmericanIndianComanche(Enum):
    """
    specDomain: S15049 (C-0-T14914-S14915-S14916-S15049-cpt)
    :cvar VALUE_1175_9:
    :cvar VALUE_1176_7:
    """
    VALUE_1175_9 = "1175-9"
    VALUE_1176_7 = "1176-7"


class RaceAmericanIndianCoushatta(Enum):
    """
    specDomain: S15055 (C-0-T14914-S14915-S14916-S15055-cpt)
    :cvar VALUE_1186_6:
    :cvar VALUE_1187_4:
    """
    VALUE_1186_6 = "1186-6"
    VALUE_1187_4 = "1187-4"


class RaceAmericanIndianCreek(Enum):
    """
    specDomain: S15059 (C-0-T14914-S14915-S14916-S15059-cpt)
    :cvar VALUE_1193_2:
    :cvar VALUE_1194_0:
    :cvar VALUE_1195_7:
    :cvar VALUE_1196_5:
    :cvar VALUE_1197_3:
    :cvar VALUE_1198_1:
    :cvar VALUE_1199_9:
    :cvar VALUE_1200_5:
    :cvar VALUE_1201_3:
    :cvar VALUE_1202_1:
    :cvar VALUE_1203_9:
    :cvar VALUE_1204_7:
    :cvar VALUE_1205_4:
    """
    VALUE_1193_2 = "1193-2"
    VALUE_1194_0 = "1194-0"
    VALUE_1195_7 = "1195-7"
    VALUE_1196_5 = "1196-5"
    VALUE_1197_3 = "1197-3"
    VALUE_1198_1 = "1198-1"
    VALUE_1199_9 = "1199-9"
    VALUE_1200_5 = "1200-5"
    VALUE_1201_3 = "1201-3"
    VALUE_1202_1 = "1202-1"
    VALUE_1203_9 = "1203-9"
    VALUE_1204_7 = "1204-7"
    VALUE_1205_4 = "1205-4"


class RaceAmericanIndianCupeno(Enum):
    """
    specDomain: S15074 (C-0-T14914-S14915-S14916-S15074-cpt)
    :cvar VALUE_1211_2:
    :cvar VALUE_1212_0:
    """
    VALUE_1211_2 = "1211-2"
    VALUE_1212_0 = "1212-0"


class RaceAmericanIndianDelaware(Enum):
    """
    specDomain: S15076 (C-0-T14914-S14915-S14916-S15076-cpt)
    :cvar VALUE_1214_6:
    :cvar VALUE_1215_3:
    :cvar VALUE_1216_1:
    :cvar VALUE_1217_9:
    :cvar VALUE_1218_7:
    :cvar VALUE_1219_5:
    :cvar VALUE_1220_3:
    """
    VALUE_1214_6 = "1214-6"
    VALUE_1215_3 = "1215-3"
    VALUE_1216_1 = "1216-1"
    VALUE_1217_9 = "1217-9"
    VALUE_1218_7 = "1218-7"
    VALUE_1219_5 = "1219-5"
    VALUE_1220_3 = "1220-3"


class RaceAmericanIndianDiegueno(Enum):
    """
    specDomain: S15083 (C-0-T14914-S14915-S14916-S15083-cpt)
    :cvar VALUE_1222_9:
    :cvar VALUE_1223_7:
    :cvar VALUE_1224_5:
    :cvar VALUE_1225_2:
    :cvar VALUE_1226_0:
    :cvar VALUE_1227_8:
    :cvar VALUE_1228_6:
    :cvar VALUE_1229_4:
    :cvar VALUE_1230_2:
    :cvar VALUE_1231_0:
    """
    VALUE_1222_9 = "1222-9"
    VALUE_1223_7 = "1223-7"
    VALUE_1224_5 = "1224-5"
    VALUE_1225_2 = "1225-2"
    VALUE_1226_0 = "1226-0"
    VALUE_1227_8 = "1227-8"
    VALUE_1228_6 = "1228-6"
    VALUE_1229_4 = "1229-4"
    VALUE_1230_2 = "1230-2"
    VALUE_1231_0 = "1231-0"


class RaceAmericanIndianEasternTribes(Enum):
    """
    specDomain: S15093 (C-0-T14914-S14915-S14916-S15093-cpt)
    :cvar VALUE_1233_6:
    :cvar VALUE_1234_4:
    :cvar VALUE_1235_1:
    :cvar VALUE_1236_9:
    :cvar VALUE_1237_7:
    :cvar VALUE_1238_5:
    :cvar VALUE_1239_3:
    :cvar VALUE_1240_1:
    :cvar VALUE_1241_9:
    :cvar VALUE_1242_7:
    :cvar VALUE_1243_5:
    :cvar VALUE_1244_3:
    :cvar VALUE_1245_0:
    :cvar VALUE_1246_8:
    :cvar VALUE_1247_6:
    :cvar VALUE_1248_4:
    """
    VALUE_1233_6 = "1233-6"
    VALUE_1234_4 = "1234-4"
    VALUE_1235_1 = "1235-1"
    VALUE_1236_9 = "1236-9"
    VALUE_1237_7 = "1237-7"
    VALUE_1238_5 = "1238-5"
    VALUE_1239_3 = "1239-3"
    VALUE_1240_1 = "1240-1"
    VALUE_1241_9 = "1241-9"
    VALUE_1242_7 = "1242-7"
    VALUE_1243_5 = "1243-5"
    VALUE_1244_3 = "1244-3"
    VALUE_1245_0 = "1245-0"
    VALUE_1246_8 = "1246-8"
    VALUE_1247_6 = "1247-6"
    VALUE_1248_4 = "1248-4"


class RaceAmericanIndianGrosVentres(Enum):
    """
    specDomain: S15116 (C-0-T14914-S14915-S14916-S15116-cpt)
    :cvar VALUE_1264_1:
    :cvar VALUE_1265_8:
    """
    VALUE_1264_1 = "1264-1"
    VALUE_1265_8 = "1265-8"


class RaceAmericanIndianHoopa(Enum):
    """
    specDomain: S15120 (C-0-T14914-S14915-S14916-S15120-cpt)
    :cvar VALUE_1271_6:
    :cvar VALUE_1272_4:
    :cvar VALUE_1273_2:
    """
    VALUE_1271_6 = "1271-6"
    VALUE_1272_4 = "1272-4"
    VALUE_1273_2 = "1273-2"


class RaceAmericanIndianIowa(Enum):
    """
    specDomain: S15126 (C-0-T14914-S14915-S14916-S15126-cpt)
    :cvar VALUE_1281_5:
    :cvar VALUE_1282_3:
    :cvar VALUE_1283_1:
    """
    VALUE_1281_5 = "1281-5"
    VALUE_1282_3 = "1282-3"
    VALUE_1283_1 = "1283-1"


class RaceAmericanIndianIroquois(Enum):
    """
    specDomain: S15129 (C-0-T14914-S14915-S14916-S15129-cpt)
    :cvar VALUE_1285_6:
    :cvar VALUE_1286_4:
    :cvar VALUE_1287_2:
    :cvar VALUE_1288_0:
    :cvar VALUE_1289_8:
    :cvar VALUE_1290_6:
    :cvar VALUE_1291_4:
    :cvar VALUE_1292_2:
    :cvar VALUE_1293_0:
    :cvar VALUE_1294_8:
    :cvar VALUE_1295_5:
    """
    VALUE_1285_6 = "1285-6"
    VALUE_1286_4 = "1286-4"
    VALUE_1287_2 = "1287-2"
    VALUE_1288_0 = "1288-0"
    VALUE_1289_8 = "1289-8"
    VALUE_1290_6 = "1290-6"
    VALUE_1291_4 = "1291-4"
    VALUE_1292_2 = "1292-2"
    VALUE_1293_0 = "1293-0"
    VALUE_1294_8 = "1294-8"
    VALUE_1295_5 = "1295-5"


class RaceAmericanIndianKickapoo(Enum):
    """
    specDomain: S15144 (C-0-T14914-S14915-S14916-S15144-cpt)
    :cvar VALUE_1305_2:
    :cvar VALUE_1306_0:
    :cvar VALUE_1307_8:
    """
    VALUE_1305_2 = "1305-2"
    VALUE_1306_0 = "1306-0"
    VALUE_1307_8 = "1307-8"


class RaceAmericanIndianKiowa(Enum):
    """
    specDomain: S15147 (C-0-T14914-S14915-S14916-S15147-cpt)
    :cvar VALUE_1309_4:
    :cvar VALUE_1310_2:
    """
    VALUE_1309_4 = "1309-4"
    VALUE_1310_2 = "1310-2"


class RaceAmericanIndianKlallam(Enum):
    """
    specDomain: S15149 (C-0-T14914-S14915-S14916-S15149-cpt)
    :cvar VALUE_1312_8:
    :cvar VALUE_1313_6:
    :cvar VALUE_1314_4:
    :cvar VALUE_1315_1:
    """
    VALUE_1312_8 = "1312-8"
    VALUE_1313_6 = "1313-6"
    VALUE_1314_4 = "1314-4"
    VALUE_1315_1 = "1315-1"


class RaceAmericanIndianLongIsland(Enum):
    """
    specDomain: S15157 (C-0-T14914-S14915-S14916-S15157-cpt)
    :cvar VALUE_1325_0:
    :cvar VALUE_1326_8:
    :cvar VALUE_1327_6:
    :cvar VALUE_1328_4:
    :cvar VALUE_1329_2:
    """
    VALUE_1325_0 = "1325-0"
    VALUE_1326_8 = "1326-8"
    VALUE_1327_6 = "1327-6"
    VALUE_1328_4 = "1328-4"
    VALUE_1329_2 = "1329-2"


class RaceAmericanIndianLuiseno(Enum):
    """
    specDomain: S15162 (C-0-T14914-S14915-S14916-S15162-cpt)
    :cvar VALUE_1331_8:
    :cvar VALUE_1332_6:
    :cvar VALUE_1333_4:
    :cvar VALUE_1334_2:
    :cvar VALUE_1335_9:
    :cvar VALUE_1336_7:
    :cvar VALUE_1338_3:
    :cvar VALUE_1337_5:
    """
    VALUE_1331_8 = "1331-8"
    VALUE_1332_6 = "1332-6"
    VALUE_1333_4 = "1333-4"
    VALUE_1334_2 = "1334-2"
    VALUE_1335_9 = "1335-9"
    VALUE_1336_7 = "1336-7"
    VALUE_1338_3 = "1338-3"
    VALUE_1337_5 = "1337-5"


class RaceAmericanIndianMaidu(Enum):
    """
    specDomain: S15172 (C-0-T14914-S14915-S14916-S15172-cpt)
    :cvar VALUE_1344_1:
    :cvar VALUE_1345_8:
    :cvar VALUE_1346_6:
    """
    VALUE_1344_1 = "1344-1"
    VALUE_1345_8 = "1345-8"
    VALUE_1346_6 = "1346-6"


class RaceAmericanIndianMiami(Enum):
    """
    specDomain: S15180 (C-0-T14914-S14915-S14916-S15180-cpt)
    :cvar VALUE_1358_1:
    :cvar VALUE_1359_9:
    :cvar VALUE_1360_7:
    :cvar VALUE_1361_5:
    """
    VALUE_1358_1 = "1358-1"
    VALUE_1359_9 = "1359-9"
    VALUE_1360_7 = "1360-7"
    VALUE_1361_5 = "1361-5"


class RaceAmericanIndianMicmac(Enum):
    """
    specDomain: S15185 (C-0-T14914-S14915-S14916-S15185-cpt)
    :cvar VALUE_1365_6:
    :cvar VALUE_1366_4:
    """
    VALUE_1365_6 = "1365-6"
    VALUE_1366_4 = "1366-4"


class RaceAmericanIndianNavajo(Enum):
    """
    specDomain: S15194 (C-0-T14914-S14915-S14916-S15194-cpt)
    :cvar VALUE_1382_1:
    :cvar VALUE_1383_9:
    :cvar VALUE_1384_7:
    :cvar VALUE_1385_4:
    """
    VALUE_1382_1 = "1382-1"
    VALUE_1383_9 = "1383-9"
    VALUE_1384_7 = "1384-7"
    VALUE_1385_4 = "1385-4"


class RaceAmericanIndianNorthwestTribes(Enum):
    """
    specDomain: S15200 (C-0-T14914-S14915-S14916-S15200-cpt)
    :cvar VALUE_1391_2:
    :cvar VALUE_1392_0:
    :cvar VALUE_1393_8:
    :cvar VALUE_1394_6:
    :cvar VALUE_1395_3:
    :cvar VALUE_1396_1:
    :cvar VALUE_1397_9:
    :cvar VALUE_1398_7:
    :cvar VALUE_1399_5:
    :cvar VALUE_1400_1:
    :cvar VALUE_1401_9:
    """
    VALUE_1391_2 = "1391-2"
    VALUE_1392_0 = "1392-0"
    VALUE_1393_8 = "1393-8"
    VALUE_1394_6 = "1394-6"
    VALUE_1395_3 = "1395-3"
    VALUE_1396_1 = "1396-1"
    VALUE_1397_9 = "1397-9"
    VALUE_1398_7 = "1398-7"
    VALUE_1399_5 = "1399-5"
    VALUE_1400_1 = "1400-1"
    VALUE_1401_9 = "1401-9"


class RaceAmericanIndianOttawa(Enum):
    """
    specDomain: S15215 (C-0-T14914-S14915-S14916-S15215-cpt)
    :cvar VALUE_1411_8:
    :cvar VALUE_1412_6:
    :cvar VALUE_1413_4:
    :cvar VALUE_1414_2:
    """
    VALUE_1411_8 = "1411-8"
    VALUE_1412_6 = "1412-6"
    VALUE_1413_4 = "1413-4"
    VALUE_1414_2 = "1414-2"


class RaceAmericanIndianPaiute(Enum):
    """
    specDomain: S15219 (C-0-T14914-S14915-S14916-S15219-cpt)
    :cvar VALUE_1416_7:
    :cvar VALUE_1417_5:
    :cvar VALUE_1418_3:
    :cvar VALUE_1419_1:
    :cvar VALUE_1420_9:
    :cvar VALUE_1421_7:
    :cvar VALUE_1422_5:
    :cvar VALUE_1423_3:
    :cvar VALUE_1424_1:
    :cvar VALUE_1425_8:
    :cvar VALUE_1426_6:
    :cvar VALUE_1427_4:
    :cvar VALUE_1428_2:
    :cvar VALUE_1429_0:
    :cvar VALUE_1430_8:
    :cvar VALUE_1431_6:
    :cvar VALUE_1432_4:
    :cvar VALUE_1433_2:
    :cvar VALUE_1434_0:
    :cvar VALUE_1435_7:
    :cvar VALUE_1436_5:
    :cvar VALUE_1437_3:
    """
    VALUE_1416_7 = "1416-7"
    VALUE_1417_5 = "1417-5"
    VALUE_1418_3 = "1418-3"
    VALUE_1419_1 = "1419-1"
    VALUE_1420_9 = "1420-9"
    VALUE_1421_7 = "1421-7"
    VALUE_1422_5 = "1422-5"
    VALUE_1423_3 = "1423-3"
    VALUE_1424_1 = "1424-1"
    VALUE_1425_8 = "1425-8"
    VALUE_1426_6 = "1426-6"
    VALUE_1427_4 = "1427-4"
    VALUE_1428_2 = "1428-2"
    VALUE_1429_0 = "1429-0"
    VALUE_1430_8 = "1430-8"
    VALUE_1431_6 = "1431-6"
    VALUE_1432_4 = "1432-4"
    VALUE_1433_2 = "1433-2"
    VALUE_1434_0 = "1434-0"
    VALUE_1435_7 = "1435-7"
    VALUE_1436_5 = "1436-5"
    VALUE_1437_3 = "1437-3"


class RaceAmericanIndianPassamaquoddy(Enum):
    """
    specDomain: S15242 (C-0-T14914-S14915-S14916-S15242-cpt)
    :cvar VALUE_1441_5:
    :cvar VALUE_1442_3:
    :cvar VALUE_1443_1:
    """
    VALUE_1441_5 = "1441-5"
    VALUE_1442_3 = "1442-3"
    VALUE_1443_1 = "1443-1"


class RaceAmericanIndianPawnee(Enum):
    """
    specDomain: S15245 (C-0-T14914-S14915-S14916-S15245-cpt)
    :cvar VALUE_1445_6:
    :cvar VALUE_1446_4:
    """
    VALUE_1445_6 = "1445-6"
    VALUE_1446_4 = "1446-4"


class RaceAmericanIndianPeoria(Enum):
    """
    specDomain: S15248 (C-0-T14914-S14915-S14916-S15248-cpt)
    :cvar VALUE_1450_6:
    :cvar VALUE_1451_4:
    """
    VALUE_1450_6 = "1450-6"
    VALUE_1451_4 = "1451-4"


class RaceAmericanIndianPequot(Enum):
    """
    specDomain: S15250 (C-0-T14914-S14915-S14916-S15250-cpt)
    :cvar VALUE_1453_0:
    :cvar VALUE_1454_8:
    """
    VALUE_1453_0 = "1453-0"
    VALUE_1454_8 = "1454-8"


class RaceAmericanIndianPima(Enum):
    """
    specDomain: S15252 (C-0-T14914-S14915-S14916-S15252-cpt)
    :cvar VALUE_1456_3:
    :cvar VALUE_1457_1:
    :cvar VALUE_1458_9:
    """
    VALUE_1456_3 = "1456-3"
    VALUE_1457_1 = "1457-1"
    VALUE_1458_9 = "1458-9"


class RaceAmericanIndianPomo(Enum):
    """
    specDomain: S15257 (C-0-T14914-S14915-S14916-S15257-cpt)
    :cvar VALUE_1464_7:
    :cvar VALUE_1465_4:
    :cvar VALUE_1466_2:
    :cvar VALUE_1467_0:
    :cvar VALUE_1468_8:
    :cvar VALUE_1469_6:
    :cvar VALUE_1470_4:
    :cvar VALUE_1471_2:
    :cvar VALUE_1472_0:
    """
    VALUE_1464_7 = "1464-7"
    VALUE_1465_4 = "1465-4"
    VALUE_1466_2 = "1466-2"
    VALUE_1467_0 = "1467-0"
    VALUE_1468_8 = "1468-8"
    VALUE_1469_6 = "1469-6"
    VALUE_1470_4 = "1470-4"
    VALUE_1471_2 = "1471-2"
    VALUE_1472_0 = "1472-0"


class RaceAmericanIndianPonca(Enum):
    """
    specDomain: S15266 (C-0-T14914-S14915-S14916-S15266-cpt)
    :cvar VALUE_1474_6:
    :cvar VALUE_1475_3:
    :cvar VALUE_1476_1:
    """
    VALUE_1474_6 = "1474-6"
    VALUE_1475_3 = "1475-3"
    VALUE_1476_1 = "1476-1"


class RaceAmericanIndianPotawatomi(Enum):
    """
    specDomain: S15269 (C-0-T14914-S14915-S14916-S15269-cpt)
    :cvar VALUE_1478_7:
    :cvar VALUE_1479_5:
    :cvar VALUE_1480_3:
    :cvar VALUE_1481_1:
    :cvar VALUE_1482_9:
    :cvar VALUE_1483_7:
    :cvar VALUE_1484_5:
    :cvar VALUE_1485_2:
    """
    VALUE_1478_7 = "1478-7"
    VALUE_1479_5 = "1479-5"
    VALUE_1480_3 = "1480-3"
    VALUE_1481_1 = "1481-1"
    VALUE_1482_9 = "1482-9"
    VALUE_1483_7 = "1483-7"
    VALUE_1484_5 = "1484-5"
    VALUE_1485_2 = "1485-2"


class RaceAmericanIndianPueblo(Enum):
    """
    specDomain: S15278 (C-0-T14914-S14915-S14916-S15278-cpt)
    :cvar VALUE_1489_4:
    :cvar VALUE_1490_2:
    :cvar VALUE_1491_0:
    :cvar VALUE_1492_8:
    :cvar VALUE_1493_6:
    :cvar VALUE_1494_4:
    :cvar VALUE_1495_1:
    :cvar VALUE_1496_9:
    :cvar VALUE_1497_7:
    :cvar VALUE_1498_5:
    :cvar VALUE_1499_3:
    :cvar VALUE_1500_8:
    :cvar VALUE_1501_6:
    :cvar VALUE_1502_4:
    :cvar VALUE_1503_2:
    :cvar VALUE_1506_5:
    :cvar VALUE_1505_7:
    :cvar VALUE_1504_0:
    :cvar VALUE_1507_3:
    :cvar VALUE_1508_1:
    :cvar VALUE_1509_9:
    :cvar VALUE_1510_7:
    :cvar VALUE_1511_5:
    :cvar VALUE_1512_3:
    :cvar VALUE_1513_1:
    :cvar VALUE_1514_9:
    :cvar VALUE_1515_6:
    :cvar VALUE_1516_4:
    """
    VALUE_1489_4 = "1489-4"
    VALUE_1490_2 = "1490-2"
    VALUE_1491_0 = "1491-0"
    VALUE_1492_8 = "1492-8"
    VALUE_1493_6 = "1493-6"
    VALUE_1494_4 = "1494-4"
    VALUE_1495_1 = "1495-1"
    VALUE_1496_9 = "1496-9"
    VALUE_1497_7 = "1497-7"
    VALUE_1498_5 = "1498-5"
    VALUE_1499_3 = "1499-3"
    VALUE_1500_8 = "1500-8"
    VALUE_1501_6 = "1501-6"
    VALUE_1502_4 = "1502-4"
    VALUE_1503_2 = "1503-2"
    VALUE_1506_5 = "1506-5"
    VALUE_1505_7 = "1505-7"
    VALUE_1504_0 = "1504-0"
    VALUE_1507_3 = "1507-3"
    VALUE_1508_1 = "1508-1"
    VALUE_1509_9 = "1509-9"
    VALUE_1510_7 = "1510-7"
    VALUE_1511_5 = "1511-5"
    VALUE_1512_3 = "1512-3"
    VALUE_1513_1 = "1513-1"
    VALUE_1514_9 = "1514-9"
    VALUE_1515_6 = "1515-6"
    VALUE_1516_4 = "1516-4"


class RaceAmericanIndianPugetSoundSalish(Enum):
    """
    specDomain: S15306 (C-0-T14914-S14915-S14916-S15306-cpt)
    :cvar VALUE_1518_0:
    :cvar VALUE_1519_8:
    :cvar VALUE_1520_6:
    :cvar VALUE_1521_4:
    :cvar VALUE_1522_2:
    :cvar VALUE_1523_0:
    :cvar VALUE_1524_8:
    :cvar VALUE_1525_5:
    :cvar VALUE_1526_3:
    :cvar VALUE_1527_1:
    :cvar VALUE_1528_9:
    :cvar VALUE_1529_7:
    :cvar VALUE_1530_5:
    :cvar VALUE_1531_3:
    :cvar VALUE_1532_1:
    :cvar VALUE_1533_9:
    :cvar VALUE_1534_7:
    :cvar VALUE_1535_4:
    :cvar VALUE_1536_2:
    :cvar VALUE_1537_0:
    :cvar VALUE_1538_8:
    :cvar VALUE_1539_6:
    """
    VALUE_1518_0 = "1518-0"
    VALUE_1519_8 = "1519-8"
    VALUE_1520_6 = "1520-6"
    VALUE_1521_4 = "1521-4"
    VALUE_1522_2 = "1522-2"
    VALUE_1523_0 = "1523-0"
    VALUE_1524_8 = "1524-8"
    VALUE_1525_5 = "1525-5"
    VALUE_1526_3 = "1526-3"
    VALUE_1527_1 = "1527-1"
    VALUE_1528_9 = "1528-9"
    VALUE_1529_7 = "1529-7"
    VALUE_1530_5 = "1530-5"
    VALUE_1531_3 = "1531-3"
    VALUE_1532_1 = "1532-1"
    VALUE_1533_9 = "1533-9"
    VALUE_1534_7 = "1534-7"
    VALUE_1535_4 = "1535-4"
    VALUE_1536_2 = "1536-2"
    VALUE_1537_0 = "1537-0"
    VALUE_1538_8 = "1538-8"
    VALUE_1539_6 = "1539-6"


class RaceAmericanIndianSacFox(Enum):
    """
    specDomain: S15333 (C-0-T14914-S14915-S14916-S15333-cpt)
    :cvar VALUE_1551_1:
    :cvar VALUE_1552_9:
    :cvar VALUE_1553_7:
    :cvar VALUE_1554_5:
    """
    VALUE_1551_1 = "1551-1"
    VALUE_1552_9 = "1552-9"
    VALUE_1553_7 = "1553-7"
    VALUE_1554_5 = "1554-5"


class RaceAmericanIndianSeminole(Enum):
    """
    specDomain: S15342 (C-0-T14914-S14915-S14916-S15342-cpt)
    :cvar VALUE_1566_9:
    :cvar VALUE_1567_7:
    :cvar VALUE_1568_5:
    :cvar VALUE_1569_3:
    :cvar VALUE_1570_1:
    :cvar VALUE_1571_9:
    """
    VALUE_1566_9 = "1566-9"
    VALUE_1567_7 = "1567-7"
    VALUE_1568_5 = "1568-5"
    VALUE_1569_3 = "1569-3"
    VALUE_1570_1 = "1570-1"
    VALUE_1571_9 = "1571-9"


class RaceAmericanIndianSerrano(Enum):
    """
    specDomain: S15348 (C-0-T14914-S14915-S14916-S15348-cpt)
    :cvar VALUE_1573_5:
    :cvar VALUE_1574_3:
    """
    VALUE_1573_5 = "1573-5"
    VALUE_1574_3 = "1574-3"


class RaceAmericanIndianShawnee(Enum):
    """
    specDomain: S15351 (C-0-T14914-S14915-S14916-S15351-cpt)
    :cvar VALUE_1578_4:
    :cvar VALUE_1579_2:
    :cvar VALUE_1580_0:
    """
    VALUE_1578_4 = "1578-4"
    VALUE_1579_2 = "1579-2"
    VALUE_1580_0 = "1580-0"


class RaceAmericanIndianShoshone(Enum):
    """
    specDomain: S15356 (C-0-T14914-S14915-S14916-S15356-cpt)
    :cvar VALUE_1586_7:
    :cvar VALUE_1587_5:
    :cvar VALUE_1588_3:
    :cvar VALUE_1589_1:
    :cvar VALUE_1590_9:
    :cvar VALUE_1591_7:
    :cvar VALUE_1592_5:
    :cvar VALUE_1593_3:
    :cvar VALUE_1594_1:
    :cvar VALUE_1595_8:
    :cvar VALUE_1596_6:
    :cvar VALUE_1597_4:
    :cvar VALUE_1598_2:
    :cvar VALUE_1599_0:
    :cvar VALUE_1600_6:
    """
    VALUE_1586_7 = "1586-7"
    VALUE_1587_5 = "1587-5"
    VALUE_1588_3 = "1588-3"
    VALUE_1589_1 = "1589-1"
    VALUE_1590_9 = "1590-9"
    VALUE_1591_7 = "1591-7"
    VALUE_1592_5 = "1592-5"
    VALUE_1593_3 = "1593-3"
    VALUE_1594_1 = "1594-1"
    VALUE_1595_8 = "1595-8"
    VALUE_1596_6 = "1596-6"
    VALUE_1597_4 = "1597-4"
    VALUE_1598_2 = "1598-2"
    VALUE_1599_0 = "1599-0"
    VALUE_1600_6 = "1600-6"


class RaceAmericanIndianShoshonePaiute(Enum):
    """
    specDomain: S15371 (C-0-T14914-S14915-S14916-S15371-cpt)
    :cvar VALUE_1602_2:
    :cvar VALUE_1603_0:
    :cvar VALUE_1604_8:
    :cvar VALUE_1605_5:
    """
    VALUE_1602_2 = "1602-2"
    VALUE_1603_0 = "1603-0"
    VALUE_1604_8 = "1604-8"
    VALUE_1605_5 = "1605-5"


class RaceAmericanIndianSioux(Enum):
    """
    specDomain: S15376 (C-0-T14914-S14915-S14916-S15376-cpt)
    :cvar VALUE_1609_7:
    :cvar VALUE_1610_5:
    :cvar VALUE_1611_3:
    :cvar VALUE_1612_1:
    :cvar VALUE_1613_9:
    :cvar VALUE_1614_7:
    :cvar VALUE_1615_4:
    :cvar VALUE_1616_2:
    :cvar VALUE_1617_0:
    :cvar VALUE_1618_8:
    :cvar VALUE_1619_6:
    :cvar VALUE_1620_4:
    :cvar VALUE_1621_2:
    :cvar VALUE_1622_0:
    :cvar VALUE_1623_8:
    :cvar VALUE_1624_6:
    :cvar VALUE_1625_3:
    :cvar VALUE_1626_1:
    :cvar VALUE_1627_9:
    :cvar VALUE_1628_7:
    :cvar VALUE_1629_5:
    :cvar VALUE_1631_1:
    :cvar VALUE_1630_3:
    :cvar VALUE_1632_9:
    :cvar VALUE_1633_7:
    :cvar VALUE_1634_5:
    :cvar VALUE_1635_2:
    :cvar VALUE_1636_0:
    :cvar VALUE_1637_8:
    :cvar VALUE_1638_6:
    :cvar VALUE_1639_4:
    :cvar VALUE_1640_2:
    :cvar VALUE_1641_0:
    """
    VALUE_1609_7 = "1609-7"
    VALUE_1610_5 = "1610-5"
    VALUE_1611_3 = "1611-3"
    VALUE_1612_1 = "1612-1"
    VALUE_1613_9 = "1613-9"
    VALUE_1614_7 = "1614-7"
    VALUE_1615_4 = "1615-4"
    VALUE_1616_2 = "1616-2"
    VALUE_1617_0 = "1617-0"
    VALUE_1618_8 = "1618-8"
    VALUE_1619_6 = "1619-6"
    VALUE_1620_4 = "1620-4"
    VALUE_1621_2 = "1621-2"
    VALUE_1622_0 = "1622-0"
    VALUE_1623_8 = "1623-8"
    VALUE_1624_6 = "1624-6"
    VALUE_1625_3 = "1625-3"
    VALUE_1626_1 = "1626-1"
    VALUE_1627_9 = "1627-9"
    VALUE_1628_7 = "1628-7"
    VALUE_1629_5 = "1629-5"
    VALUE_1631_1 = "1631-1"
    VALUE_1630_3 = "1630-3"
    VALUE_1632_9 = "1632-9"
    VALUE_1633_7 = "1633-7"
    VALUE_1634_5 = "1634-5"
    VALUE_1635_2 = "1635-2"
    VALUE_1636_0 = "1636-0"
    VALUE_1637_8 = "1637-8"
    VALUE_1638_6 = "1638-6"
    VALUE_1639_4 = "1639-4"
    VALUE_1640_2 = "1640-2"
    VALUE_1641_0 = "1641-0"


class RaceAmericanIndianTohonoOodham(Enum):
    """
    specDomain: S15414 (C-0-T14914-S14915-S14916-S15414-cpt)
    :cvar VALUE_1653_5:
    :cvar VALUE_1654_3:
    :cvar VALUE_1655_0:
    :cvar VALUE_1656_8:
    :cvar VALUE_1657_6:
    """
    VALUE_1653_5 = "1653-5"
    VALUE_1654_3 = "1654-3"
    VALUE_1655_0 = "1655-0"
    VALUE_1656_8 = "1656-8"
    VALUE_1657_6 = "1657-6"


class RaceAmericanIndianUmpqua(Enum):
    """
    specDomain: S15423 (C-0-T14914-S14915-S14916-S15423-cpt)
    :cvar VALUE_1667_5:
    :cvar VALUE_1668_3:
    """
    VALUE_1667_5 = "1667-5"
    VALUE_1668_3 = "1668-3"


class RaceAmericanIndianUte(Enum):
    """
    specDomain: S15425 (C-0-T14914-S14915-S14916-S15425-cpt)
    :cvar VALUE_1670_9:
    :cvar VALUE_1671_7:
    :cvar VALUE_1672_5:
    :cvar VALUE_1673_3:
    """
    VALUE_1670_9 = "1670-9"
    VALUE_1671_7 = "1671-7"
    VALUE_1672_5 = "1672-5"
    VALUE_1673_3 = "1673-3"


class RaceAmericanIndianWampanoag(Enum):
    """
    specDomain: S15431 (C-0-T14914-S14915-S14916-S15431-cpt)
    :cvar VALUE_1679_0:
    :cvar VALUE_1680_8:
    :cvar VALUE_1681_6:
    """
    VALUE_1679_0 = "1679-0"
    VALUE_1680_8 = "1680-8"
    VALUE_1681_6 = "1681-6"


class RaceAmericanIndianWashoe(Enum):
    """
    specDomain: S15436 (C-0-T14914-S14915-S14916-S15436-cpt)
    :cvar VALUE_1687_3:
    :cvar VALUE_1688_1:
    :cvar VALUE_1689_9:
    :cvar VALUE_1690_7:
    """
    VALUE_1687_3 = "1687-3"
    VALUE_1688_1 = "1688-1"
    VALUE_1689_9 = "1689-9"
    VALUE_1690_7 = "1690-7"


class RaceAmericanIndianWinnebago(Enum):
    """
    specDomain: S15442 (C-0-T14914-S14915-S14916-S15442-cpt)
    :cvar VALUE_1696_4:
    :cvar VALUE_1697_2:
    :cvar VALUE_1698_0:
    """
    VALUE_1696_4 = "1696-4"
    VALUE_1697_2 = "1697-2"
    VALUE_1698_0 = "1698-0"


class RaceAmericanIndianYuman(Enum):
    """
    specDomain: S15460 (C-0-T14914-S14915-S14916-S15460-cpt)
    :cvar VALUE_1724_4:
    :cvar VALUE_1725_1:
    :cvar VALUE_1726_9:
    :cvar VALUE_1727_7:
    :cvar VALUE_1728_5:
    :cvar VALUE_1729_3:
    :cvar VALUE_1730_1:
    :cvar VALUE_1731_9:
    """
    VALUE_1724_4 = "1724-4"
    VALUE_1725_1 = "1725-1"
    VALUE_1726_9 = "1726-9"
    VALUE_1727_7 = "1727-7"
    VALUE_1728_5 = "1728-5"
    VALUE_1729_3 = "1729-3"
    VALUE_1730_1 = "1730-1"
    VALUE_1731_9 = "1731-9"


class RaceAmericanIndianYurok(Enum):
    """
    specDomain: S15468 (C-0-T14914-S14915-S14916-S15468-cpt)
    :cvar VALUE_1732_7:
    :cvar VALUE_1733_5:
    """
    VALUE_1732_7 = "1732-7"
    VALUE_1733_5 = "1733-5"


class RaceAsian(Enum):
    """
    specDomain: S15743 (C-0-T14914-S15743-cpt)
    :cvar VALUE_2028_9:
    :cvar VALUE_2029_7:
    :cvar VALUE_2030_5:
    :cvar VALUE_2031_3:
    :cvar VALUE_2032_1:
    :cvar VALUE_2033_9:
    :cvar VALUE_2034_7:
    :cvar VALUE_2036_2:
    :cvar VALUE_2037_0:
    :cvar VALUE_2038_8:
    :cvar VALUE_2048_7:
    :cvar VALUE_2039_6:
    :cvar VALUE_2040_4:
    :cvar VALUE_2041_2:
    :cvar VALUE_2052_9:
    :cvar VALUE_2042_0:
    :cvar VALUE_2049_5:
    :cvar VALUE_2050_3:
    :cvar VALUE_2043_8:
    :cvar VALUE_2044_6:
    :cvar VALUE_2051_1:
    :cvar VALUE_2045_3:
    :cvar VALUE_2035_4:
    :cvar VALUE_2046_1:
    :cvar VALUE_2047_9:
    """
    VALUE_2028_9 = "2028-9"
    VALUE_2029_7 = "2029-7"
    VALUE_2030_5 = "2030-5"
    VALUE_2031_3 = "2031-3"
    VALUE_2032_1 = "2032-1"
    VALUE_2033_9 = "2033-9"
    VALUE_2034_7 = "2034-7"
    VALUE_2036_2 = "2036-2"
    VALUE_2037_0 = "2037-0"
    VALUE_2038_8 = "2038-8"
    VALUE_2048_7 = "2048-7"
    VALUE_2039_6 = "2039-6"
    VALUE_2040_4 = "2040-4"
    VALUE_2041_2 = "2041-2"
    VALUE_2052_9 = "2052-9"
    VALUE_2042_0 = "2042-0"
    VALUE_2049_5 = "2049-5"
    VALUE_2050_3 = "2050-3"
    VALUE_2043_8 = "2043-8"
    VALUE_2044_6 = "2044-6"
    VALUE_2051_1 = "2051-1"
    VALUE_2045_3 = "2045-3"
    VALUE_2035_4 = "2035-4"
    VALUE_2046_1 = "2046-1"
    VALUE_2047_9 = "2047-9"


class RaceBlackOrAfricanAmerican(Enum):
    """
    specDomain: S15768 (C-0-T14914-S15768-cpt)
    :cvar VALUE_2060_2:
    :cvar VALUE_2061_0:
    :cvar VALUE_2062_8:
    :cvar VALUE_2063_6:
    :cvar VALUE_2064_4:
    :cvar VALUE_2065_1:
    :cvar VALUE_2066_9:
    :cvar VALUE_2054_5:
    :cvar VALUE_2058_6:
    :cvar VALUE_2067_7:
    :cvar VALUE_2068_5:
    :cvar VALUE_2056_0:
    :cvar VALUE_2070_1:
    :cvar VALUE_2069_3:
    :cvar VALUE_2071_9:
    :cvar VALUE_2072_7:
    :cvar VALUE_2073_5:
    :cvar VALUE_2074_3:
    :cvar VALUE_2075_0:
    """
    VALUE_2060_2 = "2060-2"
    VALUE_2061_0 = "2061-0"
    VALUE_2062_8 = "2062-8"
    VALUE_2063_6 = "2063-6"
    VALUE_2064_4 = "2064-4"
    VALUE_2065_1 = "2065-1"
    VALUE_2066_9 = "2066-9"
    VALUE_2054_5 = "2054-5"
    VALUE_2058_6 = "2058-6"
    VALUE_2067_7 = "2067-7"
    VALUE_2068_5 = "2068-5"
    VALUE_2056_0 = "2056-0"
    VALUE_2070_1 = "2070-1"
    VALUE_2069_3 = "2069-3"
    VALUE_2071_9 = "2071-9"
    VALUE_2072_7 = "2072-7"
    VALUE_2073_5 = "2073-5"
    VALUE_2074_3 = "2074-3"
    VALUE_2075_0 = "2075-0"


class RaceCanadianLatinIndian(Enum):
    """
    specDomain: S14965 (C-0-T14914-S14915-S14916-S14965-cpt)
    :cvar VALUE_1068_6:
    :cvar VALUE_1069_4:
    :cvar VALUE_1070_2:
    :cvar VALUE_1071_0:
    :cvar VALUE_1072_8:
    :cvar VALUE_1073_6:
    """
    VALUE_1068_6 = "1068-6"
    VALUE_1069_4 = "1069-4"
    VALUE_1070_2 = "1070-2"
    VALUE_1071_0 = "1071-0"
    VALUE_1072_8 = "1072-8"
    VALUE_1073_6 = "1073-6"


class RaceHawaiianOrPacificIsland(Enum):
    """
    specDomain: S15787 (C-0-T14914-S15787-cpt)
    :cvar VALUE_2100_6:
    :cvar VALUE_2101_4:
    :cvar VALUE_2104_8:
    :cvar VALUE_2102_2:
    :cvar VALUE_2103_0:
    :cvar VALUE_2085_9:
    :cvar VALUE_2092_5:
    :cvar VALUE_2088_3:
    :cvar VALUE_2097_4:
    :cvar VALUE_2087_5:
    :cvar VALUE_2086_7:
    :cvar VALUE_2096_6:
    :cvar VALUE_2093_3:
    :cvar VALUE_2089_1:
    :cvar VALUE_2090_9:
    :cvar VALUE_2091_7:
    :cvar VALUE_2094_1:
    :cvar VALUE_2095_8:
    :cvar VALUE_2098_2:
    :cvar VALUE_2078_4:
    :cvar VALUE_2079_2:
    :cvar VALUE_2080_0:
    :cvar VALUE_2081_8:
    :cvar VALUE_2083_4:
    :cvar VALUE_2082_6:
    :cvar VALUE_2076_8:
    :cvar VALUE_2500_7:
    """
    VALUE_2100_6 = "2100-6"
    VALUE_2101_4 = "2101-4"
    VALUE_2104_8 = "2104-8"
    VALUE_2102_2 = "2102-2"
    VALUE_2103_0 = "2103-0"
    VALUE_2085_9 = "2085-9"
    VALUE_2092_5 = "2092-5"
    VALUE_2088_3 = "2088-3"
    VALUE_2097_4 = "2097-4"
    VALUE_2087_5 = "2087-5"
    VALUE_2086_7 = "2086-7"
    VALUE_2096_6 = "2096-6"
    VALUE_2093_3 = "2093-3"
    VALUE_2089_1 = "2089-1"
    VALUE_2090_9 = "2090-9"
    VALUE_2091_7 = "2091-7"
    VALUE_2094_1 = "2094-1"
    VALUE_2095_8 = "2095-8"
    VALUE_2098_2 = "2098-2"
    VALUE_2078_4 = "2078-4"
    VALUE_2079_2 = "2079-2"
    VALUE_2080_0 = "2080-0"
    VALUE_2081_8 = "2081-8"
    VALUE_2083_4 = "2083-4"
    VALUE_2082_6 = "2082-6"
    VALUE_2076_8 = "2076-8"
    VALUE_2500_7 = "2500-7"


class RaceNativeAmerican(Enum):
    """
    specDomain: S14915 (C-0-T14914-S14915-cpt)
    :cvar VALUE_1739_2:
    :cvar VALUE_1740_0:
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    :cvar VALUE_1811_9:
    :cvar VALUE_1737_6:
    :cvar VALUE_1968_7:
    :cvar VALUE_1969_5:
    :cvar VALUE_1970_3:
    :cvar VALUE_1972_9:
    :cvar VALUE_1973_7:
    :cvar VALUE_1974_5:
    :cvar VALUE_1975_2:
    :cvar VALUE_1976_0:
    :cvar VALUE_1977_8:
    :cvar VALUE_1978_6:
    :cvar VALUE_1979_4:
    :cvar VALUE_1980_2:
    :cvar VALUE_1981_0:
    :cvar VALUE_1982_8:
    :cvar VALUE_1984_4:
    :cvar VALUE_1985_1:
    :cvar VALUE_1986_9:
    :cvar VALUE_1987_7:
    :cvar VALUE_1988_5:
    :cvar VALUE_1992_7:
    :cvar VALUE_1994_3:
    :cvar VALUE_1993_5:
    :cvar VALUE_1995_0:
    :cvar VALUE_1996_8:
    :cvar VALUE_1997_6:
    :cvar VALUE_1998_4:
    :cvar VALUE_1999_2:
    :cvar VALUE_2000_8:
    :cvar VALUE_2006_5:
    :cvar VALUE_2007_3:
    :cvar VALUE_2008_1:
    :cvar VALUE_2009_9:
    :cvar VALUE_2010_7:
    :cvar VALUE_2011_5:
    :cvar VALUE_2012_3:
    :cvar VALUE_2013_1:
    :cvar VALUE_2015_6:
    :cvar VALUE_2014_9:
    :cvar VALUE_2016_4:
    :cvar VALUE_2017_2:
    :cvar VALUE_2018_0:
    :cvar VALUE_2019_8:
    :cvar VALUE_2020_6:
    :cvar VALUE_2023_0:
    :cvar VALUE_2024_8:
    :cvar VALUE_2021_4:
    :cvar VALUE_2022_2:
    :cvar VALUE_2025_5:
    :cvar VALUE_2026_3:
    :cvar VALUE_1966_1:
    :cvar VALUE_1990_1:
    :cvar VALUE_2002_4:
    :cvar VALUE_2004_0:
    :cvar VALUE_1844_0:
    :cvar VALUE_1845_7:
    :cvar VALUE_1846_5:
    :cvar VALUE_1847_3:
    :cvar VALUE_1849_9:
    :cvar VALUE_1848_1:
    :cvar VALUE_1850_7:
    :cvar VALUE_1851_5:
    :cvar VALUE_1852_3:
    :cvar VALUE_1853_1:
    :cvar VALUE_1854_9:
    :cvar VALUE_1855_6:
    :cvar VALUE_1856_4:
    :cvar VALUE_1857_2:
    :cvar VALUE_1858_0:
    :cvar VALUE_1859_8:
    :cvar VALUE_1860_6:
    :cvar VALUE_1861_4:
    :cvar VALUE_1862_2:
    :cvar VALUE_1863_0:
    :cvar VALUE_1864_8:
    :cvar VALUE_1865_5:
    :cvar VALUE_1866_3:
    :cvar VALUE_1867_1:
    :cvar VALUE_1868_9:
    :cvar VALUE_1869_7:
    :cvar VALUE_1889_5:
    :cvar VALUE_1870_5:
    :cvar VALUE_1871_3:
    :cvar VALUE_1872_1:
    :cvar VALUE_1873_9:
    :cvar VALUE_1874_7:
    :cvar VALUE_1875_4:
    :cvar VALUE_1876_2:
    :cvar VALUE_1877_0:
    :cvar VALUE_1878_8:
    :cvar VALUE_1879_6:
    :cvar VALUE_1880_4:
    :cvar VALUE_1881_2:
    :cvar VALUE_1882_0:
    :cvar VALUE_1883_8:
    :cvar VALUE_1884_6:
    :cvar VALUE_1885_3:
    :cvar VALUE_1886_1:
    :cvar VALUE_1887_9:
    :cvar VALUE_1888_7:
    :cvar VALUE_1891_1:
    :cvar VALUE_1892_9:
    :cvar VALUE_1893_7:
    :cvar VALUE_1894_5:
    :cvar VALUE_1896_0:
    :cvar VALUE_1897_8:
    :cvar VALUE_1898_6:
    :cvar VALUE_1899_4:
    :cvar VALUE_1900_0:
    :cvar VALUE_1901_8:
    :cvar VALUE_1902_6:
    :cvar VALUE_1903_4:
    :cvar VALUE_1904_2:
    :cvar VALUE_1905_9:
    :cvar VALUE_1906_7:
    :cvar VALUE_1907_5:
    :cvar VALUE_1908_3:
    :cvar VALUE_1909_1:
    :cvar VALUE_1910_9:
    :cvar VALUE_1911_7:
    :cvar VALUE_1912_5:
    :cvar VALUE_1913_3:
    :cvar VALUE_1914_1:
    :cvar VALUE_1915_8:
    :cvar VALUE_1916_6:
    :cvar VALUE_1917_4:
    :cvar VALUE_1962_0:
    :cvar VALUE_1918_2:
    :cvar VALUE_1919_0:
    :cvar VALUE_1920_8:
    :cvar VALUE_1921_6:
    :cvar VALUE_1922_4:
    :cvar VALUE_1923_2:
    :cvar VALUE_1924_0:
    :cvar VALUE_1925_7:
    :cvar VALUE_1926_5:
    :cvar VALUE_1927_3:
    :cvar VALUE_1928_1:
    :cvar VALUE_1929_9:
    :cvar VALUE_1930_7:
    :cvar VALUE_1931_5:
    :cvar VALUE_1932_3:
    :cvar VALUE_1933_1:
    :cvar VALUE_1934_9:
    :cvar VALUE_1935_6:
    :cvar VALUE_1937_2:
    :cvar VALUE_1938_0:
    :cvar VALUE_1936_4:
    :cvar VALUE_1940_6:
    :cvar VALUE_1939_8:
    :cvar VALUE_1941_4:
    :cvar VALUE_1942_2:
    :cvar VALUE_1943_0:
    :cvar VALUE_1944_8:
    :cvar VALUE_1945_5:
    :cvar VALUE_1946_3:
    :cvar VALUE_1947_1:
    :cvar VALUE_1948_9:
    :cvar VALUE_1949_7:
    :cvar VALUE_1950_5:
    :cvar VALUE_1952_1:
    :cvar VALUE_1953_9:
    :cvar VALUE_1954_7:
    :cvar VALUE_1963_8:
    :cvar VALUE_1951_3:
    :cvar VALUE_1955_4:
    :cvar VALUE_1956_2:
    :cvar VALUE_1957_0:
    :cvar VALUE_1958_8:
    :cvar VALUE_1959_6:
    :cvar VALUE_1960_4:
    :cvar VALUE_1961_2:
    :cvar VALUE_1964_6:
    :cvar VALUE_1840_8:
    :cvar VALUE_1842_4:
    :cvar VALUE_1735_0:
    :cvar VALUE_1076_9:
    :cvar VALUE_1744_2:
    :cvar VALUE_1741_8:
    :cvar VALUE_1742_6:
    :cvar VALUE_1743_4:
    :cvar VALUE_1745_9:
    :cvar VALUE_1746_7:
    :cvar VALUE_1747_5:
    :cvar VALUE_1748_3:
    :cvar VALUE_1749_1:
    :cvar VALUE_1750_9:
    :cvar VALUE_1751_7:
    :cvar VALUE_1752_5:
    :cvar VALUE_1753_3:
    :cvar VALUE_1754_1:
    :cvar VALUE_1755_8:
    :cvar VALUE_1756_6:
    :cvar VALUE_1757_4:
    :cvar VALUE_1758_2:
    :cvar VALUE_1759_0:
    :cvar VALUE_1760_8:
    :cvar VALUE_1761_6:
    :cvar VALUE_1762_4:
    :cvar VALUE_1763_2:
    :cvar VALUE_1764_0:
    :cvar VALUE_1765_7:
    :cvar VALUE_1766_5:
    :cvar VALUE_1767_3:
    :cvar VALUE_1768_1:
    :cvar VALUE_1769_9:
    :cvar VALUE_1770_7:
    :cvar VALUE_1771_5:
    :cvar VALUE_1772_3:
    :cvar VALUE_1773_1:
    :cvar VALUE_1774_9:
    :cvar VALUE_1775_6:
    :cvar VALUE_1776_4:
    :cvar VALUE_1777_2:
    :cvar VALUE_1778_0:
    :cvar VALUE_1780_6:
    :cvar VALUE_1779_8:
    :cvar VALUE_1781_4:
    :cvar VALUE_1782_2:
    :cvar VALUE_1783_0:
    :cvar VALUE_1784_8:
    :cvar VALUE_1785_5:
    :cvar VALUE_1786_3:
    :cvar VALUE_1787_1:
    :cvar VALUE_1788_9:
    :cvar VALUE_1789_7:
    :cvar VALUE_1790_5:
    :cvar VALUE_1791_3:
    :cvar VALUE_1792_1:
    :cvar VALUE_1793_9:
    :cvar VALUE_1795_4:
    :cvar VALUE_1794_7:
    :cvar VALUE_1796_2:
    :cvar VALUE_1797_0:
    :cvar VALUE_1798_8:
    :cvar VALUE_1799_6:
    :cvar VALUE_1800_2:
    :cvar VALUE_1801_0:
    :cvar VALUE_1802_8:
    :cvar VALUE_1803_6:
    :cvar VALUE_1804_4:
    :cvar VALUE_1805_1:
    :cvar VALUE_1806_9:
    :cvar VALUE_1807_7:
    :cvar VALUE_1808_5:
    :cvar VALUE_1809_3:
    :cvar VALUE_1010_8:
    :cvar VALUE_1011_6:
    :cvar VALUE_1012_4:
    :cvar VALUE_1013_2:
    :cvar VALUE_1014_0:
    :cvar VALUE_1015_7:
    :cvar VALUE_1016_5:
    :cvar VALUE_1017_3:
    :cvar VALUE_1018_1:
    :cvar VALUE_1019_9:
    :cvar VALUE_1021_5:
    :cvar VALUE_1022_3:
    :cvar VALUE_1023_1:
    :cvar VALUE_1024_9:
    :cvar VALUE_1030_6:
    :cvar VALUE_1031_4:
    :cvar VALUE_1041_3:
    :cvar VALUE_1042_1:
    :cvar VALUE_1044_7:
    :cvar VALUE_1045_4:
    :cvar VALUE_1046_2:
    :cvar VALUE_1047_0:
    :cvar VALUE_1048_8:
    :cvar VALUE_1049_6:
    :cvar VALUE_1050_4:
    :cvar VALUE_1051_2:
    :cvar VALUE_1053_8:
    :cvar VALUE_1054_6:
    :cvar VALUE_1055_3:
    :cvar VALUE_1056_1:
    :cvar VALUE_1057_9:
    :cvar VALUE_1058_7:
    :cvar VALUE_1059_5:
    :cvar VALUE_1060_3:
    :cvar VALUE_1061_1:
    :cvar VALUE_1062_9:
    :cvar VALUE_1063_7:
    :cvar VALUE_1064_5:
    :cvar VALUE_1065_2:
    :cvar VALUE_1066_0:
    :cvar VALUE_1082_7:
    :cvar VALUE_1083_5:
    :cvar VALUE_1084_3:
    :cvar VALUE_1088_4:
    :cvar VALUE_1089_2:
    :cvar VALUE_1090_0:
    :cvar VALUE_1091_8:
    :cvar VALUE_1092_6:
    :cvar VALUE_1093_4:
    :cvar VALUE_1094_2:
    :cvar VALUE_1095_9:
    :cvar VALUE_1096_7:
    :cvar VALUE_1097_5:
    :cvar VALUE_1098_3:
    :cvar VALUE_1102_3:
    :cvar VALUE_1103_1:
    :cvar VALUE_1104_9:
    :cvar VALUE_1108_0:
    :cvar VALUE_1109_8:
    :cvar VALUE_1110_6:
    :cvar VALUE_1114_8:
    :cvar VALUE_1115_5:
    :cvar VALUE_1116_3:
    :cvar VALUE_1117_1:
    :cvar VALUE_1118_9:
    :cvar VALUE_1119_7:
    :cvar VALUE_1120_5:
    :cvar VALUE_1121_3:
    :cvar VALUE_1123_9:
    :cvar VALUE_1124_7:
    :cvar VALUE_1125_4:
    :cvar VALUE_1126_2:
    :cvar VALUE_1127_0:
    :cvar VALUE_1128_8:
    :cvar VALUE_1129_6:
    :cvar VALUE_1130_4:
    :cvar VALUE_1131_2:
    :cvar VALUE_1132_0:
    :cvar VALUE_1134_6:
    :cvar VALUE_1133_8:
    :cvar VALUE_1135_3:
    :cvar VALUE_1136_1:
    :cvar VALUE_1137_9:
    :cvar VALUE_1138_7:
    :cvar VALUE_1139_5:
    :cvar VALUE_1140_3:
    :cvar VALUE_1141_1:
    :cvar VALUE_1142_9:
    :cvar VALUE_1143_7:
    :cvar VALUE_1145_2:
    :cvar VALUE_1146_0:
    :cvar VALUE_1144_5:
    :cvar VALUE_1147_8:
    :cvar VALUE_1148_6:
    :cvar VALUE_1150_2:
    :cvar VALUE_1151_0:
    :cvar VALUE_1155_1:
    :cvar VALUE_1156_9:
    :cvar VALUE_1157_7:
    :cvar VALUE_1158_5:
    :cvar VALUE_1159_3:
    :cvar VALUE_1160_1:
    :cvar VALUE_1162_7:
    :cvar VALUE_1163_5:
    :cvar VALUE_1175_9:
    :cvar VALUE_1176_7:
    :cvar VALUE_1186_6:
    :cvar VALUE_1187_4:
    :cvar VALUE_1193_2:
    :cvar VALUE_1194_0:
    :cvar VALUE_1195_7:
    :cvar VALUE_1196_5:
    :cvar VALUE_1197_3:
    :cvar VALUE_1198_1:
    :cvar VALUE_1199_9:
    :cvar VALUE_1200_5:
    :cvar VALUE_1201_3:
    :cvar VALUE_1202_1:
    :cvar VALUE_1203_9:
    :cvar VALUE_1204_7:
    :cvar VALUE_1205_4:
    :cvar VALUE_1211_2:
    :cvar VALUE_1212_0:
    :cvar VALUE_1214_6:
    :cvar VALUE_1215_3:
    :cvar VALUE_1216_1:
    :cvar VALUE_1217_9:
    :cvar VALUE_1218_7:
    :cvar VALUE_1219_5:
    :cvar VALUE_1220_3:
    :cvar VALUE_1222_9:
    :cvar VALUE_1223_7:
    :cvar VALUE_1224_5:
    :cvar VALUE_1225_2:
    :cvar VALUE_1226_0:
    :cvar VALUE_1227_8:
    :cvar VALUE_1228_6:
    :cvar VALUE_1229_4:
    :cvar VALUE_1230_2:
    :cvar VALUE_1231_0:
    :cvar VALUE_1233_6:
    :cvar VALUE_1234_4:
    :cvar VALUE_1235_1:
    :cvar VALUE_1236_9:
    :cvar VALUE_1237_7:
    :cvar VALUE_1238_5:
    :cvar VALUE_1239_3:
    :cvar VALUE_1240_1:
    :cvar VALUE_1241_9:
    :cvar VALUE_1242_7:
    :cvar VALUE_1243_5:
    :cvar VALUE_1244_3:
    :cvar VALUE_1245_0:
    :cvar VALUE_1246_8:
    :cvar VALUE_1247_6:
    :cvar VALUE_1248_4:
    :cvar VALUE_1264_1:
    :cvar VALUE_1265_8:
    :cvar VALUE_1271_6:
    :cvar VALUE_1272_4:
    :cvar VALUE_1273_2:
    :cvar VALUE_1281_5:
    :cvar VALUE_1282_3:
    :cvar VALUE_1283_1:
    :cvar VALUE_1285_6:
    :cvar VALUE_1286_4:
    :cvar VALUE_1287_2:
    :cvar VALUE_1288_0:
    :cvar VALUE_1289_8:
    :cvar VALUE_1290_6:
    :cvar VALUE_1291_4:
    :cvar VALUE_1292_2:
    :cvar VALUE_1293_0:
    :cvar VALUE_1294_8:
    :cvar VALUE_1295_5:
    :cvar VALUE_1305_2:
    :cvar VALUE_1306_0:
    :cvar VALUE_1307_8:
    :cvar VALUE_1309_4:
    :cvar VALUE_1310_2:
    :cvar VALUE_1312_8:
    :cvar VALUE_1313_6:
    :cvar VALUE_1314_4:
    :cvar VALUE_1315_1:
    :cvar VALUE_1325_0:
    :cvar VALUE_1326_8:
    :cvar VALUE_1327_6:
    :cvar VALUE_1328_4:
    :cvar VALUE_1329_2:
    :cvar VALUE_1331_8:
    :cvar VALUE_1332_6:
    :cvar VALUE_1333_4:
    :cvar VALUE_1334_2:
    :cvar VALUE_1335_9:
    :cvar VALUE_1336_7:
    :cvar VALUE_1338_3:
    :cvar VALUE_1337_5:
    :cvar VALUE_1344_1:
    :cvar VALUE_1345_8:
    :cvar VALUE_1346_6:
    :cvar VALUE_1358_1:
    :cvar VALUE_1359_9:
    :cvar VALUE_1360_7:
    :cvar VALUE_1361_5:
    :cvar VALUE_1365_6:
    :cvar VALUE_1366_4:
    :cvar VALUE_1382_1:
    :cvar VALUE_1383_9:
    :cvar VALUE_1384_7:
    :cvar VALUE_1385_4:
    :cvar VALUE_1391_2:
    :cvar VALUE_1392_0:
    :cvar VALUE_1393_8:
    :cvar VALUE_1394_6:
    :cvar VALUE_1395_3:
    :cvar VALUE_1396_1:
    :cvar VALUE_1397_9:
    :cvar VALUE_1398_7:
    :cvar VALUE_1399_5:
    :cvar VALUE_1400_1:
    :cvar VALUE_1401_9:
    :cvar VALUE_1411_8:
    :cvar VALUE_1412_6:
    :cvar VALUE_1413_4:
    :cvar VALUE_1414_2:
    :cvar VALUE_1416_7:
    :cvar VALUE_1417_5:
    :cvar VALUE_1418_3:
    :cvar VALUE_1419_1:
    :cvar VALUE_1420_9:
    :cvar VALUE_1421_7:
    :cvar VALUE_1422_5:
    :cvar VALUE_1423_3:
    :cvar VALUE_1424_1:
    :cvar VALUE_1425_8:
    :cvar VALUE_1426_6:
    :cvar VALUE_1427_4:
    :cvar VALUE_1428_2:
    :cvar VALUE_1429_0:
    :cvar VALUE_1430_8:
    :cvar VALUE_1431_6:
    :cvar VALUE_1432_4:
    :cvar VALUE_1433_2:
    :cvar VALUE_1434_0:
    :cvar VALUE_1435_7:
    :cvar VALUE_1436_5:
    :cvar VALUE_1437_3:
    :cvar VALUE_1441_5:
    :cvar VALUE_1442_3:
    :cvar VALUE_1443_1:
    :cvar VALUE_1445_6:
    :cvar VALUE_1446_4:
    :cvar VALUE_1450_6:
    :cvar VALUE_1451_4:
    :cvar VALUE_1453_0:
    :cvar VALUE_1454_8:
    :cvar VALUE_1456_3:
    :cvar VALUE_1457_1:
    :cvar VALUE_1458_9:
    :cvar VALUE_1464_7:
    :cvar VALUE_1465_4:
    :cvar VALUE_1466_2:
    :cvar VALUE_1467_0:
    :cvar VALUE_1468_8:
    :cvar VALUE_1469_6:
    :cvar VALUE_1470_4:
    :cvar VALUE_1471_2:
    :cvar VALUE_1472_0:
    :cvar VALUE_1474_6:
    :cvar VALUE_1475_3:
    :cvar VALUE_1476_1:
    :cvar VALUE_1478_7:
    :cvar VALUE_1479_5:
    :cvar VALUE_1480_3:
    :cvar VALUE_1481_1:
    :cvar VALUE_1482_9:
    :cvar VALUE_1483_7:
    :cvar VALUE_1484_5:
    :cvar VALUE_1485_2:
    :cvar VALUE_1489_4:
    :cvar VALUE_1490_2:
    :cvar VALUE_1491_0:
    :cvar VALUE_1492_8:
    :cvar VALUE_1493_6:
    :cvar VALUE_1494_4:
    :cvar VALUE_1495_1:
    :cvar VALUE_1496_9:
    :cvar VALUE_1497_7:
    :cvar VALUE_1498_5:
    :cvar VALUE_1499_3:
    :cvar VALUE_1500_8:
    :cvar VALUE_1501_6:
    :cvar VALUE_1502_4:
    :cvar VALUE_1503_2:
    :cvar VALUE_1506_5:
    :cvar VALUE_1505_7:
    :cvar VALUE_1504_0:
    :cvar VALUE_1507_3:
    :cvar VALUE_1508_1:
    :cvar VALUE_1509_9:
    :cvar VALUE_1510_7:
    :cvar VALUE_1511_5:
    :cvar VALUE_1512_3:
    :cvar VALUE_1513_1:
    :cvar VALUE_1514_9:
    :cvar VALUE_1515_6:
    :cvar VALUE_1516_4:
    :cvar VALUE_1518_0:
    :cvar VALUE_1519_8:
    :cvar VALUE_1520_6:
    :cvar VALUE_1521_4:
    :cvar VALUE_1522_2:
    :cvar VALUE_1523_0:
    :cvar VALUE_1524_8:
    :cvar VALUE_1525_5:
    :cvar VALUE_1526_3:
    :cvar VALUE_1527_1:
    :cvar VALUE_1528_9:
    :cvar VALUE_1529_7:
    :cvar VALUE_1530_5:
    :cvar VALUE_1531_3:
    :cvar VALUE_1532_1:
    :cvar VALUE_1533_9:
    :cvar VALUE_1534_7:
    :cvar VALUE_1535_4:
    :cvar VALUE_1536_2:
    :cvar VALUE_1537_0:
    :cvar VALUE_1538_8:
    :cvar VALUE_1539_6:
    :cvar VALUE_1551_1:
    :cvar VALUE_1552_9:
    :cvar VALUE_1553_7:
    :cvar VALUE_1554_5:
    :cvar VALUE_1566_9:
    :cvar VALUE_1567_7:
    :cvar VALUE_1568_5:
    :cvar VALUE_1569_3:
    :cvar VALUE_1570_1:
    :cvar VALUE_1571_9:
    :cvar VALUE_1573_5:
    :cvar VALUE_1574_3:
    :cvar VALUE_1578_4:
    :cvar VALUE_1579_2:
    :cvar VALUE_1580_0:
    :cvar VALUE_1586_7:
    :cvar VALUE_1587_5:
    :cvar VALUE_1588_3:
    :cvar VALUE_1589_1:
    :cvar VALUE_1590_9:
    :cvar VALUE_1591_7:
    :cvar VALUE_1592_5:
    :cvar VALUE_1593_3:
    :cvar VALUE_1594_1:
    :cvar VALUE_1595_8:
    :cvar VALUE_1596_6:
    :cvar VALUE_1597_4:
    :cvar VALUE_1598_2:
    :cvar VALUE_1599_0:
    :cvar VALUE_1600_6:
    :cvar VALUE_1602_2:
    :cvar VALUE_1603_0:
    :cvar VALUE_1604_8:
    :cvar VALUE_1605_5:
    :cvar VALUE_1609_7:
    :cvar VALUE_1610_5:
    :cvar VALUE_1611_3:
    :cvar VALUE_1612_1:
    :cvar VALUE_1613_9:
    :cvar VALUE_1614_7:
    :cvar VALUE_1615_4:
    :cvar VALUE_1616_2:
    :cvar VALUE_1617_0:
    :cvar VALUE_1618_8:
    :cvar VALUE_1619_6:
    :cvar VALUE_1620_4:
    :cvar VALUE_1621_2:
    :cvar VALUE_1622_0:
    :cvar VALUE_1623_8:
    :cvar VALUE_1624_6:
    :cvar VALUE_1625_3:
    :cvar VALUE_1626_1:
    :cvar VALUE_1627_9:
    :cvar VALUE_1628_7:
    :cvar VALUE_1629_5:
    :cvar VALUE_1631_1:
    :cvar VALUE_1630_3:
    :cvar VALUE_1632_9:
    :cvar VALUE_1633_7:
    :cvar VALUE_1634_5:
    :cvar VALUE_1635_2:
    :cvar VALUE_1636_0:
    :cvar VALUE_1637_8:
    :cvar VALUE_1638_6:
    :cvar VALUE_1639_4:
    :cvar VALUE_1640_2:
    :cvar VALUE_1641_0:
    :cvar VALUE_1653_5:
    :cvar VALUE_1654_3:
    :cvar VALUE_1655_0:
    :cvar VALUE_1656_8:
    :cvar VALUE_1657_6:
    :cvar VALUE_1667_5:
    :cvar VALUE_1668_3:
    :cvar VALUE_1670_9:
    :cvar VALUE_1671_7:
    :cvar VALUE_1672_5:
    :cvar VALUE_1673_3:
    :cvar VALUE_1679_0:
    :cvar VALUE_1680_8:
    :cvar VALUE_1681_6:
    :cvar VALUE_1687_3:
    :cvar VALUE_1688_1:
    :cvar VALUE_1689_9:
    :cvar VALUE_1690_7:
    :cvar VALUE_1696_4:
    :cvar VALUE_1697_2:
    :cvar VALUE_1698_0:
    :cvar VALUE_1724_4:
    :cvar VALUE_1725_1:
    :cvar VALUE_1726_9:
    :cvar VALUE_1727_7:
    :cvar VALUE_1728_5:
    :cvar VALUE_1729_3:
    :cvar VALUE_1730_1:
    :cvar VALUE_1731_9:
    :cvar VALUE_1732_7:
    :cvar VALUE_1733_5:
    :cvar VALUE_1068_6:
    :cvar VALUE_1069_4:
    :cvar VALUE_1070_2:
    :cvar VALUE_1071_0:
    :cvar VALUE_1072_8:
    :cvar VALUE_1073_6:
    :cvar VALUE_1704_6:
    :cvar VALUE_1705_3:
    :cvar VALUE_1711_1:
    :cvar VALUE_1712_9:
    :cvar VALUE_1713_7:
    :cvar VALUE_1717_8:
    :cvar VALUE_1718_6:
    :cvar VALUE_1719_4:
    :cvar VALUE_1720_2:
    :cvar VALUE_1004_1:
    :cvar VALUE_1006_6:
    :cvar VALUE_1008_2:
    :cvar VALUE_1026_4:
    :cvar VALUE_1028_0:
    :cvar VALUE_1033_0:
    :cvar VALUE_1035_5:
    :cvar VALUE_1037_1:
    :cvar VALUE_1039_7:
    :cvar VALUE_1078_5:
    :cvar VALUE_1080_1:
    :cvar VALUE_1086_8:
    :cvar VALUE_1100_7:
    :cvar VALUE_1106_4:
    :cvar VALUE_1112_2:
    :cvar VALUE_1153_6:
    :cvar VALUE_1165_0:
    :cvar VALUE_1167_6:
    :cvar VALUE_1169_2:
    :cvar VALUE_1171_8:
    :cvar VALUE_1173_4:
    :cvar VALUE_1180_9:
    :cvar VALUE_1178_3:
    :cvar VALUE_1182_5:
    :cvar VALUE_1184_1:
    :cvar VALUE_1189_0:
    :cvar VALUE_1191_6:
    :cvar VALUE_1207_0:
    :cvar VALUE_1209_6:
    :cvar VALUE_1250_0:
    :cvar VALUE_1252_6:
    :cvar VALUE_1254_2:
    :cvar VALUE_1258_3:
    :cvar VALUE_1256_7:
    :cvar VALUE_1260_9:
    :cvar VALUE_1262_5:
    :cvar VALUE_1267_4:
    :cvar VALUE_1269_0:
    :cvar VALUE_1275_7:
    :cvar VALUE_1277_3:
    :cvar VALUE_1279_9:
    :cvar VALUE_1297_1:
    :cvar VALUE_1299_7:
    :cvar VALUE_1301_1:
    :cvar VALUE_1303_7:
    :cvar VALUE_1317_7:
    :cvar VALUE_1319_3:
    :cvar VALUE_1321_9:
    :cvar VALUE_1323_5:
    :cvar VALUE_1340_9:
    :cvar VALUE_1342_5:
    :cvar VALUE_1348_2:
    :cvar VALUE_1350_8:
    :cvar VALUE_1352_4:
    :cvar VALUE_1354_0:
    :cvar VALUE_1356_5:
    :cvar VALUE_1363_1:
    :cvar VALUE_1368_0:
    :cvar VALUE_1370_6:
    :cvar VALUE_1372_2:
    :cvar VALUE_1374_8:
    :cvar VALUE_1376_3:
    :cvar VALUE_1378_9:
    :cvar VALUE_1380_5:
    :cvar VALUE_1387_0:
    :cvar VALUE_1389_6:
    :cvar VALUE_1403_5:
    :cvar VALUE_1405_0:
    :cvar VALUE_1407_6:
    :cvar VALUE_1409_2:
    :cvar VALUE_1439_9:
    :cvar VALUE_1448_0:
    :cvar VALUE_1460_5:
    :cvar VALUE_1462_1:
    :cvar VALUE_1487_8:
    :cvar VALUE_1541_2:
    :cvar VALUE_1543_8:
    :cvar VALUE_1545_3:
    :cvar VALUE_1547_9:
    :cvar VALUE_1549_5:
    :cvar VALUE_1556_0:
    :cvar VALUE_1558_6:
    :cvar VALUE_1560_2:
    :cvar VALUE_1562_8:
    :cvar VALUE_1564_4:
    :cvar VALUE_1576_8:
    :cvar VALUE_1582_6:
    :cvar VALUE_1584_2:
    :cvar VALUE_1607_1:
    :cvar VALUE_1643_6:
    :cvar VALUE_1074_4:
    :cvar VALUE_1645_1:
    :cvar VALUE_1647_7:
    :cvar VALUE_1649_3:
    :cvar VALUE_1651_9:
    :cvar VALUE_1659_2:
    :cvar VALUE_1661_8:
    :cvar VALUE_1663_4:
    :cvar VALUE_1665_9:
    :cvar VALUE_1675_8:
    :cvar VALUE_1677_4:
    :cvar VALUE_1683_2:
    :cvar VALUE_1685_7:
    :cvar VALUE_1692_3:
    :cvar VALUE_1694_9:
    :cvar VALUE_1700_4:
    :cvar VALUE_1702_0:
    :cvar VALUE_1707_9:
    :cvar VALUE_1709_5:
    :cvar VALUE_1715_2:
    :cvar VALUE_1722_8:
    :cvar VALUE_1002_5:
    """
    VALUE_1739_2 = "1739-2"
    VALUE_1740_0 = "1740-0"
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"
    VALUE_1811_9 = "1811-9"
    VALUE_1737_6 = "1737-6"
    VALUE_1968_7 = "1968-7"
    VALUE_1969_5 = "1969-5"
    VALUE_1970_3 = "1970-3"
    VALUE_1972_9 = "1972-9"
    VALUE_1973_7 = "1973-7"
    VALUE_1974_5 = "1974-5"
    VALUE_1975_2 = "1975-2"
    VALUE_1976_0 = "1976-0"
    VALUE_1977_8 = "1977-8"
    VALUE_1978_6 = "1978-6"
    VALUE_1979_4 = "1979-4"
    VALUE_1980_2 = "1980-2"
    VALUE_1981_0 = "1981-0"
    VALUE_1982_8 = "1982-8"
    VALUE_1984_4 = "1984-4"
    VALUE_1985_1 = "1985-1"
    VALUE_1986_9 = "1986-9"
    VALUE_1987_7 = "1987-7"
    VALUE_1988_5 = "1988-5"
    VALUE_1992_7 = "1992-7"
    VALUE_1994_3 = "1994-3"
    VALUE_1993_5 = "1993-5"
    VALUE_1995_0 = "1995-0"
    VALUE_1996_8 = "1996-8"
    VALUE_1997_6 = "1997-6"
    VALUE_1998_4 = "1998-4"
    VALUE_1999_2 = "1999-2"
    VALUE_2000_8 = "2000-8"
    VALUE_2006_5 = "2006-5"
    VALUE_2007_3 = "2007-3"
    VALUE_2008_1 = "2008-1"
    VALUE_2009_9 = "2009-9"
    VALUE_2010_7 = "2010-7"
    VALUE_2011_5 = "2011-5"
    VALUE_2012_3 = "2012-3"
    VALUE_2013_1 = "2013-1"
    VALUE_2015_6 = "2015-6"
    VALUE_2014_9 = "2014-9"
    VALUE_2016_4 = "2016-4"
    VALUE_2017_2 = "2017-2"
    VALUE_2018_0 = "2018-0"
    VALUE_2019_8 = "2019-8"
    VALUE_2020_6 = "2020-6"
    VALUE_2023_0 = "2023-0"
    VALUE_2024_8 = "2024-8"
    VALUE_2021_4 = "2021-4"
    VALUE_2022_2 = "2022-2"
    VALUE_2025_5 = "2025-5"
    VALUE_2026_3 = "2026-3"
    VALUE_1966_1 = "1966-1"
    VALUE_1990_1 = "1990-1"
    VALUE_2002_4 = "2002-4"
    VALUE_2004_0 = "2004-0"
    VALUE_1844_0 = "1844-0"
    VALUE_1845_7 = "1845-7"
    VALUE_1846_5 = "1846-5"
    VALUE_1847_3 = "1847-3"
    VALUE_1849_9 = "1849-9"
    VALUE_1848_1 = "1848-1"
    VALUE_1850_7 = "1850-7"
    VALUE_1851_5 = "1851-5"
    VALUE_1852_3 = "1852-3"
    VALUE_1853_1 = "1853-1"
    VALUE_1854_9 = "1854-9"
    VALUE_1855_6 = "1855-6"
    VALUE_1856_4 = "1856-4"
    VALUE_1857_2 = "1857-2"
    VALUE_1858_0 = "1858-0"
    VALUE_1859_8 = "1859-8"
    VALUE_1860_6 = "1860-6"
    VALUE_1861_4 = "1861-4"
    VALUE_1862_2 = "1862-2"
    VALUE_1863_0 = "1863-0"
    VALUE_1864_8 = "1864-8"
    VALUE_1865_5 = "1865-5"
    VALUE_1866_3 = "1866-3"
    VALUE_1867_1 = "1867-1"
    VALUE_1868_9 = "1868-9"
    VALUE_1869_7 = "1869-7"
    VALUE_1889_5 = "1889-5"
    VALUE_1870_5 = "1870-5"
    VALUE_1871_3 = "1871-3"
    VALUE_1872_1 = "1872-1"
    VALUE_1873_9 = "1873-9"
    VALUE_1874_7 = "1874-7"
    VALUE_1875_4 = "1875-4"
    VALUE_1876_2 = "1876-2"
    VALUE_1877_0 = "1877-0"
    VALUE_1878_8 = "1878-8"
    VALUE_1879_6 = "1879-6"
    VALUE_1880_4 = "1880-4"
    VALUE_1881_2 = "1881-2"
    VALUE_1882_0 = "1882-0"
    VALUE_1883_8 = "1883-8"
    VALUE_1884_6 = "1884-6"
    VALUE_1885_3 = "1885-3"
    VALUE_1886_1 = "1886-1"
    VALUE_1887_9 = "1887-9"
    VALUE_1888_7 = "1888-7"
    VALUE_1891_1 = "1891-1"
    VALUE_1892_9 = "1892-9"
    VALUE_1893_7 = "1893-7"
    VALUE_1894_5 = "1894-5"
    VALUE_1896_0 = "1896-0"
    VALUE_1897_8 = "1897-8"
    VALUE_1898_6 = "1898-6"
    VALUE_1899_4 = "1899-4"
    VALUE_1900_0 = "1900-0"
    VALUE_1901_8 = "1901-8"
    VALUE_1902_6 = "1902-6"
    VALUE_1903_4 = "1903-4"
    VALUE_1904_2 = "1904-2"
    VALUE_1905_9 = "1905-9"
    VALUE_1906_7 = "1906-7"
    VALUE_1907_5 = "1907-5"
    VALUE_1908_3 = "1908-3"
    VALUE_1909_1 = "1909-1"
    VALUE_1910_9 = "1910-9"
    VALUE_1911_7 = "1911-7"
    VALUE_1912_5 = "1912-5"
    VALUE_1913_3 = "1913-3"
    VALUE_1914_1 = "1914-1"
    VALUE_1915_8 = "1915-8"
    VALUE_1916_6 = "1916-6"
    VALUE_1917_4 = "1917-4"
    VALUE_1962_0 = "1962-0"
    VALUE_1918_2 = "1918-2"
    VALUE_1919_0 = "1919-0"
    VALUE_1920_8 = "1920-8"
    VALUE_1921_6 = "1921-6"
    VALUE_1922_4 = "1922-4"
    VALUE_1923_2 = "1923-2"
    VALUE_1924_0 = "1924-0"
    VALUE_1925_7 = "1925-7"
    VALUE_1926_5 = "1926-5"
    VALUE_1927_3 = "1927-3"
    VALUE_1928_1 = "1928-1"
    VALUE_1929_9 = "1929-9"
    VALUE_1930_7 = "1930-7"
    VALUE_1931_5 = "1931-5"
    VALUE_1932_3 = "1932-3"
    VALUE_1933_1 = "1933-1"
    VALUE_1934_9 = "1934-9"
    VALUE_1935_6 = "1935-6"
    VALUE_1937_2 = "1937-2"
    VALUE_1938_0 = "1938-0"
    VALUE_1936_4 = "1936-4"
    VALUE_1940_6 = "1940-6"
    VALUE_1939_8 = "1939-8"
    VALUE_1941_4 = "1941-4"
    VALUE_1942_2 = "1942-2"
    VALUE_1943_0 = "1943-0"
    VALUE_1944_8 = "1944-8"
    VALUE_1945_5 = "1945-5"
    VALUE_1946_3 = "1946-3"
    VALUE_1947_1 = "1947-1"
    VALUE_1948_9 = "1948-9"
    VALUE_1949_7 = "1949-7"
    VALUE_1950_5 = "1950-5"
    VALUE_1952_1 = "1952-1"
    VALUE_1953_9 = "1953-9"
    VALUE_1954_7 = "1954-7"
    VALUE_1963_8 = "1963-8"
    VALUE_1951_3 = "1951-3"
    VALUE_1955_4 = "1955-4"
    VALUE_1956_2 = "1956-2"
    VALUE_1957_0 = "1957-0"
    VALUE_1958_8 = "1958-8"
    VALUE_1959_6 = "1959-6"
    VALUE_1960_4 = "1960-4"
    VALUE_1961_2 = "1961-2"
    VALUE_1964_6 = "1964-6"
    VALUE_1840_8 = "1840-8"
    VALUE_1842_4 = "1842-4"
    VALUE_1735_0 = "1735-0"
    VALUE_1076_9 = "1076-9"
    VALUE_1744_2 = "1744-2"
    VALUE_1741_8 = "1741-8"
    VALUE_1742_6 = "1742-6"
    VALUE_1743_4 = "1743-4"
    VALUE_1745_9 = "1745-9"
    VALUE_1746_7 = "1746-7"
    VALUE_1747_5 = "1747-5"
    VALUE_1748_3 = "1748-3"
    VALUE_1749_1 = "1749-1"
    VALUE_1750_9 = "1750-9"
    VALUE_1751_7 = "1751-7"
    VALUE_1752_5 = "1752-5"
    VALUE_1753_3 = "1753-3"
    VALUE_1754_1 = "1754-1"
    VALUE_1755_8 = "1755-8"
    VALUE_1756_6 = "1756-6"
    VALUE_1757_4 = "1757-4"
    VALUE_1758_2 = "1758-2"
    VALUE_1759_0 = "1759-0"
    VALUE_1760_8 = "1760-8"
    VALUE_1761_6 = "1761-6"
    VALUE_1762_4 = "1762-4"
    VALUE_1763_2 = "1763-2"
    VALUE_1764_0 = "1764-0"
    VALUE_1765_7 = "1765-7"
    VALUE_1766_5 = "1766-5"
    VALUE_1767_3 = "1767-3"
    VALUE_1768_1 = "1768-1"
    VALUE_1769_9 = "1769-9"
    VALUE_1770_7 = "1770-7"
    VALUE_1771_5 = "1771-5"
    VALUE_1772_3 = "1772-3"
    VALUE_1773_1 = "1773-1"
    VALUE_1774_9 = "1774-9"
    VALUE_1775_6 = "1775-6"
    VALUE_1776_4 = "1776-4"
    VALUE_1777_2 = "1777-2"
    VALUE_1778_0 = "1778-0"
    VALUE_1780_6 = "1780-6"
    VALUE_1779_8 = "1779-8"
    VALUE_1781_4 = "1781-4"
    VALUE_1782_2 = "1782-2"
    VALUE_1783_0 = "1783-0"
    VALUE_1784_8 = "1784-8"
    VALUE_1785_5 = "1785-5"
    VALUE_1786_3 = "1786-3"
    VALUE_1787_1 = "1787-1"
    VALUE_1788_9 = "1788-9"
    VALUE_1789_7 = "1789-7"
    VALUE_1790_5 = "1790-5"
    VALUE_1791_3 = "1791-3"
    VALUE_1792_1 = "1792-1"
    VALUE_1793_9 = "1793-9"
    VALUE_1795_4 = "1795-4"
    VALUE_1794_7 = "1794-7"
    VALUE_1796_2 = "1796-2"
    VALUE_1797_0 = "1797-0"
    VALUE_1798_8 = "1798-8"
    VALUE_1799_6 = "1799-6"
    VALUE_1800_2 = "1800-2"
    VALUE_1801_0 = "1801-0"
    VALUE_1802_8 = "1802-8"
    VALUE_1803_6 = "1803-6"
    VALUE_1804_4 = "1804-4"
    VALUE_1805_1 = "1805-1"
    VALUE_1806_9 = "1806-9"
    VALUE_1807_7 = "1807-7"
    VALUE_1808_5 = "1808-5"
    VALUE_1809_3 = "1809-3"
    VALUE_1010_8 = "1010-8"
    VALUE_1011_6 = "1011-6"
    VALUE_1012_4 = "1012-4"
    VALUE_1013_2 = "1013-2"
    VALUE_1014_0 = "1014-0"
    VALUE_1015_7 = "1015-7"
    VALUE_1016_5 = "1016-5"
    VALUE_1017_3 = "1017-3"
    VALUE_1018_1 = "1018-1"
    VALUE_1019_9 = "1019-9"
    VALUE_1021_5 = "1021-5"
    VALUE_1022_3 = "1022-3"
    VALUE_1023_1 = "1023-1"
    VALUE_1024_9 = "1024-9"
    VALUE_1030_6 = "1030-6"
    VALUE_1031_4 = "1031-4"
    VALUE_1041_3 = "1041-3"
    VALUE_1042_1 = "1042-1"
    VALUE_1044_7 = "1044-7"
    VALUE_1045_4 = "1045-4"
    VALUE_1046_2 = "1046-2"
    VALUE_1047_0 = "1047-0"
    VALUE_1048_8 = "1048-8"
    VALUE_1049_6 = "1049-6"
    VALUE_1050_4 = "1050-4"
    VALUE_1051_2 = "1051-2"
    VALUE_1053_8 = "1053-8"
    VALUE_1054_6 = "1054-6"
    VALUE_1055_3 = "1055-3"
    VALUE_1056_1 = "1056-1"
    VALUE_1057_9 = "1057-9"
    VALUE_1058_7 = "1058-7"
    VALUE_1059_5 = "1059-5"
    VALUE_1060_3 = "1060-3"
    VALUE_1061_1 = "1061-1"
    VALUE_1062_9 = "1062-9"
    VALUE_1063_7 = "1063-7"
    VALUE_1064_5 = "1064-5"
    VALUE_1065_2 = "1065-2"
    VALUE_1066_0 = "1066-0"
    VALUE_1082_7 = "1082-7"
    VALUE_1083_5 = "1083-5"
    VALUE_1084_3 = "1084-3"
    VALUE_1088_4 = "1088-4"
    VALUE_1089_2 = "1089-2"
    VALUE_1090_0 = "1090-0"
    VALUE_1091_8 = "1091-8"
    VALUE_1092_6 = "1092-6"
    VALUE_1093_4 = "1093-4"
    VALUE_1094_2 = "1094-2"
    VALUE_1095_9 = "1095-9"
    VALUE_1096_7 = "1096-7"
    VALUE_1097_5 = "1097-5"
    VALUE_1098_3 = "1098-3"
    VALUE_1102_3 = "1102-3"
    VALUE_1103_1 = "1103-1"
    VALUE_1104_9 = "1104-9"
    VALUE_1108_0 = "1108-0"
    VALUE_1109_8 = "1109-8"
    VALUE_1110_6 = "1110-6"
    VALUE_1114_8 = "1114-8"
    VALUE_1115_5 = "1115-5"
    VALUE_1116_3 = "1116-3"
    VALUE_1117_1 = "1117-1"
    VALUE_1118_9 = "1118-9"
    VALUE_1119_7 = "1119-7"
    VALUE_1120_5 = "1120-5"
    VALUE_1121_3 = "1121-3"
    VALUE_1123_9 = "1123-9"
    VALUE_1124_7 = "1124-7"
    VALUE_1125_4 = "1125-4"
    VALUE_1126_2 = "1126-2"
    VALUE_1127_0 = "1127-0"
    VALUE_1128_8 = "1128-8"
    VALUE_1129_6 = "1129-6"
    VALUE_1130_4 = "1130-4"
    VALUE_1131_2 = "1131-2"
    VALUE_1132_0 = "1132-0"
    VALUE_1134_6 = "1134-6"
    VALUE_1133_8 = "1133-8"
    VALUE_1135_3 = "1135-3"
    VALUE_1136_1 = "1136-1"
    VALUE_1137_9 = "1137-9"
    VALUE_1138_7 = "1138-7"
    VALUE_1139_5 = "1139-5"
    VALUE_1140_3 = "1140-3"
    VALUE_1141_1 = "1141-1"
    VALUE_1142_9 = "1142-9"
    VALUE_1143_7 = "1143-7"
    VALUE_1145_2 = "1145-2"
    VALUE_1146_0 = "1146-0"
    VALUE_1144_5 = "1144-5"
    VALUE_1147_8 = "1147-8"
    VALUE_1148_6 = "1148-6"
    VALUE_1150_2 = "1150-2"
    VALUE_1151_0 = "1151-0"
    VALUE_1155_1 = "1155-1"
    VALUE_1156_9 = "1156-9"
    VALUE_1157_7 = "1157-7"
    VALUE_1158_5 = "1158-5"
    VALUE_1159_3 = "1159-3"
    VALUE_1160_1 = "1160-1"
    VALUE_1162_7 = "1162-7"
    VALUE_1163_5 = "1163-5"
    VALUE_1175_9 = "1175-9"
    VALUE_1176_7 = "1176-7"
    VALUE_1186_6 = "1186-6"
    VALUE_1187_4 = "1187-4"
    VALUE_1193_2 = "1193-2"
    VALUE_1194_0 = "1194-0"
    VALUE_1195_7 = "1195-7"
    VALUE_1196_5 = "1196-5"
    VALUE_1197_3 = "1197-3"
    VALUE_1198_1 = "1198-1"
    VALUE_1199_9 = "1199-9"
    VALUE_1200_5 = "1200-5"
    VALUE_1201_3 = "1201-3"
    VALUE_1202_1 = "1202-1"
    VALUE_1203_9 = "1203-9"
    VALUE_1204_7 = "1204-7"
    VALUE_1205_4 = "1205-4"
    VALUE_1211_2 = "1211-2"
    VALUE_1212_0 = "1212-0"
    VALUE_1214_6 = "1214-6"
    VALUE_1215_3 = "1215-3"
    VALUE_1216_1 = "1216-1"
    VALUE_1217_9 = "1217-9"
    VALUE_1218_7 = "1218-7"
    VALUE_1219_5 = "1219-5"
    VALUE_1220_3 = "1220-3"
    VALUE_1222_9 = "1222-9"
    VALUE_1223_7 = "1223-7"
    VALUE_1224_5 = "1224-5"
    VALUE_1225_2 = "1225-2"
    VALUE_1226_0 = "1226-0"
    VALUE_1227_8 = "1227-8"
    VALUE_1228_6 = "1228-6"
    VALUE_1229_4 = "1229-4"
    VALUE_1230_2 = "1230-2"
    VALUE_1231_0 = "1231-0"
    VALUE_1233_6 = "1233-6"
    VALUE_1234_4 = "1234-4"
    VALUE_1235_1 = "1235-1"
    VALUE_1236_9 = "1236-9"
    VALUE_1237_7 = "1237-7"
    VALUE_1238_5 = "1238-5"
    VALUE_1239_3 = "1239-3"
    VALUE_1240_1 = "1240-1"
    VALUE_1241_9 = "1241-9"
    VALUE_1242_7 = "1242-7"
    VALUE_1243_5 = "1243-5"
    VALUE_1244_3 = "1244-3"
    VALUE_1245_0 = "1245-0"
    VALUE_1246_8 = "1246-8"
    VALUE_1247_6 = "1247-6"
    VALUE_1248_4 = "1248-4"
    VALUE_1264_1 = "1264-1"
    VALUE_1265_8 = "1265-8"
    VALUE_1271_6 = "1271-6"
    VALUE_1272_4 = "1272-4"
    VALUE_1273_2 = "1273-2"
    VALUE_1281_5 = "1281-5"
    VALUE_1282_3 = "1282-3"
    VALUE_1283_1 = "1283-1"
    VALUE_1285_6 = "1285-6"
    VALUE_1286_4 = "1286-4"
    VALUE_1287_2 = "1287-2"
    VALUE_1288_0 = "1288-0"
    VALUE_1289_8 = "1289-8"
    VALUE_1290_6 = "1290-6"
    VALUE_1291_4 = "1291-4"
    VALUE_1292_2 = "1292-2"
    VALUE_1293_0 = "1293-0"
    VALUE_1294_8 = "1294-8"
    VALUE_1295_5 = "1295-5"
    VALUE_1305_2 = "1305-2"
    VALUE_1306_0 = "1306-0"
    VALUE_1307_8 = "1307-8"
    VALUE_1309_4 = "1309-4"
    VALUE_1310_2 = "1310-2"
    VALUE_1312_8 = "1312-8"
    VALUE_1313_6 = "1313-6"
    VALUE_1314_4 = "1314-4"
    VALUE_1315_1 = "1315-1"
    VALUE_1325_0 = "1325-0"
    VALUE_1326_8 = "1326-8"
    VALUE_1327_6 = "1327-6"
    VALUE_1328_4 = "1328-4"
    VALUE_1329_2 = "1329-2"
    VALUE_1331_8 = "1331-8"
    VALUE_1332_6 = "1332-6"
    VALUE_1333_4 = "1333-4"
    VALUE_1334_2 = "1334-2"
    VALUE_1335_9 = "1335-9"
    VALUE_1336_7 = "1336-7"
    VALUE_1338_3 = "1338-3"
    VALUE_1337_5 = "1337-5"
    VALUE_1344_1 = "1344-1"
    VALUE_1345_8 = "1345-8"
    VALUE_1346_6 = "1346-6"
    VALUE_1358_1 = "1358-1"
    VALUE_1359_9 = "1359-9"
    VALUE_1360_7 = "1360-7"
    VALUE_1361_5 = "1361-5"
    VALUE_1365_6 = "1365-6"
    VALUE_1366_4 = "1366-4"
    VALUE_1382_1 = "1382-1"
    VALUE_1383_9 = "1383-9"
    VALUE_1384_7 = "1384-7"
    VALUE_1385_4 = "1385-4"
    VALUE_1391_2 = "1391-2"
    VALUE_1392_0 = "1392-0"
    VALUE_1393_8 = "1393-8"
    VALUE_1394_6 = "1394-6"
    VALUE_1395_3 = "1395-3"
    VALUE_1396_1 = "1396-1"
    VALUE_1397_9 = "1397-9"
    VALUE_1398_7 = "1398-7"
    VALUE_1399_5 = "1399-5"
    VALUE_1400_1 = "1400-1"
    VALUE_1401_9 = "1401-9"
    VALUE_1411_8 = "1411-8"
    VALUE_1412_6 = "1412-6"
    VALUE_1413_4 = "1413-4"
    VALUE_1414_2 = "1414-2"
    VALUE_1416_7 = "1416-7"
    VALUE_1417_5 = "1417-5"
    VALUE_1418_3 = "1418-3"
    VALUE_1419_1 = "1419-1"
    VALUE_1420_9 = "1420-9"
    VALUE_1421_7 = "1421-7"
    VALUE_1422_5 = "1422-5"
    VALUE_1423_3 = "1423-3"
    VALUE_1424_1 = "1424-1"
    VALUE_1425_8 = "1425-8"
    VALUE_1426_6 = "1426-6"
    VALUE_1427_4 = "1427-4"
    VALUE_1428_2 = "1428-2"
    VALUE_1429_0 = "1429-0"
    VALUE_1430_8 = "1430-8"
    VALUE_1431_6 = "1431-6"
    VALUE_1432_4 = "1432-4"
    VALUE_1433_2 = "1433-2"
    VALUE_1434_0 = "1434-0"
    VALUE_1435_7 = "1435-7"
    VALUE_1436_5 = "1436-5"
    VALUE_1437_3 = "1437-3"
    VALUE_1441_5 = "1441-5"
    VALUE_1442_3 = "1442-3"
    VALUE_1443_1 = "1443-1"
    VALUE_1445_6 = "1445-6"
    VALUE_1446_4 = "1446-4"
    VALUE_1450_6 = "1450-6"
    VALUE_1451_4 = "1451-4"
    VALUE_1453_0 = "1453-0"
    VALUE_1454_8 = "1454-8"
    VALUE_1456_3 = "1456-3"
    VALUE_1457_1 = "1457-1"
    VALUE_1458_9 = "1458-9"
    VALUE_1464_7 = "1464-7"
    VALUE_1465_4 = "1465-4"
    VALUE_1466_2 = "1466-2"
    VALUE_1467_0 = "1467-0"
    VALUE_1468_8 = "1468-8"
    VALUE_1469_6 = "1469-6"
    VALUE_1470_4 = "1470-4"
    VALUE_1471_2 = "1471-2"
    VALUE_1472_0 = "1472-0"
    VALUE_1474_6 = "1474-6"
    VALUE_1475_3 = "1475-3"
    VALUE_1476_1 = "1476-1"
    VALUE_1478_7 = "1478-7"
    VALUE_1479_5 = "1479-5"
    VALUE_1480_3 = "1480-3"
    VALUE_1481_1 = "1481-1"
    VALUE_1482_9 = "1482-9"
    VALUE_1483_7 = "1483-7"
    VALUE_1484_5 = "1484-5"
    VALUE_1485_2 = "1485-2"
    VALUE_1489_4 = "1489-4"
    VALUE_1490_2 = "1490-2"
    VALUE_1491_0 = "1491-0"
    VALUE_1492_8 = "1492-8"
    VALUE_1493_6 = "1493-6"
    VALUE_1494_4 = "1494-4"
    VALUE_1495_1 = "1495-1"
    VALUE_1496_9 = "1496-9"
    VALUE_1497_7 = "1497-7"
    VALUE_1498_5 = "1498-5"
    VALUE_1499_3 = "1499-3"
    VALUE_1500_8 = "1500-8"
    VALUE_1501_6 = "1501-6"
    VALUE_1502_4 = "1502-4"
    VALUE_1503_2 = "1503-2"
    VALUE_1506_5 = "1506-5"
    VALUE_1505_7 = "1505-7"
    VALUE_1504_0 = "1504-0"
    VALUE_1507_3 = "1507-3"
    VALUE_1508_1 = "1508-1"
    VALUE_1509_9 = "1509-9"
    VALUE_1510_7 = "1510-7"
    VALUE_1511_5 = "1511-5"
    VALUE_1512_3 = "1512-3"
    VALUE_1513_1 = "1513-1"
    VALUE_1514_9 = "1514-9"
    VALUE_1515_6 = "1515-6"
    VALUE_1516_4 = "1516-4"
    VALUE_1518_0 = "1518-0"
    VALUE_1519_8 = "1519-8"
    VALUE_1520_6 = "1520-6"
    VALUE_1521_4 = "1521-4"
    VALUE_1522_2 = "1522-2"
    VALUE_1523_0 = "1523-0"
    VALUE_1524_8 = "1524-8"
    VALUE_1525_5 = "1525-5"
    VALUE_1526_3 = "1526-3"
    VALUE_1527_1 = "1527-1"
    VALUE_1528_9 = "1528-9"
    VALUE_1529_7 = "1529-7"
    VALUE_1530_5 = "1530-5"
    VALUE_1531_3 = "1531-3"
    VALUE_1532_1 = "1532-1"
    VALUE_1533_9 = "1533-9"
    VALUE_1534_7 = "1534-7"
    VALUE_1535_4 = "1535-4"
    VALUE_1536_2 = "1536-2"
    VALUE_1537_0 = "1537-0"
    VALUE_1538_8 = "1538-8"
    VALUE_1539_6 = "1539-6"
    VALUE_1551_1 = "1551-1"
    VALUE_1552_9 = "1552-9"
    VALUE_1553_7 = "1553-7"
    VALUE_1554_5 = "1554-5"
    VALUE_1566_9 = "1566-9"
    VALUE_1567_7 = "1567-7"
    VALUE_1568_5 = "1568-5"
    VALUE_1569_3 = "1569-3"
    VALUE_1570_1 = "1570-1"
    VALUE_1571_9 = "1571-9"
    VALUE_1573_5 = "1573-5"
    VALUE_1574_3 = "1574-3"
    VALUE_1578_4 = "1578-4"
    VALUE_1579_2 = "1579-2"
    VALUE_1580_0 = "1580-0"
    VALUE_1586_7 = "1586-7"
    VALUE_1587_5 = "1587-5"
    VALUE_1588_3 = "1588-3"
    VALUE_1589_1 = "1589-1"
    VALUE_1590_9 = "1590-9"
    VALUE_1591_7 = "1591-7"
    VALUE_1592_5 = "1592-5"
    VALUE_1593_3 = "1593-3"
    VALUE_1594_1 = "1594-1"
    VALUE_1595_8 = "1595-8"
    VALUE_1596_6 = "1596-6"
    VALUE_1597_4 = "1597-4"
    VALUE_1598_2 = "1598-2"
    VALUE_1599_0 = "1599-0"
    VALUE_1600_6 = "1600-6"
    VALUE_1602_2 = "1602-2"
    VALUE_1603_0 = "1603-0"
    VALUE_1604_8 = "1604-8"
    VALUE_1605_5 = "1605-5"
    VALUE_1609_7 = "1609-7"
    VALUE_1610_5 = "1610-5"
    VALUE_1611_3 = "1611-3"
    VALUE_1612_1 = "1612-1"
    VALUE_1613_9 = "1613-9"
    VALUE_1614_7 = "1614-7"
    VALUE_1615_4 = "1615-4"
    VALUE_1616_2 = "1616-2"
    VALUE_1617_0 = "1617-0"
    VALUE_1618_8 = "1618-8"
    VALUE_1619_6 = "1619-6"
    VALUE_1620_4 = "1620-4"
    VALUE_1621_2 = "1621-2"
    VALUE_1622_0 = "1622-0"
    VALUE_1623_8 = "1623-8"
    VALUE_1624_6 = "1624-6"
    VALUE_1625_3 = "1625-3"
    VALUE_1626_1 = "1626-1"
    VALUE_1627_9 = "1627-9"
    VALUE_1628_7 = "1628-7"
    VALUE_1629_5 = "1629-5"
    VALUE_1631_1 = "1631-1"
    VALUE_1630_3 = "1630-3"
    VALUE_1632_9 = "1632-9"
    VALUE_1633_7 = "1633-7"
    VALUE_1634_5 = "1634-5"
    VALUE_1635_2 = "1635-2"
    VALUE_1636_0 = "1636-0"
    VALUE_1637_8 = "1637-8"
    VALUE_1638_6 = "1638-6"
    VALUE_1639_4 = "1639-4"
    VALUE_1640_2 = "1640-2"
    VALUE_1641_0 = "1641-0"
    VALUE_1653_5 = "1653-5"
    VALUE_1654_3 = "1654-3"
    VALUE_1655_0 = "1655-0"
    VALUE_1656_8 = "1656-8"
    VALUE_1657_6 = "1657-6"
    VALUE_1667_5 = "1667-5"
    VALUE_1668_3 = "1668-3"
    VALUE_1670_9 = "1670-9"
    VALUE_1671_7 = "1671-7"
    VALUE_1672_5 = "1672-5"
    VALUE_1673_3 = "1673-3"
    VALUE_1679_0 = "1679-0"
    VALUE_1680_8 = "1680-8"
    VALUE_1681_6 = "1681-6"
    VALUE_1687_3 = "1687-3"
    VALUE_1688_1 = "1688-1"
    VALUE_1689_9 = "1689-9"
    VALUE_1690_7 = "1690-7"
    VALUE_1696_4 = "1696-4"
    VALUE_1697_2 = "1697-2"
    VALUE_1698_0 = "1698-0"
    VALUE_1724_4 = "1724-4"
    VALUE_1725_1 = "1725-1"
    VALUE_1726_9 = "1726-9"
    VALUE_1727_7 = "1727-7"
    VALUE_1728_5 = "1728-5"
    VALUE_1729_3 = "1729-3"
    VALUE_1730_1 = "1730-1"
    VALUE_1731_9 = "1731-9"
    VALUE_1732_7 = "1732-7"
    VALUE_1733_5 = "1733-5"
    VALUE_1068_6 = "1068-6"
    VALUE_1069_4 = "1069-4"
    VALUE_1070_2 = "1070-2"
    VALUE_1071_0 = "1071-0"
    VALUE_1072_8 = "1072-8"
    VALUE_1073_6 = "1073-6"
    VALUE_1704_6 = "1704-6"
    VALUE_1705_3 = "1705-3"
    VALUE_1711_1 = "1711-1"
    VALUE_1712_9 = "1712-9"
    VALUE_1713_7 = "1713-7"
    VALUE_1717_8 = "1717-8"
    VALUE_1718_6 = "1718-6"
    VALUE_1719_4 = "1719-4"
    VALUE_1720_2 = "1720-2"
    VALUE_1004_1 = "1004-1"
    VALUE_1006_6 = "1006-6"
    VALUE_1008_2 = "1008-2"
    VALUE_1026_4 = "1026-4"
    VALUE_1028_0 = "1028-0"
    VALUE_1033_0 = "1033-0"
    VALUE_1035_5 = "1035-5"
    VALUE_1037_1 = "1037-1"
    VALUE_1039_7 = "1039-7"
    VALUE_1078_5 = "1078-5"
    VALUE_1080_1 = "1080-1"
    VALUE_1086_8 = "1086-8"
    VALUE_1100_7 = "1100-7"
    VALUE_1106_4 = "1106-4"
    VALUE_1112_2 = "1112-2"
    VALUE_1153_6 = "1153-6"
    VALUE_1165_0 = "1165-0"
    VALUE_1167_6 = "1167-6"
    VALUE_1169_2 = "1169-2"
    VALUE_1171_8 = "1171-8"
    VALUE_1173_4 = "1173-4"
    VALUE_1180_9 = "1180-9"
    VALUE_1178_3 = "1178-3"
    VALUE_1182_5 = "1182-5"
    VALUE_1184_1 = "1184-1"
    VALUE_1189_0 = "1189-0"
    VALUE_1191_6 = "1191-6"
    VALUE_1207_0 = "1207-0"
    VALUE_1209_6 = "1209-6"
    VALUE_1250_0 = "1250-0"
    VALUE_1252_6 = "1252-6"
    VALUE_1254_2 = "1254-2"
    VALUE_1258_3 = "1258-3"
    VALUE_1256_7 = "1256-7"
    VALUE_1260_9 = "1260-9"
    VALUE_1262_5 = "1262-5"
    VALUE_1267_4 = "1267-4"
    VALUE_1269_0 = "1269-0"
    VALUE_1275_7 = "1275-7"
    VALUE_1277_3 = "1277-3"
    VALUE_1279_9 = "1279-9"
    VALUE_1297_1 = "1297-1"
    VALUE_1299_7 = "1299-7"
    VALUE_1301_1 = "1301-1"
    VALUE_1303_7 = "1303-7"
    VALUE_1317_7 = "1317-7"
    VALUE_1319_3 = "1319-3"
    VALUE_1321_9 = "1321-9"
    VALUE_1323_5 = "1323-5"
    VALUE_1340_9 = "1340-9"
    VALUE_1342_5 = "1342-5"
    VALUE_1348_2 = "1348-2"
    VALUE_1350_8 = "1350-8"
    VALUE_1352_4 = "1352-4"
    VALUE_1354_0 = "1354-0"
    VALUE_1356_5 = "1356-5"
    VALUE_1363_1 = "1363-1"
    VALUE_1368_0 = "1368-0"
    VALUE_1370_6 = "1370-6"
    VALUE_1372_2 = "1372-2"
    VALUE_1374_8 = "1374-8"
    VALUE_1376_3 = "1376-3"
    VALUE_1378_9 = "1378-9"
    VALUE_1380_5 = "1380-5"
    VALUE_1387_0 = "1387-0"
    VALUE_1389_6 = "1389-6"
    VALUE_1403_5 = "1403-5"
    VALUE_1405_0 = "1405-0"
    VALUE_1407_6 = "1407-6"
    VALUE_1409_2 = "1409-2"
    VALUE_1439_9 = "1439-9"
    VALUE_1448_0 = "1448-0"
    VALUE_1460_5 = "1460-5"
    VALUE_1462_1 = "1462-1"
    VALUE_1487_8 = "1487-8"
    VALUE_1541_2 = "1541-2"
    VALUE_1543_8 = "1543-8"
    VALUE_1545_3 = "1545-3"
    VALUE_1547_9 = "1547-9"
    VALUE_1549_5 = "1549-5"
    VALUE_1556_0 = "1556-0"
    VALUE_1558_6 = "1558-6"
    VALUE_1560_2 = "1560-2"
    VALUE_1562_8 = "1562-8"
    VALUE_1564_4 = "1564-4"
    VALUE_1576_8 = "1576-8"
    VALUE_1582_6 = "1582-6"
    VALUE_1584_2 = "1584-2"
    VALUE_1607_1 = "1607-1"
    VALUE_1643_6 = "1643-6"
    VALUE_1074_4 = "1074-4"
    VALUE_1645_1 = "1645-1"
    VALUE_1647_7 = "1647-7"
    VALUE_1649_3 = "1649-3"
    VALUE_1651_9 = "1651-9"
    VALUE_1659_2 = "1659-2"
    VALUE_1661_8 = "1661-8"
    VALUE_1663_4 = "1663-4"
    VALUE_1665_9 = "1665-9"
    VALUE_1675_8 = "1675-8"
    VALUE_1677_4 = "1677-4"
    VALUE_1683_2 = "1683-2"
    VALUE_1685_7 = "1685-7"
    VALUE_1692_3 = "1692-3"
    VALUE_1694_9 = "1694-9"
    VALUE_1700_4 = "1700-4"
    VALUE_1702_0 = "1702-0"
    VALUE_1707_9 = "1707-9"
    VALUE_1709_5 = "1709-5"
    VALUE_1715_2 = "1715-2"
    VALUE_1722_8 = "1722-8"
    VALUE_1002_5 = "1002-5"


class RacePacificIslandMelanesian(Enum):
    """
    specDomain: S15808 (C-0-T14914-S15787-S15808-cpt)
    :cvar VALUE_2100_6:
    :cvar VALUE_2101_4:
    :cvar VALUE_2104_8:
    :cvar VALUE_2102_2:
    :cvar VALUE_2103_0:
    """
    VALUE_2100_6 = "2100-6"
    VALUE_2101_4 = "2101-4"
    VALUE_2104_8 = "2104-8"
    VALUE_2102_2 = "2102-2"
    VALUE_2103_0 = "2103-0"


class RacePacificIslandMicronesian(Enum):
    """
    specDomain: S15794 (C-0-T14914-S15787-S15794-cpt)
    :cvar VALUE_2085_9:
    :cvar VALUE_2092_5:
    :cvar VALUE_2088_3:
    :cvar VALUE_2097_4:
    :cvar VALUE_2087_5:
    :cvar VALUE_2086_7:
    :cvar VALUE_2096_6:
    :cvar VALUE_2093_3:
    :cvar VALUE_2089_1:
    :cvar VALUE_2090_9:
    :cvar VALUE_2091_7:
    :cvar VALUE_2094_1:
    :cvar VALUE_2095_8:
    :cvar VALUE_2098_2:
    """
    VALUE_2085_9 = "2085-9"
    VALUE_2092_5 = "2092-5"
    VALUE_2088_3 = "2088-3"
    VALUE_2097_4 = "2097-4"
    VALUE_2087_5 = "2087-5"
    VALUE_2086_7 = "2086-7"
    VALUE_2096_6 = "2096-6"
    VALUE_2093_3 = "2093-3"
    VALUE_2089_1 = "2089-1"
    VALUE_2090_9 = "2090-9"
    VALUE_2091_7 = "2091-7"
    VALUE_2094_1 = "2094-1"
    VALUE_2095_8 = "2095-8"
    VALUE_2098_2 = "2098-2"


class RacePacificIslandPolynesian(Enum):
    """
    specDomain: S15788 (C-0-T14914-S15787-S15788-cpt)
    :cvar VALUE_2078_4:
    :cvar VALUE_2079_2:
    :cvar VALUE_2080_0:
    :cvar VALUE_2081_8:
    :cvar VALUE_2083_4:
    :cvar VALUE_2082_6:
    """
    VALUE_2078_4 = "2078-4"
    VALUE_2079_2 = "2079-2"
    VALUE_2080_0 = "2080-0"
    VALUE_2081_8 = "2081-8"
    VALUE_2083_4 = "2083-4"
    VALUE_2082_6 = "2082-6"


class RaceSoutheastAlaskanIndian(Enum):
    """
    specDomain: S15543 (C-0-T14914-S14915-S15470-S15471-S15543-cpt)
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    :cvar VALUE_1811_9:
    """
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"
    VALUE_1811_9 = "1811-9"


class RaceSoutheastAlaskanIndianTlingit(Enum):
    """
    specDomain: S15544 (C-0-T14914-S14915-S15470-S15471-S15543-S15544-cpt)
    :cvar VALUE_1813_5:
    :cvar VALUE_1814_3:
    :cvar VALUE_1815_0:
    :cvar VALUE_1816_8:
    :cvar VALUE_1817_6:
    :cvar VALUE_1818_4:
    :cvar VALUE_1819_2:
    :cvar VALUE_1820_0:
    :cvar VALUE_1821_8:
    :cvar VALUE_1822_6:
    :cvar VALUE_1823_4:
    :cvar VALUE_1824_2:
    :cvar VALUE_1825_9:
    :cvar VALUE_1826_7:
    :cvar VALUE_1827_5:
    :cvar VALUE_1828_3:
    :cvar VALUE_1829_1:
    :cvar VALUE_1830_9:
    :cvar VALUE_1831_7:
    :cvar VALUE_1832_5:
    :cvar VALUE_1833_3:
    :cvar VALUE_1834_1:
    :cvar VALUE_1835_8:
    """
    VALUE_1813_5 = "1813-5"
    VALUE_1814_3 = "1814-3"
    VALUE_1815_0 = "1815-0"
    VALUE_1816_8 = "1816-8"
    VALUE_1817_6 = "1817-6"
    VALUE_1818_4 = "1818-4"
    VALUE_1819_2 = "1819-2"
    VALUE_1820_0 = "1820-0"
    VALUE_1821_8 = "1821-8"
    VALUE_1822_6 = "1822-6"
    VALUE_1823_4 = "1823-4"
    VALUE_1824_2 = "1824-2"
    VALUE_1825_9 = "1825-9"
    VALUE_1826_7 = "1826-7"
    VALUE_1827_5 = "1827-5"
    VALUE_1828_3 = "1828-3"
    VALUE_1829_1 = "1829-1"
    VALUE_1830_9 = "1830-9"
    VALUE_1831_7 = "1831-7"
    VALUE_1832_5 = "1832-5"
    VALUE_1833_3 = "1833-3"
    VALUE_1834_1 = "1834-1"
    VALUE_1835_8 = "1835-8"


class RaceSoutheastAlaskanIndianTsimshian(Enum):
    """
    specDomain: S15567 (C-0-T14914-S14915-S15470-S15471-S15543-S15567-cpt)
    :cvar VALUE_1837_4:
    :cvar VALUE_1838_2:
    """
    VALUE_1837_4 = "1837-4"
    VALUE_1838_2 = "1838-2"


class RaceWhite(Enum):
    """
    specDomain: S15814 (C-0-T14914-S15814-cpt)
    :cvar VALUE_2129_5:
    :cvar VALUE_2108_9:
    :cvar VALUE_2109_7:
    :cvar VALUE_2110_5:
    :cvar VALUE_2111_3:
    :cvar VALUE_2112_1:
    :cvar VALUE_2113_9:
    :cvar VALUE_2114_7:
    :cvar VALUE_2115_4:
    :cvar VALUE_2116_2:
    :cvar VALUE_2118_8:
    :cvar VALUE_2126_1:
    :cvar VALUE_2119_6:
    :cvar VALUE_2120_4:
    :cvar VALUE_2121_2:
    :cvar VALUE_2122_0:
    :cvar VALUE_2127_9:
    :cvar VALUE_2123_8:
    :cvar VALUE_2124_6:
    :cvar VALUE_2125_3:
    :cvar VALUE_2106_3:
    """
    VALUE_2129_5 = "2129-5"
    VALUE_2108_9 = "2108-9"
    VALUE_2109_7 = "2109-7"
    VALUE_2110_5 = "2110-5"
    VALUE_2111_3 = "2111-3"
    VALUE_2112_1 = "2112-1"
    VALUE_2113_9 = "2113-9"
    VALUE_2114_7 = "2114-7"
    VALUE_2115_4 = "2115-4"
    VALUE_2116_2 = "2116-2"
    VALUE_2118_8 = "2118-8"
    VALUE_2126_1 = "2126-1"
    VALUE_2119_6 = "2119-6"
    VALUE_2120_4 = "2120-4"
    VALUE_2121_2 = "2121-2"
    VALUE_2122_0 = "2122-0"
    VALUE_2127_9 = "2127-9"
    VALUE_2123_8 = "2123-8"
    VALUE_2124_6 = "2124-6"
    VALUE_2125_3 = "2125-3"
    VALUE_2106_3 = "2106-3"


class RaceWhiteArab(Enum):
    """
    specDomain: S15834 (C-0-T14914-S15814-S15834-cpt)
    :cvar VALUE_2129_5:
    """
    VALUE_2129_5 = "2129-5"


class RaceWhiteEuropean(Enum):
    """
    specDomain: S15815 (C-0-T14914-S15814-S15815-cpt)
    :cvar VALUE_2108_9:
    :cvar VALUE_2109_7:
    :cvar VALUE_2110_5:
    :cvar VALUE_2111_3:
    :cvar VALUE_2112_1:
    :cvar VALUE_2113_9:
    :cvar VALUE_2114_7:
    :cvar VALUE_2115_4:
    :cvar VALUE_2116_2:
    """
    VALUE_2108_9 = "2108-9"
    VALUE_2109_7 = "2109-7"
    VALUE_2110_5 = "2110-5"
    VALUE_2111_3 = "2111-3"
    VALUE_2112_1 = "2112-1"
    VALUE_2113_9 = "2113-9"
    VALUE_2114_7 = "2114-7"
    VALUE_2115_4 = "2115-4"
    VALUE_2116_2 = "2116-2"


class RaceWhiteMiddleEast(Enum):
    """
    specDomain: S15824 (C-0-T14914-S15814-S15824-cpt)
    :cvar VALUE_2118_8:
    :cvar VALUE_2126_1:
    :cvar VALUE_2119_6:
    :cvar VALUE_2120_4:
    :cvar VALUE_2121_2:
    :cvar VALUE_2122_0:
    :cvar VALUE_2127_9:
    :cvar VALUE_2123_8:
    :cvar VALUE_2124_6:
    :cvar VALUE_2125_3:
    """
    VALUE_2118_8 = "2118-8"
    VALUE_2126_1 = "2126-1"
    VALUE_2119_6 = "2119-6"
    VALUE_2120_4 = "2120-4"
    VALUE_2121_2 = "2121-2"
    VALUE_2122_0 = "2122-0"
    VALUE_2127_9 = "2127-9"
    VALUE_2123_8 = "2123-8"
    VALUE_2124_6 = "2124-6"
    VALUE_2125_3 = "2125-3"


class RadDiagTherPracticeSetting(Enum):
    """
    specDomain: S10908 (C-0-T12206-A17660-A19450-A10588-S10902-S10908-cpt)
    :cvar RADDX:
    :cvar RNEU:
    :cvar VALUE_261_QX0203_N:
    :cvar RADO:
    """
    RADDX = "RADDX"
    RNEU = "RNEU"
    VALUE_261_QX0203_N = "261QX0203N"
    RADO = "RADO"


class RadiologicTechnologistHipaa(Enum):
    """
    abstDomain: A13645 (C-0-T13129-A13130-A13644-A13645-cpt)
    :cvar VALUE_2471_C1101_N:
    :cvar VALUE_2471_C3401_N:
    :cvar VALUE_2471_C3402_N:
    :cvar VALUE_2471_D1300_N:
    :cvar VALUE_2471_M1201_N:
    :cvar VALUE_2471_M1202_N:
    :cvar VALUE_2471_M2300_N:
    :cvar VALUE_2471_N0900_N:
    :cvar VALUE_2471_Q0001_N:
    :cvar VALUE_2471_Q0002_N:
    :cvar VALUE_2471_R0003_N:
    :cvar VALUE_2471_R0002_N:
    :cvar VALUE_2471_R1500_N:
    :cvar VALUE_2471_S1302_N:
    """
    VALUE_2471_C1101_N = "2471C1101N"
    VALUE_2471_C3401_N = "2471C3401N"
    VALUE_2471_C3402_N = "2471C3402N"
    VALUE_2471_D1300_N = "2471D1300N"
    VALUE_2471_M1201_N = "2471M1201N"
    VALUE_2471_M1202_N = "2471M1202N"
    VALUE_2471_M2300_N = "2471M2300N"
    VALUE_2471_N0900_N = "2471N0900N"
    VALUE_2471_Q0001_N = "2471Q0001N"
    VALUE_2471_Q0002_N = "2471Q0002N"
    VALUE_2471_R0003_N = "2471R0003N"
    VALUE_2471_R0002_N = "2471R0002N"
    VALUE_2471_R1500_N = "2471R1500N"
    VALUE_2471_S1302_N = "2471S1302N"


class RadiologicTechnologistProviderCodes(Enum):
    """
    specDomain: S20609 (C-0-T19465-S20608-S20609-cpt)
    :cvar VALUE_247100000_X:
    :cvar VALUE_2471_B0102_X:
    :cvar VALUE_2471_C1106_X:
    :cvar VALUE_2471_C1101_X:
    :cvar VALUE_2471_C3401_X:
    :cvar VALUE_2471_M1202_X:
    :cvar VALUE_2471_M2300_X:
    :cvar VALUE_2471_N0900_X:
    :cvar VALUE_2471_Q0001_X:
    :cvar VALUE_2471_R0002_X:
    :cvar VALUE_2471_C3402_X:
    :cvar VALUE_2471_S1302_X:
    :cvar VALUE_2471_V0105_X:
    :cvar VALUE_2471_V0106_X:
    """
    VALUE_247100000_X = "247100000X"
    VALUE_2471_B0102_X = "2471B0102X"
    VALUE_2471_C1106_X = "2471C1106X"
    VALUE_2471_C1101_X = "2471C1101X"
    VALUE_2471_C3401_X = "2471C3401X"
    VALUE_2471_M1202_X = "2471M1202X"
    VALUE_2471_M2300_X = "2471M2300X"
    VALUE_2471_N0900_X = "2471N0900X"
    VALUE_2471_Q0001_X = "2471Q0001X"
    VALUE_2471_R0002_X = "2471R0002X"
    VALUE_2471_C3402_X = "2471C3402X"
    VALUE_2471_S1302_X = "2471S1302X"
    VALUE_2471_V0105_X = "2471V0105X"
    VALUE_2471_V0106_X = "2471V0106X"


class RadiologyProviderCodes(Enum):
    """
    specDomain: S20253 (C-0-T19465-S20096-S20253-cpt)
    :cvar VALUE_208500000_X:
    :cvar VALUE_2085_B0100_X:
    :cvar VALUE_2085_R0202_X:
    :cvar VALUE_2085_U0001_X:
    :cvar VALUE_2085_N0700_X:
    :cvar VALUE_2085_N0904_X:
    :cvar VALUE_2085_P0229_X:
    :cvar VALUE_2085_R0001_X:
    :cvar VALUE_2085_R0205_X:
    :cvar VALUE_2085_R0203_X:
    :cvar VALUE_2085_R0204_X:
    """
    VALUE_208500000_X = "208500000X"
    VALUE_2085_B0100_X = "2085B0100X"
    VALUE_2085_R0202_X = "2085R0202X"
    VALUE_2085_U0001_X = "2085U0001X"
    VALUE_2085_N0700_X = "2085N0700X"
    VALUE_2085_N0904_X = "2085N0904X"
    VALUE_2085_P0229_X = "2085P0229X"
    VALUE_2085_R0001_X = "2085R0001X"
    VALUE_2085_R0205_X = "2085R0205X"
    VALUE_2085_R0203_X = "2085R0203X"
    VALUE_2085_R0204_X = "2085R0204X"


class ReactionDetectedIssueCode(Enum):
    """
    specDomain: S16672 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16672-cpt)
    :cvar REACT:
    :cvar ALGY:
    :cvar INT_VALUE:
    """
    REACT = "REACT"
    ALGY = "ALGY"
    INT_VALUE = "INT"


class RealmOfUse(Enum):
    """
    abstDomain: A11050 (C-0-T11046-A11050-cpt)
    :cvar CANADA:
    :cvar NORTH_AMERICA:
    :cvar USA:
    :cvar UV:
    """
    CANADA = "Canada"
    NORTH_AMERICA = "NorthAmerica"
    USA = "USA"
    UV = "UV"


class RectalInstillation(Enum):
    """
    specDomain: S14715 (C-0-T14581-A17021-A17311-S14715-cpt)
    :cvar RECINSTL:
    :cvar RECTINSTL:
    """
    RECINSTL = "RECINSTL"
    RECTINSTL = "RECTINSTL"


class RectalRoute(Enum):
    """
    abstDomain: A17311 (C-0-T14581-A17021-A17311-cpt)
    :cvar RECINSTL:
    :cvar RECTINSTL:
    :cvar ENEMA:
    :cvar RETENEMA:
    :cvar PR:
    :cvar RECIRR:
    :cvar RECTAL:
    """
    RECINSTL = "RECINSTL"
    RECTINSTL = "RECTINSTL"
    ENEMA = "ENEMA"
    RETENEMA = "RETENEMA"
    PR = "PR"
    RECIRR = "RECIRR"
    RECTAL = "RECTAL"


class RefillCompletePharmacySupplyType(Enum):
    """
    specDomain: S16216 (C-0-T13953-A13954-A16208-S16215-S16216-cpt)
    :cvar RFC:
    :cvar RFCS:
    """
    RFC = "RFC"
    RFCS = "RFCS"


class RefillFirstHerePharmacySupplyType(Enum):
    """
    specDomain: S16218 (C-0-T13953-A13954-A16208-S16215-S16218-cpt)
    :cvar RFF:
    :cvar RFFS:
    """
    RFF = "RFF"
    RFFS = "RFFS"


class RefillPartFillPharmacySupplyType(Enum):
    """
    specDomain: S16217 (C-0-T13953-A13954-A16208-S16215-S16217-cpt)
    :cvar RFP:
    :cvar RFPS:
    """
    RFP = "RFP"
    RFPS = "RFPS"


class RefillPharmacySupplyType(Enum):
    """
    specDomain: S16215 (C-0-T13953-A13954-A16208-S16215-cpt)
    :cvar RFC:
    :cvar RFCS:
    :cvar RFF:
    :cvar RFFS:
    :cvar RFP:
    :cvar RFPS:
    :cvar TB:
    :cvar TBS:
    :cvar RF:
    :cvar DF:
    :cvar UD:
    :cvar RFS:
    """
    RFC = "RFC"
    RFCS = "RFCS"
    RFF = "RFF"
    RFFS = "RFFS"
    RFP = "RFP"
    RFPS = "RFPS"
    TB = "TB"
    TBS = "TBS"
    RF = "RF"
    DF = "DF"
    UD = "UD"
    RFS = "RFS"


class RefillTrialBalancePharmacySupplyType(Enum):
    """
    specDomain: S16213 (C-0-T13953-A13954-A16208-S16215-S16213-cpt)
    :cvar TB:
    :cvar TBS:
    """
    TB = "TB"
    TBS = "TBS"


class RegisteredDieticianHipaa(Enum):
    """
    specDomain: S13201 (C-0-T13129-A13130-A13197-S13201-cpt)
    :cvar VALUE_133_V00000_N:
    :cvar VALUE_133_VN1006_N:
    :cvar VALUE_133_VN1004_N:
    :cvar VALUE_133_VN1005_N:
    """
    VALUE_133_V00000_N = "133V00000N"
    VALUE_133_VN1006_N = "133VN1006N"
    VALUE_133_VN1004_N = "133VN1004N"
    VALUE_133_VN1005_N = "133VN1005N"


class RegisteredNurseHipaa(Enum):
    """
    specDomain: S13232 (C-0-T13129-A13130-A13229-S13232-cpt)
    :cvar VALUE_163_W00000_N:
    :cvar VALUE_163_WA0400_N:
    :cvar VALUE_163_WA2000_N:
    :cvar VALUE_163_WC3500_N:
    :cvar VALUE_163_WC0400_N:
    :cvar VALUE_163_WC1400_N:
    :cvar VALUE_163_WC1500_N:
    :cvar VALUE_163_WC2100_N:
    :cvar VALUE_163_WC1600_N:
    :cvar VALUE_163_WC0200_N:
    :cvar VALUE_163_WD0400_N:
    :cvar VALUE_163_WD1100_N:
    :cvar VALUE_163_WE0003_N:
    :cvar VALUE_163_WE0900_N:
    :cvar VALUE_163_WF0300_N:
    :cvar VALUE_163_WG0100_N:
    :cvar VALUE_163_WG0000_N:
    :cvar VALUE_163_WG0600_N:
    :cvar VALUE_163_WH0500_N:
    :cvar VALUE_163_WH0200_N:
    :cvar VALUE_163_WH1000_N:
    :cvar VALUE_163_WI0600_N:
    :cvar VALUE_163_WI0500_N:
    :cvar VALUE_163_WL0100_N:
    :cvar VALUE_163_WM1400_N:
    :cvar VALUE_163_WM0102_N:
    :cvar VALUE_163_WM0705_N:
    :cvar VALUE_163_WN0002_N:
    :cvar VALUE_163_WN0003_N:
    :cvar VALUE_163_WN0300_N:
    :cvar VALUE_163_WN0800_N:
    :cvar VALUE_163_WN1003_N:
    :cvar VALUE_163_WX0002_N:
    :cvar VALUE_163_WX0003_N:
    :cvar VALUE_163_WX0106_N:
    :cvar VALUE_163_WX0200_N:
    :cvar VALUE_163_WX1000_N:
    :cvar VALUE_163_WX1100_N:
    :cvar VALUE_163_WX0800_N:
    :cvar VALUE_163_WX1500_N:
    :cvar VALUE_163_WX0601_N:
    :cvar VALUE_163_WP0000_N:
    :cvar VALUE_163_WP0218_N:
    :cvar VALUE_163_WP0200_N:
    :cvar VALUE_163_WP1700_N:
    :cvar VALUE_163_WP2200_N:
    :cvar VALUE_163_WP2201_N:
    :cvar VALUE_163_WP0808_N:
    :cvar VALUE_163_WP0809_N:
    :cvar VALUE_163_WP0807_N:
    :cvar VALUE_163_WR0400_N:
    :cvar VALUE_163_WR1000_N:
    :cvar VALUE_163_WS0200_N:
    :cvar VALUE_163_WS0121_N:
    :cvar VALUE_163_WU0100_N:
    :cvar VALUE_163_WW0101_N:
    :cvar VALUE_163_WW0000_N:
    """
    VALUE_163_W00000_N = "163W00000N"
    VALUE_163_WA0400_N = "163WA0400N"
    VALUE_163_WA2000_N = "163WA2000N"
    VALUE_163_WC3500_N = "163WC3500N"
    VALUE_163_WC0400_N = "163WC0400N"
    VALUE_163_WC1400_N = "163WC1400N"
    VALUE_163_WC1500_N = "163WC1500N"
    VALUE_163_WC2100_N = "163WC2100N"
    VALUE_163_WC1600_N = "163WC1600N"
    VALUE_163_WC0200_N = "163WC0200N"
    VALUE_163_WD0400_N = "163WD0400N"
    VALUE_163_WD1100_N = "163WD1100N"
    VALUE_163_WE0003_N = "163WE0003N"
    VALUE_163_WE0900_N = "163WE0900N"
    VALUE_163_WF0300_N = "163WF0300N"
    VALUE_163_WG0100_N = "163WG0100N"
    VALUE_163_WG0000_N = "163WG0000N"
    VALUE_163_WG0600_N = "163WG0600N"
    VALUE_163_WH0500_N = "163WH0500N"
    VALUE_163_WH0200_N = "163WH0200N"
    VALUE_163_WH1000_N = "163WH1000N"
    VALUE_163_WI0600_N = "163WI0600N"
    VALUE_163_WI0500_N = "163WI0500N"
    VALUE_163_WL0100_N = "163WL0100N"
    VALUE_163_WM1400_N = "163WM1400N"
    VALUE_163_WM0102_N = "163WM0102N"
    VALUE_163_WM0705_N = "163WM0705N"
    VALUE_163_WN0002_N = "163WN0002N"
    VALUE_163_WN0003_N = "163WN0003N"
    VALUE_163_WN0300_N = "163WN0300N"
    VALUE_163_WN0800_N = "163WN0800N"
    VALUE_163_WN1003_N = "163WN1003N"
    VALUE_163_WX0002_N = "163WX0002N"
    VALUE_163_WX0003_N = "163WX0003N"
    VALUE_163_WX0106_N = "163WX0106N"
    VALUE_163_WX0200_N = "163WX0200N"
    VALUE_163_WX1000_N = "163WX1000N"
    VALUE_163_WX1100_N = "163WX1100N"
    VALUE_163_WX0800_N = "163WX0800N"
    VALUE_163_WX1500_N = "163WX1500N"
    VALUE_163_WX0601_N = "163WX0601N"
    VALUE_163_WP0000_N = "163WP0000N"
    VALUE_163_WP0218_N = "163WP0218N"
    VALUE_163_WP0200_N = "163WP0200N"
    VALUE_163_WP1700_N = "163WP1700N"
    VALUE_163_WP2200_N = "163WP2200N"
    VALUE_163_WP2201_N = "163WP2201N"
    VALUE_163_WP0808_N = "163WP0808N"
    VALUE_163_WP0809_N = "163WP0809N"
    VALUE_163_WP0807_N = "163WP0807N"
    VALUE_163_WR0400_N = "163WR0400N"
    VALUE_163_WR1000_N = "163WR1000N"
    VALUE_163_WS0200_N = "163WS0200N"
    VALUE_163_WS0121_N = "163WS0121N"
    VALUE_163_WU0100_N = "163WU0100N"
    VALUE_163_WW0101_N = "163WW0101N"
    VALUE_163_WW0000_N = "163WW0000N"


class RegisteredNurseProviderCodes(Enum):
    """
    specDomain: S20370 (C-0-T19465-S20366-S20370-cpt)
    :cvar VALUE_163_W00000_X:
    :cvar VALUE_163_WA0400_X:
    :cvar VALUE_163_WA2000_X:
    :cvar VALUE_163_WP2201_X:
    :cvar VALUE_163_WC3500_X:
    :cvar VALUE_163_WC0400_X:
    :cvar VALUE_163_WC1400_X:
    :cvar VALUE_163_WC1500_X:
    :cvar VALUE_163_WC2100_X:
    :cvar VALUE_163_WC1600_X:
    :cvar VALUE_163_WC0200_X:
    :cvar VALUE_163_WD0400_X:
    :cvar VALUE_163_WD1100_X:
    :cvar VALUE_163_WE0003_X:
    :cvar VALUE_163_WE0900_X:
    :cvar VALUE_163_WF0300_X:
    :cvar VALUE_163_WG0100_X:
    :cvar VALUE_163_WG0000_X:
    :cvar VALUE_163_WG0600_X:
    :cvar VALUE_163_WH0500_X:
    :cvar VALUE_163_WH0200_X:
    :cvar VALUE_163_WH1000_X:
    :cvar VALUE_163_WI0600_X:
    :cvar VALUE_163_WI0500_X:
    :cvar VALUE_163_WL0100_X:
    :cvar VALUE_163_WM0102_X:
    :cvar VALUE_163_WM0705_X:
    :cvar VALUE_163_WN0002_X:
    :cvar VALUE_163_WN0003_X:
    :cvar VALUE_163_WN0300_X:
    :cvar VALUE_163_WN0800_X:
    :cvar VALUE_163_WM1400_X:
    :cvar VALUE_163_WN1003_X:
    :cvar VALUE_163_WX0002_X:
    :cvar VALUE_163_WX0003_X:
    :cvar VALUE_163_WX0106_X:
    :cvar VALUE_163_WX0200_X:
    :cvar VALUE_163_WX1100_X:
    :cvar VALUE_163_WX0800_X:
    :cvar VALUE_163_WX1500_X:
    :cvar VALUE_163_WX0601_X:
    :cvar VALUE_163_WP0000_X:
    :cvar VALUE_163_WP0218_X:
    :cvar VALUE_163_WP0200_X:
    :cvar VALUE_163_WP1700_X:
    :cvar VALUE_163_WS0121_X:
    :cvar VALUE_163_WP0808_X:
    :cvar VALUE_163_WP0809_X:
    :cvar VALUE_163_WP0807_X:
    :cvar VALUE_163_WR0400_X:
    :cvar VALUE_163_WR1000_X:
    :cvar VALUE_163_WS0200_X:
    :cvar VALUE_163_WU0100_X:
    :cvar VALUE_163_WW0101_X:
    :cvar VALUE_163_WW0000_X:
    """
    VALUE_163_W00000_X = "163W00000X"
    VALUE_163_WA0400_X = "163WA0400X"
    VALUE_163_WA2000_X = "163WA2000X"
    VALUE_163_WP2201_X = "163WP2201X"
    VALUE_163_WC3500_X = "163WC3500X"
    VALUE_163_WC0400_X = "163WC0400X"
    VALUE_163_WC1400_X = "163WC1400X"
    VALUE_163_WC1500_X = "163WC1500X"
    VALUE_163_WC2100_X = "163WC2100X"
    VALUE_163_WC1600_X = "163WC1600X"
    VALUE_163_WC0200_X = "163WC0200X"
    VALUE_163_WD0400_X = "163WD0400X"
    VALUE_163_WD1100_X = "163WD1100X"
    VALUE_163_WE0003_X = "163WE0003X"
    VALUE_163_WE0900_X = "163WE0900X"
    VALUE_163_WF0300_X = "163WF0300X"
    VALUE_163_WG0100_X = "163WG0100X"
    VALUE_163_WG0000_X = "163WG0000X"
    VALUE_163_WG0600_X = "163WG0600X"
    VALUE_163_WH0500_X = "163WH0500X"
    VALUE_163_WH0200_X = "163WH0200X"
    VALUE_163_WH1000_X = "163WH1000X"
    VALUE_163_WI0600_X = "163WI0600X"
    VALUE_163_WI0500_X = "163WI0500X"
    VALUE_163_WL0100_X = "163WL0100X"
    VALUE_163_WM0102_X = "163WM0102X"
    VALUE_163_WM0705_X = "163WM0705X"
    VALUE_163_WN0002_X = "163WN0002X"
    VALUE_163_WN0003_X = "163WN0003X"
    VALUE_163_WN0300_X = "163WN0300X"
    VALUE_163_WN0800_X = "163WN0800X"
    VALUE_163_WM1400_X = "163WM1400X"
    VALUE_163_WN1003_X = "163WN1003X"
    VALUE_163_WX0002_X = "163WX0002X"
    VALUE_163_WX0003_X = "163WX0003X"
    VALUE_163_WX0106_X = "163WX0106X"
    VALUE_163_WX0200_X = "163WX0200X"
    VALUE_163_WX1100_X = "163WX1100X"
    VALUE_163_WX0800_X = "163WX0800X"
    VALUE_163_WX1500_X = "163WX1500X"
    VALUE_163_WX0601_X = "163WX0601X"
    VALUE_163_WP0000_X = "163WP0000X"
    VALUE_163_WP0218_X = "163WP0218X"
    VALUE_163_WP0200_X = "163WP0200X"
    VALUE_163_WP1700_X = "163WP1700X"
    VALUE_163_WS0121_X = "163WS0121X"
    VALUE_163_WP0808_X = "163WP0808X"
    VALUE_163_WP0809_X = "163WP0809X"
    VALUE_163_WP0807_X = "163WP0807X"
    VALUE_163_WR0400_X = "163WR0400X"
    VALUE_163_WR1000_X = "163WR1000X"
    VALUE_163_WS0200_X = "163WS0200X"
    VALUE_163_WU0100_X = "163WU0100X"
    VALUE_163_WW0101_X = "163WW0101X"
    VALUE_163_WW0000_X = "163WW0000X"


class RehabilitationCounselorHipaa(Enum):
    """
    specDomain: S13625 (C-0-T13129-A13130-A13592-S13625-cpt)
    :cvar VALUE_225_C00000_N:
    :cvar VALUE_225_CA2400_N:
    """
    VALUE_225_C00000_N = "225C00000N"
    VALUE_225_CA2400_N = "225CA2400N"


class RehabilitationCounselorProviderCodes(Enum):
    """
    specDomain: S20563 (C-0-T19465-S20532-S20563-cpt)
    :cvar VALUE_225_C00000_X:
    :cvar VALUE_225_CA2400_X:
    :cvar VALUE_225_CA2500_X:
    """
    VALUE_225_C00000_X = "225C00000X"
    VALUE_225_CA2400_X = "225CA2400X"
    VALUE_225_CA2500_X = "225CA2500X"


class RehabilitationHospital(Enum):
    """
    specDomain: S10604 (C-0-T12206-A17660-A19450-A10588-S10602-S10604-cpt)
    :cvar RH:
    :cvar VALUE_283_XC2000_N:
    """
    RH = "RH"
    VALUE_283_XC2000_N = "283XC2000N"


class RehabilitationHospitalProviderCodes(Enum):
    """
    specDomain: S20746 (C-0-T19465-S20733-S20746-cpt)
    :cvar VALUE_283_X00000_X:
    :cvar VALUE_283_XC2000_X:
    """
    VALUE_283_X00000_X = "283X00000X"
    VALUE_283_XC2000_X = "283XC2000X"


class RejectedEditStatus(Enum):
    """
    specDomain: S11043 (C-0-T11040-S11043-cpt)
    :cvar R:
    """
    R = "R"


class RelatedReactionDetectedIssueCode(Enum):
    """
    specDomain: S16676 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16676-cpt)
    :cvar RREACT:
    :cvar RALG:
    :cvar RINT:
    :cvar RAR:
    """
    RREACT = "RREACT"
    RALG = "RALG"
    RINT = "RINT"
    RAR = "RAR"


class RelationalOperator(Enum):
    """
    vocSet: T209 (C-0-T209-cpt)
    :cvar CT:
    :cvar EQ:
    :cvar GN:
    :cvar GT:
    :cvar GE:
    :cvar LT:
    :cvar LE:
    :cvar NE:
    """
    CT = "CT"
    EQ = "EQ"
    GN = "GN"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"
    NE = "NE"


class RelationshipConjunction(Enum):
    """
    vocSet: T10365 (C-0-T10365-cpt)
    :cvar AND_VALUE:
    :cvar XOR:
    :cvar OR_VALUE:
    """
    AND_VALUE = "AND"
    XOR = "XOR"
    OR_VALUE = "OR"


class ReligiousAffiliation(Enum):
    """
    vocSet: T19185 (C-0-T19185-cpt)
    :cvar VALUE_1001:
    :cvar VALUE_1002:
    :cvar VALUE_1003:
    :cvar VALUE_1004:
    :cvar VALUE_1005:
    :cvar VALUE_1006:
    :cvar VALUE_1061:
    :cvar VALUE_1007:
    :cvar VALUE_1008:
    :cvar VALUE_1009:
    :cvar VALUE_1010:
    :cvar VALUE_1062:
    :cvar VALUE_1011:
    :cvar VALUE_1012:
    :cvar VALUE_1013:
    :cvar VALUE_1063:
    :cvar VALUE_1064:
    :cvar VALUE_1065:
    :cvar VALUE_1014:
    :cvar VALUE_1066:
    :cvar VALUE_1015:
    :cvar VALUE_1067:
    :cvar VALUE_1016:
    :cvar VALUE_1068:
    :cvar VALUE_1069:
    :cvar VALUE_1070:
    :cvar VALUE_1017:
    :cvar VALUE_1018:
    :cvar VALUE_1071:
    :cvar VALUE_1072:
    :cvar VALUE_1019:
    :cvar VALUE_1020:
    :cvar VALUE_1021:
    :cvar VALUE_1022:
    :cvar VALUE_1023:
    :cvar VALUE_1024:
    :cvar VALUE_1025:
    :cvar VALUE_1026:
    :cvar VALUE_1027:
    :cvar VALUE_1028:
    :cvar VALUE_1029:
    :cvar VALUE_1030:
    :cvar VALUE_1031:
    :cvar VALUE_1073:
    :cvar VALUE_1032:
    :cvar VALUE_1074:
    :cvar VALUE_1075:
    :cvar VALUE_1033:
    :cvar VALUE_1035:
    :cvar VALUE_1036:
    :cvar VALUE_1037:
    :cvar VALUE_1038:
    :cvar VALUE_1076:
    :cvar VALUE_1039:
    :cvar VALUE_1077:
    :cvar VALUE_1078:
    :cvar VALUE_1079:
    :cvar VALUE_1040:
    :cvar VALUE_1041:
    :cvar VALUE_1080:
    :cvar VALUE_1042:
    :cvar VALUE_1043:
    :cvar VALUE_1044:
    :cvar VALUE_1045:
    :cvar VALUE_1046:
    :cvar VALUE_1047:
    :cvar VALUE_1048:
    :cvar VALUE_1049:
    :cvar VALUE_1050:
    :cvar VALUE_1051:
    :cvar VALUE_1081:
    :cvar VALUE_1052:
    :cvar VALUE_1082:
    :cvar VALUE_1053:
    :cvar VALUE_1054:
    :cvar VALUE_1055:
    :cvar VALUE_1056:
    :cvar VALUE_1057:
    :cvar VALUE_1058:
    :cvar VALUE_1059:
    :cvar VALUE_1060:
    :cvar VALUE_1034:
    """
    VALUE_1001 = "1001"
    VALUE_1002 = "1002"
    VALUE_1003 = "1003"
    VALUE_1004 = "1004"
    VALUE_1005 = "1005"
    VALUE_1006 = "1006"
    VALUE_1061 = "1061"
    VALUE_1007 = "1007"
    VALUE_1008 = "1008"
    VALUE_1009 = "1009"
    VALUE_1010 = "1010"
    VALUE_1062 = "1062"
    VALUE_1011 = "1011"
    VALUE_1012 = "1012"
    VALUE_1013 = "1013"
    VALUE_1063 = "1063"
    VALUE_1064 = "1064"
    VALUE_1065 = "1065"
    VALUE_1014 = "1014"
    VALUE_1066 = "1066"
    VALUE_1015 = "1015"
    VALUE_1067 = "1067"
    VALUE_1016 = "1016"
    VALUE_1068 = "1068"
    VALUE_1069 = "1069"
    VALUE_1070 = "1070"
    VALUE_1017 = "1017"
    VALUE_1018 = "1018"
    VALUE_1071 = "1071"
    VALUE_1072 = "1072"
    VALUE_1019 = "1019"
    VALUE_1020 = "1020"
    VALUE_1021 = "1021"
    VALUE_1022 = "1022"
    VALUE_1023 = "1023"
    VALUE_1024 = "1024"
    VALUE_1025 = "1025"
    VALUE_1026 = "1026"
    VALUE_1027 = "1027"
    VALUE_1028 = "1028"
    VALUE_1029 = "1029"
    VALUE_1030 = "1030"
    VALUE_1031 = "1031"
    VALUE_1073 = "1073"
    VALUE_1032 = "1032"
    VALUE_1074 = "1074"
    VALUE_1075 = "1075"
    VALUE_1033 = "1033"
    VALUE_1035 = "1035"
    VALUE_1036 = "1036"
    VALUE_1037 = "1037"
    VALUE_1038 = "1038"
    VALUE_1076 = "1076"
    VALUE_1039 = "1039"
    VALUE_1077 = "1077"
    VALUE_1078 = "1078"
    VALUE_1079 = "1079"
    VALUE_1040 = "1040"
    VALUE_1041 = "1041"
    VALUE_1080 = "1080"
    VALUE_1042 = "1042"
    VALUE_1043 = "1043"
    VALUE_1044 = "1044"
    VALUE_1045 = "1045"
    VALUE_1046 = "1046"
    VALUE_1047 = "1047"
    VALUE_1048 = "1048"
    VALUE_1049 = "1049"
    VALUE_1050 = "1050"
    VALUE_1051 = "1051"
    VALUE_1081 = "1081"
    VALUE_1052 = "1052"
    VALUE_1082 = "1082"
    VALUE_1053 = "1053"
    VALUE_1054 = "1054"
    VALUE_1055 = "1055"
    VALUE_1056 = "1056"
    VALUE_1057 = "1057"
    VALUE_1058 = "1058"
    VALUE_1059 = "1059"
    VALUE_1060 = "1060"
    VALUE_1034 = "1034"


class RepetitionsOutOfRange(Enum):
    """
    specDomain: S21662 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-S21662-cpt)
    :cvar REP_RANGE:
    :cvar MAXOCCURS:
    :cvar MINOCCURS:
    """
    REP_RANGE = "REP_RANGE"
    MAXOCCURS = "MAXOCCURS"
    MINOCCURS = "MINOCCURS"


class ResearchSubjectRoleBasis(Enum):
    """
    abstDomain: A19417 (C-0-T12206-A19417-cpt)
    :cvar ERL:
    :cvar SCN:
    """
    ERL = "ERL"
    SCN = "SCN"


class ResidentialTreatmentFacilitiesProviderCodes(Enum):
    """
    specDomain: S20766 (C-0-T19465-S20766-cpt)
    :cvar VALUE_324500000_X:
    :cvar VALUE_3245_S0500_X:
    :cvar VALUE_320000000_X:
    :cvar VALUE_320800000_X:
    :cvar VALUE_320900000_X:
    :cvar VALUE_323_P00000_X:
    :cvar VALUE_322_D00000_X:
    :cvar VALUE_320600000_X:
    :cvar VALUE_320700000_X:
    """
    VALUE_324500000_X = "324500000X"
    VALUE_3245_S0500_X = "3245S0500X"
    VALUE_320000000_X = "320000000X"
    VALUE_320800000_X = "320800000X"
    VALUE_320900000_X = "320900000X"
    VALUE_323_P00000_X = "323P00000X"
    VALUE_322_D00000_X = "322D00000X"
    VALUE_320600000_X = "320600000X"
    VALUE_320700000_X = "320700000X"


class ResidentialTreatmentPracticeSetting(Enum):
    """
    specDomain: S10607 (C-0-T12206-A17660-A19450-A10588-S10607-cpt)
    :cvar RTF:
    :cvar PRC:
    :cvar VALUE_324500000_N:
    :cvar SURF:
    """
    RTF = "RTF"
    PRC = "PRC"
    VALUE_324500000_N = "324500000N"
    SURF = "SURF"


class ResourceGroupEntityType(Enum):
    """
    abstDomain: A19652 (C-0-T16040-A19652-cpt)
    :cvar PRAC:
    """
    PRAC = "PRAC"


class RespiratoryAndOrRehabilitativeAndOrRestorativeProviderHipaa(Enum):
    """
    abstDomain: A13592 (C-0-T13129-A13130-A13592-cpt)
    :cvar VALUE_225_X00000_N:
    :cvar VALUE_225_XC0400_N:
    :cvar VALUE_225_XE1200_N:
    :cvar VALUE_225_XH1200_N:
    :cvar VALUE_225_XH1300_N:
    :cvar VALUE_225_XN1300_N:
    :cvar VALUE_225_XP0200_N:
    :cvar VALUE_225_XR0403_N:
    :cvar VALUE_225100000_N:
    :cvar VALUE_2251_C2600_N:
    :cvar VALUE_2251_C0400_N:
    :cvar VALUE_2251_E1300_N:
    :cvar VALUE_2251_E1200_N:
    :cvar VALUE_2251_G0304_N:
    :cvar VALUE_2251_H1200_N:
    :cvar VALUE_2251_H1300_N:
    :cvar VALUE_2251_N0400_N:
    :cvar VALUE_2251_X0800_N:
    :cvar VALUE_2251_P0200_N:
    :cvar VALUE_2251_S0007_N:
    :cvar VALUE_225_C00000_N:
    :cvar VALUE_225_CA2400_N:
    :cvar VALUE_2255_A2300_N:
    :cvar VALUE_2255_R0406_N:
    :cvar VALUE_225900000_N:
    :cvar VALUE_2259_P1700_N:
    :cvar VALUE_221700000_N:
    :cvar VALUE_225600000_N:
    :cvar VALUE_226300000_N:
    :cvar VALUE_225700000_N:
    :cvar VALUE_225_A00000_N:
    :cvar VALUE_224_Z00000_N:
    :cvar VALUE_225000000_N:
    :cvar VALUE_222_Z00000_N:
    :cvar VALUE_225200000_N:
    :cvar VALUE_224_P00000_N:
    :cvar VALUE_225_B00000_N:
    :cvar VALUE_225800000_N:
    :cvar VALUE_225400000_N:
    """
    VALUE_225_X00000_N = "225X00000N"
    VALUE_225_XC0400_N = "225XC0400N"
    VALUE_225_XE1200_N = "225XE1200N"
    VALUE_225_XH1200_N = "225XH1200N"
    VALUE_225_XH1300_N = "225XH1300N"
    VALUE_225_XN1300_N = "225XN1300N"
    VALUE_225_XP0200_N = "225XP0200N"
    VALUE_225_XR0403_N = "225XR0403N"
    VALUE_225100000_N = "225100000N"
    VALUE_2251_C2600_N = "2251C2600N"
    VALUE_2251_C0400_N = "2251C0400N"
    VALUE_2251_E1300_N = "2251E1300N"
    VALUE_2251_E1200_N = "2251E1200N"
    VALUE_2251_G0304_N = "2251G0304N"
    VALUE_2251_H1200_N = "2251H1200N"
    VALUE_2251_H1300_N = "2251H1300N"
    VALUE_2251_N0400_N = "2251N0400N"
    VALUE_2251_X0800_N = "2251X0800N"
    VALUE_2251_P0200_N = "2251P0200N"
    VALUE_2251_S0007_N = "2251S0007N"
    VALUE_225_C00000_N = "225C00000N"
    VALUE_225_CA2400_N = "225CA2400N"
    VALUE_2255_A2300_N = "2255A2300N"
    VALUE_2255_R0406_N = "2255R0406N"
    VALUE_225900000_N = "225900000N"
    VALUE_2259_P1700_N = "2259P1700N"
    VALUE_221700000_N = "221700000N"
    VALUE_225600000_N = "225600000N"
    VALUE_226300000_N = "226300000N"
    VALUE_225700000_N = "225700000N"
    VALUE_225_A00000_N = "225A00000N"
    VALUE_224_Z00000_N = "224Z00000N"
    VALUE_225000000_N = "225000000N"
    VALUE_222_Z00000_N = "222Z00000N"
    VALUE_225200000_N = "225200000N"
    VALUE_224_P00000_N = "224P00000N"
    VALUE_225_B00000_N = "225B00000N"
    VALUE_225800000_N = "225800000N"
    VALUE_225400000_N = "225400000N"


class RespiratoryAndOrRehabilitativeAndOrRestorativeSpecialistOrTechnologistHipaa(Enum):
    """
    abstDomain: A13631 (C-0-T13129-A13130-A13592-A13631-cpt)
    :cvar VALUE_2255_A2300_N:
    :cvar VALUE_2255_R0406_N:
    """
    VALUE_2255_A2300_N = "2255A2300N"
    VALUE_2255_R0406_N = "2255R0406N"


class RespiratoryRehabilitativeandRestorativeServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20532 (C-0-T19465-S20532-cpt)
    :cvar VALUE_225_X00000_X:
    :cvar VALUE_225_XE1200_X:
    :cvar VALUE_225_XH1200_X:
    :cvar VALUE_225_XH1300_X:
    :cvar VALUE_225_XN1300_X:
    :cvar VALUE_225_XP0200_X:
    :cvar VALUE_225_XR0403_X:
    :cvar VALUE_225100000_X:
    :cvar VALUE_2251_C2600_X:
    :cvar VALUE_2251_E1300_X:
    :cvar VALUE_2251_E1200_X:
    :cvar VALUE_2251_G0304_X:
    :cvar VALUE_2251_H1200_X:
    :cvar VALUE_2251_H1300_X:
    :cvar VALUE_2251_N0400_X:
    :cvar VALUE_2251_X0800_X:
    :cvar VALUE_2251_P0200_X:
    :cvar VALUE_2251_S0007_X:
    :cvar VALUE_225_C00000_X:
    :cvar VALUE_225_CA2400_X:
    :cvar VALUE_225_CA2500_X:
    :cvar VALUE_227800000_X:
    :cvar VALUE_2278_C0205_X:
    :cvar VALUE_2278_E0002_X:
    :cvar VALUE_2278_G1100_X:
    :cvar VALUE_2278_G0305_X:
    :cvar VALUE_2278_H0200_X:
    :cvar VALUE_2278_P3900_X:
    :cvar VALUE_2278_P3800_X:
    :cvar VALUE_2278_E1000_X:
    :cvar VALUE_2278_P4000_X:
    :cvar VALUE_2278_P1004_X:
    :cvar VALUE_2278_P1006_X:
    :cvar VALUE_2278_P1005_X:
    :cvar VALUE_2278_S1500_X:
    :cvar VALUE_227900000_X:
    :cvar VALUE_2279_C0205_X:
    :cvar VALUE_2279_E0002_X:
    :cvar VALUE_2279_G1100_X:
    :cvar VALUE_2279_G0305_X:
    :cvar VALUE_2279_H0200_X:
    :cvar VALUE_2279_P3900_X:
    :cvar VALUE_2279_P3800_X:
    :cvar VALUE_2279_E1000_X:
    :cvar VALUE_2279_P4000_X:
    :cvar VALUE_2279_P1004_X:
    :cvar VALUE_2279_P1006_X:
    :cvar VALUE_2279_P1005_X:
    :cvar VALUE_2279_S1500_X:
    :cvar VALUE_225500000_X:
    :cvar VALUE_2255_A2300_X:
    :cvar VALUE_2255_R0406_X:
    :cvar VALUE_220000000_X:
    :cvar VALUE_221700000_X:
    :cvar VALUE_225600000_X:
    :cvar VALUE_226300000_X:
    :cvar VALUE_225700000_X:
    :cvar VALUE_225_A00000_X:
    :cvar VALUE_224_Z00000_X:
    :cvar VALUE_225000000_X:
    :cvar VALUE_222_Z00000_X:
    :cvar VALUE_225200000_X:
    :cvar VALUE_224_P00000_X:
    :cvar VALUE_225_B00000_X:
    :cvar VALUE_225800000_X:
    :cvar VALUE_225400000_X:
    """
    VALUE_225_X00000_X = "225X00000X"
    VALUE_225_XE1200_X = "225XE1200X"
    VALUE_225_XH1200_X = "225XH1200X"
    VALUE_225_XH1300_X = "225XH1300X"
    VALUE_225_XN1300_X = "225XN1300X"
    VALUE_225_XP0200_X = "225XP0200X"
    VALUE_225_XR0403_X = "225XR0403X"
    VALUE_225100000_X = "225100000X"
    VALUE_2251_C2600_X = "2251C2600X"
    VALUE_2251_E1300_X = "2251E1300X"
    VALUE_2251_E1200_X = "2251E1200X"
    VALUE_2251_G0304_X = "2251G0304X"
    VALUE_2251_H1200_X = "2251H1200X"
    VALUE_2251_H1300_X = "2251H1300X"
    VALUE_2251_N0400_X = "2251N0400X"
    VALUE_2251_X0800_X = "2251X0800X"
    VALUE_2251_P0200_X = "2251P0200X"
    VALUE_2251_S0007_X = "2251S0007X"
    VALUE_225_C00000_X = "225C00000X"
    VALUE_225_CA2400_X = "225CA2400X"
    VALUE_225_CA2500_X = "225CA2500X"
    VALUE_227800000_X = "227800000X"
    VALUE_2278_C0205_X = "2278C0205X"
    VALUE_2278_E0002_X = "2278E0002X"
    VALUE_2278_G1100_X = "2278G1100X"
    VALUE_2278_G0305_X = "2278G0305X"
    VALUE_2278_H0200_X = "2278H0200X"
    VALUE_2278_P3900_X = "2278P3900X"
    VALUE_2278_P3800_X = "2278P3800X"
    VALUE_2278_E1000_X = "2278E1000X"
    VALUE_2278_P4000_X = "2278P4000X"
    VALUE_2278_P1004_X = "2278P1004X"
    VALUE_2278_P1006_X = "2278P1006X"
    VALUE_2278_P1005_X = "2278P1005X"
    VALUE_2278_S1500_X = "2278S1500X"
    VALUE_227900000_X = "227900000X"
    VALUE_2279_C0205_X = "2279C0205X"
    VALUE_2279_E0002_X = "2279E0002X"
    VALUE_2279_G1100_X = "2279G1100X"
    VALUE_2279_G0305_X = "2279G0305X"
    VALUE_2279_H0200_X = "2279H0200X"
    VALUE_2279_P3900_X = "2279P3900X"
    VALUE_2279_P3800_X = "2279P3800X"
    VALUE_2279_E1000_X = "2279E1000X"
    VALUE_2279_P4000_X = "2279P4000X"
    VALUE_2279_P1004_X = "2279P1004X"
    VALUE_2279_P1006_X = "2279P1006X"
    VALUE_2279_P1005_X = "2279P1005X"
    VALUE_2279_S1500_X = "2279S1500X"
    VALUE_225500000_X = "225500000X"
    VALUE_2255_A2300_X = "2255A2300X"
    VALUE_2255_R0406_X = "2255R0406X"
    VALUE_220000000_X = "220000000X"
    VALUE_221700000_X = "221700000X"
    VALUE_225600000_X = "225600000X"
    VALUE_226300000_X = "226300000X"
    VALUE_225700000_X = "225700000X"
    VALUE_225_A00000_X = "225A00000X"
    VALUE_224_Z00000_X = "224Z00000X"
    VALUE_225000000_X = "225000000X"
    VALUE_222_Z00000_X = "222Z00000X"
    VALUE_225200000_X = "225200000X"
    VALUE_224_P00000_X = "224P00000X"
    VALUE_225_B00000_X = "225B00000X"
    VALUE_225800000_X = "225800000X"
    VALUE_225400000_X = "225400000X"


class RespiratoryTherapistCertifiedProviderCodes(Enum):
    """
    specDomain: S20567 (C-0-T19465-S20532-S20567-cpt)
    :cvar VALUE_227800000_X:
    :cvar VALUE_2278_C0205_X:
    :cvar VALUE_2278_E0002_X:
    :cvar VALUE_2278_G1100_X:
    :cvar VALUE_2278_G0305_X:
    :cvar VALUE_2278_H0200_X:
    :cvar VALUE_2278_P3900_X:
    :cvar VALUE_2278_P3800_X:
    :cvar VALUE_2278_E1000_X:
    :cvar VALUE_2278_P4000_X:
    :cvar VALUE_2278_P1004_X:
    :cvar VALUE_2278_P1006_X:
    :cvar VALUE_2278_P1005_X:
    :cvar VALUE_2278_S1500_X:
    """
    VALUE_227800000_X = "227800000X"
    VALUE_2278_C0205_X = "2278C0205X"
    VALUE_2278_E0002_X = "2278E0002X"
    VALUE_2278_G1100_X = "2278G1100X"
    VALUE_2278_G0305_X = "2278G0305X"
    VALUE_2278_H0200_X = "2278H0200X"
    VALUE_2278_P3900_X = "2278P3900X"
    VALUE_2278_P3800_X = "2278P3800X"
    VALUE_2278_E1000_X = "2278E1000X"
    VALUE_2278_P4000_X = "2278P4000X"
    VALUE_2278_P1004_X = "2278P1004X"
    VALUE_2278_P1006_X = "2278P1006X"
    VALUE_2278_P1005_X = "2278P1005X"
    VALUE_2278_S1500_X = "2278S1500X"


class RespiratoryTherapistHipaa(Enum):
    """
    specDomain: S13629 (C-0-T13129-A13130-A13592-S13629-cpt)
    :cvar VALUE_225900000_N:
    :cvar VALUE_2259_P1700_N:
    """
    VALUE_225900000_N = "225900000N"
    VALUE_2259_P1700_N = "2259P1700N"


class RespiratoryTherapistRegisteredProviderCodes(Enum):
    """
    specDomain: S20581 (C-0-T19465-S20532-S20581-cpt)
    :cvar VALUE_227900000_X:
    :cvar VALUE_2279_C0205_X:
    :cvar VALUE_2279_E0002_X:
    :cvar VALUE_2279_G1100_X:
    :cvar VALUE_2279_G0305_X:
    :cvar VALUE_2279_H0200_X:
    :cvar VALUE_2279_P3900_X:
    :cvar VALUE_2279_P3800_X:
    :cvar VALUE_2279_E1000_X:
    :cvar VALUE_2279_P4000_X:
    :cvar VALUE_2279_P1004_X:
    :cvar VALUE_2279_P1006_X:
    :cvar VALUE_2279_P1005_X:
    :cvar VALUE_2279_S1500_X:
    """
    VALUE_227900000_X = "227900000X"
    VALUE_2279_C0205_X = "2279C0205X"
    VALUE_2279_E0002_X = "2279E0002X"
    VALUE_2279_G1100_X = "2279G1100X"
    VALUE_2279_G0305_X = "2279G0305X"
    VALUE_2279_H0200_X = "2279H0200X"
    VALUE_2279_P3900_X = "2279P3900X"
    VALUE_2279_P3800_X = "2279P3800X"
    VALUE_2279_E1000_X = "2279E1000X"
    VALUE_2279_P4000_X = "2279P4000X"
    VALUE_2279_P1004_X = "2279P1004X"
    VALUE_2279_P1006_X = "2279P1006X"
    VALUE_2279_P1005_X = "2279P1005X"
    VALUE_2279_S1500_X = "2279S1500X"


class RespiteCareFacilityProviderCodes(Enum):
    """
    specDomain: S20770 (C-0-T19465-S20770-cpt)
    :cvar VALUE_385_H00000_X:
    :cvar VALUE_385_HR2050_X:
    :cvar VALUE_385_HR2055_X:
    :cvar VALUE_385_HR2060_X:
    :cvar VALUE_385_HR2065_X:
    :cvar VALUE_380000000_X:
    """
    VALUE_385_H00000_X = "385H00000X"
    VALUE_385_HR2050_X = "385HR2050X"
    VALUE_385_HR2055_X = "385HR2055X"
    VALUE_385_HR2060_X = "385HR2060X"
    VALUE_385_HR2065_X = "385HR2065X"
    VALUE_380000000_X = "380000000X"


class RespiteCareProviderCodes(Enum):
    """
    specDomain: S20771 (C-0-T19465-S20770-S20771-cpt)
    :cvar VALUE_385_H00000_X:
    :cvar VALUE_385_HR2050_X:
    :cvar VALUE_385_HR2055_X:
    :cvar VALUE_385_HR2060_X:
    :cvar VALUE_385_HR2065_X:
    """
    VALUE_385_H00000_X = "385H00000X"
    VALUE_385_HR2050_X = "385HR2050X"
    VALUE_385_HR2055_X = "385HR2055X"
    VALUE_385_HR2060_X = "385HR2060X"
    VALUE_385_HR2065_X = "385HR2065X"


class ResponseLevel(Enum):
    """
    vocSet: T14761 (C-0-T14761-cpt)
    :cvar C:
    :cvar F:
    :cvar D:
    :cvar E:
    :cvar N:
    :cvar R:
    :cvar X:
    """
    C = "C"
    F = "F"
    D = "D"
    E = "E"
    N = "N"
    R = "R"
    X = "X"


class ResponseModality(Enum):
    """
    vocSet: T394 (C-0-T394-cpt)
    :cvar B:
    :cvar T:
    :cvar R:
    """
    B = "B"
    T = "T"
    R = "R"


class ResponseMode(Enum):
    """
    vocSet: T19650 (C-0-T19650-cpt)
    :cvar D:
    :cvar I:
    :cvar Q:
    """
    D = "D"
    I = "I"
    Q = "Q"


class ResponsibleParty(Enum):
    """
    specDomain: S22030 (C-0-T12206-A19690-S22030-cpt)
    :cvar POWATT:
    :cvar DPOWATT:
    :cvar HPOWATT:
    :cvar SPOWATT:
    :cvar RESPRSN:
    :cvar EXCEST:
    :cvar GUARD:
    :cvar GUADLTM:
    """
    POWATT = "POWATT"
    DPOWATT = "DPOWATT"
    HPOWATT = "HPOWATT"
    SPOWATT = "SPOWATT"
    RESPRSN = "RESPRSN"
    EXCEST = "EXCEST"
    GUARD = "GUARD"
    GUADLTM = "GUADLTM"


class RetrobulbarRoute(Enum):
    """
    abstDomain: A17321 (C-0-T14581-A17021-A17321-cpt)
    :cvar RBINJ:
    """
    RBINJ = "RBINJ"


class RheumClinPracticeSetting(Enum):
    """
    specDomain: S10593 (C-0-T12206-A17660-A19450-A10588-S10589-S10593-cpt)
    :cvar RHEUM:
    :cvar PEDRHEUM:
    """
    RHEUM = "RHEUM"
    PEDRHEUM = "PEDRHEUM"


class Rinse(Enum):
    """
    abstDomain: A14730 (C-0-T14581-A16931-A14730-cpt)
    :cvar DENRINSE:
    :cvar ORRINSE:
    """
    DENRINSE = "DENRINSE"
    ORRINSE = "ORRINSE"


class Ritwan(Enum):
    """
    abstDomain: A18189 (C-0-T18130-A18131-A18189-cpt)
    :cvar X_YUR:
    """
    X_YUR = "x-YUR"


class River(Enum):
    """
    abstDomain: A18282 (C-0-T18130-A18241-A18274-A18275-A18282-cpt)
    :cvar X_MRC:
    :cvar X_MOV:
    :cvar X_YUM:
    """
    X_MRC = "x-MRC"
    X_MOV = "x-MOV"
    X_YUM = "x-YUM"


class RoleClassAgent(Enum):
    """
    specDomain: S14006 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-cpt)
    :cvar CON:
    :cvar ECON:
    :cvar NOK:
    :cvar ASSIGNED:
    :cvar COMPAR:
    :cvar SGNOFF:
    :cvar AGNT:
    :cvar GUARD:
    """
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"


class RoleClassAssignedEntity(Enum):
    """
    specDomain: S11595 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-S11595-cpt)
    :cvar CON:
    :cvar ECON:
    :cvar NOK:
    :cvar ASSIGNED:
    :cvar COMPAR:
    :cvar SGNOFF:
    """
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"


class RoleClassContact(Enum):
    """
    specDomain: S12205 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-S11595-S12205-cpt)
    :cvar CON:
    :cvar ECON:
    :cvar NOK:
    """
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"


class RoleClassCoveredParty(Enum):
    """
    specDomain: S14011 (C-0-T11555-S13940-A19313-A19316-A10416-S14011-cpt)
    :cvar NAMED:
    :cvar DEPEN:
    :cvar INDIV:
    :cvar SUBSCR:
    :cvar COVPTY:
    :cvar CLAIM:
    :cvar PROG:
    """
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    PROG = "PROG"


class RoleClassDistributedMaterial(Enum):
    """
    specDomain: S10418 (C-0-T11555-S13940-A19313-A19105-S10418-cpt)
    :cvar DST:
    :cvar RET:
    """
    DST = "DST"
    RET = "RET"


class RoleClassEmployee(Enum):
    """
    specDomain: S11569 (C-0-T11555-S13940-A19313-A19316-A10416-S11569-cpt)
    :cvar EMP:
    :cvar MIL:
    """
    EMP = "EMP"
    MIL = "MIL"


class RoleClassEquivalentEntity(Enum):
    """
    vocSet: O20270 (C-0-O20270-cpt)
    :cvar SAME:
    :cvar SUBY:
    """
    SAME = "SAME"
    SUBY = "SUBY"


class RoleClassExposureAgentCarrier(Enum):
    """
    specDomain: S22350 (C-0-T11555-S13940-A10429-S22350-cpt)
    :cvar EXPAGTCAR:
    :cvar EXPVECTOR:
    :cvar FOMITE:
    """
    EXPAGTCAR = "EXPAGTCAR"
    EXPVECTOR = "EXPVECTOR"
    FOMITE = "FOMITE"


class RoleClassInactiveIngredient(Enum):
    """
    specDomain: S19089 (C-0-T11555-S13940-A10429-S10430-S19089-cpt)
    :cvar IACT:
    :cvar COLR:
    :cvar FLVR:
    :cvar PRSV:
    :cvar STBL:
    """
    IACT = "IACT"
    COLR = "COLR"
    FLVR = "FLVR"
    PRSV = "PRSV"
    STBL = "STBL"


class RoleClassIngredientEntity(Enum):
    """
    specDomain: S10430 (C-0-T11555-S13940-A10429-S10430-cpt)
    :cvar IACT:
    :cvar COLR:
    :cvar FLVR:
    :cvar PRSV:
    :cvar STBL:
    :cvar ACTI:
    :cvar ACTIB:
    :cvar ACTIM:
    :cvar ACTIR:
    :cvar INGR:
    :cvar ADTV:
    :cvar BASE:
    """
    IACT = "IACT"
    COLR = "COLR"
    FLVR = "FLVR"
    PRSV = "PRSV"
    STBL = "STBL"
    ACTI = "ACTI"
    ACTIB = "ACTIB"
    ACTIM = "ACTIM"
    ACTIR = "ACTIR"
    INGR = "INGR"
    ADTV = "ADTV"
    BASE = "BASE"


class RoleClassIngredientEntityActiveIngredientByBot(Enum):
    """
    specDomain: S10433 (C-0-T11555-S13940-A10429-S10430-S10433-cpt)
    :cvar ACTI:
    :cvar ACTIB:
    :cvar ACTIM:
    :cvar ACTIR:
    """
    ACTI = "ACTI"
    ACTIB = "ACTIB"
    ACTIM = "ACTIM"
    ACTIR = "ACTIR"


class RoleClassInvestigationSubject(Enum):
    """
    specDomain: S21464 (C-0-T11555-S13940-A19313-A19316-A10416-S21464-cpt)
    :cvar INVSBJ:
    :cvar CASEBJ:
    :cvar RESBJ:
    """
    INVSBJ = "INVSBJ"
    CASEBJ = "CASEBJ"
    RESBJ = "RESBJ"


class RoleClassIsSpeciesEntity(Enum):
    """
    specDomain: S10441 (C-0-T11555-S13940-A10428-S10441-cpt)
    :cvar GEN:
    :cvar GRIC:
    """
    GEN = "GEN"
    GRIC = "GRIC"


class RoleClassLicensedEntity(Enum):
    """
    specDomain: S16773 (C-0-T11555-S13940-A19313-A19316-A10416-S16773-cpt)
    :cvar LIC:
    :cvar PROV:
    :cvar NOT_VALUE:
    """
    LIC = "LIC"
    PROV = "PROV"
    NOT_VALUE = "NOT"


class RoleClassLocatedEntity(Enum):
    """
    specDomain: S16815 (C-0-T11555-S13940-A10429-S16815-cpt)
    :cvar LOCE:
    :cvar STOR:
    """
    LOCE = "LOCE"
    STOR = "STOR"


class RoleClassManufacturedProduct(Enum):
    """
    specDomain: S11580 (C-0-T11555-S13940-A19313-A19105-S11580-cpt)
    :cvar MANU:
    :cvar THER:
    """
    MANU = "MANU"
    THER = "THER"


class RoleClassMutualRelationship(Enum):
    """
    abstDomain: A19316 (C-0-T11555-S13940-A19313-A19316-cpt)
    :cvar CON:
    :cvar ECON:
    :cvar NOK:
    :cvar ASSIGNED:
    :cvar COMPAR:
    :cvar SGNOFF:
    :cvar AGNT:
    :cvar GUARD:
    :cvar NAMED:
    :cvar DEPEN:
    :cvar INDIV:
    :cvar SUBSCR:
    :cvar COVPTY:
    :cvar CLAIM:
    :cvar PROG:
    :cvar EMP:
    :cvar MIL:
    :cvar INVSBJ:
    :cvar CASEBJ:
    :cvar RESBJ:
    :cvar LIC:
    :cvar PROV:
    :cvar NOT_VALUE:
    :cvar AFFL:
    :cvar CIT:
    :cvar CRINV:
    :cvar CRSPNSR:
    :cvar SPNSR:
    :cvar GUAR:
    :cvar PAYOR:
    :cvar PAT:
    :cvar PAYEE:
    :cvar POLHOLD:
    :cvar QUAL:
    :cvar STD:
    :cvar UNDWRT:
    :cvar CAREGIVER:
    :cvar PRS:
    """
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    PROG = "PROG"
    EMP = "EMP"
    MIL = "MIL"
    INVSBJ = "INVSBJ"
    CASEBJ = "CASEBJ"
    RESBJ = "RESBJ"
    LIC = "LIC"
    PROV = "PROV"
    NOT_VALUE = "NOT"
    AFFL = "AFFL"
    CIT = "CIT"
    CRINV = "CRINV"
    CRSPNSR = "CRSPNSR"
    SPNSR = "SPNSR"
    GUAR = "GUAR"
    PAYOR = "PAYOR"
    PAT = "PAT"
    PAYEE = "PAYEE"
    POLHOLD = "POLHOLD"
    QUAL = "QUAL"
    STD = "STD"
    UNDWRT = "UNDWRT"
    CAREGIVER = "CAREGIVER"
    PRS = "PRS"


class RoleClassNamedInsured(Enum):
    """
    specDomain: S21957 (C-0-T11555-S13940-A19313-A19316-A10416-S14011-S21957-cpt)
    :cvar NAMED:
    :cvar DEPEN:
    :cvar INDIV:
    :cvar SUBSCR:
    """
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"


class RoleClassOntological(Enum):
    """
    abstDomain: A10428 (C-0-T11555-S13940-A10428-cpt)
    :cvar GEN:
    :cvar GRIC:
    :cvar EQUIV:
    :cvar SAME:
    :cvar SUBY:
    :cvar INST:
    :cvar SUBS:
    """
    GEN = "GEN"
    GRIC = "GRIC"
    EQUIV = "EQUIV"
    SAME = "SAME"
    SUBY = "SUBY"
    INST = "INST"
    SUBS = "SUBS"


class RoleClassOntologicalEquivalentEntityByBot(Enum):
    """
    specDomain: S22399 (C-0-T11555-S13940-A10428-S22399-cpt)
    :cvar EQUIV:
    :cvar SAME:
    :cvar SUBY:
    """
    EQUIV = "EQUIV"
    SAME = "SAME"
    SUBY = "SUBY"


class RoleClassPartitive(Enum):
    """
    abstDomain: A10429 (C-0-T11555-S13940-A10429-cpt)
    :cvar EXPAGTCAR:
    :cvar EXPVECTOR:
    :cvar FOMITE:
    :cvar IACT:
    :cvar COLR:
    :cvar FLVR:
    :cvar PRSV:
    :cvar STBL:
    :cvar ACTI:
    :cvar ACTIB:
    :cvar ACTIM:
    :cvar ACTIR:
    :cvar INGR:
    :cvar ADTV:
    :cvar BASE:
    :cvar LOCE:
    :cvar STOR:
    :cvar PART:
    :cvar ACTM:
    :cvar SPEC:
    :cvar ALQT:
    :cvar ISLT:
    :cvar CONT:
    :cvar MBR:
    """
    EXPAGTCAR = "EXPAGTCAR"
    EXPVECTOR = "EXPVECTOR"
    FOMITE = "FOMITE"
    IACT = "IACT"
    COLR = "COLR"
    FLVR = "FLVR"
    PRSV = "PRSV"
    STBL = "STBL"
    ACTI = "ACTI"
    ACTIB = "ACTIB"
    ACTIM = "ACTIM"
    ACTIR = "ACTIR"
    INGR = "INGR"
    ADTV = "ADTV"
    BASE = "BASE"
    LOCE = "LOCE"
    STOR = "STOR"
    PART = "PART"
    ACTM = "ACTM"
    SPEC = "SPEC"
    ALQT = "ALQT"
    ISLT = "ISLT"
    CONT = "CONT"
    MBR = "MBR"


class RoleClassPartitivePartByBot(Enum):
    """
    specDomain: S19102 (C-0-T11555-S13940-A10429-S19102-cpt)
    :cvar PART:
    :cvar ACTM:
    """
    PART = "PART"
    ACTM = "ACTM"


class RoleClassPassive(Enum):
    """
    abstDomain: A19105 (C-0-T11555-S13940-A19313-A19105-cpt)
    :cvar DST:
    :cvar RET:
    :cvar MANU:
    :cvar THER:
    :cvar SDLOC:
    :cvar DSDLOC:
    :cvar ISDLOC:
    :cvar ADMM:
    :cvar ACCESS:
    :cvar BIRTHPL:
    :cvar EXPR:
    :cvar HLTHCHRT:
    :cvar HLD:
    :cvar IDENT:
    :cvar MNT:
    :cvar OWN:
    :cvar DEATHPLC:
    :cvar RGPR:
    :cvar TERR:
    :cvar WRTE:
    """
    DST = "DST"
    RET = "RET"
    MANU = "MANU"
    THER = "THER"
    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"
    ADMM = "ADMM"
    ACCESS = "ACCESS"
    BIRTHPL = "BIRTHPL"
    EXPR = "EXPR"
    HLTHCHRT = "HLTHCHRT"
    HLD = "HLD"
    IDENT = "IDENT"
    MNT = "MNT"
    OWN = "OWN"
    DEATHPLC = "DEATHPLC"
    RGPR = "RGPR"
    TERR = "TERR"
    WRTE = "WRTE"


class RoleClassRelationshipFormal(Enum):
    """
    abstDomain: A10416 (C-0-T11555-S13940-A19313-A19316-A10416-cpt)
    :cvar CON:
    :cvar ECON:
    :cvar NOK:
    :cvar ASSIGNED:
    :cvar COMPAR:
    :cvar SGNOFF:
    :cvar AGNT:
    :cvar GUARD:
    :cvar NAMED:
    :cvar DEPEN:
    :cvar INDIV:
    :cvar SUBSCR:
    :cvar COVPTY:
    :cvar CLAIM:
    :cvar PROG:
    :cvar EMP:
    :cvar MIL:
    :cvar INVSBJ:
    :cvar CASEBJ:
    :cvar RESBJ:
    :cvar LIC:
    :cvar PROV:
    :cvar NOT_VALUE:
    :cvar AFFL:
    :cvar CIT:
    :cvar CRINV:
    :cvar CRSPNSR:
    :cvar SPNSR:
    :cvar GUAR:
    :cvar PAYOR:
    :cvar PAT:
    :cvar PAYEE:
    :cvar POLHOLD:
    :cvar QUAL:
    :cvar STD:
    :cvar UNDWRT:
    """
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    PROG = "PROG"
    EMP = "EMP"
    MIL = "MIL"
    INVSBJ = "INVSBJ"
    CASEBJ = "CASEBJ"
    RESBJ = "RESBJ"
    LIC = "LIC"
    PROV = "PROV"
    NOT_VALUE = "NOT"
    AFFL = "AFFL"
    CIT = "CIT"
    CRINV = "CRINV"
    CRSPNSR = "CRSPNSR"
    SPNSR = "SPNSR"
    GUAR = "GUAR"
    PAYOR = "PAYOR"
    PAT = "PAT"
    PAYEE = "PAYEE"
    POLHOLD = "POLHOLD"
    QUAL = "QUAL"
    STD = "STD"
    UNDWRT = "UNDWRT"


class RoleClassServiceDeliveryLocation(Enum):
    """
    specDomain: S16927 (C-0-T11555-S13940-A19313-A19105-S16927-cpt)
    :cvar SDLOC:
    :cvar DSDLOC:
    :cvar ISDLOC:
    """
    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"


class RoleClassSpecimen(Enum):
    """
    specDomain: S11591 (C-0-T11555-S13940-A10429-S11591-cpt)
    :cvar SPEC:
    :cvar ALQT:
    :cvar ISLT:
    """
    SPEC = "SPEC"
    ALQT = "ALQT"
    ISLT = "ISLT"


class RoleLinkRelated(Enum):
    """
    specDomain: S21429 (C-0-T11603-S21429-cpt)
    :cvar REL:
    :cvar IDENT:
    :cvar DIRAUTH:
    :cvar INDAUTH:
    :cvar PART:
    :cvar BACKUP:
    :cvar REPL:
    """
    REL = "REL"
    IDENT = "IDENT"
    DIRAUTH = "DIRAUTH"
    INDAUTH = "INDAUTH"
    PART = "PART"
    BACKUP = "BACKUP"
    REPL = "REPL"


class RoleLinkType(Enum):
    """
    vocSet: T11603 (C-0-T11603-cpt)
    :cvar REL:
    :cvar IDENT:
    :cvar DIRAUTH:
    :cvar INDAUTH:
    :cvar PART:
    :cvar BACKUP:
    :cvar REPL:
    """
    REL = "REL"
    IDENT = "IDENT"
    DIRAUTH = "DIRAUTH"
    INDAUTH = "INDAUTH"
    PART = "PART"
    BACKUP = "BACKUP"
    REPL = "REPL"


class RoleStatus(Enum):
    """
    vocSet: T15999 (C-0-T15999-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar PENDING:
    :cvar SUSPENDED:
    :cvar TERMINATED:
    :cvar NULLIFIED:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PENDING = "pending"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"
    NULLIFIED = "nullified"


class RoleStatusNormal(Enum):
    """
    specDomain: S16000 (C-0-T15999-S16000-cpt)
    :cvar NORMAL:
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar PENDING:
    :cvar SUSPENDED:
    :cvar TERMINATED:
    """
    NORMAL = "normal"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PENDING = "pending"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"


class Sahaptian(Enum):
    """
    abstDomain: A18500 (C-0-T18130-A18413-A18498-A18500-cpt)
    :cvar X_WAR:
    :cvar X_UMA:
    :cvar X_WAA:
    :cvar X_YAK:
    """
    X_WAR = "x-WAR"
    X_UMA = "x-UMA"
    X_WAA = "x-WAA"
    X_YAK = "x-YAK"


class SaukFoxKickapoo(Enum):
    """
    abstDomain: A18164 (C-0-T18130-A18131-A18132-A18164-cpt)
    :cvar X_KIC:
    :cvar X_SAC:
    :cvar X_SJW:
    """
    X_KIC = "x-KIC"
    X_SAC = "x-SAC"
    X_SJW = "x-SJW"


class ScalpRoute(Enum):
    """
    abstDomain: A17323 (C-0-T14581-A17021-A17323-cpt)
    :cvar SCALP:
    """
    SCALP = "SCALP"


class SchedulingActReason(Enum):
    """
    abstDomain: A14879 (C-0-T14878-A14879-cpt)
    :cvar MTG:
    :cvar MED:
    :cvar FIN:
    :cvar DEC:
    :cvar PAT:
    :cvar PHY:
    :cvar BLK:
    """
    MTG = "MTG"
    MED = "MED"
    FIN = "FIN"
    DEC = "DEC"
    PAT = "PAT"
    PHY = "PHY"
    BLK = "BLK"


class Sequencing(Enum):
    """
    vocSet: T390 (C-0-T390-cpt)
    :cvar A:
    :cvar D:
    :cvar N:
    """
    A = "A"
    D = "D"
    N = "N"


class SerranoGabrielino(Enum):
    """
    abstDomain: A18622 (C-0-T18130-A18605-A18621-A18622-cpt)
    :cvar X_SER:
    """
    X_SER = "x-SER"


class SetOperator(Enum):
    """
    vocSet: T17416 (C-0-T17416-cpt)
    :cvar VALUE_SET_OPERATOR:
    :cvar H:
    :cvar E:
    :cvar I:
    :cvar A:
    :cvar P:
    """
    VALUE_SET_OPERATOR = "_ValueSetOperator"
    H = "H"
    E = "E"
    I = "I"
    A = "A"
    P = "P"


class SetUpdateMode(Enum):
    """
    abstDomain: A10024 (C-0-T10018-A10024-cpt)
    :cvar ESA:
    :cvar ESAC:
    :cvar ESC:
    :cvar ESD:
    """
    ESA = "ESA"
    ESAC = "ESAC"
    ESC = "ESC"
    ESD = "ESD"


class SeverityObservation(Enum):
    """
    abstDomain: A16643 (C-0-T16614-A16643-cpt)
    :cvar H:
    :cvar L:
    :cvar M:
    """
    H = "H"
    L = "L"
    M = "M"


class Shasta(Enum):
    """
    abstDomain: A18244 (C-0-T18130-A18241-A18244-cpt)
    :cvar X_SHT:
    """
    X_SHT = "x-SHT"


class Sibling(Enum):
    """
    specDomain: S11567 (C-0-T12206-A19563-S17926-S11567-cpt)
    :cvar HSIB:
    :cvar HBRO:
    :cvar HSIS:
    :cvar NSIB:
    :cvar NBRO:
    :cvar NSIS:
    :cvar SIBINLAW:
    :cvar BROINLAW:
    :cvar SISINLAW:
    :cvar STPSIB:
    :cvar STPBRO:
    :cvar STPSIS:
    :cvar SIB:
    :cvar BRO:
    :cvar SIS:
    """
    HSIB = "HSIB"
    HBRO = "HBRO"
    HSIS = "HSIS"
    NSIB = "NSIB"
    NBRO = "NBRO"
    NSIS = "NSIS"
    SIBINLAW = "SIBINLAW"
    BROINLAW = "BROINLAW"
    SISINLAW = "SISINLAW"
    STPSIB = "STPSIB"
    STPBRO = "STPBRO"
    STPSIS = "STPSIS"
    SIB = "SIB"
    BRO = "BRO"
    SIS = "SIS"


class SiblingInLaw(Enum):
    """
    specDomain: S19782 (C-0-T12206-A19563-S17926-S11567-S19782-cpt)
    :cvar SIBINLAW:
    :cvar BROINLAW:
    :cvar SISINLAW:
    """
    SIBINLAW = "SIBINLAW"
    BROINLAW = "BROINLAW"
    SISINLAW = "SISINLAW"


class SignificantOtherRoleType(Enum):
    """
    specDomain: S19755 (C-0-T12206-A19563-S17926-S19755-cpt)
    :cvar SPS:
    :cvar HUSB:
    :cvar WIFE:
    :cvar SIGOTHR:
    """
    SPS = "SPS"
    HUSB = "HUSB"
    WIFE = "WIFE"
    SIGOTHR = "SIGOTHR"


class SinusUnspecifiedRoute(Enum):
    """
    abstDomain: A17325 (C-0-T14581-A17021-A17325-cpt)
    :cvar ENDOSININJ:
    :cvar SININSTIL:
    """
    ENDOSININJ = "ENDOSININJ"
    SININSTIL = "SININSTIL"


class SirenikskiYupik(Enum):
    """
    abstDomain: A18193 (C-0-T18130-A18191-A18192-A18193-cpt)
    :cvar X_ESU:
    :cvar X_ESS:
    :cvar X_EMS:
    """
    X_ESU = "x-ESU"
    X_ESS = "x-ESS"
    X_EMS = "x-EMS"


class SkilledNursingFacilityProviderCodes(Enum):
    """
    specDomain: S20765 (C-0-T19465-S20758-S20765-cpt)
    :cvar VALUE_314000000_X:
    :cvar VALUE_3140_N1450_X:
    """
    VALUE_314000000_X = "314000000X"
    VALUE_3140_N1450_X = "3140N1450X"


class SkinRoute(Enum):
    """
    abstDomain: A17328 (C-0-T14581-A17021-A17328-cpt)
    :cvar OCDRESTA:
    :cvar SKIN:
    """
    OCDRESTA = "OCDRESTA"
    SKIN = "SKIN"


class SocialWorkerHipaa(Enum):
    """
    specDomain: S13171 (C-0-T13129-A13130-A13131-S13171-cpt)
    :cvar VALUE_104100000_N:
    :cvar VALUE_1041_C0700_N:
    :cvar VALUE_1041_S0200_N:
    """
    VALUE_104100000_N = "104100000N"
    VALUE_1041_C0700_N = "1041C0700N"
    VALUE_1041_S0200_N = "1041S0200N"


class SocialWorkerProviderCodes(Enum):
    """
    specDomain: S20305 (C-0-T19465-S20275-S20305-cpt)
    :cvar VALUE_104100000_X:
    :cvar VALUE_1041_C0700_X:
    :cvar VALUE_1041_S0200_X:
    """
    VALUE_104100000_X = "104100000X"
    VALUE_1041_C0700_X = "1041C0700X"
    VALUE_1041_S0200_X = "1041S0200X"


class SoftTissueRoute(Enum):
    """
    abstDomain: A17331 (C-0-T14581-A17021-A17331-cpt)
    :cvar SOFTISINJ:
    :cvar SOFTISINSTIL:
    """
    SOFTISINJ = "SOFTISINJ"
    SOFTISINSTIL = "SOFTISINSTIL"


class SolidDrugForm(Enum):
    """
    abstDomain: A14484 (C-0-T19651-A14411-A14412-A14484-cpt)
    :cvar BARSOAP:
    :cvar MEDBAR:
    :cvar BAR:
    :cvar CHEWBAR:
    :cvar PAD:
    :cvar MEDPAD:
    :cvar TPATCH:
    :cvar TPATH16:
    :cvar TPATH24:
    :cvar TPATH72:
    :cvar TPATH2_WK:
    :cvar TPATHWK:
    :cvar PATCH:
    :cvar ENTCAP:
    :cvar ERENTCAP:
    :cvar ERCAP:
    :cvar ERCAP12:
    :cvar ERCAP24:
    :cvar ERECCAP:
    :cvar ORCAP:
    :cvar CAP:
    :cvar BUCTAB:
    :cvar SRBUCTAB:
    :cvar ECTAB:
    :cvar ERECTAB:
    :cvar ERTAB:
    :cvar ERTAB12:
    :cvar ERTAB24:
    :cvar ORTAB:
    :cvar CAPLET:
    :cvar CHEWTAB:
    :cvar CPTAB:
    :cvar DRTAB:
    :cvar DISINTAB:
    :cvar ORTROCHE:
    :cvar SLTAB:
    :cvar TAB:
    :cvar VAGTAB:
    :cvar PILL:
    :cvar TOPPWD:
    :cvar RECPWD:
    :cvar VAGPWD:
    :cvar POWD:
    :cvar SUPP:
    :cvar RECSUPP:
    :cvar URETHSUPP:
    :cvar VAGSUPP:
    :cvar SWAB:
    :cvar MEDSWAB:
    :cvar BEAD:
    :cvar CAKE:
    :cvar CEMENT:
    :cvar GUM:
    :cvar CRYS:
    :cvar DISK:
    :cvar FLAKE:
    :cvar GRAN:
    :cvar PELLET:
    :cvar WAFER:
    """
    BARSOAP = "BARSOAP"
    MEDBAR = "MEDBAR"
    BAR = "BAR"
    CHEWBAR = "CHEWBAR"
    PAD = "PAD"
    MEDPAD = "MEDPAD"
    TPATCH = "TPATCH"
    TPATH16 = "TPATH16"
    TPATH24 = "TPATH24"
    TPATH72 = "TPATH72"
    TPATH2_WK = "TPATH2WK"
    TPATHWK = "TPATHWK"
    PATCH = "PATCH"
    ENTCAP = "ENTCAP"
    ERENTCAP = "ERENTCAP"
    ERCAP = "ERCAP"
    ERCAP12 = "ERCAP12"
    ERCAP24 = "ERCAP24"
    ERECCAP = "ERECCAP"
    ORCAP = "ORCAP"
    CAP = "CAP"
    BUCTAB = "BUCTAB"
    SRBUCTAB = "SRBUCTAB"
    ECTAB = "ECTAB"
    ERECTAB = "ERECTAB"
    ERTAB = "ERTAB"
    ERTAB12 = "ERTAB12"
    ERTAB24 = "ERTAB24"
    ORTAB = "ORTAB"
    CAPLET = "CAPLET"
    CHEWTAB = "CHEWTAB"
    CPTAB = "CPTAB"
    DRTAB = "DRTAB"
    DISINTAB = "DISINTAB"
    ORTROCHE = "ORTROCHE"
    SLTAB = "SLTAB"
    TAB = "TAB"
    VAGTAB = "VAGTAB"
    PILL = "PILL"
    TOPPWD = "TOPPWD"
    RECPWD = "RECPWD"
    VAGPWD = "VAGPWD"
    POWD = "POWD"
    SUPP = "SUPP"
    RECSUPP = "RECSUPP"
    URETHSUPP = "URETHSUPP"
    VAGSUPP = "VAGSUPP"
    SWAB = "SWAB"
    MEDSWAB = "MEDSWAB"
    BEAD = "BEAD"
    CAKE = "CAKE"
    CEMENT = "CEMENT"
    GUM = "GUM"
    CRYS = "CRYS"
    DISK = "DISK"
    FLAKE = "FLAKE"
    GRAN = "GRAN"
    PELLET = "PELLET"
    WAFER = "WAFER"


class SolutionDrugForm(Enum):
    """
    specDomain: S14419 (C-0-T19651-A14411-A14412-A14413-S14419-cpt)
    :cvar DROP:
    :cvar NDROP:
    :cvar OPDROP:
    :cvar ORDROP:
    :cvar OTDROP:
    :cvar IRSOL:
    :cvar DOUCHE:
    :cvar ENEMA:
    :cvar OPIRSOL:
    :cvar ORALSOL:
    :cvar ELIXIR:
    :cvar RINSE:
    :cvar SYRUP:
    :cvar TOPSOL:
    :cvar LIN:
    :cvar MUCTOPSOL:
    :cvar TINC:
    :cvar SOL:
    :cvar IPSOL:
    :cvar IVSOL:
    :cvar RECSOL:
    """
    DROP = "DROP"
    NDROP = "NDROP"
    OPDROP = "OPDROP"
    ORDROP = "ORDROP"
    OTDROP = "OTDROP"
    IRSOL = "IRSOL"
    DOUCHE = "DOUCHE"
    ENEMA = "ENEMA"
    OPIRSOL = "OPIRSOL"
    ORALSOL = "ORALSOL"
    ELIXIR = "ELIXIR"
    RINSE = "RINSE"
    SYRUP = "SYRUP"
    TOPSOL = "TOPSOL"
    LIN = "LIN"
    MUCTOPSOL = "MUCTOPSOL"
    TINC = "TINC"
    SOL = "SOL"
    IPSOL = "IPSOL"
    IVSOL = "IVSOL"
    RECSOL = "RECSOL"


class SouthernAlaska(Enum):
    """
    abstDomain: A18359 (C-0-T18130-A18352-A18356-A18358-A18359-cpt)
    :cvar X_AHT:
    :cvar X_TFN:
    """
    X_AHT = "x-AHT"
    X_TFN = "x-TFN"


class SouthernCaddoan(Enum):
    """
    abstDomain: A18233 (C-0-T18130-A18223-A18233-cpt)
    :cvar X_CAD:
    """
    X_CAD = "x-CAD"


class SouthernNumic(Enum):
    """
    abstDomain: A18617 (C-0-T18130-A18605-A18606-A18617-cpt)
    :cvar X_KAW:
    :cvar X_UTE:
    """
    X_KAW = "x-KAW"
    X_UTE = "x-UTE"


class SpecialistProviderCodes(Enum):
    """
    specDomain: S20448 (C-0-T19465-S20434-S20448-cpt)
    :cvar VALUE_174_M00000_X:
    :cvar VALUE_174_MM1900_X:
    :cvar VALUE_174400000_X:
    :cvar VALUE_1744_G0900_X:
    :cvar VALUE_1744_P3200_X:
    :cvar VALUE_1744_R1103_X:
    :cvar VALUE_1744_R1102_X:
    """
    VALUE_174_M00000_X = "174M00000X"
    VALUE_174_MM1900_X = "174MM1900X"
    VALUE_174400000_X = "174400000X"
    VALUE_1744_G0900_X = "1744G0900X"
    VALUE_1744_P3200_X = "1744P3200X"
    VALUE_1744_R1103_X = "1744R1103X"
    VALUE_1744_R1102_X = "1744R1102X"


class SpecialistTechnologistCardiovascularProviderCodes(Enum):
    """
    specDomain: S20623 (C-0-T19465-S20608-S20623-cpt)
    :cvar VALUE_246_X00000_X:
    :cvar VALUE_246_XC2901_X:
    :cvar VALUE_246_XS1301_X:
    :cvar VALUE_246_XC2903_X:
    """
    VALUE_246_X00000_X = "246X00000X"
    VALUE_246_XC2901_X = "246XC2901X"
    VALUE_246_XS1301_X = "246XS1301X"
    VALUE_246_XC2903_X = "246XC2903X"


class SpecialistTechnologistHealthInformationProviderCodes(Enum):
    """
    specDomain: S20627 (C-0-T19465-S20608-S20627-cpt)
    :cvar VALUE_246_Y00000_X:
    :cvar VALUE_246_YC3301_X:
    :cvar VALUE_246_YC3302_X:
    :cvar VALUE_246_YR1600_X:
    """
    VALUE_246_Y00000_X = "246Y00000X"
    VALUE_246_YC3301_X = "246YC3301X"
    VALUE_246_YC3302_X = "246YC3302X"
    VALUE_246_YR1600_X = "246YR1600X"


class SpecialistTechnologistOtherProviderCodes(Enum):
    """
    specDomain: S20631 (C-0-T19465-S20608-S20631-cpt)
    :cvar VALUE_246_Z00000_X:
    :cvar VALUE_246_ZA2600_X:
    :cvar VALUE_246_ZB0500_X:
    :cvar VALUE_246_ZB0301_X:
    :cvar VALUE_246_ZB0302_X:
    :cvar VALUE_246_ZB0600_X:
    :cvar VALUE_246_ZE0500_X:
    :cvar VALUE_246_ZE0600_X:
    :cvar VALUE_246_ZG1000_X:
    :cvar VALUE_246_ZG0701_X:
    :cvar VALUE_246_ZI1000_X:
    :cvar VALUE_246_ZN0300_X:
    :cvar VALUE_246_ZS0400_X:
    """
    VALUE_246_Z00000_X = "246Z00000X"
    VALUE_246_ZA2600_X = "246ZA2600X"
    VALUE_246_ZB0500_X = "246ZB0500X"
    VALUE_246_ZB0301_X = "246ZB0301X"
    VALUE_246_ZB0302_X = "246ZB0302X"
    VALUE_246_ZB0600_X = "246ZB0600X"
    VALUE_246_ZE0500_X = "246ZE0500X"
    VALUE_246_ZE0600_X = "246ZE0600X"
    VALUE_246_ZG1000_X = "246ZG1000X"
    VALUE_246_ZG0701_X = "246ZG0701X"
    VALUE_246_ZI1000_X = "246ZI1000X"
    VALUE_246_ZN0300_X = "246ZN0300X"
    VALUE_246_ZS0400_X = "246ZS0400X"


class SpecialistTechnologistPathologyProviderCodes(Enum):
    """
    specDomain: S20644 (C-0-T19465-S20608-S20644-cpt)
    :cvar VALUE_246_Q00000_X:
    :cvar VALUE_246_QB0000_X:
    :cvar VALUE_246_QC1000_X:
    :cvar VALUE_246_QC2700_X:
    :cvar VALUE_246_QH0401_X:
    :cvar VALUE_246_QH0000_X:
    :cvar VALUE_246_QH0600_X:
    :cvar VALUE_246_QI0000_X:
    :cvar VALUE_246_QL0900_X:
    :cvar VALUE_246_QL0901_X:
    :cvar VALUE_246_QM0706_X:
    :cvar VALUE_246_QM0900_X:
    """
    VALUE_246_Q00000_X = "246Q00000X"
    VALUE_246_QB0000_X = "246QB0000X"
    VALUE_246_QC1000_X = "246QC1000X"
    VALUE_246_QC2700_X = "246QC2700X"
    VALUE_246_QH0401_X = "246QH0401X"
    VALUE_246_QH0000_X = "246QH0000X"
    VALUE_246_QH0600_X = "246QH0600X"
    VALUE_246_QI0000_X = "246QI0000X"
    VALUE_246_QL0900_X = "246QL0900X"
    VALUE_246_QL0901_X = "246QL0901X"
    VALUE_246_QM0706_X = "246QM0706X"
    VALUE_246_QM0900_X = "246QM0900X"


class SpecialistTechnologistProviderCodes(Enum):
    """
    specDomain: S20595 (C-0-T19465-S20532-S20595-cpt)
    :cvar VALUE_225500000_X:
    :cvar VALUE_2255_A2300_X:
    :cvar VALUE_2255_R0406_X:
    """
    VALUE_225500000_X = "225500000X"
    VALUE_2255_A2300_X = "2255A2300X"
    VALUE_2255_R0406_X = "2255R0406X"


class SpecimenEntityType(Enum):
    """
    abstDomain: A19464 (C-0-T16040-A16041-A19464-cpt)
    :cvar ABS:
    :cvar AMN:
    :cvar ASP:
    :cvar BPH:
    :cvar BIFL:
    :cvar BLDCO:
    :cvar BLDA:
    :cvar BBL:
    :cvar BLDC:
    :cvar BPU:
    :cvar BLDV:
    :cvar FLU:
    :cvar BON:
    :cvar MILK:
    :cvar BRO:
    :cvar BRN:
    :cvar CALC:
    :cvar STON:
    :cvar CNL:
    :cvar CDM:
    :cvar CTP:
    :cvar CSF:
    :cvar CVM:
    :cvar CVX:
    :cvar COL:
    :cvar CNJT:
    :cvar CRN:
    :cvar CUR:
    :cvar CYST:
    :cvar DIAF:
    :cvar DOSE:
    :cvar DRN:
    :cvar DUFL:
    :cvar EAR:
    :cvar EARW:
    :cvar ELT:
    :cvar ENDC:
    :cvar ENDM:
    :cvar EOS:
    :cvar RBC:
    :cvar BRTH:
    :cvar EXG:
    :cvar EYE:
    :cvar FIB:
    :cvar FLT:
    :cvar FIST:
    :cvar FOOD:
    :cvar GAS:
    :cvar GAST:
    :cvar GEN:
    :cvar GENC:
    :cvar GENF:
    :cvar GENL:
    :cvar GENV:
    :cvar HAR:
    :cvar IHG:
    :cvar IT:
    :cvar ISLT:
    :cvar LAM:
    :cvar WBC:
    :cvar LN:
    :cvar LNA:
    :cvar LNV:
    :cvar LIQ:
    :cvar LYM:
    :cvar MAC:
    :cvar MAR:
    :cvar MEC:
    :cvar MBLD:
    :cvar MLK:
    :cvar NAIL:
    :cvar NOS:
    :cvar PAFL:
    :cvar PAT:
    :cvar PRT:
    :cvar PLC:
    :cvar PLAS:
    :cvar PLB:
    :cvar PPP:
    :cvar PRP:
    :cvar PLR:
    :cvar PMN:
    :cvar PUS:
    :cvar SAL:
    :cvar SMN:
    :cvar SMPLS:
    :cvar SER:
    :cvar SKM:
    :cvar SKN:
    :cvar SPRM:
    :cvar SPT:
    :cvar SPTC:
    :cvar SPTT:
    :cvar STL:
    :cvar SWT:
    :cvar SNV:
    :cvar TEAR:
    :cvar THRT:
    :cvar THRB:
    :cvar TISG:
    :cvar TLGI:
    :cvar TLNG:
    :cvar TISPL:
    :cvar TSMI:
    :cvar TISU:
    :cvar TISS:
    :cvar TUB:
    :cvar ULC:
    :cvar UMB:
    :cvar UMED:
    :cvar USUB:
    :cvar URTH:
    :cvar UR:
    :cvar URT:
    :cvar URC:
    :cvar URNS:
    :cvar VOM:
    :cvar WAT:
    :cvar BLD:
    :cvar BDY:
    :cvar WICK:
    :cvar WND:
    :cvar WNDA:
    :cvar WNDD:
    :cvar WNDE:
    """
    ABS = "ABS"
    AMN = "AMN"
    ASP = "ASP"
    BPH = "BPH"
    BIFL = "BIFL"
    BLDCO = "BLDCO"
    BLDA = "BLDA"
    BBL = "BBL"
    BLDC = "BLDC"
    BPU = "BPU"
    BLDV = "BLDV"
    FLU = "FLU"
    BON = "BON"
    MILK = "MILK"
    BRO = "BRO"
    BRN = "BRN"
    CALC = "CALC"
    STON = "STON"
    CNL = "CNL"
    CDM = "CDM"
    CTP = "CTP"
    CSF = "CSF"
    CVM = "CVM"
    CVX = "CVX"
    COL = "COL"
    CNJT = "CNJT"
    CRN = "CRN"
    CUR = "CUR"
    CYST = "CYST"
    DIAF = "DIAF"
    DOSE = "DOSE"
    DRN = "DRN"
    DUFL = "DUFL"
    EAR = "EAR"
    EARW = "EARW"
    ELT = "ELT"
    ENDC = "ENDC"
    ENDM = "ENDM"
    EOS = "EOS"
    RBC = "RBC"
    BRTH = "BRTH"
    EXG = "EXG"
    EYE = "EYE"
    FIB = "FIB"
    FLT = "FLT"
    FIST = "FIST"
    FOOD = "FOOD"
    GAS = "GAS"
    GAST = "GAST"
    GEN = "GEN"
    GENC = "GENC"
    GENF = "GENF"
    GENL = "GENL"
    GENV = "GENV"
    HAR = "HAR"
    IHG = "IHG"
    IT = "IT"
    ISLT = "ISLT"
    LAM = "LAM"
    WBC = "WBC"
    LN = "LN"
    LNA = "LNA"
    LNV = "LNV"
    LIQ = "LIQ"
    LYM = "LYM"
    MAC = "MAC"
    MAR = "MAR"
    MEC = "MEC"
    MBLD = "MBLD"
    MLK = "MLK"
    NAIL = "NAIL"
    NOS = "NOS"
    PAFL = "PAFL"
    PAT = "PAT"
    PRT = "PRT"
    PLC = "PLC"
    PLAS = "PLAS"
    PLB = "PLB"
    PPP = "PPP"
    PRP = "PRP"
    PLR = "PLR"
    PMN = "PMN"
    PUS = "PUS"
    SAL = "SAL"
    SMN = "SMN"
    SMPLS = "SMPLS"
    SER = "SER"
    SKM = "SKM"
    SKN = "SKN"
    SPRM = "SPRM"
    SPT = "SPT"
    SPTC = "SPTC"
    SPTT = "SPTT"
    STL = "STL"
    SWT = "SWT"
    SNV = "SNV"
    TEAR = "TEAR"
    THRT = "THRT"
    THRB = "THRB"
    TISG = "TISG"
    TLGI = "TLGI"
    TLNG = "TLNG"
    TISPL = "TISPL"
    TSMI = "TSMI"
    TISU = "TISU"
    TISS = "TISS"
    TUB = "TUB"
    ULC = "ULC"
    UMB = "UMB"
    UMED = "UMED"
    USUB = "USUB"
    URTH = "URTH"
    UR = "UR"
    URT = "URT"
    URC = "URC"
    URNS = "URNS"
    VOM = "VOM"
    WAT = "WAT"
    BLD = "BLD"
    BDY = "BDY"
    WICK = "WICK"
    WND = "WND"
    WNDA = "WNDA"
    WNDD = "WNDD"
    WNDE = "WNDE"


class SpecimenRoleType(Enum):
    """
    abstDomain: A16515 (C-0-T12206-A16515-cpt)
    :cvar Q:
    :cvar B:
    :cvar E:
    :cvar F:
    :cvar O:
    :cvar V:
    :cvar C:
    :cvar G:
    :cvar P:
    :cvar L:
    :cvar R:
    """
    Q = "Q"
    B = "B"
    E = "E"
    F = "F"
    O = "O"
    V = "V"
    C = "C"
    G = "G"
    P = "P"
    L = "L"
    R = "R"


class SpeechAndOrLanguageAndOrHearingServiceSpecialistOrTechnologistHipaa(Enum):
    """
    abstDomain: A13640 (C-0-T13129-A13130-A13634-A13640-cpt)
    :cvar VALUE_2355_A2700_N:
    :cvar VALUE_2355_S0801_N:
    """
    VALUE_2355_A2700_N = "2355A2700N"
    VALUE_2355_S0801_N = "2355S0801N"


class SpeechLanguageTechnologistProviderCodes(Enum):
    """
    specDomain: S20604 (C-0-T19465-S20598-S20604-cpt)
    :cvar VALUE_235500000_X:
    :cvar VALUE_2355_A2700_X:
    :cvar VALUE_2355_S0801_X:
    """
    VALUE_235500000_X = "235500000X"
    VALUE_2355_A2700_X = "2355A2700X"
    VALUE_2355_S0801_X = "2355S0801X"


class SpeechLanguageandHearingProvidersProviderCodes(Enum):
    """
    specDomain: S20598 (C-0-T19465-S20598-cpt)
    :cvar VALUE_231_H00000_X:
    :cvar VALUE_231_HA2400_X:
    :cvar VALUE_231_HA2500_X:
    :cvar VALUE_235500000_X:
    :cvar VALUE_2355_A2700_X:
    :cvar VALUE_2355_S0801_X:
    :cvar VALUE_230000000_X:
    :cvar VALUE_237600000_X:
    :cvar VALUE_237700000_X:
    :cvar VALUE_235_Z00000_X:
    """
    VALUE_231_H00000_X = "231H00000X"
    VALUE_231_HA2400_X = "231HA2400X"
    VALUE_231_HA2500_X = "231HA2500X"
    VALUE_235500000_X = "235500000X"
    VALUE_2355_A2700_X = "2355A2700X"
    VALUE_2355_S0801_X = "2355S0801X"
    VALUE_230000000_X = "230000000X"
    VALUE_237600000_X = "237600000X"
    VALUE_237700000_X = "237700000X"
    VALUE_235_Z00000_X = "235Z00000X"


class SponsorParticipationFunction(Enum):
    """
    abstDomain: A19905 (C-0-T10267-A19903-A19905-cpt)
    :cvar FULINRD:
    :cvar SELFINRD:
    """
    FULINRD = "FULINRD"
    SELFINRD = "SELFINRD"


class Spouse(Enum):
    """
    specDomain: S19742 (C-0-T12206-A19563-S17926-S19755-S19742-cpt)
    :cvar SPS:
    :cvar HUSB:
    :cvar WIFE:
    """
    SPS = "SPS"
    HUSB = "HUSB"
    WIFE = "WIFE"


class StepChild(Enum):
    """
    specDomain: S11562 (C-0-T12206-A19563-S17926-S16360-S11562-cpt)
    :cvar STPCHLD:
    :cvar STPDAU:
    :cvar STPSON:
    """
    STPCHLD = "STPCHLD"
    STPDAU = "STPDAU"
    STPSON = "STPSON"


class StepParent(Enum):
    """
    specDomain: S19767 (C-0-T12206-A19563-S17926-S16346-S19767-cpt)
    :cvar STPPRN:
    :cvar STPFTH:
    :cvar STPMTH:
    """
    STPPRN = "STPPRN"
    STPFTH = "STPFTH"
    STPMTH = "STPMTH"


class StepSibling(Enum):
    """
    specDomain: S19779 (C-0-T12206-A19563-S17926-S11567-S19779-cpt)
    :cvar STPSIB:
    :cvar STPBRO:
    :cvar STPSIS:
    """
    STPSIB = "STPSIB"
    STPBRO = "STPBRO"
    STPSIS = "STPSIS"


class StreetAddressLine(Enum):
    """
    specDomain: S14822 (C-0-T10642-S14822-cpt)
    :cvar BNS:
    :cvar POB:
    :cvar BNR:
    :cvar BNN:
    :cvar STR_VALUE:
    :cvar STB:
    :cvar STTYP:
    :cvar SAL:
    :cvar DIR:
    """
    BNS = "BNS"
    POB = "POB"
    BNR = "BNR"
    BNN = "BNN"
    STR_VALUE = "STR"
    STB = "STB"
    STTYP = "STTYP"
    SAL = "SAL"
    DIR = "DIR"


class StreetName(Enum):
    """
    specDomain: S10648 (C-0-T10642-S14822-S10648-cpt)
    :cvar STR_VALUE:
    :cvar STB:
    :cvar STTYP:
    """
    STR_VALUE = "STR"
    STB = "STB"
    STTYP = "STTYP"


class StudentRoleType(Enum):
    """
    specDomain: S21318 (C-0-T12206-A19809-A19805-A19813-S21318-cpt)
    :cvar STUD:
    :cvar FSTUD:
    :cvar PSTUD:
    """
    STUD = "STUD"
    FSTUD = "FSTUD"
    PSTUD = "PSTUD"


class SubarachnoidRoute(Enum):
    """
    abstDomain: A17334 (C-0-T14581-A17021-A17334-cpt)
    :cvar SUBARACHINJ:
    """
    SUBARACHINJ = "SUBARACHINJ"


class SubconjunctivalRoute(Enum):
    """
    abstDomain: A17336 (C-0-T14581-A17021-A17336-cpt)
    :cvar SCINJ:
    :cvar SUBCONJTA:
    """
    SCINJ = "SCINJ"
    SUBCONJTA = "SUBCONJTA"


class SubcutaneousRoute(Enum):
    """
    abstDomain: A17339 (C-0-T14581-A17021-A17339-cpt)
    :cvar SQIMPLNT:
    :cvar SQINFUS:
    :cvar IPUMPINJ:
    :cvar SQ:
    :cvar SQSURGINS:
    """
    SQIMPLNT = "SQIMPLNT"
    SQINFUS = "SQINFUS"
    IPUMPINJ = "IPUMPINJ"
    SQ = "SQ"
    SQSURGINS = "SQSURGINS"


class SublesionalRoute(Enum):
    """
    abstDomain: A17345 (C-0-T14581-A17021-A17345-cpt)
    :cvar SLESINJ:
    """
    SLESINJ = "SLESINJ"


class SublingualRoute(Enum):
    """
    abstDomain: A17347 (C-0-T14581-A17021-A17347-cpt)
    :cvar SL:
    """
    SL = "SL"


class SubmucosalRoute(Enum):
    """
    abstDomain: A17349 (C-0-T14581-A17021-A17349-cpt)
    :cvar SUBMUCINJ:
    :cvar SMUCMAB:
    """
    SUBMUCINJ = "SUBMUCINJ"
    SMUCMAB = "SMUCMAB"


class SubscriberCoveredPartyRoleType(Enum):
    """
    abstDomain: A19814 (C-0-T12206-A19809-A19805-A19814-cpt)
    :cvar MIL:
    :cvar ACTMIL:
    :cvar RETMIL:
    :cvar VET:
    :cvar COCBEN:
    :cvar RETIREE:
    """
    MIL = "MIL"
    ACTMIL = "ACTMIL"
    RETMIL = "RETMIL"
    VET = "VET"
    COCBEN = "COCBEN"
    RETIREE = "RETIREE"


class SubsidizedHealthProgram(Enum):
    """
    specDomain: S22137 (C-0-T13953-A13954-A19855-A19858-S19718-S22137-cpt)
    :cvar SUBSIDIZ:
    :cvar SUBSIDMC:
    :cvar SUBSUPP:
    """
    SUBSIDIZ = "SUBSIDIZ"
    SUBSIDMC = "SUBSIDMC"
    SUBSUPP = "SUBSUPP"


class SubstanceAbuseDisorderRehabilitationFacilityProviderCodes(Enum):
    """
    specDomain: S20769 (C-0-T19465-S20766-S20769-cpt)
    :cvar VALUE_324500000_X:
    :cvar VALUE_3245_S0500_X:
    """
    VALUE_324500000_X = "324500000X"
    VALUE_3245_S0500_X = "3245S0500X"


class SubstanceAdminGenericSubstitution(Enum):
    """
    specDomain: S16623 (C-0-T13953-A13954-A16621-S16623-cpt)
    :cvar G:
    :cvar TE:
    """
    G = "G"
    TE = "TE"


class SubstanceAdminSubstitutionNotAllowedReason(Enum):
    """
    abstDomain: A19719 (C-0-T14878-A19719-cpt)
    :cvar PAT:
    :cvar ALGINT:
    :cvar TRIAL:
    :cvar COMPCON:
    :cvar THERCHAR:
    """
    PAT = "PAT"
    ALGINT = "ALGINT"
    TRIAL = "TRIAL"
    COMPCON = "COMPCON"
    THERCHAR = "THERCHAR"


class SubstanceAdminSubstitutionReason(Enum):
    """
    abstDomain: A19377 (C-0-T14878-A19377-cpt)
    :cvar CT:
    :cvar FP:
    :cvar OS:
    :cvar RR:
    """
    CT = "CT"
    FP = "FP"
    OS = "OS"
    RR = "RR"


class SubstitutionCondition(Enum):
    """
    vocSet: T17719 (C-0-T17719-cpt)
    :cvar CONFIRM:
    :cvar NOTIFY:
    :cvar NOSUB:
    :cvar UNCOND:
    """
    CONFIRM = "CONFIRM"
    NOTIFY = "NOTIFY"
    NOSUB = "NOSUB"
    UNCOND = "UNCOND"


class SupernumeraryTooth(Enum):
    """
    abstDomain: A19343 (C-0-T16537-A16538-A19346-A19343-cpt)
    :cvar TID10S:
    :cvar TID11S:
    :cvar TID12S:
    :cvar TID13S:
    :cvar TID14S:
    :cvar TID15S:
    :cvar TID16S:
    :cvar TID17S:
    :cvar TID18S:
    :cvar TID19S:
    :cvar TID1S:
    :cvar TID20S:
    :cvar TID21S:
    :cvar TID22S:
    :cvar TID23S:
    :cvar TID24S:
    :cvar TID25S:
    :cvar TID26S:
    :cvar TID27S:
    :cvar TID28S:
    :cvar TID29S:
    :cvar TID2S:
    :cvar TID30S:
    :cvar TID31S:
    :cvar TID32S:
    :cvar TID3S:
    :cvar TID4S:
    :cvar TID5S:
    :cvar TID6S:
    :cvar TID7S:
    :cvar TID8S:
    :cvar TID9S:
    :cvar TIDAS:
    :cvar TIDBS:
    :cvar TIDCS:
    :cvar TIDDS:
    :cvar TIDES:
    :cvar TIDFS:
    :cvar TIDGS:
    :cvar TIDHS:
    :cvar TIDIS:
    :cvar TIDJS:
    :cvar TIDKS:
    :cvar TIDLS:
    :cvar TIDMS:
    :cvar TIDNS:
    :cvar TIDOS:
    :cvar TIDPS:
    :cvar TIDQS:
    :cvar TIDRS:
    :cvar TIDSS:
    :cvar TIDTS:
    """
    TID10S = "TID10s"
    TID11S = "TID11s"
    TID12S = "TID12s"
    TID13S = "TID13s"
    TID14S = "TID14s"
    TID15S = "TID15s"
    TID16S = "TID16s"
    TID17S = "TID17s"
    TID18S = "TID18s"
    TID19S = "TID19s"
    TID1S = "TID1s"
    TID20S = "TID20s"
    TID21S = "TID21s"
    TID22S = "TID22s"
    TID23S = "TID23s"
    TID24S = "TID24s"
    TID25S = "TID25s"
    TID26S = "TID26s"
    TID27S = "TID27s"
    TID28S = "TID28s"
    TID29S = "TID29s"
    TID2S = "TID2s"
    TID30S = "TID30s"
    TID31S = "TID31s"
    TID32S = "TID32s"
    TID3S = "TID3s"
    TID4S = "TID4s"
    TID5S = "TID5s"
    TID6S = "TID6s"
    TID7S = "TID7s"
    TID8S = "TID8s"
    TID9S = "TID9s"
    TIDAS = "TIDAs"
    TIDBS = "TIDBs"
    TIDCS = "TIDCs"
    TIDDS = "TIDDs"
    TIDES = "TIDEs"
    TIDFS = "TIDFs"
    TIDGS = "TIDGs"
    TIDHS = "TIDHs"
    TIDIS = "TIDIs"
    TIDJS = "TIDJs"
    TIDKS = "TIDKs"
    TIDLS = "TIDLs"
    TIDMS = "TIDMs"
    TIDNS = "TIDNs"
    TIDOS = "TIDOs"
    TIDPS = "TIDPs"
    TIDQS = "TIDQs"
    TIDRS = "TIDRs"
    TIDSS = "TIDSs"
    TIDTS = "TIDTs"


class SupplierHipaa(Enum):
    """
    abstDomain: A13833 (C-0-T13129-A13715-A13833-cpt)
    :cvar VALUE_332_B00000_N:
    :cvar VALUE_332_BC3200_N:
    :cvar VALUE_332_BD1200_N:
    :cvar VALUE_332_BN1400_N:
    :cvar VALUE_332_BX2000_N:
    :cvar VALUE_332_BP3500_N:
    :cvar VALUE_331_L00000_N:
    :cvar VALUE_332_G00000_N:
    :cvar VALUE_332_H00000_N:
    :cvar VALUE_332_S00000_N:
    :cvar VALUE_332_U00000_N:
    :cvar VALUE_335_U00000_N:
    :cvar VALUE_333600000_N:
    :cvar VALUE_335_V00000_N:
    :cvar VALUE_335_E00000_N:
    """
    VALUE_332_B00000_N = "332B00000N"
    VALUE_332_BC3200_N = "332BC3200N"
    VALUE_332_BD1200_N = "332BD1200N"
    VALUE_332_BN1400_N = "332BN1400N"
    VALUE_332_BX2000_N = "332BX2000N"
    VALUE_332_BP3500_N = "332BP3500N"
    VALUE_331_L00000_N = "331L00000N"
    VALUE_332_G00000_N = "332G00000N"
    VALUE_332_H00000_N = "332H00000N"
    VALUE_332_S00000_N = "332S00000N"
    VALUE_332_U00000_N = "332U00000N"
    VALUE_335_U00000_N = "335U00000N"
    VALUE_333600000_N = "333600000N"
    VALUE_335_V00000_N = "335V00000N"
    VALUE_335_E00000_N = "335E00000N"


class SuppliersProviderCodes(Enum):
    """
    specDomain: S20772 (C-0-T19465-S20772-cpt)
    :cvar VALUE_332_B00000_X:
    :cvar VALUE_332_BC3200_X:
    :cvar VALUE_332_BD1200_X:
    :cvar VALUE_332_BN1400_X:
    :cvar VALUE_332_BX2000_X:
    :cvar VALUE_332_BP3500_X:
    :cvar VALUE_330000000_X:
    :cvar VALUE_331_L00000_X:
    :cvar VALUE_332_G00000_X:
    :cvar VALUE_332_H00000_X:
    :cvar VALUE_332_S00000_X:
    :cvar VALUE_332_U00000_X:
    :cvar VALUE_335_U00000_X:
    :cvar VALUE_333600000_X:
    :cvar VALUE_335_V00000_X:
    :cvar VALUE_335_E00000_X:
    """
    VALUE_332_B00000_X = "332B00000X"
    VALUE_332_BC3200_X = "332BC3200X"
    VALUE_332_BD1200_X = "332BD1200X"
    VALUE_332_BN1400_X = "332BN1400X"
    VALUE_332_BX2000_X = "332BX2000X"
    VALUE_332_BP3500_X = "332BP3500X"
    VALUE_330000000_X = "330000000X"
    VALUE_331_L00000_X = "331L00000X"
    VALUE_332_G00000_X = "332G00000X"
    VALUE_332_H00000_X = "332H00000X"
    VALUE_332_S00000_X = "332S00000X"
    VALUE_332_U00000_X = "332U00000X"
    VALUE_335_U00000_X = "335U00000X"
    VALUE_333600000_X = "333600000X"
    VALUE_335_V00000_X = "335V00000X"
    VALUE_335_E00000_X = "335E00000X"


class SupplyAppropriateManagementCode(Enum):
    """
    specDomain: S16709 (C-0-T13953-A13954-A16695-S16709-cpt)
    :cvar VALUE_14:
    :cvar VALUE_18:
    :cvar VALUE_15:
    :cvar VALUE_16:
    :cvar VALUE_17:
    """
    VALUE_14 = "14"
    VALUE_18 = "18"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"


class SupplyDetectedIssueCode(Enum):
    """
    abstDomain: A16691 (C-0-T14878-A19692-A19781-A16124-A16656-A16691-cpt)
    :cvar TOOLATE:
    :cvar TOOSOON:
    """
    TOOLATE = "TOOLATE"
    TOOSOON = "TOOSOON"


class SupplyOrderAbortReasonCode(Enum):
    """
    abstDomain: A19787 (C-0-T14878-A19692-A19787-cpt)
    :cvar IMPROV:
    :cvar INTOL:
    :cvar NEWSTR:
    :cvar NEWTHER:
    """
    IMPROV = "IMPROV"
    INTOL = "INTOL"
    NEWSTR = "NEWSTR"
    NEWTHER = "NEWTHER"


class SuppositoryDrugForm(Enum):
    """
    specDomain: S14538 (C-0-T19651-A14411-A14412-A14484-S14538-cpt)
    :cvar SUPP:
    :cvar RECSUPP:
    :cvar URETHSUPP:
    :cvar VAGSUPP:
    """
    SUPP = "SUPP"
    RECSUPP = "RECSUPP"
    URETHSUPP = "URETHSUPP"
    VAGSUPP = "VAGSUPP"


class SuppositoryRoute(Enum):
    """
    abstDomain: A17003 (C-0-T14581-A16931-A17003-cpt)
    :cvar URETHSUP:
    """
    URETHSUP = "URETHSUP"


class SurgClinPracticeSetting(Enum):
    """
    specDomain: S10968 (C-0-T12206-A17660-A19450-A10588-S10589-S10968-cpt)
    :cvar SU:
    :cvar PLS:
    :cvar URO:
    """
    SU = "SU"
    PLS = "PLS"
    URO = "URO"


class SurgeryProviderCodes(Enum):
    """
    specDomain: S20264 (C-0-T19465-S20096-S20264-cpt)
    :cvar VALUE_208600000_X:
    :cvar VALUE_2086_S0120_X:
    :cvar VALUE_2086_S0122_X:
    :cvar VALUE_2086_S0105_X:
    :cvar VALUE_2086_S0102_X:
    :cvar VALUE_2086_X0206_X:
    :cvar VALUE_208_G00000_X:
    :cvar VALUE_204_F00000_X:
    :cvar VALUE_2086_S0127_X:
    :cvar VALUE_2086_S0129_X:
    """
    VALUE_208600000_X = "208600000X"
    VALUE_2086_S0120_X = "2086S0120X"
    VALUE_2086_S0122_X = "2086S0122X"
    VALUE_2086_S0105_X = "2086S0105X"
    VALUE_2086_S0102_X = "2086S0102X"
    VALUE_2086_X0206_X = "2086X0206X"
    VALUE_208_G00000_X = "208G00000X"
    VALUE_204_F00000_X = "204F00000X"
    VALUE_2086_S0127_X = "2086S0127X"
    VALUE_2086_S0129_X = "2086S0129X"


class SuspensionDrugForm(Enum):
    """
    specDomain: S14454 (C-0-T19651-A14411-A14412-A14441-S14454-cpt)
    :cvar ERSUSP:
    :cvar ERSUSP12:
    :cvar ERSUSP24:
    :cvar ORSUSP:
    :cvar SUSP:
    :cvar ITSUSP:
    :cvar OPSUSP:
    :cvar OTSUSP:
    :cvar RECSUSP:
    """
    ERSUSP = "ERSUSP"
    ERSUSP12 = "ERSUSP12"
    ERSUSP24 = "ERSUSP24"
    ORSUSP = "ORSUSP"
    SUSP = "SUSP"
    ITSUSP = "ITSUSP"
    OPSUSP = "OPSUSP"
    OTSUSP = "OTSUSP"
    RECSUSP = "RECSUSP"


class SwabDrugForm(Enum):
    """
    specDomain: S14542 (C-0-T19651-A14411-A14412-A14484-S14542-cpt)
    :cvar SWAB:
    :cvar MEDSWAB:
    """
    SWAB = "SWAB"
    MEDSWAB = "MEDSWAB"


class Swish(Enum):
    """
    abstDomain: A14736 (C-0-T14581-A16931-A14736-cpt)
    :cvar SWISHSPIT:
    :cvar SWISHSWAL:
    """
    SWISHSPIT = "SWISHSPIT"
    SWISHSWAL = "SWISHSWAL"


class TableCellHorizontalAlign(Enum):
    """
    vocSet: T10981 (C-0-T10981-cpt)
    :cvar CENTER:
    :cvar CHAR:
    :cvar JUSTIFY:
    :cvar LEFT:
    :cvar RIGHT:
    """
    CENTER = "center"
    CHAR = "char"
    JUSTIFY = "justify"
    LEFT = "left"
    RIGHT = "right"


class TableCellScope(Enum):
    """
    vocSet: T11012 (C-0-T11012-cpt)
    :cvar COL:
    :cvar COLGROUP:
    :cvar ROW:
    :cvar ROWGROUP:
    """
    COL = "col"
    COLGROUP = "colgroup"
    ROW = "row"
    ROWGROUP = "rowgroup"


class TableCellVerticalAlign(Enum):
    """
    vocSet: T10987 (C-0-T10987-cpt)
    :cvar BASELINE:
    :cvar BOTTOM:
    :cvar MIDDLE:
    :cvar TOP:
    """
    BASELINE = "baseline"
    BOTTOM = "bottom"
    MIDDLE = "middle"
    TOP = "top"


class TableFrame(Enum):
    """
    vocSet: T10992 (C-0-T10992-cpt)
    :cvar ABOVE:
    :cvar BELOW:
    :cvar BORDER:
    :cvar BOX:
    :cvar HSIDES:
    :cvar LHS:
    :cvar RHS:
    :cvar VOID:
    :cvar VSIDES:
    """
    ABOVE = "above"
    BELOW = "below"
    BORDER = "border"
    BOX = "box"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VOID = "void"
    VSIDES = "vsides"


class TableRuleStyle(Enum):
    """
    abstDomain: A19604 (C-0-T19602-A19604-cpt)
    :cvar BOTRULE:
    :cvar LRULE:
    :cvar RRULE:
    :cvar TOPRULE:
    """
    BOTRULE = "Botrule"
    LRULE = "Lrule"
    RRULE = "Rrule"
    TOPRULE = "Toprule"


class TableRules(Enum):
    """
    vocSet: T11002 (C-0-T11002-cpt)
    :cvar ALL:
    :cvar COLS:
    :cvar GROUPS:
    :cvar NONE_VALUE:
    :cvar ROWS:
    """
    ALL = "all"
    COLS = "cols"
    GROUPS = "groups"
    NONE_VALUE = "none"
    ROWS = "rows"


class TabletDrugForm(Enum):
    """
    specDomain: S14515 (C-0-T19651-A14411-A14412-A14484-S14506-S14515-cpt)
    :cvar BUCTAB:
    :cvar SRBUCTAB:
    :cvar ECTAB:
    :cvar ERECTAB:
    :cvar ERTAB:
    :cvar ERTAB12:
    :cvar ERTAB24:
    :cvar ORTAB:
    :cvar CAPLET:
    :cvar CHEWTAB:
    :cvar CPTAB:
    :cvar DRTAB:
    :cvar DISINTAB:
    :cvar ORTROCHE:
    :cvar SLTAB:
    :cvar TAB:
    :cvar VAGTAB:
    """
    BUCTAB = "BUCTAB"
    SRBUCTAB = "SRBUCTAB"
    ECTAB = "ECTAB"
    ERECTAB = "ERECTAB"
    ERTAB = "ERTAB"
    ERTAB12 = "ERTAB12"
    ERTAB24 = "ERTAB24"
    ORTAB = "ORTAB"
    CAPLET = "CAPLET"
    CHEWTAB = "CHEWTAB"
    CPTAB = "CPTAB"
    DRTAB = "DRTAB"
    DISINTAB = "DISINTAB"
    ORTROCHE = "ORTROCHE"
    SLTAB = "SLTAB"
    TAB = "TAB"
    VAGTAB = "VAGTAB"


class Tanana(Enum):
    """
    abstDomain: A18374 (C-0-T18130-A18352-A18356-A18358-A18365-A18371-A18374-cpt)
    :cvar X_TAA:
    :cvar X_TCB:
    :cvar X_TAU:
    """
    X_TAA = "x-TAA"
    X_TCB = "x-TCB"
    X_TAU = "x-TAU"


class TananaTutchone(Enum):
    """
    abstDomain: A18371 (C-0-T18130-A18352-A18356-A18358-A18365-A18371-cpt)
    :cvar X_TAA:
    :cvar X_TCB:
    :cvar X_TAU:
    :cvar X_KUU:
    """
    X_TAA = "x-TAA"
    X_TCB = "x-TCB"
    X_TAU = "x-TAU"
    X_KUU = "x-KUU"


class TargetAwareness(Enum):
    """
    vocSet: T10310 (C-0-T10310-cpt)
    :cvar D:
    :cvar F:
    :cvar I:
    :cvar M:
    :cvar P:
    :cvar U:
    """
    D = "D"
    F = "F"
    I = "I"
    M = "M"
    P = "P"
    U = "U"


class TechnicianHealthInformationProviderCodes(Enum):
    """
    specDomain: S20657 (C-0-T19465-S20608-S20657-cpt)
    :cvar VALUE_247000000_X:
    :cvar VALUE_2470_A2800_X:
    """
    VALUE_247000000_X = "247000000X"
    VALUE_2470_A2800_X = "2470A2800X"


class TechnicianOtherProviderCodes(Enum):
    """
    specDomain: S20659 (C-0-T19465-S20608-S20659-cpt)
    :cvar VALUE_247200000_X:
    :cvar VALUE_2472_B0301_X:
    :cvar VALUE_2472_D0500_X:
    :cvar VALUE_2472_E0500_X:
    :cvar VALUE_2472_R0900_X:
    :cvar VALUE_2472_V0600_X:
    """
    VALUE_247200000_X = "247200000X"
    VALUE_2472_B0301_X = "2472B0301X"
    VALUE_2472_D0500_X = "2472D0500X"
    VALUE_2472_E0500_X = "2472E0500X"
    VALUE_2472_R0900_X = "2472R0900X"
    VALUE_2472_V0600_X = "2472V0600X"


class TechnicianPathologyProviderCodes(Enum):
    """
    specDomain: S20665 (C-0-T19465-S20608-S20665-cpt)
    :cvar VALUE_246_R00000_X:
    :cvar VALUE_246_RH0600_X:
    :cvar VALUE_246_RM2200_X:
    :cvar VALUE_246_RP1900_X:
    """
    VALUE_246_R00000_X = "246R00000X"
    VALUE_246_RH0600_X = "246RH0600X"
    VALUE_246_RM2200_X = "246RM2200X"
    VALUE_246_RP1900_X = "246RP1900X"


class TechnicianProviderCodes(Enum):
    """
    specDomain: S20432 (C-0-T19465-S20425-S20432-cpt)
    :cvar VALUE_374700000_X:
    :cvar VALUE_3747_A0650_X:
    :cvar VALUE_3747_P1801_X:
    """
    VALUE_374700000_X = "374700000X"
    VALUE_3747_A0650_X = "3747A0650X"
    VALUE_3747_P1801_X = "3747P1801X"


class TechnicianTechnologistProviderCodes(Enum):
    """
    specDomain: S20356 (C-0-T19465-S20348-S20356-cpt)
    :cvar VALUE_156_F00000_X:
    :cvar VALUE_156_FC0800_X:
    :cvar VALUE_156_FC0801_X:
    :cvar VALUE_156_FX1700_X:
    :cvar VALUE_156_FX1100_X:
    :cvar VALUE_156_FX1101_X:
    :cvar VALUE_156_FX1800_X:
    :cvar VALUE_156_FX1201_X:
    :cvar VALUE_156_FX1202_X:
    :cvar VALUE_156_FX1900_X:
    """
    VALUE_156_F00000_X = "156F00000X"
    VALUE_156_FC0800_X = "156FC0800X"
    VALUE_156_FC0801_X = "156FC0801X"
    VALUE_156_FX1700_X = "156FX1700X"
    VALUE_156_FX1100_X = "156FX1100X"
    VALUE_156_FX1101_X = "156FX1101X"
    VALUE_156_FX1800_X = "156FX1800X"
    VALUE_156_FX1201_X = "156FX1201X"
    VALUE_156_FX1202_X = "156FX1202X"
    VALUE_156_FX1900_X = "156FX1900X"


class TechnologistTechnicianandOtherTechnicalServiceProvidersProviderCodes(Enum):
    """
    specDomain: S20608 (C-0-T19465-S20608-cpt)
    :cvar VALUE_247100000_X:
    :cvar VALUE_2471_B0102_X:
    :cvar VALUE_2471_C1106_X:
    :cvar VALUE_2471_C1101_X:
    :cvar VALUE_2471_C3401_X:
    :cvar VALUE_2471_M1202_X:
    :cvar VALUE_2471_M2300_X:
    :cvar VALUE_2471_N0900_X:
    :cvar VALUE_2471_Q0001_X:
    :cvar VALUE_2471_R0002_X:
    :cvar VALUE_2471_C3402_X:
    :cvar VALUE_2471_S1302_X:
    :cvar VALUE_2471_V0105_X:
    :cvar VALUE_2471_V0106_X:
    :cvar VALUE_246_X00000_X:
    :cvar VALUE_246_XC2901_X:
    :cvar VALUE_246_XS1301_X:
    :cvar VALUE_246_XC2903_X:
    :cvar VALUE_246_Y00000_X:
    :cvar VALUE_246_YC3301_X:
    :cvar VALUE_246_YC3302_X:
    :cvar VALUE_246_YR1600_X:
    :cvar VALUE_246_Z00000_X:
    :cvar VALUE_246_ZA2600_X:
    :cvar VALUE_246_ZB0500_X:
    :cvar VALUE_246_ZB0301_X:
    :cvar VALUE_246_ZB0302_X:
    :cvar VALUE_246_ZB0600_X:
    :cvar VALUE_246_ZE0500_X:
    :cvar VALUE_246_ZE0600_X:
    :cvar VALUE_246_ZG1000_X:
    :cvar VALUE_246_ZG0701_X:
    :cvar VALUE_246_ZI1000_X:
    :cvar VALUE_246_ZN0300_X:
    :cvar VALUE_246_ZS0400_X:
    :cvar VALUE_246_Q00000_X:
    :cvar VALUE_246_QB0000_X:
    :cvar VALUE_246_QC1000_X:
    :cvar VALUE_246_QC2700_X:
    :cvar VALUE_246_QH0401_X:
    :cvar VALUE_246_QH0000_X:
    :cvar VALUE_246_QH0600_X:
    :cvar VALUE_246_QI0000_X:
    :cvar VALUE_246_QL0900_X:
    :cvar VALUE_246_QL0901_X:
    :cvar VALUE_246_QM0706_X:
    :cvar VALUE_246_QM0900_X:
    :cvar VALUE_247000000_X:
    :cvar VALUE_2470_A2800_X:
    :cvar VALUE_247200000_X:
    :cvar VALUE_2472_B0301_X:
    :cvar VALUE_2472_D0500_X:
    :cvar VALUE_2472_E0500_X:
    :cvar VALUE_2472_R0900_X:
    :cvar VALUE_2472_V0600_X:
    :cvar VALUE_246_R00000_X:
    :cvar VALUE_246_RH0600_X:
    :cvar VALUE_246_RM2200_X:
    :cvar VALUE_246_RP1900_X:
    :cvar VALUE_240000000_X:
    :cvar VALUE_246_W00000_X:
    """
    VALUE_247100000_X = "247100000X"
    VALUE_2471_B0102_X = "2471B0102X"
    VALUE_2471_C1106_X = "2471C1106X"
    VALUE_2471_C1101_X = "2471C1101X"
    VALUE_2471_C3401_X = "2471C3401X"
    VALUE_2471_M1202_X = "2471M1202X"
    VALUE_2471_M2300_X = "2471M2300X"
    VALUE_2471_N0900_X = "2471N0900X"
    VALUE_2471_Q0001_X = "2471Q0001X"
    VALUE_2471_R0002_X = "2471R0002X"
    VALUE_2471_C3402_X = "2471C3402X"
    VALUE_2471_S1302_X = "2471S1302X"
    VALUE_2471_V0105_X = "2471V0105X"
    VALUE_2471_V0106_X = "2471V0106X"
    VALUE_246_X00000_X = "246X00000X"
    VALUE_246_XC2901_X = "246XC2901X"
    VALUE_246_XS1301_X = "246XS1301X"
    VALUE_246_XC2903_X = "246XC2903X"
    VALUE_246_Y00000_X = "246Y00000X"
    VALUE_246_YC3301_X = "246YC3301X"
    VALUE_246_YC3302_X = "246YC3302X"
    VALUE_246_YR1600_X = "246YR1600X"
    VALUE_246_Z00000_X = "246Z00000X"
    VALUE_246_ZA2600_X = "246ZA2600X"
    VALUE_246_ZB0500_X = "246ZB0500X"
    VALUE_246_ZB0301_X = "246ZB0301X"
    VALUE_246_ZB0302_X = "246ZB0302X"
    VALUE_246_ZB0600_X = "246ZB0600X"
    VALUE_246_ZE0500_X = "246ZE0500X"
    VALUE_246_ZE0600_X = "246ZE0600X"
    VALUE_246_ZG1000_X = "246ZG1000X"
    VALUE_246_ZG0701_X = "246ZG0701X"
    VALUE_246_ZI1000_X = "246ZI1000X"
    VALUE_246_ZN0300_X = "246ZN0300X"
    VALUE_246_ZS0400_X = "246ZS0400X"
    VALUE_246_Q00000_X = "246Q00000X"
    VALUE_246_QB0000_X = "246QB0000X"
    VALUE_246_QC1000_X = "246QC1000X"
    VALUE_246_QC2700_X = "246QC2700X"
    VALUE_246_QH0401_X = "246QH0401X"
    VALUE_246_QH0000_X = "246QH0000X"
    VALUE_246_QH0600_X = "246QH0600X"
    VALUE_246_QI0000_X = "246QI0000X"
    VALUE_246_QL0900_X = "246QL0900X"
    VALUE_246_QL0901_X = "246QL0901X"
    VALUE_246_QM0706_X = "246QM0706X"
    VALUE_246_QM0900_X = "246QM0900X"
    VALUE_247000000_X = "247000000X"
    VALUE_2470_A2800_X = "2470A2800X"
    VALUE_247200000_X = "247200000X"
    VALUE_2472_B0301_X = "2472B0301X"
    VALUE_2472_D0500_X = "2472D0500X"
    VALUE_2472_E0500_X = "2472E0500X"
    VALUE_2472_R0900_X = "2472R0900X"
    VALUE_2472_V0600_X = "2472V0600X"
    VALUE_246_R00000_X = "246R00000X"
    VALUE_246_RH0600_X = "246RH0600X"
    VALUE_246_RM2200_X = "246RM2200X"
    VALUE_246_RP1900_X = "246RP1900X"
    VALUE_240000000_X = "240000000X"
    VALUE_246_W00000_X = "246W00000X"


class TelecommunicationAddressUse(Enum):
    """
    vocSet: T201 (C-0-T201-cpt)
    :cvar H:
    :cvar HP:
    :cvar HV:
    :cvar WP:
    :cvar DIR:
    :cvar PUB:
    :cvar BAD:
    :cvar TMP:
    :cvar AS_VALUE:
    :cvar EC:
    :cvar MC:
    :cvar PG:
    """
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    AS_VALUE = "AS"
    EC = "EC"
    MC = "MC"
    PG = "PG"


class Tepiman(Enum):
    """
    abstDomain: A18629 (C-0-T18130-A18605-A18629-cpt)
    :cvar X_PAP:
    """
    X_PAP = "x-PAP"


class TextMediaType(Enum):
    """
    abstDomain: A14825 (C-0-T14824-A14825-cpt)
    :cvar TEXT_X_HL7_FT:
    :cvar TEXT_HTML:
    :cvar TEXT_PLAIN:
    :cvar TEXT_RTF:
    :cvar TEXT_SGML:
    :cvar TEXT_XML:
    """
    TEXT_X_HL7_FT = "text/x-hl7-ft"
    TEXT_HTML = "text/html"
    TEXT_PLAIN = "text/plain"
    TEXT_RTF = "text/rtf"
    TEXT_SGML = "text/sgml"
    TEXT_XML = "text/xml"


class TherapeuticProductDetectedIssueCode(Enum):
    """
    specDomain: S17807 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-A16659-S17807-cpt)
    :cvar TPROD:
    :cvar DRG:
    :cvar NHP:
    :cvar NONRX:
    """
    TPROD = "TPROD"
    DRG = "DRG"
    NHP = "NHP"
    NONRX = "NONRX"


class TherapyAppropriateManagementCode(Enum):
    """
    specDomain: S16696 (C-0-T13953-A13954-A16695-S16696-cpt)
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_4:
    :cvar VALUE_19:
    :cvar VALUE_7:
    :cvar VALUE_3:
    """
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_4 = "4"
    VALUE_19 = "19"
    VALUE_7 = "7"
    VALUE_3 = "3"


class TimingDetectedIssueCode(Enum):
    """
    specDomain: S21700 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-S21700-cpt)
    :cvar TIME:
    :cvar ENDLATE:
    :cvar STRTLATE:
    """
    TIME = "TIME"
    ENDLATE = "ENDLATE"
    STRTLATE = "STRTLATE"


class TimingEvent(Enum):
    """
    vocSet: T10706 (C-0-T10706-cpt)
    :cvar AC:
    :cvar ACD:
    :cvar ACM:
    :cvar ACV:
    :cvar HS:
    :cvar IC:
    :cvar ICD:
    :cvar ICM:
    :cvar ICV:
    :cvar PC:
    :cvar PCD:
    :cvar PCM:
    :cvar PCV:
    """
    AC = "AC"
    ACD = "ACD"
    ACM = "ACM"
    ACV = "ACV"
    HS = "HS"
    IC = "IC"
    ICD = "ICD"
    ICM = "ICM"
    ICV = "ICV"
    PC = "PC"
    PCD = "PCD"
    PCM = "PCM"
    PCV = "PCV"


class Tiwa(Enum):
    """
    abstDomain: A18331 (C-0-T18130-A18327-A18331-cpt)
    :cvar X_TAO:
    :cvar X_TIX:
    """
    X_TAO = "x-TAO"
    X_TIX = "x-TIX"


class TopicalAbsorptionRoute(Enum):
    """
    abstDomain: A17006 (C-0-T14581-A16931-A17006-cpt)
    :cvar TTYMPTABSORP:
    """
    TTYMPTABSORP = "TTYMPTABSORP"


class TopicalApplication(Enum):
    """
    abstDomain: A14739 (C-0-T14581-A16931-A14739-cpt)
    :cvar OCDRESTA:
    :cvar SUBCONJTA:
    :cvar TOPICAL:
    :cvar BUC:
    :cvar CERV:
    :cvar DEN:
    :cvar GIN:
    :cvar HAIR:
    :cvar ICORNTA:
    :cvar ICORONTA:
    :cvar IESOPHTA:
    :cvar IILEALTA:
    :cvar ILTOP:
    :cvar ILUMTA:
    :cvar IOTOP:
    :cvar IONTO:
    :cvar LARYNGTA:
    :cvar MUC:
    :cvar NAIL:
    :cvar NASAL:
    :cvar OPTHALTA:
    :cvar ORALTA:
    :cvar ORMUC:
    :cvar OROPHARTA:
    :cvar PERIANAL:
    :cvar PERINEAL:
    :cvar PDONTTA:
    :cvar RECTAL:
    :cvar SCALP:
    :cvar SKIN:
    :cvar DRESS:
    :cvar SWAB:
    :cvar TMUCTA:
    :cvar VAGINS:
    """
    OCDRESTA = "OCDRESTA"
    SUBCONJTA = "SUBCONJTA"
    TOPICAL = "TOPICAL"
    BUC = "BUC"
    CERV = "CERV"
    DEN = "DEN"
    GIN = "GIN"
    HAIR = "HAIR"
    ICORNTA = "ICORNTA"
    ICORONTA = "ICORONTA"
    IESOPHTA = "IESOPHTA"
    IILEALTA = "IILEALTA"
    ILTOP = "ILTOP"
    ILUMTA = "ILUMTA"
    IOTOP = "IOTOP"
    IONTO = "IONTO"
    LARYNGTA = "LARYNGTA"
    MUC = "MUC"
    NAIL = "NAIL"
    NASAL = "NASAL"
    OPTHALTA = "OPTHALTA"
    ORALTA = "ORALTA"
    ORMUC = "ORMUC"
    OROPHARTA = "OROPHARTA"
    PERIANAL = "PERIANAL"
    PERINEAL = "PERINEAL"
    PDONTTA = "PDONTTA"
    RECTAL = "RECTAL"
    SCALP = "SCALP"
    SKIN = "SKIN"
    DRESS = "DRESS"
    SWAB = "SWAB"
    TMUCTA = "TMUCTA"
    VAGINS = "VAGINS"


class TopicalPowder(Enum):
    """
    specDomain: S14535 (C-0-T19651-A14411-A14412-A14484-S14534-S14535-cpt)
    :cvar TOPPWD:
    :cvar RECPWD:
    :cvar VAGPWD:
    """
    TOPPWD = "TOPPWD"
    RECPWD = "RECPWD"
    VAGPWD = "VAGPWD"


class TopicalSolution(Enum):
    """
    specDomain: S14437 (C-0-T19651-A14411-A14412-A14413-S14419-S14437-cpt)
    :cvar TOPSOL:
    :cvar LIN:
    :cvar MUCTOPSOL:
    :cvar TINC:
    """
    TOPSOL = "TOPSOL"
    LIN = "LIN"
    MUCTOPSOL = "MUCTOPSOL"
    TINC = "TINC"


class TracheostomyRoute(Enum):
    """
    abstDomain: A17352 (C-0-T14581-A17021-A17352-cpt)
    :cvar TRACH:
    :cvar TRACHINSTL:
    """
    TRACH = "TRACH"
    TRACHINSTL = "TRACHINSTL"


class Transdermal(Enum):
    """
    abstDomain: A17356 (C-0-T14581-A17021-A17356-cpt)
    :cvar TRNSDERMD:
    """
    TRNSDERMD = "TRNSDERMD"


class TransdermalPatch(Enum):
    """
    specDomain: S14500 (C-0-T19651-A14411-A14412-A14484-S14499-S14500-cpt)
    :cvar TPATCH:
    :cvar TPATH16:
    :cvar TPATH24:
    :cvar TPATH72:
    :cvar TPATH2_WK:
    :cvar TPATHWK:
    """
    TPATCH = "TPATCH"
    TPATH16 = "TPATH16"
    TPATH24 = "TPATH24"
    TPATH72 = "TPATH72"
    TPATH2_WK = "TPATH2WK"
    TPATHWK = "TPATHWK"


class Transfer(Enum):
    """
    specDomain: S17959 (C-0-T13953-A13954-A17958-S17959-cpt)
    :cvar TRANSFER:
    :cvar SALE:
    """
    TRANSFER = "TRANSFER"
    SALE = "SALE"


class TransferActReason(Enum):
    """
    abstDomain: A15983 (C-0-T14878-A15983-cpt)
    :cvar ER:
    :cvar RQ:
    """
    ER = "ER"
    RQ = "RQ"


class TransmissionRelationshipTypeCode(Enum):
    """
    vocSet: T19833 (C-0-T19833-cpt)
    :cvar SEQL:
    """
    SEQL = "SEQL"


class TransmucosalRoute(Enum):
    """
    abstDomain: A17357 (C-0-T14581-A17021-A17357-cpt)
    :cvar TMUCTA:
    """
    TMUCTA = "TMUCTA"


class TransplacentalRoute(Enum):
    """
    abstDomain: A17359 (C-0-T14581-A17021-A17359-cpt)
    :cvar TRPLACINJ:
    """
    TRPLACINJ = "TRPLACINJ"


class TransportationServiceHipaa(Enum):
    """
    abstDomain: A13849 (C-0-T13129-A13715-A13849-cpt)
    :cvar VALUE_3416_A0800_N:
    :cvar VALUE_3416_L0300_N:
    :cvar VALUE_3416_S0300_N:
    :cvar VALUE_343900000_N:
    :cvar VALUE_344600000_N:
    """
    VALUE_3416_A0800_N = "3416A0800N"
    VALUE_3416_L0300_N = "3416L0300N"
    VALUE_3416_S0300_N = "3416S0300N"
    VALUE_343900000_N = "343900000N"
    VALUE_344600000_N = "344600000N"


class TransportationServicesProviderCodes(Enum):
    """
    specDomain: S20788 (C-0-T19465-S20788-cpt)
    :cvar VALUE_341600000_X:
    :cvar VALUE_3416_A0800_X:
    :cvar VALUE_3416_L0300_X:
    :cvar VALUE_3416_S0300_X:
    :cvar VALUE_340000000_X:
    :cvar VALUE_347_B00000_X:
    :cvar VALUE_343900000_X:
    :cvar VALUE_347_C00000_X:
    :cvar VALUE_343800000_X:
    :cvar VALUE_344600000_X:
    :cvar VALUE_347_D00000_X:
    :cvar VALUE_347_E00000_X:
    """
    VALUE_341600000_X = "341600000X"
    VALUE_3416_A0800_X = "3416A0800X"
    VALUE_3416_L0300_X = "3416L0300X"
    VALUE_3416_S0300_X = "3416S0300X"
    VALUE_340000000_X = "340000000X"
    VALUE_347_B00000_X = "347B00000X"
    VALUE_343900000_X = "343900000X"
    VALUE_347_C00000_X = "347C00000X"
    VALUE_343800000_X = "343800000X"
    VALUE_344600000_X = "344600000X"
    VALUE_347_D00000_X = "347D00000X"
    VALUE_347_E00000_X = "347E00000X"


class TranstrachealRoute(Enum):
    """
    abstDomain: A17361 (C-0-T14581-A17021-A17361-cpt)
    :cvar TRTRACHINJ:
    """
    TRTRACHINJ = "TRTRACHINJ"


class TranstympanicRoute(Enum):
    """
    abstDomain: A17363 (C-0-T14581-A17021-A17363-cpt)
    :cvar TRTYMPINSTIL:
    :cvar TTYMPTABSORP:
    """
    TRTYMPINSTIL = "TRTYMPINSTIL"
    TTYMPTABSORP = "TTYMPTABSORP"


class TribalEntityUs(Enum):
    """
    vocSet: T11631 (C-0-T11631-cpt)
    :cvar VALUE_339:
    :cvar VALUE_341:
    :cvar VALUE_342:
    :cvar VALUE_345:
    :cvar VALUE_347:
    :cvar VALUE_348:
    :cvar VALUE_352:
    :cvar VALUE_354:
    :cvar VALUE_355:
    :cvar VALUE_356:
    :cvar VALUE_359:
    :cvar VALUE_361:
    :cvar VALUE_364:
    :cvar VALUE_549:
    :cvar VALUE_369:
    :cvar VALUE_371:
    :cvar VALUE_372:
    :cvar VALUE_375:
    :cvar VALUE_376:
    :cvar VALUE_377:
    :cvar VALUE_378:
    :cvar VALUE_382:
    :cvar VALUE_383:
    :cvar VALUE_386:
    :cvar VALUE_388:
    :cvar VALUE_392:
    :cvar VALUE_395:
    :cvar VALUE_396:
    :cvar VALUE_398:
    :cvar VALUE_400:
    :cvar VALUE_401:
    :cvar VALUE_406:
    :cvar VALUE_411:
    :cvar VALUE_413:
    :cvar VALUE_414:
    :cvar VALUE_415:
    :cvar VALUE_417:
    :cvar VALUE_418:
    :cvar VALUE_419:
    :cvar VALUE_420:
    :cvar VALUE_422:
    :cvar VALUE_423:
    :cvar VALUE_424:
    :cvar VALUE_425:
    :cvar VALUE_427:
    :cvar VALUE_434:
    :cvar VALUE_435:
    :cvar VALUE_437:
    :cvar VALUE_438:
    :cvar VALUE_441:
    :cvar VALUE_443:
    :cvar VALUE_445:
    :cvar VALUE_450:
    :cvar VALUE_456:
    :cvar VALUE_455:
    :cvar VALUE_457:
    :cvar VALUE_459:
    :cvar VALUE_460:
    :cvar VALUE_463:
    :cvar VALUE_465:
    :cvar VALUE_466:
    :cvar VALUE_468:
    :cvar VALUE_340:
    :cvar VALUE_343:
    :cvar VALUE_346:
    :cvar VALUE_349:
    :cvar VALUE_357:
    :cvar VALUE_360:
    :cvar VALUE_362:
    :cvar VALUE_365:
    :cvar VALUE_366:
    :cvar VALUE_367:
    :cvar VALUE_368:
    :cvar VALUE_373:
    :cvar VALUE_374:
    :cvar VALUE_379:
    :cvar VALUE_380:
    :cvar VALUE_381:
    :cvar VALUE_385:
    :cvar VALUE_389:
    :cvar VALUE_390:
    :cvar VALUE_393:
    :cvar VALUE_394:
    :cvar VALUE_397:
    :cvar VALUE_399:
    :cvar VALUE_402:
    :cvar VALUE_403:
    :cvar VALUE_404:
    :cvar VALUE_405:
    :cvar VALUE_407:
    :cvar VALUE_408:
    :cvar VALUE_409:
    :cvar VALUE_412:
    :cvar VALUE_416:
    :cvar VALUE_430:
    :cvar VALUE_431:
    :cvar VALUE_433:
    :cvar VALUE_436:
    :cvar VALUE_439:
    :cvar VALUE_440:
    :cvar VALUE_442:
    :cvar VALUE_444:
    :cvar VALUE_446:
    :cvar VALUE_448:
    :cvar VALUE_449:
    :cvar VALUE_452:
    :cvar VALUE_453:
    :cvar VALUE_454:
    :cvar VALUE_461:
    :cvar VALUE_462:
    :cvar VALUE_464:
    :cvar VALUE_467:
    :cvar VALUE_469:
    :cvar VALUE_470:
    :cvar VALUE_471:
    :cvar VALUE_472:
    :cvar VALUE_473:
    :cvar VALUE_479:
    :cvar VALUE_481:
    :cvar VALUE_483:
    :cvar VALUE_488:
    :cvar VALUE_491:
    :cvar VALUE_496:
    :cvar VALUE_497:
    :cvar VALUE_500:
    :cvar VALUE_502:
    :cvar VALUE_504:
    :cvar VALUE_506:
    :cvar VALUE_507:
    :cvar VALUE_508:
    :cvar VALUE_509:
    :cvar VALUE_510:
    :cvar VALUE_517:
    :cvar VALUE_519:
    :cvar VALUE_522:
    :cvar VALUE_524:
    :cvar VALUE_525:
    :cvar VALUE_528:
    :cvar VALUE_529:
    :cvar VALUE_530:
    :cvar VALUE_532:
    :cvar VALUE_539:
    :cvar VALUE_542:
    :cvar VALUE_543:
    :cvar VALUE_544:
    :cvar VALUE_545:
    :cvar VALUE_547:
    :cvar VALUE_548:
    :cvar VALUE_552:
    :cvar VALUE_553:
    :cvar VALUE_555:
    :cvar VALUE_558:
    :cvar VALUE_559:
    :cvar VALUE_561:
    :cvar VALUE_563:
    :cvar VALUE_564:
    :cvar VALUE_474:
    :cvar VALUE_475:
    :cvar VALUE_476:
    :cvar VALUE_477:
    :cvar VALUE_478:
    :cvar VALUE_480:
    :cvar VALUE_482:
    :cvar VALUE_484:
    :cvar VALUE_485:
    :cvar VALUE_486:
    :cvar VALUE_487:
    :cvar VALUE_489:
    :cvar VALUE_490:
    :cvar VALUE_410:
    :cvar VALUE_426:
    :cvar VALUE_432:
    :cvar VALUE_451:
    :cvar VALUE_523:
    :cvar VALUE_494:
    :cvar VALUE_495:
    :cvar VALUE_498:
    :cvar VALUE_499:
    :cvar VALUE_501:
    :cvar VALUE_503:
    :cvar VALUE_505:
    :cvar VALUE_511:
    :cvar VALUE_512:
    :cvar VALUE_513:
    :cvar VALUE_514:
    :cvar VALUE_515:
    :cvar VALUE_518:
    :cvar VALUE_520:
    :cvar VALUE_526:
    :cvar VALUE_527:
    :cvar VALUE_531:
    :cvar VALUE_533:
    :cvar VALUE_534:
    :cvar VALUE_537:
    :cvar VALUE_538:
    :cvar VALUE_541:
    :cvar VALUE_546:
    :cvar VALUE_550:
    :cvar VALUE_551:
    :cvar VALUE_554:
    :cvar VALUE_556:
    :cvar VALUE_557:
    :cvar VALUE_338:
    :cvar VALUE_344:
    :cvar VALUE_350:
    :cvar VALUE_353:
    :cvar VALUE_358:
    :cvar VALUE_363:
    :cvar VALUE_370:
    :cvar VALUE_384:
    :cvar VALUE_387:
    :cvar VALUE_391:
    :cvar VALUE_421:
    :cvar VALUE_428:
    :cvar VALUE_429:
    :cvar VALUE_447:
    :cvar VALUE_458:
    :cvar VALUE_492:
    :cvar VALUE_493:
    :cvar VALUE_516:
    :cvar VALUE_521:
    :cvar VALUE_535:
    :cvar VALUE_536:
    :cvar VALUE_540:
    :cvar VALUE_560:
    :cvar VALUE_562:
    :cvar VALUE_565:
    :cvar VALUE_566:
    :cvar VALUE_351:
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    :cvar VALUE_10:
    :cvar VALUE_11:
    :cvar VALUE_12:
    :cvar VALUE_33:
    :cvar VALUE_13:
    :cvar VALUE_14:
    :cvar VALUE_15:
    :cvar VALUE_16:
    :cvar VALUE_17:
    :cvar VALUE_18:
    :cvar VALUE_19:
    :cvar VALUE_20:
    :cvar VALUE_21:
    :cvar VALUE_160:
    :cvar VALUE_22:
    :cvar VALUE_23:
    :cvar VALUE_24:
    :cvar VALUE_25:
    :cvar VALUE_26:
    :cvar VALUE_27:
    :cvar VALUE_29:
    :cvar VALUE_28:
    :cvar VALUE_30:
    :cvar VALUE_31:
    :cvar VALUE_32:
    :cvar VALUE_35:
    :cvar VALUE_36:
    :cvar VALUE_37:
    :cvar VALUE_38:
    :cvar VALUE_39:
    :cvar VALUE_40:
    :cvar VALUE_42:
    :cvar VALUE_41:
    :cvar VALUE_43:
    :cvar VALUE_44:
    :cvar VALUE_45:
    :cvar VALUE_46:
    :cvar VALUE_47:
    :cvar VALUE_48:
    :cvar VALUE_49:
    :cvar VALUE_50:
    :cvar VALUE_51:
    :cvar VALUE_52:
    :cvar VALUE_53:
    :cvar VALUE_54:
    :cvar VALUE_55:
    :cvar VALUE_64:
    :cvar VALUE_56:
    :cvar VALUE_57:
    :cvar VALUE_58:
    :cvar VALUE_59:
    :cvar VALUE_60:
    :cvar VALUE_61:
    :cvar VALUE_62:
    :cvar VALUE_63:
    :cvar VALUE_65:
    :cvar VALUE_66:
    :cvar VALUE_67:
    :cvar VALUE_68:
    :cvar VALUE_69:
    :cvar VALUE_71:
    :cvar VALUE_70:
    :cvar VALUE_72:
    :cvar VALUE_73:
    :cvar VALUE_74:
    :cvar VALUE_75:
    :cvar VALUE_76:
    :cvar VALUE_77:
    :cvar VALUE_78:
    :cvar VALUE_79:
    :cvar VALUE_80:
    :cvar VALUE_81:
    :cvar VALUE_82:
    :cvar VALUE_83:
    :cvar VALUE_84:
    :cvar VALUE_85:
    :cvar VALUE_86:
    :cvar VALUE_87:
    :cvar VALUE_88:
    :cvar VALUE_89:
    :cvar VALUE_90:
    :cvar VALUE_91:
    :cvar VALUE_92:
    :cvar VALUE_93:
    :cvar VALUE_94:
    :cvar VALUE_95:
    :cvar VALUE_96:
    :cvar VALUE_97:
    :cvar VALUE_98:
    :cvar VALUE_99:
    :cvar VALUE_100:
    :cvar VALUE_101:
    :cvar VALUE_102:
    :cvar VALUE_103:
    :cvar VALUE_104:
    :cvar VALUE_105:
    :cvar VALUE_106:
    :cvar VALUE_107:
    :cvar VALUE_108:
    :cvar VALUE_109:
    :cvar VALUE_110:
    :cvar VALUE_111:
    :cvar VALUE_112:
    :cvar VALUE_113:
    :cvar VALUE_114:
    :cvar VALUE_115:
    :cvar VALUE_116:
    :cvar VALUE_117:
    :cvar VALUE_118:
    :cvar VALUE_119:
    :cvar VALUE_120:
    :cvar VALUE_121:
    :cvar VALUE_122:
    :cvar VALUE_123:
    :cvar VALUE_124:
    :cvar VALUE_127:
    :cvar VALUE_125:
    :cvar VALUE_126:
    :cvar VALUE_128:
    :cvar VALUE_129:
    :cvar VALUE_130:
    :cvar VALUE_131:
    :cvar VALUE_132:
    :cvar VALUE_133:
    :cvar VALUE_135:
    :cvar VALUE_134:
    :cvar VALUE_136:
    :cvar VALUE_137:
    :cvar VALUE_138:
    :cvar VALUE_140:
    :cvar VALUE_141:
    :cvar VALUE_142:
    :cvar VALUE_143:
    :cvar VALUE_139:
    :cvar VALUE_144:
    :cvar VALUE_145:
    :cvar VALUE_146:
    :cvar VALUE_147:
    :cvar VALUE_148:
    :cvar VALUE_149:
    :cvar VALUE_150:
    :cvar VALUE_151:
    :cvar VALUE_152:
    :cvar VALUE_153:
    :cvar VALUE_154:
    :cvar VALUE_155:
    :cvar VALUE_156:
    :cvar VALUE_157:
    :cvar VALUE_158:
    :cvar VALUE_159:
    :cvar VALUE_161:
    :cvar VALUE_162:
    :cvar VALUE_163:
    :cvar VALUE_164:
    :cvar VALUE_165:
    :cvar VALUE_166:
    :cvar VALUE_167:
    :cvar VALUE_168:
    :cvar VALUE_169:
    :cvar VALUE_170:
    :cvar VALUE_171:
    :cvar VALUE_172:
    :cvar VALUE_173:
    :cvar VALUE_174:
    :cvar VALUE_175:
    :cvar VALUE_176:
    :cvar VALUE_177:
    :cvar VALUE_178:
    :cvar VALUE_179:
    :cvar VALUE_180:
    :cvar VALUE_181:
    :cvar VALUE_182:
    :cvar VALUE_184:
    :cvar VALUE_183:
    :cvar VALUE_185:
    :cvar VALUE_186:
    :cvar VALUE_188:
    :cvar VALUE_187:
    :cvar VALUE_189:
    :cvar VALUE_190:
    :cvar VALUE_191:
    :cvar VALUE_192:
    :cvar VALUE_193:
    :cvar VALUE_194:
    :cvar VALUE_195:
    :cvar VALUE_196:
    :cvar VALUE_197:
    :cvar VALUE_198:
    :cvar VALUE_199:
    :cvar VALUE_200:
    :cvar VALUE_201:
    :cvar VALUE_202:
    :cvar VALUE_203:
    :cvar VALUE_204:
    :cvar VALUE_205:
    :cvar VALUE_206:
    :cvar VALUE_207:
    :cvar VALUE_208:
    :cvar VALUE_209:
    :cvar VALUE_210:
    :cvar VALUE_212:
    :cvar VALUE_211:
    :cvar VALUE_213:
    :cvar VALUE_214:
    :cvar VALUE_215:
    :cvar VALUE_216:
    :cvar VALUE_217:
    :cvar VALUE_219:
    :cvar VALUE_218:
    :cvar VALUE_220:
    :cvar VALUE_221:
    :cvar VALUE_222:
    :cvar VALUE_223:
    :cvar VALUE_224:
    :cvar VALUE_225:
    :cvar VALUE_226:
    :cvar VALUE_227:
    :cvar VALUE_228:
    :cvar VALUE_229:
    :cvar VALUE_230:
    :cvar VALUE_231:
    :cvar VALUE_232:
    :cvar VALUE_233:
    :cvar VALUE_234:
    :cvar VALUE_235:
    :cvar VALUE_236:
    :cvar VALUE_237:
    :cvar VALUE_238:
    :cvar VALUE_239:
    :cvar VALUE_240:
    :cvar VALUE_241:
    :cvar VALUE_242:
    :cvar VALUE_243:
    :cvar VALUE_244:
    :cvar VALUE_245:
    :cvar VALUE_247:
    :cvar VALUE_248:
    :cvar VALUE_246:
    :cvar VALUE_249:
    :cvar VALUE_250:
    :cvar VALUE_251:
    :cvar VALUE_252:
    :cvar VALUE_253:
    :cvar VALUE_254:
    :cvar VALUE_255:
    :cvar VALUE_257:
    :cvar VALUE_256:
    :cvar VALUE_258:
    :cvar VALUE_259:
    :cvar VALUE_260:
    :cvar VALUE_261:
    :cvar VALUE_262:
    :cvar VALUE_263:
    :cvar VALUE_264:
    :cvar VALUE_265:
    :cvar VALUE_266:
    :cvar VALUE_267:
    :cvar VALUE_268:
    :cvar VALUE_269:
    :cvar VALUE_270:
    :cvar VALUE_271:
    :cvar VALUE_272:
    :cvar VALUE_273:
    :cvar VALUE_274:
    :cvar VALUE_275:
    :cvar VALUE_276:
    :cvar VALUE_277:
    :cvar VALUE_278:
    :cvar VALUE_279:
    :cvar VALUE_280:
    :cvar VALUE_281:
    :cvar VALUE_282:
    :cvar VALUE_283:
    :cvar VALUE_284:
    :cvar VALUE_285:
    :cvar VALUE_286:
    :cvar VALUE_287:
    :cvar VALUE_288:
    :cvar VALUE_289:
    :cvar VALUE_291:
    :cvar VALUE_290:
    :cvar VALUE_292:
    :cvar VALUE_293:
    :cvar VALUE_294:
    :cvar VALUE_295:
    :cvar VALUE_296:
    :cvar VALUE_297:
    :cvar VALUE_298:
    :cvar VALUE_299:
    :cvar VALUE_300:
    :cvar VALUE_301:
    :cvar VALUE_302:
    :cvar VALUE_303:
    :cvar VALUE_304:
    :cvar VALUE_305:
    :cvar VALUE_306:
    :cvar VALUE_308:
    :cvar VALUE_307:
    :cvar VALUE_309:
    :cvar VALUE_310:
    :cvar VALUE_311:
    :cvar VALUE_312:
    :cvar VALUE_313:
    :cvar VALUE_314:
    :cvar VALUE_315:
    :cvar VALUE_316:
    :cvar VALUE_317:
    :cvar VALUE_318:
    :cvar VALUE_319:
    :cvar VALUE_320:
    :cvar VALUE_321:
    :cvar VALUE_34:
    :cvar VALUE_322:
    :cvar VALUE_323:
    :cvar VALUE_324:
    :cvar VALUE_325:
    :cvar VALUE_326:
    :cvar VALUE_327:
    :cvar VALUE_328:
    :cvar VALUE_329:
    :cvar VALUE_330:
    :cvar VALUE_331:
    :cvar VALUE_332:
    :cvar VALUE_333:
    :cvar VALUE_334:
    :cvar VALUE_335:
    :cvar VALUE_336:
    :cvar VALUE_337:
    """
    VALUE_339 = "339"
    VALUE_341 = "341"
    VALUE_342 = "342"
    VALUE_345 = "345"
    VALUE_347 = "347"
    VALUE_348 = "348"
    VALUE_352 = "352"
    VALUE_354 = "354"
    VALUE_355 = "355"
    VALUE_356 = "356"
    VALUE_359 = "359"
    VALUE_361 = "361"
    VALUE_364 = "364"
    VALUE_549 = "549"
    VALUE_369 = "369"
    VALUE_371 = "371"
    VALUE_372 = "372"
    VALUE_375 = "375"
    VALUE_376 = "376"
    VALUE_377 = "377"
    VALUE_378 = "378"
    VALUE_382 = "382"
    VALUE_383 = "383"
    VALUE_386 = "386"
    VALUE_388 = "388"
    VALUE_392 = "392"
    VALUE_395 = "395"
    VALUE_396 = "396"
    VALUE_398 = "398"
    VALUE_400 = "400"
    VALUE_401 = "401"
    VALUE_406 = "406"
    VALUE_411 = "411"
    VALUE_413 = "413"
    VALUE_414 = "414"
    VALUE_415 = "415"
    VALUE_417 = "417"
    VALUE_418 = "418"
    VALUE_419 = "419"
    VALUE_420 = "420"
    VALUE_422 = "422"
    VALUE_423 = "423"
    VALUE_424 = "424"
    VALUE_425 = "425"
    VALUE_427 = "427"
    VALUE_434 = "434"
    VALUE_435 = "435"
    VALUE_437 = "437"
    VALUE_438 = "438"
    VALUE_441 = "441"
    VALUE_443 = "443"
    VALUE_445 = "445"
    VALUE_450 = "450"
    VALUE_456 = "456"
    VALUE_455 = "455"
    VALUE_457 = "457"
    VALUE_459 = "459"
    VALUE_460 = "460"
    VALUE_463 = "463"
    VALUE_465 = "465"
    VALUE_466 = "466"
    VALUE_468 = "468"
    VALUE_340 = "340"
    VALUE_343 = "343"
    VALUE_346 = "346"
    VALUE_349 = "349"
    VALUE_357 = "357"
    VALUE_360 = "360"
    VALUE_362 = "362"
    VALUE_365 = "365"
    VALUE_366 = "366"
    VALUE_367 = "367"
    VALUE_368 = "368"
    VALUE_373 = "373"
    VALUE_374 = "374"
    VALUE_379 = "379"
    VALUE_380 = "380"
    VALUE_381 = "381"
    VALUE_385 = "385"
    VALUE_389 = "389"
    VALUE_390 = "390"
    VALUE_393 = "393"
    VALUE_394 = "394"
    VALUE_397 = "397"
    VALUE_399 = "399"
    VALUE_402 = "402"
    VALUE_403 = "403"
    VALUE_404 = "404"
    VALUE_405 = "405"
    VALUE_407 = "407"
    VALUE_408 = "408"
    VALUE_409 = "409"
    VALUE_412 = "412"
    VALUE_416 = "416"
    VALUE_430 = "430"
    VALUE_431 = "431"
    VALUE_433 = "433"
    VALUE_436 = "436"
    VALUE_439 = "439"
    VALUE_440 = "440"
    VALUE_442 = "442"
    VALUE_444 = "444"
    VALUE_446 = "446"
    VALUE_448 = "448"
    VALUE_449 = "449"
    VALUE_452 = "452"
    VALUE_453 = "453"
    VALUE_454 = "454"
    VALUE_461 = "461"
    VALUE_462 = "462"
    VALUE_464 = "464"
    VALUE_467 = "467"
    VALUE_469 = "469"
    VALUE_470 = "470"
    VALUE_471 = "471"
    VALUE_472 = "472"
    VALUE_473 = "473"
    VALUE_479 = "479"
    VALUE_481 = "481"
    VALUE_483 = "483"
    VALUE_488 = "488"
    VALUE_491 = "491"
    VALUE_496 = "496"
    VALUE_497 = "497"
    VALUE_500 = "500"
    VALUE_502 = "502"
    VALUE_504 = "504"
    VALUE_506 = "506"
    VALUE_507 = "507"
    VALUE_508 = "508"
    VALUE_509 = "509"
    VALUE_510 = "510"
    VALUE_517 = "517"
    VALUE_519 = "519"
    VALUE_522 = "522"
    VALUE_524 = "524"
    VALUE_525 = "525"
    VALUE_528 = "528"
    VALUE_529 = "529"
    VALUE_530 = "530"
    VALUE_532 = "532"
    VALUE_539 = "539"
    VALUE_542 = "542"
    VALUE_543 = "543"
    VALUE_544 = "544"
    VALUE_545 = "545"
    VALUE_547 = "547"
    VALUE_548 = "548"
    VALUE_552 = "552"
    VALUE_553 = "553"
    VALUE_555 = "555"
    VALUE_558 = "558"
    VALUE_559 = "559"
    VALUE_561 = "561"
    VALUE_563 = "563"
    VALUE_564 = "564"
    VALUE_474 = "474"
    VALUE_475 = "475"
    VALUE_476 = "476"
    VALUE_477 = "477"
    VALUE_478 = "478"
    VALUE_480 = "480"
    VALUE_482 = "482"
    VALUE_484 = "484"
    VALUE_485 = "485"
    VALUE_486 = "486"
    VALUE_487 = "487"
    VALUE_489 = "489"
    VALUE_490 = "490"
    VALUE_410 = "410"
    VALUE_426 = "426"
    VALUE_432 = "432"
    VALUE_451 = "451"
    VALUE_523 = "523"
    VALUE_494 = "494"
    VALUE_495 = "495"
    VALUE_498 = "498"
    VALUE_499 = "499"
    VALUE_501 = "501"
    VALUE_503 = "503"
    VALUE_505 = "505"
    VALUE_511 = "511"
    VALUE_512 = "512"
    VALUE_513 = "513"
    VALUE_514 = "514"
    VALUE_515 = "515"
    VALUE_518 = "518"
    VALUE_520 = "520"
    VALUE_526 = "526"
    VALUE_527 = "527"
    VALUE_531 = "531"
    VALUE_533 = "533"
    VALUE_534 = "534"
    VALUE_537 = "537"
    VALUE_538 = "538"
    VALUE_541 = "541"
    VALUE_546 = "546"
    VALUE_550 = "550"
    VALUE_551 = "551"
    VALUE_554 = "554"
    VALUE_556 = "556"
    VALUE_557 = "557"
    VALUE_338 = "338"
    VALUE_344 = "344"
    VALUE_350 = "350"
    VALUE_353 = "353"
    VALUE_358 = "358"
    VALUE_363 = "363"
    VALUE_370 = "370"
    VALUE_384 = "384"
    VALUE_387 = "387"
    VALUE_391 = "391"
    VALUE_421 = "421"
    VALUE_428 = "428"
    VALUE_429 = "429"
    VALUE_447 = "447"
    VALUE_458 = "458"
    VALUE_492 = "492"
    VALUE_493 = "493"
    VALUE_516 = "516"
    VALUE_521 = "521"
    VALUE_535 = "535"
    VALUE_536 = "536"
    VALUE_540 = "540"
    VALUE_560 = "560"
    VALUE_562 = "562"
    VALUE_565 = "565"
    VALUE_566 = "566"
    VALUE_351 = "351"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_33 = "33"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_160 = "160"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_29 = "29"
    VALUE_28 = "28"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_42 = "42"
    VALUE_41 = "41"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_64 = "64"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_71 = "71"
    VALUE_70 = "70"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_81 = "81"
    VALUE_82 = "82"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_88 = "88"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"
    VALUE_100 = "100"
    VALUE_101 = "101"
    VALUE_102 = "102"
    VALUE_103 = "103"
    VALUE_104 = "104"
    VALUE_105 = "105"
    VALUE_106 = "106"
    VALUE_107 = "107"
    VALUE_108 = "108"
    VALUE_109 = "109"
    VALUE_110 = "110"
    VALUE_111 = "111"
    VALUE_112 = "112"
    VALUE_113 = "113"
    VALUE_114 = "114"
    VALUE_115 = "115"
    VALUE_116 = "116"
    VALUE_117 = "117"
    VALUE_118 = "118"
    VALUE_119 = "119"
    VALUE_120 = "120"
    VALUE_121 = "121"
    VALUE_122 = "122"
    VALUE_123 = "123"
    VALUE_124 = "124"
    VALUE_127 = "127"
    VALUE_125 = "125"
    VALUE_126 = "126"
    VALUE_128 = "128"
    VALUE_129 = "129"
    VALUE_130 = "130"
    VALUE_131 = "131"
    VALUE_132 = "132"
    VALUE_133 = "133"
    VALUE_135 = "135"
    VALUE_134 = "134"
    VALUE_136 = "136"
    VALUE_137 = "137"
    VALUE_138 = "138"
    VALUE_140 = "140"
    VALUE_141 = "141"
    VALUE_142 = "142"
    VALUE_143 = "143"
    VALUE_139 = "139"
    VALUE_144 = "144"
    VALUE_145 = "145"
    VALUE_146 = "146"
    VALUE_147 = "147"
    VALUE_148 = "148"
    VALUE_149 = "149"
    VALUE_150 = "150"
    VALUE_151 = "151"
    VALUE_152 = "152"
    VALUE_153 = "153"
    VALUE_154 = "154"
    VALUE_155 = "155"
    VALUE_156 = "156"
    VALUE_157 = "157"
    VALUE_158 = "158"
    VALUE_159 = "159"
    VALUE_161 = "161"
    VALUE_162 = "162"
    VALUE_163 = "163"
    VALUE_164 = "164"
    VALUE_165 = "165"
    VALUE_166 = "166"
    VALUE_167 = "167"
    VALUE_168 = "168"
    VALUE_169 = "169"
    VALUE_170 = "170"
    VALUE_171 = "171"
    VALUE_172 = "172"
    VALUE_173 = "173"
    VALUE_174 = "174"
    VALUE_175 = "175"
    VALUE_176 = "176"
    VALUE_177 = "177"
    VALUE_178 = "178"
    VALUE_179 = "179"
    VALUE_180 = "180"
    VALUE_181 = "181"
    VALUE_182 = "182"
    VALUE_184 = "184"
    VALUE_183 = "183"
    VALUE_185 = "185"
    VALUE_186 = "186"
    VALUE_188 = "188"
    VALUE_187 = "187"
    VALUE_189 = "189"
    VALUE_190 = "190"
    VALUE_191 = "191"
    VALUE_192 = "192"
    VALUE_193 = "193"
    VALUE_194 = "194"
    VALUE_195 = "195"
    VALUE_196 = "196"
    VALUE_197 = "197"
    VALUE_198 = "198"
    VALUE_199 = "199"
    VALUE_200 = "200"
    VALUE_201 = "201"
    VALUE_202 = "202"
    VALUE_203 = "203"
    VALUE_204 = "204"
    VALUE_205 = "205"
    VALUE_206 = "206"
    VALUE_207 = "207"
    VALUE_208 = "208"
    VALUE_209 = "209"
    VALUE_210 = "210"
    VALUE_212 = "212"
    VALUE_211 = "211"
    VALUE_213 = "213"
    VALUE_214 = "214"
    VALUE_215 = "215"
    VALUE_216 = "216"
    VALUE_217 = "217"
    VALUE_219 = "219"
    VALUE_218 = "218"
    VALUE_220 = "220"
    VALUE_221 = "221"
    VALUE_222 = "222"
    VALUE_223 = "223"
    VALUE_224 = "224"
    VALUE_225 = "225"
    VALUE_226 = "226"
    VALUE_227 = "227"
    VALUE_228 = "228"
    VALUE_229 = "229"
    VALUE_230 = "230"
    VALUE_231 = "231"
    VALUE_232 = "232"
    VALUE_233 = "233"
    VALUE_234 = "234"
    VALUE_235 = "235"
    VALUE_236 = "236"
    VALUE_237 = "237"
    VALUE_238 = "238"
    VALUE_239 = "239"
    VALUE_240 = "240"
    VALUE_241 = "241"
    VALUE_242 = "242"
    VALUE_243 = "243"
    VALUE_244 = "244"
    VALUE_245 = "245"
    VALUE_247 = "247"
    VALUE_248 = "248"
    VALUE_246 = "246"
    VALUE_249 = "249"
    VALUE_250 = "250"
    VALUE_251 = "251"
    VALUE_252 = "252"
    VALUE_253 = "253"
    VALUE_254 = "254"
    VALUE_255 = "255"
    VALUE_257 = "257"
    VALUE_256 = "256"
    VALUE_258 = "258"
    VALUE_259 = "259"
    VALUE_260 = "260"
    VALUE_261 = "261"
    VALUE_262 = "262"
    VALUE_263 = "263"
    VALUE_264 = "264"
    VALUE_265 = "265"
    VALUE_266 = "266"
    VALUE_267 = "267"
    VALUE_268 = "268"
    VALUE_269 = "269"
    VALUE_270 = "270"
    VALUE_271 = "271"
    VALUE_272 = "272"
    VALUE_273 = "273"
    VALUE_274 = "274"
    VALUE_275 = "275"
    VALUE_276 = "276"
    VALUE_277 = "277"
    VALUE_278 = "278"
    VALUE_279 = "279"
    VALUE_280 = "280"
    VALUE_281 = "281"
    VALUE_282 = "282"
    VALUE_283 = "283"
    VALUE_284 = "284"
    VALUE_285 = "285"
    VALUE_286 = "286"
    VALUE_287 = "287"
    VALUE_288 = "288"
    VALUE_289 = "289"
    VALUE_291 = "291"
    VALUE_290 = "290"
    VALUE_292 = "292"
    VALUE_293 = "293"
    VALUE_294 = "294"
    VALUE_295 = "295"
    VALUE_296 = "296"
    VALUE_297 = "297"
    VALUE_298 = "298"
    VALUE_299 = "299"
    VALUE_300 = "300"
    VALUE_301 = "301"
    VALUE_302 = "302"
    VALUE_303 = "303"
    VALUE_304 = "304"
    VALUE_305 = "305"
    VALUE_306 = "306"
    VALUE_308 = "308"
    VALUE_307 = "307"
    VALUE_309 = "309"
    VALUE_310 = "310"
    VALUE_311 = "311"
    VALUE_312 = "312"
    VALUE_313 = "313"
    VALUE_314 = "314"
    VALUE_315 = "315"
    VALUE_316 = "316"
    VALUE_317 = "317"
    VALUE_318 = "318"
    VALUE_319 = "319"
    VALUE_320 = "320"
    VALUE_321 = "321"
    VALUE_34 = "34"
    VALUE_322 = "322"
    VALUE_323 = "323"
    VALUE_324 = "324"
    VALUE_325 = "325"
    VALUE_326 = "326"
    VALUE_327 = "327"
    VALUE_328 = "328"
    VALUE_329 = "329"
    VALUE_330 = "330"
    VALUE_331 = "331"
    VALUE_332 = "332"
    VALUE_333 = "333"
    VALUE_334 = "334"
    VALUE_335 = "335"
    VALUE_336 = "336"
    VALUE_337 = "337"


class Tsamosan(Enum):
    """
    abstDomain: A18533 (C-0-T18130-A18523-A18533-cpt)
    :cvar X_COW:
    :cvar X_CEA:
    :cvar X_QUN:
    :cvar X_CJH:
    """
    X_COW = "x-COW"
    X_CEA = "x-CEA"
    X_QUN = "x-QUN"
    X_CJH = "x-CJH"


class Tsimshianic(Enum):
    """
    abstDomain: A18511 (C-0-T18130-A18413-A18511-cpt)
    :cvar X_TSI:
    """
    X_TSI = "x-TSI"


class Urlscheme(Enum):
    """
    vocSet: T14866 (C-0-T14866-cpt)
    :cvar FAX:
    :cvar MAILTO:
    :cvar TEL:
    :cvar FTP:
    :cvar FILE:
    :cvar HTTP:
    :cvar MLLP:
    :cvar MODEM:
    :cvar NFS:
    :cvar TELNET:
    """
    FAX = "fax"
    MAILTO = "mailto"
    TEL = "tel"
    FTP = "ftp"
    FILE = "file"
    HTTP = "http"
    MLLP = "mllp"
    MODEM = "modem"
    NFS = "nfs"
    TELNET = "telnet"


class UnderwriterParticipationFunction(Enum):
    """
    abstDomain: A19904 (C-0-T10267-A19903-A19904-cpt)
    :cvar PAYORCNTR:
    :cvar REINS:
    :cvar RETROCES:
    :cvar SUBCTRT:
    :cvar UNDERWRTNG:
    """
    PAYORCNTR = "PAYORCNTR"
    REINS = "REINS"
    RETROCES = "RETROCES"
    SUBCTRT = "SUBCTRT"
    UNDERWRTNG = "UNDERWRTNG"


class UnitOfMeasureAtomBaseUnitInsens(Enum):
    """
    abstDomain: A12550 (C-0-T12549-A12550-cpt)
    :cvar C:
    :cvar K:
    :cvar CD:
    :cvar G:
    :cvar M:
    :cvar RAD:
    :cvar S:
    """
    C = "C"
    K = "K"
    CD = "CD"
    G = "G"
    M = "M"
    RAD = "RAD"
    S = "S"


class UnitOfMeasureAtomBaseUnitSens(Enum):
    """
    abstDomain: A12840 (C-0-T12839-A12840-cpt)
    :cvar C:
    :cvar K:
    :cvar CD:
    :cvar G:
    :cvar M:
    :cvar RAD:
    :cvar S:
    """
    C = "C"
    K = "K"
    CD = "cd"
    G = "g"
    M = "m"
    RAD = "rad"
    S = "s"


class UnitOfMeasureAtomInsens(Enum):
    """
    abstDomain: A12558 (C-0-T12549-A12558-cpt)
    :cvar APL_U:
    :cvar A:
    :cvar AO:
    :cvar BQ:
    :cvar BETH_U:
    :cvar BI:
    :cvar BDSK_U:
    :cvar K:
    :cvar BTU_39:
    :cvar BTU_59:
    :cvar BTU_60:
    :cvar BTU_IT:
    :cvar BTU_M:
    :cvar BTU_TH:
    :cvar BTU:
    :cvar CAL:
    :cvar CH:
    :cvar CI:
    :cvar DYE_U:
    :cvar F:
    :cvar GPL_U:
    :cvar GL:
    :cvar GS:
    :cvar GB:
    :cvar GY:
    :cvar H:
    :cvar HZ:
    :cvar HNSF_U:
    :cvar J:
    :cvar KY:
    :cvar KA_U:
    :cvar KNK_U:
    :cvar LMB:
    :cvar MPL_U:
    :cvar MCLG_U:
    :cvar MX:
    :cvar N:
    :cvar GC:
    :cvar OE:
    :cvar OHM:
    :cvar PAL:
    :cvar H_1:
    :cvar P:
    :cvar PCA_PR:
    :cvar PNT_PR:
    :cvar ROE:
    :cvar SIE:
    :cvar SV:
    :cvar SMGY_U:
    :cvar ST:
    :cvar S:
    :cvar T:
    :cvar TODD_U:
    :cvar U:
    :cvar USP_U:
    :cvar V:
    :cvar W:
    :cvar WB:
    :cvar G:
    :cvar ACR_BR:
    :cvar ACR_US:
    :cvar ARB_U:
    :cvar AR:
    :cvar ASU:
    :cvar ATM:
    :cvar ATT:
    :cvar BAR:
    :cvar BRN:
    :cvar BBL_US:
    :cvar BD:
    :cvar B:
    :cvar B_KW:
    :cvar B_UV:
    :cvar B_MV:
    :cvar B_SPL:
    :cvar B_V:
    :cvar B_W:
    :cvar BIT:
    :cvar BIT_S:
    :cvar BF_I:
    :cvar BU_US:
    :cvar PK_BR:
    :cvar BY:
    :cvar CAL_15:
    :cvar CAL_20:
    :cvar CAL_IT:
    :cvar CAL_M:
    :cvar CAL_TH:
    :cvar CAL_1:
    :cvar CAR_M:
    :cvar CAR_AU:
    :cvar CH_BR:
    :cvar CH_US:
    :cvar RCH_US:
    :cvar CICERO:
    :cvar CIRC:
    :cvar CML_I:
    :cvar CR_I:
    :cvar CRD_US:
    :cvar CFT_I:
    :cvar CIN_I:
    :cvar CYD_I:
    :cvar CUP_US:
    :cvar D:
    :cvar DEG:
    :cvar CEL:
    :cvar DEGF:
    :cvar DIDOT:
    :cvar DIOP:
    :cvar DR_AV:
    :cvar DR_AP:
    :cvar DRP:
    :cvar DPT_US:
    :cvar DQT_US:
    :cvar DYN:
    :cvar M_E:
    :cvar EV:
    :cvar E:
    :cvar EQ:
    :cvar ERG:
    :cvar FTH_BR:
    :cvar FTH_I:
    :cvar FTH_US:
    :cvar FDR_BR:
    :cvar FDR_US:
    :cvar FOZ_BR:
    :cvar FOZ_US:
    :cvar FT_BR:
    :cvar FT_I:
    :cvar FT_US:
    :cvar RD_BR:
    :cvar FUR_US:
    :cvar GAL_BR:
    :cvar GAL_US:
    :cvar GIL_BR:
    :cvar GIL_US:
    :cvar GON:
    :cvar GR:
    :cvar G_1:
    :cvar GF:
    :cvar HD_I:
    :cvar HPF:
    :cvar HR:
    :cvar IN_BR:
    :cvar IN_I:
    :cvar IN_US:
    :cvar IN_I_HG:
    :cvar IN_I_H2_O:
    :cvar IU:
    :cvar KAT:
    :cvar KN_BR:
    :cvar KN_I:
    :cvar LY:
    :cvar LIGNE:
    :cvar LNE:
    :cvar LK_BR:
    :cvar LK_US:
    :cvar RLK_US:
    :cvar L:
    :cvar LCWT_AV:
    :cvar LTON_AV:
    :cvar LPF:
    :cvar LM:
    :cvar LX:
    :cvar MESH_I:
    :cvar MET:
    :cvar M_HG:
    :cvar M_H2_O:
    :cvar MIL_I:
    :cvar MIL_US:
    :cvar MI_BR:
    :cvar MI_US:
    :cvar MIN_BR:
    :cvar MIN_US:
    :cvar VALUE:
    :cvar MIN:
    :cvar MOL:
    :cvar MO:
    :cvar MO_G:
    :cvar MO_J:
    :cvar MO_S:
    :cvar NMI_BR:
    :cvar NMI_I:
    :cvar NEP:
    :cvar OSM:
    :cvar OZ_AP:
    :cvar OZ_AV:
    :cvar OZ_TR:
    :cvar PH:
    :cvar PC_BR:
    :cvar PRS:
    :cvar PPB:
    :cvar PPM:
    :cvar PPTH:
    :cvar PPTR:
    :cvar BU_BR:
    :cvar PK_US:
    :cvar PWT_TR:
    :cvar VALUE_1:
    :cvar PRU:
    :cvar MU_0:
    :cvar EPS_0:
    :cvar PHT:
    :cvar PCA:
    :cvar PIED:
    :cvar PT_BR:
    :cvar PT_US:
    :cvar PNT:
    :cvar POUCE:
    :cvar LB_AP:
    :cvar LB_AV:
    :cvar LB_TR:
    :cvar LBF_AV:
    :cvar M_P:
    :cvar PSI:
    :cvar QT_BR:
    :cvar QT_US:
    :cvar RAD:
    :cvar REM:
    :cvar RD_US:
    :cvar SC_AP:
    :cvar VALUE_2:
    :cvar SCT:
    :cvar SCWT_AV:
    :cvar STON_AV:
    :cvar SPH:
    :cvar SFT_I:
    :cvar SIN_I:
    :cvar SMI_US:
    :cvar SRD_US:
    :cvar SYD_I:
    :cvar MI_I:
    :cvar STR_VALUE:
    :cvar SB:
    :cvar STONE_AV:
    :cvar SR:
    :cvar TBS_US:
    :cvar TSP_US:
    :cvar VALUE_10:
    :cvar PI:
    :cvar TNE:
    :cvar TWP:
    :cvar TB_U:
    :cvar AMU:
    :cvar C:
    :cvar WK:
    :cvar GAL_WI:
    :cvar YD_BR:
    :cvar YD_I:
    :cvar YD_US:
    :cvar ANN:
    :cvar ANN_G:
    :cvar ANN_J:
    :cvar ANN_T:
    """
    APL_U = "[APL'U]"
    A = "A"
    AO = "AO"
    BQ = "BQ"
    BETH_U = "[BETH'U]"
    BI = "BI"
    BDSK_U = "[BDSK'U]"
    K = "[K]"
    BTU_39 = "[BTU_39]"
    BTU_59 = "[BTU_59]"
    BTU_60 = "[BTU_60]"
    BTU_IT = "[BTU_IT]"
    BTU_M = "[BTU_M]"
    BTU_TH = "[BTU_TH]"
    BTU = "[BTU]"
    CAL = "[CAL]"
    CH = "[CH]"
    CI = "CI"
    DYE_U = "[DYE'U]"
    F = "F"
    GPL_U = "[GPL'U]"
    GL = "GL"
    GS = "GS"
    GB = "GB"
    GY = "GY"
    H = "H"
    HZ = "HZ"
    HNSF_U = "[HNSF'U]"
    J = "J"
    KY = "KY"
    KA_U = "[KA'U]"
    KNK_U = "[KNK'U]"
    LMB = "LMB"
    MPL_U = "[MPL'U]"
    MCLG_U = "[MCLG'U]"
    MX = "MX"
    N = "N"
    GC = "[GC]"
    OE = "OE"
    OHM = "OHM"
    PAL = "PAL"
    H_1 = "[H]"
    P = "P"
    PCA_PR = "[PCA_PR]"
    PNT_PR = "[PNT_PR]"
    ROE = "ROE"
    SIE = "SIE"
    SV = "SV"
    SMGY_U = "[SMGY'U]"
    ST = "ST"
    S = "[S]"
    T = "T"
    TODD_U = "[TODD'U]"
    U = "U"
    USP_U = "[USP'U]"
    V = "V"
    W = "W"
    WB = "WB"
    G = "[G]"
    ACR_BR = "[ACR_BR]"
    ACR_US = "[ACR_US]"
    ARB_U = "[ARB'U]"
    AR = "AR"
    ASU = "ASU"
    ATM = "ATM"
    ATT = "ATT"
    BAR = "BAR"
    BRN = "BRN"
    BBL_US = "[BBL_US]"
    BD = "BD"
    B = "B"
    B_KW = "B[KW]"
    B_UV = "B[UV]"
    B_MV = "B[MV]"
    B_SPL = "B[SPL]"
    B_V = "B[V]"
    B_W = "B[W]"
    BIT = "BIT"
    BIT_S = "BIT_S"
    BF_I = "[BF_I]"
    BU_US = "[BU_US]"
    PK_BR = "[PK_BR]"
    BY = "BY"
    CAL_15 = "CAL_[15]"
    CAL_20 = "CAL_[20]"
    CAL_IT = "CAL_IT"
    CAL_M = "CAL_M"
    CAL_TH = "CAL_TH"
    CAL_1 = "CAL"
    CAR_M = "[CAR_M]"
    CAR_AU = "[CAR_AU]"
    CH_BR = "[CH_BR]"
    CH_US = "[CH_US]"
    RCH_US = "[RCH_US]"
    CICERO = "[CICERO]"
    CIRC = "CIRC"
    CML_I = "[CML_I]"
    CR_I = "[CR_I]"
    CRD_US = "[CRD_US]"
    CFT_I = "[CFT_I]"
    CIN_I = "[CIN_I]"
    CYD_I = "[CYD_I]"
    CUP_US = "[CUP_US]"
    D = "D"
    DEG = "DEG"
    CEL = "CEL"
    DEGF = "[DEGF]"
    DIDOT = "[DIDOT]"
    DIOP = "[DIOP]"
    DR_AV = "[DR_AV]"
    DR_AP = "[DR_AP]"
    DRP = "[DRP]"
    DPT_US = "[DPT_US]"
    DQT_US = "[DQT_US]"
    DYN = "DYN"
    M_E = "[M_E]"
    EV = "EV"
    E = "[E]"
    EQ = "EQ"
    ERG = "ERG"
    FTH_BR = "[FTH_BR]"
    FTH_I = "[FTH_I]"
    FTH_US = "[FTH_US]"
    FDR_BR = "[FDR_BR]"
    FDR_US = "[FDR_US]"
    FOZ_BR = "[FOZ_BR]"
    FOZ_US = "[FOZ_US]"
    FT_BR = "[FT_BR]"
    FT_I = "[FT_I]"
    FT_US = "[FT_US]"
    RD_BR = "[RD_BR]"
    FUR_US = "[FUR_US]"
    GAL_BR = "[GAL_BR]"
    GAL_US = "[GAL_US]"
    GIL_BR = "[GIL_BR]"
    GIL_US = "[GIL_US]"
    GON = "GON"
    GR = "[GR]"
    G_1 = "G%"
    GF = "GF"
    HD_I = "[HD_I]"
    HPF = "[HPF]"
    HR = "HR"
    IN_BR = "[IN_BR]"
    IN_I = "[IN_I]"
    IN_US = "[IN_US]"
    IN_I_HG = "[IN_I'HG]"
    IN_I_H2_O = "[IN_I'H2O]"
    IU = "[IU]"
    KAT = "KAT"
    KN_BR = "[KN_BR]"
    KN_I = "[KN_I]"
    LY = "[LY]"
    LIGNE = "[LIGNE]"
    LNE = "[LNE]"
    LK_BR = "[LK_BR]"
    LK_US = "[LK_US]"
    RLK_US = "[RLK_US]"
    L = "L"
    LCWT_AV = "[LCWT_AV]"
    LTON_AV = "[LTON_AV]"
    LPF = "[LPF]"
    LM = "LM"
    LX = "LX"
    MESH_I = "[MESH_I]"
    MET = "[MET]"
    M_HG = "M[HG]"
    M_H2_O = "M[H2O]"
    MIL_I = "[MIL_I]"
    MIL_US = "[MIL_US]"
    MI_BR = "[MI_BR]"
    MI_US = "[MI_US]"
    MIN_BR = "[MIN_BR]"
    MIN_US = "[MIN_US]"
    VALUE = "'"
    MIN = "MIN"
    MOL = "MOL"
    MO = "MO"
    MO_G = "MO_G"
    MO_J = "MO_J"
    MO_S = "MO_S"
    NMI_BR = "[NMI_BR]"
    NMI_I = "[NMI_I]"
    NEP = "NEP"
    OSM = "OSM"
    OZ_AP = "[OZ_AP]"
    OZ_AV = "[OZ_AV]"
    OZ_TR = "[OZ_TR]"
    PH = "[PH]"
    PC_BR = "[PC_BR]"
    PRS = "PRS"
    PPB = "[PPB]"
    PPM = "[PPM]"
    PPTH = "[PPTH]"
    PPTR = "[PPTR]"
    BU_BR = "[BU_BR]"
    PK_US = "[PK_US]"
    PWT_TR = "[PWT_TR]"
    VALUE_1 = "%"
    PRU = "[PRU]"
    MU_0 = "[MU_0]"
    EPS_0 = "[EPS_0]"
    PHT = "PHT"
    PCA = "[PCA]"
    PIED = "[PIED]"
    PT_BR = "[PT_BR]"
    PT_US = "[PT_US]"
    PNT = "[PNT]"
    POUCE = "[POUCE]"
    LB_AP = "[LB_AP]"
    LB_AV = "[LB_AV]"
    LB_TR = "[LB_TR]"
    LBF_AV = "[LBF_AV]"
    M_P = "[M_P]"
    PSI = "[PSI]"
    QT_BR = "[QT_BR]"
    QT_US = "[QT_US]"
    RAD = "[RAD]"
    REM = "[REM]"
    RD_US = "[RD_US]"
    SC_AP = "[SC_AP]"
    VALUE_2 = "''"
    SCT = "[SCT]"
    SCWT_AV = "[SCWT_AV]"
    STON_AV = "[STON_AV]"
    SPH = "SPH"
    SFT_I = "[SFT_I]"
    SIN_I = "[SIN_I]"
    SMI_US = "[SMI_US]"
    SRD_US = "[SRD_US]"
    SYD_I = "[SYD_I]"
    MI_I = "[MI_I]"
    STR_VALUE = "STR"
    SB = "SB"
    STONE_AV = "[STONE_AV]"
    SR = "SR"
    TBS_US = "[TBS_US]"
    TSP_US = "[TSP_US]"
    VALUE_10 = "10*"
    PI = "[PI]"
    TNE = "TNE"
    TWP = "[TWP]"
    TB_U = "[TB'U]"
    AMU = "AMU"
    C = "[C]"
    WK = "WK"
    GAL_WI = "[GAL_WI]"
    YD_BR = "[YD_BR]"
    YD_I = "[YD_I]"
    YD_US = "[YD_US]"
    ANN = "ANN"
    ANN_G = "ANN_G"
    ANN_J = "ANN_J"
    ANN_T = "ANN_T"


class UnitOfMeasureAtomSens(Enum):
    """
    abstDomain: A12848 (C-0-T12839-A12848-cpt)
    :cvar APL_U:
    :cvar A:
    :cvar AO:
    :cvar BQ:
    :cvar BETH_U:
    :cvar BI:
    :cvar BDSK_U:
    :cvar K:
    :cvar BTU_39:
    :cvar BTU_59:
    :cvar BTU_60:
    :cvar BTU_IT:
    :cvar BTU_M:
    :cvar BTU_TH:
    :cvar BTU:
    :cvar CAL:
    :cvar CH:
    :cvar CI:
    :cvar DYE_U:
    :cvar F:
    :cvar GPL_U:
    :cvar GAL:
    :cvar G:
    :cvar GB:
    :cvar GY:
    :cvar H:
    :cvar HZ:
    :cvar HNSF_U:
    :cvar J:
    :cvar KY:
    :cvar KA_U:
    :cvar KNK_U:
    :cvar LMB:
    :cvar MPL_U:
    :cvar MCLG_U:
    :cvar MX:
    :cvar N:
    :cvar G_1:
    :cvar OE:
    :cvar OHM:
    :cvar PA:
    :cvar H_1:
    :cvar P:
    :cvar PCA_PR:
    :cvar PNT_PR:
    :cvar R:
    :cvar S:
    :cvar SV:
    :cvar SMGY_U:
    :cvar ST:
    :cvar S_1:
    :cvar T:
    :cvar TODD_U:
    :cvar U:
    :cvar USP_U:
    :cvar V:
    :cvar W:
    :cvar WB:
    :cvar G_2:
    :cvar ACR_BR:
    :cvar ACR_US:
    :cvar ARB_U:
    :cvar AR:
    :cvar AU:
    :cvar ATM:
    :cvar ATT:
    :cvar BAR:
    :cvar B:
    :cvar BBL_US:
    :cvar BD:
    :cvar B_1:
    :cvar B_K_W:
    :cvar B_U_V:
    :cvar B_M_V:
    :cvar B_SPL:
    :cvar B_V:
    :cvar B_W:
    :cvar BIT:
    :cvar BIT_S:
    :cvar BF_I:
    :cvar BU_US:
    :cvar PK_BR:
    :cvar BY:
    :cvar CAL_15:
    :cvar CAL_20:
    :cvar CAL_IT:
    :cvar CAL_M:
    :cvar CAL_TH:
    :cvar CAL_1:
    :cvar CAR_M:
    :cvar CAR_AU:
    :cvar CH_BR:
    :cvar CH_US:
    :cvar RCH_US:
    :cvar CICERO:
    :cvar CIRC:
    :cvar CML_I:
    :cvar CR_I:
    :cvar CRD_US:
    :cvar CFT_I:
    :cvar CIN_I:
    :cvar CYD_I:
    :cvar CUP_US:
    :cvar D:
    :cvar DEG:
    :cvar CEL:
    :cvar DEG_F:
    :cvar DIDOT:
    :cvar DIOP:
    :cvar DR_AV:
    :cvar DR_AP:
    :cvar DRP:
    :cvar DPT_US:
    :cvar DQT_US:
    :cvar DYN:
    :cvar M_E:
    :cvar E_V:
    :cvar E:
    :cvar EQ:
    :cvar ERG:
    :cvar FTH_BR:
    :cvar FTH_I:
    :cvar FTH_US:
    :cvar FDR_BR:
    :cvar FDR_US:
    :cvar FOZ_BR:
    :cvar FOZ_US:
    :cvar FT_BR:
    :cvar FT_I:
    :cvar FT_US:
    :cvar RD_BR:
    :cvar FUR_US:
    :cvar GAL_BR:
    :cvar GAL_US:
    :cvar GIL_BR:
    :cvar GIL_US:
    :cvar GON:
    :cvar GR:
    :cvar G_3:
    :cvar GF:
    :cvar HD_I:
    :cvar HPF:
    :cvar H_2:
    :cvar IN_BR:
    :cvar IN_I:
    :cvar IN_US:
    :cvar IN_I_HG:
    :cvar IN_I_H2_O:
    :cvar I_U:
    :cvar KAT:
    :cvar KN_BR:
    :cvar KN_I:
    :cvar LY:
    :cvar LIGNE:
    :cvar LNE:
    :cvar LK_BR:
    :cvar LK_US:
    :cvar RLK_US:
    :cvar L:
    :cvar LCWT_AV:
    :cvar LTON_AV:
    :cvar LPF:
    :cvar LM:
    :cvar LX:
    :cvar MESH_I:
    :cvar MET:
    :cvar M_HG:
    :cvar M_H2_O:
    :cvar MIL_I:
    :cvar MIL_US:
    :cvar MI_BR:
    :cvar MI_US:
    :cvar MIN_BR:
    :cvar MIN_US:
    :cvar VALUE:
    :cvar MIN:
    :cvar MOL:
    :cvar MO:
    :cvar MO_G:
    :cvar MO_J:
    :cvar MO_S:
    :cvar NMI_BR:
    :cvar NMI_I:
    :cvar NP:
    :cvar OSM:
    :cvar OZ_AP:
    :cvar OZ_AV:
    :cvar OZ_TR:
    :cvar P_H:
    :cvar PC_BR:
    :cvar PC:
    :cvar PPB:
    :cvar PPM:
    :cvar PPTH:
    :cvar PPTR:
    :cvar BU_BR:
    :cvar PK_US:
    :cvar PWT_TR:
    :cvar VALUE_1:
    :cvar PRU:
    :cvar MU_0:
    :cvar EPS_0:
    :cvar PH_1:
    :cvar PCA:
    :cvar PIED:
    :cvar PT_BR:
    :cvar PT_US:
    :cvar PNT:
    :cvar POUCE:
    :cvar LB_AP:
    :cvar LB_AV:
    :cvar LB_TR:
    :cvar LBF_AV:
    :cvar M_P:
    :cvar PSI:
    :cvar QT_BR:
    :cvar QT_US:
    :cvar RAD:
    :cvar REM:
    :cvar RD_US:
    :cvar SC_AP:
    :cvar VALUE_2:
    :cvar SCT:
    :cvar SCWT_AV:
    :cvar STON_AV:
    :cvar SPH:
    :cvar SFT_I:
    :cvar SIN_I:
    :cvar SMI_US:
    :cvar SRD_US:
    :cvar SYD_I:
    :cvar MI_I:
    :cvar ST_1:
    :cvar SB:
    :cvar STONE_AV:
    :cvar SR:
    :cvar TBS_US:
    :cvar TSP_US:
    :cvar VALUE_10:
    :cvar PI:
    :cvar T_1:
    :cvar TWP:
    :cvar TB_U:
    :cvar U_1:
    :cvar C:
    :cvar WK:
    :cvar GAL_WI:
    :cvar YD_BR:
    :cvar YD_I:
    :cvar YD_US:
    :cvar A_1:
    :cvar A_G:
    :cvar A_J:
    :cvar A_T:
    """
    APL_U = "[APL'U]"
    A = "A"
    AO = "Ao"
    BQ = "Bq"
    BETH_U = "[beth'U]"
    BI = "Bi"
    BDSK_U = "[bdsk'U]"
    K = "[k]"
    BTU_39 = "[Btu_39]"
    BTU_59 = "[Btu_59]"
    BTU_60 = "[Btu_60]"
    BTU_IT = "[Btu_IT]"
    BTU_M = "[Btu_m]"
    BTU_TH = "[Btu_th]"
    BTU = "[Btu]"
    CAL = "[Cal]"
    CH = "[Ch]"
    CI = "Ci"
    DYE_U = "[dye'U]"
    F = "F"
    GPL_U = "[GPL'U]"
    GAL = "Gal"
    G = "G"
    GB = "Gb"
    GY = "Gy"
    H = "H"
    HZ = "Hz"
    HNSF_U = "[hnsf'U]"
    J = "J"
    KY = "Ky"
    KA_U = "[ka'U]"
    KNK_U = "[knk'U]"
    LMB = "Lmb"
    MPL_U = "[MPL'U]"
    MCLG_U = "[mclg'U]"
    MX = "Mx"
    N = "N"
    G_1 = "[G]"
    OE = "Oe"
    OHM = "Ohm"
    PA = "Pa"
    H_1 = "[h]"
    P = "P"
    PCA_PR = "[pca_pr]"
    PNT_PR = "[pnt_pr]"
    R = "R"
    S = "S"
    SV = "Sv"
    SMGY_U = "[smgy'U]"
    ST = "St"
    S_1 = "[S]"
    T = "T"
    TODD_U = "[todd'U]"
    U = "U"
    USP_U = "[USP'U]"
    V = "V"
    W = "W"
    WB = "Wb"
    G_2 = "[g]"
    ACR_BR = "[acr_br]"
    ACR_US = "[acr_us]"
    ARB_U = "[arb'U]"
    AR = "ar"
    AU = "AU"
    ATM = "atm"
    ATT = "att"
    BAR = "bar"
    B = "b"
    BBL_US = "[bbl_us]"
    BD = "Bd"
    B_1 = "B"
    B_K_W = "B[kW]"
    B_U_V = "B[uV]"
    B_M_V = "B[mV]"
    B_SPL = "B[SPL]"
    B_V = "B[V]"
    B_W = "B[W]"
    BIT = "bit"
    BIT_S = "bit_s"
    BF_I = "[bf_i]"
    BU_US = "[bu_us]"
    PK_BR = "[pk_br]"
    BY = "By"
    CAL_15 = "cal_[15]"
    CAL_20 = "cal_[20]"
    CAL_IT = "cal_IT"
    CAL_M = "cal_m"
    CAL_TH = "cal_th"
    CAL_1 = "cal"
    CAR_M = "[car_m]"
    CAR_AU = "[car_Au]"
    CH_BR = "[ch_br]"
    CH_US = "[ch_us]"
    RCH_US = "[rch_us]"
    CICERO = "[cicero]"
    CIRC = "circ"
    CML_I = "[cml_i]"
    CR_I = "[cr_i]"
    CRD_US = "[crd_us]"
    CFT_I = "[cft_i]"
    CIN_I = "[cin_i]"
    CYD_I = "[cyd_i]"
    CUP_US = "[cup_us]"
    D = "d"
    DEG = "deg"
    CEL = "Cel"
    DEG_F = "[degF]"
    DIDOT = "[didot]"
    DIOP = "[diop]"
    DR_AV = "[dr_av]"
    DR_AP = "[dr_ap]"
    DRP = "[drp]"
    DPT_US = "[dpt_us]"
    DQT_US = "[dqt_us]"
    DYN = "dyn"
    M_E = "[m_e]"
    E_V = "eV"
    E = "[e]"
    EQ = "eq"
    ERG = "erg"
    FTH_BR = "[fth_br]"
    FTH_I = "[fth_i]"
    FTH_US = "[fth_us]"
    FDR_BR = "[fdr_br]"
    FDR_US = "[fdr_us]"
    FOZ_BR = "[foz_br]"
    FOZ_US = "[foz_us]"
    FT_BR = "[ft_br]"
    FT_I = "[ft_i]"
    FT_US = "[ft_us]"
    RD_BR = "[rd_br]"
    FUR_US = "[fur_us]"
    GAL_BR = "[gal_br]"
    GAL_US = "[gal_us]"
    GIL_BR = "[gil_br]"
    GIL_US = "[gil_us]"
    GON = "gon"
    GR = "[gr]"
    G_3 = "g%"
    GF = "gf"
    HD_I = "[hd_i]"
    HPF = "[HPF]"
    H_2 = "h"
    IN_BR = "[in_br]"
    IN_I = "[in_i]"
    IN_US = "[in_us]"
    IN_I_HG = "[in_i'Hg]"
    IN_I_H2_O = "[in_i'H2O]"
    I_U = "[iU]"
    KAT = "kat"
    KN_BR = "[kn_br]"
    KN_I = "[kn_i]"
    LY = "[ly]"
    LIGNE = "[ligne]"
    LNE = "[lne]"
    LK_BR = "[lk_br]"
    LK_US = "[lk_us]"
    RLK_US = "[rlk_us]"
    L = "l"
    LCWT_AV = "[lcwt_av]"
    LTON_AV = "[lton_av]"
    LPF = "[LPF]"
    LM = "lm"
    LX = "lx"
    MESH_I = "[mesh_i]"
    MET = "[MET]"
    M_HG = "m[Hg]"
    M_H2_O = "m[H2O]"
    MIL_I = "[mil_i]"
    MIL_US = "[mil_us]"
    MI_BR = "[mi_br]"
    MI_US = "[mi_us]"
    MIN_BR = "[min_br]"
    MIN_US = "[min_us]"
    VALUE = "'"
    MIN = "min"
    MOL = "mol"
    MO = "mo"
    MO_G = "mo_g"
    MO_J = "mo_j"
    MO_S = "mo_s"
    NMI_BR = "[nmi_br]"
    NMI_I = "[nmi_i]"
    NP = "Np"
    OSM = "osm"
    OZ_AP = "[oz_ap]"
    OZ_AV = "[oz_av]"
    OZ_TR = "[oz_tr]"
    P_H = "[pH]"
    PC_BR = "[pc_br]"
    PC = "pc"
    PPB = "[ppb]"
    PPM = "[ppm]"
    PPTH = "[ppth]"
    PPTR = "[pptr]"
    BU_BR = "[bu_br]"
    PK_US = "[pk_us]"
    PWT_TR = "[pwt_tr]"
    VALUE_1 = "%"
    PRU = "[PRU]"
    MU_0 = "[mu_0]"
    EPS_0 = "[eps_0]"
    PH_1 = "ph"
    PCA = "[pca]"
    PIED = "[pied]"
    PT_BR = "[pt_br]"
    PT_US = "[pt_us]"
    PNT = "[pnt]"
    POUCE = "[pouce]"
    LB_AP = "[lb_ap]"
    LB_AV = "[lb_av]"
    LB_TR = "[lb_tr]"
    LBF_AV = "[lbf_av]"
    M_P = "[m_p]"
    PSI = "[psi]"
    QT_BR = "[qt_br]"
    QT_US = "[qt_us]"
    RAD = "RAD"
    REM = "REM"
    RD_US = "[rd_us]"
    SC_AP = "[sc_ap]"
    VALUE_2 = "''"
    SCT = "[sct]"
    SCWT_AV = "[scwt_av]"
    STON_AV = "[ston_av]"
    SPH = "sph"
    SFT_I = "[sft_i]"
    SIN_I = "[sin_i]"
    SMI_US = "[smi_us]"
    SRD_US = "[srd_us]"
    SYD_I = "[syd_i]"
    MI_I = "[mi_i]"
    ST_1 = "st"
    SB = "sb"
    STONE_AV = "[stone_av]"
    SR = "sr"
    TBS_US = "[tbs_us]"
    TSP_US = "[tsp_us]"
    VALUE_10 = "10*"
    PI = "[pi]"
    T_1 = "t"
    TWP = "[twp]"
    TB_U = "[tb'U]"
    U_1 = "u"
    C = "[c]"
    WK = "wk"
    GAL_WI = "[gal_wi]"
    YD_BR = "[yd_br]"
    YD_I = "[yd_i]"
    YD_US = "[yd_us]"
    A_1 = "a"
    A_G = "a_g"
    A_J = "a_j"
    A_T = "a_t"


class UnitOfMeasurePrefixInsens(Enum):
    """
    abstDomain: A12814 (C-0-T12549-A12814-cpt)
    :cvar A:
    :cvar C:
    :cvar D:
    :cvar DA:
    :cvar EX:
    :cvar F:
    :cvar GIB:
    :cvar GA:
    :cvar H:
    :cvar KIB:
    :cvar K:
    :cvar MIB:
    :cvar MA:
    :cvar U:
    :cvar M:
    :cvar N:
    :cvar PT:
    :cvar P:
    :cvar TIB:
    :cvar TR:
    :cvar YO:
    :cvar YA:
    :cvar ZO:
    :cvar ZA:
    """
    A = "A"
    C = "C"
    D = "D"
    DA = "DA"
    EX = "EX"
    F = "F"
    GIB = "GIB"
    GA = "GA"
    H = "H"
    KIB = "KIB"
    K = "K"
    MIB = "MIB"
    MA = "MA"
    U = "U"
    M = "M"
    N = "N"
    PT = "PT"
    P = "P"
    TIB = "TIB"
    TR = "TR"
    YO = "YO"
    YA = "YA"
    ZO = "ZO"
    ZA = "ZA"


class UnitOfMeasurePrefixSens(Enum):
    """
    abstDomain: A13104 (C-0-T12839-A13104-cpt)
    :cvar A:
    :cvar C:
    :cvar D:
    :cvar DA:
    :cvar E:
    :cvar F:
    :cvar GI:
    :cvar G:
    :cvar H:
    :cvar KI:
    :cvar K:
    :cvar MI:
    :cvar M:
    :cvar U:
    :cvar M_1:
    :cvar N:
    :cvar P:
    :cvar P_1:
    :cvar TI:
    :cvar T:
    :cvar Y:
    :cvar Y_1:
    :cvar Z:
    :cvar Z_1:
    """
    A = "a"
    C = "c"
    D = "d"
    DA = "da"
    E = "E"
    F = "f"
    GI = "Gi"
    G = "G"
    H = "h"
    KI = "Ki"
    K = "k"
    MI = "Mi"
    M = "M"
    U = "u"
    M_1 = "m"
    N = "n"
    P = "P"
    P_1 = "p"
    TI = "Ti"
    T = "T"
    Y = "y"
    Y_1 = "Y"
    Z = "z"
    Z_1 = "Z"


class UnitsOfMeasureCaseInsensitive(Enum):
    """
    vocSet: T12549 (C-0-T12549-cpt)
    :cvar C:
    :cvar K:
    :cvar CD:
    :cvar G:
    :cvar M:
    :cvar RAD:
    :cvar S:
    :cvar APL_U:
    :cvar A:
    :cvar AO:
    :cvar BQ:
    :cvar BETH_U:
    :cvar BI:
    :cvar BDSK_U:
    :cvar K_1:
    :cvar BTU_39:
    :cvar BTU_59:
    :cvar BTU_60:
    :cvar BTU_IT:
    :cvar BTU_M:
    :cvar BTU_TH:
    :cvar BTU:
    :cvar CAL:
    :cvar CH:
    :cvar CI:
    :cvar DYE_U:
    :cvar F:
    :cvar GPL_U:
    :cvar GL:
    :cvar GS:
    :cvar GB:
    :cvar GY:
    :cvar H:
    :cvar HZ:
    :cvar HNSF_U:
    :cvar J:
    :cvar KY:
    :cvar KA_U:
    :cvar KNK_U:
    :cvar LMB:
    :cvar MPL_U:
    :cvar MCLG_U:
    :cvar MX:
    :cvar N:
    :cvar GC:
    :cvar OE:
    :cvar OHM:
    :cvar PAL:
    :cvar H_1:
    :cvar P:
    :cvar PCA_PR:
    :cvar PNT_PR:
    :cvar ROE:
    :cvar SIE:
    :cvar SV:
    :cvar SMGY_U:
    :cvar ST:
    :cvar S_1:
    :cvar T:
    :cvar TODD_U:
    :cvar U:
    :cvar USP_U:
    :cvar V:
    :cvar W:
    :cvar WB:
    :cvar G_1:
    :cvar ACR_BR:
    :cvar ACR_US:
    :cvar ARB_U:
    :cvar AR:
    :cvar ASU:
    :cvar ATM:
    :cvar ATT:
    :cvar BAR:
    :cvar BRN:
    :cvar BBL_US:
    :cvar BD:
    :cvar B:
    :cvar B_KW:
    :cvar B_UV:
    :cvar B_MV:
    :cvar B_SPL:
    :cvar B_V:
    :cvar B_W:
    :cvar BIT:
    :cvar BIT_S:
    :cvar BF_I:
    :cvar BU_US:
    :cvar PK_BR:
    :cvar BY:
    :cvar CAL_15:
    :cvar CAL_20:
    :cvar CAL_IT:
    :cvar CAL_M:
    :cvar CAL_TH:
    :cvar CAL_1:
    :cvar CAR_M:
    :cvar CAR_AU:
    :cvar CH_BR:
    :cvar CH_US:
    :cvar RCH_US:
    :cvar CICERO:
    :cvar CIRC:
    :cvar CML_I:
    :cvar CR_I:
    :cvar CRD_US:
    :cvar CFT_I:
    :cvar CIN_I:
    :cvar CYD_I:
    :cvar CUP_US:
    :cvar D:
    :cvar DEG:
    :cvar CEL:
    :cvar DEGF:
    :cvar DIDOT:
    :cvar DIOP:
    :cvar DR_AV:
    :cvar DR_AP:
    :cvar DRP:
    :cvar DPT_US:
    :cvar DQT_US:
    :cvar DYN:
    :cvar M_E:
    :cvar EV:
    :cvar E:
    :cvar EQ:
    :cvar ERG:
    :cvar FTH_BR:
    :cvar FTH_I:
    :cvar FTH_US:
    :cvar FDR_BR:
    :cvar FDR_US:
    :cvar FOZ_BR:
    :cvar FOZ_US:
    :cvar FT_BR:
    :cvar FT_I:
    :cvar FT_US:
    :cvar RD_BR:
    :cvar FUR_US:
    :cvar GAL_BR:
    :cvar GAL_US:
    :cvar GIL_BR:
    :cvar GIL_US:
    :cvar GON:
    :cvar GR:
    :cvar G_2:
    :cvar GF:
    :cvar HD_I:
    :cvar HPF:
    :cvar HR:
    :cvar IN_BR:
    :cvar IN_I:
    :cvar IN_US:
    :cvar IN_I_HG:
    :cvar IN_I_H2_O:
    :cvar IU:
    :cvar KAT:
    :cvar KN_BR:
    :cvar KN_I:
    :cvar LY:
    :cvar LIGNE:
    :cvar LNE:
    :cvar LK_BR:
    :cvar LK_US:
    :cvar RLK_US:
    :cvar L:
    :cvar LCWT_AV:
    :cvar LTON_AV:
    :cvar LPF:
    :cvar LM:
    :cvar LX:
    :cvar MESH_I:
    :cvar MET:
    :cvar M_HG:
    :cvar M_H2_O:
    :cvar MIL_I:
    :cvar MIL_US:
    :cvar MI_BR:
    :cvar MI_US:
    :cvar MIN_BR:
    :cvar MIN_US:
    :cvar VALUE:
    :cvar MIN:
    :cvar MOL:
    :cvar MO:
    :cvar MO_G:
    :cvar MO_J:
    :cvar MO_S:
    :cvar NMI_BR:
    :cvar NMI_I:
    :cvar NEP:
    :cvar OSM:
    :cvar OZ_AP:
    :cvar OZ_AV:
    :cvar OZ_TR:
    :cvar PH:
    :cvar PC_BR:
    :cvar PRS:
    :cvar PPB:
    :cvar PPM:
    :cvar PPTH:
    :cvar PPTR:
    :cvar BU_BR:
    :cvar PK_US:
    :cvar PWT_TR:
    :cvar VALUE_1:
    :cvar PRU:
    :cvar MU_0:
    :cvar EPS_0:
    :cvar PHT:
    :cvar PCA:
    :cvar PIED:
    :cvar PT_BR:
    :cvar PT_US:
    :cvar PNT:
    :cvar POUCE:
    :cvar LB_AP:
    :cvar LB_AV:
    :cvar LB_TR:
    :cvar LBF_AV:
    :cvar M_P:
    :cvar PSI:
    :cvar QT_BR:
    :cvar QT_US:
    :cvar RAD_1:
    :cvar REM:
    :cvar RD_US:
    :cvar SC_AP:
    :cvar VALUE_2:
    :cvar SCT:
    :cvar SCWT_AV:
    :cvar STON_AV:
    :cvar SPH:
    :cvar SFT_I:
    :cvar SIN_I:
    :cvar SMI_US:
    :cvar SRD_US:
    :cvar SYD_I:
    :cvar MI_I:
    :cvar STR_VALUE:
    :cvar SB:
    :cvar STONE_AV:
    :cvar SR:
    :cvar TBS_US:
    :cvar TSP_US:
    :cvar VALUE_10:
    :cvar PI:
    :cvar TNE:
    :cvar TWP:
    :cvar TB_U:
    :cvar AMU:
    :cvar C_1:
    :cvar WK:
    :cvar GAL_WI:
    :cvar YD_BR:
    :cvar YD_I:
    :cvar YD_US:
    :cvar ANN:
    :cvar ANN_G:
    :cvar ANN_J:
    :cvar ANN_T:
    :cvar DA:
    :cvar EX:
    :cvar GIB:
    :cvar GA:
    :cvar KIB:
    :cvar MIB:
    :cvar MA:
    :cvar PT:
    :cvar TIB:
    :cvar TR:
    :cvar YO:
    :cvar YA:
    :cvar ZO:
    :cvar ZA:
    """
    C = "C"
    K = "K"
    CD = "CD"
    G = "G"
    M = "M"
    RAD = "RAD"
    S = "S"
    APL_U = "[APL'U]"
    A = "A"
    AO = "AO"
    BQ = "BQ"
    BETH_U = "[BETH'U]"
    BI = "BI"
    BDSK_U = "[BDSK'U]"
    K_1 = "[K]"
    BTU_39 = "[BTU_39]"
    BTU_59 = "[BTU_59]"
    BTU_60 = "[BTU_60]"
    BTU_IT = "[BTU_IT]"
    BTU_M = "[BTU_M]"
    BTU_TH = "[BTU_TH]"
    BTU = "[BTU]"
    CAL = "[CAL]"
    CH = "[CH]"
    CI = "CI"
    DYE_U = "[DYE'U]"
    F = "F"
    GPL_U = "[GPL'U]"
    GL = "GL"
    GS = "GS"
    GB = "GB"
    GY = "GY"
    H = "H"
    HZ = "HZ"
    HNSF_U = "[HNSF'U]"
    J = "J"
    KY = "KY"
    KA_U = "[KA'U]"
    KNK_U = "[KNK'U]"
    LMB = "LMB"
    MPL_U = "[MPL'U]"
    MCLG_U = "[MCLG'U]"
    MX = "MX"
    N = "N"
    GC = "[GC]"
    OE = "OE"
    OHM = "OHM"
    PAL = "PAL"
    H_1 = "[H]"
    P = "P"
    PCA_PR = "[PCA_PR]"
    PNT_PR = "[PNT_PR]"
    ROE = "ROE"
    SIE = "SIE"
    SV = "SV"
    SMGY_U = "[SMGY'U]"
    ST = "ST"
    S_1 = "[S]"
    T = "T"
    TODD_U = "[TODD'U]"
    U = "U"
    USP_U = "[USP'U]"
    V = "V"
    W = "W"
    WB = "WB"
    G_1 = "[G]"
    ACR_BR = "[ACR_BR]"
    ACR_US = "[ACR_US]"
    ARB_U = "[ARB'U]"
    AR = "AR"
    ASU = "ASU"
    ATM = "ATM"
    ATT = "ATT"
    BAR = "BAR"
    BRN = "BRN"
    BBL_US = "[BBL_US]"
    BD = "BD"
    B = "B"
    B_KW = "B[KW]"
    B_UV = "B[UV]"
    B_MV = "B[MV]"
    B_SPL = "B[SPL]"
    B_V = "B[V]"
    B_W = "B[W]"
    BIT = "BIT"
    BIT_S = "BIT_S"
    BF_I = "[BF_I]"
    BU_US = "[BU_US]"
    PK_BR = "[PK_BR]"
    BY = "BY"
    CAL_15 = "CAL_[15]"
    CAL_20 = "CAL_[20]"
    CAL_IT = "CAL_IT"
    CAL_M = "CAL_M"
    CAL_TH = "CAL_TH"
    CAL_1 = "CAL"
    CAR_M = "[CAR_M]"
    CAR_AU = "[CAR_AU]"
    CH_BR = "[CH_BR]"
    CH_US = "[CH_US]"
    RCH_US = "[RCH_US]"
    CICERO = "[CICERO]"
    CIRC = "CIRC"
    CML_I = "[CML_I]"
    CR_I = "[CR_I]"
    CRD_US = "[CRD_US]"
    CFT_I = "[CFT_I]"
    CIN_I = "[CIN_I]"
    CYD_I = "[CYD_I]"
    CUP_US = "[CUP_US]"
    D = "D"
    DEG = "DEG"
    CEL = "CEL"
    DEGF = "[DEGF]"
    DIDOT = "[DIDOT]"
    DIOP = "[DIOP]"
    DR_AV = "[DR_AV]"
    DR_AP = "[DR_AP]"
    DRP = "[DRP]"
    DPT_US = "[DPT_US]"
    DQT_US = "[DQT_US]"
    DYN = "DYN"
    M_E = "[M_E]"
    EV = "EV"
    E = "[E]"
    EQ = "EQ"
    ERG = "ERG"
    FTH_BR = "[FTH_BR]"
    FTH_I = "[FTH_I]"
    FTH_US = "[FTH_US]"
    FDR_BR = "[FDR_BR]"
    FDR_US = "[FDR_US]"
    FOZ_BR = "[FOZ_BR]"
    FOZ_US = "[FOZ_US]"
    FT_BR = "[FT_BR]"
    FT_I = "[FT_I]"
    FT_US = "[FT_US]"
    RD_BR = "[RD_BR]"
    FUR_US = "[FUR_US]"
    GAL_BR = "[GAL_BR]"
    GAL_US = "[GAL_US]"
    GIL_BR = "[GIL_BR]"
    GIL_US = "[GIL_US]"
    GON = "GON"
    GR = "[GR]"
    G_2 = "G%"
    GF = "GF"
    HD_I = "[HD_I]"
    HPF = "[HPF]"
    HR = "HR"
    IN_BR = "[IN_BR]"
    IN_I = "[IN_I]"
    IN_US = "[IN_US]"
    IN_I_HG = "[IN_I'HG]"
    IN_I_H2_O = "[IN_I'H2O]"
    IU = "[IU]"
    KAT = "KAT"
    KN_BR = "[KN_BR]"
    KN_I = "[KN_I]"
    LY = "[LY]"
    LIGNE = "[LIGNE]"
    LNE = "[LNE]"
    LK_BR = "[LK_BR]"
    LK_US = "[LK_US]"
    RLK_US = "[RLK_US]"
    L = "L"
    LCWT_AV = "[LCWT_AV]"
    LTON_AV = "[LTON_AV]"
    LPF = "[LPF]"
    LM = "LM"
    LX = "LX"
    MESH_I = "[MESH_I]"
    MET = "[MET]"
    M_HG = "M[HG]"
    M_H2_O = "M[H2O]"
    MIL_I = "[MIL_I]"
    MIL_US = "[MIL_US]"
    MI_BR = "[MI_BR]"
    MI_US = "[MI_US]"
    MIN_BR = "[MIN_BR]"
    MIN_US = "[MIN_US]"
    VALUE = "'"
    MIN = "MIN"
    MOL = "MOL"
    MO = "MO"
    MO_G = "MO_G"
    MO_J = "MO_J"
    MO_S = "MO_S"
    NMI_BR = "[NMI_BR]"
    NMI_I = "[NMI_I]"
    NEP = "NEP"
    OSM = "OSM"
    OZ_AP = "[OZ_AP]"
    OZ_AV = "[OZ_AV]"
    OZ_TR = "[OZ_TR]"
    PH = "[PH]"
    PC_BR = "[PC_BR]"
    PRS = "PRS"
    PPB = "[PPB]"
    PPM = "[PPM]"
    PPTH = "[PPTH]"
    PPTR = "[PPTR]"
    BU_BR = "[BU_BR]"
    PK_US = "[PK_US]"
    PWT_TR = "[PWT_TR]"
    VALUE_1 = "%"
    PRU = "[PRU]"
    MU_0 = "[MU_0]"
    EPS_0 = "[EPS_0]"
    PHT = "PHT"
    PCA = "[PCA]"
    PIED = "[PIED]"
    PT_BR = "[PT_BR]"
    PT_US = "[PT_US]"
    PNT = "[PNT]"
    POUCE = "[POUCE]"
    LB_AP = "[LB_AP]"
    LB_AV = "[LB_AV]"
    LB_TR = "[LB_TR]"
    LBF_AV = "[LBF_AV]"
    M_P = "[M_P]"
    PSI = "[PSI]"
    QT_BR = "[QT_BR]"
    QT_US = "[QT_US]"
    RAD_1 = "[RAD]"
    REM = "[REM]"
    RD_US = "[RD_US]"
    SC_AP = "[SC_AP]"
    VALUE_2 = "''"
    SCT = "[SCT]"
    SCWT_AV = "[SCWT_AV]"
    STON_AV = "[STON_AV]"
    SPH = "SPH"
    SFT_I = "[SFT_I]"
    SIN_I = "[SIN_I]"
    SMI_US = "[SMI_US]"
    SRD_US = "[SRD_US]"
    SYD_I = "[SYD_I]"
    MI_I = "[MI_I]"
    STR_VALUE = "STR"
    SB = "SB"
    STONE_AV = "[STONE_AV]"
    SR = "SR"
    TBS_US = "[TBS_US]"
    TSP_US = "[TSP_US]"
    VALUE_10 = "10*"
    PI = "[PI]"
    TNE = "TNE"
    TWP = "[TWP]"
    TB_U = "[TB'U]"
    AMU = "AMU"
    C_1 = "[C]"
    WK = "WK"
    GAL_WI = "[GAL_WI]"
    YD_BR = "[YD_BR]"
    YD_I = "[YD_I]"
    YD_US = "[YD_US]"
    ANN = "ANN"
    ANN_G = "ANN_G"
    ANN_J = "ANN_J"
    ANN_T = "ANN_T"
    DA = "DA"
    EX = "EX"
    GIB = "GIB"
    GA = "GA"
    KIB = "KIB"
    MIB = "MIB"
    MA = "MA"
    PT = "PT"
    TIB = "TIB"
    TR = "TR"
    YO = "YO"
    YA = "YA"
    ZO = "ZO"
    ZA = "ZA"


class UnitsOfMeasureCaseSensitive(Enum):
    """
    vocSet: T12839 (C-0-T12839-cpt)
    :cvar C:
    :cvar K:
    :cvar CD:
    :cvar G:
    :cvar M:
    :cvar RAD:
    :cvar S:
    :cvar APL_U:
    :cvar A:
    :cvar AO:
    :cvar BQ:
    :cvar BETH_U:
    :cvar BI:
    :cvar BDSK_U:
    :cvar K_1:
    :cvar BTU_39:
    :cvar BTU_59:
    :cvar BTU_60:
    :cvar BTU_IT:
    :cvar BTU_M:
    :cvar BTU_TH:
    :cvar BTU:
    :cvar CAL:
    :cvar CH:
    :cvar CI:
    :cvar DYE_U:
    :cvar F:
    :cvar GPL_U:
    :cvar GAL:
    :cvar G_1:
    :cvar GB:
    :cvar GY:
    :cvar H:
    :cvar HZ:
    :cvar HNSF_U:
    :cvar J:
    :cvar KY:
    :cvar KA_U:
    :cvar KNK_U:
    :cvar LMB:
    :cvar MPL_U:
    :cvar MCLG_U:
    :cvar MX:
    :cvar N:
    :cvar G_2:
    :cvar OE:
    :cvar OHM:
    :cvar PA:
    :cvar H_1:
    :cvar P:
    :cvar PCA_PR:
    :cvar PNT_PR:
    :cvar R:
    :cvar S_1:
    :cvar SV:
    :cvar SMGY_U:
    :cvar ST:
    :cvar S_2:
    :cvar T:
    :cvar TODD_U:
    :cvar U:
    :cvar USP_U:
    :cvar V:
    :cvar W:
    :cvar WB:
    :cvar G_3:
    :cvar ACR_BR:
    :cvar ACR_US:
    :cvar ARB_U:
    :cvar AR:
    :cvar AU:
    :cvar ATM:
    :cvar ATT:
    :cvar BAR:
    :cvar B:
    :cvar BBL_US:
    :cvar BD:
    :cvar B_1:
    :cvar B_K_W:
    :cvar B_U_V:
    :cvar B_M_V:
    :cvar B_SPL:
    :cvar B_V:
    :cvar B_W:
    :cvar BIT:
    :cvar BIT_S:
    :cvar BF_I:
    :cvar BU_US:
    :cvar PK_BR:
    :cvar BY:
    :cvar CAL_15:
    :cvar CAL_20:
    :cvar CAL_IT:
    :cvar CAL_M:
    :cvar CAL_TH:
    :cvar CAL_1:
    :cvar CAR_M:
    :cvar CAR_AU:
    :cvar CH_BR:
    :cvar CH_US:
    :cvar RCH_US:
    :cvar CICERO:
    :cvar CIRC:
    :cvar CML_I:
    :cvar CR_I:
    :cvar CRD_US:
    :cvar CFT_I:
    :cvar CIN_I:
    :cvar CYD_I:
    :cvar CUP_US:
    :cvar D:
    :cvar DEG:
    :cvar CEL:
    :cvar DEG_F:
    :cvar DIDOT:
    :cvar DIOP:
    :cvar DR_AV:
    :cvar DR_AP:
    :cvar DRP:
    :cvar DPT_US:
    :cvar DQT_US:
    :cvar DYN:
    :cvar M_E:
    :cvar E_V:
    :cvar E:
    :cvar EQ:
    :cvar ERG:
    :cvar FTH_BR:
    :cvar FTH_I:
    :cvar FTH_US:
    :cvar FDR_BR:
    :cvar FDR_US:
    :cvar FOZ_BR:
    :cvar FOZ_US:
    :cvar FT_BR:
    :cvar FT_I:
    :cvar FT_US:
    :cvar RD_BR:
    :cvar FUR_US:
    :cvar GAL_BR:
    :cvar GAL_US:
    :cvar GIL_BR:
    :cvar GIL_US:
    :cvar GON:
    :cvar GR:
    :cvar G_4:
    :cvar GF:
    :cvar HD_I:
    :cvar HPF:
    :cvar H_2:
    :cvar IN_BR:
    :cvar IN_I:
    :cvar IN_US:
    :cvar IN_I_HG:
    :cvar IN_I_H2_O:
    :cvar I_U:
    :cvar KAT:
    :cvar KN_BR:
    :cvar KN_I:
    :cvar LY:
    :cvar LIGNE:
    :cvar LNE:
    :cvar LK_BR:
    :cvar LK_US:
    :cvar RLK_US:
    :cvar L:
    :cvar LCWT_AV:
    :cvar LTON_AV:
    :cvar LPF:
    :cvar LM:
    :cvar LX:
    :cvar MESH_I:
    :cvar MET:
    :cvar M_HG:
    :cvar M_H2_O:
    :cvar MIL_I:
    :cvar MIL_US:
    :cvar MI_BR:
    :cvar MI_US:
    :cvar MIN_BR:
    :cvar MIN_US:
    :cvar VALUE:
    :cvar MIN:
    :cvar MOL:
    :cvar MO:
    :cvar MO_G:
    :cvar MO_J:
    :cvar MO_S:
    :cvar NMI_BR:
    :cvar NMI_I:
    :cvar NP:
    :cvar OSM:
    :cvar OZ_AP:
    :cvar OZ_AV:
    :cvar OZ_TR:
    :cvar P_H:
    :cvar PC_BR:
    :cvar PC:
    :cvar PPB:
    :cvar PPM:
    :cvar PPTH:
    :cvar PPTR:
    :cvar BU_BR:
    :cvar PK_US:
    :cvar PWT_TR:
    :cvar VALUE_1:
    :cvar PRU:
    :cvar MU_0:
    :cvar EPS_0:
    :cvar PH_1:
    :cvar PCA:
    :cvar PIED:
    :cvar PT_BR:
    :cvar PT_US:
    :cvar PNT:
    :cvar POUCE:
    :cvar LB_AP:
    :cvar LB_AV:
    :cvar LB_TR:
    :cvar LBF_AV:
    :cvar M_P:
    :cvar PSI:
    :cvar QT_BR:
    :cvar QT_US:
    :cvar RAD_1:
    :cvar REM:
    :cvar RD_US:
    :cvar SC_AP:
    :cvar VALUE_2:
    :cvar SCT:
    :cvar SCWT_AV:
    :cvar STON_AV:
    :cvar SPH:
    :cvar SFT_I:
    :cvar SIN_I:
    :cvar SMI_US:
    :cvar SRD_US:
    :cvar SYD_I:
    :cvar MI_I:
    :cvar ST_1:
    :cvar SB:
    :cvar STONE_AV:
    :cvar SR:
    :cvar TBS_US:
    :cvar TSP_US:
    :cvar VALUE_10:
    :cvar PI:
    :cvar T_1:
    :cvar TWP:
    :cvar TB_U:
    :cvar U_1:
    :cvar C_1:
    :cvar WK:
    :cvar GAL_WI:
    :cvar YD_BR:
    :cvar YD_I:
    :cvar YD_US:
    :cvar A_1:
    :cvar A_G:
    :cvar A_J:
    :cvar A_T:
    :cvar C_2:
    :cvar DA:
    :cvar E_1:
    :cvar F_1:
    :cvar GI:
    :cvar KI:
    :cvar K_2:
    :cvar MI:
    :cvar M_1:
    :cvar N_1:
    :cvar P_1:
    :cvar TI:
    :cvar Y:
    :cvar Y_1:
    :cvar Z:
    :cvar Z_1:
    """
    C = "C"
    K = "K"
    CD = "cd"
    G = "g"
    M = "m"
    RAD = "rad"
    S = "s"
    APL_U = "[APL'U]"
    A = "A"
    AO = "Ao"
    BQ = "Bq"
    BETH_U = "[beth'U]"
    BI = "Bi"
    BDSK_U = "[bdsk'U]"
    K_1 = "[k]"
    BTU_39 = "[Btu_39]"
    BTU_59 = "[Btu_59]"
    BTU_60 = "[Btu_60]"
    BTU_IT = "[Btu_IT]"
    BTU_M = "[Btu_m]"
    BTU_TH = "[Btu_th]"
    BTU = "[Btu]"
    CAL = "[Cal]"
    CH = "[Ch]"
    CI = "Ci"
    DYE_U = "[dye'U]"
    F = "F"
    GPL_U = "[GPL'U]"
    GAL = "Gal"
    G_1 = "G"
    GB = "Gb"
    GY = "Gy"
    H = "H"
    HZ = "Hz"
    HNSF_U = "[hnsf'U]"
    J = "J"
    KY = "Ky"
    KA_U = "[ka'U]"
    KNK_U = "[knk'U]"
    LMB = "Lmb"
    MPL_U = "[MPL'U]"
    MCLG_U = "[mclg'U]"
    MX = "Mx"
    N = "N"
    G_2 = "[G]"
    OE = "Oe"
    OHM = "Ohm"
    PA = "Pa"
    H_1 = "[h]"
    P = "P"
    PCA_PR = "[pca_pr]"
    PNT_PR = "[pnt_pr]"
    R = "R"
    S_1 = "S"
    SV = "Sv"
    SMGY_U = "[smgy'U]"
    ST = "St"
    S_2 = "[S]"
    T = "T"
    TODD_U = "[todd'U]"
    U = "U"
    USP_U = "[USP'U]"
    V = "V"
    W = "W"
    WB = "Wb"
    G_3 = "[g]"
    ACR_BR = "[acr_br]"
    ACR_US = "[acr_us]"
    ARB_U = "[arb'U]"
    AR = "ar"
    AU = "AU"
    ATM = "atm"
    ATT = "att"
    BAR = "bar"
    B = "b"
    BBL_US = "[bbl_us]"
    BD = "Bd"
    B_1 = "B"
    B_K_W = "B[kW]"
    B_U_V = "B[uV]"
    B_M_V = "B[mV]"
    B_SPL = "B[SPL]"
    B_V = "B[V]"
    B_W = "B[W]"
    BIT = "bit"
    BIT_S = "bit_s"
    BF_I = "[bf_i]"
    BU_US = "[bu_us]"
    PK_BR = "[pk_br]"
    BY = "By"
    CAL_15 = "cal_[15]"
    CAL_20 = "cal_[20]"
    CAL_IT = "cal_IT"
    CAL_M = "cal_m"
    CAL_TH = "cal_th"
    CAL_1 = "cal"
    CAR_M = "[car_m]"
    CAR_AU = "[car_Au]"
    CH_BR = "[ch_br]"
    CH_US = "[ch_us]"
    RCH_US = "[rch_us]"
    CICERO = "[cicero]"
    CIRC = "circ"
    CML_I = "[cml_i]"
    CR_I = "[cr_i]"
    CRD_US = "[crd_us]"
    CFT_I = "[cft_i]"
    CIN_I = "[cin_i]"
    CYD_I = "[cyd_i]"
    CUP_US = "[cup_us]"
    D = "d"
    DEG = "deg"
    CEL = "Cel"
    DEG_F = "[degF]"
    DIDOT = "[didot]"
    DIOP = "[diop]"
    DR_AV = "[dr_av]"
    DR_AP = "[dr_ap]"
    DRP = "[drp]"
    DPT_US = "[dpt_us]"
    DQT_US = "[dqt_us]"
    DYN = "dyn"
    M_E = "[m_e]"
    E_V = "eV"
    E = "[e]"
    EQ = "eq"
    ERG = "erg"
    FTH_BR = "[fth_br]"
    FTH_I = "[fth_i]"
    FTH_US = "[fth_us]"
    FDR_BR = "[fdr_br]"
    FDR_US = "[fdr_us]"
    FOZ_BR = "[foz_br]"
    FOZ_US = "[foz_us]"
    FT_BR = "[ft_br]"
    FT_I = "[ft_i]"
    FT_US = "[ft_us]"
    RD_BR = "[rd_br]"
    FUR_US = "[fur_us]"
    GAL_BR = "[gal_br]"
    GAL_US = "[gal_us]"
    GIL_BR = "[gil_br]"
    GIL_US = "[gil_us]"
    GON = "gon"
    GR = "[gr]"
    G_4 = "g%"
    GF = "gf"
    HD_I = "[hd_i]"
    HPF = "[HPF]"
    H_2 = "h"
    IN_BR = "[in_br]"
    IN_I = "[in_i]"
    IN_US = "[in_us]"
    IN_I_HG = "[in_i'Hg]"
    IN_I_H2_O = "[in_i'H2O]"
    I_U = "[iU]"
    KAT = "kat"
    KN_BR = "[kn_br]"
    KN_I = "[kn_i]"
    LY = "[ly]"
    LIGNE = "[ligne]"
    LNE = "[lne]"
    LK_BR = "[lk_br]"
    LK_US = "[lk_us]"
    RLK_US = "[rlk_us]"
    L = "l"
    LCWT_AV = "[lcwt_av]"
    LTON_AV = "[lton_av]"
    LPF = "[LPF]"
    LM = "lm"
    LX = "lx"
    MESH_I = "[mesh_i]"
    MET = "[MET]"
    M_HG = "m[Hg]"
    M_H2_O = "m[H2O]"
    MIL_I = "[mil_i]"
    MIL_US = "[mil_us]"
    MI_BR = "[mi_br]"
    MI_US = "[mi_us]"
    MIN_BR = "[min_br]"
    MIN_US = "[min_us]"
    VALUE = "'"
    MIN = "min"
    MOL = "mol"
    MO = "mo"
    MO_G = "mo_g"
    MO_J = "mo_j"
    MO_S = "mo_s"
    NMI_BR = "[nmi_br]"
    NMI_I = "[nmi_i]"
    NP = "Np"
    OSM = "osm"
    OZ_AP = "[oz_ap]"
    OZ_AV = "[oz_av]"
    OZ_TR = "[oz_tr]"
    P_H = "[pH]"
    PC_BR = "[pc_br]"
    PC = "pc"
    PPB = "[ppb]"
    PPM = "[ppm]"
    PPTH = "[ppth]"
    PPTR = "[pptr]"
    BU_BR = "[bu_br]"
    PK_US = "[pk_us]"
    PWT_TR = "[pwt_tr]"
    VALUE_1 = "%"
    PRU = "[PRU]"
    MU_0 = "[mu_0]"
    EPS_0 = "[eps_0]"
    PH_1 = "ph"
    PCA = "[pca]"
    PIED = "[pied]"
    PT_BR = "[pt_br]"
    PT_US = "[pt_us]"
    PNT = "[pnt]"
    POUCE = "[pouce]"
    LB_AP = "[lb_ap]"
    LB_AV = "[lb_av]"
    LB_TR = "[lb_tr]"
    LBF_AV = "[lbf_av]"
    M_P = "[m_p]"
    PSI = "[psi]"
    QT_BR = "[qt_br]"
    QT_US = "[qt_us]"
    RAD_1 = "RAD"
    REM = "REM"
    RD_US = "[rd_us]"
    SC_AP = "[sc_ap]"
    VALUE_2 = "''"
    SCT = "[sct]"
    SCWT_AV = "[scwt_av]"
    STON_AV = "[ston_av]"
    SPH = "sph"
    SFT_I = "[sft_i]"
    SIN_I = "[sin_i]"
    SMI_US = "[smi_us]"
    SRD_US = "[srd_us]"
    SYD_I = "[syd_i]"
    MI_I = "[mi_i]"
    ST_1 = "st"
    SB = "sb"
    STONE_AV = "[stone_av]"
    SR = "sr"
    TBS_US = "[tbs_us]"
    TSP_US = "[tsp_us]"
    VALUE_10 = "10*"
    PI = "[pi]"
    T_1 = "t"
    TWP = "[twp]"
    TB_U = "[tb'U]"
    U_1 = "u"
    C_1 = "[c]"
    WK = "wk"
    GAL_WI = "[gal_wi]"
    YD_BR = "[yd_br]"
    YD_I = "[yd_i]"
    YD_US = "[yd_us]"
    A_1 = "a"
    A_G = "a_g"
    A_J = "a_j"
    A_T = "a_t"
    C_2 = "c"
    DA = "da"
    E_1 = "E"
    F_1 = "f"
    GI = "Gi"
    KI = "Ki"
    K_2 = "k"
    MI = "Mi"
    M_1 = "M"
    N_1 = "n"
    P_1 = "p"
    TI = "Ti"
    Y = "y"
    Y_1 = "Y"
    Z = "z"
    Z_1 = "Z"


class Unknown(Enum):
    """
    specDomain: S10612 (C-0-T10609-S10610-S10612-cpt)
    :cvar ASKU:
    :cvar NAV:
    :cvar UNK:
    :cvar QS:
    :cvar NASK:
    :cvar TRC:
    """
    ASKU = "ASKU"
    NAV = "NAV"
    UNK = "UNK"
    QS = "QS"
    NASK = "NASK"
    TRC = "TRC"


class UnorderedListStyle(Enum):
    """
    abstDomain: A19607 (C-0-T19602-A19605-A19607-cpt)
    :cvar CIRCLE:
    :cvar DISC:
    :cvar SQUARE:
    """
    CIRCLE = "Circle"
    DISC = "Disc"
    SQUARE = "Square"


class UpperChinook(Enum):
    """
    abstDomain: A18415 (C-0-T18130-A18413-A18414-A18415-cpt)
    :cvar X_WAC:
    """
    X_WAC = "x-WAC"


class UreteralRoute(Enum):
    """
    abstDomain: A17366 (C-0-T14581-A17021-A17366-cpt)
    :cvar URETINJ:
    """
    URETINJ = "URETINJ"


class UrethralRoute(Enum):
    """
    abstDomain: A17368 (C-0-T14581-A17021-A17368-cpt)
    :cvar URETHINJ:
    :cvar URETHINS:
    :cvar URETHSUP:
    :cvar URETHINSTL:
    """
    URETHINJ = "URETHINJ"
    URETHINS = "URETHINS"
    URETHSUP = "URETHSUP"
    URETHINSTL = "URETHINSTL"


class UrinaryBladderIrrigation(Enum):
    """
    specDomain: S14725 (C-0-T14581-A17021-A17373-S14725-cpt)
    :cvar BLADIRR:
    :cvar BLADIRRC:
    :cvar BLADIRRT:
    """
    BLADIRR = "BLADIRR"
    BLADIRRC = "BLADIRRC"
    BLADIRRT = "BLADIRRT"


class UrinaryBladderRoute(Enum):
    """
    abstDomain: A17373 (C-0-T14581-A17021-A17373-cpt)
    :cvar BLADIRR:
    :cvar BLADIRRC:
    :cvar BLADIRRT:
    :cvar BLADINJ:
    """
    BLADIRR = "BLADIRR"
    BLADIRRC = "BLADIRRC"
    BLADIRRT = "BLADIRRT"
    BLADINJ = "BLADINJ"


class UrinaryTractRoute(Enum):
    """
    abstDomain: A17378 (C-0-T14581-A17021-A17378-cpt)
    :cvar BLADINSTL:
    """
    BLADINSTL = "BLADINSTL"


class VaccineEntityType(Enum):
    """
    specDomain: S21458 (C-0-T16040-A19667-A19668-S21458-cpt)
    :cvar VCCNE:
    """
    VCCNE = "VCCNE"


class VaccineManufacturer(Enum):
    """
    vocSet: T227 (C-0-T227-cpt)
    :cvar AB:
    :cvar AD:
    :cvar ALP:
    :cvar AR:
    :cvar PMC:
    :cvar AVI:
    :cvar BA:
    :cvar BAY:
    :cvar BPC:
    :cvar BP:
    :cvar MIP:
    :cvar CEN:
    :cvar CHI:
    :cvar CON:
    :cvar EVN:
    :cvar GRE:
    :cvar IAG:
    :cvar IUS:
    :cvar KGC:
    :cvar LED:
    :cvar MA:
    :cvar MED:
    :cvar MSD:
    :cvar IM:
    :cvar MIL:
    :cvar NAB:
    :cvar NYB:
    :cvar NAV:
    :cvar NOV:
    :cvar OTC:
    :cvar ORT:
    :cvar PD:
    :cvar PRX:
    :cvar SCL:
    :cvar SKB:
    :cvar SI:
    :cvar JPN:
    :cvar USA:
    :cvar WAL:
    :cvar WA:
    """
    AB = "AB"
    AD = "AD"
    ALP = "ALP"
    AR = "AR"
    PMC = "PMC"
    AVI = "AVI"
    BA = "BA"
    BAY = "BAY"
    BPC = "BPC"
    BP = "BP"
    MIP = "MIP"
    CEN = "CEN"
    CHI = "CHI"
    CON = "CON"
    EVN = "EVN"
    GRE = "GRE"
    IAG = "IAG"
    IUS = "IUS"
    KGC = "KGC"
    LED = "LED"
    MA = "MA"
    MED = "MED"
    MSD = "MSD"
    IM = "IM"
    MIL = "MIL"
    NAB = "NAB"
    NYB = "NYB"
    NAV = "NAV"
    NOV = "NOV"
    OTC = "OTC"
    ORT = "ORT"
    PD = "PD"
    PRX = "PRX"
    SCL = "SCL"
    SKB = "SKB"
    SI = "SI"
    JPN = "JPN"
    USA = "USA"
    WAL = "WAL"
    WA = "WA"


class VaccineType(Enum):
    """
    vocSet: T228 (C-0-T228-cpt)
    :cvar VALUE_24:
    :cvar VALUE_19:
    :cvar VALUE_29:
    :cvar VALUE_26:
    :cvar VALUE_28:
    :cvar VALUE_1:
    :cvar VALUE_22:
    :cvar VALUE_20:
    :cvar VALUE_50:
    :cvar VALUE_30:
    :cvar VALUE_61:
    :cvar VALUE_62:
    :cvar VALUE_57:
    :cvar VALUE_85:
    :cvar VALUE_52:
    :cvar VALUE_83:
    :cvar VALUE_84:
    :cvar VALUE_31:
    :cvar VALUE_45:
    :cvar VALUE_8:
    :cvar VALUE_42:
    :cvar VALUE_43:
    :cvar VALUE_44:
    :cvar VALUE_58:
    :cvar VALUE_59:
    :cvar VALUE_47:
    :cvar VALUE_46:
    :cvar VALUE_49:
    :cvar VALUE_48:
    :cvar VALUE_17:
    :cvar VALUE_51:
    :cvar VALUE_86:
    :cvar VALUE_14:
    :cvar VALUE_87:
    :cvar VALUE_10:
    :cvar VALUE_39:
    :cvar VALUE_63:
    :cvar VALUE_66:
    :cvar VALUE_4:
    :cvar VALUE_3:
    :cvar VALUE_94:
    :cvar VALUE_2:
    :cvar VALUE_70:
    :cvar VALUE_34:
    :cvar VALUE_71:
    :cvar VALUE_93:
    :cvar VALUE_73:
    :cvar VALUE_76:
    :cvar VALUE_13:
    :cvar VALUE_98:
    :cvar VALUE_95:
    :cvar VALUE_96:
    :cvar VALUE_97:
    :cvar VALUE_9:
    :cvar VALUE_92:
    :cvar VALUE_81:
    :cvar VALUE_80:
    :cvar VALUE_36:
    :cvar VALUE_82:
    :cvar VALUE_54:
    :cvar VALUE_55:
    :cvar VALUE_27:
    :cvar VALUE_56:
    :cvar VALUE_12:
    :cvar VALUE_60:
    :cvar VALUE_88:
    :cvar VALUE_15:
    :cvar VALUE_16:
    :cvar VALUE_64:
    :cvar VALUE_65:
    :cvar VALUE_67:
    :cvar VALUE_5:
    :cvar VALUE_68:
    :cvar VALUE_32:
    :cvar VALUE_7:
    :cvar VALUE_69:
    :cvar VALUE_11:
    :cvar VALUE_23:
    :cvar VALUE_33:
    :cvar VALUE_100:
    :cvar VALUE_89:
    :cvar VALUE_90:
    :cvar VALUE_40:
    :cvar VALUE_18:
    :cvar VALUE_72:
    :cvar VALUE_74:
    :cvar VALUE_6:
    :cvar VALUE_38:
    :cvar VALUE_75:
    :cvar VALUE_35:
    :cvar VALUE_77:
    :cvar VALUE_78:
    :cvar VALUE_91:
    :cvar VALUE_101:
    :cvar VALUE_25:
    :cvar VALUE_41:
    :cvar VALUE_53:
    :cvar VALUE_79:
    :cvar VALUE_21:
    :cvar VALUE_37:
    """
    VALUE_24 = "24"
    VALUE_19 = "19"
    VALUE_29 = "29"
    VALUE_26 = "26"
    VALUE_28 = "28"
    VALUE_1 = "1"
    VALUE_22 = "22"
    VALUE_20 = "20"
    VALUE_50 = "50"
    VALUE_30 = "30"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_57 = "57"
    VALUE_85 = "85"
    VALUE_52 = "52"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_31 = "31"
    VALUE_45 = "45"
    VALUE_8 = "8"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_47 = "47"
    VALUE_46 = "46"
    VALUE_49 = "49"
    VALUE_48 = "48"
    VALUE_17 = "17"
    VALUE_51 = "51"
    VALUE_86 = "86"
    VALUE_14 = "14"
    VALUE_87 = "87"
    VALUE_10 = "10"
    VALUE_39 = "39"
    VALUE_63 = "63"
    VALUE_66 = "66"
    VALUE_4 = "4"
    VALUE_3 = "3"
    VALUE_94 = "94"
    VALUE_2 = "2"
    VALUE_70 = "70"
    VALUE_34 = "34"
    VALUE_71 = "71"
    VALUE_93 = "93"
    VALUE_73 = "73"
    VALUE_76 = "76"
    VALUE_13 = "13"
    VALUE_98 = "98"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_9 = "9"
    VALUE_92 = "92"
    VALUE_81 = "81"
    VALUE_80 = "80"
    VALUE_36 = "36"
    VALUE_82 = "82"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_27 = "27"
    VALUE_56 = "56"
    VALUE_12 = "12"
    VALUE_60 = "60"
    VALUE_88 = "88"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_67 = "67"
    VALUE_5 = "5"
    VALUE_68 = "68"
    VALUE_32 = "32"
    VALUE_7 = "7"
    VALUE_69 = "69"
    VALUE_11 = "11"
    VALUE_23 = "23"
    VALUE_33 = "33"
    VALUE_100 = "100"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_40 = "40"
    VALUE_18 = "18"
    VALUE_72 = "72"
    VALUE_74 = "74"
    VALUE_6 = "6"
    VALUE_38 = "38"
    VALUE_75 = "75"
    VALUE_35 = "35"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_91 = "91"
    VALUE_101 = "101"
    VALUE_25 = "25"
    VALUE_41 = "41"
    VALUE_53 = "53"
    VALUE_79 = "79"
    VALUE_21 = "21"
    VALUE_37 = "37"


class VaginalCream(Enum):
    """
    specDomain: S14473 (C-0-T19651-A14411-A14412-A14463-S14466-S14473-cpt)
    :cvar VAGCRM:
    :cvar VAGCRMAPL:
    """
    VAGCRM = "VAGCRM"
    VAGCRMAPL = "VAGCRMAPL"


class VaginalFoam(Enum):
    """
    specDomain: S14549 (C-0-T19651-A14411-A14412-A14545-S14546-S14549-cpt)
    :cvar VAGFOAM:
    :cvar VAGFOAMAPL:
    """
    VAGFOAM = "VAGFOAM"
    VAGFOAMAPL = "VAGFOAMAPL"


class VaginalGel(Enum):
    """
    specDomain: S14449 (C-0-T19651-A14411-A14412-A14441-S14442-S14449-cpt)
    :cvar VAGGEL:
    :cvar VGELAPL:
    """
    VAGGEL = "VAGGEL"
    VGELAPL = "VGELAPL"


class VaginalOintment(Enum):
    """
    specDomain: S14482 (C-0-T19651-A14411-A14412-A14463-S14475-S14482-cpt)
    :cvar VAGOINT:
    :cvar VAGOINTAPL:
    """
    VAGOINT = "VAGOINT"
    VAGOINTAPL = "VAGOINTAPL"


class VaginalRoute(Enum):
    """
    abstDomain: A17380 (C-0-T14581-A17021-A17380-cpt)
    :cvar DOUCHE:
    :cvar VAGINSI:
    :cvar VAGINS:
    """
    DOUCHE = "DOUCHE"
    VAGINSI = "VAGINSI"
    VAGINS = "VAGINS"


class ValidationIssue(Enum):
    """
    specDomain: S21651 (C-0-T14878-A19692-A19781-A16124-A19429-A19620-S21651-cpt)
    :cvar CODE_INVAL:
    :cvar CODE_DEPREC:
    :cvar DUPTHPY:
    :cvar DUPTHPGEN:
    :cvar DUPTHPCLS:
    :cvar COMPLY:
    :cvar PLYDOC:
    :cvar PLYPHRM:
    :cvar ABUSE:
    :cvar FRAUD:
    :cvar DOSE:
    :cvar DOSEDUR:
    :cvar DOSEIVL:
    :cvar DOSEH:
    :cvar DOSEL:
    :cvar DOSECOND:
    :cvar MDOSE:
    :cvar LEN_RANGE:
    :cvar LEN_LONG:
    :cvar LEN_SHORT:
    :cvar OBSA:
    :cvar AGE:
    :cvar COND:
    :cvar GEND:
    :cvar GEN:
    :cvar LAB:
    :cvar REACT:
    :cvar RREACT:
    :cvar CREACT:
    :cvar REP_RANGE:
    :cvar MAXOCCURS:
    :cvar MINOCCURS:
    :cvar VALIDAT:
    :cvar KEY205:
    :cvar KEY204:
    :cvar BUS:
    :cvar MISSCOND:
    :cvar NODUPS:
    :cvar ILLEGAL:
    :cvar FORMAT:
    :cvar MISSMAND:
    """
    CODE_INVAL = "CODE_INVAL"
    CODE_DEPREC = "CODE_DEPREC"
    DUPTHPY = "DUPTHPY"
    DUPTHPGEN = "DUPTHPGEN"
    DUPTHPCLS = "DUPTHPCLS"
    COMPLY = "COMPLY"
    PLYDOC = "PLYDOC"
    PLYPHRM = "PLYPHRM"
    ABUSE = "ABUSE"
    FRAUD = "FRAUD"
    DOSE = "DOSE"
    DOSEDUR = "DOSEDUR"
    DOSEIVL = "DOSEIVL"
    DOSEH = "DOSEH"
    DOSEL = "DOSEL"
    DOSECOND = "DOSECOND"
    MDOSE = "MDOSE"
    LEN_RANGE = "LEN_RANGE"
    LEN_LONG = "LEN_LONG"
    LEN_SHORT = "LEN_SHORT"
    OBSA = "OBSA"
    AGE = "AGE"
    COND = "COND"
    GEND = "GEND"
    GEN = "GEN"
    LAB = "LAB"
    REACT = "REACT"
    RREACT = "RREACT"
    CREACT = "CREACT"
    REP_RANGE = "REP_RANGE"
    MAXOCCURS = "MAXOCCURS"
    MINOCCURS = "MINOCCURS"
    VALIDAT = "VALIDAT"
    KEY205 = "KEY205"
    KEY204 = "KEY204"
    BUS = "BUS"
    MISSCOND = "MISSCOND"
    NODUPS = "NODUPS"
    ILLEGAL = "ILLEGAL"
    FORMAT = "FORMAT"
    MISSMAND = "MISSMAND"


class ValueSetOperator(Enum):
    """
    vocSet: T11037 (C-0-T11037-cpt)
    :cvar E:
    :cvar I:
    """
    E = "E"
    I = "I"


class ValueSetPropertyId(Enum):
    """
    vocSet: T19362 (C-0-T19362-cpt)
    :cvar APPLIES_TO:
    :cvar HOW_APPLIES:
    :cvar OPEN_ISSUE:
    """
    APPLIES_TO = "appliesTo"
    HOW_APPLIES = "howApplies"
    OPEN_ISSUE = "openIssue"


class ValueSetStatus(Enum):
    """
    vocSet: T19360-1 (C-0-T19360-1-cpt)
    :cvar A:
    :cvar D:
    :cvar P:
    :cvar R:
    """
    A = "A"
    D = "D"
    P = "P"
    R = "R"


class VerificationMethod(Enum):
    """
    abstDomain: A19707 (C-0-T14079-A19707-cpt)
    :cvar VDOC:
    :cvar VTOKEN:
    :cvar VREG:
    :cvar VVOICE:
    """
    VDOC = "VDOC"
    VTOKEN = "VTOKEN"
    VREG = "VREG"
    VVOICE = "VVOICE"


class VerificationOutcomeValue(Enum):
    """
    abstDomain: A19793 (C-0-T16614-A19793-cpt)
    :cvar ACTPEND:
    :cvar ACT:
    :cvar ELG:
    :cvar INACT:
    :cvar INPNDUPD:
    :cvar INPNDINV:
    :cvar NELG:
    """
    ACTPEND = "ACTPEND"
    ACT = "ACT"
    ELG = "ELG"
    INACT = "INACT"
    INPNDUPD = "INPNDUPD"
    INPNDINV = "INPNDINV"
    NELG = "NELG"


class VeterinarianHipaa(Enum):
    """
    abstDomain: A13352 (C-0-T13129-A13130-A13136-A13352-cpt)
    :cvar VALUE_174_MM1900_N:
    """
    VALUE_174_MM1900_N = "174MM1900N"


class VeterinarianProviderCodes(Enum):
    """
    specDomain: S20453 (C-0-T19465-S20434-S20448-S20453-cpt)
    :cvar VALUE_174_M00000_X:
    :cvar VALUE_174_MM1900_X:
    """
    VALUE_174_M00000_X = "174M00000X"
    VALUE_174_MM1900_X = "174MM1900X"


class VideoMediaType(Enum):
    """
    abstDomain: A14845 (C-0-T14824-A14845-cpt)
    :cvar VIDEO_MPEG:
    :cvar VIDEO_X_AVI:
    """
    VIDEO_MPEG = "video/mpeg"
    VIDEO_X_AVI = "video/x-avi"


class VitreousHumourRoute(Enum):
    """
    abstDomain: A17384 (C-0-T14581-A17021-A17384-cpt)
    :cvar IVITIMPLNT:
    """
    IVITIMPLNT = "IVITIMPLNT"


class VocabularyDomainQualifier(Enum):
    """
    vocSet: T11046 (C-0-T11046-cpt)
    :cvar CNE:
    :cvar CWE:
    :cvar CANADA:
    :cvar NORTH_AMERICA:
    :cvar USA:
    :cvar UV:
    """
    CNE = "CNE"
    CWE = "CWE"
    CANADA = "Canada"
    NORTH_AMERICA = "NorthAmerica"
    USA = "USA"
    UV = "UV"


class WeightAlert(Enum):
    """
    abstDomain: A17794 (C-0-T14878-A19692-A19781-A16124-A16656-A16657-A16658-S16664-S16665-A17794-cpt)
    :cvar DOSEHINDW:
    :cvar DOSELINDW:
    """
    DOSEHINDW = "DOSEHINDW"
    DOSELINDW = "DOSELINDW"


class WesternApachean(Enum):
    """
    abstDomain: A18400 (C-0-T18130-A18352-A18356-A18358-A18399-A18400-cpt)
    :cvar X_NAV:
    :cvar X_APM:
    :cvar X_APW:
    """
    X_NAV = "x-NAV"
    X_APM = "x-APM"
    X_APW = "x-APW"


class WesternMiwok(Enum):
    """
    abstDomain: A18460 (C-0-T18130-A18413-A18458-A18459-A18460-cpt)
    :cvar X_CSI:
    :cvar X_LMW:
    """
    X_CSI = "x-CSI"
    X_LMW = "x-LMW"


class WesternMuskogean(Enum):
    """
    abstDomain: A18339 (C-0-T18130-A18338-A18339-cpt)
    :cvar X_CIC:
    :cvar X_CCT:
    """
    X_CIC = "x-CIC"
    X_CCT = "x-CCT"


class WesternNumic(Enum):
    """
    abstDomain: A18607 (C-0-T18130-A18605-A18606-A18607-cpt)
    :cvar X_MON:
    :cvar X_PAO:
    """
    X_MON = "x-MON"
    X_PAO = "x-PAO"


class Wintuan(Enum):
    """
    abstDomain: A18431 (C-0-T18130-A18413-A18431-cpt)
    :cvar X_WIT:
    """
    X_WIT = "x-WIT"


class Wiyot(Enum):
    """
    specDomain: S15447 (C-0-T14914-S14915-S14916-S15447-cpt)
    :cvar VALUE_1704_6:
    :cvar VALUE_1705_3:
    """
    VALUE_1704_6 = "1704-6"
    VALUE_1705_3 = "1705-3"


class WorkPlaceAddressUse(Enum):
    """
    specDomain: S10631 (C-0-T201-A190-S10631-cpt)
    :cvar WP:
    :cvar DIR:
    :cvar PUB:
    """
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"


class Yaqui(Enum):
    """
    specDomain: S15451 (C-0-T14914-S14915-S14916-S15451-cpt)
    :cvar VALUE_1711_1:
    :cvar VALUE_1712_9:
    :cvar VALUE_1713_7:
    """
    VALUE_1711_1 = "1711-1"
    VALUE_1712_9 = "1712-9"
    VALUE_1713_7 = "1713-7"


class Yokuts(Enum):
    """
    specDomain: S15455 (C-0-T14914-S14915-S14916-S15455-cpt)
    :cvar VALUE_1717_8:
    :cvar VALUE_1718_6:
    :cvar VALUE_1719_4:
    :cvar VALUE_1720_2:
    """
    VALUE_1717_8 = "1717-8"
    VALUE_1718_6 = "1718-6"
    VALUE_1719_4 = "1719-4"
    VALUE_1720_2 = "1720-2"


class Yokutsan(Enum):
    """
    abstDomain: A18479 (C-0-T18130-A18413-A18479-cpt)
    :cvar X_GSH:
    :cvar X_ENH:
    :cvar X_PYL:
    :cvar X_TKH:
    """
    X_GSH = "x-GSH"
    X_ENH = "x-ENH"
    X_PYL = "x-PYL"
    X_TKH = "x-TKH"


class Yukian(Enum):
    """
    abstDomain: A18646 (C-0-T18130-A18646-cpt)
    :cvar X_WAO:
    :cvar X_YUK:
    """
    X_WAO = "x-WAO"
    X_YUK = "x-YUK"


class Type0272(Enum):
    """
    specDomain: S21445 (C-0-T14079-S21445-cpt)
    :cvar VALUE_0272:
    :cvar VALUE_0245:
    :cvar VALUE_0246:
    """
    VALUE_0272 = "0272"
    VALUE_0245 = "0245"
    VALUE_0246 = "0246"


class Type0275a(Enum):
    """
    specDomain: S21449 (C-0-T14079-S21449-cpt)
    :cvar VALUE_0275A:
    """
    VALUE_0275A = "0275a"


class Type0280(Enum):
    """
    specDomain: S21454 (C-0-T14079-S21454-cpt)
    :cvar VALUE_0280:
    :cvar VALUE_0278:
    :cvar VALUE_0240:
    :cvar VALUE_0241:
    :cvar VALUE_0242:
    :cvar VALUE_0279:
    :cvar VALUE_0275:
    :cvar VALUE_0272:
    :cvar VALUE_0275A:
    :cvar VALUE_0277:
    :cvar VALUE_0276:
    :cvar VALUE_0273:
    :cvar VALUE_0274:
    """
    VALUE_0280 = "0280"
    VALUE_0278 = "0278"
    VALUE_0240 = "0240"
    VALUE_0241 = "0241"
    VALUE_0242 = "0242"
    VALUE_0279 = "0279"
    VALUE_0275 = "0275"
    VALUE_0272 = "0272"
    VALUE_0275A = "0275a"
    VALUE_0277 = "0277"
    VALUE_0276 = "0276"
    VALUE_0273 = "0273"
    VALUE_0274 = "0274"


class XAccommodationRequestorRole(Enum):
    """
    abstDomain: A19352 (C-0-T11555-A19352-cpt)
    :cvar AGNT:
    :cvar PROV:
    :cvar PAT:
    :cvar PRS:
    """
    AGNT = "AGNT"
    PROV = "PROV"
    PAT = "PAT"
    PRS = "PRS"


class XActClassCareProvisionEncounter(Enum):
    """
    abstDomain: A19887 (C-0-T11527-A19887-cpt)
    :cvar PCPR:
    :cvar ENC:
    """
    PCPR = "PCPR"
    ENC = "ENC"


class XActClassCareProvisionObservation(Enum):
    """
    abstDomain: A19888 (C-0-T11527-A19888-cpt)
    :cvar PCPR:
    :cvar OBS:
    """
    PCPR = "PCPR"
    OBS = "OBS"


class XActClassCareProvisionProcedure(Enum):
    """
    abstDomain: A19889 (C-0-T11527-A19889-cpt)
    :cvar PCPR:
    :cvar PROC:
    """
    PCPR = "PCPR"
    PROC = "PROC"


class XActClassDocumentEntryAct(Enum):
    """
    abstDomain: A19599 (C-0-T11527-A19599-cpt)
    :cvar ACCM:
    :cvar ACT:
    :cvar PCPR:
    :cvar CTTEVENT:
    :cvar CONS:
    :cvar INC:
    :cvar INFRM:
    :cvar REG:
    :cvar SPCTRT:
    :cvar TRNS:
    """
    ACCM = "ACCM"
    ACT = "ACT"
    PCPR = "PCPR"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    INC = "INC"
    INFRM = "INFRM"
    REG = "REG"
    SPCTRT = "SPCTRT"
    TRNS = "TRNS"


class XActClassDocumentEntryOrganizer(Enum):
    """
    abstDomain: A19598 (C-0-T11527-A19598-cpt)
    :cvar CLUSTER:
    :cvar BATTERY:
    """
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"


class XActEncounterReason(Enum):
    """
    abstDomain: A19456 (C-0-T14878-A19456-cpt)
    :cvar MEDNEC:
    :cvar PAT:
    """
    MEDNEC = "MEDNEC"
    PAT = "PAT"


class XActFinancialProductAcquisitionCode(Enum):
    """
    abstDomain: A17963 (C-0-T13953-A13954-A17963-cpt)
    :cvar RENT:
    :cvar SALE:
    """
    RENT = "RENT"
    SALE = "SALE"


class XActMoodDefEvn(Enum):
    """
    abstDomain: A19375 (C-0-T10196-A19375-cpt)
    :cvar DEF_VALUE:
    :cvar EVN:
    """
    DEF_VALUE = "DEF"
    EVN = "EVN"


class XActMoodDefEvnRqo(Enum):
    """
    abstDomain: A19762 (C-0-T10196-A19762-cpt)
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar RQO:
    """
    DEF_VALUE = "DEF"
    EVN = "EVN"
    RQO = "RQO"


class XActMoodDefEvnRqoPrmsPrp(Enum):
    """
    abstDomain: A19371 (C-0-T10196-A19371-cpt)
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    DEF_VALUE = "DEF"
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XActMoodDocumentObservation(Enum):
    """
    abstDomain: A18943 (C-0-T10196-A18943-cpt)
    :cvar GOL:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    GOL = "GOL"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XActMoodEvnOrdPrmsPrp(Enum):
    """
    abstDomain: A18965 (C-0-T10196-A18965-cpt)
    :cvar EVN:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XActMoodIntentEvent(Enum):
    """
    abstDomain: A16742 (C-0-T10196-A16742-cpt)
    :cvar EVN:
    """
    EVN = "EVN"


class XActMoodOrdPrms(Enum):
    """
    abstDomain: A16735 (C-0-T10196-A16735-cpt)
    :cvar PRMS:
    :cvar RQO:
    """
    PRMS = "PRMS"
    RQO = "RQO"


class XActMoodOrdPrmsEvn(Enum):
    """
    abstDomain: A16730 (C-0-T10196-A16730-cpt)
    :cvar EVN:
    :cvar PRMS:
    :cvar RQO:
    """
    EVN = "EVN"
    PRMS = "PRMS"
    RQO = "RQO"


class XActMoodPermPermrq(Enum):
    """
    abstDomain: A19689 (C-0-T10196-A19689-cpt)
    :cvar PERM:
    :cvar PERMRQ:
    """
    PERM = "PERM"
    PERMRQ = "PERMRQ"


class XActMoodRequestEvent(Enum):
    """
    abstDomain: A19763 (C-0-T10196-A19763-cpt)
    :cvar EVN:
    :cvar RQO:
    """
    EVN = "EVN"
    RQO = "RQO"


class XActMoodRqoPrpAptArq(Enum):
    """
    abstDomain: A19372 (C-0-T10196-A19372-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    PRP = "PRP"
    RQO = "RQO"


class XActOrderableOrBillable(Enum):
    """
    abstDomain: A19822 (C-0-T11527-A19822-cpt)
    :cvar ACCM:
    :cvar PCPR:
    :cvar ENC:
    :cvar SBADM:
    :cvar TRNS:
    """
    ACCM = "ACCM"
    PCPR = "PCPR"
    ENC = "ENC"
    SBADM = "SBADM"
    TRNS = "TRNS"


class XActRelationshipDocument(Enum):
    """
    abstDomain: A11610 (C-0-T10317-A11610-cpt)
    :cvar APND:
    :cvar RPLC:
    :cvar XFRM:
    """
    APND = "APND"
    RPLC = "RPLC"
    XFRM = "XFRM"


class XActRelationshipEntry(Enum):
    """
    abstDomain: A19446 (C-0-T10317-A19446-cpt)
    :cvar COMP:
    :cvar DRIV:
    """
    COMP = "COMP"
    DRIV = "DRIV"


class XActRelationshipEntryRelationship(Enum):
    """
    abstDomain: A19447 (C-0-T10317-A19447-cpt)
    :cvar XCRPT:
    :cvar GEVL:
    :cvar COMP:
    :cvar RSON:
    :cvar SUBJ:
    :cvar SPRT:
    :cvar CAUS:
    :cvar MFST:
    :cvar REFR:
    :cvar SAS:
    """
    XCRPT = "XCRPT"
    GEVL = "GEVL"
    COMP = "COMP"
    RSON = "RSON"
    SUBJ = "SUBJ"
    SPRT = "SPRT"
    CAUS = "CAUS"
    MFST = "MFST"
    REFR = "REFR"
    SAS = "SAS"


class XActRelationshipExternalReference(Enum):
    """
    abstDomain: A19000 (C-0-T10317-A19000-cpt)
    :cvar XCRPT:
    :cvar ELNK:
    :cvar SUBJ:
    :cvar SPRT:
    :cvar REFR:
    :cvar RPLC:
    """
    XCRPT = "XCRPT"
    ELNK = "ELNK"
    SUBJ = "SUBJ"
    SPRT = "SPRT"
    REFR = "REFR"
    RPLC = "RPLC"


class XActRelationshipPatientTransport(Enum):
    """
    abstDomain: A19005 (C-0-T10317-A19005-cpt)
    :cvar ARR:
    :cvar DEP:
    """
    ARR = "ARR"
    DEP = "DEP"


class XActRelationshipPertinentInfo(Enum):
    """
    abstDomain: A19562 (C-0-T10317-A19562-cpt)
    :cvar SUBJ:
    :cvar SPRT:
    :cvar CAUS:
    :cvar MFST:
    :cvar REFR:
    """
    SUBJ = "SUBJ"
    SPRT = "SPRT"
    CAUS = "CAUS"
    MFST = "MFST"
    REFR = "REFR"


class XActRelationshipRelatedAuthorizations(Enum):
    """
    abstDomain: A19825 (C-0-T10317-A19825-cpt)
    :cvar AUTH:
    :cvar REFR:
    """
    AUTH = "AUTH"
    REFR = "REFR"


class XActReplaceOrRevise(Enum):
    """
    abstDomain: A19764 (C-0-T10317-A19764-cpt)
    :cvar MOD:
    :cvar RPLC:
    """
    MOD = "MOD"
    RPLC = "RPLC"


class XActStatusActiveComplete(Enum):
    """
    abstDomain: A19890 (C-0-T15933-A19890-cpt)
    :cvar ACTIVE:
    :cvar COMPLETED:
    """
    ACTIVE = "active"
    COMPLETED = "completed"


class XActStatusActiveSuspended(Enum):
    """
    abstDomain: A19891 (C-0-T15933-A19891-cpt)
    :cvar ACTIVE:
    :cvar SUSPENDED:
    """
    ACTIVE = "active"
    SUSPENDED = "suspended"


class XAdverseEventCausalityAssessmentMethods(Enum):
    """
    abstDomain: A19380 (C-0-T14079-A19380-cpt)
    :cvar ALGM:
    :cvar BYCL:
    :cvar GINT:
    """
    ALGM = "ALGM"
    BYCL = "BYCL"
    GINT = "GINT"


class XBasicConfidentialityKind(Enum):
    """
    abstDomain: A16926 (C-0-T10228-A16926-cpt)
    :cvar N:
    :cvar R:
    :cvar V:
    """
    N = "N"
    R = "R"
    V = "V"


class XClinicalStatementActMood(Enum):
    """
    abstDomain: A19649 (C-0-T10196-A19649-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementEncounterMood(Enum):
    """
    abstDomain: A19648 (C-0-T10196-A19648-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementObservationMood(Enum):
    """
    abstDomain: A19644 (C-0-T10196-A19644-cpt)
    :cvar GOL:
    :cvar APT:
    :cvar ARQ:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    GOL = "GOL"
    APT = "APT"
    ARQ = "ARQ"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementProcedureMood(Enum):
    """
    abstDomain: A19647 (C-0-T10196-A19647-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementSubstanceMood(Enum):
    """
    abstDomain: A19645 (C-0-T10196-A19645-cpt)
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementSupplyMood(Enum):
    """
    abstDomain: A19646 (C-0-T10196-A19646-cpt)
    :cvar EVN:
    :cvar INT_VALUE:
    """
    EVN = "EVN"
    INT_VALUE = "INT"


class XDeterminerInstanceKind(Enum):
    """
    abstDomain: A19670 (C-0-T10878-A19670-cpt)
    :cvar KIND:
    :cvar QUANTIFIED_KIND:
    :cvar INSTANCE:
    """
    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
    INSTANCE = "INSTANCE"


class XDocumentActMood(Enum):
    """
    abstDomain: A19458 (C-0-T10196-A19458-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentEncounterMood(Enum):
    """
    abstDomain: A19459 (C-0-T10196-A19459-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentEntrySubject(Enum):
    """
    abstDomain: A19367 (C-0-T11555-A19367-cpt)
    :cvar PAT:
    :cvar PRS:
    :cvar SPEC:
    """
    PAT = "PAT"
    PRS = "PRS"
    SPEC = "SPEC"


class XDocumentProcedureMood(Enum):
    """
    abstDomain: A19460 (C-0-T10196-A19460-cpt)
    :cvar APT:
    :cvar ARQ:
    :cvar DEF_VALUE:
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    APT = "APT"
    ARQ = "ARQ"
    DEF_VALUE = "DEF"
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentStatus(Enum):
    """
    abstDomain: A16916 (C-0-T15933-A16916-cpt)
    :cvar ACTIVE:
    :cvar CANCELLED:
    :cvar NEW:
    :cvar OBSOLETE:
    """
    ACTIVE = "active"
    CANCELLED = "cancelled"
    NEW = "new"
    OBSOLETE = "obsolete"


class XDocumentSubject(Enum):
    """
    abstDomain: A19368 (C-0-T11555-A19368-cpt)
    :cvar PAT:
    :cvar PRS:
    """
    PAT = "PAT"
    PRS = "PRS"


class XDocumentSubstanceMood(Enum):
    """
    abstDomain: A19461 (C-0-T10196-A19461-cpt)
    :cvar EVN:
    :cvar INT_VALUE:
    :cvar PRMS:
    :cvar PRP:
    :cvar RQO:
    """
    EVN = "EVN"
    INT_VALUE = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XEncounterAdmissionUrgency(Enum):
    """
    abstDomain: A19457 (C-0-T16866-A19457-cpt)
    :cvar EL:
    :cvar EM:
    :cvar R:
    :cvar UR:
    """
    EL = "EL"
    EM = "EM"
    R = "R"
    UR = "UR"


class XEncounterParticipant(Enum):
    """
    abstDomain: A19600 (C-0-T10901-A19600-cpt)
    :cvar ADM:
    :cvar ATND:
    :cvar CON:
    :cvar DIS:
    :cvar REF:
    """
    ADM = "ADM"
    ATND = "ATND"
    CON = "CON"
    DIS = "DIS"
    REF = "REF"


class XEncounterPerformerParticipation(Enum):
    """
    abstDomain: A16764 (C-0-T10901-A16764-cpt)
    :cvar CON:
    :cvar PRF:
    :cvar SPRF:
    """
    CON = "CON"
    PRF = "PRF"
    SPRF = "SPRF"


class XEntityClassDocumentReceiving(Enum):
    """
    abstDomain: A19462 (C-0-T10882-A19462-cpt)
    :cvar HCE:
    :cvar PSN:
    """
    HCE = "HCE"
    PSN = "PSN"


class XEntityClassPersonOrOrgReceiving(Enum):
    """
    abstDomain: A19463 (C-0-T10882-A19463-cpt)
    :cvar PSN:
    """
    PSN = "PSN"


class XInformationRecipient(Enum):
    """
    abstDomain: A19366 (C-0-T10901-A19366-cpt)
    :cvar PRCP:
    :cvar TRC:
    """
    PRCP = "PRCP"
    TRC = "TRC"


class XInformationRecipientRole(Enum):
    """
    abstDomain: A16772 (C-0-T11555-A16772-cpt)
    :cvar ASSIGNED:
    :cvar HLTHCHRT:
    """
    ASSIGNED = "ASSIGNED"
    HLTHCHRT = "HLTHCHRT"


class XLabProcessClassCodes(Enum):
    """
    abstDomain: A19657 (C-0-T11527-A19657-cpt)
    :cvar ACSN:
    :cvar CONTREG:
    :cvar PROC:
    :cvar SPCTRT:
    :cvar TRNS:
    """
    ACSN = "ACSN"
    CONTREG = "CONTREG"
    PROC = "PROC"
    SPCTRT = "SPCTRT"
    TRNS = "TRNS"


class XLabSpecimenCollectionProviders(Enum):
    """
    abstDomain: A19748 (C-0-T12206-A19679-A19748-cpt)
    :cvar COMMUNITY_LABORATORY:
    :cvar HOME_HEALTH:
    :cvar LABORATORY:
    :cvar PATHOLOGIST:
    :cvar PHLEBOTOMIST:
    :cvar SELF:
    :cvar THIRD_PARTY:
    """
    COMMUNITY_LABORATORY = "communityLaboratory"
    HOME_HEALTH = "homeHealth"
    LABORATORY = "laboratory"
    PATHOLOGIST = "pathologist"
    PHLEBOTOMIST = "phlebotomist"
    SELF = "self"
    THIRD_PARTY = "thirdParty"


class XMedicationOrImmunization(Enum):
    """
    abstDomain: A19745 (C-0-T13953-A13954-A19708-A19745-cpt)
    :cvar DRUG:
    :cvar IMMUNIZ:
    """
    DRUG = "DRUG"
    IMMUNIZ = "IMMUNIZ"


class XOrganizationNamePartType(Enum):
    """
    abstDomain: A15881 (C-0-T15880-A15881-cpt)
    :cvar DEL_VALUE:
    :cvar PFX:
    :cvar SFX:
    """
    DEL_VALUE = "DEL"
    PFX = "PFX"
    SFX = "SFX"


class XParticipationAuthorPerformer(Enum):
    """
    abstDomain: A19080 (C-0-T10901-A19080-cpt)
    :cvar AUT:
    :cvar PRF:
    """
    AUT = "AUT"
    PRF = "PRF"


class XParticipationEntVrf(Enum):
    """
    abstDomain: A19588 (C-0-T10901-A19588-cpt)
    :cvar ENT:
    :cvar VRF:
    """
    ENT = "ENT"
    VRF = "VRF"


class XParticipationPrfEntVrf(Enum):
    """
    abstDomain: A19589 (C-0-T10901-A19589-cpt)
    :cvar ENT:
    :cvar PRF:
    :cvar VRF:
    """
    ENT = "ENT"
    PRF = "PRF"
    VRF = "VRF"


class XParticipationVrfRespSprfWit(Enum):
    """
    abstDomain: A19083 (C-0-T10901-A19083-cpt)
    :cvar RESP:
    :cvar SPRF:
    :cvar VRF:
    :cvar WIT:
    """
    RESP = "RESP"
    SPRF = "SPRF"
    VRF = "VRF"
    WIT = "WIT"


class XPayeeRelationshipRoleType(Enum):
    """
    abstDomain: A18105 (C-0-T12206-A18105-cpt)
    :cvar FM:
    :cvar GT:
    :cvar PT:
    :cvar PH:
    """
    FM = "FM"
    GT = "GT"
    PT = "PT"
    PH = "PH"


class XPersonNamePartType(Enum):
    """
    abstDomain: A10653 (C-0-T15880-A10653-cpt)
    :cvar DEL_VALUE:
    :cvar FAM:
    :cvar GIV:
    :cvar PFX:
    :cvar SFX:
    """
    DEL_VALUE = "DEL"
    FAM = "FAM"
    GIV = "GIV"
    PFX = "PFX"
    SFX = "SFX"


class XPhoneOrEmailUrlscheme(Enum):
    """
    abstDomain: A19741 (C-0-T14866-A19741-cpt)
    :cvar FAX:
    :cvar MAILTO:
    :cvar TEL:
    """
    FAX = "fax"
    MAILTO = "mailto"
    TEL = "tel"


class XPhoneUrlscheme(Enum):
    """
    abstDomain: A19742 (C-0-T14866-A19742-cpt)
    :cvar FAX:
    :cvar TEL:
    """
    FAX = "fax"
    TEL = "tel"


class XPhysicalVerbalParticipationMode(Enum):
    """
    abstDomain: A19739 (C-0-T16543-A19739-cpt)
    :cvar PHYSICAL:
    :cvar VERBAL:
    """
    PHYSICAL = "PHYSICAL"
    VERBAL = "VERBAL"


class XRoleClassAccommodationRequestor(Enum):
    """
    abstDomain: A19382 (C-0-T11555-A19382-cpt)
    :cvar AGNT:
    :cvar PROV:
    :cvar PAT:
    :cvar PRS:
    """
    AGNT = "AGNT"
    PROV = "PROV"
    PAT = "PAT"
    PRS = "PRS"


class XRoleClassCoverage(Enum):
    """
    abstDomain: A14008 (C-0-T11555-A14008-cpt)
    :cvar SPNSR:
    :cvar COVPTY:
    :cvar POLHOLD:
    :cvar UNDWRT:
    """
    SPNSR = "SPNSR"
    COVPTY = "COVPTY"
    POLHOLD = "POLHOLD"
    UNDWRT = "UNDWRT"


class XRoleClassCoverageInvoice(Enum):
    """
    abstDomain: A14013 (C-0-T11555-A14013-cpt)
    :cvar PAYOR:
    :cvar PAYEE:
    """
    PAYOR = "PAYOR"
    PAYEE = "PAYEE"


class XRoleClassCredentialedEntity(Enum):
    """
    abstDomain: A16930 (C-0-T11555-A16930-cpt)
    :cvar ASSIGNED:
    :cvar QUAL:
    """
    ASSIGNED = "ASSIGNED"
    QUAL = "QUAL"


class XRoleClassPayeePolicyRelationship(Enum):
    """
    abstDomain: A19395 (C-0-T11555-A19395-cpt)
    :cvar COVPTY:
    :cvar GUAR:
    :cvar PROV:
    :cvar PRS:
    :cvar POLHOLD:
    """
    COVPTY = "COVPTY"
    GUAR = "GUAR"
    PROV = "PROV"
    PRS = "PRS"
    POLHOLD = "POLHOLD"


class XSuccReplPrev(Enum):
    """
    abstDomain: A19753 (C-0-T10317-A19753-cpt)
    :cvar PREV:
    :cvar RPLC:
    :cvar SUCC:
    """
    PREV = "PREV"
    RPLC = "RPLC"
    SUCC = "SUCC"


class XServiceEventPerformer(Enum):
    """
    abstDomain: A19601 (C-0-T10901-A19601-cpt)
    :cvar PRF:
    :cvar SPRF:
    """
    PRF = "PRF"
    SPRF = "SPRF"


class XSubstitutionConditionNoneOrUnconditional(Enum):
    """
    abstDomain: A19740 (C-0-T17719-A19740-cpt)
    :cvar NOSUB:
    :cvar UNCOND:
    """
    NOSUB = "NOSUB"
    UNCOND = "UNCOND"


class XVeryBasicConfidentialityKind(Enum):
    """
    abstDomain: A19738 (C-0-T10228-A19738-cpt)
    :cvar N:
    :cvar R:
    """
    N = "N"
    R = "R"
