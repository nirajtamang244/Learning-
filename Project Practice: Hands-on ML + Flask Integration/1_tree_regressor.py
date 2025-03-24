import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score


# read the data using pandas
data= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

x= data[["sepal_length","sepal_width","petal_width"]]
y=data[["petal_length"]]

#splitting the data into 80% training and 20% testing model
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.20,random_state=42)


# using tree regressor
prediction= DecisionTreeRegressor(random_state=42)
prediction.fit(x_train,y_train)



user_input= np.array([[5.4,3.4,0.4]])# the array has to be 2d and not 1d. this is why we used two brackets
final_prediction= prediction.predict(user_input)
print(f"preditcted petal length i is:{final_prediction}")


# check the accuracy
predicted_y= prediction.predict(x_test)
final_accuracy= r2_score(y_test, predicted_y)
print(f"the accuracy is : {final_accuracy*100}%")