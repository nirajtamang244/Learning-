import matplotlib.pyplot as plt
import matplotlib
import sys
import pandas as pd
import seaborn as sns
matplotlib.use("Agg")

titanic_data= {
    "age":[21,22,20,11,3,12,5,52,34,54],
    "survived":[2,1,2,0,3,6,12,23,33,1]
}

tips_data= {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23],
    "sex": ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female", "Male"]
}

data1= pd.DataFrame(titanic_data)
data2= pd.DataFrame(tips_data)

sns.histplot(x="age",data=data1,bins=10,kde=True,color= "red")
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig("histogramplot.png")
plt.show()
plt.close()

sns.scatterplot(x="total_bill",y= "tip", data=data2,hue="sex")
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig ("scatterplot.png")
plt.show()
plt.close()