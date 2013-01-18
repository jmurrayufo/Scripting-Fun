import psutil
import time
import curses 
import curses.wrapper

# psutil found @ http://code.google.com/p/psutil/

class DataStore:
   sent=0
   recv=0

def PrintData(scr,bytes,typeStr="Sent",time=-1):
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

def main(scr):
   delay = 1
   start = time.time()

   # Minutes to keep track of as well
   times = [1,5,15]


   timesLastUpdate=time.time()
   totals = DataStore()
   totalsLast = DataStore()
   pTimes=list()
   pTimes.append((time.time(),(totals.sent,totals.recv)))
   pLast=psutil.network_io_counters()

   while(1):

      stdscr.clear()
      p=psutil.network_io_counters()

      # Add up new data
      if p.bytes_sent >= pLast.bytes_sent:
         totals.sent += p.bytes_sent - pLast.bytes_sent
      else:
         # Bytes rolled over, just add the current amount
         totals.sent += p.bytes_sent

      if p.bytes_recv >= pLast.bytes_recv:
         totals.recv += p.bytes_recv - pLast.bytes_recv
      else:
         # Bytes rolled over, just add the current amount
         totals.recv += p.bytes_recv

      print "\n\n"
      print "<Totals>"
      PrintData(scr,totals.sent,"Sent")
      PrintData(scr,totals.recv,"Recv")

      print "\n<Last %ds>"%(delay)
      PrintData(scr,totals.sent - totalsLast.sent,"Sent")
      PrintData(scr,totals.recv - totalsLast.recv,"Recv")
      totalsLast.sent = totals.sent
      totalsLast.recv = totals.recv
      pLast = psutil.network_io_counters()

      # Append current (time, data)
      #pTimes.append((time.time(),psutil.network_io_counters()))
      pTimes.append((time.time(),(totals.sent,totals.recv)))

      for i in range(len(times)):
         for y in reversed(range(len(pTimes))):
            if(pTimes[y][0] <= time.time() - times[i]*60):
               print "\n<Last %dm>"%(times[i])
               PrintData(scr,totals.sent - pTimes[y][1][0],"Sent",time.time()-pTimes[y][0])
               PrintData(scr,totals.recv - pTimes[y][1][1],"Recv",time.time()-pTimes[y][0])
               # We found the first one that fits, don't check the rest!
               break
         else:
            print "\n<Last %.1fm>"%((time.time()-pTimes[0][0])/60)
            print "Full range not yet avaliable..."
            PrintData(scr,totals.sent - pTimes[0][1][0],"Sent",time.time()-pTimes[0][0])  
            PrintData(scr,totals.recv - pTimes[0][1][1],"Recv",time.time()-pTimes[0][0])  
            # We dont need to print out copies of this, break from the i loop
            break  
      if(pTimes[0][0] < time.time() - max(times)*60):
         pTimes.remove(pTimes[0])

      time.sleep(delay)

curses.wrapper(main)