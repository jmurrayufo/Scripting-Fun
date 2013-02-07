import urllib2
import time
import re

def GetWeather(timeStr="06"):
   """
   Get the current ADDS weather, and return a dict of direction/speed/temp tuples. 
   Valid inputs for timeStr are 06, 12 and 24
   """

   retVal=dict()

   # Read data and prep for indexing
   rawData =  urllib2.urlopen("http://aviationweather.gov/products/nws/all?fint=%s&lvl=lo"%(timeStr))
   listData = list()
   for idx,val in enumerate(rawData):
      if val=="000\n":
         dataStart = idx
      listData.append(val)
   time.sleep(1) 
   idx = dataStart
   

   # Insert the time range into the Dict
   while(1):
      if listData[idx][0]=="<":
         break
      match = re.search("FOR USE (\d{4})-(\d{4})Z",listData[idx])
      if match:
         retVal["FOR USE"]=[int(match.group(1)),int(match.group(2))]
         break
      idx+=1 


   # Insert the altitude headers into the Dict
   while(1):
      if listData[idx][0]=="<":
         break
      match = re.search("FT\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)\ +(\d+)",listData[idx])
      if match:
         retVal["ALTS"]=[
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
            int(match.group(5)),
            int(match.group(6)),
            int(match.group(7)),
            int(match.group(8)),
            int(match.group(9))
            ]
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
      # Check out that indent dropoff!
      retVal[apt[0]] = apt[1:-1]
      # End for indexW,i in enumerate(apt):
   # End for indexApt,apt in enumerate(aptData):
   return retVal

for i in GetWeather():
   print i
