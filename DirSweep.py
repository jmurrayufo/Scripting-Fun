import os
import time
import math
from pprint import pprint

def FileScan():

   print time.time()

   for dirname, dirnames, filenames in os.walk('.'):
      if( os.path.basename(dirname).startswith(".") ):
         continue
      if( not os.listdir(dirname) ):
         print dirname
         print " Age:",(time.time() - os.stat( dirname ).st_mtime)/60/60/24
         continue
      else:
         for fn in filenames:
            if( fn.startswith(".") ):
               continue
            fn = os.path.join(dirname,fn)
            age = (time.time() - os.stat( fn ).st_mtime)/60/60/24
            if( age > 30 ):
               print fn
               print " Age:",age

def get_size(start_path = '.'):
   total_size = 0
   for dirpath, dirnames, filenames in os.walk(start_path):
      for f in filenames:
         fp = os.path.join(dirpath, f)
         total_size += os.path.getsize(fp)
   return total_size

def MaxFileAge( dirSize, dirSizeMax = 100*2**20, maxAge = 365 ):
   # File sizes are in bytes, max age in days
   def Logistic( x ):
      return (1 - 1 / ( 1 + math.exp( -( (x)/15.17065377712 ) ) ))*2
   return Logistic( dirSize / float(dirSizeMax)*100 ) * maxAge
   # return ( 1 - dirSize / float( dirSizeMax ) ) * maxAge

def GetSortedFileSizeList( rootDir = "." ):
   # Return tuple list of (size,age,name)
   retList = []

   for dirname, dirnames, filenames in os.walk(rootDir):
      if( not os.listdir(dirname) ):
         retList.append( 
            (
               os.stat(dirname).st_size,
               (time.time() - os.stat( dirname ).st_mtime)/60/60/24,
               dirname
            )
         )
         continue
      else:
         for fn in filenames:
            fn = os.path.join(dirname,fn)
            age = (time.time() - os.stat( fn ).st_mtime)/60/60/24
            retList.append( 
               (
                  os.stat( fn ).st_size,
                  (time.time() - os.stat( fn ).st_mtime)/60/60/24,
                  fn
               )
            )
   retList = sorted( retList, key = lambda tup: tup[1], reverse=True )
   return retList

def SumSizesList( data ):
   retVal = 0
   for i in data:
      retVal += i[0]
   return retVal

def DeleteRoutine( data ):
   DirMaxSize = 10000000
   MaxAge = MaxFileAge( SumSizesList(data), DirMaxSize, 365 )
   print "Initial Max Age:",MaxAge
   while( data[0][1] > MaxAge ):
      print 
      print "DirSize:", SumSizesList( data )
      print "Removed:", data.pop(0)
      print "DirSize:", SumSizesList( data )
      MaxAge = MaxFileAge( SumSizesList(data), DirMaxSize, 365 )
      print "New Max Age:",MaxAge


data = GetSortedFileSizeList(".")
# print SumSizesList(data)
DeleteRoutine( data )
# pprint( GetSortedFileSizeList(".") )