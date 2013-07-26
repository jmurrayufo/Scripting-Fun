import csv
import time
import json
import urllib
from math import *

ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json'

# Data gathered from http://www.ourairports.com/data/

def GetNaviadLatLon( targetName ):
   with open( "csvData/navaids.csv" ) as fp:
      navreader = csv.reader( fp )
      for row in navreader:
         if row[2].upper() == targetName.upper():
            return row[6:8]

def GetAirportLatLon( targetName ):
   with open( "csvData/airports.csv" ) as fp:
      navreader = csv.reader( fp )
      for row in navreader:
         if row[1].upper() == targetName.upper():
            return row[4:6]

def FormatValidPath( data ):
   pathStr = data[0][0] + "," + data[0][1] 
   for i in data[1:]:
      pathStr += "|" + i[0] + "," + i[1]
   return pathStr
   # return P1[0] + "," + P1[1] + "|" + P2[0] + "," + P2[1]

def GetDistanceLatLot( P1, P2 ):
   lon1, lat1, lon2, lat2 = map(radians, [
      float(P1[1]), 
      float(P1[0]), 
      float(P2[1]), 
      float(P2[0])
      ])

   dlon = lon2 - lon1
   dlat = lat2 - lat1
   a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
   c = 2 * atan2(sqrt(a), sqrt(1-a))
   return 6371 * c * 0.539957 # 1 km = 0.539957 nm

def GetLatLonPointsAlongPath( P1, P2, Steps=10 ):
   assert( Steps <  50 )
   dlat = float(P2[0]) - float(P1[0])
   dlon = float(P2[1]) - float(P1[1])
   pathArray = []
   for i in range(Steps+1):
      pathArray.append( [str(float(P1[0]) + dlat * i/Steps), str(float(P1[1]) + dlon * i/Steps)] )
   return pathArray

def getElevation(path="36.578581,-118.291994|36.23998,-116.83171",samples="2",sensor="false", **elvtn_args):
   # Example found at https://developers.google.com/maps/documentation/elevation/
   elvtn_args.update({
     'path': path,
     'samples': str(samples),
     'sensor': sensor
   })

   url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
   assert( len(url) <= 2048 ),"URL exceeded max characters"
   response = json.load(urllib.urlopen(url))

   # Create a dictionary for each results[] object
   elevationArray = []

   for resultset in response['results']:
     elevationArray.append(resultset['elevation'] * 3.28084 )

   return elevationArray


P1=GetAirportLatLon("KLMO")
P2=GetNaviadLatLon("RLG")


# print GetDistanceLatLot(P1,P2)
path = GetLatLonPointsAlongPath(P1,P2,20)
points = len(path)
# print points
path = FormatValidPath( path )
# print path
print getElevation( path, points)