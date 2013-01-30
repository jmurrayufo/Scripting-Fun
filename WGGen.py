# World guard generator 
import time # Delays



def Print2File(string,fp):
   """ Print a string to the command line, and to the file fp. """
   print string
   fp = open(fp,"a+")
   fp.write(string+"\n")
   fp.close()

class WGZone:
   __init__(self):
      self.name=""
      self.xBounds=[0,0]
      self.zBounds=[0,0]
      self.flags=dict()
   def Output(file):
      pass
   def SetLoc(x,z,size,orientation="sw"):
      """
         x: X coord to base location from
         z: Z coord to base location from
         size: True dimensions of the square
         orientation: How the shape relates to the x and z locations
            c = centered (will round down)
            ne = x,z are the North East Corner
            se = x,z are the South East Corner
            sw = x,z are the South West Corner (Default)
            nw = x,z are the North West Corner
      """
      # TODO: This section could be shunk by several lines with some digital logic
      if(orientation=="c"):
         self.xBounds = [x - size//2,x + size//2] # Round down divide
         self.zBounds = [z - size//2,z + size//2] # Round down divide
      elif(orientation=="ne"):
         self.xBounds = [x - size,x]
         self.zBounds = [z + size,z]
      elif(orientation=="se"):
         self.xBounds = [x - size,x]
         self.zBounds = [z,z - size]
      elif(orientation=="sw"):
         self.xBounds = [x,x + size]
         self.zBounds = [z,z - size]
      elif(orientation=="nw"):
         self.xBounds = [x,x + size]
         self.zBounds = [z + size,z]

# Get user inputs
print "<=Plot Names=>"
areaName = raw_input(">")
fileName = areaName+".txt"

print "\n<=Select Plot Dimension=>"
plotDim = input(">")
print "Plots will be %dx%d (%d m^2)(%d m^3)"%(plotDim,plotDim,plotDim*plotDim,plotDim*plotDim*256)
plotDim -= 1

print "\n<=Select X (south) Edge=>"
plotCenterX = input(">:")

print "\n<=Select Z (Western) Edge=>"
plotCenterY = input(">:")

print "\n<=Select Street Width=>"
streetWidth = input(">:")
if(float(streetWidth)/2 == int(streetWidth)/2):
   print "WARNING: Streets will be even"
streetWidth += 1

print "\n<=Number of Plots to the North=>"
plotsNorth = input(">")

print "\n<=Number of Plots to the East=>"
plotsEast = input(">")



# Loop thought all locations that we plan to have a plot. This ignores any limitations for
#  land area and exports the results to a file in the directory the command was run from. 
for z in range(plotsNorth):
   for x in range (plotsEast):
      plotName = "%s%02d%02d"%(areaName,z,x)
      # Spacing on the following lines is important. It allows for copy/paste into the regions.yml file when done. 
      Print2File("    %s:"%(plotName),fileName)
      Print2File("        type: cuboid",fileName)
      Print2File("        min: {x: %d, y: 0.0, z: %d}"%( plotCenterX + x*plotDim + x*streetWidth,
                                                         plotCenterY - z*plotDim - z*streetWidth ),
         fileName)
      Print2File("        max: {x: %d, y: 256.0, z: %d}" %( plotCenterX + (x+1)*plotDim + x*streetWidth,
                                                            plotCenterY - (z+1)*plotDim - z*streetWidth ),
         fileName)
      Print2File("        priority: 0",fileName)
      Print2File("        flags: {",fileName)
      Print2File("        greeting: Entering %s,"%(plotName),fileName)
      Print2File("        farewell: Leaving %s"%(plotName),fileName)
      Print2File("        }",fileName)
      Print2File("        owners: {}",fileName)
      Print2File("        members: {}",fileName)