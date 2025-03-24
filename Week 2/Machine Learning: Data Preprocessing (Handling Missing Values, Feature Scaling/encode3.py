import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

df = pd.DataFrame({'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']})


df["city_label"]= LabelEncoder().fit_transform(df["City"])

print(df)


variable= pd.get_dummies(df, columns= ["City"],dtype= int)
print(variable)