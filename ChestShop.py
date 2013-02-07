import re
import time
from datetime import *
from matplotlib import pyplot as plt
from matplotlib import dates
"""
Column Breakdown:
    0: Date/time
    1: Client
    2: Action (buy or sell)
    3: Amount
    4: Item
    5: Price (total transaction)
    6: Shop Owner
    7: Location

"""
def FindUniqueCol(listOfItems,colNum):
    s=list()
    for i in listOfItems:
        if i[colNum] not in s:
            s.append(i[colNum])
        # time.sleep(1)
    return s

def FilterData( data=list(),
                dateMin=datetime(2013,1,1),
                dateMax=datetime.now(),
                item="Dirt",
                xIndex = 5
              ):
    dataX=list()
    dataY=list()
    for i in data:
        if (i[0] > dateMin and
            i[0] < dateMax and
            i[4] == item):
            dataX.append(i[0])
            dataY.append(i[xIndex])
    return (dataX,dataY)

def CustomBarPlot(X,Y,numBoxes):
    # Determine Bins
    xBins = list()
    xBins.append(min(X))
    while(xBins[-1]<max(X)):
        xBins.append(xBins[-1] + (max(X) - min(X))/numBoxes)
    # Note: len(xBins) = numBoxes + 1. this is ok, as we can use these as ranges

    # Sum Data into Bins
    yBins=list()
    ind=0
    for i in range(len(xBins)):
        if i+1 == len(xBins):
            break
        yBins.append(0)
        while X[ind] < xBins[i+1]:
            yBins[i]+=Y[ind]
            ind+=1
    # We don't need that final bin anymore, so pop it off the list. We only care about the left side of each bin for plotting
    xBins.pop() 
    fig=plt.figure()
    plt.bar(xBins,yBins,(max(X) - min(X) ).total_seconds()/86400/numBoxes)
    return fig
    
ReMatStr = "(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})"
ReMatStr += " \[ChestShop\]"
ReMatStr += " (\w+)"
ReMatStr += " (sold|bought)"
ReMatStr += " (\d)"
ReMatStr += " (\w+)"
ReMatStr += " for"
ReMatStr += " (\d+\.\d{2})"
ReMatStr += " (?:from|to)"
ReMatStr += " (\w+(?:\ Shop)?)"
ReMatStr += " at"
ReMatStr += " \[(\w+)\]"

data = list()

fp = open("C:\Program Files (x86)\Minecraft\plugins\ChestShop\ChestShop.log","r")

for i in fp:
    matches = re.search(ReMatStr,i)
    if matches:
        data.append(list(matches.groups()))
        # print matches.groups()
        # print datetime.datetime.strptime(data[-1][0],"%Y/%m/%d %H:%M:%S")
        data[-1][0]=datetime.strptime(data[-1][0],"%Y/%m/%d %H:%M:%S")
        data[-1][3]=eval(data[-1][3])
        data[-1][5]=eval(data[-1][5])



# print "Cleints:",FindUniqueCol(data,1)
# print "Items:",FindUniqueCol(data,4)
# print "Shops:",FindUniqueCol(data,6)

# Prep empty list to hold the plot data
(X,Y)=FilterData(data)


fig = CustomBarPlot(X,Y,7)
fig.autofmt_xdate()
ax=fig.add_subplot(111)
ax.xaxis.set_major_locator(dates.DayLocator())
hfmt = dates.DateFormatter('%m/%d')
ax.xaxis.set_major_formatter(hfmt)
plt.show()
# plt.title("test")
# plt.savefig("test.png")