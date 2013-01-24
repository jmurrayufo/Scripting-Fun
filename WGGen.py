# World guard generator 

import time # Delays

def Print2File(string,fp):
   print string
   fp = open(fp,"a+")
   fp.write(string+"\n")
   fp.close()

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


for x in range(plotsNorth):
   for y in range (plotsEast):
      plotName = "%s%02d%02d"%(areaName,x,y)
      Print2File("    %s:"%(plotName),fileName)
      Print2File("        type: cuboid",fileName)
      Print2File("        min: {x: %d, y: 0.0, z: %d}"%(  plotCenterX + x*plotDim + x*streetWidth,
                                                      plotCenterY+  y*plotDim + y*streetWidth),
         fileName)
      Print2File("        max: {x: %d, y: 256.0, z: %d}" %(  plotCenterX + (x+1)*plotDim + x*streetWidth,
                                                         plotCenterY + (y+1)*plotDim + y*streetWidth),
         fileName)
      Print2File("        priority: 0",fileName)
      Print2File("        flags: {",fileName)
      Print2File("        greeting: Entering %s"%(plotName),fileName)
      Print2File("        farewell: Leaving %s"%(plotName),fileName)
      Print2File("        }",fileName)
      Print2File("        owners: {}",fileName)
      Print2File("        members: {}",fileName)

# spawn:
#     type: cuboid
#     min: {x: -244.0, y: 0.0, z: 160.0}
#     max: {x: -116.0, y: 256.0, z: 288.0}
#     priority: 0
#     flags: {creeper-explosion: deny, pvp: deny, greeting: Entering Spawn, 
#         enderman-grief: deny, mob-damage: deny, build: allow, mob-spawning: deny}
#     owners: {}
#     members: {}