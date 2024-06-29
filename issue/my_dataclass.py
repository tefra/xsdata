from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class ExternalTanyContentNode:
    class Meta:
        name = "ExternalTAnyContentNode"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTvalue:
    class Meta:
        name = "ExternalTValue"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TappliedCfo:
    class Meta:
        name = "TApplied_CFO"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Applied CFO",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TcrcFeedback:
    class Meta:
        name = "TCRC_Feedback"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="CRC Feedback",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TcellEntityId:
    class Meta:
        name = "TCellEntityId"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="CellEntityId",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TcellSetId:
    class Meta:
        name = "TCellSetId"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="CellSetId",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TdmrsOfdmSymbolIndex:
    class Meta:
        name = "TDMRS_OFDM_SymbolIndex"

    value: Optional["TdmrsOfdmSymbolIndex.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="DMRS_OFDM_SymbolIndex",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class TevmPerSymbol:
    class Meta:
        name = "TEVM_Per_Symbol"

    value: Optional["TevmPerSymbol.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="EVM Per Symbol",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class TfpgaApiVersion:
    class Meta:
        name = "TFPGA_API_Version"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="FPGA_API_Version",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TglobalTti:
    class Meta:
        name = "TGlobal_TTI"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Global TTI",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TglobalTtiToDecode:
    class Meta:
        name = "TGlobal_TTI_to_decode"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Global TTI to decode",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TharqProcess:
    class Meta:
        name = "THARQ_Process"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="HARQ Process",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TmeanEvm:
    class Meta:
        name = "TMean_EVM"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Mean EVM",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TmeanEvmPerLayer:
    class Meta:
        name = "TMean_EVM_Per_Layer"

    value: Optional["TmeanEvmPerLayer.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Mean EVM Per Layer",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class TmeasurementState:
    class Meta:
        name = "TMeasurement_State"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Measurement State",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TnumPuschOfdmDmrsSymbols:
    class Meta:
        name = "TNumPUSCH_OFDM_DMRS_Symbols"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="NumPUSCH_OFDM_DMRS_Symbols",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TnumAntennas:
    class Meta:
        name = "TNum_Antennas"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Num_Antennas",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TnumLayers:
    class Meta:
        name = "TNum_Layers"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Num Layers",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Tnumerology:
    class Meta:
        name = "TNumerology"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Numerology",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TphaseMeas:
    class Meta:
        name = "TPhase_Meas"

    value: Optional["TphaseMeas.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Phase_Meas",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class TpowerSummary:
    class Meta:
        name = "TPower_summary"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Power summary",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TrtApiVersion:
    class Meta:
        name = "TRT_API_Version"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="RT_API_Version",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Trnti:
    class Meta:
        name = "TRnti"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Rnti",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TrntiType:
    class Meta:
        name = "TRntiType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="RntiType",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TsamplingFreq:
    class Meta:
        name = "TSampling_freq"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Sampling freq",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TsymbolsFreqHop1:
    class Meta:
        name = "TSymbols_Freq_Hop__1"

    value: Optional["TsymbolsFreqHop1.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Symbols Freq Hop #1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class TsymbolsFreqHop2:
    class Meta:
        name = "TSymbols_Freq_Hop__2"

    value: Optional["TsymbolsFreqHop2.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Symbols Freq Hop #2",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Value:
        i: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class Tueid:
    class Meta:
        name = "TUEId"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="UEId",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TulCarrier:
    class Meta:
        name = "TUL_Carrier"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="UL Carrier",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TulTimingOffset:
    class Meta:
        name = "TUL_Timing_Offset"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="UL Timing Offset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Tuxmid:
    class Meta:
        name = "TUXMId"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="UXMId",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ExternalTdcLeakageMeasurement:
    class Meta:
        name = "ExternalTDcLeakageMeasurement"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="DC Leakage Measurement",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTdeltaCfo:
    class Meta:
        name = "ExternalTDeltaCfo"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    name: str = field(
        init=False,
        default="Delta CFO",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTdmrsCorrelation:
    class Meta:
        name = "ExternalTDmrsCorrelation"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 14,
        },
    )
    name: str = field(
        init=False,
        default="DMRS Correlation",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTdmrsPower:
    class Meta:
        name = "ExternalTDmrsPower"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 14,
        },
    )
    name: str = field(
        init=False,
        default="DMRS Power",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTdmrsSto:
    class Meta:
        name = "ExternalTDmrsSto"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 14,
        },
    )
    name: str = field(
        init=False,
        default="DMRS STO",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTdmrsStoPerLayer:
    class Meta:
        name = "ExternalTDmrsStoPerLayer"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="DMRS STO Per Layer",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer0Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer0Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer1Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer1Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 1",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer2Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer2Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 2",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer3Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer3Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 3",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer4Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer4Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 4",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer5Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer5Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 5",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer6Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer6Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 6",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevmLayer7Contentforvaluenodewithanyvalue:
    class Meta:
        name = "ExternalTEvm_Layer7Contentforvaluenodewithanyvalue"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    field_value: Optional[ExternalTvalue] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default="Layer 7",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna0:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna0"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna1:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna1"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 1",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna2:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna2"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 2",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna3:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna3"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 3",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna4:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna4"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 4",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna5:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna5"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 5",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna6:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna6"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 6",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurementsAntenna7:
    class Meta:
        name = "ExternalTPhaseMeasurements_Antenna7"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Antenna 7",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTpowerParametersMeanPower:
    class Meta:
        name = "ExternalTPowerParameters_MeanPower"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="Mean power",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTpowerParametersPaprDb:
    class Meta:
        name = "ExternalTPowerParameters_Papr_Db_"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="PAPR (dB)",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTtti:
    class Meta:
        name = "ExternalTTti"

    field_value: List[ExternalTvalue] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "min_occurs": 4,
            "max_occurs": 4,
        },
    )
    name: str = field(
        init=False,
        default="TTI",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTevm:
    class Meta:
        name = "ExternalTEvm"

    field_value: List[
        Union[
            ExternalTevmLayer0Contentforvaluenodewithanyvalue,
            ExternalTevmLayer1Contentforvaluenodewithanyvalue,
            ExternalTevmLayer2Contentforvaluenodewithanyvalue,
            ExternalTevmLayer3Contentforvaluenodewithanyvalue,
            ExternalTevmLayer4Contentforvaluenodewithanyvalue,
            ExternalTevmLayer5Contentforvaluenodewithanyvalue,
            ExternalTevmLayer6Contentforvaluenodewithanyvalue,
            ExternalTevmLayer7Contentforvaluenodewithanyvalue,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    name: str = field(
        init=False,
        default="EVM",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTphaseMeasurements:
    class Meta:
        name = "ExternalTPhaseMeasurements"

    field_value: List[
        Union[
            ExternalTvalue,
            ExternalTphaseMeasurementsAntenna0,
            ExternalTphaseMeasurementsAntenna1,
            ExternalTphaseMeasurementsAntenna2,
            ExternalTphaseMeasurementsAntenna3,
            ExternalTphaseMeasurementsAntenna4,
            ExternalTphaseMeasurementsAntenna5,
            ExternalTphaseMeasurementsAntenna6,
            ExternalTphaseMeasurementsAntenna7,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 10,
        },
    )
    name: str = field(
        init=False,
        default="Phase Measurements",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalTpowerParameters:
    class Meta:
        name = "ExternalTPowerParameters"

    field_value: List[
        Union[
            ExternalTpowerParametersMeanPower, ExternalTpowerParametersPaprDb
        ]
    ] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    name: str = field(
        init=False,
        default="Power parameters",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LogRecord:
    summary: Optional[str] = field(
        default=None,
        metadata={
            "name": "Summary",
            "type": "Element",
            "required": True,
        },
    )
    frame: Optional[int] = field(
        default=None,
        metadata={
            "name": "Frame",
            "type": "Element",
            "required": True,
        },
    )
    field_value: List[
        Union[
            TrtApiVersion,
            TfpgaApiVersion,
            Tuxmid,
            TcellSetId,
            TulCarrier,
            TcellEntityId,
            Tueid,
            TglobalTti,
            TglobalTtiToDecode,
            ExternalTtti,
            Tnumerology,
            TrntiType,
            Trnti,
            TsamplingFreq,
            TmeasurementState,
            TharqProcess,
            TsymbolsFreqHop1,
            TsymbolsFreqHop2,
            TmeanEvm,
            TmeanEvmPerLayer,
            TevmPerSymbol,
            ExternalTevm,
            TnumPuschOfdmDmrsSymbols,
            TdmrsOfdmSymbolIndex,
            ExternalTdmrsSto,
            TnumLayers,
            ExternalTdmrsStoPerLayer,
            ExternalTdmrsPower,
            ExternalTdmrsCorrelation,
            TnumAntennas,
            ExternalTpowerParameters,
            ExternalTdcLeakageMeasurement,
            TpowerSummary,
            TcrcFeedback,
            TappliedCfo,
            ExternalTdeltaCfo,
            TulTimingOffset,
            TphaseMeas,
            ExternalTphaseMeasurements,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "min_occurs": 33,
            "max_occurs": 39,
        },
    )
    schema: str = field(
        init=False,
        default="1.0.2.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
