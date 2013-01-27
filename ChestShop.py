import re
import time
import datetime
fp = open("C:\Program Files (x86)\Minecraft\plugins\ChestShop\ChestShop.log","r")
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

ReMatStr = "(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})"
ReMatStr += " \[ChestShop\]"
ReMatStr += " (\w+)"
ReMatStr += " (sold|bought)"
ReMatStr += " (\d)"
ReMatStr += " (\w+)"
ReMatStr += " for"
ReMatStr += " (\d+\.\d{2})"
ReMatStr += " from"
ReMatStr += " (\w+(?:\ Shop)?)"
ReMatStr += " at"
ReMatStr += " \[(\w+)\]"

data = list()
for i in fp:
    matches = re.search(ReMatStr,i)
    if matches:
        data.append(list(matches.groups()))
        # print matches.groups()
        # print datetime.datetime.strptime(data[-1][0],"%Y/%m/%d %H:%M:%S")
        data[-1][0]=datetime.datetime.strptime(data[-1][0],"%Y/%m/%d %H:%M:%S")
        data[-1][3]=eval(data[-1][3])
        data[-1][5]=eval(data[-1][5])
for i in data:
    print i

print "Cleints:",FindUniqueCol(data,1)
print "Items:",FindUniqueCol(data,4)
print "Shops:",FindUniqueCol(data,6)
