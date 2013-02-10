import os
import subprocess
from multiprocessing import Pool
import time
import re
import itertools
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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
    # print "Max:",max(maxes)
    # print "Average:",sum(averages)/float(len(averages))
    # print "Done"

if __name__ == '__main__':

    procs = [10,20,30,40]
    targets = [1,2,4,8,16,32,64,128,256]
    xData = list()
    yData = list()
    zData = list()
    for p,t in itertools.product(procs,targets):
        start = time.time()
        pool = Pool(processes=p)
        serverList = list()
        for i in range(1,t+1):
            serverList.append("66.150.148.%d -w 1000"%(i))
        assert(len(serverList)>0)
        tmp = pool.map_async(PingServer, serverList,callback=PrintWhenDone)  
        pool.close()
        pool.join()
        print "%d,%d,%f"%(p,t,time.time()-start)
        xData.append(p)
        yData.append(t)
        zData.append(time.time()-start)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Proc')
    ax.set_ylabel('Target')
    ax.set_zlabel('Time')

    ax.scatter(xData,yData,zData)
    plt.show()