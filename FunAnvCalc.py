import datetime
import math
import time

def calcSigFig(x):
   if x==0:
      return 1
   try:
      return int(math.log(x,10)+1)
   except ValueError:
      return int(math.log(-x,10)+1)

def calcNextSigNumber(x):
   return (int(x) / 10**(calcSigFig(x)-1)+1) * 10**(calcSigFig(x)-1)

def calcNextSigDate(x,div=1):
   """Returns three things
      x,y,z:
         x: Seconds until date
         y: Date of the Sig Date
         z: Value of that new Sig Date

   Use div to divide into different time slices (div 86400 would be in days...)
      default is to use 1, so seconds"""

   assert type(x) == type(datetime.datetime.now()),"Error got: %s"%type(x)
   start = x
   now = datetime.datetime.now().replace(microsecond=0)
   dTime = int((now-start).total_seconds())

   retX = calcNextSigNumber(dTime/div)-dTime/div
   retY = start + datetime.timedelta(seconds=calcNextSigNumber(dTime/div)*div)
   retZ = calcNextSigNumber(dTime/div)

   return retX,retY,retZ


start = datetime.datetime( year=2009,
                           month=12,
                           day=20)

now = datetime.datetime.now().replace(microsecond=0)
total_seconds=int((now-start).total_seconds())
print "Total Seconds:",total_seconds
print "Total Days:",total_seconds/86400
print "Total Weeks:",total_seconds/604800
print "Total Months:",total_seconds/int(2.63e+6)
print "Total Years:",total_seconds/int(3.156e7)

x,y,z=calcNextSigDate(start,1)
print "Next Anv is in %d seconds, on %s and will be %d seconds"%(x,y,z)

x,y,z=calcNextSigDate(start,86400)
print "Next Anv is in %d days, on %s and will be %d days"%(x,y,z)

x,y,z=calcNextSigDate(start,604800)
print "Next Anv is in %d weeks, on %s and will be %d weeks"%(x,y,z)

x,y,z=calcNextSigDate(start,int(2.63e+6))
print "Next Anv is in %d months, on %s and will be %d months"%(x,y,z)

x,y,z=calcNextSigDate(start,int(3.156e7))
print "Next Anv is in %d years, on %s and will be %d years"%(x,y,z)
# print calcNextSigNumber((now-start).total_seconds())-(now-start).total_seconds()
