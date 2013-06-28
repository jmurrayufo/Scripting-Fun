from __future__ import division

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



# CLASSES
class Weight():
   def __init__( self, weight, arm ):
      self.Weight = weight
      self.Arm = arm
      self.Moment = self.Weight*self.Arm

   def __str__( self ):
      return "%0.2f (lbs) @ %0.2f (in) [%0.2f (lb-in)]"%( self.Weight, self.Arm, self.Moment )

   def __add__( self, other ):
      mule = Weight(0,0)
      mule.Weight = self.Weight + other.Weight
      mule.Moment = self.Moment + other.Moment
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

class Plane():
   def __init__( self ):
      self.Name = ""
      self.Moments = {}
      self.Moments['Front L'] = Weight(0,0)
      self.Moments['Front R'] = Weight(0,0)
      self.Moments['Rear L']  = Weight(0,0)
      self.Moments['Fuel']    = Weight(0,0)
      self.Moments['Baggage'] = Weight(0,0)
      self.Moments['Plane']   = Weight(0,0)

   def __str__( self ):
      return self.Name

   def Print( self ):
      print "  Name: %s"%( self.Name )
      print "Moment: %s"%( self.GetTotalMoment().__str__() )
      print "    GC: %.2f"%( self.GetTotalMoment().Arm )

   def GetTotalMoment( self ):
      return sum(self.Moments.values(),Weight(0,0))

   def PromptSetMoments( self ):
      for i in self.Moments:
         print "  Setting Moment for: %s"%(i)
         tmpW = GetFloat("    Weight:")
         tmpA = GetFloat("       Arm:")
         self.Moments[i] = Weight(tmpW,tmpA)


x = Plane()

print x
print x.GetTotalMoment()
x.PromptSetMoments()

x.Print()


