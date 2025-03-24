import pandas as pd


#loading the data from the csv file
readData= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv")

#counting the missing values before any action
print(f"The number of rows with na before any action  is: {readData.isnull().sum()}")


#dropping the row with na
cleanedData= readData.dropna()
print(cleanedData)

# counting the missing values after the na row is removed.
print(f"The number of rows with na after using 'dropna' is: {cleanedData.isnull().sum()}")


#filling the column "age" which has na with median of the data in the column
readData["age"] = readData["age"].fillna(readData["age"].median())
print(readData)
print(f"The number of rows with na after using fillna is: {readData.isnull().sum()}")
