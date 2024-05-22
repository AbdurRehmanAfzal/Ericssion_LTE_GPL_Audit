import psycopg2
import csv
import argparse
import json
import os
from datetime import datetime
data = [
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "dlTransNwBandwidth",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "ulTransNwBandwidth",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "paArpOverride",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "resourceReservationForPAState",
        "Column_Golden_Value": "ACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "nrOfRbReservationsPerPaConn",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "admNrRrcDifferentiationThr",
        "Column_Golden_Value": "750",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "dlAdmDifferentiationThr",
        "Column_Golden_Value": "500",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "dlAdmOverloadThr",
        "Column_Golden_Value": "950",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "nrOfPaConnReservationsPerCell",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "ulAdmDifferentiationThr",
        "Column_Golden_Value": "500",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "ulAdmOverloadThr",
        "Column_Golden_Value": "950",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "arpBasedPreEmptionState",
        "Column_Golden_Value": "DEACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_AnrFunctionEUtran",
        "Column": "anrIntraFreqState",
        "Column_Golden_Value": "ACTIVATED"
    },
    {
        "Table": "ER_L_AnrFunctionEUtran",
        "Column": "cellAddRsrpThresholdEutran",
        "Column_Golden_Value": "-980"
    },
    {
        "Table": "ER_L_AnrFunctionEUtran",
        "Column": "hoAllowedEutranPolicy",
        "Column_Golden_Value": "TRUE "
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "drxInactivityTimer",
        "Column_Golden_Value": "PSF4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "drxRetransmissionTimer",
        "Column_Golden_Value": "PSF8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "longDrxCycle",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "longDrxCycleOnly",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "shortDrxCycle",
        "Column_Golden_Value": "SF40",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "onDurationTimer",
        "Column_Golden_Value": "PSF4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "drxInactivityTimer",
        "Column_Golden_Value": "PSF100"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "drxRetransmissionTimer",
        "Column_Golden_Value": "PSF2"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "longDrxCycle",
        "Column_Golden_Value": "SF320"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "longDrxCycleOnly",
        "Column_Golden_Value": "SF320"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "shortDrxCycle",
        "Column_Golden_Value": "SF20"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "onDurationTimer",
        "Column_Golden_Value": "PSF2"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "shortDrxCycleTimer",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_DrxProfile",
        "Column": "shortDrxCycleTimer",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalPlmnReservedList",
        "Column_Golden_Value": '["\"false\"- \"false\"- \"false\"- \"false\"- \"false\"]'
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellRange",
        "Column_Golden_Value": "9"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB1",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB2",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB3",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB4",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB5",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB6",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB7",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "changeNotification_changeNotificationSIB8",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Bahamas"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Anguilla"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "TCI"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
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
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlChannelBandwidth",
        "Column_Golden_Value": "20000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Jamaica"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlConfigurableFrequencyStart",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlFrequencyAllocationProportion",
        "Column_Golden_Value": "100"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "drxActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "minBestCellHoAttempts",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "noConsecutiveSubframes",
        "Column_Golden_Value": "SF1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCfiMode",
        "Column_Golden_Value": "CFI_AUTO_MAXIMUM_2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": " L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pMaxServingCell",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "prsPeriod",
        "Column_Golden_Value": "PP160"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pZeroNominalPucch",
        "Column_Golden_Value": "-116"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pZeroNominalPusch",
        "Column_Golden_Value": "-106"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qQualMin",
        "Column_Golden_Value": "-18"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "SIB3_sIntraSearch",
        "Column_Golden_Value": "62"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "5000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "5000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "15000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulChannelBandwidth",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulSrsEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchPowerBoostMax",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "noOfPucchCqiUsers",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "noOfPucchSrUsers",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "covTriggerdBlindHoAllowed",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Cayman"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdschTypeBGain",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "20000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "30000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellSubscriptionCapacity",
        "Column_Golden_Value": "40000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Dominica"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMinOffset",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "threshServingLow",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band "
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "SIB3_sNonIntraSearch",
        "Column_Golden_Value": "6"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "25",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'10\'-\'66\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "4"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "26",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "5"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'17\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "12"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'12\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "17"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalSpectrumEmissionValues",
        "Column_Golden_Value": "NS_01"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dl256QamEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ul64qamEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "rateShapingActive",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCovImproveQci1",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCovImproveSrb",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchCovImproveDtx",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ttiBundlingAfterHo",
        "Column_Golden_Value": "TTI_BUNDLING_ALL_HO_CASES",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ttiBundlingAfterReest",
        "Column_Golden_Value": "TTI_BUNDLING_ALL_REEST_CASES",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ttiBundlingSwitchThres",
        "Column_Golden_Value": "90",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ttiBundlingSwitchThresHyst",
        "Column_Golden_Value": "10",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "transmissionMode",
        "Column_Golden_Value": "TRANSMISSION_MODE_4"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mobCtrlAtPoorCovActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-122",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-122",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellCapMaxCellSubCap",
        "Column_Golden_Value": "100000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellCapMinCellSubCap",
        "Column_Golden_Value": "1000"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "cellCapMinMaxWriProt",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB6",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB7",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB8",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB10",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB12",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulBlerTargetEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulHarqVolteBlerTarget",
        "Column_Golden_Value": 0.02,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "srvccDelayTimer",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "tReorderingAutoConfiguration",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "enableServiceSpecificHARQ",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "sCellHandlingAtVolteCall",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "moVoiceDynUeAdmCtrlPrio",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "ulHarqVolteBlerTarget",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "pdcchTargetBlerVolte",
        "Column_Golden_Value": "6"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "blerTargetConfigEnabled",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB3",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB4",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB5",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB11",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB13",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB15",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "mappingInfo_mappingInfoSIB16",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI1",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI2",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI3",
        "Column_Golden_Value": "32"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI4",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI5",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI6",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI7",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI8",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI9",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "siPeriodicitySI10",
        "Column_Golden_Value": "64"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "dlInterferenceManagementActive",
        "Column_Golden_Value": "TRUE "
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "tReorderingAutoConfiguration",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "harqOffsetDl",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "harqOffsetUl",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellRelation",
        "Column": "loadBalancing",
        "Column_Golden_Value": "ALLOWED"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Carrier",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "mobilityAction",
        "Column_Golden_Value": "HANDOVER"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "pMax",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "presenceAntennaPort1",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qQualMin",
        "Column_Golden_Value": "-34"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "threshXHigh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Carrier",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "CWP"
    },
    {
        "Table": "ER_L_EUtranFreqRelation",
        "Column": "voicePrio",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "25",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "2"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'10\'-\'66\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "4"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "26",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "5"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'17\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "12"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "additionalFreqBandList",
        "Column_Golden_Value": "[\'12\'-\'85\']",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "17"
    },
    {
        "Table": "ER_L_ExternalUtranCellFDD",
        "Column": "srvccCapability",
        "Column_Golden_Value": "PS_AND_CS_SUPPORTED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_MACConfiguration",
        "Column": "ulTtiBundlingMaxHARQTx",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "nB",
        "Column_Golden_Value": "T"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "1400"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "4",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "3000"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "5000"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "10000"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "15000"
    },
    {
        "Table": "ER_L_Paging",
        "Column": "maxNoOfPagingRecords",
        "Column_Golden_Value": "16",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dlChannelBandwidth",
        "Condition_Table_1_Column_Value": "20000"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci2"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci3"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci4"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dataFwdPerQciEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rohcEnabled",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "VOIP",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "default",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci2",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci3",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci4",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "HI_PRIO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "absPrioOverride",
        "Column_Golden_Value": "NO_OVERRIDE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "FREQUENCY_SELECTIVE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "PROPORTIONAL_FAIR_LOW",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "6",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci8"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci9"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "aqmMode",
        "Column_Golden_Value": "MODE2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "aqmMode",
        "Column_Golden_Value": "OFF",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci5",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "drxPriority",
        "Column_Golden_Value": "98",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "drxPriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "counterActiveMode",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "inactivityTimerOffset",
        "Column_Golden_Value": "20",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdb",
        "Column_Golden_Value": "80",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdb",
        "Column_Golden_Value": "100",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdbOffset",
        "Column_Golden_Value": "50",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "priority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "priority",
        "Column_Golden_Value": "2",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "resourceType",
        "Column_Golden_Value": "GBR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "resourceType",
        "Column_Golden_Value": "NON_GBR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlcMode",
        "Column_Golden_Value": "UM",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlcMode",
        "Column_Golden_Value": "AM",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "DELAY_BASED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "schedulingAlgorithm",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "VOIP",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "serviceType",
        "Column_Golden_Value": "IMS_SIGNALING",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    
    {
        "Table": "ER_L_RlfProfile",
        "Column": "rlfProfileId",
        "Column_Golden_Value": "RlfProfile=1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "measReportConfigParams_a1ThresholdRsrpPrimOffset",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "measReportConfigParams_a2ThresholdRsrpPrimOffset",
        "Column_Golden_Value": "3",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "measReportConfigParams_b2Threshold1RsrpUtraOffset",
        "Column_Golden_Value": "5",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "bitRateRecommendationEnabled",
        "Column_Golden_Value": "TRUE",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlMaxHARQTxQci",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "ulMaxHARQTxQci",
        "Column_Golden_Value": "7",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "harqPriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciTable",
        "Condition_Table_1_Column": "qciTableId",
        "Condition_Table_1_Column_Value": "default",
        "Condition_Table_2": "ER_L_QciProfilePredefined",
        "Condition_Table_2_Column": "qciProfilePredefinedId",
        "Condition_Table_2_Column_Value": "qci1",
        "Condition_Table_3": "Dimensions",
        "Condition_Table_3_Column": "Market",
        "Condition_Table_3_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlMinBitRate",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdbOffset",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdcpSNLength",
        "Column_Golden_Value": "12",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "pdcpSNLength",
        "Column_Golden_Value": "12",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciACTuning",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciACTuning",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "20",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "relativePriority",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "resourceAllocationStrategy",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "dlResourceAllocationStrategy",
        "Column_Golden_Value": "RESOURCE_FAIR",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlcSNLength",
        "Column_Golden_Value": "10",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfPriority",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rohcEnabled",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "srsAllocationStrategy",
        "Column_Golden_Value": "DEACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "tReorderingDl",
        "Column_Golden_Value": "35",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "tReorderingUl",
        "Column_Golden_Value": "35",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "ulMinBitRate",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci8"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "200",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci9"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "hysteresisA1Prim",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "timeToTriggerA1Prim",
        "Column_Golden_Value": "640"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA1Prim",
        "Column": "a1ThresholdRsrpPrim",
        "Column_Golden_Value": "-106",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-109"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-114",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "timeToTriggerA5",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow "
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-116",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-109",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "ER_L_ReportConfigA5",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-108"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "hysteresisB2",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "timeToTriggerB2",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "triggerQuantityB2",
        "Column_Golden_Value": "RSRP"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
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
        "Table": "ER_L_ReportConfigB2Utra",
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
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-112",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-119",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-119",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-121",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-121",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "btc",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold2RscpUtra",
        "Column_Golden_Value": "-104"
    },
    {
        "Table": "ER_L_ReportConfigB2Utra",
        "Column": "b2Threshold1Rsrp",
        "Column_Golden_Value": "-124",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "freqBand",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "hysteresisA2Prim",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "timeToTriggerA2Prim",
        "Column_Golden_Value": "640"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "triggerQuantityA2Prim",
        "Column_Golden_Value": "RSRP"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
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
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
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
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
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
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBadCovPrim",
        "Column": "a2ThresholdRsrpPrim",
        "Column_Golden_Value": "-108",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "inhibitA2SearchConfig",
        "Column_Golden_Value": "INHIBIT_A2SEARCH_RSRQ"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-123",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-125",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq band"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-123",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "Low Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-125",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Flow",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq band"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "2"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThresholdRsrp",
        "Column_Golden_Value": "-118",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "4"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "timeToTriggerA2Critical",
        "Column_Golden_Value": "512"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a2CriticalThrQci1RsrpOffset",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "FLOW"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "BTC"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-113",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "12 OR 17"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrp",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama",
        "Condition_Table_2": "ER_L_EUtranCellFDD",
        "Condition_Table_2_Column": "freqBand",
        "Condition_Table_2_Column_Value": "High Freq Band"
    },
    {
        "Table": "ER_L_ReportConfigSearch",
        "Column": "a1a2SearchThresholdRsrq",
        "Column_Golden_Value": "-195"
    },
    {
        "Table": "ER_L_RlfProfile",
        "Column": "t311",
        "Column_Golden_Value": "10000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_RlfProfile",
        "Condition_Table_1_Column": "rlfProfileId",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "ER_L_RlfProfile",
        "Column": "t301",
        "Column_Golden_Value": "2000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_RlfProfile",
        "Condition_Table_1_Column": "rlfProfileId",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "ER_L_SectorCarrier",
        "Column": "noOfRxAntennas",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_SectorCarrier",
        "Column": "noOfTxAntennas",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_SectorCarrier",
        "Column": "radioTransmitPerfMode",
        "Column_Golden_Value": "COVERAGE_GREEN",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "dl256QamEnabled",
        "Condition_Table_1_Column_Value": "1"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "connectedModeMobilityPrio",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "csFallbackPrio",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "csFallbackPrioEC",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "mobilityAction",
        "Column_Golden_Value": "HANDOVER"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "mobilityActionCsfb",
        "Column_Golden_Value": "RELEASE_WITH_REDIRECT_NACC"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "pMaxUtra",
        "Column_Golden_Value": "23"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qQualMin",
        "Column_Golden_Value": "-18"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXHigh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Urban"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "High Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXLow",
        "Column_Golden_Value": "8",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_EUtranCellFDD",
        "Condition_Table_1_Column": "freqBand",
        "Condition_Table_1_Column_Value": "Low Freq Band",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Topology",
        "Condition_Table_2_Column_Value": "Rural"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
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
        "Table": "ER_L_UtranFreqRelation",
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
        "Table": "ER_L_UtranFreqRelation",
        "Column": "threshXLowQ",
        "Column_Golden_Value": "31",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-120",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_UtranFreqRelation",
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
        "Table": "ER_L_UtranFreqRelation",
        "Column": "qRxLevMin",
        "Column_Golden_Value": "-115"
    },
    {
        "Table": "ER_L_AnrFunction",
        "Column": "removeNenbTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AnrFunction",
        "Column": "removeNrelTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AnrFunction",
        "Column": "removeNcellTime",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AnrFunction",
        "Column": "cellRelHoAttRateThreshold",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "ER_L_AnrFunctionUtran",
        "Column": "anrStateUtran",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AnrFunctionUtran",
        "Column": "anrUtranAcMeasOn",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AnrFunctionUtran",
        "Column": "cellAddRscpThresholdUtranDelta",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_AnrFunctionUtran",
        "Column": "hoAllowedUtranPolicy",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_AutoCellCapEstFunction",
        "Column": "useEstimatedCellCap",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "80"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "ER_L_DataRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "dnsLookupOnTai",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "nnsfMode",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "rrcConnReestActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "initPreschedulingEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "s1GtpuEchoEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_ENodeBFunction",
        "Column": "x2GtpuEchoEnable",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_LoadBalancingFunction",
        "Column": "lbThreshold",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "ER_L_LoadBalancingFunction",
        "Column": "lbCeiling",
        "Column_Golden_Value": "200"
    },
    {
        "Table": "ER_L_PreschedulingProfile",
        "Column": "preschedulingPeriod",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_PreschedulingProfile",
        "Column": "preschedulingDataSize",
        "Column_Golden_Value": "86"
    },
    {
        "Table": "ER_L_PreschedulingProfile",
        "Column": "preschedulingDuration",
        "Column_Golden_Value": "200"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBestCell",
        "Column": "a3offset",
        "Column_Golden_Value": "30"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBestCell",
        "Column": "hysteresisA3",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBestCell",
        "Column": "timeToTriggerA3",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBestCell",
        "Column": "triggerQuantityA3",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_ReportConfigEUtraBestCellAnr",
        "Column": "timeToTriggerA3",
        "Column_Golden_Value": "320"
    },
    {
        "Table": "ER_L_ReportConfigEUtraInterFreqLb",
        "Column": "a5Threshold1Rsrp",
        "Column_Golden_Value": "-44"
    },
    {
        "Table": "ER_L_ReportConfigEUtraInterFreqLb",
        "Column": "a5threshold2Rsrp",
        "Column_Golden_Value": "-110"
    },
    {
        "Table": "ER_L_RfBranch",
        "Column": "dlAttenuation",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_RfBranch",
        "Column": "ulAttenuation",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_RfPort",
        "Column": "vswrSupervisionSensitivity",
        "Column_Golden_Value": "100"
    },
    {
        "Table": "ER_L_RfPort",
        "Column": "vswrSupervisionActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_Rrc",
        "Column": "tRrcConnectionReconfiguration",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "80"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "ulMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "dlMaxRetxThreshold",
        "Column_Golden_Value": "16"
    },
    {
        "Table": "ER_L_SignalingRadioBearer",
        "Column": "tPollRetransmitUl",
        "Column_Golden_Value": "160"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "subscriberGroupProfileId",
        "Column_Golden_Value": "VoLTE"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "profilePriority",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "spidTriggerList",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "customTriggerType",
        "Column_Golden_Value": "TRIGGER_NOT_USED"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "bearerTriggerList_qci",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "bearerTriggerList_arp",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "ulHarqBlerTarget",
        "Column_Golden_Value": "2"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "dlHarqBlerTarget",
        "Column_Golden_Value": "5"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "groupExtendInactAfterVolteRel",
        "Column_Golden_Value": "20"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "drxMode",
        "Column_Golden_Value": "DISABLE_DRX"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "pZeroNominalPucchOffset",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "pZeroNominalPuschOffset",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "subGroupConfiguration6",
        "Column_Golden_Value": "3"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "ulMcsLowerLimit",
        "Column_Golden_Value": "-1"
    },
    {
        "Table": "ER_L_SubscriberGroupProfile",
        "Column": "ulMcsUpperLimit",
        "Column_Golden_Value": "10"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "a5B2MobilityTimer",
        "Column_Golden_Value": "20000"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "filterCoefficientEUtraRsrp",
        "Column_Golden_Value": "8"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "filterCoefficientEUtraRsrq",
        "Column_Golden_Value": "11"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "measQuantityUtraFDD",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "sMeasure",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActive",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActiveCDMA2000",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "bothA5RsrpRsrqCheck",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "inhibitB2RsrqConfig",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "lowPrioMeasThresh",
        "Column_Golden_Value": "4"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "excludeInterFreqAtCritical",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActiveIF",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActiveUTRAN",
        "Column_Golden_Value": "1"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActiveGERAN",
        "Column_Golden_Value": "0"
    },
    {
        "Table": "ER_L_UeMeasControl",
        "Column": "ueMeasurementsActiveCDMA2000",
        "Column_Golden_Value": "0"
    }
]