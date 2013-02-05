import csv
import time

"""
 0  : SiteNumber
 1  : Type
 2  : LocationID
 3  : EffectiveDate
 4  : Region
 5  : DistrictOffice
 6  : State
 7  : StateName
 8  : County
 9  : CountyState
 10 : City
 11 : FacilityName
 12 : Ownership
 13 : Use
 14 : Owner
 15 : OwnerAddress
 16 : OwnerCSZ
 17 : OwnerPhone
 18 : Manager
 19 : ManagerAddress
 20 : ManagerCSZ
 21 : ManagerPhone
 22 : ARPLatitude
 23 : ARPLatitudeS
 24 : ARPLongitude
 25 : ARPLongitudeS
 26 : ARPMethod
 27 : ARPElevation
 28 : ARPElevationMethod
 29 : MagneticVariation
 30 : MagneticVariationYear
 31 : TrafficPatternAltitude
 32 : ChartName
 33 : DistanceFromCBD
 34 : DirectionFromCBD
 35 : LandAreaCoveredByAirport
 36 : BoundaryARTCCID
 37 : BoundaryARTCCComputerID
 38 : BoundaryARTCCName
 39 : ResponsibleARTCCID
 40 : ResponsibleARTCCComputerID
 41 : ResponsibleARTCCName
 42 : TieInFSS
 43 : TieInFSSID
 44 : TieInFSSName
 45 : AirportToFSSPhoneNumber
 46 : TieInFSSTollFreeNumber
 47 : AlternateFSSID
 48 : AlternateFSSName
 49 : AlternateFSSTollFreeNumber
 50 : NOTAMFacilityID
 51 : NOTAMService
 52 : ActiviationDate
 53 : AirportStatusCode
 54 : CertificationTypeDate
 55 : FederalAgreements
 56 : AirspaceDetermination
 57 : CustomsAirportOfEntry
 58 : CustomsLandingRights
 59 : MilitaryJointUse
 60 : MilitaryLandingRights
 61 : InspectionMethod
 62 : InspectionGroup
 63 : LastInspectionDate
 64 : LastOwnerInformationDate
 65 : FuelTypes
 66 : AirframeRepair
 67 : PowerPlantRepair
 68 : BottledOxygenType
 69 : BulkOxygenType
 70 : LightingSchedule
 71 : BeaconSchedule
 72 : ATCT
 73 : UNICOMFrequencies
 74 : CTAFFrequency
 75 : SegmentedCircle
 76 : BeaconColor
 77 : NonCommercialLandingFee
 78 : MedicalUse
 79 : SingleEngineGA
 80 : MultiEngineGA
 81 : JetEngineGA
 82 : HelicoptersGA
 83 : GlidersOperational
 84 : MilitaryOperational
 85 : Ultralights
 86 : OperationsCommercial
 87 : OperationsCommuter
 88 : OperationsAirTaxi
 89 : OperationsGALocal
 90 : OperationsGAItin
 91 : OperationsMilitary
 92 : OperationsDate
 93 : AirportPositionSource
 94 : AirportPositionSourceDate
 95 : AirportElevationSource
 96 : AirportElevationSourceDate
 97 : ContractFuelAvailable
 98 : TransientStorage
 99 : OtherServices
100 : WindIndicator
"""

with open('Facilities.csv','r') as csvfile:
   csvreader = csv.reader(csvfile)
   for i in csvreader:
      print "%11s"%(i[0]),",",
      print "%10s"%(i[2]),",",
      print "%40s"%(i[11]),",",
      print "%14s"%(i[22]),",",
      print "%14s"%(i[24])
