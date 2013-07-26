import os
import time
import math

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
   def Logistic( x ):
      return (1 - 1 / ( 1 + math.exp( -( (x)/15.17065377712 ) ) ))*2
   return Logistic( dirSize / float(dirSizeMax)*100 ) * maxAge
   # return ( 1 - dirSize / float( dirSizeMax ) ) * maxAge



for i in range(0,100,5):
   print MaxFileAge( i, 10, 365)