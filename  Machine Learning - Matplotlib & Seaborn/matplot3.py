import numpy as np
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 5))

# First subplot - Line graph
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), 'r', label="Sine Wave")
plt.title("Sine Function")
plt.legend()

# Second subplot - Scatter plot
plt.subplot(1, 2, 2)
plt.scatter(x, np.cos(x), color='blue', label="Cosine Wave")
plt.title("Cosine Function")
plt.legend()
plt.show()




plt.savefig("advancedSubpldot.png")