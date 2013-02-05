import csv
import time
import re #To parse strings
import math #Distance calculations
import itertools

class Airport:
   def __init__(self,csvLine = None):
      if(csvLine==None):
         return
      self.SiteNumber = csvLine[0]
      self.ID = csvLine[2]
      self.Name = csvLine[11]
      self.Latitude = parselatlon(csvLine[22])
      self.Longitude = parselatlon(csvLine[24])
      self.Elevation = int(csvLine[27])
      self.Runways = list()
   def __str__(self):
      retStr  = ""
      retStr += "Site #:"
      retStr += self.SiteNumber
      retStr += " ID:"
      retStr += self.ID
      retStr += " Name:"
      retStr += self.Name
      retStr += " Latitude:"
      retStr += str(self.Latitude)
      retStr += " Longitude:"
      retStr += str(self.Longitude)
      retStr += " Elevation:"
      retStr += str(self.Elevation)
      if(len(self.Runways)):
         retStr+=" Runways:"
         for i in self.Runways:
            retStr += i.ID
            if(i!=self.Runways[-1]):
               retStr += ","
      return retStr
      pass
   def __repr__(self):
      return self.ID
      pass

def FindSiteNumber(airports,siteNumber):
   for airport in airports:
      if airport.SiteNumber == siteNumber:
         return airport
   assert(0),"Airport not found"

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
   def __init__(self,csvLine):
      self.SiteNumber = csvLine[0]
      self.ID = csvLine[2]
      self.IDB = csvLine[13]
      self.IDBRP = True if csvLine[16]=="Y" else False
      self.IDR = csvLine[47]
      self.IDRRP = True if csvLine[50]=="Y" else False
      self.Length = int(csvLine[3])
      self.Width = int(csvLine[4])
      self.Surface = csvLine[5]
"""
   Code to find the column numbers for Airport and Runway objects
   with open('Runways.csv','r') as csvfile:
      csvreader = csv.reader(csvfile)
      for i in csvreader:
         col=0
         for x in i:
            print "%3d"%(col),",",x
            col+=1
         break
"""

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
   """
   origin/destination
      These can be any of the following
         Airport Objects
         List/Tuple of strings (in "12-23-56.7890N" format) with lat first
         List/Tuple of floats with lat first
   units 
      nm : nautical mile
      sm : miles
      km : kilometer
   """
   # Haversine formula example in Python
   # Author: Wayne Dyck
   if(type(origin)==type(Airport())):
      lat1 = origin.Latitude
      lon1 = origin.Longitude
      lat2 = destination.Latitude
      lon2 = destination.Longitude
   elif(type(origin[0])==type(float())):   
      lat1, lon1 = origin
      lat2, lon2 = destination
   elif(type(origin[0])==type(str())):
      lat1 = parselatlon(origin[0])
      lon1 = parselatlon(origin[1])
      lat2 = parselatlon(destination[0])
      lon2 = parselatlon(destination[1])
   else:
      assert(0),"Unsupported data type"


   dlat = math.radians(lat2-lat1)
   dlon = math.radians(lon2-lon1)
   a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
     * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   if(units=="km"):
      d = 6371 * c
   elif(units=="nm"):
      d = 3440.06 * c
   elif(units=="sm"):
      d = 3958.76 * c


   return d

## END TEST CODE SECTION
Airports = list()
with open('Facilities.csv','r') as csvfile:
   csvreader = csv.reader(csvfile)
   csvreader.next() # Eat header
   # Place the airports into a list
   for i in csvreader:
      Airports.append(Airport(i))

with open('Runways.csv','r') as csvfile:
   csvreader = csv.reader(csvfile)
   csvreader.next() # Eat header
   for i in csvreader:
      tmpAirport = FindSiteNumber(Airports,i[0])
      tmpAirport.Runways.append(Runway(i))

for i in itertools.combinations(Airports,2):
   print i
   print distance(i[0],i[1])
   # time.sleep(1)