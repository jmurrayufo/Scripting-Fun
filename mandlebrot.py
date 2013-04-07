import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def MandleImage(x,y,s,i):
   global img
   xmin, xmax = x
   ymin, ymax = y
   steps = s
   interations = i

   for idxr,r in enumerate( np.linspace( xmin, xmax, steps ) ):
      for idxi,i in enumerate( np.linspace( ymin, ymax, steps) ):
         img[ idxi, idxr ] = MandlePoint( complex(r,i), interations )




def MandlePoint(c,n):
   global interations
   z = 0
   for i in range(n):
      z = z**2 + c
      if abs(z) > 2:
        return i
   return 0

def onSize(event):
   pass
   # print ax.get_xlim()
   # print ax.get_ylim()

xmin, xmax = -2, 1
ymin, ymax = -1, 1
steps = 1000
interations = 30

image = np.ndarray( (steps,steps), dtype= np.uint16 )

for idxr,r in enumerate( np.linspace( xmin, xmax, steps ) ):
   for idxi,i in enumerate( np.linspace( ymin, ymax, steps) ):
      image[ idxi, idxr ] = MandlePoint( complex(r,i), interations )


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

cid = fig.canvas.mpl_connect('draw_event', onSize)
img = plt.imshow( image, origin = 'lower' )


plt.show()
print "fin"


