import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use("Agg")
x= np.array([12,13,15,20,22])
y= np.array([4,10,12,19,20])
plt.subplot(3,1,1)
plt.plot(x,y,color="red",marker="o",linestyle="dashed")

x= np.array([5,10,15,20,25])
y= np.array([11,18,19,20,30])
plt.subplot(3,1,2)
plt.bar(x,y,color="yellow", linestyle="dotted", linewidth= 0.5)


x= np.array([12,15,20,21,32])
y= np.array([11,13,15,19,20])
plt.subplot(3,1,3)
plt.scatter(x,y)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig("subdplot.png")