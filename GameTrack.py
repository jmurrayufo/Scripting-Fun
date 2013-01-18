import psutil

# psutil found @ http://code.google.com/p/psutil/

pList = psutil.get_pid_list()

for i in pList:
   p=psutil.Process(i)
   print p.name
   print p.get_cpu_times()
