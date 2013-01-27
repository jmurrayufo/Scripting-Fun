import re
import datetime
fp = open("C:\Program Files (x86)\Minecraft\plugins\ChestShop\ChestShop.log","r")

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
for i in data:
    print i