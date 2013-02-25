import time
import sys
import datetime

data = list()

foo = raw_input("Initial Value:")

data.append((time.time(),int(foo)))

while(1):
    foo=raw_input("Value: ")
    if(foo in ["-1","-","z"]):
        print "Delete last entry!"
        data.pop()
        continue
    elif(foo == ""):
        print "Got Empty!"
    elif(foo in ["?","h","-h","help"]):
        print "Enter gold amount!"
        print "Use -1 or - to delete the last entry."
    else:
        try: 
            data.append((time.time(),int(foo)))
        except ValueError:
            print "Value \"",foo,"\" is not a number, it will be ignored..."
            continue

    print "Time Today:", datetime.timedelta(seconds=data[-1][0]-data[0][0])
    print "dGold (total):",data[-1][1]-data[0][1]
    print "dGold/Hr (total): %12.2f"%((data[-1][1]-data[0][1])/(data[-1][0]-data[0][0])*60*60)
    if(len(data)>5):
        print "dGold (last 5):",data[-1][1]-data[-5][1]
        print "dGold/Hr (last 5): %12.2f"%((data[-1][1]-data[-5][1])/(data[-1][0]-data[-5][0])*60*60)
    print "dGold (last):",data[-1][1]-data[-2][1]
    print "dGold/Hr (last):  %12.2f"%((data[-1][1]-data[-2][1])/(data[-1][0]-data[-2][0])*60*60)
    print "\n\n"




