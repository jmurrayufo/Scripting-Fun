# Includes
import csv
import matplotlib.pyplot as plt
import operator
import os
import re
import signal
import time
import tkFileDialog
import ttk
from datetime import datetime, date
from Tkinter import *
from numpy import *

from progressbar import *

# DEFINES
statsDir = "C:\\Users\\495569\\Documents\\scripts\\InputStats\\2013\\"

"""
   Select keytypes from the following
      -2: All
      -1: Unknown
       0: Mouse
       1: A-Z0-9
       2: Modifier
       3: NumPad
       4: Misc
       5: Function Keys
       6: Symbol
"""
KeyTypes = [-2,0,1]

SampleRadius = 5/60.     # +/- number of hours to average into the graph

StartTime = 8

EndTime = 12+5.5

# How often do we show a new progress bar?
barUpdateDelay = 1

# ******************************
# *** Calcuate Needed Values ***
# ******************************

TimeSteps = (EndTime - StartTime)/SampleRadius # Number of locations to plot on the chart-1

KeyTypeLables = dict({
                    -2: "All",
                    -1: "Unknown",
                     0: "Mouse",
                     1: "Letters",
                     2: "Mod.",
                     3: "NumPad",
                     4: "Misc",
                     5: "F#",
                     6: "Symbol"
                     })

StatsDict=dict()



def sort_table(table, col=0):
   return sorted(table, key=operator.itemgetter(col))

def GetKeyType(key):
   # Return the TYPE of key that was pressed
   #  0: Mouse
   #  1: A-Z0-9
   #  2: Modifier
   #  3: NumPad
   #  4: Misc
   #  5: Function Keys
   #  6: Symbol
   #  -1: ????
   # Mouse "Keys"
   # Mouse "Keys"
   if(key>=1 and key<=4):
      return 0
   # Misc
   if(key>=8 and key<=46):
      return 4
   # Number keys
   if(key>=48 and key<=57):
      return 1
   # Alphabits!
   if(key>=65 and key<=90):
      return 1
   #Windows keys
   if(key>=91 and key<=92):
      return 4
   # NumPad  
   if(key>=96 and key<=111):
      return 3
   # F1-F12
   if(key>=112 and key<=123):
      return 5
   if(key>=145 and key<=165):
      return 2
   if(key>=186 and key<=222):
      return 6
   return -1

def GetTimeInSec(time):
   if(type(time)==type(datetime.time(datetime.now()))):
      return time.hour*60*60 + time.minute*60 + time.second
   if(type(time)==type(str())):
      return GetTimeInSec( ParseTimeStamp(time) )
   if(type(time)==type(datetime.now())):
      return GetTimeInSec(time.time())

def ParseTimeStamp(TimeStamp):
   """
   Return a string as a datetime.datetime object
   """
   return datetime.strptime(TimeStamp,"%Y-%m-%d %H:%M:%S")

class ParseStatsFile():
   def __init__(self, file):
      self.fileToParse=file

   def Parse(self):
      StatsDict['start']=time.time()
      if self.fileToParse=="":
         print 'No file selected. Abort'
         quit()

      # Generate Blank lists
      Data=list()

      # Read CSV file
      f=open(self.fileToParse,'rb')
      c=csv.reader(f,delimiter=',')
      f.close

      print "Load Data..."
      for row in c:
         Data.append(row)
      StatsDict['lines']=c.line_num
      # I don't understand how this works
      del c

      StatsDict['FirstDate'] = Data[0][0]
      StatsDict['LastDate'] = Data[-1][0]

      print "Process Time..."
      time.sleep(0.1)
      widgetGTIS = ['GTIS Process: ', Percentage(), ' ', Bar(), ' ',ETA()]
      pGTIS = ProgressBar(widgets=widgetGTIS, maxval=len(Data)).start()
      pGTISUpdateTimer = time.time()
      prog = 0
      for i in Data:
         prog+=1
         if(time.time() > pGTISUpdateTimer + barUpdateDelay):
            pGTIS.update(prog)
            pGTISUpdateTimer = time.time()
         i[0] = GetTimeInSec(i[0])
      pGTIS.finish()
      time.sleep(0.1)

      print "Sort Tables..."
      Data=sort_table(Data)
      xData=map(operator.itemgetter(0),Data)
      yData=map(operator.itemgetter(1),Data)
      nData=map(operator.itemgetter(2),Data)
      dData=map(operator.itemgetter(3),Data)

      # Prep figure for plots
      plt.figure()

      # Setup Progress Bars
      widget0 = ['  Sub Process: ', Percentage(), ' ', Bar(), ' ',ETA()]
      widget1 = ['Total Process: ', Percentage(), ' ', Bar(), ' ',ETA()]


      pbart = ProgressBar(widgets=widget1, maxval=100).start()


      loop=0
      StatsDict['LongestDist']=0
      StatsDict['TotalDist']=0
      pbart.start()      

      # Process all smoothing factors
      for CurrentKey in KeyTypes:
         
         # Skip the first print to make the terminal output clean
         if(loop!=0):
            print
         pbart.update((loop*100)/len(KeyTypes))
         loop+=1

         # Setup for list
         x=list()
         y=list()
         keyPressC=list()
         d=list()
         dC=list() # distance cumulative

         # Process data
         subloop=0
         subLoopUpdateTimer = time.time()
         print 
         pbars = ProgressBar(widgets=widget0, maxval=100).start()
         pbars.start()
         minDex = 0
         for item in range(int(TimeSteps)+1):
            # Only update the progress bar once every second or so
            if(time.time() > subLoopUpdateTimer + barUpdateDelay):
               pbars.update(subloop*100/len(range(int(TimeSteps)+1)))
               subLoopUpdateTimer = time.time()
            subloop+=1

            # Item is begining of the X point we are calculating
            currentTime = StartTime+((EndTime - StartTime)/float(TimeSteps))*item
            
            # LOCATE INDEX VALUES
            rangeList=list()
            for index in range(minDex,len(xData)):

               if ((xData[index]/60./60. >= currentTime) and 
                  (xData[index]/60./60. < currentTime + SampleRadius)
                  ):
                  rangeList.append(index)

               if xData[index]/60./60. > currentTime + SampleRadius:
                  break
            try:
               minDex = min(rangeList)
            except ValueError:
               minDex = minDex

            # Process average
            total=0
            distTotal=0
            for k in rangeList:

               # Pares EVERYTHING
               if(CurrentKey==-2):
                  total+=int(nData[k])
                  distTotal+=float(dData[k])
                  if(int(nData[k]) > StatsDict['LongestDist']):
                     StatsDict['LongestDist']=int(nData[k])

               # Only parse the keys that are the same type as our curent key
               if(CurrentKey==GetKeyType(int(yData[k]))):
                  total+=int(nData[k])
                  distTotal+=float(dData[k])
                  if(int(nData[k]) > StatsDict['LongestDist']):
                     StatsDict['LongestDist']=int(nData[k])

            # Append results to lists
            x.append(currentTime)
            y.append(total)
            d.append(distTotal)
            if(item>0):
               keyPressC.append(total + keyPressC[item-1])
               dC.append(distTotal + dC[item-1])
            else:
               keyPressC.append(total)
               dC.append(distTotal)
         pbars.finish()
         StatsDict['LongestDist']=max(dC)
         if(max(y)<=0):
            print "No data!"
            continue;
         string=KeyTypeLables[CurrentKey]
         plt.subplot(4,1,1)
         plt.semilogy(x,y,'-',label=string)
         plt.subplot(4,1,2)
         plt.plot(x,keyPressC)
         plt.subplot(4,1,3)
         plt.plot(x,d,)
         plt.subplot(4,1,4)
         plt.plot(x,dC)

      print 
      pbart.finish()

      ax=plt.subplot(4,1,1)
      plt.grid(True)
      string = re.findall(r'/([^/]*).csv',self.fileToParse)
      plt.ylabel('Actions')
      h,l=ax.get_legend_handles_labels()
      plt.figlegend(h,l,'right')
      plt.title(string[0])

      plt.subplot(4,1,2)
      plt.grid(True)
      plt.ylabel('Actions')

      plt.subplot(4,1,3)
      plt.grid(True)
      plt.ylabel('Distance')

      plt.subplot(4,1,4)
      plt.grid(True)
      plt.xlabel('Hours')
      plt.ylabel('Distance')

      plt.tight_layout()
      plt.subplots_adjust(right=.80)

      StatsDict['finish']=time.time()

      # Before we show the chart, print the stats!

      # Pre Calculations
      StatsDict['RangeInDays']=ParseTimeStamp( StatsDict['LastDate'] ) - ParseTimeStamp( StatsDict['FirstDate'] ) 

      print "<<<STATS>>>"
      print "Lines:",StatsDict['lines']
      print "Time: %.3f" % (StatsDict['finish']-StatsDict['start'])
      print "Lines/s: %.3f" %(StatsDict['lines']*len(KeyTypes)/(StatsDict['finish']-StatsDict['start']))
      print "Days Parsed:",StatsDict['RangeInDays'].days
      if( StatsDict['RangeInDays'].days > 0 ):
         print "Lines/Day:",StatsDict['lines']/StatsDict['RangeInDays'].days
      plt.draw()


# Get user data file
master = Tk()
master.withdraw()
statsFile = 0
statsFile = tkFileDialog.askopenfilename(title="Open file", filetypes=[("CSVs",".csv"),("All files",".*")],initialdir=statsDir,initialfile=statsFile,multiple=True)



# Parse the statsFile if we got one, else try for statsDir. If both are empty, quit()
if (statsFile):
   for i in statsFile.rsplit(" "):
      x=ParseStatsFile(i)
      x.Parse()

else:
   print "No files selected, aborted."
   quit()

plt.show()