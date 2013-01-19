import psutil
import time
import curses 
import curses.wrapper

# psutil found @ http://code.google.com/p/psutil/
# curses found @ http://www.lfd.uci.edu/~gohlke/pythonlibs/

class DataStore:
   sent=0
   recv=0

def PrintData(scr,bytes,typeStr="Sent",time=-1):
   (y,x)=scr.getyx()
   scr.move(y+1,1)
   if(bytes < 2**10):
      scr.addstr("%s: %4d          "%(typeStr,bytes))
   elif(bytes < 2**20):
      scr.addstr("%s: %8.3f (KiB)"%(typeStr,bytes/float(2**10)))
   elif(bytes < 2**30):
      scr.addstr("%s: %8.3f (MiB)"%(typeStr,bytes/float(2**20)))
   else:
      scr.addstr("%s: %8.3f (GiB)"%(typeStr,bytes/float(2**30)))

   if(time>0):
      scr.addstr(" (%6.3f KiB/s)" %((bytes/(float(2**10))/time)))

def main(scr):
   curses.curs_set(0)
   scr.nodelay(1)

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
      scr.clear()
      scr.border()
      scr.move(0,0)

      quit = 0
      tmp = scr.getch()
      while(tmp  != -1):
         if(tmp == 113):
            quit = 1
            break
         tmp=scr.getch()

      if(quit == 1):
         break

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
      
      (y,x)=scr.getyx()
      scr.move(y+1,1)
      scr.addstr("<Totals>")
      PrintData(scr,totals.sent,"Sent")
      PrintData(scr,totals.recv,"Recv")

      (y,x)=scr.getyx()
      scr.move(y+2,1)
      scr.addstr("<Last %ds>"%(delay))
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
               (y1,x1)=scr.getyx()
               scr.move(y1+2,1)
               scr.addstr("<Last %dm>"%(times[i]))
               PrintData(scr,totals.sent - pTimes[y][1][0],"Sent",time.time()-pTimes[y][0])
               PrintData(scr,totals.recv - pTimes[y][1][1],"Recv",time.time()-pTimes[y][0])
               # We found the first one that fits, don't check the rest!
               break
         else:
            (y,x)=scr.getyx()
            scr.move(y+2,1)
            scr.addstr("<Last %.1fm>"%((time.time()-pTimes[0][0])/60))
            scr.move(y+3,1)
            scr.addstr("Full range not yet avaliable...")
            PrintData(scr,totals.sent - pTimes[0][1][0],"Sent",time.time()-pTimes[0][0])  
            PrintData(scr,totals.recv - pTimes[0][1][1],"Recv",time.time()-pTimes[0][0])  
            # We dont need to print out copies of this, break from the i loop
            break  
      while(pTimes[0][0] < time.time() - max(times)*60):
         pTimes.remove(pTimes[0])
      scr.refresh()
      time.sleep(delay)

curses.wrapper(main)