import sys
import matplotlib 
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5])
y= np.array([10,20,30,40,50])

plt.plot(x,y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

plt.savefig("Lineargraph2.png")