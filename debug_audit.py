import psycopg2
import csv
import argparse
import json
from datetime import datetime
data = [
    {
        "Table": "L_AdmissionControl",
        "Column": "dlTransNwBandwidth",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "ulTransNwBandwidth",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "paArpOverride",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "resourceReservationForPAState",
        "Column_Golden_Value": "ACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "nrOfRbReservationsPerPaConn",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "admNrRrcDifferentiationThr",
        "Column_Golden_Value": "750",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "dlAdmDifferentiationThr",
        "Column_Golden_Value": "500",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "dlAdmOverloadThr",
        "Column_Golden_Value": "950",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "nrOfPaConnReservationsPerCell",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "ulAdmDifferentiationThr",
        "Column_Golden_Value": "500",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "ulAdmOverloadThr",
        "Column_Golden_Value": "950",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "arpBasedPreEmptionState",
        "Column_Golden_Value": "DEACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_AnrFunctionEUtran",
        "Column": "anrIntraFreqState",
        "Column_Golden_Value": "ACTIVATED"
    },
    {
        "Table": "L_AnrFunctionEUtran",
        "Column": "cellAddRsrpThresholdEutran",
        "Column_Golden_Value": "-980"
    },
    {
        "Table": "L_AnrFunctionEUtran",
        "Column": "hoAllowedEutranPolicy",
        "Column_Golden_Value": "TRUE"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "drxInactivityTimer",
        "Column_Golden_Value": "PSF4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "drxRetransmissionTimer",
        "Column_Golden_Value": "PSF8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "longDrxCycle",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "longDrxCycleOnly",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "shortDrxCycle",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "onDurationTimer",
        "Column_Golden_Value": "PSF4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "drxInactivityTimer",
        "Column_Golden_Value": "PSF100"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "drxRetransmissionTimer",
        "Column_Golden_Value": "PSF2"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "longDrxCycle",
        "Column_Golden_Value": "SF320"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "longDrxCycleOnly",
        "Column_Golden_Value": "SF320"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "shortDrxCycle",
        "Column_Golden_Value": "SF20"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "onDurationTimer",
        "Column_Golden_Value": "PSF2"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "shortDrxCycleTimer",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_DrxProfile",
        "Column": "shortDrxCycleTimer",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalPlmnReservedList",
        "Column_Golden_Value": '["\"false\"- \"false\"- \"false\"- \"false\"- \"false\"]'
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellRange",
        "Column_Golden_Value": "9"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB1",
        "Column_Golden_Value": "TRUE"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB2",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB3",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB4",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB5",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB6",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB7",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB8",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "5000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Barbados",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "5000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Cayman",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Bahamas"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Anguilla"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "TCI"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BVI",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Cayman",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Antigua",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Barbados",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "15000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BVI",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "20000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Antigua",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Carrier",
        "Condition_Table_2_Column_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "20000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Jamaica"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlConfigurableFrequencyStart",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlFrequencyAllocationProportion",
        "Column_Golden_Value": "100"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "drxActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "minBestCellHoAttempts",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "noConsecutiveSubframes",
        "Column_Golden_Value": "SF1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pMaxServingCell",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "prsPeriod",
        "Column_Golden_Value": "PP160"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pZeroNominalPucch",
        "Column_Golden_Value": "-116"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pZeroNominalPusch",
        "Column_Golden_Value": "-106"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qQualMin",
        "Column_Golden_Value": "-18"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "SIB3_sIntraSearch",
        "Column_Golden_Value": "62"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "5000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "5000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "15000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulSrsEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchPowerBoostMax",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "noOfPucchCqiUsers",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "noOfPucchSrUsers",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "covTriggerdBlindHoAllowed",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Cayman"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdschTypeBGain",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "20000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "30000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "40000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Dominica"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMinOffset",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band "
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "6"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "25",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'10\'-\'66\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "4"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "26",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "5"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'17\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "12"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'12\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "17"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalSpectrumEmissionValues",
        "Column_Golden_Value": "NS_01"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dl256QamEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ul64qamEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "rateShapingActive",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCovImproveQci1",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCovImproveSrb",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchCovImproveDtx",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ttiBundlingAfterHo",
        "Column_Golden_Value": "TTI_BUNDLING_ALL_HO_CASES",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ttiBundlingAfterReest",
        "Column_Golden_Value": "TTI_BUNDLING_ALL_REEST_CASES",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ttiBundlingSwitchThres",
        "Column_Golden_Value": "90",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ttiBundlingSwitchThresHyst",
        "Column_Golden_Value": "10",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "transmissionMode",
        "Column_Golden_Value": "TRANSMISSION_MODE_4"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mobCtrlAtPoorCovActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-122",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-122",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellCapMaxCellSubCap",
        "Column_Golden_Value": "100000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellCapMinCellSubCap",
        "Column_Golden_Value": "1000"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "cellCapMinMaxWriProt",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB6",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB7",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB8",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB10",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB12",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulBlerTargetEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulHarqVolteBlerTarget",
        "Column_Golden_Value": 0.02,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "srvccDelayTimer",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "tReorderingAutoConfiguration",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "enableServiceSpecificHARQ",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "sCellHandlingAtVolteCall",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "moVoiceDynUeAdmCtrlPrio",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "ulHarqVolteBlerTarget",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "pdcchTargetBlerVolte",
        "Column_Golden_Value": "6"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "blerTargetConfigEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB3",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB4",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB5",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB11",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB13",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB15",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB16",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI1",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI2",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI3",
        "Column_Golden_Value": "32"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI4",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI5",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI6",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI7",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI8",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI9",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "siPeriodicitySI10",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "dlInterferenceManagementActive",
        "Column_Golden_Value": "TRUE"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "tReorderingAutoConfiguration",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "harqOffsetDl",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "harqOffsetUl",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellRelation",
        "Column": "loadBalancing",
        "Column_Golden_Value": "ALLOWED"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Carrier",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "mobilityAction",
        "Column_Golden_Value": "HANDOVER"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "pMax",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "presenceAntennaPort1",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qQualMin",
        "Column_Golden_Value": "-34"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "threshXHigh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Carrier",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "CWP"
    },
    {
        "Table": "L_EUtranFreqRelation",
        "Column": "voicePrio",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "25",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'10\'-\'66\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "4"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "26",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "5"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'17\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "12"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'12\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "17"
    },
    {
        "Table": "L_ExternalUtranCellFDD",
        "Column": "srvccCapability",
        "Column_Golden_Value": "PS_AND_CS_SUPPORTED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_MACConfiguration",
        "Column": "ulTtiBundlingMaxHARQTx",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_Paging",
        "Column": "nB",
        "Column_Golden_Value": "T"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "1400"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "3000"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci2"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci3"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci4"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rohcEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "VOIP",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci2",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci3",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci4",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "HI_PRIO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "aqmMode",
        "Column_Golden_Value": "MODE2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "aqmMode",
        "Column_Golden_Value": "OFF",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "drxPriority",
        "Column_Golden_Value": "98",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "drxPriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "counterActiveMode",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "inactivityTimerOffset",
        "Column_Golden_Value": "20",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdb",
        "Column_Golden_Value": "80",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdb",
        "Column_Golden_Value": "100",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdbOffset",
        "Column_Golden_Value": "50",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "priority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "priority",
        "Column_Golden_Value": "2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "resourceType",
        "Column_Golden_Value": "GBR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "resourceType",
        "Column_Golden_Value": "NON_GBR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rlcMode",
        "Column_Golden_Value": "UM",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rlcMode",
        "Column_Golden_Value": "AM",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "DELAY_BASED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "VOIP",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "IMS_SIGNALING",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    
    {
        "Table": "L_RlfProfile",
        "Column": "rlfProfileId",
        "Column_Golden_Value": "RlfProfile=1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "measReportConfigParams_a1ThresholdRsrpPrimOffset",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "measReportConfigParams_a2ThresholdRsrpPrimOffset",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "measReportConfigParams_b2Threshold1RsrpUtraOffset",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "bitRateRecommendationEnabled",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlMaxHARQTxQci",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "ulMaxHARQTxQci",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "harqPriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlMinBitRate",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdbOffset",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdcpSNLength",
        "Column_Golden_Value": "12",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "pdcpSNLength",
        "Column_Golden_Value": "12",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciACTuning",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciACTuning",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "20",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "resourceAllocationStrategy",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rlcSNLength",
        "Column_Golden_Value": "10",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rlfPriority",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "rohcEnabled",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "srsAllocationStrategy",
        "Column_Golden_Value": "DEACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "tReorderingDl",
        "Column_Golden_Value": "35",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "tReorderingUl",
        "Column_Golden_Value": "35",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "ulMinBitRate",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci6"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci7"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci8"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci9"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "hysteresisA1Prim",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "timeToTriggerA1Prim",
        "Column_Golden_Value": "640"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-106",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-109"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "timeToTriggerA5",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow "
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-109",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-108"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "hysteresisB2",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "timeToTriggerB2",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "triggerQuantityB2",
        "Column_Golden_Value": "RSRP"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-117",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Suburban"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": " Rural "
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-119",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-119",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-121",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-121",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-104"
    },
    {
        "Table": "L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "freqBand",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "hysteresisA2Prim",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "timeToTriggerA2Prim",
        "Column_Golden_Value": "640"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "triggerQuantityA2Prim",
        "Column_Golden_Value": "RSRP"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "hysteresisA2Prim",
        "Column_Golden_Value": "10",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": " Rural "
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Suburban"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": " Rural "
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "inhibitA2SearchConfig",
        "Column_Golden_Value": "INHIBIT_A2SEARCH_RSRQ"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-123",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-125",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq band"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-123",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-125",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq band"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "timeToTriggerA2Critical",
        "Column_Golden_Value": "512"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a2CriticalThrQci1RsrpOffset",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "FLOW"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-113",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrq",
        "Column_Golden_Value": "-195"
    },
    {
        "Table": "L_RlfProfile",
        "Column": "t311",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_RlfProfile",
        "Condition_Table_1_Column": "rlfProfileId",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "L_RlfProfile",
        "Column": "t301",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_RlfProfile",
        "Condition_Table_1_Column": "rlfProfileId",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "L_SectorCarrier",
        "Column": "noOfRxAntennas",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_SectorCarrier",
        "Column": "noOfTxAntennas",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_SectorCarrier",
        "Column": "radioTransmitPerfMode",
        "Column_Golden_Value": "COVERAGE_GREEN",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "dl256QamEnabled",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "csFallbackPrio",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "csFallbackPrioEC",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "mobilityAction",
        "Column_Golden_Value": "HANDOVER"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "mobilityActionCsfb",
        "Column_Golden_Value": "RELEASE_WITH_REDIRECT_NACC"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "pMaxUtra",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qQualMin",
        "Column_Golden_Value": "-18"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXHigh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Suburban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": " Rural "
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "threshXLowQ",
        "Column_Golden_Value": "31",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "voicePrio",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115"
    },
    {
        "Table": "L_AnrFunction",
        "Column": "removeNenbTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AnrFunction",
        "Column": "removeNrelTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AnrFunction",
        "Column": "removeNcellTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AnrFunction",
        "Column": "cellRelHoAttRateThreshold",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "L_AnrFunctionUtran",
        "Column": "anrStateUtran",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AnrFunctionUtran",
        "Column": "anrUtranAcMeasOn",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AnrFunctionUtran",
        "Column": "cellAddRscpThresholdUtranDelta",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_AnrFunctionUtran",
        "Column": "hoAllowedUtranPolicy",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_AutoCellCapEstFunction",
        "Column": "useEstimatedCellCap",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "80"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "L_DataRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "dnsLookupOnTai",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "nnsfMode",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "rrcConnReestActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "initPreschedulingEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "s1GtpuEchoEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_ENodeBFunction",
        "Column": "x2GtpuEchoEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_LoadBalancingFunction",
        "Column": "lbThreshold",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "L_LoadBalancingFunction",
        "Column": "lbCeiling",
        "Column_Golden_Value": "200"
    },
    {
        "Table": "L_PreschedulingProfile",
        "Column": "preschedulingPeriod",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_PreschedulingProfile",
        "Column": "preschedulingDataSize",
        "Column_Golden_Value": "86"
    },
    {
        "Table": "L_PreschedulingProfile",
        "Column": "preschedulingDuration",
        "Column_Golden_Value": "200"
    },
    {
        "Table": "L_ReportConfigEUtraBestCell",
        "Column": "a3offset",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "L_ReportConfigEUtraBestCell",
        "Column": "hysteresisA3",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "L_ReportConfigEUtraBestCell",
        "Column": "timeToTriggerA3",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "L_ReportConfigEUtraBestCell",
        "Column": "triggerQuantityA3",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_ReportConfigEUtraBestCellAnr",
        "Column": "timeToTriggerA3",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "L_ReportConfigEUtraInterFreqLb",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-44"
    },
    {
        "Table": "L_ReportConfigEUtraInterFreqLb",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-110"
    },
    {
        "Table": "L_RfBranch",
        "Column": "dlAttenuation",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_RfBranch",
        "Column": "ulAttenuation",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_RfPort",
        "Column": "vswrSupervisionSensitivity",
        "Column_Golden_Value": "100"
    },
    {
        "Table": "L_RfPort",
        "Column": "vswrSupervisionActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_Rrc",
        "Column": "tRrcConnectionReconfiguration",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "80"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "L_SignalingRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "subscriberGroupProfileId",
        "Column_Golden_Value": "VoLTE"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "profilePriority",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "spidTriggerList",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "customTriggerType",
        "Column_Golden_Value": "TRIGGER_NOT_USED"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "bearerTriggerList_qci",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "bearerTriggerList_arp",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "ulHarqBlerTarget",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "dlHarqBlerTarget",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "groupExtendInactAfterVolteRel",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "drxMode",
        "Column_Golden_Value": "DISABLE_DRX"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "pZeroNominalPucchOffset",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "pZeroNominalPuschOffset",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "subGroupConfiguration6",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "ulMcsLowerLimit",
        "Column_Golden_Value": "-1"
    },
    {
        "Table": "L_SubscriberGroupProfile",
        "Column": "ulMcsUpperLimit",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "a5B2MobilityTimer",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "filterCoefficientEUtraRsrp",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "filterCoefficientEUtraRsrq",
        "Column_Golden_Value": "11"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "measQuantityUtraFDD",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "sMeasure",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActiveCDMA2000",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "bothA5RsrpRsrqCheck",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "inhibitB2RsrqConfig",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "lowPrioMeasThresh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "excludeInterFreqAtCritical",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActiveIF",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActiveUTRAN",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActiveGERAN",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "L_UeMeasControl",
        "Column": "ueMeasurementsActiveCDMA2000",
        "Column_Golden_Value": "0"
    }
]

# Function to establish database connection
# def connect_to_db():
#     try:
#         connection = psycopg2.connect(user="gpuser",
#                                       password="gpuser@123",
#                                       host="192.168.4.127",
#                                       port="5432",
#                                       database="UniversalNetworkDataHubEH_Jamaica")
#         cursor = connection.cursor()
#         return connection, cursor
#     except psycopg2.OperationalError as e:
#         print(f"Error: {e}")
#         return None, None

# # Function to execute SQL query and fetch results
# def execute_query(cursor, query):
#     try:
#         cursor.execute(query)
#         return cursor.fetchall(), None
#     except psycopg2.Error as e:
#         cursor.connection.rollback()  # Rollback the transaction to clear the error
#         error_message = str(e)
#         return [], error_message

# # Function to write results to CSV file
# def write_to_csv(results):
#     try:
#         with open('debug_audit_results.csv', mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Level', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
#             writer.writerows(results)
#     except IOError as e:
#         print(f"Error writing to CSV: {e}")

# # Function to write errors to a log file
# def write_to_log(errors):
#     try:
#         with open('query_errors.log', mode='w') as file:
#             for error in errors:
#                 file.write(f"Query: {error['query']}Error: {error['error_message']}")
#     except IOError as e:
#         print(f"Error writing to log file: {e}")

# # Function to construct SQL query based on conditions
# def construct_query(table, entry, timestamp, sites):
#     try:
#         conditions = []
#         if 'Join_Column' in entry:
#             for i in range(1, 4):
#                 condition_table = entry.get(f"Condition_Table_{i}")
#                 condition_column = entry.get(f"Condition_Table_{i}_Column")
#                 condition_value = entry.get(f"Condition_Table_{i}_Column_Value")
#                 if condition_table and condition_column and condition_value:
#                     conditions.append((condition_table, condition_column, condition_value))

#         query = f'SELECT "dbo"."{table}"."Level", "dbo"."{table}"."{entry["Column"]}" FROM "dbo"."{table}"'
        
#         if conditions:
#             for i, (condition_table, condition_column, condition_value) in enumerate(conditions):
#                 query += f'''
#                 JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND ct{i}."{condition_column}" = '{condition_value}'
#                 '''
#         return query
#     except KeyError as e:
#         print(f"KeyError: {e}")
#         return None

# def main():
#     parser = argparse.ArgumentParser(description='Database Golden Value Audit Script')
#     parser.add_argument('--tables', type=str, default='["all"]', help='List of tables in the form ["table1", "table2", ...] or ["all"]')
#     parser.add_argument('--columns', type=str, default='["all"]', help='List of columns in the form ["column1", "column2", ...] or ["all"]')
#     parser.add_argument('--timestamp', type=str, default=None, help='Timestamp value')
#     parser.add_argument('--site', type=str, default='["all"]', help='List of sites in the form ["site1", "site2", ...] or ["all"]')
#     args = parser.parse_args()

#     tables = json.loads(args.tables)
#     columns = json.loads(args.columns)
#     sites = json.loads(args.site)
#     timestamp = args.timestamp

#     # Validate input
#     if tables == ["all"] and (columns != ["all"] or timestamp is not None or sites != ["all"]):
#         print("Error: If --tables is 'all', other options must also be 'all'")
#         return

#     if columns != ["all"] and not all(isinstance(column, str) for column in columns):
#         print("Error: --columns argument must be a list of strings")
#         return

#     # Connect to the database
#     connection, cursor = connect_to_db()
#     if connection is None or cursor is None:
#         return

#     all_tables = {entry["Table"] for entry in data} if tables == ["all"] else set(tables)

#     audit_results = []
#     query_errors = []

#     # Iterate over each table and column
#     for table in all_tables:
#         for entry in data:
#             if entry["Table"] == table or table == "all":
#                 query = construct_query(table, entry, timestamp, sites)
#                 if query is not None:
#                     results, error_message = execute_query(cursor, query)
#                     if error_message:
#                         query_errors.append({"query": query, "error_message": error_message})
#                     if results:
#                         for result in results:
#                             level = result[0]
#                             current_value = result[1]
#                             if entry["Column_Golden_Value"] != current_value:
#                                 audit_results.append([level, table, entry["Column"], entry["Column_Golden_Value"], current_value])
#                     else:
#                         print(f"No data found for table '{table}'")

#     # Write the collected results to CSV
#     write_to_csv(audit_results)

#     # Write the error logs to a file
#     if query_errors:
#         write_to_log(query_errors)

#     # Close the database connection
#     if connection is not None:
#         cursor.close()
#         connection.close()

#--------------------------------above code is right ---------------------------------------------------

#------------------------------- here code also return table and columns list which are not exist in db--------------------------------------


def connect_to_db():
    try:
        connection = psycopg2.connect(user="gpuser",
                                      password="gpuser@123",
                                      host="192.168.4.127",
                                      port="5432",
                                      database="UniversalNetworkDataHubEH_Jamaica")
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        return None, None

# Function to execute SQL query and fetch results
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall(), None
    except psycopg2.Error as e:
        cursor.connection.rollback()  # Rollback the transaction to clear the error
        error_message = str(e)
        return [], error_message

# Function to check if a table exists in the database
def check_table_exists(cursor, table_name):
    query = f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}');"
    result, error = execute_query(cursor, query)
    if error:
        return False, error
    return result[0][0], None

# Function to check if a column exists in a table
def check_column_exists(cursor, table_name, column_name):
    query = f"SELECT EXISTS (SELECT FROM information_schema.columns WHERE table_name = '{table_name}' AND column_name = '{column_name}');"
    result, error = execute_query(cursor, query)
    if error:
        return False, error
    return result[0][0], None

# Function to write results to CSV file
def write_to_csv(results):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'debug_audit_results_{timestamp}.csv'
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Level', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
            writer.writerows(results)
    except IOError as e:
        print(f"Error writing to CSV: {e}")

# Function to write errors to a log file with timestamp
def write_to_log(errors):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'query_errors_{timestamp}.log'
    try:
        with open(filename, mode='w') as file:
            for error in errors:
                file.write(f"Query: {error['query']} Error: {error['error_message']}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

# Function to write missing tables and columns to a log file with timestamp
def write_missing_to_log(missing_tables, missing_columns):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'missing_tables_columns_{timestamp}.log'
    try:
        with open(filename, mode='w') as file:
            if missing_tables:
                file.write("Missing Tables:\n")
                for table in missing_tables:
                    file.write(f"{table}\n")
            if missing_columns:
                file.write("\nMissing Columns:\n")
                for table, column in missing_columns:
                    file.write(f"Table: {table}, Column: {column}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

# Function to construct SQL query based on conditions
def construct_query(table, entry, timestamp, sites):
    try:
        conditions = []
        if 'Join_Column' in entry:
            for i in range(1, 4):
                condition_table = entry.get(f"Condition_Table_{i}")
                condition_column = entry.get(f"Condition_Table_{i}_Column")
                condition_value = entry.get(f"Condition_Table_{i}_Column_Value")
                if condition_table and condition_column and condition_value:
                    conditions.append((condition_table, condition_column, condition_value))

        query = f'SELECT "dbo"."{table}"."Level", "dbo"."{table}"."{entry["Column"]}" FROM "dbo"."{table}"'
        
        if conditions:
            for i, (condition_table, condition_column, condition_value) in enumerate(conditions):
                query += f'''
                JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND ct{i}."{condition_column}" = '{condition_value}'
                '''
        return query
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Database Golden Value Audit Script')
    parser.add_argument('--tables', type=str, default='["all"]', help='List of tables in the form ["table1", "table2", ...] or ["all"]')
    parser.add_argument('--columns', type=str, default='["all"]', help='List of columns in the form ["column1", "column2", ...] or ["all"]')
    parser.add_argument('--timestamp', type=str, default=None, help='Timestamp value')
    parser.add_argument('--site', type=str, default='["all"]', help='List of sites in the form ["site1", "site2", ...] or ["all"]')
    args = parser.parse_args()

    tables = json.loads(args.tables)
    columns = json.loads(args.columns)
    sites = json.loads(args.site)
    timestamp = args.timestamp

    # Validate input
    if tables == ["all"] and (columns != ["all"] or timestamp is not None or sites != ["all"]):
        print("Error: If --tables is 'all', other options must also be 'all'")
        return

    if columns != ["all"] and not all(isinstance(column, str) for column in columns):
        print("Error: --columns argument must be a list of strings")
        return

    # Connect to the database
    connection, cursor = connect_to_db()
    if connection is None or cursor is None:
        return

    all_tables = {entry["Table"] for entry in data} if tables == ["all"] else set(tables)

    audit_results = []
    query_errors = []
    missing_tables = []
    missing_columns = []

    # Iterate over each table and column
    for table in all_tables:
        table_exists, error = check_table_exists(cursor, table)
        if error:
            query_errors.append({"query": f"Check table {table}", "error_message": error})
            continue
        if not table_exists:
            missing_tables.append(table)
            continue

        for entry in data:
            if entry["Table"] == table or table == "all":
                column_exists, error = check_column_exists(cursor, table, entry["Column"])
                if error:
                    query_errors.append({"query": f"Check column {entry['Column']} in table {table}", "error_message": error})
                    continue
                if not column_exists:
                    missing_columns.append((table, entry["Column"]))
                    continue

                query = construct_query(table, entry, timestamp, sites)
                if query is not None:
                    results, error_message = execute_query(cursor, query)
                    if error_message:
                        query_errors.append({"query": query, "error_message": error_message})
                    if results:
                        for result in results:
                            level = result[0]
                            current_value = result[1]
                            if entry["Column_Golden_Value"] != current_value:
                                audit_results.append([level, table, entry["Column"], entry["Column_Golden_Value"], current_value])
                    else:
                        print(f"No data found for table '{table}'")

    # Write the collected results to CSV
    write_to_csv(audit_results)

    # Write the error logs to a file
    if query_errors:
        write_to_log(query_errors)

    # Write the missing tables and columns to a log file
    if missing_tables or missing_columns:
        write_missing_to_log(missing_tables, missing_columns)

    # Close the database connection
    if connection is not None:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()