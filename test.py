import itertools
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

procs = [1,2,5,10,20,50]
targets = [1,2,4,8,16,32,64,128,256]

xData = list()
yData = list()
zData = list()

for p,t in itertools.product(procs,targets):
    xData.append(p)
    yData.append(t)
    zData.append(p*t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xData,yData,zData)
plt.show()