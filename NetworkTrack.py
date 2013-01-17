import psutil
import time

# psutil found @ http://code.google.com/p/psutil/

def PrintData(bytes,typeStr="Sent",time=-1):
   if(bytes < 2**10):
      print "%s: %4d"%(typeStr,bytes),
   elif(bytes < 2**20):
      print "%s: %8.3f (KiB)"%(typeStr,bytes/float(2**10)),
   elif(bytes < 2**30):
      print "%s: %8.3f (MiB)"%(typeStr,bytes/float(2**20)),
   else:
      print "%s: %8.3f (GiB)"%(typeStr,bytes/float(2**30)),
   if(time>0):
      print "(%7.3f KiB/s)" %((bytes/(float(2**10))/time))
   else:
      print

delay = 1
start = time.time()

# Minutes to keep track of as well
times = [1,5,15]

pTimes=list()
pTimes.append((time.time(),psutil.network_io_counters()))
timesLastUpdate=time.time()

pFirst=psutil.network_io_counters()
pLast=psutil.network_io_counters()

while(1):
   p=psutil.network_io_counters()

   print "\n\n"
   print "<Totals>"
   PrintData(p.bytes_sent,"Sent")
   PrintData(p.bytes_recv,"Recv")

   print "\n<Last %ds>"%(delay)
   PrintData(p.bytes_sent - pLast.bytes_sent,"Sent")
   PrintData(p.bytes_recv - pLast.bytes_recv,"Recv")
   pLast=psutil.network_io_counters()

   print "\n<Last %ds>"%(time.time()-start)
   PrintData(p.bytes_sent - pFirst.bytes_sent,"Sent",time.time()-start)
   PrintData(p.bytes_recv - pFirst.bytes_recv,"Recv",time.time()-start)
   pLast=psutil.network_io_counters()

   # Append current (time, data)
   pTimes.append((time.time(),psutil.network_io_counters()))

   for i in range(len(times)):
      for y in reversed(range(len(pTimes))):
         if(pTimes[y][0] <= time.time() - times[i]*60):
            print "\n<Last %dm>"%(times[i])
            PrintData(p.bytes_sent - pTimes[y][1].bytes_sent,"Sent",time.time()-pTimes[y][0])
            PrintData(p.bytes_recv - pTimes[y][1].bytes_recv,"Recv",time.time()-pTimes[y][0])
            # We found the first one that fits, don't check the rest!
            break
      else:
         print "\n<Last %.1fm>"%((time.time()-pTimes[0][0])/60)
         print "Full range not yet avaliable..."
         PrintData(p.bytes_sent - pTimes[0][1].bytes_sent,"Sent",time.time()-pTimes[0][0])  
         PrintData(p.bytes_recv - pTimes[0][1].bytes_recv,"Recv",time.time()-pTimes[0][0])  
         # We dont need to print out copies of this, break from the i loop
         break  
   if(pTimes[0][0] < time.time() - max(times)*60):
      pTimes.remove(pTimes[0])



   time.sleep(delay)
