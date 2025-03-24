import sys
import matplotlib 
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

x= np.array(["nepal","india","pakistan","bangladesh","USA"])
y= np.array([123123,4343434,343243,324342,2343243])

plt.bar(x,y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig("Barchart.png")
