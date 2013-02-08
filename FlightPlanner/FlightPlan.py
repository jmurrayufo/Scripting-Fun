import csv
import urllib2
import time
import re #To parse strings
import math #Distance calculations

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

class Runway:
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

class WeatherReport:
   def __init__(self):
      self.Forcast06 = None
      self.UseFor06 = None
      self.Forcast12 = None
      self.UseFor12 = None
      self.Forcast24 = None
      self.UseFor24 = None
      pass

   # Populate the current weather report
   def Populate(self,airports):
      self.Forcast06,self.UseFor06 = self.GetWeather(6)
      self.Forcast12,self.UseFor12 = self.GetWeather(12)
      self.Forcast24,self.UseFor24 = self.GetWeather(24)
      self.Airports=airports
      pass

   # Get the winds at a given time
   def WindsAtAirport(self,airport,altitude,zulu):
      # assert(type(airport)==type(str()))
      # assert(type(altitude)==type(int()))
      # assert(type(zulu)==type(datetime.datetime()))

      # Locate Airport in the Airports listing
      for apt in self.Airports:
         if apt.ID == airport:
            break
      else:
         assert(0),"Airport not found"
         
      # Check to make sure found airport is in the Weather Report
      for weather in self.Forcast06:
         if weather == apt.ID:
            weatherResult = weather
            print "Found it!"
            break
      # If it isn't find the three nearest airports and average to location
      else:
         print "Triangulate"
         time.sleep(1)
         distList = [(float('inf'),None),
                     (float('inf'),None),
                     (float('inf'),None)]
         for station in self.Forcast06:
            for i in self.Airports:
               if station == i.ID:
                  station = i
                  break
            else:
               continue
            for idx in range(len(distList)):
               if distance(apt,station) < distList[idx][0]:
                  distList.insert(idx,(distance(apt,station),station))
                  distList.pop()
                  break
         # Now calculat the Averages and produce a fake weather report for that location
         sumDistList = distList[0][0]+distList[1][0]+distList[2][0]
         for i in distList:
            print self.Forcast06[i[1].ID]
         self.CalcWindsAtAltitude(self.Forcast06[i[1].ID],0)
         # TODO: Find the target altitude %'s and then calculate out the result of the distList
      # Calculate wind/temp at that altitude for that time
      #TODO: Calculate this
      # Return
      pass

   def WindsAtLatLot(self,lat,lon,altitude,time):
      pass

   def GetWeather(self,timeStr="06"):
      """
      Get the current ADDS weather, and return a dict of direction/speed/temp tuples. 
      Valid inputs for timeStr are 06, 12 and 24
      """
      start = time.time()
      if type(timeStr)==type(int()) or type(timeStr)==type(float()):
         timeStr = "%02d"%(timeStr)

      if timeStr not in ["06","12","24"]:
         assert(0),"Time must be 6, 12, or 24"
      retVal1=dict()
      retVal2=dict()

      # Read data and prep for indexing
      rawData =  urllib2.urlopen("http://aviationweather.gov/products/nws/all?fint=%s&lvl=lo"%(timeStr))

      listData = list()
      for idx,val in enumerate(rawData):
         if val=="000\n":
            dataStart = idx
         listData.append(val)
      idx = dataStart
      

      # Insert the time range into the Dict
      while(1):
         if listData[idx][0]=="<":
            break
         match = re.search("FOR USE (\d{4})-(\d{4})Z",listData[idx])
         if match:
            retVal2["FOR USE"]=[int(match.group(1)),int(match.group(2))]
            break
         idx+=1 


      # Insert the altitude headers into the Dict
      while(1):
         if listData[idx][0]=="<":
            break
         match = re.search("FT\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)",listData[idx])
         if match:
            # TODO: We will parse this in a different function
            # retVal["ALTS"]=[
            #    int(match.group(1)),
            #    int(match.group(2)),
            #    int(match.group(3)),
            #    int(match.group(4)),
            #    int(match.group(5)),
            #    int(match.group(6)),
            #    int(match.group(7)),
            #    int(match.group(8)),
            #    int(match.group(9))
            #    ]
            idx+=1
            break
         idx+=1


      # Parse airports, and place them into the Dict
      aptData=list()
      while(1):
         if listData[idx][0]=="<":
            break
         # Beak line into the numbers
         match = re.split("(\d{4,6}(?:[-+]\d{2})?)",listData[idx])
         if match:
            # Trim out the blank and new line matches
            for i,val in enumerate(match):
               if val[0]==' ' or val[0]=='\n':
                  del match[i]
            # Insert 'None' objects to replace empty locations
            while(len(match)<10):
               match.insert(1,None)
            # Trim white space
            match[0]=match[0].strip()
            aptData.append(match)
         idx+=1

      for indexApt,apt in enumerate(aptData):
         # Parse each airport found
         for indexW,wether in enumerate(apt):
            # Skip empties
            if(wether==None):
               continue
            # Skip the name
            if(len(wether)==3):
               continue
            # Parse the data and store as a three part list
            # TODO: This could be another function
            match = re.match("(\d{2})(\d{2})([-+])?(\d{2})?",wether)
            if match:
               tmpWData = [0,0,0]
               # print
               # print match.group(0) #All
               # print match.group(1) # Heading
               # print match.group(2) # Speed
               # print match.group(3) # -/+
               # print match.group(4) # Temp

               if match.group(1) == "99":
                  tmpWData[0] = 0
                  tmpWData[1] = 0
               elif int(match.group(1)) > 36:
                  tmpWData[0] = (int(match.group(1)) - 50)*10
                  tmpWData[1] = int(match.group(2)) + 100
               else:
                  tmpWData[0] = (int(match.group(1)))*10
                  tmpWData[1] = int(match.group(2))

               if match.group(3) == None and match.group(4) == None:
                  pass
               elif match.group(3) == None or match.group(3) == "-":
                  tmpWData[2] = -int(match.group(4))
               elif match.group(3) == "+":
                  tmpWData[2] = int(match.group(4))
               aptData[indexApt][indexW] = tmpWData
         retVal1[apt[0]] = apt[1:]
         # End for indexW,i in enumerate(apt):
      # End for indexApt,apt in enumerate(aptData):
      return retVal1,retVal2

   def CalcWindsAtAltitude(self,windList,targetAltitude):
      print "CalcWindsAtAltitude"
      altitudeList = [3000,6000,9000,12000,18000,24000,30000,34000,39000]
      print len(windList)
      print windList
      print len(altitudeList)
      print altitudeList
      time.sleep(1)
      assert(len(windList)==len(altitudeList))
      for idx,value in enumerate(altitudeList):
         if idx==0 and targetAltitude<value:
            print "<3K"
         if value==altitudeList[-1] and targetAltitude>value:
            print ">39000"


def findSiteNumber(airports,siteNumber):
   for airport in airports:
      if airport.SiteNumber == siteNumber:
         return airport
   assert(0),"Airport not found"
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
   elif(type(origin[0])==type(float())):   
      lat1, lon1 = origin
   elif(type(origin[0])==type(str())):
      lat1 = parselatlon(origin[0])
      lon1 = parselatlon(origin[1])
   else:
      assert(0),"Unsupported data type"   
   if(type(destination)==type(Airport())):
      lat2 = destination.Latitude
      lon2 = destination.Longitude
   elif(type(destination[0])==type(float())):  
      lat2, lon2 = destination
   elif(type(destination[0])==type(str())):
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
# Slurp up Airport data
Airports = list()
# TODO: We need a full airports list for CO and its other local states, for longer flights
with open('Facilities.csv','r') as csvfile:
   csvreader = csv.reader(csvfile)
   csvreader.next() # Eat header
   # Place the airports into a list
   for i in csvreader:
      Airports.append(Airport(i))

# Slurp up Runway Data
with open('Runways.csv','r') as csvfile:
   csvreader = csv.reader(csvfile)
   csvreader.next() # Eat header
   for i in csvreader:
      tmpAirport = findSiteNumber(Airports,i[0])
      tmpAirport.Runways.append(Runway(i))

#Slurp up weather data
# TODO: Add code for this

tmp = WeatherReport()

tmp.Populate(Airports)
tmp.WindsAtAirport("LMO",None,None)
