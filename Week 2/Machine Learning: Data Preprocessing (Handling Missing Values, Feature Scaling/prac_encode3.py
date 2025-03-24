#Convert the Gender column into binary values (0 for Male, 1 for Female) using label encoding.
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'Dave', 'Emma'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Car Brand': ['Toyota', 'Honda', 'Ford', 'BMW', 'Toyota']
}

loaded_data=pd.DataFrame(data)

loaded_data["Gender_Label"]=LabelEncoder().fit_transform(loaded_data["Gender"])
print(loaded_data)


#Load a dataset containing categorical values (e.g., car brands) and apply one-hot encoding.

variable= pd.get_dummies(loaded_data,columns= ["Car Brand"], dtype=int)
print(variable)