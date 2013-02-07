import random
import time

x = [float('inf'),float('inf'),float('inf')]

# for i in range(20):
#    tmp = random.random()*500
#    for idx in range(len(x)):
#       if tmp < x[idx]:
#          x.insert(idx,tmp)
#          x.pop()
#          break
#    print "[%.2f,%.2f,%.2f]"%(x[0],x[1],x[2]),
#    print " Sum: %.2f"%(sum(x))
#    print "[%.2f,%.2f,%.2f]"%(1-x[0]/sum(x),1-x[1]/sum(x),1-x[2]/sum(x))

distList = [(float(5),"DEN"),
            (float(6),"LMO"),
            (float(5.5),"BJC")]

print distList
print sorted(distList)