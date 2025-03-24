import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#inputting the value for the columns into x and y 
x= data[["sepal_length","sepal_width","petal_width"]]# this is what we will input in the system
y=data[["petal_length"]]                  # this is what we will get as a result from the system. from x, 
                            #we can predict the value of y which is the petal_length


#train the data
# for training the data we have to split the data. 
# 80% will be there for training the data or feeding information to the data whereas 
# the rest 20% will be to check the accuracy

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.20,random_state=42)# test_size determines 
                                                        # the amount of data used for testing or accuracy


# train the model
train= LinearRegression()   
train.fit(x_train,y_train)



#test the model
user_input= np.array([[5.4,3.4,0.4]])# the array has to be 2d and not 1d. this is why we used two brackets
final_prediction= train.predict(user_input)
print(f"Predicted petal length is :   {final_prediction}")



# accuracy level check of the model  
y_predict= train.predict(x_test)    # this predicts the value of y from the given input (the "x"values on line 10)
accuracy= r2_score(y_test,y_predict) # compares the predicted value which we got from linear regression to the actual value in the csv file.
print(f"the model accuracy is: {accuracy*100}%") # the value will be in the range of 0 to 1. we multiplied it by 100 to make it user readable and output it percentage wise.