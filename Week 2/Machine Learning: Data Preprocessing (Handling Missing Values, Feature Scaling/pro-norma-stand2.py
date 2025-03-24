import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample dataset
df = pd.DataFrame({
    'Salary': [30000, 50000, 75000, 100000, 150000],  # To normalize
    'Age': [22, 25, 30, 35, 40],  # To standardize
    'Experience': [1, 3, 5, 7, 10]  # To standardize
})


df["Salary_normal"]= MinMaxScaler().fit_transform(df[["Salary"]])

df[["Age_Standard","Experience_Standard"]]= StandardScaler().fit_transform(df[["Age","Experience"]])

print(df)