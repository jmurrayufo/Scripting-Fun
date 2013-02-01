# World guard generator 
import time # Delays



def Print2File(string,fp):
   """ Print a string to the command line, and to the file fp. """
   print string,
   fp = open(fp,"a+")
   fp.write(string)
   fp.close()

class WGZone:
   
   def __init__(self):
      self.name=""
      self.xBounds=[0,0]
      self.zBounds=[0,0]
      self.flags=dict()
   
   def Output(self,fileName):      
      # Spacing on the following lines is important. It allows for copy/paste into the regions.yml file when done. 
      Print2File("    %s:\n"%(self.name),fileName)
      Print2File("        type: cuboid\n",fileName)
      Print2File("        min: {x: %d, y:   0.0, z: %d}\n"%(self.xBounds[0],self.zBounds[0]),fileName)
      Print2File("        max: {x: %d, y: 256.0, z: %d}\n"%(self.xBounds[1],self.zBounds[1]),fileName)
      Print2File("        priority: 0\n",fileName)
      Print2File("        flags: {\n",fileName)
      tmp = 0
      for i in self.flags:
         Print2File("            %s:%s"%(i,self.flags[i]),fileName)
         tmp+=1
         if(tmp<len(self.flags)):
            Print2File(",\n",fileName)
         else:
            Print2File("\n",fileName)

      Print2File("        }\n",fileName)
      Print2File("        owners: {}\n",fileName)
      Print2File("        members: {}\n",fileName)

   def SetLoc(self,z,x,origin,size=16,streetWidth=0):
      """
         x: X coord to base location from
         z: Z coord to base location from
         size: True dimensions of the square
      """
      z=origin[0] + z*size + z*streetWidth
      x=origin[1] + x*size + x*streetWidth

      # TODO: This section could be shunk by several lines with some digital logic
      self.zBounds = [-z-size,-z]
      self.xBounds = [x,x + size]
   def SetFlag(self,flag,value):
      self.flags[flag]=value

   def SetName(self,areaName,z,x):
      self.name = "%s%02d%02d"%(areaName,z,x)


# Get user inputs
print "<=Plot Names=>"
areaName = raw_input(">")
fileName = areaName+".txt"

print "\n<=Select Plot Dimension=>"
plotDim = input(">")
print "Plots will be %dx%d (%d m^2)(%d m^3)"%(plotDim,plotDim,plotDim*plotDim,plotDim*plotDim*256)
plotDim -= 1

print "\n<=Select X (+X is Eastern) Edge=>"
plotCenterX = input(">")

print "\n<=Select Z (-Z is Northern) Edge=>"
plotCenterZ = input(">")

print "\n<=Select Street Width=>"
streetWidth = input(">")
if(float(streetWidth)/2 == int(streetWidth)/2 and streetWidth!=0):
   print "WARNING: Streets will be even"
elif(streetWidth <0):
   assert(0),"Negative street width"
streetWidth += 1

print "\n<=Number of Plots to the North=>"
plotsNorth = input(">")

print "\n<=Number of Plots to the East=>"
plotsEast = input(">")



# Loop thought all locations that we plan to have a plot. This ignores any limitations for
#  land area and exports the results to a file in the directory the command was run from. 
for z in range(plotsNorth):
   for x in range (plotsEast):
      # print "Z: %3d X: %3d"%(z,x)
      tmp=WGZone()
      tmp.SetLoc(z,x,[plotCenterZ,plotCenterX],plotDim,streetWidth)
      tmp.SetName(areaName,z,x)
      tmp.SetFlag("greeting","Entering %s"%(tmp.name))
      tmp.SetFlag("farewell","Leaving %s"%(tmp.name))
      tmp.Output("test.txt")

      """
      plotName = "%s%02d%02d"%(areaName,z,x)
      # Spacing on the following lines is important. It allows for copy/paste into the regions.yml file when done. 
      Print2File("    %s:\n"%(plotName),fileName)
      Print2File("        type: cuboid\n",fileName)
      Print2File("        min: {x: %d, y: 0.0, z: %d}\n"%( plotCenterX + x*plotDim + x*streetWidth,
                                                         plotCenterY - z*plotDim - z*streetWidth ),
         fileName)
      Print2File("        max: {x: %d, y: 256.0, z: %d}\n" %( plotCenterX + (x+1)*plotDim + x*streetWidth,
                                                            plotCenterY - (z+1)*plotDim - z*streetWidth ),
         fileName)
      Print2File("        priority: 0\n",fileName)
      Print2File("        flags: {\n",fileName)
      Print2File("        greeting: Entering %s,\n"%(plotName),fileName)
      Print2File("        farewell: Leaving %s\n"%(plotName),fileName)
      Print2File("        }\n",fileName)
      Print2File("        owners: {}\n",fileName)
      Print2File("        members: {}\n",fileName)
      """