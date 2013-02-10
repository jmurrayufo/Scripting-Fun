import os
import subprocess
from multiprocessing import Pool
import time
import re

def PingServer(IP):
    try:
        tmp = subprocess.check_output("ping "+IP, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError: 
        return None
    except:
        raise
    tmp = tmp.replace("\r","").split("\n")
    tmp = filter(None, tmp)
    return tmp

def PrintWhenDone(arg):
    maxes = list()
    averages = list()
    for i in arg:
        if i == None:
            continue
        # print i[-1]
        match = re.search("    Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms",i[-1])
        if match:
            maxes.append(int(match.group(2)))
            averages.append(int(match.group(3)))
    print "Max:",max(maxes)
    print "Average:",sum(averages)/float(len(averages))
    print "Done"

if __name__ == '__main__':
    pool = Pool(processes=2)
    serverList = list()
    for i in range(1,21):
        serverList.append("66.150.148.%d -w 1000"%(i))
    print len(serverList)
    assert(len(serverList)>0)
    tmp = pool.map_async(PingServer, serverList,callback=PrintWhenDone)  
    pool.close()
    pool.join()