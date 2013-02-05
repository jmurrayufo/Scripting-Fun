import csv
import time
import re #To parse strings
import math

class Airport:
   SiteNumber=str()
   ID=str()
   Name=str()
   Latitude=float()
   Longitude=float()
   Elevation=int()
   Runways=list()
   def __init__(self,siteArg,idArg,nameArg,latArg,lonArg,elevArg,rwArg):
      pass

class Runway:
   SiteNumber=str()
   ID=str()
   IDB=str() #base
   IDBRP=bool() #right Pattern
   IDR=str() #Reciprocal
   IDRRP=bool() # Right Pattern
   Length=int()
   Width=int()
   Surface=str()

def parselatlon(input):
   """
   Parse a lat/lon string into a floating point number
   """
   matches = re.match("(\-?\d+)\-(\d+)\-(\d+)\.(\d{4})([NSEW])",input)
   if matches:
      matches = matches.groups()
      retVal = float(matches[0])
      retVal += float(matches[1])/60
      retVal += float(matches[2])/60/60
      retVal += float(matches[3])/60/60/10000
      # Set negative for south/west locations
      if (matches[4]=="S" or matches[4]=="W"):
         retVal *=-1
   return retVal

def distance(origin, destination,units="nm"):
   # Haversine formula example in Python
   # Author: Wayne Dyck
   lat1, lon1 = origin
   lat2, lon2 = destination

   dlat = math.radians(lat2-lat1)
   dlon = math.radians(lon2-lon1)
   a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
     * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   if(units=="km"):
      d = 6371 * c
   elif(units=="nm"):
      d = 3440.06 * c


   return d


## TEST CODE SECTION
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
# with open('Facilities.csv','r') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for i in csvreader:
#       print "%11s"%(i[0]),",",
#       print "%10s"%(i[2]),",",
#       print "%40s"%(i[11]),",",
#       print "%14s"%(i[22]),",",
#       print "%14s"%(i[24])
"""
   0 , SiteNumber
   1 , State
   2 , RunwayID
   3 , RunwayLength
   4 , RunwayWidth
   5 , RunwaySurfaceTypeCondition
   6 , RunwaySurfaceTreatment
   7 , PavementClass
   8 , RunwayWeightBearingCapacitySW
   9 , RunwayWeightBearingCapacityDW
   10 , RunwayWeightBearingCapacityDT
   11 , RunwayWeightBearingCapacityDDT
   12 , EdgeLightsIntensity
   13 , BaseEndID
   14 , BaseEndTrueAlignment
   15 , BaseEndILSType
   16 , BaseEndRightTrafficPattern
   17 , BaseEndMarkingsType
   18 , BaseEndMarkingsCondition
   19 , BaseEndPhysicalLatitude
   20 , BaseEndPhysicalLatitudeS
   21 , BaseEndPhysicalLongitude
   22 , BaseEndPhysicalLongitudeS
   23 , BaseEndPhysicalElevation
   24 , BaseEndCrossingHeight
   25 , BaseEndGlidePathAngle
   26 , BaseEndDisplacedLatitude
   27 , BaseEndDisplacedLatitudeS
   28 , BaseEndDisplacedLongitude
   29 , BaseEndDisplacedLongitudeS
   30 , BaseEndDisplacedElevation
   31 , BaseEndDisplacedLength
   32 , BaseEndTDZElevation
   33 , BaseEndVASI
   34 , BaseEndRVR
   35 , BaseEndRVV
   36 , BaseEndALS
   37 , BaseEndREIL
   38 , BaseEndCenterlineLights
   39 , BaseEndTouchdownLights
   40 , BaseEndObjectDescription
   41 , BaseEndObjectMarkLight
   42 , BaseEndPart77Category
   43 , BaseEndObjectClearSlope
   44 , BaseEndObjectHeight
   45 , BaseEndObjectDistance
   46 , BaseEndObjectOffset
   47 , ReciprocalEndID
   48 , ReciprocalEndTrueAlignment
   49 , ReciprocalEndILSType
   50 , ReciprocalEndRightTrafficPattern
   51 , ReciprocalEndMarkingsType
   52 , ReciprocalEndMarkingsCondition
   53 , ReciprocalEndPhysicalLatitude
   54 , ReciprocalEndPhysicalLatitudeS
   55 , ReciprocalEndPhysicalLongitude
   56 , ReciprocalEndPhysicalLongitudeS
   57 , ReciprocalEndPhysicalElevation
   58 , ReciprocalEndCrossingHeight
   59 , ReciprocalEndGlidePathAngle
   60 , ReciprocalEndDisplacedLatitude
   61 , ReciprocalEndDisplacedLatitudeS
   62 , ReciprocalEndDisplacedLongitude
   63 , ReciprocalEndDisplacedLongitudeS
   64 , ReciprocalEndDisplacedElevation
   65 , ReciprocalEndDisplacedLength
   66 , ReciprocalEndTDZElevation
   67 , ReciprocalEndVASI
   68 , ReciprocalEndRVR
   69 , ReciprocalEndRVV
   70 , ReciprocalEndALS
   71 , ReciprocalEndREIL
   72 , ReciprocalEndCenterlineLights
   73 , ReciprocalEndTouchdownLights
   74 , ReciprocalEndObjectDescription
   75 , ReciprocalEndObjectMarkLight
   76 , ReciprocalEndPart77Category
   77 , ReciprocalEndObjectClearSlope
   78 , ReciprocalEndObjectHeight
   79 , ReciprocalEndObjectDistance
   80 , ReciprocalEndObjectOffset
   81 , RunwayLengthSource
   82 , RunwayLengthSourceDate
   83 , BaseEndGradient
   84 , BaseEndGradientDirection
   85 , BaseEndPositionSource
   86 , BaseEndPositionSourceDate
   87 , BaseEndElevationSource
   88 , BaseEndElevationSourceDate
   89 , BaseEndDisplacedThresholdPositionSource
   90 , BaseEndDisplacedThresholdPositionSourceDate
   91 , BaseEndDisplacedThresholdElevationSource
   92 , BaseEndDisplacedThresholdElevationSourceDate
   93 , BaseEndTouchdownZoneElevationSource
   94 , BaseEndTouchdownZoneElevationSourceDate
   95 , BaseEndTakeOffRunAvailableTORA
   96 , BaseEndTakeOffDistanceAvailableTODA
   97 , BaseEndAcltStopDistanceAvailableASDA
   98 , BaseEndLandingDistanceAvailableLDA
   99 , ReciprocalEndGradient
   100 , ReciprocalEndGradientDirection
   101 , ReciprocalEndPositionSource
   102 , ReciprocalEndPositionSourceDate
   103 , ReciprocalEndElevationSource
   104 , ReciprocalEndElevationSourceDate
   105 , ReciprocalEndDisplacedThresholdPositionSource
   106 , ReciprocalEndDisplacedThresholdPositionSourceDate
   107 , ReciprocalEndDisplacedThresholdElevationSource
   108 , ReciprocalEndDisplacedThresholdElevationSourceDate
   109 , ReciprocalEndTouchdownZoneElevationSource
   110 , ReciprocalEndTouchdownZoneElevationSourceDate
   111 , ReciprocalEndTakeOffRunAvailableTORA
   112 , ReciprocalEndTakeOffDistanceAvailableTODA
   113 , ReciprocalEndAcltStopDistanceAvailableASDA
   114 , ReciprocalEndLandingDistanceAvailableLDA
"""
# with open('Runways.csv','r') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for i in csvreader:
#       col=0
#       for x in i:
#          print "%3d"%(col),",",x
#          col+=1
#       break

lmo = (parselatlon("40-09-51.4650N"),parselatlon("105-09-49.4350W"))
bjc = (parselatlon("39-54-31.7000N"),parselatlon("105-07-01.9000W"))
print lmo
print bjc
print distance(lmo,bjc)

## END TEST CODE SECTION
