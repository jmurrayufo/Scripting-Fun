from __future__ import division
import json

# HELPER FUNCTIONS
def PointInPoly(x,y,poly):
   n = len(poly)
   inside =False
   p1x,p1y = poly[0]
   for i in range(n+1):
      p2x,p2y = poly[i % n]
      if y > min(p1y,p2y):
         if y <= max(p1y,p2y):
            if x <= max(p1x,p2x):
               if p1y != p2y:
                  xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
               if p1x == p2x or x <= xinters:
                  inside = not inside
      p1x,p1y = p2x,p2y
   return inside

def GetFloat( prompt, default=0.0 ):
   try:
      return input(prompt)
   except( SyntaxError ):
      return default

def Gal2Lbs( gallons, temperature=15 ):
   return gallons * (temperature * -0.0065 + 6.1348)

def Lbs2Gal( Lbs, temperature=15 ):
   return Lbs / (temperature * -0.0065 + 6.1348)

def Num2Str( value ):
   return "{:,}".format( int( value ) )


# CLASSES
class Weight():


   def __init__( self, weight, arm ):
      self.Weight = weight
      self.Arm = arm
      self.Moment = self.Weight*self.Arm


   def __str__( self ):
      return "%6.1f (lbs) @ %3d (in) [%7.1f (lb-in)]"%( self.Weight, self.Arm, self.Moment )


   def __add__( self, other ):
      mule = Weight(0,0)
      mule.Weight = self.Weight + other.Weight
      mule.Moment = self.Moment + other.Moment
      if( mule.Weight ):
         mule.Arm = mule.Moment / float(mule.Weight)
      else:
         mule.Arm = 0.0
      return mule


   def __sub__( self, other ):
      mule = Weight(0,0)
      mule.Weight = self.Weight - other.Weight
      mule.Moment = self.Moment - other.Moment
      if( mule.Weight ):
         mule.Arm = mule.Moment / float(mule.Weight)
      else:
         mule.Arm = 0.0
      return mule

   def GetGC( self ):
      if( self.Moment and self.Weight):
         return self.Moment / self.Weight
      else:
         return 0.0


   def Calc( self ):
      self.Moment = self.Weight*self.Arm



class Plane():
  

   def __init__( self ):
      self.Name = ""
      self.Moments = {}
      self.Moments['Front L'] = Weight(0,0)
      self.Moments['Front R'] = Weight(0,0)
      self.Moments['Rear L']  = Weight(0,0)
      self.Moments['Rear R']  = Weight(0,0)
      self.Moments['Fuel']    = Weight(0,0)
      self.Moments['Baggage'] = Weight(0,0)
      self.Moments['Plane']   = Weight(0,0)
      self.LoadZonePoly = []
      self.UtilityZonePoly = []
      self.DepartAltitude = 5673
      self.TOGroundRoll = None
      self.TO50ftObs = None
      self.STDTemperature =  15 - 2 * self.DepartAltitude / 1000.0
      self.Temperature = self.STDTemperature

   
   def __str__( self ):
      return self.Name

   
   def Print( self ):
      print "  Name: %s"%( self.Name )
      print "Moment: %s"%( self.GetTotalMoment().__str__() )
      print "    GC: %.2f"%( self.GetTotalMoment().Arm )

  
   def PrintDetailed( self ):
      print "  Name: %s"%( self.Name )
      print "  Moments>"
      print "    Front L:",self.Moments['Front L']
      print "    Front R:",self.Moments['Front R']
      print "     Rear L:",self.Moments['Rear L']
      print "     Rear R:",self.Moments['Rear R']
      print "       Fuel:",self.Moments['Fuel']
      print "    Baggage:",self.Moments['Baggage']
      print "      Plane:",self.Moments['Plane']
      print "           ="
      print "      Total: %s"%( self.GetTotalMoment().__str__() )
      print "                   GC: %.2f (in)"%( self.GetTotalMoment().Arm )
      if( len( self.LoadZonePoly ) ):
         print "     Load Limits Good:",PointInPoly(
                                             self.GetTotalMoment().Arm,
                                             self.GetTotalMoment().Weight,
                                             self.LoadZonePoly
                                             )
      if( len( self.UtilityZonePoly ) ):
         print "  Utility Limits Good:",PointInPoly(
                                             self.GetTotalMoment().Arm,
                                             self.GetTotalMoment().Weight,
                                             self.UtilityZonePoly
                                             )
      print "        Departure Altitude:",self.DepartAltitude
      print "     Departure Temperature:",self.Temperature
      print "           STD Temperature:",self.STDTemperature
      tempAdjustment = 1+.1*( (self.Temperature - self.STDTemperature) / 13. )
      print "  TO Distances Adjusted By: %.1f%%"%( ( tempAdjustment - 1 ) * 100 )
      if( self.TOGroundRoll ):
         x = self.DepartAltitude
         print "      Take-Off Ground Roll: %s (ft)"%( Num2Str( eval( self.TOGroundRoll ) * tempAdjustment ) )
      if( self.TO50ftObs ):
         x = self.DepartAltitude
         print "    Take-Off 50ft Obstacle: %s (ft)"%( Num2Str( eval( self.TO50ftObs ) * tempAdjustment ) )

   
   def GetTotalMoment( self ):
      return sum( self.Moments.values(), Weight(0,0) )

   
   def PromptSetMoments( self ):

      print "What is your departure Altitude?"
      self.DepartAltitude = GetFloat(">",5500.0)

      print "What is the Ambient Air Temperature (in C)?"
      self.Temperature = GetFloat( ">", self.STDTemperature )
 
      print "What is your pilots weight?"
      self.Moments['Front L'].Weight = GetFloat(">",210)
      self.Moments['Front L'].Calc()
      
      print "What is your front seat passenger's weight?"
      self.Moments['Front R'].Weight = GetFloat(">",0)
      self.Moments['Front R'].Calc()
      
      print "What is your rear left passenger's weight?"
      self.Moments['Rear L'].Weight = GetFloat(">",0)
      self.Moments['Rear L'].Calc()
      
      print "What is your rear right passenger's weight?"
      self.Moments['Rear R'].Weight = GetFloat(">",0)
      self.Moments['Rear R'].Calc()
      
      print "What is your baggage weight?"
      self.Moments['Baggage'].Weight = GetFloat(">",5)
      self.Moments['Baggage'].Calc()

   
   def LoadJson( self, file ):
      with open( file ) as fp:
         data = json.load(fp)
      tmp = data['Moments']['Front L']
      self.Moments['Front L'] = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Front R']
      self.Moments['Front R'] = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Rear L']
      self.Moments['Rear L']  = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Rear R']
      self.Moments['Rear R']  = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Fuel']
      self.Moments['Fuel']    = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Baggage']
      self.Moments['Baggage'] = Weight( tmp[0], tmp[1] )
      tmp = data['Moments']['Plane']
      self.Moments['Plane']   = Weight( tmp[0], tmp[1] )
      self.LoadZonePoly = data['LoadZonePoly']
      self.UtilityZonePoly = data['UtilityZonePoly']
      self.TOGroundRoll = data['Formula']['TOGroundRoll']
      self.TO50ftObs = data['Formula']['TO50ftObs']

   def Plot( self ):
      import numpy as np
      import matplotlib.pyplot as plt
      from matplotlib.patches import Polygon
      fig = plt.figure()
      ax = fig.add_subplot(111)
      vertsLoad = np.array( self.LoadZonePoly )
      vertsUtility = np.array( self.UtilityZonePoly )
      maxes = vertsLoad.max(0)
      mins  = vertsLoad.min(0)

      ax.add_patch( Polygon( vertsLoad, facecolor='LightGreen', lw=2) )
      ax.add_patch( Polygon( vertsUtility, facecolor='LimeGreen', lw=2) )
      
      plt.plot( 
         self.GetTotalMoment().Arm, 
         self.GetTotalMoment().Weight, 
         'go',
         markersize=12 )
      
      plt.plot( 
         (self.GetTotalMoment()-self.Moments['Fuel']).Arm, 
         (self.GetTotalMoment()-self.Moments['Fuel']).Weight, 
         'ro',
         markersize=12 )

      plt.ylim([mins[1]*.9,maxes[1]*1.1])
      plt.xlim([mins[0]*.9,maxes[0]*1.1])
      plt.grid()
      plt.draw()
      plt.show()





x = Plane()

x.LoadJson("data/N13453.json")
x.PromptSetMoments()
x.PrintDetailed()
x.Plot()
