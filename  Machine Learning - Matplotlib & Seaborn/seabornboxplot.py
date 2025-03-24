import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import matplotlib
matplotlib.use("Agg")


data1= "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

iris= pd.read_csv(data1)

plt.figure(figsize= (5,6))
sns.boxplot(x="species",y="petal_length",data=iris)

plt.title("Boxplot of Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal length")
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig("boxplot.png")
