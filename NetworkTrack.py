import psutil

# psutil found @ http://code.google.com/p/psutil/


def PrintData(bytes,typeStr="Sent"):
   if(bytes < 2**10):
      print "%s: %d"%(typeStr,bytes)
   elif(bytes < 2**20):
      print "%s:(KiB) %0.3f"%(typeStr,bytes/float(2**10))
   elif(bytes < 2**30):
      print "%s:(MiB) %0.3f"%(typeStr,bytes/float(2**20))
   else:
      print "%s:(GiB) %0.3f"%(typeStr,bytes/float(2**30))


p=psutil.network_io_counters()

PrintData(p.bytes_sent,"Sent")
PrintData(p.bytes_recv,"Recv")